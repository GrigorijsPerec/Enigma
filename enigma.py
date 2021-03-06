from tkinter import *
from PIL import Image, ImageTk
import string


abc = list(string.ascii_uppercase)

# rotor 3
class thirdRotor:
	def __init__(self):
		self.dictionary = [(1,3),(5,20),(17,2),(2,15),(14,18),(8,1),(12,13),(18,10),(9,5),(13,24),(3,19),(23,6),(6,17),(16,12),(25,21),(15,26),(4,8),(10,25),(21,9),(26,14),(22,11),(19,16),(11,23),(24,7),(7,4),(20,22)]
		self.code_position = 0
		self.decode_position = 0

	def code(self, input, direction):
		self.code_position = self.code_position + 1
		if self.code_position > 26:
			self.code_position = self.code_position - 26
		search = self.cykleSearch((input + self.code_position))
		result = 0
		for i in range(0,26):
			if self.dictionary[i][switchDirection(direction)] == search:
				result = self.dictionary[i][direction]
		return result

	def cykleSearch(self, search):
		while search > 26:
			search = search - 26
		return search

class stator:
	def __init__(self):
		self.dictionary = [(5,24),(14,19),(9,23),(26,13),(22,7),(20,12),(17,1),(21,25),(16,2),(18,3),(11,8),(10,6),(4,15),(24,5),(19,14),(23,9),(13,26),(7,22),(12,20),(1,17),(25,21),(2,16),(3,18),(8,11),(6,10),(15,4)]

	def find(self, input):
		for i in range(0,26):
			if self.dictionary[i][0] == input:
				return self.dictionary[i][1]
# rotor 2
class secondRotor:
	def __init__(self):
		self.dictionary = [(18,8),(4,6),(13,5),(23,24),(12,25),(19,21),(2,14),(24,16),(3,19),(7,1),(10,23),(6,2),(20,13),(15,12),(14,10),(5,20),(17,3),(16,17),(9,22),(25,15),(11,18),(8,26),(1,7),(21,9),(22,11),(26,4)]
		self.code_position = 0

	def code(self, input, direction):
		self.code_position = self.code_position + 1
		real_position = self.code_position

		search = self.cykleSearch(input + self.cycleItterator(real_position))
		result = 0
		for i in range(0,26):
			if self.dictionary[i][switchDirection(direction)] == search:
				result = self.dictionary[i][direction]
		return result


	def cycleItterator(self, itterator):
		while itterator > 26:
			itterator = itterator // 26
		return itterator

	def cykleSearch(self, search):
		while search > 26:
			search = search - 26
		return search


# rotor 1
class firstRotor:
	def __init__(self):
		self.dictionary = [(24,19),(19,20),(5,13),(6,7),(2,5),(15,25),(8,17),(9,4),(20,10),(12,11),(25,23),(11,6),(18,8),(23,2),(21,16),(16,26),(26,1),(7,21),(3,3),(4,12),(14,15),(22,9),(17,24),(13,22),(1,14),(10,18)]


	def code(self, input, direction):
		self.code_position = self.code_position + 1
		real_position = self.code_position

		search = self.cykleSearch(input + self.cycleItteratorSqrt(real_position))
		result = 0
		for i in range(0,26):
			if self.dictionary[i][switchDirection(direction)] == search:
				result = self.dictionary[i][direction]
		return result

	def cycleItteratorSqrt(self, itterator):
		if itterator // (26*26) > 1:
			while itterator > (26*26):
				itterator = itterator // (26*26)
		else:
			itterator = itterator // (26*26)
		return itterator

	def cykleSearch(self, search):
		while search > 26:
			search = search - 26
		return search


rotor_3 = thirdRotor()
rotor_2 = secondRotor()
rotor_1 = firstRotor()
stator = stator()

def crypt_word(word):
	result = list()
	for letter in word:
		result.append(codeByRotors(letter))
	return result


def codeByRotors(letter):
	number = abc.index(letter) + 1
	thirdRtl = rotor_3.code(number, 0)
	secondRtl = rotor_2.code(thirdRtl, 0)
	firstRtl = rotor_1.code(secondRtl, 0)
	statorRtl = stator.find(firstRtl)
	firstLtr = rotor_1.code(statorRtl, 1)
	secondLtr = rotor_2.code(firstLtr, 1)
	thirdLtr = rotor_3.code(secondLtr, 1)
	result = thirdLtr

	return abc[result - 1]


def switchDirection(direction):
	return 0 if direction == 1 else 1

def configureMachine(frtRrStart, sndRrStart, trdRrStart):
	rotor_1.code_position = frtRrStart
	rotor_2.code_position = sndRrStart
	rotor_3.code_position = trdRrStart


def runMachine(stringByWords):
	result = ''
	strg = ''
	for word in stringByWords:
		crypted = crypt_word(word)
		result += strg.join(crypted)
		result += ' '
	return result


def process(frtRrStart, sndRrStart, trdRrStart, inputString):
	inputString = inputString.upper()
	stringByWords = inputString.split()
	configureMachine(int(frtRrStart), int(sndRrStart), int(trdRrStart))
	result = runMachine(stringByWords)
	return result




#gui
root = Tk()
root.geometry("310x430")
root.title("Enigma Simulator 3000")
root['bg'] = '#FF8F29'

#startentry
startentry = Entry(root, bg='#F7B237', justify=CENTER)
startentry.place(x = 10,y = 10, width=285, height=115)

#company logo
clogo = ImageTk.PhotoImage(Image.open("companylogo.jpg").resize((120, 120)))
logo = Label(root, image = clogo)
logo.place(x=10, y = 150)


def Rotor_add(rotor: Label, count: int = 1):
    rotor.configure(text=rotor["text"] + count)

def Rotor_reset():
    rotor1.configure(text = 0)
    rotor2.configure(text = 0)
    rotor3.configure(text = 0)


#rotters
rotor3btn1 = Button(root, text='<', command=lambda: Rotor_add(rotor3, -1))
rotor3btn2 = Button(root, text='>', command=lambda: Rotor_add(rotor3))

rotor2btn1 = Button(root, text='<', command=lambda: Rotor_add(rotor2, -1))
rotor2btn2 = Button(root, text='>', command=lambda: Rotor_add(rotor2))

rotor1btn1 = Button(root, text='<', command=lambda: Rotor_add(rotor1, -1))
rotor1btn2 = Button(root, text='>', command=lambda: Rotor_add(rotor1))

rotor3btn1.place(x=185, y=250)
rotor3btn2.place(x=250, y=250)
rotor2btn1.place(x=185, y=210)
rotor2btn2.place(x=250, y=210)
rotor1btn1.place(x=185, y=170)
rotor1btn2.place(x=250, y=170)

#

#rotors values

rotor3 = Label(root, fg='black', bg='#FF8F29', text=0)
rotor3.place(x=220, y=250)
rotor2 = Label(root, fg='black', bg='#FF8F29', text=0)
rotor2.place(x=220, y=210)
rotor1 = Label(root, fg='black', bg='#FF8F29', text=0)
rotor1.place(x=220, y=170)

#endentry
endentry = Text(root, bg='#F7B237')
endentry.place(x = 10,y = 305, width=285, height=115)

def Enigma_Start():
    inputString = startentry.get()
    rotor1_get = rotor1['text']
    rotor2_get = rotor2['text']
    rotor3_get = rotor3['text']
    print(rotor1_get,rotor2_get,rotor3_get,inputString)
    result_all = process(rotor1_get,rotor2_get,rotor3_get, inputString)
    endentry.delete(CURRENT, END)
    endentry.insert(END ,result_all)

EncryptBtn = Button(root, text='Encrypt', command = lambda: Enigma_Start())
EncryptBtn.place(x=185, y = 135)
ResetBtn = Button(root, text='Reset', command = lambda: Rotor_reset())
ResetBtn.place(x=245, y = 135)


root.mainloop()
