from flask import Blueprint, render_template

second = Blueprint("second", __name__, template_folder='templates')

@second.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')