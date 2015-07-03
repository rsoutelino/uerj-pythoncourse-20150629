import pandas as pd

filename = 'currents.csv'

def parse_dates(datestr): 
    return dt.datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S")


df  = pd.read_csv(filename, sep='\t', 
                       parse_dates=1, 
                       date_parser=parse_dates, index_col=['Time'])