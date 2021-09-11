from flask import Flask, render_template, request

# initialise the app
app = Flask(__name__)


@app.route('/')
def hello_word():
    return render_template('home.html')

@app.route('/predict' , methods = ['post'])
def predict():
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    email = request.form.get('email')
    phone = request.form.get('phone')

    print(first_name)
    print(last_name)
    print(email)
    print(phone)

    return 'Form Submitted'

#run the app
app.run(debug=True)
