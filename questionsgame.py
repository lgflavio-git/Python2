def get_answer():
  answers = ('a', 'b', 'c')
  while True:
    answer = input('Select your answer (a/b/c): ').lower()
    if (answer
            not in answers):
      print('Invalid answer')
    else:
      return answer



def main():
  questions = (
    "Q1:Capital of France? a)Paris b)London C)Rome",
    "Q2:Capital of UK? a)Paris b)London C)Rome",
    "Q3:Capital of Italy? a)Paris b)London C)Rome"
  )

  correct_answers = ("a","b","c")
  score = 0

  for i in range (0,3):
    print(questions[i])
    current_answer = get_answer()

    if current_answer in correct_answers[i]:
      print('Correct')
      score += 1
    else:
      print('Incorrect')
  print (f'\nYour score is: {score}/3\n')

if __name__ == "__main__":
  main()

