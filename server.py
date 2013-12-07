from flask import Flask, render_template, abort
from calendar import Calendar
from datetime import date
from events import sources

app = Flask(__name__)

defaults = {'year': date.today().year, 'month':date.today().month}

@app.route('/', defaults=defaults)
@app.route('/<int:year>/', defaults = defaults)
@app.route('/<int:year>/<int:month>/', defaults = defaults)
def index(year,month):
    try:
        day = date.today().day
        today = date(year,month,day)
    except Exception, e:
        abort(404)
    else:
        return render_template('cal.html', today = today, sources = sources)
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)
