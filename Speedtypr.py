import time
import random

with open("words.txt", "r", encoding="utf-8") as file:
    commands = [line.strip() for line in file.readlines()]

completed = []
y = False
while y == False:
    words = input("How many words do you want to type? \n")
    if words.isdigit() and int(words) > 0:
        y = True
    else:
        print("Please enter a valid number.")
        continue 

wdone = 0
mistakes = 0

if int(words) > len(commands):
    words = str(len(commands))

input("Press Enter to ready")

timea = time.time()
while wdone < int(words):
    rand = random.choice(commands)
    if rand in completed:
        continue
        
    print(f"Type: {rand}")
    input_txt = input("> ")
    
    if input_txt == rand:
        print("Correct!")
        completed.append(rand)
        wdone += 1
    else:
        print("You messed it up!")
        mistakes += 1
     
timestop = time.time()
full = timestop - timea

if int(words) > 10 and full < 5:
    print(f"You're fast! it took you only {full:.2f} seconds!")
else:
    print(f"That took you {full:.2f} seconds to type that.")

print(f"You made {mistakes} mistakes.")
input("Press Enter to exit")