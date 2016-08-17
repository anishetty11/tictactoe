import sys
import time
import random


c='computer'
u1='Player 1'
u2='Player 2'

def disp(t):
	print "\n \n The game was won by",t,'\n \n'
	if (raw_input('Do you want to play again? y/n: \t')=='y'):
		body()
	else:
		sys.exit()
	
	
# define conditions for a win
def win(x,y,z,t):
	if ((board[x]=='O' and board[y]=='O' and board[z])=='O')or ((board[x]=='X' and board[y]=='X' and board[z])=='X') :
		disp(t) 
	
def win_check(t):
	win(0,1,2,t)
	win(3,4,5,t)
	win(6,7,8,t)
	win(0,3,6,t)
	win(1,4,7,t)
	win(2,5,8,t)
	win(0,4,8,t)
	win(2,4,6,t)


# double plyer or against computer
def opponent_selector():
	global opponent
	if (opponent=='C' or opponent=='T'):
		pass
	else:
		opponent=raw_input("\n \n You have to select either 'T' (2 player),\n or 'C' (against computer) -->").upper()
		opponent_selector()


# to print board(the matrix containing 'O' and 'X') in a 3*3 matrix
def board_print():
	print '_'*120
	if (opponent=='T'):
		print "\nPlayer 1 is \"",user, "\" AND Player 2 is \"",computer,'"'
	else:
		print "\nPlayer 1 is \"",user, "\" AND Computer is \"",computer,'"'
	print "\n \n"
	for i in range(6,-1,-3):
		for j in range(3):
			print board[i+j],
		print "\n"

# allow user to select 'X' or 'O'
def x_o():
	global user
	if (user=='O' or user=='X'):
		pass
	else:
		user=raw_input("\n \n Please enter only 'O' or 'X': \t").upper()
		x_o()
 
	


def tied_game():
	if (len(entries)>8):
		print "Game ended in a tie"
		if (raw_input('Do you want to play again? y/n : \t').lower()=='y'):
			body()
		else:
			sys.exit()
		
# player1's turn 
def user_game():
	tied_game()
	user_turn=int(raw_input("Enter Player1's choice 1-9:\t"))-1
	if (entries.count(user_turn)!=0):
		print "Enter a different number"
		user_game()
	entries.append(user_turn)
	board[user_turn]=user
	board_print()
	win_check(u1)
	computer_game()
	
# player2's / computer's turn. (based on selection)
def computer_game():
	global computer_turn
	tied_game()
	if (opponent=='T'):
		computer_turn=int(raw_input("Enter Player2's choice 1-9:\t"))-1
	else:
		artificial()
	entries.append(computer_turn)
	board[computer_turn]=computer
	board_print()
	if (opponent=='T'):
		win_check(u2)
	else:
		win_check(c)
	user_game()
	
# AI to play against computer. 

def horizantal(x,y,z,puter):
	global counter
	global computer_turn
	if ((board[x]==puter and board[y]==puter and board[z])=='_'):
			computer_turn=z
			counter=1
	elif ((board[x]=='_' and board[y]==puter and board[z])==puter):
			computer_turn=x
			counter=1
	elif((board[x]==puter and board[y]=='_' and board[z])==puter):
			computer_turn=y
			counter=1

# if any sides are empty, they are filled by comp randmonly			
def sides():
	global computer_turn
	temp2=[7,3,5,1]
	computer_turn=random.choice(temp2)
	if (entries.count(computer_turn)!=0):
			sides()
			
# if any corner are empty, they are filled by comp randmonly
def corners():
	global computer_turn
	temp1=[6,8,0,2]
	if (board[6]=='_' or board[8]=='_' or board[0]=='_' or board[2]=='_'):
		computer_turn=random.choice(temp1)
		if (entries.count(computer_turn)!=0):
			corners()
	else:
		if (board[4]=='_'):
			computer_turn=4
		sides()

# matrixi  is filled in this order-> comp win, user win, centre, corner, side		
def artificial():
	global counter
	counter=0
	global computer_turn
	horizantal(0,1,2,user)
	horizantal(3,4,5,user)
	horizantal(6,7,8,user)
	horizantal(0,3,6,user)
	horizantal(1,4,7,user)
	horizantal(2,5,8,user)
	horizantal(0,4,8,user)
	horizantal(2,4,6,user)
	# if computer has a chance to win, the below lines overwrite the above lines
	horizantal(0,1,2,computer)
	horizantal(3,4,5,computer)
	horizantal(6,7,8,computer)
	horizantal(0,3,6,computer)
	horizantal(1,4,7,computer)
	horizantal(2,5,8,computer)
	horizantal(0,4,8,computer)
	horizantal(2,4,6,computer)
	
	#centre fill
	
	if (counter==0):
		corners()


# main function
def body():
	global opponent
	global computer
	global board
	global user
	global entries
	board=['_','_','_','_','_','_','_','_','_']  #the matrix
	entries=[]                                   # contains all entries made by user and computer, to avoid duplicate entry
	opponent=raw_input("\n \n Select 'T' for Two player game,\n Select 'C' to play against computer:\n -->").upper()
	opponent_selector()
	user=raw_input("\n \n Select either 'O' or 'X' : \t").upper()
	x_o()
	if (user=='X'):
		computer='O'
	else:
		computer='X'
	board_print()
	counter=0
	computer_turn=0
	who_goes_first=random.randint(0,2)
	if (who_goes_first==0):
		print " \n Player 1 goes first \n"
		user_game()
	
	else:
		if(opponent=='T'):
			print "\n Player 2 goes first \n"
			computer_game()
		else:
			print "\n Computer goes first \n"
			computer_game()

opponent=''
board=[]
entries=[]
computer=''
user=''
body()
