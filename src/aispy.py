from Tkinter import Tk, Label, Button, Frame
from PIL import ImageTk
import tts
import visionEnglishModule
from gtts import gTTS

class InitGUI:
	def __init__(self, master):
		self.master = master
		master.title("AI Spy")
		master.geometry('{}x{}'.format(800, 600))
		master.configure(background='#03A9F4')
		

		parent = Frame(master)
		parent.configure(background='#03A9F4')
		
		#Label Titulo
		self.Title = Label(parent, text = "Show me an object", fg="White", bg="#03A9F4")
		self.Title.config(font=("Roboto bold", 44, "bold"))
		self.Title.pack(fill="x", pady=40)


		#Label Palabra
		self.Word = Label(parent, text = "", fg="White", bg="#03A9F4")
		self.Word.config(font=("Roboto bold", 44, "bold"))
		self.Word.pack(fill="x")

		#Boton para reproducir pronunciacion
		self.SayButton = Button(parent, command=self.speak, bg='#03A9F4')
		self.iconImage = ImageTk.PhotoImage(file="img/speak-icon.png")
		self.SayButton.config(image = self.iconImage, width=100, height=100,
		highlightbackground="#03A9F4", highlightthickness=0, relief='flat')
		self.SayButton.pack(pady=40)

		parent.pack(expand=True)  # same as expand=True
		master.after(1000, self.see)

	def speak(self):
		word = self.Word.cget("text")
		tts.greet_thread(word)

	def setWord(self, word):
		self.Word.config(text=word)

	def see(self):
		word = visionEnglishModule.detectImage('http://192.168.1.53:8080/shot.jpg')
		self.setWord(word.title())
		self.master.after(1000, self.see)
		

root = Tk()
gui = InitGUI(root)
root.resizable(width=False, height=False)
root.mainloop()

