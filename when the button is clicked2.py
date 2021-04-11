import tkinter 
from tkinter import messagebox 
top = tkinter.Tk ()  
#Width x Height 
#Hello World mesajı yazan Hello Python adlı pencere acılcak.
def helloCallBack ():   
    messagebox.showinfo ( "Hello Python", "Hello World") 
    
B = tkinter.Button (top, text ="Hello", command = helloCallBack ) 
#hello yazan butona basınca helloCallBack fonksiyonundakiler yapılcak.
B.pack () 
B.place ( bordermode ="outside", height=100, width=200) 
top.mainloop ()