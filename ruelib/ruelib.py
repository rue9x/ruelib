import os
import sys
import time
from datetime import datetime
import csv
import json
import threading
from queue import Queue
import base64

class Worker(threading.Thread):
    '''
    Used with ThreadPool. Don't muck with it on its own.
    '''
    def __init__(self, queue):
        super(Worker, self).__init__()
        self.q = queue
        self.daemon = True
        self.start()

    def run(self):
        while True:
            f, args, kwargs = self.q.get()
            try:
                f(*args, **kwargs)
            except Exception as e:
                print(e)
            self.q.task_done()

class ThreadPool(object):
    '''
    Used for basic threading of functions.
    Use with poolvar = ThreadPool(number_of_threads), poolvar.add_task(function_name, args if any), pool.wait_complete()

    '''
    def __init__(self, thread_num=10):
        self.q = Queue(thread_num)
        for i in range(thread_num):
            Worker(self.q)

    def add_task(self, f, *args, **kwargs):
        self.q.put((f, args, kwargs))

    def wait_complete(self):
        self.q.join()

def tob64(s):
    ''' 
    Converts text string into base64
    '''
    return base64.b64encode(s.encode()).decode()


def fromb64(s):
    '''
    Converts base64 string into decoded text
    '''
    return base64.b64decode(s).decode()

def timestamp():
    '''
    Returns a simple, easy to read timestamp. Military time.
    '''
    a = datetime.now()
    return str(a)

def logprint(fn="log.txt",msg='',ts=False,prepend=True):
    '''
    Great for manually logging text.
    ts controls if you want a timestamp added.
    prepend controls if you want to prepend to the file (or, False for a standard append)
    '''
    if ts == True:
        timestampx = timestamp()
        timestampx = timestampx + ": "
        msg = timestampx+msg
    
    if os.path.exists(fn):
        if prepend == True:
            with open(fn, 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                f.write(msg.rstrip('\r\n') + '\n' + content)
        else:
            with open (fn,'a') as f:
                f.write(msg)
                f.write("\n")    
    else:
        with open (fn,'a') as f:
            f.write(msg)
            f.write("\n")    

def merge_dicts(*dicts):
    ''' 
    Merge two dictionaries.
    '''
    super_dict = {}
    for dict in dicts:
        for k, v in dict.items():
            super_dict[k] = v

    return super_dict

def remove_duplicates(val=list()):
    ''' 
    Removes duplicates from a list.
    '''
    retval = list(set(list(val)))
    return retval

def is_palindrome(string):
    '''
    Returns if a string is a palindrome or not. 
    Sick of this showing up on job interviews, ahaha. :)
    '''
    reversed_string = string[::-1]
    return string == reversed_string

def parse_csv_as_listdict(csv_path):
    ''' 
    Takes a csv file. Returns a list, each row being a dictionary containing the data for each row (key as the header, value as the cell data).
    '''
    csv_mapping_list = []
    with open(csv_path) as my_data:
       csv_reader = csv.reader(my_data, delimiter=",")
       line_count = 0
       for line in csv_reader:
           if line_count == 0:
               header = line
           else:
               row_dict = {key: value for key, value in zip(header, line)}
               csv_mapping_list.append(row_dict)
           line_count += 1 
    return csv_mapping_list

def write_json_to_file(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4) 

def read_json_from_file(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return data 
