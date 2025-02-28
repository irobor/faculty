from flask import render_template
from .. import app

@app.errorhandler(404)
def not_found_error(error):
	if app.debug:
		d = 'ssss'
	else:
		d = 'fuck'
	return render_template('404.html', d = d), 404
