import random

def roll(side): #function used to simulate dice roll
  x = random.randint(1,side)
  return x 

def user_turn():
  choice = input("What do you want to do? ")
  if choice.upper() == "FIGHT":
    attack = input("What move would you like to use? ")
    
    if attack.upper() == "FIRE":
      enemy.hp -= fire.dmg
    
      if enemy.hp > 0:
       print("Enemy received %s damage!" % fire.dmg)
       print("Enemy has %s hp left." % enemy.hp)
       
       enemy_turn()
       
      else:
       print("You have defeated your enemy! You win!")
      
    else:
      print("That was not a proper option. Your opponent takes your turn!")
      enemy_turn()
      
  elif choice.upper() == "RUN":
    run_chance = roll(2) #50% accuracy
    if run_chance == 1:
      print("You successfully ran away")
    else:
      print("Your enemy caught up to you")
      enemy_turn()
    
  else:
    print("that was not a proper option. Your opponent takes your turn!")
    enemy_turn()
    
def enemy_turn():
  acc = roll(10) #simulation of accuracy
  
  if acc >= 5: #50% accuracy rate
    hit = True
    user.hp -= fire.dmg
    print("You were burned for %s damage!" % fire.dmg)
    print("You have %s health left." % user.hp)

    if user.hp > 0:
      user_turn()
    else:
      print("You lose!")

  
  else:
    hit = False
    print("Your opponent missed!")
    user_turn()

  
  
 
class wep: #weapon class with damage attribute 
  def __init__(self, dmg):
    self.dmg = dmg
    
class player: #player class with health attribute
  def __init__(self, hp):
    self.hp = hp

#init players
user = player(100)
enemy = player(100)

"""
user.hp, enemy.hp = 100 #can also be done like this
"""

#init weapons
fire = wep(25)



user_turn() #Start the fight

  
  
