from tkinter import *
import random 


window =Tk()

window.title("Picnic Bag")
window.geometry("500x500")

l1 = Label(window, bg="GRAY")
l2 =    Label(window , bg = "PINK")
l3 = Label(window   )


l1.place(relx= 0.5, rely =0.5, anchor = CENTER)
l2.place(relx= 0.5, rely =0.6, anchor = CENTER)

def randomList():
    numbers = random.sample(range(1,7), random.randint(1,7))
    l1['text'] = "Random list Number :" + str(numbers)
    numbers.sort()
    l2['text'] = "Sorted Number :" + str(numbers)



btn = Button(window , text = "Genrate Random Number List" , command =randomList )
btn.place(relx = 0.5, rely= 0.4, anchor = CENTER)

window.mainloop()