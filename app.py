from flask import Flask, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to Github's Flask App!"

# Greeting route with a dynamic name
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! How are you today?"

# Route to accept GET query parameters
@app.route('/square')
def square():
    number = request.args.get('number', default=1, type=int)
    return f"The square of {number} is {number ** 2}."

if __name__ == '__main__':
    app.run(debug=True)
#made necessary changes