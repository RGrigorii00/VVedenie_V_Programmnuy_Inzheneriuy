"""
	Gadalka
"""
from brain import Brain

brain = Brain()
prompt = "What you want?"

question = " "

while (question != "Stop!"):
	print(prompt, end=' ')
	answer = brain.think(input())
	print(answer)


































	
#if question == "Stop!": 
#	print(prompt, end=' ')
#	answer = brain.think(input())
#	print(answer)
#elif question == "Stop!":
#exit()

#if question != "хватит":
 #   print(prompt, end = ' ')
  #  answer = brain.think(input())
   # print(answer)
#else:
 #   exit()