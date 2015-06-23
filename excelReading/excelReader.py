'''
Created on Jun 13, 2015

@author: tbanda
'''
#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from xlrd import xldate
# from zipfile import ZipFile
import sys
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


# def open_zip(datafile):
#     with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
#         myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    
    maxtime = 0
    maxvalue = 0
    minvalue = sys.maxint
    mintime = sys.maxint
    total = 0
    

    for row in range(sheet.nrows):
            if sheet.cell_type(row, 1) == 2:
                total += sheet.cell_value(row, 1)
                if sheet.cell_value(row, 1) > maxvalue:
                    maxvalue = sheet.cell_value(row, 1)
                    maxtime = sheet.cell_value(row, 0)
                if sheet.cell_value(row, 1) < minvalue:
                    minvalue = sheet.cell_value(row, 1)
                    mintime = sheet.cell_value(row, 0)


    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }
    
    data['maxtime'] = xlrd.xldate_as_tuple(maxtime, 0)
    data['maxvalue'] = maxvalue
    data['mintime'] = xlrd.xldate_as_tuple(mintime, 0)
    data['minvalue'] = minvalue
    data['avgcoast'] = total/(sheet.nrows-1)
    return data


def test():
#     open_zip(datafile)
    data = parse_file(datafile)
    print data.items()

#     assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
#     assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()