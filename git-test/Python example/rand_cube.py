def rand_cube():
    import random
    val1 = random.randint(1,6)
    val2 = random.randint(1,6)
    if val1 < val2:
        print("Player 2 win: ", val1, " ", val2)
    elif val1 > val2:
        print("Player 1 win", val1, " ", val2)
    else:
        print("Dead heat", val1, " ", val2)
