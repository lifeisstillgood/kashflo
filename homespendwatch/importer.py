#!/usr/local/env python
#! -*- coding: utf-8 -*-

"""
Importer collection of features
===============================

(cos its not really a program, a library or anything much more than a
mess)



Aim: to allow me to download csv files from Bank(s)
     import files as transactions into a dbase 
     categorise the trasnactions using simple string matches
     and then see how much we spend in each category


1. Obtain csv files, usually for longest period possible.

2. Ensure they are in format below

    hdr = ["Date","Type","Description","out","in","Balance"]

3. either create a new database

  python importer.py init -

4. or just load another file into the existing dbase

  python importer.py load bank.csv

5. Categorise using current matching

   python importer.py match -

6. See how well matched a given workd works 

   python importer.py test starbucks Costa

7. See how we are doing

   python importer.py summary

   Actually run run.sh and see this from web)








#Summary, Category, search term

["utilities", "British Gas", "gas"].

python importer.py <action>

Action is 
    
   init - initdb() - creates table in /tmp/money.db


* matching txt in sep file
* output into HTML


python importer init <file.csv>


Issues:

* TO and FROM dates to be more sane

"""

HEADERS = ["Date","Type","Description","out","in","Balance"]
GROUPBY_FIRSTXCHARS = 10



import csv
import sqlite3
import os, sys
import matchers
import logging
import datetime

lgr = logging.getLogger(__name__)
logging.basicConfig()

## import template code

from tmpl import *

def showremaining():
    """ all remaining uncategorised items"""
    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()

    c.execute("select ROWID, trans.* from trans where cty_high is NULL order by CAST(tout AS REAL) DESC;")
    rs = c.fetchall()
    rows = rs2obj(rs)

    
    outstr = '<h2>Remaining</h2><table border="1">'
    s = """<tr>
<td>%s </td>
<td>%s </td>
<td>%s </td>
<td>%s </td>

</tr>"""  

    for r in rows:
        outstr += s % (r.desc, r.moneyin, r.moneyout, r.tdate)

    return outstr + "</table>"


def test(word):

    tot = 0
    allrows = allremaining()
    for r in allrows:

       if r.desc.lower().find(word.lower()) >= 0:
            print "****>", r.desc,
            print r.moneyin - r.moneyout
            amt = r.moneyin - r.moneyout
            tot += amt
    print tot

def categorise(matchers):
    """
    I should use fnmatch in here ?
    """

    allrows = allremaining()

    try:
        for r in allrows:
            for matcher in matchers:
                word, cty_low, cty_mid, cty_high = matcher 
                if r.desc.lower().find(word.lower()) >= 0:
                    updaterow(r.rowid, cty_low, cty_mid, cty_high)
    except Exception, e:
        print r, matcher
  



def updaterow(rowid, cty_low, cty_mid, cty_high):
    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()
    print ".",
    sql = """UPDATE trans set cty_low = '%s', 
                              cty_mid = '%s',
                              cty_high = '%s'
                 WHERE ROWID = %s;""" % (cty_low, cty_mid, cty_high, rowid)            
    c.execute(sql)
    conn.commit()
    c.close()   

class tran(object):
    """ """
    def __init__(self, rowid, desc, moneyin, moneyout, tdate):
        self.desc = desc
        self.moneyin = moneyin
        self.moneyout = moneyout
        self.rowid = rowid
        self.tdate = tdate 

    def __repr__(self):
        x = "%s/%s/%s-%s" % (self.desc, self.moneyin, self.moneyout,
                          self.tdate)
        return x
    

def initdb():

    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()
    c.execute("""CREATE TABLE trans(
tdate TEXT,
ttype TEXT,
tdesc TEXT,
tout TEXT,
tin TEXT,
balance TEXT,
cty_low TEXT,
cty_mid TEXT,
cty_high TEXT);""")
    

def happystr(s):
    """mainly to replace errant pound signs

   .replace("£","")))
     """
    if not s: return ""
    newstr = ''
    for char in s:
        if ord(char) > 128: 
            pass
        else:
            newstr += char
    return newstr

def normalise_date(dstr):
    """
    given a string formatted as %d %b %Y
    return YYYY-MM-DD

    >>> normalise_date("24 Oct 2011")
    '2011-10-24'
    
    """
    import datetime, time
    try:
        dt = time.strptime(dstr, "%d %b %Y")
    except ValueError, e:
        lgr.error("dagtestring: %s" % dstr)
        raise e
    outstr = time.strftime("%Y-%m-%d", dt)
    return outstr
    
def addtrans(row):
    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()
    desc = row["Description"].replace("'","")
    #clean up transactions a bit -
    #maybe wrong place for this

    s = """INSERT INTO trans (tdate, ttype, tdesc, tout, tin, balance) 
                 VALUES ('%s','%s','%s','%s','%s','%s');""" % (str(normalise_date(row["Date"])),
                                                               str(row["Type"]), 
                                             happystr(desc), 
                                             happystr(row["out"]), 
                                             happystr(row["in"]),
                                             happystr(row["Balance"]))

    c.execute(s)    
    conn.commit()
    print ".",

def allremaining():
    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()

    c.execute("select ROWID, trans.* from trans where cty_high is NULL Order BY tdesc;")
    rs = c.fetchall()
    rows = rs2obj(rs)
    return rows   

def rs2obj(rs):
    """ select ROWID, trans.* f  < send rs of this in, get rows of trans objs"""
    rows = []
    hdr =["Date","Type","Description","out","in","Balance"]
    for row in rs:
        rowid = row[0]
        date = row[1]
        desc = str(row[2]) + ":" + str(row[3])
        moneyout = row[4]
        moneyin = row[5]

        #.. todo:: handle the "statmet" style error which is no real transaction
        #this should be better handled
        if moneyin == '' and moneyout == '': continue
 
        try:
            if not moneyin or moneyin == '': 
                moneyin = 0.0
                moneyout = float(moneyout)
        except Exception, e:
            print moneyout, row
            raise e 

        try:
            if not moneyout or moneyout == '': 
                moneyout = 0.0
                moneyin = float(moneyin) * -1
        except Exception, e:
            print moneyin, row
            raise e 

        
        rows.append(tran(rowid, desc, moneyin, moneyout, date))

    return rows



def load(f):
    """Given a CSV file of right format. create a transaction in db for eadch row """
    hdr = HEADERS
    try:
        c = csv.DictReader(open(f), hdr)
    except:
        c = csv.DictReader(open(f), hdr[-1:]) ##slice off balance
    
    for row in c:
        if row["Date"] == "Date": continue
        addtrans(row)

def amount_to_float(tout, tin):
    """
    """
    fin = 0.0
    
    try:
        fout = float(tout)
    except:
        fout = 0.0
        try:
            fin = float(tin)
        except:
            fin = 0.0
    return fout - fin

def table_from_rs_bycategory(rs):
    """ """

    tblbody = '''<table border="1">
    <tr>
    <td>Date</td> <td>Desc</td> <td>Type</td>
        <td>Category High</td><td>Category mid</td><td>Category Low</td>
            <td>TOut</td><td>TIn</td>
    </tr>
    '''
    totalval = 0
    currdesc = ''
    currdescsum = 0
    for row in rs:

        if currdesc != row[1][:GROUPBY_FIRSTXCHARS]:
            tblbody += """<tr><td colspan="8" align="right">%s: %s</td></tr>""" % (currdesc, currdescsum)
            currdesc = row[1][:GROUPBY_FIRSTXCHARS]
            currdescsum = amount_to_float(row[6], row[7])                

            tmpl2 = "<tr> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td></tr>\n"
            tblbody += tmpl2 % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            totalval += amount_to_float(row[6], row[7])

            
        else:
            tmpl2 = "<tr> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td></tr>\n"
            tblbody += tmpl2 % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            totalval += amount_to_float(row[6], row[7])

            currdescsum += amount_to_float(row[6], row[7])

    tblbody += """<tr><td colspan="8" align="right">%s: %s</td></tr>""" % (currdesc, currdescsum)

    return tblbody,totalval

def past6mths():
    '''Give me a list of first day of past 6 mths
    '''
    pass

def mk_monthly_summary_links(category_str):
    """
    Only show the last 6 mths


    aaarggh - this is painful.
    do it simple style for now
    """
    # calc last 6 mths
    
    today = datetime.datetime.today()
    delta = datetime.timedelta(days=30)
    last_6_mths = []
    for i in range(5):
        curryr = today.year
        currmth = today.month
        
        last_6_mths.append(datetime.datetime(year=curryr,
                                             month=currmth, day=1))
        today = today - delta
    
    s = ''
    onemth = datetime.timedelta(days=30)
    anchor_tmpl = mthly_tmpl
    for dt in last_6_mths:
        endofmonth = dt + onemth
        s += anchor_tmpl % (category_str, dt.strftime("%Y-%m-%d"),
                            endofmonth.strftime("%Y-%m-%d"),
                            dt.strftime("%b %Y")) + "\n"
    return s
                            
    
def table_from_rs_fullsummary(rs):
    """ """

    tblbody = '''<table border="1">
    <tr>
    <td>Amount</td> <td>Category High</td>
    <td colspan="6">By Month, last 6 mths</td>
    </tr>
    '''

    totalval = 0

    for row in rs:
        mthstr = mk_monthly_summary_links(row[1])
        tblbody += rowtmpl % (row[0], row[1], row[1], mthstr)
        totalval += amount_to_float(row[0], 0)###errors liurcking here

    tblbody += "</table>"
    return tblbody, totalval

    
def summaryview(cty_high=None, FROMDATE=None, TODATE=None):
    """
    Given a category (or None == all cty) return a table
    of that categories spend
    """
    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()

    rows = []

    html = ""
    
    
    if cty_high is None: #we want all spending, by cty_high

        c.execute("""select sum(tout), cty_high from trans
                 WHERE date(tdate) > '2012-01-01'
                 GROUP BY SUBSTR(cty_high,0,16) ORDER BY sum(tout) DESC;""")
        rs = c.fetchall()
        tblbody, totalval = table_from_rs_fullsummary(rs)
        
    elif cty_high and FROMDATE:
        c.execute("""SELECT tdate, tdesc, ttype, cty_high, cty_mid, cty_low, tout, tin
                  FROM trans WHERE cty_high = '%s'
                  AND tdate > '%s' AND tdate <= '%s'
                  ORDER BY tdesc, tdate DESC""" % (cty_high, FROMDATE, TODATE))  ###i know sql injection
        rs = c.fetchall()
        tblbody, totalval = table_from_rs_bycategory(rs)

    else:
        c.execute("""SELECT tdate, tdesc, ttype, cty_high, cty_mid, cty_low, tout, tin
                  FROM trans WHERE cty_high = '%s'
                  ORDER BY tdesc, tdate DESC""" % (cty_high))  ###i know sql injection
        rs = c.fetchall()
        tblbody, totalval = table_from_rs_bycategory(rs)

        
    html += summarypagetop % tblbody
    
    html += "<p>Total Outgoings: %s</p>" % totalval
    return html
    
    
def create_chart():
    ''' 

    return [(outmoney, category), (outmoney, category)
    '''
    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()

    c.execute("select sum(tout), cty_high from trans GROUP BY cty_high;")
    rs = c.fetchall()
    data = []

    #IGNORE transfer

    for row in rs:
        if row[0]:
            val = int(row[0])
        else:
            val = 0

        if row[1]:
            label = row[1]
        else:
            label = ''
        if label in ("transfer",): continue
        
        data.append((val, label))
    do_chart(data)


def print_categories():
    conn = sqlite3.connect(DATABASE_URI)
    c = conn.cursor()

    c.execute("select distinct cty_high from trans;")
    print "cty_high"
    for row in c.fetchall():
        print row[0]

    c.execute("select distinct cty_mid from trans;")
    print "cty_mid"
    for row in c.fetchall():
        print row[0]

    c.execute("select distinct cty_low from trans;")
    print "cty_low"
    for row in c.fetchall():
        print row[0]


def help_summary():
        
    rows = showremaining()
    for r in rows:
        s = "['%s'," % r.desc
        s = s.ljust(32)
        s += "'-', '-', '-'],"
        print s
  
###############################################Matchers

def show_categories():
 
    hidict = {}
    lodict = {}

    for tpl in matchers._matchers:

        hi = tpl[3]
        lo = tpl[1]
        phrase = tpl[0]
        hidict.setdefault(hi, []).append(phrase)
        lodict.setdefault(lo, []).append(phrase)        

    s = '<table barder="1">'

    for k in hidict:
        s += "<tr><td> %s : %s</td></tr>" % (k, len(hidict[k]))
        s += "<tr><td>%s</td></tr>" % ", ".join(hidict[k])


    s += "</table>"
    return s


        
###############################################CHARTS


from pygooglechart import PieChart2D
from pygooglechart import PieChart3D


def do_chart(chart_data):
    '''data = [(val,label), ... 
    '''
    # Create a chart object of 200x100 pixels
    chart = PieChart2D(400, 320)
    vals = []
    labels = []
    for item in chart_data:
        vals.append(item[0])
        labels.append(item[1])
    
    print vals
    print labels
    print chart_data

    # Add some data
    chart.add_data(vals)

    # Assign the labels to the pie data
    chart.set_pie_labels(labels)

    # Download the chart
    try:
        chart.download('summarypie.png')
    except Exception, e:
        pass

#############################################################
DATABASE_URI = './money.db'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit()    

    ### test whats in db per word
    action = sys.argv[1]
    f = sys.argv[2]

    if action == 'test':

        ### test for words 
        words = sys.argv[2:]
        for w in words:
            print test(w)
        ###
    elif action == 'doctest':
        ### initialise from csv
        import doctest
        doctest.testmod()

    elif action == 'init':
        ### initialise from csv
        initdb()

    elif action == 'load':
        load(f)

    elif action == 'match':

        #### catgorise from matchers
        categorise(matchers._matchers)

    elif action == 'summary':
        summaryview()
        help_summary()
        create_chart()

    elif action == 'normalise':
        print_categories()


    else:
        print "init, test, match"



