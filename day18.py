import re


def read_input(input_file="day18.txt"):
    with open(input_file) as input:
        return input.readlines()


def find_sub_expression(expr):
    m = re.search(r"\(\d+ [*+-] \d+[*+-\\d ]*\)", expr)
    if m:
        return m.group(0)
    return False


def find_next_addition(tokens):
    try:
        return tokens.index("+")
    except ValueError as e:
        return False


def calculate(expr):
    sub = find_sub_expression(expr)
    while sub:
        sub_r = calculate(sub.replace("(", "").replace(")", ""))
        expr = expr.replace(sub, str(sub_r))
        sub = find_sub_expression(expr)

    tokens = expr.strip("\n").split(" ")

    next_addition = find_next_addition(tokens)
    while next_addition:
        a = tokens[next_addition - 1]
        b = tokens[next_addition + 1]
        c = str(int(a) + int(b))
        tokens = tokens[: next_addition - 1] + [c] + tokens[next_addition + 2 :]
        next_addition = find_next_addition(tokens)

    r = int(tokens[0])
    operation = None
    for tok in tokens[1:]:
        if tok in "+-*":
            operation = tok
        else:
            n = int(tok)
            if operation == "+":
                r += n
            elif operation == "-":
                r -= n
            elif operation == "*":
                r *= n
            operation = None
    return r


if __name__ == "__main__":
    result = sum([calculate(e) for e in read_input()])
    print(f"Sum for all expressions: {result}")
