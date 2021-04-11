from tkinter import * # Import tkinter
    
#FRAME, ekranda dikdörtgen bir alandır. FRAME, karmaşık widget'ları uygulamak için temel bir sınıf
# olarak da kullanılabilir. Bu widget bir grup düzenlemek için kullanılır.
#Scrollbar widget'ı, listbox, text ve canvas gibi diğer widget'ların içeriğini aşağı kaydırmak için
# kullanılır. Bununla birlikte, giriş widget'ına Scrollbar da oluşturabiliriz.

class ScrollText:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Scroll Text Demo") # Set title
        
        frame1 = Frame(window)
        frame1.pack()
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side = RIGHT, fill = Y)
        text = Text(frame1, width = 40, height = 10, wrap = WORD, 
                    yscrollcommand = scrollbar.set)
        text.pack()
        scrollbar.config(command = text.yview)
        
        window.mainloop() # Create an event loop

ScrollText() # Create GUI