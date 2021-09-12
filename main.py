import random

def main():
    a = [i for i in range(0, 101)]
    guesses = 0
    begin = 0
    end = len(a) - 1
    print("Hello, and welcome to the computer guessing game.")
    print("I want you to think of a number between 1 and 100.")
    print("I will now try to guess this number.")

    while begin <= end:
        midpoint = begin + (end - begin) // 2
        midpoint_value = a[midpoint]
        answer = input(f"Is your number {midpoint_value}? ")
        if answer == 'no':
            guesses += 1
            answer1 = input("Is your number higher or lower? ")
            if answer1.lower() == 'lower':
                end = midpoint - 1
            else:
                begin = midpoint + 1

        if answer.lower() == 'yes':
            print("Eureka! I've got it!")
            print(f"It took me {guesses} guesses to get your number!")
            break


if __name__ == "__main__":
	main()
