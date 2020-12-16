def make_rule(p1_low, p1_high, p2_low, p2_high):
    return lambda x: (p1_low <= x <= p1_high) or (p2_low <= x <= p2_high)

def parse_rules(rules):
    r = {}
    for rule in rules:
        name, rest = rule.split(":")
        p1, p2 = rest.split("or")
        p1_low, p1_high = p1.split("-")
        p1_low = int(p1_low)
        p1_high = int(p1_high)
        p2_low, p2_high = p2.split("-")
        p2_low = int(p2_low)
        p2_high = int(p2_high)
        r[name] = make_rule(p1_low, p1_high, p2_low, p2_high)
    return r


def parse_ticket(ticket):
    return [int(f) for f in ticket.split(",")]


def parse_input(filename="day16.txt"):
    with open(filename) as input_file:
        lines = [line.strip("\n") for line in input_file.readlines()]
    my_ticket_idx = lines.index("your ticket:")
    rules = lines[:my_ticket_idx - 1]
    rules = parse_rules(rules)
    my_ticket = lines[my_ticket_idx + 1]
    my_ticket = parse_ticket(my_ticket)
    nearby_tickets_idx = lines.index("nearby tickets:")
    nearby_tickets = lines[nearby_tickets_idx + 1:]
    nearby_tickets = [parse_ticket(t) for t in nearby_tickets]
    return rules, my_ticket, nearby_tickets


def valid_fields(x, rules):
    r = set()
    for name, f in rules.items():
        if f(x) == True:
            r.add(name)
    return r


def is_valid(t, rules):
    for f in t:
        if len(valid_fields(f, rules)) == 0:
            return False
    return True


if __name__ == "__main__":
    rules, my_ticket, nearby_tickets = parse_input()

    valid_tickets = [t for t in nearby_tickets if is_valid(t, rules)]
    valid_tickets.append(my_ticket)

    possible_fields = {}
    for i in range(len(my_ticket)):
        sets = [valid_fields(t[i], rules) for t in valid_tickets]
        sr = sets[0]
        for s in sets:
            sr.intersection_update(s)
        possible_fields[i] = sr
    print(possible_fields)

    solution = [16, 5, 18, 8, 13, 10]
    result = 1
    for i in solution:
        result *= my_ticket[i]
    print(result)

