import os
import sys
import time

from datetime import date


class FileCsvDataWriter:
    """
    Used to write CSV data to a file. The file is
    automatically named as todays date and given
    the type csv.
    """
    def __init__(self, path):
        """
        path:
            Path to file, a new file is created if no file
            matches path/todaysdate.csv.
        """
        self._path = path

        self._open_file_writer()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close_file()

    def __del__(self):
        self._close_file()

    def write_csv_lines(self, csv_data_list):
        """
        Writes list (iterable structure) of csv data with each item as single
        line using write_csv_line.
        """
        for csv_data in csv_data_list:
            self.write_csv_line(csv_data)

    def write_csv_line(self, csv_data):
        """
        Write data as line to file

        csv_data:
            Data to write. Accept tuple or str.

        raise:
            TypeError if csv_data is not of type str or tuple
            Errors from file.
        """
        if type(tuple_data) == tuple:
            str_data = str(tuple_data)
        elif type(tuple_data) == str:
            str_data = tuple_data
        else:
            raise TypeError('Only accepting tuple_data as str or tuple')

        if self._file_writer.closed:
            self._open_file_writer()
        
        self._file_writer.println(str_data)

    def _open_file_writer(self):
        if self._path[-1] != os.pathsep:
            self._path = self._path + os.pathsep
        
        file = self._path + str(date.today()) + '.csv'
        self._file_writer = open(file=file, mode='a', encoding='utf-8')

    def _close_file(self):
        try:
            if self._file_writer.closed:
                self._file_writer.close()
        except:
            raise
            print("Unexpected error:", sys.exc_info())