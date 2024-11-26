import datetime
from playsound import playsound  # The actual value can be retrieved by calling gmtime(0)
import random
from time import sleep
sent = open("sentences.txt","w")
sent.write("life is like riding a bicycle,To keep your balance you must keep moving\nit always seems impossible until it is done")
sent.close()
def sound_playing(d_N,h,m,Choose_option):
 if d_N == "PM":
     h += 12
 while True:  # or (1==1)
  if h == datetime.datetime.now().hour and m == datetime.datetime.now().minute:
    if Choose_option == 1:
         playsound('/Users/rehabmahmoud/PycharmProjects/pythonProject6/As7a ya shalbi.mp3')
    elif Choose_option==2:
      playsound('/Users/rehabmahmoud/PycharmProjects/pythonProject6/toot toot toot.mp3')
    elif Choose_option==3:
     playsound('/Users/rehabmahmoud/PycharmProjects/pythonProject6/omy ya bet.mp3')
    else: print("invalid option")

def Sound_playing(d_N,h,m):
 if d_N == "PM":
  h += 12
  while True:  # or (1==1)
    if h == datetime.datetime.now().hour and m == datetime.datetime.now().minute:
        print("playing...")
        playsound('/Users/rehabmahmoud/PycharmProjects/pythonProject6/As7a ya shalbi.mp3')
        break
 else:
    if d_N == "AM":
      while True:  # or (1==1)
        if h == datetime.datetime.now().hour and m == datetime.datetime.now().minute:
         print("playing...")
         playsound('/Users/rehabmahmoud/PycharmProjects/pythonProject6/As7a ya shalbi.mp3')
         break
def wake_up_mission() :

 print("1 Math problem")
 print("2 random number")
 print("3 typing")
def random_num():
 number = random.randint(10,200)
 num2 = random.randint(200,300)
 num3= random.randint(150,250)
 print(num2,  num3, number )
 sleep(3)
 print(num2, num3, "**")
 num1= int(input("Enter the numbner:"))
 while num1 != number:
        num1 =int(input("wrong write it again "))

def typing_sentences():
 sent=open("sentences.txt","r")
 lines=sent.readlines()
 line=random.choice(lines)    #chosing a random line from the file
 print(line)
 quote = input("Please write this statement")
 c =0
 quote = quote.split()
 line = line.strip().split()
 while len(quote)!=len(line):
     quote= input("The statement does not match the right one ").split()
 #quote = quote.split()
 for i in range(len(quote)):
   for j in range (len(line)):
     if line[j] == quote[i]:
            c +=1
 if c == 0:
        print("False")
 else:
        print("correct")

def level_one():
    score=0
    P=int(input("what is the number of problems do you want to solve?"))     #p for number of problems
    for i in range(P):
        num1=random.randint(1,10)
        num2=random.randint(1,10)
        print('solve this to wake up :' ,num1 ,'+', num2,' = ?')
        ans=num1+num2                   #ans for answer
        user_ans=int(input("..."))      #user_ans for user answer
        if ans==user_ans:
            score+=1
            print("bravo! that's correct!")
        else:
            while user_ans!=ans:
                print("the answer is wrong,try again!")
                user_ans=int(input("..."))
                score=1
        print("your score is:",score)

#second level
def level_two():
 score=0
 P=int(input("what is the number of problems do you want to solve?"))     #p for number of problems
 for i in range(P):
    num1=random.randint(10,99)
    num2=random.randint(10,99)
    print('solve this to wake up :' ,num1 ,'+', num2,' = ?')
    ans=num1+num2                   #ans for answer
    user_ans=int(input("..."))      #user_ans for user answer
    if ans==user_ans:
        score+=1
        print("bravo! that's correct!")
    else:
         while user_ans!=ans:
          print("the answer is wrong,try again!")
          user_ans=int(input("..."))
          score=1
          print("your score is:",score)


def level_three():
    score=0
    P=int(input("what is the number of problems do you want to solve?"))     #p for number of problems
    for i in range(P):
        num1=random.randint(100,199)
        num2=random.randint(100,199)
        print('solve this to wake up :' ,num1 ,'+', num2,' = ?')
        ans=num1+num2                   #ans for answer
        user_ans=int(input("..."))      #user_ans for user answer
        if ans==user_ans:
            score+=1
            print("bravo! that's correct!")
        else:
            while user_ans!=ans:
                print("the answer is wrong,try again!")
                user_ans=int(input("..."))
                score=1
        print("your score is:",score)
def sz(snz):
    if snz == 1:
        sleep(2)
        playsound('/Users/rehabmahmoud/PycharmProjects/pythonProject6/As7a ya shalbi.mp3')
    else:
        print("fine")

H = int(input("enter an hour:"))  # this lines takes the alarm time details
M = int(input("enter minutes:"))
D_N = input("AM or PM?:") # if this did not work str( the input
choose_option = int(input("press 1 to ringtone 1 and so on"))
wum = int(input("Do you want a wake-up mission:  1(yes) 2(No)"))
if wum == 2:
 print("sweet dreams")
 sound_playing(D_N,H,M,choose_option)
 snooze = int(input("DO you need a snooze press 1 for yes"))
 sz(snooze)
else:
    wake_up_mission()  #showing the list of task the user can do

mission = int(input("Enter your option"))
if mission == 1 :
 x=int(input("PRESS 1 TO LEVEL ONE:\nPRESS 2 TO LEVEL TWO:\nPRESS 3 TO LEVEL THREE:\n"))
 if x == 1 :     #first level
     Sound_playing(D_N,H,M)
     level_one()
 else:
     if x == 2:
         Sound_playing(D_N,H,M)
         level_two()    #second level
     else :
         if x == 3:
             Sound_playing(D_N,H,M)
             level_three()   #third level
         else:
             print("invalid option")
elif mission == 2:
    #sound_playing(D_N,H,M)
    #times=int(input("number of times"))
    sound_playing(D_N,H,M,choose_option)
    #for counter in range(times):  #looping to do the number of times the user want to do that mission
    random_num()

elif mission==3:
    Sound_playing(D_N,H,M)
    typing_sentences()
else: print("invalid option")
