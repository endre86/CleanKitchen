import os
import time

from data_read import CsvSerialReader
from data_write import FileCsvDataWriter


def test_reading_and_writing(port, path, execution_time_ms):
    start_time = time.time()
    with CsvSerialReader(port, timeout=2) as reader, \
         FileCsvDataWriter(path) as writer:

        while time.time() - start_time < execution_time_ms:
            print('reading values')
            read_values = reader.read(3)
            print('got valuse:', read_values)
            writer.write_csv_lines(read_values)
            print('wrote values to file')
    

if __name__ == '__main__':
    path, filename = os.path.split(os.path.abspath(__file__))
    path = os.path.join(path, 'testdata')
    test_reading_and_writing('COM4', path, 30000)
    print("EXIT")
else:
    raise SystemExit('testing.py is only a scriptfile used for testing purposes')