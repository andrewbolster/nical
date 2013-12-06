from flask import Flask, render_template, abort
from calendar import Calendar
from datetime import date

app = Flask(__name__)

defaults = {'year': date.today().year, 'month':date.today().month}

@app.route('/', defaults=defaults)
@app.route('/<int:year>/')
@app.route('/<int:year>/<int:month>/')
def index(year,month):
	cal = Calendar(0)
	try:
		if not year:
			year = date.today().year
		month = date.today().month
		day = date.today().day
		cal_list = [cal.monthdatescalendar(year, i+1) for i in xrange(12)]
	except Exception, e:
		abort(404)
	else:
		return render_template('cal.html', year=year, today = date.today(), cal=cal_list)
	abort(404)

if __name__ == '__main__':
    app.run(debug=True)
