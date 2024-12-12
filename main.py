def main(arg):
    # Here we define a dict with all the values associated to the letters
    ScrabbleScore = {
        "a": 1,
        "e": 1,
        "i": 1,
        "l": 1,
        "n": 1,
        "o": 1,
        "r": 1,
        "s": 1,
        "t": 1,
        "u": 1,
        "d": 2,
        "g": 2,
        "b": 3,
        "c": 3,
        "m": 3,
        "p": 3,
        "f": 4,
        "h": 4,
        "v": 4,
        "w": 4,
        "y": 4,
        "k": 5,
        "j": 8,
        "k": 8,
        "q": 10,
        "z": 10,
    }

    # Then we define a variable in which to store the total score
    result = 0

    # Then we iterate through every element in the input and add the relative value to the
    # score variable
    for i in arg.lower():
        result += ScrabbleScore[i]

    # Finally returning the total score
    return result


if __name__ == "__main__":
    inpt = input("Write down a word to obtain its Scrabble value: ")
    print(main(inpt))
