#import whatever we need

Settings=[]
#LOAD OUR SETTINGS
character="Kendrick"
try:
    Settings_file = open('Settings.txt')
    all_the_lines = Settings_file.readlines()
    for i in all_the_lines:
        Settings.append(i)
    print(Settings,":Settings")
    x=int(Settings[0])
    y=int(Settings[1])
    print(x,y)
    Settings_file.close()
except:
    #Settings = open("Settings.txt", "w")
    print()
    x=40
    y=760






import sys
from pathlib import Path
from tkinter import *
import threading
import os
from tkinter import ttk
import tkinter as tk
import pyperclip as pc
from pathlib import Path
from tkinter import messagebox
import time
import string
import random

moving=False

#variableeeeeesss

infofile= open('readme.txt','r')

#my filessssss
try:
    with open('readme.txt') as f:
        lines = f.readlines()
except:
    with open('readme.txt', 'w') as f:
        f.write('')

#variablesss contd
recent=[]
letters=[i for i in string.ascii_lowercase]

letters2=[i for i in string.ascii_uppercase]
numbers=["1","2","3","4","5","6","7","8","9","0"]
characters=["!","@","#","$"]
specialchars=["%","^","&","*","(",")","-","=","+"]
words=[]
clipboaard=[]
psswords=[]
window = Tk()
window.geometry('100x100+'+str(x)+'+'+str(y))
impath ='~//Documents//VirtualAssistant//files//Assistant//'
impath='Files/Assistant/'
print(impath)
TimerActive=False
window.resizable(0,0)

window.protocol("WM_DELETE_WINDOW", print(""))

#password generating func



def accept_pos():
    print
    (""
    )
















def gen_password(craters,passtype):
    passcode=""
    print(passtype)
    rice=1
    for i in range(0,craters):
        if passtype==1:
            rice=random.randint(1,5)
        if passtype==2:
            rice=random.randint(1,6)
        if passtype==3:
            rice=random.randint(1,7)
        if passtype==4:
            rice=random.randint(1,8)
        if passtype==5:
            rice=random.randint(1,9)
        if passtype==6:
            rice=random.randint(1,10)
        if rice==1 or rice==2:    
            passcode=passcode+random.choice(letters)
        if rice==3 or rice==4:
            passcode=passcode+random.choice(letters2)
        if rice==5 or rice==6 or rice==9:
            passcode=passcode+random.choice(numbers)
        if rice==7 or rice==8 or rice==10:
            passcode=passcode+random.choice(characters)
    pc.copy(passcode)
    print(passcode)


#info saving func
    
def save_info(loading):
    if loading ==False:
        with open('readme.txt', 'a+') as f:
            f.write("\n")
            f.write(pc.paste())
        clipboaard.append(pc.paste())
        print(pc.paste())
    var=pc.paste()
    recent.clear()
    recent.append((pc.paste()))
    first_char=var
    if len(var)>24:
        first_char=""
        for i in range(0, 24):
            first_char = first_char + var[i]
        first_char=first_char+'...'
    
    infomenu.add_command(label=first_char,command=lambda:copy_info(var),background="green")


def copy_info(info):
    pc.copy(info)

def copy_recent_info():
    pc.copy(recent[0])


def delete_recent_info():
    clipboaard.remove(recent[0])
    print(clipboaard)

def clear_info():
    for x in clipboaard:
        clipboaard.remove(x)
    infomenu.delete(0,"end")
    file = open("readme.txt","r+")
    file. truncate(0)
    file. close()


#managing our timee
def custom_timer():
    Timr=tk.Tk()
    canvas1 = tk.Canvas(Timr, width = 125, height = 123)
    canvas1.grid()
    hh= tk.StringVar(Timr,value='0')
    mm= tk.StringVar(Timr,value='0')
    ss= tk.StringVar(Timr,value='0')
    hours = tk.Entry(Timr,width=4,textvariable=hh)
    minutes = tk.Entry(Timr,width=4,textvariable=mm)
    seconds = tk.Entry(Timr,width=4,textvariable=ss)
    canvas1.create_window(20, 14, window=hours)  
    canvas1.create_window(60, 14, window=minutes)    
    canvas1.create_window(100, 14, window=seconds)
    option_var=tk.StringVar(Timr,value='Disturbing')
    button1 = tk.Button(Timr,text='Start Timer!',command=lambda:timer(hh.get(),mm.get(),ss.get(),option_var.get()))
    canvas1.create_window(60, 70, window=button1)
    alert_types=('Disturbing','Loud','noise','quiet')
    paddings={'padx':5,'pady':5}
    option_menu=ttk.OptionMenu(Timr,option_var,alert_types[0],*alert_types)
    option_menu.grid(column=3,row=0,sticky=tk.W,**paddings)
    label=ttk.Label(Timr, text='type of alarm: ')
    label.grid(column=2,row=0,sticky=tk.W, **paddings)

    output_label = ttk.Label(Timr, foreground='red')
    output_label.grid(column=0, row=1, sticky=tk.W, **paddings)

    


def timer(hour,minute,second,alerttype):
    timer=threading.Timer((int(hour)*(360))+(int(minute)*(60))+int(second),alertwindow,args=[2,"Your Time is now Up"])
    print((int(hour)*(360))+(int(minute)*(60))+int(second))
    timer.start()
    print(alerttype)

    

def alertwindow(attype,message):
    window = Tk()
    window.title("Welcome to TutorialsPoint")
    window.geometry('325x100')
    window.configure(background = "gray")
    ttk.Button(window, text="Snooze").grid(column=10) 
    ttk.Button(window, text="Dismiss").grid(column=10)
    window.mainloop()

    
def prnt(atype):
    print("your time is up")
    if atype == "Disturbing":
        alertwindow("Your timer is now up!")


        

#window config
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes("-topmost",0.98)
window.wm_attributes('-transparentcolor','black')
window.wm_attributes("white","black")

C = Canvas(window, height=90, width=90)
filename = PhotoImage(file = impath+'Kendrick.png')
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def changeface(name):
    print(name)
    character=name
    global background_label
    filename = PhotoImage(file = impath+name+'.png')
    background_label.configure(image=filename)
    background_label.image=filename

##########meeneueueueueueue
wordpath =Path('Files/Assistant').expanduser()
for (root, dirs, files) in os.walk(wordpath):
    print(files)
    ctrs=[]
    ctrs=files
    break
try:
    menuimage=tk.PhotoImage(file='Files/Assistant/'+ctrs[0])
    menuimage2=tk.PhotoImage(file='Files/Assistant/'+ctrs[1])
    menuimage3=tk.PhotoImage(file='Files/Assistant/'+ctrs[2])
    menuimage4=tk.PhotoImage(file='Files/Assistant/'+ctrs[3])
    menuimage5=tk.PhotoImage(file='Files/Assistant/'+ctrs[4])
    menuimage6=tk.PhotoImage(file='Files/Assistant/'+ctrs[5])
    menuimage7=tk.PhotoImage(file='Files/Assistant/'+ctrs[6])
    menuimage8=tk.PhotoImage(file='Files/Assistant/'+ctrs[7])
    menuimage9=tk.PhotoImage(file='Files/Assistant/'+ctrs[8])
    menuimage0=tk.PhotoImage(file='Files/Assistant/'+ctrs[9])
    menuimage0=tk.PhotoImage(file='Files/Assistant/'+ctrs[10])
    middle=tk.PhotoImage(file='middle.png')
except:
    pass



menu = Menu(window, tearoff = 0,selectcolor="#844344")

time_menu = Menu(menu, tearoff=0,activebackground="#844344",selectcolor="#844344")
time_menu.add_command(label='30 minutes',command=lambda:timer(0,30,0,"Disturbing"),background="#613943",foreground="red")
time_menu.add_command(label='5 seconds',command=lambda:timer(0,0,5,"Disturbing"),background="#613943")
time_menu.add_command(label='1 minute',command=lambda:timer(0,1,0,"Disturbing"),background="#613943")
time_menu.add_command(label='30 seconds',command=lambda:timer(0,0,30,"Disturbing"),background="#613943")
time_menu.add_command(label='5 minutes',command=lambda:timer(0,5,0,"Disturbing"),background="#613943")
time_menu.add_command(label='Custom',command=custom_timer,background="#613943")

menu.add_cascade(label ="Start a timer",menu=time_menu,background="#613943")
menu.add_command(label ="Set a Reminder",background="#613943")
menu.add_command(label ="Store Information",command=lambda:save_info(False),background="#613943")
menu.add_command(label="create music playlist",background="#613943")
menu.add_command(label ="Speak",background="#613943")
menu.add_separator(background="#613943")
menu.add_command(label ="Dismiss Assistant",command=lambda:sys.exit(1),background="#613943",accelerator="Control-Q")
#menu.add_checkbutton(label="eatme")

passmenu=Menu(menu,tearoff=0,activebackground="#844344")
sub_menu = Menu(menu, tearoff=0,selectcolor="#844344")
sub_menu.add_command(label='Position',command=lambda:change_wp(1),background="#613943")



char_menu = Menu(menu, tearoff=0,bd=0,selectcolor="#844344")
mended=[]
for i in ctrs:
    name=i.replace(".png","")
    mended.append(name)
try:
    char_menu.add_command(label='',command=lambda:changeface(ctrs[0].replace(".png","")),background="#613943",image=menuimage)
    char_menu.add_command(label='',command=lambda:changeface(ctrs[1].replace(".png","")),background="#613943",image=menuimage2)
    char_menu.add_command(label='',command=lambda:changeface(ctrs[2].replace(".png","")),background="#613943",image=menuimage3)
    char_menu.add_command(label='',command=lambda:changeface(ctrs[3].replace(".png","")),background="#613943",image=menuimage4)
    char_menu.add_command(label='',command=lambda:changeface(ctrs[4].replace(".png","")),background="#613943",image=menuimage5)
    char_menu.add_command(label='',command=lambda:changeface(ctrs[5].replace(".png","")),background="#613943",image=menuimage6)
    char_menu.add_command(label='',command=lambda:changeface(ctrs[6].replace(".png","")),background="#613943",image=menuimage7)
    char_menu.add_command(label='',command=lambda:changeface(ctrs[7].replace(".png","")),background="#613943",image=menuimage8)
    char_menu.add_command(label='',command=lambda:changeface(ctrs[8].replace(".png","")),background="#613943",image=menuimage9)
    char_menu.add_command(label='',command=lambda:changeface(ctrs[9].replace(".png","")),background="#613943",image=menuimage0)
    char_menu.add_command(label='',command=lambda:changeface(ctrs[10].replace(".png","")),background="#613943",image=menuimage0)
except:
    pass
sub_menu.add_cascade(label='Assistant', menu=char_menu,background="#613943")

print()
info_menu = Menu(menu, tearoff=0,selectcolor="#844344")
info_menu.add_command(label='Copy Last Info Stored',command=copy_recent_info)
info_menu.add_command(label='Delete Most recent Info Stored',command=delete_recent_info)
info_menu.add_command(label='Open all Info in File Explorer')
info_menu.entryconfig("Open all Info in File Explorer",state="disabled")
info_menu.add_command(label='Clear all info',command=clear_info)
info_menu.add_cascade(label="passwordmenu",menu=passmenu)

help_menu = Menu(menu, tearoff=0,selectcolor="#844344")
help_menu.add_command(label='README.MD',command=copy_recent_info)
help_menu.add_command(label='Website tutorial',command=delete_recent_info)
help_menu.add_command(label='Youtube tutorial')
help_menu.add_command(label="request feature")
help_menu.add_command(label='Uninstall')
infomenu=Menu(menu, tearoff=0)

info_menu.add_cascade(label='Info',menu=infomenu)

menu.add_cascade(
    label="Preferences",
    menu=sub_menu,background="#613943",activebackground="#844344"
)
menu.add_cascade(
    label="Help",
    menu=help_menu,background="#613943",activebackground="#844344"
)
menu.add_cascade(
    label="Stored Information",
    menu=info_menu,background="#613943",activebackground="#844344"
)



wordpath =Path('Files/Assistant/SB').expanduser()
for (root, dirs, files) in os.walk(wordpath):
    print(files)
    listy=files
    break




def passwordmenu(tions):
    changer=0
    for i in range(5,tions):
        for b in range(i,i+1):
            vae='c'+str(b)+'menyou'
            globals()[vae]=Menu(menu,tearoff=0)
            passmenu.add_cascade(label=str(i)+' characters',menu=globals()[vae])
            for c in range(1,7):
                globals()[vae].add_command(label="Security level: "+str(c),command= lambda: gen_password(i,c))

passwordmenu(8)



def do_popup(event):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()
def speak(event):
    wordpath ='~/Documents/VirtualAssistant/Files/Assistant/SB/'+random.choice(listy)
    popup=Toplevel(window)
    popup.geometry('96x96+'+str(window.winfo_x())+'+'+str(window.winfo_y()-90))
    filename = tk.PhotoImage(file = wordpath)
    popup.config(highlightbackground='black')
    Ce = Canvas(popup, height=110, width=110)
    popup.overrideredirect(True)
    background_label = Label(popup, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    popup.wm_attributes("-topmost",True)
    popup.wm_attributes('-transparentcolor','black')
    Ce.image=filename
    Ce.create_image(40,50,image=filename)
    Ce.pack()
    popup.after(2000, popup.destroy)




def loadinfo(num):
    for i in range(0,num):
        line = infofile.readline()
        clipboaard.append(line.strip())
        try:
            clipboaard.remove('')
        except:
            print("")
        if not line:
            break
        print(line.strip())
    print(len(clipboaard))
    for c in (clipboaard):
        pc.copy(c)
        save_info(True)
    




def change_wp():
    window.overrideredirect(False)
    
    
def up(event):
    global y    
    if moving==True:
        y=y-2
        window.geometry('100x100+'+str(x)+'+'+str(y))
        with open('Settings.txt', 'r') as file:
            data = file.readlines()

        data[1] = str(int(data[1])-2)+'\n'

        with open('Settings.txt', 'w') as file:
            file.writelines(data)



    
def down(event):
    global y
    if moving==True:
        y=y+2
        window.geometry('100x100+'+str(x)+'+'+str(y))
        with open('Settings.txt', 'r') as file:
            data = file.readlines()

        data[1] = str(int(data[1])+2)+'\n'

        with open('Settings.txt', 'w') as file:
            file.writelines(data)

    
def left(event):
    global x
    if moving==True:
        x=x+2
        window.geometry('100x100+'+str(x)+'+'+str(y))
        with open('Settings.txt', 'r') as file:
            data = file.readlines()

        data[0] = str(int(data[0])+2)+'\n'

        with open('Settings.txt', 'w') as file:
            file.writelines(data)
    
def right(event):
    global x
    if moving==True:
        x=x-2
        window.geometry('100x100+'+str(x)+'+'+str(y))
        with open('Settings.txt', 'r') as file:
            data = file.readlines()

        data[0] = str(int(data[0])-2)+'\n'

        with open('Settings.txt', 'w') as file:
            file.writelines(data)

def change_wp(event):
    print(event)
    global moving
    if moving==True:
        moving=False
    else:
        moving=True
def ex(event):
    sys.exit(1)
window.bind("<Control-q>",ex)
window.bind("<Left>",right)
window.bind("<Right>",left)
window.bind("<Down>",down)
window.bind("<Up>",up)
window.bind("<Control-p>",change_wp)
changeface("Kendrick")
window.bind("<Button-3>", do_popup)
  
window.bind("<Button-1>", speak)

# open file in read mode
count=0
with open("readme.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines')
numbr=count+1
loadinfo(numbr)
window.mainloop()

  
