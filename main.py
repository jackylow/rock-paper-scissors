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
choice_people = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
spisok = [rock, paper, scissors]
computer = random.choice(spisok)
print(computer)
print("Computer chose:")
if choice_people == 0:
  print(rock)
elif choice_people == 1:
  print(paper)
elif choice_people == 2:
  print(scissors)
else:
  print("Error.")

if choice_people == 0 and computer == scissors:
  print("You win.")
elif choice_people == 2 and computer == paper:
  print("You win.")
elif choice_people == 1 and computer == rock:
  print("You win.")
elif (choice_people == 0 and computer == rock) or (choice_people == 1 and computer == paper) or (choice_people == 2 and computer == scissors):
  print("Try again.")
elif choice_people >= 3 or choice_people < 0:
  print("You lose. Invalid number.")
else:
  print("You lose.")
