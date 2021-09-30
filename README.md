# CS-4-Class

For anyone seeing this online, this is my personal repo for my CS 4 class at Lakeside. Feel free to look around, but please don't edit stuff.

Everything should be in http://www.2122.lakeside-cs.org/DarrowHartman/<file-name>, unless Miss. O'Neal has removed it.

# Setting up file (Automatic)

(only works on mac)
Setup file by: `chmod 700 init-project`
And then: `./init-project`


# Setting up file (Manual)

1. Make a new file in repo
2. Run `touch runflask.bat`
3. Add this code to that .bat file:
```
export FLASK_APP=app.py && export FLASK_ENV=development
flask run
```
4. Run `touch app.py`
5. Add this code to the file:
```
from flask import Flask, render_template
app = Flask(__name__) #this has 2 underscores on each side

@app.route('/')
def hello_world():
   return render_template('index.html')
```
6. Add an `index.html` file in `/templates`
7. Run `chmod 777 runflask.bat` and then `./runflask.bat`
8. Go to http://127.0.0.1:5000 and start coding!
