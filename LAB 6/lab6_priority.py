# Author: Ved Vyas
# Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
# Functionality of code: This is my implementation of a priority queue system that simulates how 
# an operating system might handle different types of processes. I've created a system where 
# high-priority OS tasks take precedence over low-priority user tasks, similar to how real 
# operating systems work.

import random
from queues import CircularQueue

class Job:
    def __init__(self, priority = 0, process_name = None):
        '''
        I'm creating job objects with different priorities and names
        '''
        # Giving each job a random ID between 1 and 1000
        self.__id = random.randint(1,1000)
        self.__priority = priority
        
        # If no process name is given, I'll assign one based on priority
        if process_name is None:
            if self.high_priority():
                # High priority jobs are OS-related
                self.__process_name = random.choice(['[OS] File Write', '[OS] File Read', '[OS] Display'])
            else:
                # Low priority jobs are user applications
                self.__process_name = random.choice(['[USER] Browser', '[USER] Music', '[USER] Calculator'])
    
    def high_priority(self):
        '''
        Quick check if this is a high priority job
        '''
        return self.__priority == 1
    
    def process_name(self):
        '''
        Getter for my process name
        '''
        return self.__process_name
    
    def __str__(self):
        # Nice formatted string representation of my job
        return '{:<15} : {:<20}\n{:<15} : {:<20}\n{:<15} : {:<20}'.format(
            'ID', self.__id,
            'Process Name', self.__process_name,
            'Priority', 'HIGH' if self.__priority == 1 else 'LOW'
        )

def get_job():
    '''
    This is my job generator - it creates new jobs with different probabilities
    '''
    # 50% chance of high priority job
    if random.random() < .5:
        return Job(priority=1)
    # 40% chance of low priority job
    if random.random() < .9:
        return Job(priority=0)
    # 10% chance of no job
    return None

def process_complete():
    '''
    I'm simulating whether a process has finished running
    '''
    # 50-50 chance of process completion
    return random.random() < 0.5

def main():
    # Setting up my initial system state
    process_running = False  # No process running at start
    current_job = None
    # Creating my priority queues
    high_priority_queue = CircularQueue(1000)
    low_priority_queue = CircularQueue(1000)
    
    # Running my simulation for 10 time steps
    time_steps = 10
    for t in range(time_steps):
        print("######## RUN : {} ########\n".format(t + 1))
        
        # Getting a new job (if any)
        job = get_job()
        if job:
            print("Job {} generated\n".format(job.process_name()))
        
        # Adding the job to appropriate queue based on priority
        if job and job.high_priority():
            high_priority_queue.enqueue(job)
        elif job:
            low_priority_queue.enqueue(job)
        
        # Checking if current job is done
        if process_running:
            current_process_status = process_complete()
            if current_process_status:
                process_running = False
                print("JOB COMPLETED\n{}".format(current_job))
                current_job = None
        
        # If no job is running, I'll start a new one
        # High priority jobs always get processed first
        if not process_running:
            if not high_priority_queue.isEmpty():
                current_job = high_priority_queue.dequeue()
                process_running = True
            elif not low_priority_queue.isEmpty():
                current_job = low_priority_queue.dequeue()
                process_running = True
        
        # Showing current processor status
        if not process_running:
            print("\n[PROCESSOR] Idle")
        else:
            print("\n[PROCESSOR] Busy")
        
        # Displaying queue status
        print("Jobs waiting in High Priority Queue :{}".format(high_priority_queue.size()))
        print("Jobs waiting in Low Priority Queue :{}\n".format(low_priority_queue.size()))

if __name__ == '__main__':
    main()