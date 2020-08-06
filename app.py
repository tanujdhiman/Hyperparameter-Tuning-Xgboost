import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('clf.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    final_features = np.array(int_features)
    if final_features[0] == "France":
        final_features[0] = 0
    elif final_features[0] == "Spain":
        final_features[0] = 1
    elif final_features[0] == "Germany":
        final_features[0] = 2

    if final_features[1] == "Male":
        final_features[1] = 1
    elif final_feature[1] == "Female":
        final_features[1] = 0
    prediction = model.predict(final_features)

    #output = round(prediction[0], 2)
    if prediction[0][0] == 1:
        out = 'Oops, according to the customer information, he/she can be exit from bank'
    elif prediction[0][0] == 0:
        out = 'Nice, according to the customer information, he/she can not exit from bank'
    return render_template('index.html', prediction_text='{}'.format(out))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)