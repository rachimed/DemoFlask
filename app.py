from flask import Flask, render_template, request,  url_for, redirect
import pandas as pd
from Models.Classifier import model

# instanciation off app Flask
app = Flask(__name__)


#! Routes
@app.route("/")
def home():


    return render_template('index.html')

#! Route formulaire

@app.route('/form', methods=["POST", "GET"])
def form():
    
    
    if request.method == 'POST':
        data = {}
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        pclass = int(request.form['class'])
        
        data={
            'age':age,
            'sex': sex,
            'pclass': pclass
        }
        # data['age'] =age
        # data['sex'] =sex
        # data['pclass'] =pclass
        df = pd.DataFrame(data, index=[0])
        
        result = model.survie(df)
        
        print(age, sex, pclass)
        
        return render_template('form.html', result=result, title="resultat")
    else:
        return render_template('form.html', title="resultat")





# Variables environement
if __name__ == "__main__":
    app.run(port=8080)