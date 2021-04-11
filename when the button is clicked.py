import tkinter
from tkinter import messagebox

#callback function
#butona basınca adı 'Response' olan içinde  'You have clicked the button' yazan mesaj kutusu oluşur.
def do_something():
    #the following line of code show messagebox
    messagebox.showinfo('Response', 'You have clicked the button')

def main():
    # Create a root window
    root = tkinter.Tk()
    # create a button widget
    button = tkinter.Button(root, text="Click Me", command = do_something)
    #command: butına basınca olacak işlem do_something olmasını sağlar.
    button.pack()
    # Call the event loop
    root.mainloop()

# Call the function main
main()