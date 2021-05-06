import json
import random
import os
import sys

quiz_db = {}
quiz_db_keys = []

def inputandremove(text):
  return_ = input(text)
  print("\033[A                                                                                                                                  \033[A") # ANSI escape sequence
  return return_


def clear_console():
  if sys.platform == "linux":
    os.system('clear')
  else:
    for _ in range(50):
      print()


def load_quiz():
  global quiz_db, quiz_db_keys
  clear_console()
  print(' > Loading quiz data..')
  with open('quizdata_demo.json') as file_:
    quiz_db = json.load(file_)
  
  for key in quiz_db:
    quiz_db_keys.append(key)

  questioncounter = 0
  for category in quiz_db_keys:
    for _ in quiz_db[category]:
      questioncounter += 1

  print(' > Done. Loaded {0} questions in {1} categories.'.format(questioncounter, len(quiz_db_keys)))


def ask_random_question(learnmode=0):
  clear_console()
  random_category = quiz_db_keys[random.randrange(0, len(quiz_db_keys))]
  random_question_in_category = random.randrange(0, len(quiz_db[random_category]))
  question = quiz_db[random_category][random_question_in_category]["Question"]
  correct_answers = quiz_db[random_category][random_question_in_category]["Correct Answers"]
  answers = quiz_db[random_category][random_question_in_category]["Answers"]
  answered_correctly = False
  print("Category:\t", random_category)
  print("Questions:\t There are", len(quiz_db[random_category]), "questions in this category.")
  print("Answercount:\t", len(correct_answers), "Answer" if len(correct_answers) == 1 else "Answers")
  print("Question:\t", question)
  print()
  if learnmode>0:
    if learnmode==2:
      inputandremove("Press enter to reveal Answers.")
    for answer in correct_answers:
      print("\t\t -", answers[answer-1])
    print()
    ask_to_quit = inputandremove("Press enter to continue or q to quit. ")
    if ask_to_quit.lower() == "q":
      return True
    return
  print("")

  answerindex = 1
  for answer in answers:
    print("\t", answerindex, "-", answer)
    answerindex += 1
  

  while not answered_correctly:
    guess = inputandremove("Your Answer (q to quit, if multiple answers type numbers seperated by space): ")
    if guess == "q":
      return True
    if guess == "":
      continue
    if not "".join(guess.lower().split(" ")).isnumeric(): # its so bloated ♡(˘꒳˘❀) cspell:disable-line
      continue
    guess = guess.lower().split(" ")
    for item in range(0, len(guess)):
      guess[item] = int(guess[item])
    if set(guess) == set(correct_answers):
      print(guess, "is correct.")
      inputandremove("Press enter to continue.")
      return
    else:
      print(guess, "is wrong, try again.")

def mainmenu():
  print("\tMainmenu:")
  print("\t1: 1 Random Question")
  print("\t2: Random Questions")
  print("\tL: Learning/Zen mode")
  print("\tLL: Learning/Zen mode (press for answer)")
  print("\tQ: Quit")
  _ = input("Option: ")
  if _ == "1":
    ask_random_question()
    clear_console()
    mainmenu()
  elif _ == "2":
    multiple_questions()
    clear_console()
    mainmenu()
  elif _.lower() == "q":
    pass
  elif _.lower() == "l":
    multiple_questions(learnmode=1)
    clear_console()
    mainmenu()
  elif _.lower() == "ll":
    multiple_questions(learnmode=2)
    clear_console()
    mainmenu()
  else:
    clear_console()
    mainmenu()

def multiple_questions(learnmode=0):
  finished = False
  while not finished:
    finished = ask_random_question(learnmode)

load_quiz()
mainmenu()