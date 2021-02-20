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
            
            return random.choice(data['prompts'])
            
print(get_prompt())

if __name__ == "__main__":
        app.run(debug=True)

# Basic Script:
'''
import time

prompt = "bored in the house and im in the house bored\n"
start = time.time()
user_str = input(prompt)

if not user_str + "\n" == prompt:
  end = time.time()
  print(f'it took you {end-start} seconds to write the wrong sentence.\n Your wpm is {(len(user_str.split(" ")))/((end-start))}')

else:
  end=time.time()
  print(f'it took you {end-start} seconds to write the right sentence.\n Your wpm is {round((len(prompt.split(" ")))/((end-start))*60)}')
'''
