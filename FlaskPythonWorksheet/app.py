from flask import Flask, render_template
app = Flask(__name__) #this has 2 underscores on each side

@app.route('/')
def hello_world():
   return render_template('index.html.j2', variablewww=123)
@app.route('/wowie')
def wowie():
   return 'wowie'
@app.route('/factorial')
def factorialPage():
    numList = [1,2,6,9,17,28,93,111]
    factorialList = []
    for i in range(len(numList)):
        factorialList.append(calculateFactorial(numList[i]))
    return render_template('factorial.html.j2', factorialList=factorialList)

    # return str(factorialList[2])

def calculateFactorial(num):
    factorial = 1
    i = 1
    while i <= num:
      factorial*=i
      i += 1
    return (factorial)
