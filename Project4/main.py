import random

rock_icon = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_icon = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors_icon = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

win_message = "You win!"
lose_message = "You lose!"
tie_message = "It's a tie!"

icons = [rock_icon, paper_icon, scissors_icon]
messages = [win_message, lose_message, tie_message]

player_decision = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_decision = random.randint(0, 2)

if not 0 <= player_decision <= 2:
    print("You typed an invalid number. You lose!")
    raise SystemExit

print(icons[player_decision])
print(f"Computer chose:\n{icons[computer_decision]}")

# 0 for player, 1 for computer, 2 for tie
winner = 0
if computer_decision == (player_decision + 1) % 3:
    winner = 1
elif player_decision == computer_decision:
    winner = 2

print(messages[winner])

