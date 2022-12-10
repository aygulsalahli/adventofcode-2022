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

cmd = {
    "XA": "Z",
    "XB": "X",
    "XC": "Y",
    "YA": "X",
    "YB": "Y",
    "YC": "Z",
    "ZA": "Y",
    "ZB": "Z",
    "ZC": "X",
}


def get_round_score(op, command):
    me = cmd[f"{command}{op}"]
    score = rsp[me]
    score += pairs[f"{op}{me}"]
    return score


with open("../input.txt") as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        op, command = line.split()
        total += get_round_score(op, command)
    print(f"total points: {total}")
