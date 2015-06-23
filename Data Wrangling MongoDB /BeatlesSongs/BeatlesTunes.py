'''
Created on Jun 13, 2015

@author: tbanda
'''
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
    headers = ['Title', 'Released', 'Label', 'UK Chart Position', 'US Chart Position', 'BPI Certification', 'RIAA Certification']
    dataArray = []
    with open(datafile, "r") as f:
        next(f)
        for x, line in enumerate(f):
            if x < 10:
                my_dict = {}
                line = line.strip()
                new_line =  line.split(',')
    #             print new_line
                for i in range(len(new_line)):
                    if new_line[i] == '\xe2\x80\x94':
                        my_dict[headers[i]] = "-"
                    else:
                        my_dict[headers[i]] = new_line[i]
                dataArray.append(my_dict)
                print my_dict
                
        return dataArray
        

def main():
    d = parse_file(DATAFILE)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    
    if d[0] ==firstline:
        print "True"
    else:
        print "False"

if __name__ == '__main__':
    main()