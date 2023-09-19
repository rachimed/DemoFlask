from flask import Flask, render_template, request,  url_for, redirect
# import pandas as pd

# instanciation off app Flask
app = Flask(__name__)

#! Routes
@app.route("/")
def home():


    return render_template('index.html')

#! Route formulaire

@app.route('/form', methods=["POST", "GET"])
def form():
    data =242
    
    if request.method == 'POST':
        print("post")
        age = request.form.get('age')
        sex = request.form['sex']
        pclass = request.form['class']
        print(age, sex, pclass)
    result = data
    return render_template('form.html', result=result, title="resultat")




# @app.route("/add_nbre")
# def fct_add():
#     nbre= request.args.get('nbre')
#     nbre=Mathematica.addition(int(nbre))
#     return f'<h1>Addition + 100 = {nbre}'

# Variables environement
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)