import os
from flask import Flask, render_template, request

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')

def index():
	return render_template('home.html')

@app.route('/home', methods=['POST'])

def home():
	target = os.path.join(APP_ROOT, 'static/')

	if not os.path.isdir(target):
		os.mkdir(target)

	for file in request.files.getlist("file"):
		filename = file.filename
		destination = '/'.join([target, filename])
		file.save(destination)

	return render_template("completed.html", imagename=filename)
	

if __name__ == '__main__':
	#REMOVE
	app.run(debug=True)