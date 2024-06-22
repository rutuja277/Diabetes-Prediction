from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open(r"C:\Users\RutujaKshirsagar\Desktop\Diab proj\random_forest_model.pkl", 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    # Make prediction
    prediction = model.predict(final_features)
    
    # Output result
    output = prediction[0]
    
    if output == 1:
        result = "Diabetic"
    else:
        result = "Non-diabetic"
    
    return render_template('index.html', prediction_text=f'The person is {result}')

if __name__ == "__main__":
    app.run(debug=True)
