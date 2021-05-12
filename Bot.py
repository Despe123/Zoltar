import json
import random


f = open('data.json',)

data = json.load(f)
  
list_of_word = data['word']['Word_list']

f.close()


print("Welcome to the Zoltar Machine. Ask your question and we will predict your future.")
answer = str(input("enter your question:  "))

for i in list_of_word:
    if i in answer:
        print( data[i]['Word_list'][random.randint(0, len(data[i]['Word_list'])-1)] )

  
        
# les deux premiers []= a la liste dans le json
# tout le reste correspond a l indentation d un element de la liste de maniere aleatoire

