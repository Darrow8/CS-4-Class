from flask import Flask, render_template
app = Flask(__name__) #this has 2 underscores on each side

@app.route('/')
def index():
	return render_template('index.html.j2')

@app.route('/signup')
def signup():
	return render_template('register.html.j2')

@app.route('/profile')
def profile():
	return render_template('profile.html.j2')
