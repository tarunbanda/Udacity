"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint
from types import NoneType
from datetime import date, datetime
import dateutil.parser

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):

    goodRows = []
    badRows = []
    
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        for row in reader:
            if "dbpedia.org" in row['URI']:
                if row["productionStartYear"] != 'NULL':
                    d_time = row["productionStartYear"].split('-')[0]
                    try:
                        if 1886 <= int(d_time) <= 2014:
                            row["productionStartYear"] = d_time
                            goodRows.append(row)
                    except:
                        badRows.append(row)
                else:
                    badRows.append(row)
                    
    write_to_csv(OUTPUT_GOOD, goodRows, header)
    write_to_csv(OUTPUT_BAD, badRows, header)
            
def write_to_csv(filename, array, header):
    #     This is just an example on how you can use csv.DictWriter
#     Remember that you have to output 2 files
    with open(filename, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in array:
            writer.writerow(row) 
    g.close()



def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()