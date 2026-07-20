number = 12
guess_count = 1
guess_limit = 3
msg = "guess btw 1 to 12 = "


while guess_count <= guess_limit :
      user_guess = int(input( msg ))


      if user_guess == number :
        print("you got it right")
        break
        
      elif user_guess < number :
        print("you did it wrong")

      else:
        print("you did it wrong")

      guess_count = guess_count + 1

      if guess_count > guess_limit :
        print("game over")
