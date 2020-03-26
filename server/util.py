import json
import pickle 
import numpy as np

__home_teams = None
__away_teams = None
__data_columns = None
__model = None

def get_predict_winner(home,away):
    try: 
        loc_home = __data_columns.index(home.lower())
        loc_away = __data_columns.index(away.lower())
    except:
        loc_home = -1
        loc_away = -1
    x = np.zeros(len(__data_columns))
    if loc_home >= 0:
        x[loc_home] = 1
    if loc_away >= 0:
        x[loc_away] = 1
    return __model.predict([x])[0]

def get_home_teams():
    return __home_teams

def get_away_teams():
    return __away_teams

def get_data_columns():
    return __data_columns

def load_saved_artificats():
    print("Loading saved arificats....start")
    global __data_columns
    global __home_teams
    global __away_teams
    global __model
    with open("./artifacts/columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']
        __home_teams = __data_columns[0:39]
        __away_teams = __data_columns[39:]
    
    with open("./artifacts/PremierLeague_prediction.pickle","rb") as f:
        __model = pickle.load(f)
    print("Loading artificats....done")
        
if __name__ == "__main__":
    load_saved_artificats()
    print(get_home_teams())
    print(get_away_teams())
        