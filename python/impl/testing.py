import os
import time

import data_gathering

from data_read import CsvSerialReader
from data_write import FileCsvDataWriter


###########################################

port = 'COM4'	            # port to listen to (wrk: COM4, priv: COM3, rpi: /dev/ttyUSB0)
timeout = 2                 # empty data read timeout
read_timeout = 3            # non-empty data read timeout 
path = os.path.join(        # path to test data
        os.path.dirname(
        	os.path.dirname(os.path.abspath(__file__))), 'data')

###########################################


def test_reading_and_writing(execution_time_seconds = 10):
    start_time = time.time()
    with CsvSerialReader(port, timeout=timeout) as reader, \
         FileCsvDataWriter(path) as writer:

        while time.time() - start_time < execution_time_seconds:
            read_values = reader.read(read_timeout)
            writer.write_csv_lines(read_values)

def test_data_gathering():
    # def identifier_generator():
    #     i = 0
    #     while True:
    #         yield i
    #         i = i + 1

    data_gathering.run(port, path, timeout, read_timeout)

if __name__ == '__main__':
    print('START')
    # test_reading_and_writing()
    test_data_gathering()
    print('EXIT')
else:
    raise SystemExit('testing.py is only a scriptfile used for testing purposes')