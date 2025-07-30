from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome  to the flask app!"

@app.route('/hello')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)