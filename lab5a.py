#!/usr/bin/env python3
# Author ID: rfrancisco6

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')    # open in read mode
    contents = f.read()         # read file
    f.close()                   
    return contents             # returnn string

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')    # open in read mode
    listline = f.readlines()    # make list
    f.close()

    # remove new line chars
    clean_lines = []            # create eempty list
    for listline in listline:   # loop
        clean_lines.append(listline.strip())    # remove whitespace
    return clean_lines          # return clean

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))