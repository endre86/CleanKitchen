
import functools

from datetime import datetime

from data_read import CsvSerialReader
from data_write import FileCsvDataWriter


def run(port, path, timeout, max_read_time):
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
    """
    _print_info()

    with CsvSerialReader(port, timeout=timeout) as reader, \
         FileCsvDataWriter(path) as writer:

        label = 'na' 
        while True:
            curr_label = input('Enter label (empty to use previous)')
            if(len(curr_label) > 0):
                label = curr_label

            _record_read(reader, writer, max_read_time, str(datetime.now()), label)


def add_metadata(identifier, label, data):
    """
    Used to add identifier and label to data tuple

    data:
        Read data.
    identifier:
        The unique identifier used to identify data sets
    label:
        Label  
    """
    return (identifier,) + data + (label,) 

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
    print('Exit using keyboard interruption (ctrl+z).')