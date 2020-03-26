from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_home_teams',methods=['GET'])
def get_home_teams():
    response = jsonify({
        'home_team':util.get_home_teams()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_away_teams',methods=['GET'])
def get_away_teams():
    response = jsonify({
        'away_team':util.get_away_teams()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_winner',methods=['GET','POST'])
def predict_winner():
        
    home = request.form['home_team']
    away = request.form['away_team']
    

    response = jsonify({
        'predict_winner':float(util.get_predict_winner(home,away))
    })

    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Starting python Flask Server for Home Price Prediction")
    util.load_saved_artificats()
    app.run()