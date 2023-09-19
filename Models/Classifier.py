import joblib

loaded_model = joblib.load("./Models/titanic_log_reg.pkl")
class model():
    def survie(data):
        prediction = loaded_model.predict(data)
        if prediction == 1:
            return "Vous avez survecu "
        else:
            return "Vous ete mort"
            