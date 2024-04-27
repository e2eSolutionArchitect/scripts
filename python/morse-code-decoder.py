def create_dictionary():
    # Create a dictionary object
    dictionary_obj = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--.."
    }
    return dictionary_obj

def create_rev_dictionary():
    # Create a dictionary object
    rev_dictionary_obj = {
        ".-":"A",
        "-...":"B",
        "-.-.":"C",
        "-..":"D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....":"H",
        "..":"I",
        ".---":"J",
        "-.-":"K",
        ".-..":"L",
        "--":"M",
        "-.":"N",
        "---":"O",
        ".--.":"P",
        "--.-":"Q",
        ".-.":"R",
        "...":"S",
        "-":"T",
        "..-":"U",
        "...-":"V",
        ".--":"W",
        "-..-":"X",
        "-.--":"Y",
        "--..":"Z"
    }
    return rev_dictionary_obj

def search(dictionary_obj, search_string):
    result = ""
    for letter in search_string:
        if letter.upper() in dictionary_obj:
            result += dictionary_obj[letter.upper()] + " "
        else:
            result += "Not Found" + " "
    return result.strip()

def rev_search(rev_dictionary_obj, rev_search_string):
    # Split the input string by space to get tokens
    tokens = rev_search_string.split()
    result = ""
    for token in tokens:
        if token in rev_dictionary_obj:
            result += rev_dictionary_obj[token] + " "
        else:
            result += "Not Found" + " "
    return result.strip()

def main():
    # Create a dictionary
    dictionary_obj = create_dictionary()
    rev_dictionary_obj = create_rev_dictionary()

    # Read input from the user
    search_string = "Hello"
    rev_search_string = ". .-.. .-.. ---"

    # Search for values based on the input string
    result = search(dictionary_obj, search_string)
    print("Result:", result)
    rev_result = rev_search(rev_dictionary_obj, rev_search_string)
    print("Rev Result:", rev_result)

if __name__ == "__main__":
    main()
