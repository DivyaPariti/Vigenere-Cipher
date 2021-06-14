# import tkinter module
from tkinter import *

# import other necessery modules
import random
import time
import datetime

# creating root object
root = Tk()

# defining size of window
root.geometry("950x600")

# setting up the title of window
root.title("Message Encryption and Decryption")

Tops = Frame(root, width = 1600, relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root, width = 800, height = 700,
							relief = SUNKEN)
f1.pack(side = LEFT)

# ==============================================
#				 TIME
# ==============================================
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font = ('georgia', 50, 'bold'),
		text = "SECRET MESSAGING",
					fg = "darkslategray", bd = 10, anchor='w')
					
lblInfo.grid(row = 0, column = 0)

lblInfo = Label(Tops, font=('georgia', 18, 'bold'),
			text = localtime, fg = "lemonchiffon4",
						anchor = 'w')
						
lblInfo.grid(row = 1, column = 0)

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

# exit function
def qExit():
	root.destroy()

# Function to reset the window
def Reset():
	rand.set("")
	Msg.set("")
	key.set("")
	mode.set("")
	Result.set("")


# name
lblReference = Label(f1, font = ('times', 16, 'bold'),
				text = "Name", bd = 16, anchor = "w")
				
lblReference.grid(row = 0, column = 0)

txtReference = Entry(f1, font = ('helvetica', 16, 'bold'),
			textvariable = rand, bd = 5, insertwidth = 4,
						bg = "seashell2", justify = 'left')
						
txtReference.grid(row = 0, column = 1)

# message
lblMsg = Label(f1, font = ('times', 16, 'bold'),
		text = "Message", bd = 16, anchor = "w")
		
lblMsg.grid(row = 1, column = 0)

txtMsg = Entry(f1, font = ('helvetica', 16, 'bold'),
		textvariable = Msg, bd = 5, insertwidth = 4,
				bg = "seashell2", justify = 'left')
				
txtMsg.grid(row = 1, column = 1)

#key
lblkey = Label(f1, font = ('times', 16, 'bold'),
			text = "Key", bd = 16, anchor = "w")
			
lblkey.grid(row = 2, column = 0)

txtkey = Entry(f1, font = ('helvetica', 16, 'bold'),
		textvariable = key, bd = 5, insertwidth = 4,
				bg = "seashell2", justify = 'left')
				
txtkey.grid(row = 2, column = 1)

#mode
lblmode = Label(f1, font = ('times', 16, 'bold'),
		text = "Encryption/Decryption", bd = 16, anchor = "w")
								
lblmode.grid(row = 3, column = 0)

txtmode = Entry(f1, font = ('helvetica', 16, 'bold'),
		textvariable = mode, bd = 5, insertwidth = 4,
				bg = "seashell2", justify = 'left')
					
txtmode.grid(row = 3, column = 1)

#result
lblService = Label(f1, font = ('times', 16, 'bold'),
			text = "Converted Message", bd = 16, anchor = "w")
			
lblService.grid(row = 1, column = 3)

txtService = Entry(f1, font = ('helvetica', 16, 'bold'),
			textvariable = Result, bd = 5, insertwidth = 4,
					bg = "seashell2", justify = 'left')
						
txtService.grid(row = 2, column = 3)

# Vigenère cipher
import base64

# Function to encode
def encode(key, clear):
	enc = []
	
	for i in range(len(clear)):
		key_c = key[i % len(key)]
		enc_c = chr((ord(clear[i]) +
					ord(key_c)) % 256)
					
		enc.append(enc_c)
		
	return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Function to decode
def decode(key, enc):
	dec = []
	
	enc = base64.urlsafe_b64decode(enc).decode()
	for i in range(len(enc)):
		key_c = key[i % len(key)]
		dec_c = chr((256 + ord(enc[i]) -
						ord(key_c)) % 256)
							
		dec.append(dec_c)
	return "".join(dec)


def Ref():
	print("Message= ", (Msg.get()))

	clear = Msg.get()
	k = key.get()
	m = mode.get()

	if (m == 'e'):
		Result.set(encode(k, clear))
	else:
		Result.set(decode(k, clear))

# Show message button
btnTotal = Button(f1, padx = 16, pady = 8, bd = 7, fg = "black",
						font = ('georgia', 15), width = 10,
					text = "Show Message", bg = "mistyrose3",
						command = Ref).grid(row = 7, column = 1)

# Reset button
btnReset = Button(f1, padx = 16, pady = 8, bd = 7,
				fg = "black", font = ('georgia', 15),
					width = 5, text = "Reset", bg = "burlywood4",
				command = Reset).grid(row = 7, column = 2)

# Exit button
btnExit = Button(f1, padx = 16, pady = 8, bd = 7,
				fg = "black", font = ('georgia', 15),
					width = 5, text = "Exit", bg = "grey",
				command = qExit).grid(row = 7, column = 3)

# keeps window alive
root.mainloop()
