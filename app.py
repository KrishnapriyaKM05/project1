from flask import Flask,jsonify,render_template
import random

app=Flask(__name__)
options=("rock","paper","scissors")
winning=("paper","scissors","rock")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/play/<player>")
def play(player):
    computer = random.choice(options)

    if player == computer:
        result = "It's a tie!"
    elif winning[options.index(computer)] == player:
        result = "You win! "
    else:
        result = "You lose! "

    return jsonify({"computer": computer, "result": result})  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)



