from flask import Flask, render_template
app=Flask(__name__)


@app.route('/')
def index():
	return render_template('content.html')


@app.route('/sign')
def sign():
	return render_template('sign.html')


@app.route('/signin')
def signin():
	return render_template('signin.html')


if __name__=='__main__':
	app.run(host='0.0.0.0')