from flask import Flask, render_template, request
app = Flask(__name__) #this has 2 underscores on each side

@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/results',methods=['POST'])
def results():
    name = request.form.get('name')
    is_secret = request.form.getlist('is_secret')
    url = request.form.get('myURL')
    doesWork = processResults()
    return render_template('results.html.j2', name=name, works=doesWork,is_secret=is_secret,url=url)

# For processing the results from the main page form to make sure that everything exists
def processResults():
    if(len(request.form.get('name')) == 0):
        return False
    if(request.form.getlist('is_secret') != ['yes']):
        return False
    if(len(request.form.get('myURL')) == 0):
        return False
