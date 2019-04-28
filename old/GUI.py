import Tkinter,tkFileDialog,tkMessageBox

def browse_button():
    global folder_path
    filename = tkFileDialog.askdirectory()
    folder_path.set(filename)
    print(filename)

def say_it():
    if txt2voiceBox.get("1.0", Tkinter.END)=="\n":
        tkMessageBox.showinfo("Error", "The text box is empty!")
    else:
        print("No")

def about():
    tkMessageBox.showinfo("About", "I don't know yet.")

def credits():
    tkMessageBox.showinfo("Credits", "It's only me for now.")

root = Tkinter.Tk()
root.title("Accessibility")
frame = Tkinter.Frame(root)
frame.pack()

accessibility = Tkinter.Label(frame, 
                   text="\nACCESSIBILITY APPLICATION\n",
                   font='Helvetica 14 bold', 
                   fg="black")
accessibility.pack()

img2txtButton = Tkinter.Button(frame, 
                   text="Read words from an Image", 
                   fg="red",
                   command=browse_button)
img2txtButton.pack()


img2txtBox = Tkinter.Text(frame, height=2, width=40)
img2txtBox.pack()

voice2txtButton = Tkinter.Button(frame, 
                   text="Listen to words and display it into Text", 
                   fg="green",
                   command=browse_button)
voice2txtButton.pack()

voice2txtBox = Tkinter.Text(frame, height=2, width=40)
voice2txtBox.pack()

txt2voiceButton = Tkinter.Button(frame, 
                   text="Read Text with a Voice", 
                   fg="blue",
                   command=say_it)
txt2voiceButton.pack()

txt2voiceBox = Tkinter.Text(frame, height=2, width=40)
txt2voiceBox.pack()


quitButton = Tkinter.Button(frame, 
                   text="Quit", 
                   fg="black",
                   command=quit)
quitButton.pack(side=Tkinter.RIGHT)

creditsButton = Tkinter.Button(frame, 
                   text="Credits", 
                   fg="black",
                   command=credits)
creditsButton.pack(side=Tkinter.LEFT)

aboutButton = Tkinter.Button(frame, 
                   text="About", 
                   fg="black",
                   command=about)
aboutButton.pack(side=Tkinter.BOTTOM)

root.mainloop()
