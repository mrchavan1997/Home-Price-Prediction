from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_location')
def get_location():
    res = jsonify({
        'location' : util.get_location()
        })
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res


@app.route('/predict_price', methods = ['POST'])
def predict_price():
    location = request.form['location']
    sqft = float(request.form['total_sqft'])
    bath = float(request.form['bath'])
    balcony = float(request.form['balcony'])
    bhk = float(request.form['BHK'])
    
    responce = jsonify({
        'price' : util.predict_price(location, sqft, bath, balcony, bhk)
        })
    responce.headers.add('Access-Control-Allow-Origin', '*');

    return responce;
    
#return util.predict_price(location, sqft, bath, balcony, bhk)
    

if __name__ == '__main__':
    print('server is started...')
    util.get_artifact()
    app.run()