# Quiz Game

questions = ("Which of these cities is most northerly?",
             "Which capital city is home to the Parthenon?",
             "What is the capital city of New Zealand?",
             "Which of these capital cities has the highest population?",
             "Addis Ababa is the capital city of what country?")

options = (("A. Stockholm", "B. Reykjavik", "C. Copenhagen"),
           ("A. Athens", "B. Rome", "C. Turkey"),
           ("A. Auckland", "B. Wellington", "C. Christchurch"),
           ("A. Tokyo", "B. Seoul", "C. London"),
           ("A. Kenya", "B. Ethiopia", "C. Sudan"))
           
answers = ("B", "A", "B", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
  print("----------------------------")
  print(question)
  for option in options[question_num]:
    print(option)
  
  guess = input("Enter (A, B, C): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score += 1
    print("CORRECT!")
  else:
    print("INCORRECT!")
    print(f"{answers[question_num]} is the correct answer.")
  question_num += 1

print("----------------------------")
print(         "YOUR SCORE"         )
print("----------------------------")

print("Answers: ", end="")
for answer in answers:
  print(answer, end=" ")
print()  
 
print("Guess: ", end="  ")
for guess in guesses:
  print(guess, end=" ")
print() 

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")