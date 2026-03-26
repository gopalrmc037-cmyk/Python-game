import random
print("BE READY TO PLAY ROCK,PAPER AND SISSOR") 
choice={"rock":1,
      "paper":-1,
      "sissor":0
      }
computer=random.choice([1,-1,0])
reversechoice={
    1:"rock",
    -1:"paper",
    0:"sissor"
}
com=(reversechoice[computer])
yourchoise=input("what your choice?").lower()
you=(choice[yourchoise])
print("You choose:",yourchoise)
print("computer choose:",com)
if (you==computer):
    print("You have tied.")
elif computer==1 and you==-1 or computer==-1 and you==0 or computer==0 and you==1:
    print("You have won.")
else:
    print("Computer have won.")


