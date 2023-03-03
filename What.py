import tkinter as tt
import random
from tkinter import messagebox


window = tt.Tk()
window.resizable(width=False, height=False)

def add_idea():
    value = EnterText.get()
    if value != '':
        with open("Idea.txt", "a+", encoding="utf-8") as file1:
            file1.write(value+"\n")
        EnterText.delete(0, 'end')
    else:
        tt.messagebox.showinfo("Ошибка ввода!", ("Пустое поле ввода!"))

def give_idea():
    with open("Idea.txt", "r", encoding="utf-8") as file2:
        line = file2.readlines()
        tt.messagebox.showinfo("Идея", (random.choice(line)))

def enter_key(e):
    add_idea()

# Название окна
window.title("Идеи")
window.geometry('720x360')
window['bg'] = "black"

# Текст приложения
advice_idea = tt.Label(window, text='Добавить идею: ', font=('Times New Roman', 20), fg='lime', bg='black')
advice_idea.place(x=100, y=20)

# Окно ввода
EnterText = tt.Entry(fg="black", width=45)
EnterText.place(x=220, y=65)

# Кнопка
bottom_of_idea = tt.Button(window, text="Добавить", command=add_idea, width="40", height="2", fg="black", bg="white")
bottom_of_idea.place(x=210, y=110)

window.bind('<Return>', bottom_of_idea)

# Текст приложения
return_idea = tt.Label(window, text='Выдать идею: ', font=('Times New Roman', 20), fg='lime', bg='black')
return_idea.place(x=100, y=170)

# Кнопка
bottom_of_id = tt.Button(window, text="Предложить", command=give_idea, width="40", height="2", fg="black", bg="white")
bottom_of_id.place(x=210, y=220)

window.mainloop()
