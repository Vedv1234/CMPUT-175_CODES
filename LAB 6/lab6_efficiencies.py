# Author: Ved Vyas
# Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
# Functionality of code: In this code, I'm comparing the performance differences between Bounded and 
# Circular queues by conducting experiments on dequeue operations. I'm measuring execution times for 
# different queue sizes and visualizing the results using terminal plots. This helps me understand 
# how queue implementations affect performance in real-world scenarios.

import random  # I need this for generating random numbers for my queue elements
import time    # I'll use this to measure execution time of my operations
from queues import BoundedQueue   # Importing my queue implementations
from queues import CircularQueue  
from decimal import Decimal       # This helps me format my scientific notation nicely
from terminalplot import plot2    # I'm using this for creating visual plots in the terminal

def enqueue_experiment(queue_class, queue_size):
    '''
    I created this function to fill up queues with random values for testing
    '''
    # Creating a new queue object of whatever type I specified
    queue = queue_class(queue_size)
    
    # I'm adding random values until the queue is completely full
    while not queue.isFull():
        value = random.random()
        queue.enqueue(value)
    
    return queue

def dequeue_experiment(queue):
    '''
    This is where I measure how long it takes to empty a queue
    '''
    # Recording my start time before dequeuing
    start_time = time.time()
    
    # I'm removing everything from the queue and timing it
    while not queue.isEmpty():
        queue.dequeue()
    
    # Calculating how long it took
    end_time = time.time()
    time_interval = end_time - start_time
    
    return time_interval

def avg_dequeue_experiment(queue_class, size, sample_size = 5):
    '''
    I'm running multiple dequeue tests and averaging them for more accurate results
    '''
    q_run_avg = 0
    # Running the experiment multiple times to get a good average
    for i in range(sample_size):
        queue = enqueue_experiment(queue_class, size)
        q_run_avg += dequeue_experiment(queue)
    
    return float(q_run_avg)/sample_size

def main():
    # These are my test queue sizes - I picked sizes that would show clear differences
    queues_sizes = [10000, 30000, 50000, 70000, 90000, 100000]
    
    # Setting up my experiment with both queue types
    bqueues = []
    cqueues = []
    for q in queues_sizes:
        bq = enqueue_experiment(BoundedQueue, q)
        cq = enqueue_experiment(CircularQueue, q)
        bqueues.append(bq)
        cqueues.append(cq)
    
    # Running my dequeue tests on both queue types
    bounded_queue_times = [dequeue_experiment(q) for q in bqueues]
    circular_queue_times = [dequeue_experiment(q) for q in cqueues]
    
    # Creating a nice formatted table to show my results
    print("Times for Bounded and Circular Queue without using Average")
    line = '-'*(13 + 14*len(queues_sizes))
    line2 = str('-'*13 + '+')*(1 + len(queues_sizes))
    print(line)
    print(str(" Queue Size  | " + ' '.join(" {:<10} |".format(q) for q in queues_sizes)))
    print(line2)
    print(str(" B que Time  | " + ' '.join(" {:<10} |".format(('%.2E' % Decimal(str(q)))[:10]) for q in bounded_queue_times)))
    print(line2)
    print(str(" C que Time  | " + ' '.join(" {:<10} |".format(('%.2E' % Decimal(str(q)))[:10]) for q in circular_queue_times)))
    print(line)
    
    # Trying to create a visual plot of my results
    try:
        print('''
        Legend : 
        '*' : Points of the Bounded Queue
        '#' : Points of Circular Queue
        '+' : Points where both coincide''')
        
        plot2(queues_sizes, bounded_queue_times, circular_queue_times)
    except:
        print("Not able to print graph. Continuing .....")
    
    # Now I'm running the same experiment but with averaging for more accurate results
    avg_b_queue_times = [avg_dequeue_experiment(BoundedQueue, size) for size in queues_sizes]
    avg_c_queue_times = [avg_dequeue_experiment(CircularQueue, size) for size in queues_sizes]
    
    # Displaying my averaged results
    print("Times for Bounded and Circular Queue with Averaging")
    print(line)
    print(str(" Queue Size  | " + ' '.join(" {:<10} |".format(q) for q in queues_sizes)))
    print(line2)
    print(str(" B que Time  | " + ' '.join(" {:<10} |".format(('%.2E' % Decimal(str(q)))[:10]) for q in avg_b_queue_times)))
    print(line2)
    print(str(" C que Time  | " + ' '.join(" {:<10} |".format(('%.2E' % Decimal(str(q)))[:10]) for q in avg_c_queue_times)))
    print(line)
    
    # Trying to plot my averaged results
    try:
        print('''
        Legend : 
        '*' : Points of the Bounded Queue
        '#' : Points of Circular Queue
        '+' : Points where both coincide''')
        
        plot2(queues_sizes, avg_b_queue_times, avg_c_queue_times)
    except:
        print("Not able to print graph. Continuing .....")

if __name__ == '__main__':
    # I'm tracking how long my whole program takes to run
    start = time.time()
    main()
    end = time.time()
    print("The program took {} seconds to run".format(end - start))