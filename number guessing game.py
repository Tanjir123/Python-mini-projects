import random
low=1
high=100
number=random.randint(low,high)
total=0
while True:
  total=total+1
  print(f"guess a number between {low} and {high}:")
  guess=input()
  if guess.isdigit():
      guess=int(guess)
      if guess==number:
          print("CORRECT!!!")
          break
      elif guess<number:
          print("Too low.take another guess")
      elif guess>number:
          print("Too high.take another guess")
  else:
      print("invalid input")
print(f"you took {total} guesses")