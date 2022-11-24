print("Quiz Time")
question1 = "Who is the ceo of google"?"
options1 = "a.Myslef\nb. His dad\nc. sundar Pichai \nd. Barack Obama\n"
print(question1)
print(options1)

while True:
    response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

    if response == "d":
        break
    else:
        print("Incorrect!!! Try again.")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "d":
                stop = True
                break
            else:
                print("Incorrect!!! You ran out of your attempts")
                stop = True
                break
        if stop:
            break

# Now the program will ask the user to go for the bonus question or not

while True:
    bonus = input("Would you like to give a try to the bonus question?\nHit 'y' for yes and 'n' for no.\n")

    if bonus == "y":
        print("Who invented Facebook?")
        print("a. \nb. His dad\nc. Mark Zuckerberg\nd. Aliens")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "c":
                break
            else:
                print("Incorrect!!! Try again.")

            while True:
                response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")


                if response == "c":
                    stop = True
                    break
                else:
                    print("Incorrect!!! You ran out of your attempts")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("INVALID INPUT!!! Only hit 'y' or 'n' for your response")

# Now do the same as done above for the next round and another bonus question
