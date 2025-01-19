import random
s=0
print("Menu".center(50,"="))
print("1.Type s for snake\n2.Type w for Water\n3.Type g for Gun")
while True:
  computer=random.choice([-1,0,1])
  print("="*50)
  youstr=input("enter your choice: ")
  youdict={"s":1,"w":-1,"g":0}
  reverse={1:"Snake",-1:"Water",0:"Gun"}
  you=youdict[youstr]
  print(f"You choose: {reverse [you]}\ncomputer choice: {reverse [computer]}")
  
  if(computer==you):
    print("its a draw")
    print("No Score Added!! Continue Playing")
  else:
    if(computer==-1 and you==1):
     print("you win!!")
     s=s+1
     print(f"Your current Score{s}!!\n Continue Playing")

    
    elif(computer==-1 and you==0):
      print("you loose!!")
      print(f"Game Ends\n Your Final score:{s}")
      break
    
    elif(computer==1 and you==-1):
      print("you loose!!")
      print(f"Game Ends\n Your Final score:{s}")
      break
    elif(computer==1 and you==0):
      print("you Win!!")
      s=s+1
      print(f"Your current Score{s}!!\n Continue Playing")
    elif(computer==0 and you==-1):
      print("you Win!!")
      s=s+1
      print(f"Your current Score{s}!!\n Continue Playing")
    elif(computer==0 and you==1):
      print("you loose!!")
      print(f"Game Ends\n Your Final score:{s}")
      break
    else:
      print("something went wrong")
    
    
    
  
