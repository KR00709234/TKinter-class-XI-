from tkinter import*
import random
from tkinter import messagebox
root=Tk()
root.title("TKINTER Project Class XI-TILE MATCHING GAME")
root.geometry("500x550")

global winner,matches
winner=0

matches=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]            #creating the number of matches to be displayed on the tile                
random.shuffle(matches)                                              #shuffling the matches
my_frame=Frame(root)                                                # creating the button frames for the buttons
my_frame.pack(pady=10)

count=0                                                                      #defining some variables   
answer_list=[]
answer_dict={}

def reset():                                                                #reset the game
    global matches,winner                                         #set the winner counter
    winner=0
    matches=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]                   
    random.shuffle(matches)
    my_label.config(text=" ")                                      #reset the label
    button_list=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19]      #reset the buttons
    for button in button_list:
        button.config(text=" ",bg="SystemButtonFace",state="normal")

def close():
    root.destroy
        
#creating win function    
def win():
    my_label.config(text="CONGRATULATIONS!! YOU WIN!!")
    button_list=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19]
    for button in button_list:                                                 #loop through the buttons and change the colour 
        button.config(bg="yellow")
        
#function for clicking  buttons
def button_click(b,number):
    global count,answer_list,answer_dict,winner

    if b["text"]== ' ' and count < 2:
        b["text"]=matches[number]
        answer_list.append(number)                                              #adding number to answer_list
        answer_dict[b]=matches[number]                                      #adding button and number to answer_dict
        #increment the count
        count+=1
        
     #start to determine whether the number clicked match or not   
    if len(answer_list)==2:
        if matches[answer_list[0]]==matches[answer_list[1]]:
            my_label.config(text="MATCH!!")
            for key in answer_dict:
                key["state"]="disabled"                                           #disabling the button after the numbers match
            count=0
            answer_list = []
            answer_dict = {}
            winner+=1                                                                   #increment the winner count
            if winner==10:
                win()
        else:
            my_label.config(text="Did not match,Try again")
            count=0
            answer_list=[]
            messagebox.showinfo("Incorrect","Incorrect")                  #pop up box if the numbers didnt match

             #reset the buttons 
            for key in answer_dict:                                                        
                key["text"]=" "
            answer_dict={}
            


#defining the buttons
b0=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b0,0),relief="groove")                          
b1=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b1,1),relief="groove")
b2=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b2,2),relief="groove")
b3=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b3,3),relief="groove")
b4=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b4,4),relief="groove")
b5=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b5,5),relief="groove")
b6=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b6,6),relief="groove")
b7=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b7,7),relief="groove")
b8=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b8,8),relief="groove")
b9=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b9,9),relief="groove")
b10=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b10,10),relief="groove")
b11=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b11,11),relief="groove")
b12=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b12,12),relief="groove")
b13=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b13,13),relief="groove")
b14=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b14,14),relief="groove")
b15=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b15,15),relief="groove")
b16=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b16,16),relief="groove")
b17=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b17,17),relief="groove")
b18=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b18,18),relief="groove")
b19=Button(my_frame,text=' ',font=("Helvetica",15),height=3,width=6,command=lambda:button_click(b19,19),relief="groove")

#grid our buttons
b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)

b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)

b12.grid(row=3,column=0)
b13.grid(row=3,column=1)
b14.grid(row=3,column=2)
b15.grid(row=3,column=3)

b16.grid(row=4,column=0)
b17.grid(row=4,column=1)
b18.grid(row=4,column=2)
b19.grid(row=4,column=3)

my_label=Label(root,text="")
my_label.pack(pady=20)

my_menu=Menu(root)          #create a menu
root.config(menu=my_menu)

#create an option dropdown menu
option_menu=Menu(my_menu,tearoff=False)         #used to detach the menu making floating menus
my_menu.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="Reset Game",command=reset)
option_menu.add_separator()
option_menu.add_command(label="Exit Game",command=root.destroy)

root.mainloop()

   


