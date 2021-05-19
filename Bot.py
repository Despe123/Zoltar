#!/usr/bin/python3
#  -*- coding: utf-8 -*-
# Date of begin: Thu 13 April 2021 17:02:27 CET
# Last update: Wed 19 May 2021
# Author: Maud Margaron
# Description:
# Python Version 3.9
# ECAM - EENG 1 - Zoltar Project

import json
import random

def random_bot(twitter_question):
    """ The random_bot function will open a json will where you will have a dictonary with all the key word use in the sentence (the input) and the coresponding anwser.
        For exemple if in the input you have the word 'futur' it will take only the word 'futur' then go in the proper line in the json.file and will give you a random
        answer that the computer will chose by itself."""
    
    f = open('data.json',encoding="utf8")

    data = json.load(f)
  
    list_of_word = data['word']['Word_list']

    f.close()


    for i in list_of_word:
        if i in twitter_question:
            return data[i]['Word_list'][random.randint(0, len(data[i]['Word_list'])-1)] 

  
        
# les deux premiers []= a la liste dans le json
# tout le reste correspond a l indentation d un element de la liste de maniere aleatoire


#Red Ranger PC Local test (Blue Ranger Please comment Following lines before working on Twitter API0
print("Welcome to the Zoltar Machine. Ask your question and we will predict your future.")
answer = str(input("enter your question:  "))
print(random_bot(answer))
