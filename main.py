import time
global Data
Data = {"soda": 0, "chapter": 0,"name": ""}
oldhp = 10
permission = 0
Potat = 0

def chapter1end():
      print("end of chapter 1 ")
      print("you have " + str(Data["soda"]) + " sodas")
      print("You finished chapter: " + str(Data["chapter"]))
      

def oldman():
  global Data, oldhp
  print(oldhp)
  bput = input("the old man charges at you, you can hit them with a soda(1), or you can dodge(2) ")
  if bput == "1":
    if Data["soda"] == 0:
      print("you have no soda")
      print("try something else.")
      oldman()
    else:
      print("the soda waded him off,for now")
      oldhp -= 1
      Data["soda"] -= 1 
      time.sleep(2)
      print("the old man has returned!!!")
      oldman()
    if oldhp < 1:
      print("the old man is dead.")
      time.sleep(5)
      print("Y0U killed him.")
    else:
      time.sleep(4)
      print("the old man has returned!!!")
      oldman()
  elif bput == "2":
    print(" you dodge the old man, as he readys to shoot his scary shotgun, you kick him in the face.")
    oldhp -= 1
    if oldhp < 1:
      print("the old man is dead.")
      time.sleep(5)
      print("Y0U killed him.")
    else:
       print("the old man is madder now.")
    time.sleep(3)
    oldman()
  else:
    print("the old deranged man killed you. L")
    bozoending()

def room2():
    while True:
        choice = input("You find yourself in the next train car. There is a gramophone(1), an empty soda can(2), and the exit into the next train car(3). What will you do? ")
        
        if choice == "1":
            print("You stare at the gramophone, but it was never a gramophone. It was an ATM.")
        elif choice == "2":
            print("It's an empty soda can, what else would it be?")
            time.sleep(3)
            print("You should get on with your adventure. It's just an empty soda can.")
        elif choice == "3":
            print("You decide to leave this train car and move on to the next one.")
            break
        else:
            print("WRONG! .")

def intro():
  global Data
  
  print("Chapter 0, into the train ")
  time.sleep(1)
  print("hey how did this bum, get on the train, it's like 30 dollars to get on. ")
  time.sleep(2)
  name = input("who even are you anyway ")
  if name == "Tristan" or name == "tristan":
    print("that is a stupid name. the train will call you passenger 86. ")
    name = "passenger 86"
  else:
    print("that is a better name than tristan")
    
def chapter0():
  global Data, Potat
  potato = 0
  time.sleep(3)
  interaction = input("there are three people on this train, you can talk to person 1, 2, or 3 or leave the train car,\nplease enter a number:  ")
  if interaction == "1":
      print("don't drink the water... the put something in it.. to make you forget. wait wrong water. ")
      chapter0()
  elif interaction == "2":
      if potato < 10:
        print("what do you want... nerd ")
        potato += 1
        chapter0()
      elif potato == 10:
        print("i'll give you this potato if you leave me alone.")
        time.sleep(3)
        print("You have recieved \" Brayden the P0tato\" ")
        Potat = 1
        chapter0
      else:
        print("leave me alone " + Data["name"])  
        chapter0()
        
  elif interaction == "3":
      if Data["soda"] == 0:
        print("here, have a soda ")
        Data["soda"] += 1
        chapter0()
      else:
        print("I don't have a Soda for you... sorry")
        chapter0()
  else:
      print("you decide to leave the train car ")
      print("end of chapter 1 ")
      print("you have " + str(Data["soda"]) + " sodas")
      print("You finished chapter: " + str(Data["chapter"]))

def chapter1():
  global Data,permission
  Data["chapter"] = 1
  print("")
  print("")
  room = input("you find yourself in another train car, you see a person(1), a fridge(2), and the exit to  the train car(3), where do you go?")
  if room == "1":
    print("you know there are some dangerous people on this train, you can use soda to ward them off...")
    permission = 1
    time.sleep(2)
    print("there is some of my arsenal in that fridge, I don't know how many haven't gone flat.")
    print("don't worry... i gave up escape a long time ago.")
    time.sleep(3)
    chapter1()
  elif room == "2":
    if permission == 0:
      print("hey punk, the least you could do is ask first...")
      chapter1()
    elif permission == 1:
      print("yup thats it... There might be some   usably ones in there")
      Data["soda"]  += 4

  else: room2()

  user_input = input("in this train car, you find a deranged man, and his shotgun, would you like the train to print it?(1), or not(anything else)")
  if user_input == "1":
    print(" pew pew pew -- - -<\ 0n0 ")
    time.sleep(1)
    print("pretty scary right?")
    time.sleep(3)
    print("the deranged old man charges at you, initiating a battle. T0 TH3 D34TH!!!1q!")
    oldhp = 10
    oldman()
  else:
    print("the deranged old man charges at you, initiating a battle. T0 TH3 D34TH!!!1q!")
    oldhp = 10
    oldman()

  print("now that the old man is dead, you can get along with your adventure,")
  time.sleep(5)
  leave = input("there is nothing left here, you can leave the train car.(1)")
  if leave == 1:
    print("you decide to leave the train car.")
    chapter1end()
  else: 
    print("there is nothing left for you here,")
    print("even if you check the shotgun, its empty.")
    print("you decide to leave the traincar.")
    chapter1end()

def chapter2():
    print("")
    print("")
    print("you are in the next train car, the large group of people are in this car")
    print("well that came back to bite FAST")
    peace = input("the people in the train car recognize you as the person you killed the old man... you lie(1) or tell the truth(2)")    
    def lord():
      if peace == 1:
        print("the people believe you.")
        time.sleep(3)
      elif peace == 2:
        print("the people of the train car collectively decide to kill you.")
        time.sleep(1)
        print("womp womp.")    
        bozoending()
      else:
        print("try again")
        lord()
    print("qwerty. aanyway continue")
    def funcqwerty():
      qwerty = input("there are 4 people in this room, you cAan talk to the people  (1-4) or leave the car(5)")
      if qwerty == "1":
        print("hey.if you want anything, head to the next car. the bar there is full of soda")
        funcqwerty()
      elif qwerty == "2":
        print(" if you didnt...who killed thst guy then...")
      elif qwerty
def bozoending():
    print("you died, game over. you had no chance. hee hee hoo hoo.")
    time.sleep(3)
    print("THE END. you have the BOZO ending")
    exit()
    








def main():
  intro()
  chapter0()
  chapter1()

#this is the main funtion caller (PHIL [ps: beat not to delete this, {pps: unless you need to}])
main()
print("thank you so much for playing Express86 VER. 0.4")