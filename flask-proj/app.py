from flask import Flask, render_template
app = Flask(__name__) #this has 2 underscores on each side

@app.route('/')
def index():
   return render_template('index.html')
