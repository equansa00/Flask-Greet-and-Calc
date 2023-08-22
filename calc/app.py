# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/math/add')
def math_addition():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = add(a, b)
    return str(result)

@app.route('/math/sub')
def math_subtraction():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = sub(a, b)
    return str(result)

@app.route('/math/mult')
def math_multiplication():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = mult(a, b)
    return str(result)

@app.route('/math/div')
def math_division():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = div(a, b)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
