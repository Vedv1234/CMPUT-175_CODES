# Author: Ved Vyas
# Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
# Resources used: Based on code from https://github.com/kressi/terminalplot/blob/master/terminalplot/terminalplot.py
# Functionality of code: This is my terminal-based plotting utility that I use to visualize data directly 
# in the command line. It's particularly useful for showing the performance comparisons between my 
# different queue implementations. I've modified the original code to support multiple plots and added 
# my own customizations for better visualization.

import os
import struct

def plot_multiple(x1, y1, y2, rows=None, columns=None):
    '''
    My function to plot two sets of data points with different markers
    '*' for first dataset, '#' for second dataset
    '''
    # Getting terminal dimensions if not specified
    if not rows or not columns:
        rows, columns = get_terminal_size()
    
    # Adding some padding for labels
    arows = rows + 2
    acols = columns + 4
    rows -= 4  # Making space for the caption
    
    # Scaling my points to fit the terminal
    x_scaled = xscale(x1, columns)
    y1_scaled, y2_scaled = yscale(y1, y2, rows)
    
    # Creating my empty canvas
    canvas = [[' ' for _ in range(columns)] for _ in range(rows)]
    
    # Plotting first dataset with '*'
    for ix, iy in zip(x_scaled, y1_scaled):
        canvas[rows - iy - 1][ix] = '*'
    
    # Plotting second dataset with '#' or '+' if points overlap
    for ix, iy in zip(x_scaled, y2_scaled):
        if canvas[rows - iy - 1][ix] == '*':
            canvas[rows - iy - 1][ix] = '#'
        else:
            canvas[rows - iy - 1][ix] = '+'
    
    # Displaying my plot
    for row in [''.join(row) for row in canvas]:
        print(row)
    
    # Adding scale information at the bottom
    print(''.join([
        '\nMin x: ', str(min(x1)),
        ' Max x: ', str(max(x1)),
        ' Min y: ', str(min(min(y1), min(y2))),
        ' Max y: ', str(max(max(y1), max(y2)))
    ]))

def plot2(x, y1, y2, rows=None, columns=None):
    '''
    My simplified version of the plotting function
    '''
    if not rows or not columns:
        rows, columns = get_terminal_size()
    
    rows -= 4  # Space for caption
    
    # Scaling points to fit my display
    x_scaled = scale(x, columns)
    y1_scaled, y2_scaled = yscale(y1, y2, rows)
    
    # Creating empty canvas
    canvas = [[' ' for _ in range(columns)] for _ in range(rows)]
    
    # Plotting both datasets
    for ix, iy in zip(x_scaled, y1_scaled):
        canvas[rows - iy - 1][ix] = '*'
    
    for ix, iy in zip(x_scaled, y2_scaled):
        if canvas[rows - iy - 1][ix] == '*':
            canvas[rows - iy - 1][ix] = '+'
        else:
            canvas[rows - iy - 1][ix] = '#'
    
    # Displaying the plot
    for row in [''.join(row) for row in canvas]:
        print(row)
    
    # Adding scale information
    print(''.join([
        '\nMin x: ', str(min(x)),
        ' Max x: ', str(max(x)),
        ' Min y: ', str(min(min(y1), min(y2))),
        ' Max y: ', str(max(max(y1), max(y2)))
    ]))

def scale(x, length):
    '''
    My helper function to scale values to fit the display width
    '''
    s = float(length - 1) / \
        (max(x) - min(x)) if x and max(x) - min(x) != 0 else length
    return [int((i - min(x)) * s) for i in x]

def xscale(x, length):
    '''
    Similar to scale() but specifically for x-axis values
    '''
    s = float(length - 1) / \
        (max(x) - min(x)) if x and max(x) - min(x) != 0 else length
    return [int((i - min(x)) * s) for i in x]

def yscale(y1, y2, length):
    '''
    My scaling function for y-values, handles two datasets
    '''
    max_ = max(max(y1), max(y2))
    min_ = min(min(y1), min(y2))
    s = float(length - 1) / \
        (max_ - min_) if (y1 or y2) and max_ - min_ != 0 else length
    return [int((i - min_) * s) for i in y1], [int((i - min_) * s) for i in y2]

def get_terminal_size():
    '''
    Gets my terminal dimensions in a cross-platform way
    '''
    try:
        with open(os.ctermid(), 'r') as fd:
            rc = struct.unpack(
                'hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
    except:
        # Fallback to environment variables if can't get terminal size
        rc = (os.getenv('LINES', 25), os.getenv('COLUMNS', 80))
    
    return rc

if __name__ == '__main__':
    # Example usage if run directly
    plot_multiple2(x, y1, y2)