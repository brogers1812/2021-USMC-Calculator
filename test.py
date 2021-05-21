def inputPull(message):

    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not a numerical value! Try again.")
            continue
        else:
            return userInput
            break

pullup = inputPull("How many pulls did you perform?")


print(pullup)