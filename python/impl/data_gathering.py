
import itertools
import functools
import sys
import types

from datetime import datetime

from data_read import CsvSerialReader
from data_write import FileCsvDataWriter


def run(port, path, timeout, max_read_time, identifier_generator=None):
    """
    Run console data gathering.

    port:
        Port to read from
    path:
        Path to put data file
    timeout:
        Timeout on read when not receiving any data
    max_read_time:
        Max time for single read
    identifier_generator:
        Generator for creating identifiers for reads. Must be 
        initialized (ie type() == 'generator')
        Defaults to datetime.now
    """
    _print_info()
    if(isinstance(identifier_generator, types.GeneratorType)):
        ident_gen = identifier_generator
        print('tes!')
    else:
        print(type(identifier_generator))
        ident_gen = _default_generator()

    with CsvSerialReader(port, timeout=timeout) as reader, \
         FileCsvDataWriter(path) as writer:

        label = 'NA'
        while True:
            curr_label = input('Enter label (empty to use previous)')

            if curr_label == 'exit':
                break # exit 

            if(len(curr_label) > 0):
                label = curr_label

            identifier = str(next(ident_gen))

            _record_read(reader, writer, max_read_time, identifier, label)

def add_metadata(identifier, label, data):
    """
    Used to add identifier and label to data tuple.
    Label is always cast to str and uppercased.

    data:
        Read data.
    identifier:
        The unique identifier used to identify data sets
    label:
        Label  
    """
    label = str(label).upper()
    return [identifier, label] + data 

def _record_read(reader, writer, max_read_time, identifier, label):
    read_data = reader.read(max_read_time)
    process = functools.partial(add_metadata, identifier, label)
    read_data = map(process, read_data)
    writer.write_csv_lines(read_data)

def _print_info():
    print('Starting data gathering.')
    print('For each unique value gathered, there is added an id to ')
    print('each row of data to identify and group reads.')
    print('In addition, before each read, you will be asked to input some lable')
    print('to label the dataset with (ie: "knif").')
    print('Exit writing "exit" (in lower case) as label.')

def _default_generator():
    while True:
        yield datetime.now()