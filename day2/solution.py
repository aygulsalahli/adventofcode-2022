rsp = {"X": 1, "Y": 2, "Z": 3}

pairs = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}


def get_round_score(op, me):
    score = rsp[me]
    score += pairs[f"{op}{me}"]
    return score


with open("input.txt") as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        op, me = line.split()
        total += get_round_score(op, me)
    print(f"total points: {total}")
