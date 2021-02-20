from flask import Flask, request, render_template, send_file
from second import second
import json
import random
import os

app = Flask(__name__, template_folder='templates')
app.register_blueprint(second)

@app.route('/')
def home():
    return render_template('index.html', prompt=get_prompt())



def get_prompt():
    with open("db.json") as prompts:
            data = json.load(prompts)
            
            #return random.choice(data['prompts'])

            return make_sentence()

@app.route('/submit-score', methods=['POST'])
def submit_score():
    user = {
        "name": request.form["name"],
        "time": float(request.form["time"])
    }
    data = None
    
    with open("leaderboard.json") as leaderboard:
        data = json.load(leaderboard)
        
        already_exists = False
        for _user in data["users"]:
            if _user["name"] == user["name"]:
                _user["time"] = user["time"]
                already_exists = True
                break
        
        if not already_exists:
            data["users"].append(user)
        
    with open("leaderboard.json", "w") as leaderboard:
        if data:
            json.dump(data, leaderboard, indent=True)
    
    return request.form

@app.route('/jquery-3.5.1.js', methods=['GET'])
def jquery():
    return send_file(os.getcwd() + "/jquery-3.5.1.js")


def make_sentence():
    sentence = ""
    
    with open('words.txt', 'r+') as words:
        word_list = words.read().split('\n')
        for i in range(10):
            word = random.choice(word_list)
            sentence += word + " "
    
    return sentence.strip() 
            




if __name__ == "__main__":
        app.run(debug=True)



