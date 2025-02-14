#!/usr/bin/env python3
# Author ID: rfrancisco6

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        if isinstance(number1, str):    # check first
            number1 = int(number1)      # convert
        if isinstance(number2, str):    # check second
            number2 = int(number2)      # convert
        return number1 + number2        #return sum
    except:
        return "error: could not add numbers" # return err msg

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        f = open(filename, 'r')         
        lines = f.readlines()
        f.close()
        return lines
    except:
        return "error: could not read file"

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception