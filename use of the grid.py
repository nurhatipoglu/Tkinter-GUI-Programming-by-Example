import tkinter as tk
colours = ['red','green','orange','white','yellow','blue '] 
r = 0
for c in colours :   
    tk.Label (text=c, relief= tk.RIDGE , width=15).grid(row= r,column =0) 
    #Label:İçine metni veya görüntüleri yerleştirmemizi sağlar
    tk.Entry ( bg =c, relief= tk.SUNKEN , width=10).grid(row= r,column =1) 
    #Entry: içini, boyayabileceğimiz, yazı yazabileceğimiz boş kutu.
    #grid: yapılacak islemlerin yerleşimi.
    r = r + 1 
    tk.mainloop ()