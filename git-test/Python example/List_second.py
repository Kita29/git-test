L = [3, 6, 7, 4, -5, 4, 3, -1]
sum_L = sum(L)
if sum_L > 2:
    print("len(L) = ", len(L))
else:
    print("sum(L) =" ,sum(L))

min_L = min(L)
max_L = max(L)
rez = max_L - min_L
if rez > 10:
    print("sorted(L) = ", sorted(L))
else:
    print("rez < 10")
