import random

def rps_friend(choice1, choice2):
	pass

def rps_AI_m(player_move):
	AI_list = [1, 2, 3]
	AI_move = random.choice(AI_list)
	
	if player_move == AI_move:
		return "Game tie"
	elif player_move == 1:
		if AI_move == 2:
			return "AI move: Paper\nAI Win"
		else:
			return "AI move: Scissors\nYou Win"
	elif player_move == 2:
		if AI_move == 3:
			return "AI move: Scissors\nAI Win"
		else:
			return "AI move: Rock\nYou Win"
	elif player_move == 3:
		if AI_move == 1:
			return "AI move: Rock\nAI Win"
		else:
			return "AI move: Paper\nYou Win"
	else:
		return "Wrong choice."



def rps_AI_h(player_move):

	if player_move == 1:
		AI_list = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3]
		AI_move = random.choice(AI_list)
		if AI_move == 1:
			return "AI move: Rock | Game tie"
		elif AI_move == 2:
			return "AI move: Paper | AI Win"
		else:
			return "AI move: Scissors | You Win"
	elif player_move == 2:
		AI_list = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
		AI_move = random.choice(AI_list)
		if AI_move == 2:
			return "AI move: Paper | Game tie"
		elif AI_move == 3:
			return "AI move: Scissors | AI Win"
		else:
			return "AI move: Rock | You Win"
	elif player_move == 3:
		AI_list = [1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3]
		AI_move = random.choice(AI_list)
		if AI_move == 3:
			return "AI move: Scissors | Game tie"
		elif AI_move == 1:
			return "AI move: Rock | AI Win"
		else:
			return "AI move: Paper | You Win"
	else:
		return "Wrong choice."