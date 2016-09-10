#!/usr/bin/python
from __future__ import division
from math import *
import random
from Tkinter import *
import string
from time import *
import os
from datetime import *
again = 0

print "Remember this, the password is 'Inventing is fun'"
print



nam = str(raw_input("What's Your Name? "))
print
print
print

def everything():
	
	if nam != "t":
	
		passw = "inventing is fun"
		print
		
		today = date.today()
		
		

		
		
		oper = str(raw_input(''''Multiply' numbers, 'divide' numbers, 'add' numbers, 'subtract' numbers, pi, power, e, abc (alphebet), rps (rock, paper, scissors), pl (pig latin), os (open Safari), gg (guessing game), tc (temperature conversion), ltn (letter to number), cth (calculate the hypotenuse), cc (circumfrence calculater), csn (cool superhero name!), fn (fun numbers!), yae (how many years after einstein died were you born), hoay (how old are you), witd (What is the date?), wimea (What is my exact age), m8b (magic 8 ball), odds
	> '''))

		oper = oper.lower()
		if oper == "yae":
			e = input("What year were born in? ")
			print "You were born", e-1955, "years after Einstein died"
			
		elif oper == "hoay":	
			e = input("What year were born in? ")
			r = date.today().year
			print "You are around", r-e, "years old"
			
		elif oper == "witd":
			
			print
			print date(today.year, today.month, today.day)

			
			
		elif oper == "wimea":
			print
			ry = input("What year were you born in? ")
			ye = today.year - ry
			
			rm = input("What month were you born in? Please type it in number form. ")
			mo = today.month - rm
			
			rd = input("What day of the month were you born on? ")
			da = today.day - rd
			
			print "You are", ye, "years,", mo, "months", da, "days old!"
			
			
		
			
		
		elif oper == "gg":
			def main():
							
				h = nam
				secret = random.randint(1, 999)
				guess = 0
				tries = 0
				print "Hi", h, "I'm thinking of a number between 1 and 1000 I bet ya can't guess it!"
				while guess != secret and tries < 6:
					guess = int(raw_input("What's you're guess? "))
					if not guess: break
					if guess < secret:	
						print guess, "is too low."
					elif guess > secret:
						print guess, "is too high."
					tries = tries + 1
					if guess == secret:
						print
						print "You've got it!!! You're a genius!!!"
						
						h = str(raw_input("Do you want to play again? "))
						if h == "yes":
							print
							print
							main()
						if h == "no":
							print "Bye"
					if tries == 20:
						print
						print "You've ran out of guesses. The number was", secret
						print
						h = str(raw_input("Do you want to play again? "))
						if h == "yes":
							print
							print	
							main()
								
						if h == "no":
							print
							print "Bye"
						
						
			main()
			
					
			

				

		elif oper == "cth":
		
			fs = input("Enter the first side of the right angle triangle: ")
			scs	= input("Enter the second side: ")
			fs_t = fs**2
			scs_t = scs**2
			not_so_final = fs_t + scs_t
			final = sqrt(not_so_final)
			print "The hypotenuse is", final
		
		elif oper == "cc":
			d = input("Enter the Diameter: ")
			r = d/2
			final = 2*pi*r
			start = "The circumfrence of you circle is"
			print start, final
			
		elif oper == "tc":
			h = int(raw_input("Enter a temperature in Fahrenheit: "))
			c = (h - 32) * 5.0 / 9
			print h, "Fahrenheit in Celsius is", c
			


		elif oper == "multiply":
			
			num = int(raw_input('Enter a number: '))
			numf = int(raw_input('Enter another number: '))
			multi = num * numf
			print multi
			
		elif oper == "divide":
			num = int(raw_input('Enter a number: '))
			numf = int(raw_input('Enter another number: '))
			if numf > num:
				divi = numf / num
				print numf, "/", num, "=", divi
				
			elif num > numf:
				divi = num / numf
				print num, "/", numf, "=", divi
				
			
			

		elif oper == "add":
			num = int(raw_input('Enter a number: '))
			numf = int(raw_input('Enter another number: '))
			addi = num + numf
			print num, "+", numf, "=", addi
			
			
			
		elif oper == "subtract":
			num = int(raw_input('Enter a number: '))
			numf = int(raw_input('Enter another number: '))
			if numf > num:
				divi = numf - num
				print numf, "-", num, "=", divi
				
			elif num > numf:
				subi = num - numf
				print num, "-", numf, "=", divi
			

		elif oper == "abc":
			def main():
				string = str(raw_input('Enter a lowercase letter: '))
				print string, "is in: a b c d e f g h i j k l m n o p q r s t u v w x y z"
			main()
			
			
				
		elif oper == "pi":
			print "Would you like to 'multiply' something by pi or just find out what 'pi' is?"
			x = raw_input("> ")
			if x == "pi":
				print "Pi is equal to: ", pi
			if x == "multiply":
				print "What number would you like to multiply by pi?"
				numpi = input("> ")
				ans = pi * numpi
				print "Pi *", numpi, "=", ans
				
				
			
			
		elif oper == "power":
			num = int(raw_input('Enter a number: '))
			numf = int(raw_input('Enter another number: '))
			print num, "to the power of", numf, "is:", pow(num, numf)
			print numf, "to the power of", num, "is:", pow(numf, num)
			
			
			
		elif oper == "e":
			print e
		
		
		elif oper == "csn":
			def super():
				rand1 = random.randrange(0,13)
				rand2 = random.randrange(0,13)
				print
				print
				nam1 = ["Captain", "Doctor", "The Great", "Awesome", "Mega", "Secret Agent", "Magnificent", "Professor", "Space Captain", "Invisible", "The Powerful", "Phantom", "The Amazing", "Crazy"]
				nam2 = ["Inventor", "Demolisher", "Kiwi", "Sprinkles", "Coffee", "Sumo Wrestler", "Muscle Man", "Chicken", "Baseball", "Genius", "Mathematician", "Fun", "Purple", "Red"]
				print "Your amazing new superhero name is: " + nam1[rand1] + " " + nam2[rand2]
				print
				print
				f = str(raw_input("If you want to make a new super hero name type in 'yeah'. If you don't want to play again, type anything else!"))
				print
				print
				print
				if f == "yeah":
					super()
				else:
					print "Goodbye, Have a great day!"
				super()
		
		elif oper == "fn":
			def getTerminalSize():
				def ioctl_GWINSZ(fd):
					try:
						import fcntl, termios, struct, os
						cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
					'1234'))
					except:
						return None
					return cr
				cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
				if not cr:
					try:
						fd = os.open(os.ctermid(), os.O_RDONLY)
						cr = ioctl_GWINSZ(fd)
						os.close(fd)
					except:
						pass
				if not cr:
					try:
						cr = (env['LINES'], env['COLUMNS'])
					except:
						cr = (25, 80)
				return int(cr[1]), int(cr[0])
			def getrandbin(): # get 1 or 0 randomly for the matrix
				import random
				return(random.randint(0, 9))
			import time, sys
			def matrix(): # this is actually just scrolling binary, not like the strange characters of the matrix
				x, y = getTerminalSize()
				def getLine():
					
					x, y = getTerminalSize()

					n1 = 0
					v = ''
					while n1 < x:
						x, y = getTerminalSize()
						v += str(getrandbin())
						n1 += 1
					return v
				n2 = 0
				v = ''
				while n2 < y:
					try: 
						t = 0.1
						#global t # uncomment this for the matrix to go a bit faster
						sys.stdout.write('\033\033' + getLine().replace('2', ' ') + '\033\r')
						sys.stdout.flush()
						time.sleep(t)
					except KeyboardInterrupt: #Ctrl+C
						pass
					except EOFError: #Ctrl+D
						break

			matrix()
			
			
			
			
			
			
			
			
			
			
			
			
			
				
			
		elif oper == "ltn":
			leet = string.maketrans('abegilopsz!', '46361109521')

			s = str(raw_input("Enter a phrase: "))

			print s, "translated into numbers is:", s.translate(leet)
			
			
		elif oper == "pl":
			pyg = 'ay'
			print
			
			if len(nam) > 0 and nam.isalpha():
				namey = "Your name in pig latin is: "
				print
				word = nam.lower()
				first = word[0]
				new_word = word + first + pyg
				new_word = word[1:] + first + pyg
				start = "in pig latin is:"
				print nam, start, new_word
			

			print
			original = str(raw_input('Enter a word: '))
			if len(original) > 0 and original.isalpha():
				
				print
				word = original.lower()
				first = word[0]
				new_word = word + first + pyg
				new_word = word[1:] + first + pyg
				start = "in pig latin is:"
				print word, start, new_word
			else:
				print 'empty'
			
			
		elif oper == "odds":
			import random
			odds = str(raw_input("Odd's me to: "))
			randi = random.randint(2,101)
			rands = str(randi)
			print("1 in "+ rands)
			num1 = raw_input("What is your number? ")
			num2 = random.randint(2,randi)
			if num1 == num2:
				print "Oh no! I have to do it!"
				print "Oh wait... I'm a computer! I can't "+ odds
				
				
			else:
				print "Re-odds my number was different it was: "+str(num2)
				newnum1 = raw_input("What is new number? ")
				newnum2 = random.randint(2,randi)
				if newnum1 == newnum2:
					print "Now you have to do it!"
				
				else:
					print "Thanks for playing! My number was different, it was: ", str(newnum2)	
		elif oper == "rps":
			def main():
				#intro message
				print
				print
				print("Let's play 'Rock, Paper, Scissors'!")
				#call the user's guess function
				number = user_guess()
				#call the computer's number function
				num = computer_number()
				#call the results function
				results(num, number)

			#computer_number function
			def computer_number():
				#get a random number in the range of 1 through 3
				num = random.randrange(1,4)
				#if/elif statement
				if num == 1:
					print("Computer chooses rock")
				elif num == 2:
					print("Computer chooses paper")
				elif num == 3:
					print("Computer chooses scissors")
				#return the number
				return num

			#user_guess function
			def user_guess():
				#get the user's guess
				guess = str(raw_input("Choose rock, paper, or scissors by typing that word. "))
				#while guess == 'paper' or guess == 'rock' or guess == 'scissors':
				if is_valid_guess(guess):
					#if/elif statement
					#assign 1 to rock
					if guess.lower() == 'rock':
						number = 1
					#assign 2 to paper
					elif guess.lower() == 'paper':
						number = 2
					#assign 3 to scissors
					elif guess.lower() == 'scissors':
						number = 3
					return number
				else:
					print('That was not an option.')
					user_guess()

			def is_valid_guess(guess):
				if guess == 'rock' or 'paper' or 'scissors':
					status = True
				else:
					status = False
				return status

			def restart():
				answer = str(raw_input('''Would you like to play again? Enter yes or no:
				> '''))
				#if/elif statement
				if answer == 'yes':
					print
					main()
				elif answer == 'no':
					print
					print("Goodbye!")
				else:
					print
					print("Please enter only yes or no!")
					#call restart
					restart()

			#results function
			def results(num, number):
				#find the difference in the two numbers
				difference = num - number
				#if/elif statement
				if difference == 0:
					
					print('''The result is a... 
					TIE!''')
					#call restart
					restart()
				elif difference % 3 == 1:
					
					print("I'm sorry! You lost :)")
					#call restart
					restart()
				elif difference % 3 == 2:
					
					print("Great Job!!! You won :)")
					
					#call restart
					restart()

			main()
			
			


		elif oper == "m8b":
			q = str(raw_input("Ask me anything:"))
			a = random.randint(1,8)
			if a == 1:
				print "This is for certain!"
			elif a == 2:
				print "Outlook good"
			elif answers == 3:
				print "There is a 50/50 chance"
				
			elif answers == 4:
				print "Ask again later"
				
			elif answers == 5:
				print "Concentrate and ask again"
				
			elif answers == 6:
				print "I sure hope so for your sake"
				
			elif answers == 7:
				print "My reply is no"
				
			elif answers == 8:
				print "My sources say no"
				
		
		elif oper == "os":
			import webbrowser
			h = string.maketrans(' ',"+")
			
			search = 'https://www.google.ca/?gws_rd=ssl#q='
			url = "https://"
			b = str(raw_input("Would you like to 'search' something or open a 'website' "))
			
			if b == 'website':
				print "What website would you like to go on? "
				t = str(raw_input())
				webbrowser.open_new_tab(url + t)
			if b == 'search':
				print "What would you like to search?"
				s = str(raw_input())
					

			
		
		print
		print "WHO DA BEST?"
		print str(nam.upper()) + "'S DA BEST"	
		
	def pass_enter():	
		print "Do you want to play fun machine again? If not type no. Bye Bye. If so please enter the password that was shown at the start of the program!"
		passyes  = raw_input("Enter Password Here: ").lower()	
		if passyes == "no":
			exit()			
		elif passyes == passw:	
			print
			print "You are correct!"	
			print
		else:
			print
			print "Try again!"
			print
			pass_enter()
		everything()
	pass_enter()
		
		
		
everything()


