"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
"""imports and constants"""
MIN_SCORE = 0
MAX_SCORE = 100


def main():
    """Get score, print result, print random, print result of random"""
    score = float(input("Enter score: "))
    result = get_result(score)
    print(f"Score: {score} is {result}.")
    rand_score = get_rand()
    rand_result = get_result(rand_score)
    print(f"Random score generated: {rand_score:.2f} is {rand_result}.")


def get_result(score):
    """Gives the result"""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score."
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


def get_rand():
    """Get random float"""
    get_ran = random.uniform(MIN_SCORE, MAX_SCORE)
    return get_ran


main()
