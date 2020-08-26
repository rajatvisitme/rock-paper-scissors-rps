# Generic/Built-in
import os

# Other Libs
from flask import Flask,render_template,url_for,request, redirect

#Owned
from model.model import *

mode = 10

app = Flask(__name__)

#loading home.html (home page interface)
@app.route('/', methods=['GET', 'POST'])
def home():
	game_name = 'home'
	if request.method == 'POST':
		game_name = request.form["game_name"]
		if game_name == 'rock_paper_scissors':
			return render_template('rock_paper_scissors.html')
		else:
			return render_template('home.html')
	return render_template('home.html')

@app.route('/rps_home', methods=['POST'])
def rps_home():
	return render_template('rock_paper_scissors.html')

@app.route('/rps_mode', methods=['POST'])
def rps_mode():
	if request.method == 'POST':
		
		global mode
		mode = int(request.form["mode"])

		if mode == 0:
			msg = "Friend mode"
		elif mode == 1:
			msg = "AI - Easy mode"
		elif mode == 2:
			msg = " AI - Moderate mode"
		elif mode == 3:
			msg = " AI - Hard mode"
		else:
			msg = 'Please try again.'
			return render_template('rock_paper_scissors.html',message = msg)

	return render_template('result.html',message = [msg])

@app.route('/rps_play', methods=['POST'])
def rps_play():
	if request.method == 'POST':
		
		choice = int(request.form["player_choice"])

		if mode == 0:
			msg = "Friend mode"
			winResult = rps_friend(choice1, choice2)
		elif mode == 1:
			msg = "AI - Easy mode"
			winResult = rps_AI_e(choice)
		elif mode == 2:
			msg = " AI - Moderate mode"
			winResult = rps_AI_m(choice)
		elif mode == 3:
			msg = " AI - Hard mode"
			winResult = rps_AI_h(choice)
		else:
			msg = 'Please try again.'
			return render_template('result.html',message = [msg])

	return render_template('result.html',message = [msg, winResult])

if __name__ == '__main__':
	app.run(debug=False)
