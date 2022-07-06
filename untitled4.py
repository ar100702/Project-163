from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Project 163")
root.geometry("400x00")
root.configure(background="plum1")

question1_radioButton = StringVar(value="0")

Question1=Label(root, text ="Do you experience shortness of breath during routine activities?", bg="ivory2", fg="gray5")
Question1.pack()
question1_r1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no")
question1_r2.pack()

question2_radioButton = StringVar(value="0")

Question2=Label(root, text ="Do you have swelling in feet/ ankles/ legs (shoes feel tighter) or abdomen?", bg="ivory2", fg="gray5")
Question2.pack()
question2_r1=Radiobutton(root, text = "yes", variable=question2_radioButton, value="yes")
question2_r1.pack()
question2_r2=Radiobutton(root, text = "no", variable=question2_radioButton, value="no")
question2_r2.pack()

question3_radioButton = StringVar(value="0")

Question3=Label(root, text ="Do you feel any of these symptoms - confusion, disorientation or loss of memory?", bg="ivory2", fg="gray5")
Question3.pack()
question3_r1=Radiobutton(root, text = "yes", variable=question3_radioButton, value="yes")
question3_r1.pack()
question3_r2=Radiobutton(root, text = "no", variable=question3_radioButton, value="no")
question3_r2.pack()

question4_radioButton = StringVar(value="0")

Question4=Label(root, text ="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?", bg="ivory2", fg="gray5")
Question4.pack()
question4_r1=Radiobutton(root, text = "yes", variable=question4_radioButton, value="yes")
question4_r1.pack()
question4_r2=Radiobutton(root, text = "no", variable=question4_radioButton, value="no")
question4_r2.pack()

def score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+10
        print(score)
        
    if question2_radioButton.get()=="yes":
        score = score+10
        print(score)
        
    if question3_radioButton.get()=="yes":
        score = score+10
        print(score)
        
    if question4_radioButton.get()=="yes":
        score = score+10
        print(score)
        
    if score <= 10:
        messagebox.showinfo("Report","You don't need to visit a doctor.")
    elif  score > 10 and score <= 30: 
        messagebox.showinfo("Report","You might perhaps have to visit a doctor")
    else :
        messagebox.showinfo("Report","I strongly advise you to visit a doctor")
        
btn = Button(root, text= "click me", command=score, bg="light goldenrod", fg="gray5")
btn.pack()



root.mainloop()