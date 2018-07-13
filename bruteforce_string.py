import random
import string
import time

def gen_rdm_string(lng):
    rdm_str = ''.join(random.choice(string.digits + string.ascii_letters + string.punctuation + " ") for _ in range(lng))
    return rdm_str

def score_string(gen_str, org_str, part_str):
    score = 0
    for i in range(len(gen_str)):
        check_str = "".join(part_str)
        print(check_str, end="\033[F")
        #time.sleep(0.01)
        if check_str == org_str:
            return 100, part_str
        elif gen_str[i] == org_str[i]:
            part_str[i] = gen_str[i]
            score += 1
    n_score = int(100/len(gen_str)*score)
    return n_score, part_str

def check_string():
    org_str = "SuPeR.GeH3!m3S?pA55Wor7."
    part_str = ["X"] * len(org_str)
    best_score = 0
    while best_score != 100:
        temp_score, part_str = score_string(gen_rdm_string(len(org_str)), org_str, part_str)
        if temp_score > best_score:
            best_score = temp_score
    return print("\n100%!")


print(check_string())
