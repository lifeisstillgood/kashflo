

"""
given a hdr and a tgthdr, map one to other

"""

import pprint

### Map tgthdrs and what "makes" the header from src
hdrmap_cc = {"Date": ["Date"],
          "Type": [],
          "Description":["Transactions", "Location"],
          "out": ["Paid out"],
          "in": ["Paid in"],
          "Balance": []
         }

hdrmap_bcard = {"Date":["Date"],
                "Type":["Person"],
                "Description":["Description", "unknown"],
                "out":["debit"],
                "in":["credit"],
                "Balance":[]
                }

hdrmap_pers = {"Date":["Date",],
                "Type":["Transaction type",],
                "Description":["Description",],
                "out":["Paid out",],
                "in":["Paid in",],
                "Balance":["Balance",]
                }

import csv
import os

hdr_order=["Date", "Type", "Description", "out", "in", "Balance"]



def rewritecsv(f, hdrmap):
    """Given a csv file with a fixed order, rewrite it to the new col order """

    rdr = csv.DictReader(open(f))
    newrdr = []
    for row in rdr:
        newrow = {}
        for hdr in hdrmap:
            s = ''
            for rowhdr in hdrmap[hdr]:
                s += row[rowhdr]
            newrow[hdr] = s
        newrdr.append(newrow)

    ncsv = open("adjusted_"+f, "w")
    dwriter = csv.DictWriter(ncsv, hdr_order, dialect="excel", quoting=csv.QUOTE_ALL)
    for row in newrdr:
        dwriter.writerow(row)
    ncsv.close()



annafiles = ['anna_nwcc_2012-02.csv', 'anna_bcard_2012-11.csv', 'anna_nwcc_2012-07.csv', 'anna_nwcc_2012-03.csv', 'anna_nwcc_2012-08.csv', 'anna_nwcc_2012-05.csv', 'anna_bcard_2012-10.csv', 'anna_nwcc_2012-04.csv', 'anna_bcard_2012-09.csv', 'anna_bcard_2012-08.csv', 'anna_nwcc_2012-10.csv',  'anna_pers_2011.csv', 'anna_nwcc_2012-06.csv', 'anna_bcard_2012-07.csv', 'anna_nwcc_2012-09.csv', 'anna_bcard_2012-06.csv']

for f in annafiles:
    print f,
    if f.find("pers") != -1:
        rewritecsv(f, hdrmap_pers)
    if f.find("nwcc") != -1:
        rewritecsv(f, hdrmap_cc) 
    if f.find("bcard") != -1:
        rewritecsv(f, hdrmap_bcard) 
    print "done"
