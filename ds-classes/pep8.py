def number_of_characters(input_string):
    alphabetics = 0
    numerics = 0
    whitespace = 0
    puntuations = 0

    for n in input_string:
        if n.isalpha():
            alphabetics += 1
        elif n.isspace():
            whitespace += 1
        elif n.isdigit():
            numerics += 1
        else:
            puntuations += 1

    return {
        'alphabetics': alphabetics,
        'numerics': numerics,
        'whitespace': whitespace,
        'puntuations': puntuations
    }


result = number_of_characters('Hello World !123')
print(result)
    