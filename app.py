from flask import Flask, jsonify, request
import pickle
import pandas as pd
import numpy as np
# load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# load the doctor data
df = pd.read_csv('doctor.csv', encoding='ISO-8859-1')

# initialize the Flask app
app = Flask(__name__)

# define the API endpoint
@app.route('/recommend', methods=['POST'])
def recommend():
    # parse the request data
    data = request.get_json()

    # extract the user inputs from the request data
    # location = data['location']
    # experience = data['experience']

    # convert location to numerical value
    # le = LabelEncoder()
    # location = le.fit_transform([location])[0]

    # get the recommended doctors
    # user = [0, experience, location]
    data = request.get_json(force=True)
    user = np.array(list(data.values()))

    distances, indices = model.kneighbors([user])
    recommended_doctors = []
    for i in indices[0]:
        recommended_doctors.append(df.iloc[i]['name'])

    # return the recommended doctors as a JSON response
    response = {'recommended_doctors': recommended_doctors}
    return jsonify(response)

# start the app
if __name__ == '__main__':
    app.run(debug=True)
