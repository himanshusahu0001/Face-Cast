from flask import *
import requests
import json
from datetime import date

app = Flask(__name__)


@app.route("/")
def home():
    ACCESS_KEY = 'uhTPYDLCZsCUu5LJi-h16w37TwaiZWXTYwvJ7JtzUD4'
    query = 'voting'
    params = {'query': query, 'client_id': ACCESS_KEY, 'w': 720, 'h': 600}
    endpoint = f"https://api.unsplash.com/photos/random"
    # endpoint = f"https://api.unsplash.com/photos/random?client_id={ACCESS_KEY}&w=720&h=600&query={query}" #can use like this also

    # Make the API request
    response = requests.get(endpoint, params=params)

    # Parse the response data as JSON
    data = response.json()
    img_url = data['urls']['regular']

    return render_template('home.html', img_url=img_url)



@app.route("/ongoing-elections")
def OngoingElections():
    
    # read the contents of the file
    with open('elections_list.json', 'r') as f:
        file_contents = f.read()
    # parse the JSON string back into an array
    electionsList = json.loads(file_contents)
    today = date.today()

    return render_template('OngoingElection.html',list=enumerate(electionsList), today=today)



@app.route("/admin", methods=['GET'])
def admin():
    # read the contents of the file
    with open('elections_list.json', 'r') as f:
        file_contents = f.read()
    # parse the JSON string back into an array
    electionsList = json.loads(file_contents)
    today = date.today()
    return render_template('admin.html',list=enumerate(electionsList), today=today)

@app.route("/add-election",methods=['POSt'])
def addElection():
    electionName = request.form['electionName']

    # read the contents of the file
    with open('elections_list.json', 'r') as f:
        file_contents = f.read()
    # parse the JSON string back into an array
    electionsList = json.loads(file_contents)

    ####### 
    electionsList.append(electionName)
    #######

    json_string = json.dumps(electionsList)

    # write the JSON string to a file
    with open('elections_list.json', 'w') as f:
        f.write(json_string)

    return redirect(url_for('admin'))


@app.route("/delete-election",methods=['POSt'])
def deleteElection():
    electionIndex = request.form['electionIndex']

    # read the contents of the file
    with open('elections_list.json', 'r') as f:
        file_contents = f.read()
    # parse the JSON string back into an array
    electionsList = json.loads(file_contents)

    ####### 
    electionsList.pop(int(electionIndex))
    #######

    json_string = json.dumps(electionsList)

    # write the JSON string to a file
    with open('elections_list.json', 'w') as f:
        f.write(json_string)

    return redirect(url_for('admin'))

@app.route("/signin")
def signin():
    return '<h1 style="text-align: center;  font-size: xx-large; color:red; -webkit-text-stroke: 1px black;"> Create a signin page </h1>'

@app.route("/signup")
def signup():
    return '<h1 style="text-align: center;  font-size: xx-large; color:red; -webkit-text-stroke: 1px black;"> Create a signup page </h1>'








@app.route("/tmp")
def tmp():
    return render_template('tmp.html')


if __name__ == "__main__":
    app.run(port=80, debug=True)
