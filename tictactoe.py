import sys

board=['_','_','_','_','_','_','_','_','_']
def disp(t):
	print "The game was won by",t,'\n \n'
	sys.exit()
def win(t):
	if ((board[0]=='O' and board[1]=='O' and board[2])=='O')or ((board[0]=='X' and board[1]=='X' and board[2])=='X') :
		disp(t) 

	if ((board[3]=='O' and board[4]=='O' and board[5])=='O')or ((board[3]=='X' and board[4]=='X' and board[5])=='X') :
		disp(t)
	
	if ((board[6]=='O' and board[7]=='O' and board[8])=='O')or ((board[6]=='X' and board[7]=='X' and board[8])=='X') :
		disp(t)
	
	if ((board[0]=='O' and board[3]=='O' and board[6])=='O')or ((board[0]=='X' and board[3]=='X' and board[6])=='X') :
		disp(t)
	
	if ((board[1]=='O' and board[4]=='O' and board[7])=='O')or ((board[1]=='X' and board[4]=='X' and board[7])=='X') :
		disp(t)
	
	if ((board[2]=='O' and board[5]=='O' and board[8])=='O')or ((board[2]=='X' and board[5]=='X' and board[8])=='X') :
		disp(t)
	
	if ((board[0]=='O' and board[4]=='O' and board[8])=='O')or ((board[0]=='X' and board[4]=='X' and board[8])=='X') :
		disp(t)
	
	if ((board[2]=='O' and board[4]=='O' and board[6])=='O')or ((board[2]=='X' and board[4]=='X' and board[6])=='X') :
		disp(t)
	
	


entries=[]
def board_print():
	#print board
	print "\n \n"
	for i in range(6,-1,-3):
		for j in range(3):
			print board[i+j],
		print "\n"
board_print()
c='computer'
u='user'
user=raw_input("Select either 'O' or 'X' : \t").upper()
def x_o():
	global user
	if (user=='O' or user=='X'):
		pass
	else:
		user=raw_input("Please enter only 'O' or 'X': \t").upper()
		x_o()
x_o()
if (user=='X'):
	computer='O'
else:
	computer='X' 

def tied_game():
	if (len(entries)>8):
		print "game tied"
		sys.exit()
def user_game():
	tied_game()
	board_print()
	user_turn=int(raw_input("enter your coice 0-8:\t"))-1
	#print "user turn =",user_turn
	if (entries.count(user_turn)!=0):
		print "Enter a different number"
		user_game()
	entries.append(user_turn)
	board[user_turn]=user
	board_print()
	win(u)
	computer_game()
	
def computer_game():
	tied_game()
	computer_turn=int(raw_input("enter computer choice:\t"))-1
	#print "coomputer turn =",computer_turn
	if (entries.count(computer_turn)!=0):
		print "Enter a diferent number"
		computer_game()
	entries.append(computer_turn)
	board[computer_turn]=computer
	board_print()
	win(c)
	user_game()
	
def artificial():
	pass
	

user_game()
