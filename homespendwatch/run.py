from bottle import route, run, request
import importer


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
    return html
    
@route("/summary")    
def summary():
    html = importer.summaryview(cty_high=None)
    return htmltop + html

@route('/remaining')
def remaining():
    html = importer.showremaining()
    return htmltop + html

@route('/category')
def category():
    html = importer.show_categories()
    return htmltop + html


    
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
    print cty_high, fdate, tdate
    html = importer.summaryview(cty_high=cty_high, FROMDATE=fdate, TODATE=tdate)
    return htmltop + html

def mainview():
    html = importer.summaryview(cty_high=None)
    return htmltop + html
    
route('/', callback=hello)
route('/toadd', callback=hello)## add in full summary plus charts etc
run(host='localhost', port=8080, debug=True)