from flask import Flask, render_template
#from second import second

app = Flask(__name__, template_folder='templates')
#pp.register_blueprint(second)

@app.route('/')
def home():
    return render_template('index.html')

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
