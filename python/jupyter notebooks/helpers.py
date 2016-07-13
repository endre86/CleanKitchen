import csv

def read_raw_data(filename):
    """
    Reads raw data from filename and returns it as 
    list of lists.

    filename:
        File to read from.

    returns:
        list of lists of data, where each sub list is
        is a row, and each sub list item is a row value
    """
    with open(filename, 'r') as raw_data_file:
        raw_data_reader = csv.reader(raw_data_file)
        raw_data = list(raw_data_reader)
        return raw_data

def split_data_based_on_readings(raw_data):
    """
    Splits the data into unique readings.

    raw_data: 
        List of list of data where index 0 
        is the unique identifier

    returns:
        dictionary of lists of lists,
        where each dictionary entry is a unique 
        reading.
    """
    result = {}
    for x in raw_data:
        if x[0] in result:
            result[x[0]].append(x)
        else:
            result[x[0]] = [x]
    return result