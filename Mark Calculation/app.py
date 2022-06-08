import random
from tkinter import Tk, Label, Button, Entry


def main(k, n, passM):
    t = [i for i in range(1, 101)]
    q = random.sample(t, 10)
    ml = []
    ml_min = []
    for _ in range(n):
        a = random.sample(t, k)
        m = [i for i in q if i in a]
        ml.append(len(m) * 10)
        if len(m) * 10 < passM:
            ml_min.append(len(m) * 10)
    return f"\nSkill: {k}%\nNo.of students: {n}\nPass Mark: {passM}\nMax: {max(ml)}\nMin: {min(ml)}\nAverage: {sum(ml)/len(ml)}\nNo.of Fail: {len(ml_min)}"


win = Tk()
win.geometry("1000x600")
# win.attributes('-fullscreen', True)
Label(text="Skill Percent:", font=("TimesNewRoman", 20, "bold")).pack()
e1 = Entry(font=("TimesNewRoman", 20, "bold"))
e1.pack()
Label(text="No.of Students:", font=("TimesNewRoman", 20, "bold")).pack()
e2 = Entry(font=("TimesNewRoman", 20, "bold"))
e2.pack()
Label(text="Pass mark:", font=("TimesNewRoman", 20, "bold")).pack()
e3 = Entry(font=("TimesNewRoman", 20, "bold"))
e3.pack()


def main1():
    l.configure(text=main(int(e1.get()), int(e2.get()), int(e3.get())))


Button(
    text="Submit", font=("TimesNewRoman", 20, "bold"), command=main1, bg="#00FF00"
).pack()
l = Label(text="", font=("TimesNewRoman", 20, "italic"))
l.pack()
win.mainloop()
