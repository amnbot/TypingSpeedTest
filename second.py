from flask import Blueprint, render_template
import json
from operator import itemgetter

second = Blueprint("second", __name__, template_folder='templates')



def get_leaderboard():
    with open("leaderboard.json", "r+") as leaderboard:
        leaders = json.load(leaderboard)
        
        return sorted(leaders["users"], key=itemgetter('time'))


@second.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html', board=get_leaderboard())