from bottle import route, run, request
import importer
import datetime

tmpl = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>Bootstrap 101 Template</title>

    <!-- Bootstrap -->

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
  </head>

<body>

{body}

</body>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>


</html>
'''


htmltop = """<h2>Bank Summariser</h2>
    Bank summariser
    <a href="/summary">Summary Top Level</a>
    <a href="/remaining">Remaining transactions needing cateorising</a>
    <a href="/category">Category</a>    

    """

@route('/')
def hello():
    html = """<h2>Bank Summariser</h2>
    Bank summariser
    <a href="/summary">Summary Top Level</a>
    <a href="/remaining">Remaining transactions needing cateorising</a>
    <a href="/category">Category</a>    

    """
    return tmpl.format(body=html)
    
@route("/summary")    
def summary():
    html = importer.summaryview(cty_high=None)
    return tmpl.format(body=htmltop + html)

@route("/summarymonth/<_year>/<_mth>")    
def summarymonth(_year=None, _mth=None):
    #summaryview(cty_high=None, FROMDATE=None, TODATE=None)
    mth=int(_mth)
    year=int(_year)
    if mth < 1 or mth > 12 or year < 2012:
        raise "Incorect dates"
    
    fdate = datetime.date(year=year, month=mth, day=1)
    tdate = datetime.date(year=year, month=mth, day=28)
    html = importer.summaryview(cty_high=None, FROMDATE=fdate, TODATE=tdate)
    return tmpl.format(body=htmltop + html)



@route('/remaining')
def remaining():
    html = importer.showremaining()
    return tmpl.format(body=htmltop + html)

@route('/category')
def category():
    html = importer.show_categories()
    return tmpl.format(body=htmltop + html)


    
### /summary/groceries?fdate=2013-01-01&tdate=2013-01-30
@route('/summary/<path:path>')
def summary_with_dates(path):
    """
    crap - these should be query arguments !
    """
    try:
        fdate = request.query['fdate']
        tdate = request.query['tdate']  
    except KeyError:
        fdate = None
        tdate = None
        #return "bad format - use  /summary/groceries?fdate=2013-01-01&tdate=2013-01-30 " 
    cty_high = path
    html = importer.summaryview(cty_high=cty_high, FROMDATE=fdate, TODATE=tdate)
    return tmpl.format(body=htmltop + html)

def mainview():
    html = importer.summaryview(cty_high=None)
    return tmpl.format(body=htmltop + html)
    
route('/', callback=hello)
route('/toadd', callback=hello)## add in full summary plus charts etc
run(host='localhost', port=8080, debug=True)
