import tkinter
from tkinter import *

master = Tk()
master.title("Roommate Match")
master.wm_iconbitmap("Troll_Face.ico")
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
Label(master, text="Age").grid(row=2)
Label(master, text="What state are you from? (please enter state abbreviation)"
      ).grid(row=3)
Label(master, text="Leave a personal message, or brief description of yourself"
      ).grid(row=4)
Label(master, text="Do you have any dietary restirctions be it from allergies or personal choice?").grid(row=5)
Label(master, text="Do you smoke?").grid(row=6)
Label(master, text="At about what hour do you usually go to sleep?").grid(row=7)
Label(master, text="At about what hour do you most often wake up?").grid(row=8)
Label(master, text="If you workout, about how many hours a week do you spend doing so?").grid(row=9)
Label(master, text="Which descrbe you best?").grid(row=10)
Label(master, text="Are you a light sleeper?").grid(row=11)
Label(master, text="Do you have and/or want pets?").grid(row=12)
Label(master, text="Do you have a significant other? If no, do you plan on having over night guests of any kind?").grid(row=13) 
Label(master, text="Which do you prefer?").grid(row=14)
Label(master, text="Do you have a significant other?").grid(row=15)
Label(master, text="Do you mind if your roommate has frequent over night guests?").grid(row=16)
Label(master, text="Do you mind if your roommate has frequent day time guests? If so what is an approproate time you want guest to leave?").grid(row=17)
Label(master, text="Are you willing/expecting to share personal items such as clothes, cleaning supplies, etc?").grid(row=18)
Label(master, text="Are you willing to split the grocery bill? If Yes, how much do you usually spend on groceries a month?").grid(row=19)
Label(master, text="Are you willing to split chores in shared living spaces?").grid(row=20)
Label(master, text="Living preference?").grid(row=21)
Label(master, text="'How much are you looking to spend on rent, including utilities, per month?'").grid(row=22)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e10 = Entry(master)
e11 = Entry(master)
e12 = Entry(master)
e13 = Entry(master)
e14 = Entry(master)
e15 = Entry(master)
e16 = Entry(master)
e17 = Entry(master)
e18 = Entry(master)
e19 = Entry(master)
e20 = Entry(master)
e21 = Entry(master)
e22 = Entry(master)
e23 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

master.mainloop()

