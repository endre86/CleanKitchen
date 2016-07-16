
import functools

def standarize_ms(datas, val_index, max=(2^32 - 1)):
    """
    Standarize milliseconds lapsed from Arduino reading.
    Note: Only takes height for one circulation of ms from Arduino.

    datas: 
        List of data readings
    val_index:
        Index of ms value in reading data entry
    max:
        Max time of ms - since the Arduino will output
        a circular value from the time it starts.
        For correct value, see https://www.arduino.cc/en/Reference/Millis.
    """
    def _standarize_value(initial_value, reading):
        reading[val_index] = int(reading[val_index]) - initial_value;
        if(reading[val_index] <= 0):
            reading[val_index] += max
        return reading

    initial_value = int(datas[0][val_index])
    ___standarize_value = functools.partial(_standarize_value, initial_value=initial_value)

    res = map(lambda x: _standarize_value(initial_value, x), datas)
    res = list(res)
    res[0][val_index] = 0
