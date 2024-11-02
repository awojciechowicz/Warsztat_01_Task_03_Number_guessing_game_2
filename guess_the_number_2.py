def give_me_the_number():
    while True:
        try:
            my_number = int(input("Enter your number between 1 and 1000. I will gues it in max. 10 hits: "))
            return my_number
        except ValueError:
            print("That's not an integer.")

def check_the_number():
    while True:
        my_number = give_me_the_number()
        if my_number in range(1, 1001):
            return my_number
        print("Out of range, try again.")

def guess_the_number():
    my_number = check_the_number()
    min = 1
    max = 1000
    guess = ""
    while guess != my_number:
        guess = int((max-min)/2) + min
        print(f"I'm guessing: {guess}.")
        your_answer = input("too high / too low / you win? : ").lower()
        if your_answer == "too high":
            max = guess
        elif your_answer == "too low":
            min = guess
        elif your_answer == "you win":
            return "Con gratulations!!!"
        else:
            print("Don't cheat!")
    return ("I won")

print(guess_the_number())
