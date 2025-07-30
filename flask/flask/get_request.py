from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome  to the flask app!"

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route("/index",methods = ['GET'])
def index():
    return render_template('index.html')
@app.route('/form', methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"Name: {name}, Email: {email}"

    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)