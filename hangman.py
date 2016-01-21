#Logan Saruwatari
#Assignment 1 Hangman
#Simple command line hangman game.

from random import randint
from os import system
from os import name as osName



class Hangman(object):

	def __init__(self, words):
		self.words = words
		self.currentWord = None
		self.usedWords = []
		self.wins = 0
		self.guessedChars = ''
		self.solutionArr = []
		self.correctIndecies = []
		self.lives = 10

	def clearScreen(self):
		system('cls' if osName == 'nt' else 'clear') 
		# cross platform clearing of terminal. nt is apparently windows

	def resetWords(self):
		self.words = self.usedWords
		self.usedWords = []

	def getRandomWord(self):
		if len(self.words) <= 0:
			self.resetWords()

		randIndex = randint( 0, len( self.words ) -1 )
		self.currentWord = self.words.pop(randIndex)
		self.usedWords.append(self.currentWord)

		for i in range(len(self.currentWord)): #init solution string as spaces
			self.solutionArr.append(' ')
		
		return self.currentWord

	def hasChar(self, char):
		index = self.currentWord.find(char)

		if index != -1: return True
		else: return False

	def getIndexOfChar(self, char):
		indexArr = []
		for i in range(len(self.currentWord)):
			if self.currentWord[i] == char:
				indexArr.append(i)

		return indexArr

	def isValid(self, guess):
		if len (guess) == 1: # only one char was entered
			if guess.isalpha(): # is an alpha char
				return True
			else: return False # something weird like a number

	def alreadyGuessed(self, guess):
		if guess not in self.guessedChars: return False
		else: return True

	def gameOver(self, endStatus):
		if endStatus == 'lost':
			print("Game Over. The word was {}".format(self.currentWord))

		elif endStatus == 'won':
			self.wins +=1
			print("Great job! You have guessed {} words correctly".format(self.wins))
		
		replay = input("Play Again? y/n\r\n")
		
		if replay != 'n': # if the user input is anything other than n start over
			self.start()

	def displayResults(self, errorMsg=''):
		bottomDashes = ''
		prettyguessed = ''


		if errorMsg != '': print(errorMsg) # if there is an error display it

		for i in range(len(self.guessedChars)):
			prettyguessed+= "{} ".format(self.guessedChars[i])

		for i in self.correctIndecies:
			self.solutionArr[i] = self.currentWord[i]

		for i in range(len(self.currentWord)):
			bottomDashes+= '_ '

		print(' '.join(self.solutionArr)) #print correctly guessed letters
		print(bottomDashes,"\r\n\r\n")
		print("Already Guessed: {}\r\n".format(prettyguessed))
		print("Lives Remaining: {}\r\n".format(self.lives))

	def processInput(self, guess):

		bottomDashes = ''
		self.guessedChars += guess


		if self.hasChar(guess):
			indexArr = self.getIndexOfChar(guess) # get list of int indexes of occurrances
			self.correctIndecies.extend(indexArr) # keep a list of the index of the chars that have been guessed..
			sorted(self.correctIndecies) # sort list to make the letters appear in order

			print("Correct!\r\n")
		
		else:
			self.lives-=1
			print("Incorrect!\r\n")

		self.displayResults()

		if self.lives > 0 and len(self.correctIndecies) < len(self.currentWord):
			self.getInput()
		elif self.lives > 0 and len(self.correctIndecies) == len(self.currentWord):
			self.gameOver('won')
		else: self.gameOver('lost')

	def getInput(self, invalidMessage="Input is invalid! Please enter only one letter"):
		guess = input("Please guess a letter\r\n").lower() # prompt user and convert it to lowercase as case doesn't matter
		self.clearScreen()
		if self.isValid(guess):
			if self.alreadyGuessed(guess):
				self.displayResults(errorMsg="That letter has already been guessed!")
				self.getInput() # input is valid but already guessed

			else: self.processInput(guess)
		else:
			self.displayResults(errorMsg=invalidMessage) # inform the user that they are stupid
			self.getInput(invalidMessage="Sorry you're having problems. Please try again.")

	def start(self):
		self.guessedChars = ''
		self.solutionArr = []
		self.correctIndecies = []
		self.lives = 10
		self.getRandomWord()
		self.clearScreen()
		self.displayResults()
		self.getInput()





### start ###
words = ["stuff", "things", "python", "keyboard", "laptop", "google", "linux", "visualization", "terminal", "files", "debian", "apache", "this", "iterations", "science", "hangman", "computation", "broncos", "mouse", "document"]

game = Hangman(words)
game.clearScreen()
game.start()