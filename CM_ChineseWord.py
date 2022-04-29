

from bs4 import BeautifulSoup
from tkinter import *

import os

import tkinter.messagebox as msgbox
import random
import HSKList

import webbrowser


root = Tk()
root.title("你好中国")
root.geometry()
root.resizable(False, False)
os.system("cls")



GP = 0
BP = 0
next = 0
wronganswer = []

def selectlevel1():
    '''
       선택된 레벨의 단어를 불러온다.
    '''
    label_level.config(text =str(level_var.get())+"급 단어")
 
def makequestionlist():
    '''
    랜덤으로 선택된 단어 수 만큼 새 리스트를 만든다.


    '''
    global question
    global next
    next = 0
    i = level_var.get()
    if i ==1:
        question = random.sample(HSKList.HSK1,word_var.get())
        print(question)
    elif i ==2:
        question = random.sample(HSKList.HSK2,word_var.get())
    elif i == 3:
        question = random.sample(HSKList.HSK3,word_var.get())
    elif i == 4:
        question = random.sample(HSKList.HSK4,word_var.get())  
    elif i == 5:
        question = random.sample(HSKList.HSK5,word_var.get()) 
    elif i == 6:
        question = random.sample(HSKList.HSK6,word_var.get()) 
    btn_start['state'] = NORMAL     
  
def pressdstart(): #questionlist 에서 첫번째 단어 가져오기
    '''
       문제 리스트에서 첫번째 리스트 요소를 불러와 출력한다.
    '''
    global wronganswer
    wronganswer =[]
    label_Question.config(text = str(question[0]))
    myinput['state'] = NORMAL
    btn_reset['state'] = NORMAL
    btn_start['state'] =DISABLED
    menu.entryconfig("HSK Level",state="disabled")
    menu.entryconfig("HMW",state="disabled")
   
def reset():
  
    label_level.config(text = "테스트 레벨")
    label_Question.config(text="Ready")
    label_badpoint.config(text = 0)
    label_goodpoint.config(text = 0)
    Lastindex =listbox.size()
    listbox.delete(0, Lastindex)
    DicButton['state'] = DISABLED 
    btn_reset['state'] = DISABLED
    menu.entryconfig("HSK Level",state="normal")
    menu.entryconfig("HMW",state="normal")
    btn_reset.config(fg='black')
   
def yesno():
    global GP
    global BP
    global wronganswer
    
    #respons = msgbox.showinfo("HI",str(wronganswer))
    listinsert()
    myinput.delete(0, END)
    pauseUI()
    wronganswer = list(set(wronganswer))
    label_badpoint.config(text = BP)
    label_goodpoint.config(text = GP)
    DicButton['state'] = NORMAL   

def inputevent(event): # 리스트에서 다음 단어 가져오고 점수 체크
    '''
     입력된 단어의 정,오답 여부를 가리고 다음 단어를 가져와 출력한다.
    '''
    global GP
    global BP
    global wronganswer
    global next
    
   
    if str(myinput.get()) == question[next] and next < len(question)-1 : # 赞에 점수 +

        
        GP += 1 
        label_goodpoint.config(text =GP)
        next +=1
        label_Question.config(text = str(question[next]))
        
    
    elif str(myinput.get()) == question[next] and next +1  == len(question):
        GP +=1
        label_goodpoint.config(text = GP)
        yesno()
        
    elif str(myinput.get()) != question[next] and next < len(question)-1  :  #蛋에 점수 +
        wronganswer.append(question[next])
        BP +=1
        label_badpoint.config(text = BP)
        
        next +=1
        label_Question.config(text = str(question[next]))
       
        
        

    elif str(myinput.get()) != question[next] and next+1 == len(question):
        wronganswer.append(question[next])
        BP +=1
        label_badpoint.config(text = BP)
        yesno()
    
        
    myinput.delete(0, END)  

def listinsert():
    for i in wronganswer:
        print(i)
        listbox.insert(END,i)
  
def pauseUI():
    global next
    global GP
    global BP
    next = 0
    GP = 0
    BP = 0
    btn_start['state'] = DISABLED  
    label_Question.config(text="Ready")
    myinput['state'] = DISABLED
    menu.entryconfig("HSK Level",state="disabled")
    menu.entryconfig("HMW",state="disabled")
    btn_reset.config(fg="#dbd639")
 
def searchweb():
 
    mywordindex =listbox.curselection()
    print(listbox.get(mywordindex))
    url ="https://zh.dict.naver.com/#/search?range=all&query="  + listbox.get(mywordindex)
    webbrowser.open(url)


menu = Menu(root)

level_var = IntVar()
menu_hsk = Menu(menu ,tearoff=0, bg ="#dbd639")
menu_hsk.add_separator()
menu_hsk.add_radiobutton (label = "HSK1",value = 1 ,variable = level_var,command =selectlevel1, selectcolor="red")
menu_hsk.add_radiobutton(label = "HSK2",value = 2 ,variable = level_var,command =selectlevel1, selectcolor="red")
menu_hsk.add_separator()
menu_hsk.add_radiobutton(label = "HSK3",value = 3 ,variable = level_var,command =selectlevel1, selectcolor="red")
menu_hsk.add_radiobutton(label = "HSK4",value = 4 ,variable = level_var,command =selectlevel1, selectcolor="red")
menu_hsk.add_separator()
menu_hsk.add_radiobutton(label = "HSK5",value = 5 ,variable = level_var,command =selectlevel1, selectcolor="red")
menu_hsk.add_radiobutton(label = "HSK6",value = 6 ,variable = level_var,command =selectlevel1, selectcolor="red")
menu.add_cascade(label ="HSK Level" , menu = menu_hsk,state='active')

word_var = IntVar()
menu_word = Menu(menu, tearoff= 0, bg ="#d6d360")
menu_word.add_separator()
menu_word.add_radiobutton(label = "10", value = 10, variable = word_var ,command =makequestionlist, selectcolor="red")
menu_word.add_radiobutton(label = "30", value = 30, variable = word_var ,command =makequestionlist, selectcolor="red")
menu_word.add_radiobutton(label = "50", value = 50, variable = word_var ,command =makequestionlist, selectcolor="red")
menu_word.add_radiobutton(label = "100", value = 100, variable = word_var ,command =makequestionlist, selectcolor="red")
menu_word.add_radiobutton(label = "200", value = 200, variable = word_var ,command =makequestionlist, selectcolor="red")
menu.add_cascade(label ="HMW" , menu = menu_word,state='active' )

# menu_quit = Menu(menu, tearoff = 0, bg ="#e0de8b")
# menu_quit.add_command(label = "리셋", command = reset)
# menu.add_cascade(label ="리셋", menu = menu_quit)

menu.add_cascade(label="ver:02",state='disable')


#맨윗 줄
frame_setting = LabelFrame(root, text ="Setting",fg="#dbd639" ,relief = "sunken" ,bd=5,padx =3 ,bg='#33497a')
frame_setting.pack(side ="top", fill = "both", expand=True)


label_level = Label(frame_setting,fg="white", text = "테스트 레벨",width = 10 , height= 2,bg='#33497a')
btn_start = Button(frame_setting, text = "Start",width = 5 , height= 2,command =pressdstart ,state=DISABLED,bg='#33497a')


label_level.grid(row = 0, column = 0 ,sticky=N+E+W+S ,padx=3, pady=3,rowspan =2)
btn_start.grid(row = 0, column = 2 ,sticky=N+E+W+S ,padx=3, pady=3,rowspan =2)

label_good = Label(frame_setting ,fg="#7f8182",text = "赞:",bg='#33497a')
label_goodpoint= Label(frame_setting ,text = "0",bg='#33497a')
label_bad = Label(frame_setting ,fg="#7f8182",text = "笨:",bg='#33497a')
label_badpoint = Label(frame_setting ,text = "0",bg='#33497a') 

label_good.grid(row = 0, column = 3 ,sticky=N+E+W+S ,padx=3, pady=3)
label_goodpoint.grid(row = 0, column = 4 ,sticky=N+E+W+S ,padx=3, pady=3)
label_bad.grid(row = 1, column = 3 ,sticky=N+E+W+S ,padx=3, pady=3)
label_badpoint.grid(row = 1, column = 4 ,sticky=N+E+W+S ,padx=3, pady=3)

btn_reset = Button(frame_setting, text = "Reset",width = 5 , height= 2,command =reset ,state=DISABLED,bg='#33497a')
btn_reset.grid(row = 0, column = 8 ,sticky=N+E+W+S ,padx=3, pady=3,rowspan =2)


#두번째 줄
frame_Question = LabelFrame(root ,relief = "solid",bd =2,padx =1,pady =1,bg="#95abb8")
frame_Question.pack(side ="top", fill = "both", expand=True)
label_empty01 = Label(frame_Question,text ="      ",bg="#95abb8")
label_empty01.grid(row = 1, column = 0,columnspan =2)
label_Question = Label(frame_Question, text ="Ready",width =8 , height=1,anchor= "center",bg="#95abb8")
label_Question.grid(row = 1, column = 2  ,sticky=N+E+W+S ,padx=3, pady=3,columnspan =2)
label_Question.config(font=("Courier",30,'bold'))

#입력 줄
frame_input = LabelFrame(root, relief = "solid",bd =2,padx =1,pady =1,bg='#33497a' )
frame_input.pack(side ="top",fill ="both",expand = False)
myinput = Entry (frame_input, bd = 1 ,width = 40,state='readonly')
myinput.grid(row = 0, column = 0 ,pady = 8)
myinput.bind('<Return>',inputevent)





#스크롤바

scrollbar = Scrollbar(root)
scrollbar.pack(side ="right" ,fill ="both")
listbox = Listbox(root,selectmode="extended",width=30, height = 20,yscrollcommand = scrollbar.set,bg="#33497a",fg="#6e1515",selectborderwidth=1)

listbox.pack()
scrollbar.config(command= Listbox.yview)

#사전검색
DicButton = Button(root,text="Dic.", width=15, command=searchweb,state='disabled')
DicButton.pack()


#맨 아래 줄
frame_ufo = LabelFrame(root ,bg="black")
frame_ufo.pack(side="top",fill="both",expand=True)
label_ufo =Label(frame_ufo,fg="#7f8182",text="      Made by UFORiderStudio",bg="black")
label_ufo.grid(column = 0,sticky=N+E+W+S ,padx=40)


root.config(menu =menu,background="black")

root.mainloop()
