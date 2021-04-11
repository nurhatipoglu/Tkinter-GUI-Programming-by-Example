import tkinter
def main():
    # Create a root window
    root = tkinter.Tk ()
    # create a button widget
    button = tkinter.Button ( root , text="Click Me")
    #pack() komutu ile ekranda gözükmesini sağlıyoruz.
    button.pack ()
    # Call the event loop
    root.mainloop()
    # Call the function main main()
main()