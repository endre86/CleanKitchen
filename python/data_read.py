import serial
import time


class CsvSerialReader:
    """
    Used to read CSV data from serial port using serial.Serial.
    Expecting each line to be some comma seperated values, where
    the first value is a millisecond timestamp.

    Both bytes and str is accepted values from serial device.
    (So we can use the same code on Windows and Linux with Arduino-)
    """

    def __init__(self, port, baudrate=9600, timeout=2, byte_encoding='utf-8'):
        """
        port:
            Port to read from.
        baudrate:
            Baudrate to read in.
        timeout:
            Used to terminate reading if no data is read
            within the timeout limit.
        byte_encoding:
            If serial device values are returned as bytes,
            the byte_encoding will be used to decode the values.
        """
        self.serial = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        self._byte_encoding = byte_encoding

    def read(self, max_read_time=-1):
        """
        Returns list of read values up to a specific time length or
        the initial timeout has occured. Before read is started, all old
        data is flushed.

        max_read_time:
            Maximum length the read should last. Use negative number (default) 
            to ignore this feature.

        returns:
            List of tuples of read data where each tuple value is
            an comma seperated value.
        """
        result = []
        start = time.time()

        read_data = ""
        read_data_tuple = ()

        try:
            while True:
                if max_read_time > 0 and (time.time() - start) > max_read_time:
                    break

                read_data = self.serial.readline()
                
                if len(read_data) == 0:
                    break
                
                read_data_tuple = self._transform_read_data(read_data)

                result.append(read_data_tuple) 
        except KeyboardInterrupt:
            raise
        except Exception as ex:
            print("Caught and supressing exception:", ex)
        
        return result

    def flush(self):
        """
        Flushed the Serial readers input buffer
        """
        self._serial_reader.flushInput()

    def _transform_read_data(self, read_data):
        if type(read_data) == bytes:
            read_data = read_data.decode(self._byte_encoding)

        return tuple(filter(None, read_data.replace('\r\n', '').split(',')))