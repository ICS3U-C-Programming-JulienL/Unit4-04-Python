#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: November 13, 2023
# This program is a number guessing game using a loop

import random


def main():
    # generate correct answer
    correct_guess = random.randint(0, 9)

    while True:
        # get user guess
        print("A random number has been chosen between 0 and 9. Guess the number")
        user_guess_string = input("Enter your integer: ")

        try:
            # convert user guess to an integer
            user_guess_int = int(user_guess_string)

            # if the user number is less than 0 or greater than 9, tell the user to enter a positive integer between 0 and 9
            if user_guess_int < 0 or user_guess_int > 9:
                print(
                    "{} is not a positive integer between 0 and 9.".format(
                        user_guess_string
                    )
                )
            else:
                # if user guess is not equal to correct guess, then restart the loop
                if user_guess_int != correct_guess:
                    print("{} is not the answer.".format(user_guess_string))
                else:
                    # otherwise break out of the loop
                    break
        except:
            # if the number is not an integer, then tell them their input is invalid
            print(
                "\n{} is not a valid integer. Please enter a positive integer.".format(
                    user_guess_string
                )
            )

    # once the user gets it right, tell them they got it right
    print("Right! {} is the answer".format(correct_guess))


if __name__ == "__main__":
    main()
