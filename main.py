from flask import Flask, request, render_template
from second import second
import json
import random

app = Flask(__name__, template_folder='templates')
app.register_blueprint(second)

@app.route('/')
def home():
    return render_template('index.html', prompt=get_prompt())

@app.route('/', methods=['POST'])
def home_post():
    text = request.form['text']
    processed_text = text.upper()
    
    return processed_text

def get_prompt():
    with open("db.json") as prompts:
            data = json.load(prompts)
            
            #return random.choice(data['prompts'])

            return make_sentence()
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



