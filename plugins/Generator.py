import random

#code generator

def default_generator():
    default = ""
    for _ in range(9):
        digit = random.randint(0, 9)
        default += str(digit)
    
    control_number = calculate_control_number(default)
    
    default += str(control_number)
    return default

#code calculate

def calculate_control_number(melli_code):
    melli_code = list(map(int, melli_code))
    control_sum = sum(melli_code[i] * (10 - i) for i in range(9))
    control_number = control_sum % 11

    if control_number < 2:
        return control_number
    else:
        return 11 - control_number

#round code generator

def round_generator():
    round = []
    code_sum = 0
    j = 9

    for i in range(10, 1, -1):
        j = random.randint(0, j if j >= 2 else 2)
        round.append(j)
        code_sum += j * i

    cs = code_sum % 11

    if cs < 2:
        round.append(cs)
    else:
        round.append(11 - cs)

    if all(x == round[0] for x in round[1:]):
        return round_generator()

    return ''.join(map(str, round))