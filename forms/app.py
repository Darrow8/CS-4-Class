from flask import Flask, render_template, request
app = Flask(__name__) #this has 2 underscores on each side

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    inputName = request.form.getList("inputName")
    return render_template('results.html', inputName=inputName)
