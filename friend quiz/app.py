from flask import *

app = Flask(__name__)
yesval = 0
noval = 0
score = 0
def friendscore(*args):
    global yesval,noval
    attributes = list(args)
    # score = 0
    for i in attributes:
        if i == 'yes':
            yesval += 1
        else:
            noval += 1
    return int((yesval/len(attributes))*100)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/takequiz")
def takeQuiz():
    bestie = request.args['bestie']
    if bestie == 'on':
        bestie = 'yes'
    else:
        bestie='No'
    return render_template("check.html",yourname=request.args['your-name'],friendname=request.args['name'],hobby=request.args['hobby'],bestie=bestie,friendlove=request.args['friendlove'])

@app.route("/checkres",methods=['POST'])
def checkRes():
    global score
    score = 0
    namecheck = request.form['name-check']
    hobbycheck = request.form['hobby-check']
    bestiecheck = request.form['bestie-check']
    lovecheck =request.form['love-check']
    score = friendscore(namecheck,hobbycheck,bestiecheck,lovecheck)
    return f"Your friend knows you {score}%"


if __name__ == '__main__':
    app.run(debug=True)