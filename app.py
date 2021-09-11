from flask import Flask, render_template, request
import joblib

# initialise the app
app = Flask(__name__)
model = joblib.load("dib_79.pkl")


@app.route('/')
def hello_word():
    return render_template('diabtic.html')



@app.route('/predict' , methods = ['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    output = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if output[0]==1:
        ans = 'dibatic'
    else:
        ans = 'not dibatic'
    return render_template('predict.html', pred = f"person is {ans}")


#run the app
if __name == '__main__':
    app.run()

