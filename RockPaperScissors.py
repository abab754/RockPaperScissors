import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rand = random.randint(0, 2)
if choice == 0:
  print(rock)
  if rand == 0:
    print(rock)
    print("The computer also chose rock. Draw")
  elif rand ==1:
    print(paper)
    print("The computer chose paper. You Lose")
  else:
    print(scissors)
    print("The computer chose scissors. You Win")
elif choice ==1:
  print(paper)
  if rand == 0:
      print(rock)
      print("The computer chose rock. You Win")
  elif rand ==1:
    print(paper)
    print("The computer also chose paper. Draw")
  else:
    print(scissors)
    print("The computer chose scissors. You Lose")
elif choice ==2:
    print(scissors)
    if rand == 0:
        print(rock)
        print("The computer chose rock. You Lose")
    elif rand ==1:
        print(paper)
        print("The computer chose paper. You Win")
    else:
        print(scissors)
        print("The computer also chose scissors. Draw")
else:
    print("You have entered an invalid number. You lose")
