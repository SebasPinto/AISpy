from Tkinter import Tk, Label, Button, Frame
from PIL import ImageTk
import tts
from gtts import gTTS

class InitGUI:
    def __init__(self, master):
        self.master = master
        master.title("AI Spy")
        master.geometry('{}x{}'.format(800, 600))
        master.configure(background='#009688')
        
        parent = Frame(master)
        parent.configure(background='#009688')
        
        #Label Palabra
        self.Word = Label(parent, text = "Show me an object", fg="White", bg="#009688")
        self.Word.config(font=("Roboto bold", 44, "bold"))
        self.Word.pack(fill="x")
        
        #Boton para reproducir pronunciacion
        self.SayButton = Button(parent, command=self.speak, bg='#009688')
        self.iconImage = ImageTk.PhotoImage(file="img/speak-icon.png")
        self.SayButton.config(image = self.iconImage, width=100, height=100,
								highlightbackground="#009688", highlightthickness=0, relief='flat')
        self.SayButton.pack(pady=40)
        
        parent.pack(expand=True)  # same as expand=True
        
    def speak(self):
		self.Word.config(text="Penis")
		tts.greet_thread("This is a test")

root = Tk()
gui = InitGUI(root)
root.resizable(width=False, height=False)
root.mainloop()
