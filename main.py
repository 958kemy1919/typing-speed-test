from tkinter import *
from random import randint
from math import floor
 
texts = {
    "text_1": "The fall of the Western Roman Empire (also called the fall of the Roman Empire or the fall of Rome) was the loss of central political control in the Western Roman Empire, a process in which the Empire failed to enforce its rule, and its vast territory was divided into several successor polities. The Roman Empire lost the strengths that had allowed it to exercise effective control over its Western provinces; modern historians posit factors including the effectiveness and numbers of the army, the health and numbers of the Roman population, the strength of the economy, the competence of the emperors, the internal struggles for power, the religious changes of the period, and the efficiency of the civil administration.Increasing pressure from invading barbarians outside Roman culture also contributed greatly to the collapse. Climatic changes and both endemic and epidemic disease drove many of these immediate factors. The reasons for the collapse are major subjects of the historiography of the ancient world and they inform much modern discourse on state failure.",
    "text_2": "The fall of Constantinople, also known as the conquest of Constantinople, was the capture of the capital of the Byzantine Empire by the Ottoman Empire. The city was captured on 29 May 1453 as part of the culmination of a 53-day siege which had begun on 6 April.The attacking Ottoman Army, which significantly outnumbered Constantinople's defenders, was commanded by the 21-year-old Sultan Mehmed II (later nicknamed 'the Conqueror'), while the Byzantine army was led by Emperor Constantine XI Palaiologos. After conquering the city, Mehmed II made Constantinople the new Ottoman capital, replacing Adrianople.The conquest of Constantinople and the fall of the Byzantine Empire was a watershed of the Late Middle Ages,marking the effective end of the last remains of the Roman Empire, a state which began in roughly 27 BC and had lasted nearly 1500 years.",
    "text_3": "The Napoleonic Wars were a series of major global conflicts pitting the French Empire and its allies, led by Napoleon I, against a fluctuating array of European states formed into various coalitions. It produced a period of French domination over most of continental Europe. The wars stemmed from the unresolved disputes associated with the French Revolution and the French Revolutionary Wars consisting of the War of the First Coalition and the War of the Second Coalition (1798–1802). The Napoleonic Wars are often described as five conflicts, each termed after the coalition that fought Napoleon: the Third Coalition, the Fourth, the Fifth, the Sixth, and the Seventh plus the Peninsular War and the French invasion of Russia (1812).After the end of the Napoleonic Wars, there was a period of relative peace in continental Europe, lasting until the Crimean War in 1853.",
    "text_4": "The wars of Alexander the Great were a series of conquests that were carried out by Alexander III of Macedon from 336 BC to 323 BC. They began with battles against the Achaemenid Persian Empire, then under the rule of Darius III of Persia. After Alexander's chain of victories against Achaemenid Persia, he began a campaign against local chieftains and warlords that were stretched as far from Greece as the region of Punjab in South Asia. By the time of his death, he ruled over most regions of Greece and the conquered Achaemenid Empire (including much of Persian Egypt); he did not, however, manage to conquer the Indian subcontinent in its entirety as was his initial plan. Despite his military accomplishments, Alexander did not provide any stable alternative to the rule of the Achaemenid Empire, and his untimely death threw the vast territories he conquered into a series of civil wars, commonly known as the Wars of the Diadochi."
}
 
sec = 64
 
def restart_timer():
    global sec,timer
    sec = 64
    window.after_cancel(timer)
    my_text_entry.config(state="normal")
    my_text_entry.delete(0,END)
    canvas.itemconfig(score_text,text="")
    my_text_entry.config(state="disabled")
    canvas.itemconfig(timer_text,text="Timer: 1:00",fill="black")
 
def start_timer():
    global sec
    sec -= 1
    my_text_entry.config(state="normal")
    count_down(sec)
 
def count_down(count):
    global sec,timer,text_to_type
    min_count = floor(sec / 60)
    sec_count = sec % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
 
    if count > 60:
        sec_ready = count % 60
        canvas.itemconfig(timer_text, text=f"Get ready: {sec_ready}",fill="red")
        timer = window.after(1000,start_timer)
    elif count > 0:
        canvas.itemconfig(timer_text, text=f"Time left: {min_count}:{sec_count}",fill="black")
        timer = window.after(1000,start_timer)
    else:
        canvas.itemconfig(timer_text, text=f"Time is Up: 00:00")
        my_text_entry.config(state="disabled")
        typed_text = my_text_entry.get()
        cpm_wpm = words_per_minute(typed_text,text_to_type)
        if cpm_wpm[1] != cpm_wpm[2]:
            canvas.itemconfig(score_text,text=f"Your Score: {cpm_wpm[1]} WPM, (that is {cpm_wpm[0]} CPM). In reality you typed {cpm_wpm[2]} words and {cpm_wpm[3]} characters, but you made some mistakes")
        else:
            canvas.itemconfig(score_text, text=f"Your Score: {cpm_wpm[1]} WPM, (that is {cpm_wpm[0]} CPM)")
 
 
def words_per_minute(typed_text,text_to_type):
    number_of_words = 0
    number_of_characters = 0
    all_words = 0
    all_chars = 0
    text_to_type_list = text_to_type.split(" ")
    typed_text_list = typed_text.split(" ")
    for i in range(0,len(typed_text_list)):
        all_words += 1
        all_chars += len(typed_text_list[i])
        if typed_text_list[i] == text_to_type_list[i]:
            number_of_words += 1
            number_of_characters += len(typed_text_list[i])
    num_chars_words = (number_of_characters,number_of_words,all_words,all_chars)
    return num_chars_words
 
 
window = Tk()
window.title("Typing Speed Test")
window.config(padx=30,pady=30,bg="#1F8A70")
 
bg_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800,height=526,highlightthickness=0,bg="#1F8A70")
canvas.create_image(400,263,image=bg_img)
title_text = canvas.create_text(400,50,text="TYPING SPEED TEST",font=("Arial",30,"italic","bold"),fill="black")
subtitle_text = canvas.create_text(400,100,text="How fast are your fingers? Do the one-minute typing test to find out! Press the space bar after each word. At the end, you'll get your typing speed in CPM and WPM. Good luck!",font=("Arial",12),width=600)
timer_text = canvas.create_text(400,150,text="Timer: 1:00",font=("Arial",50,"italic","bold"),fill="black")
score_text = canvas.create_text(400,230,text="",fill="white",font=("Arial",15,"bold"),width=700)
text_to_type = texts[f"text_{randint(1, 4)}"]
text = canvas.create_text(400,385,text=text_to_type,font=("Arial",13,"bold"),width=750)
canvas.grid(column=0,row=0,columnspan=2)
 
start_timer_button = Button(text="Start timer",command=start_timer)
start_timer_button.grid(column=0,row=2)
 
restart_timer_button = Button(text="Restart timer",command=restart_timer)
restart_timer_button.grid(column=1,row=2)
 
my_text_entry = Entry(bg="#1F8A70",highlightthickness=0,fg="white",width=120,state="disabled")
my_text_entry.grid(column=0,row=3,columnspan=2)
 
window.mainloop()
