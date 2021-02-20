from flask import Flask, render_template
#from second import second

app = Flask(__name__, template_folder='templates')
#pp.register_blueprint(second)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
        app.run(debug=True)