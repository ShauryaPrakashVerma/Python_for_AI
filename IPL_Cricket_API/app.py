from flask import Flask,jsonify, request

import ipl
import not_done

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'


# api return type should always be a json
# use jsonify() to convert dictionary into a json file
@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)


# this api accepts inputs
@app.route('/api/teamvteam')
def teamvteam():
    team1 = request.args.get('team1')    # accepting input
    team2 = request.args.get('team2')    # accepting input
    response = ipl.team_vs_team_API(team1, team2)
    print(response)
    return jsonify(response)

@app.route('/api/team-record')
def team_record():
    team = request.args.get('team')
    response = not_done.teamAPI(team)
    # return response
    return jsonify(response)

@app.route('/api/batting-record')
def batting_record():
    batsman = request.args.get('batsman')
    response = not_done.batsmanAPI(batsman)
    # return response
    return response

@app.route('/api/bowling-record')
def bowling_record():
    bowler = request.args.get('bowler')
    response = not_done.bowlerAPI(bowler)
    # return response
    return response
app.run(debug = True)