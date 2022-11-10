import random
import os 
dst = 'http://imgur.com/gallery/j4rmG6E'
os.link = (dst)

#Answer
answer = "Magic 8-Ball's answer: "

#Asker
name = "Asiah"

#If there's no name


#Question
question = ""
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)


#Random answer
random_number = random.randint(1, 11)

#8-ball's answers
if question == "":
  print("Closed mouths don't get fed.")
else:
  if random_number == 1:
   print(answer + "Yes, defintely.")
  elif random_number == 2:
    print(answer + "It is decidely so.")
  elif random_number == 3:
   print(answer + "Without a doubt.")
  elif random_number == 4:
    print(answer + "Reply hazy, try again.")
  elif random_number == 5:
    print(answer + "Ask again later.")
  elif random_number == 6:
    print(answer + "Better not tell you now.")
  elif random_number == 7:
    print(answer + "My sources say no.")
  elif random_number == 8:
    print(answer + "Outlook not so good.")
  elif random_number == 9:
   print(answer + "Very doubtful.")
  elif random_number == 10:
    print("This is what I think will happen: " + os.link)
  else: 
    print("Error")

