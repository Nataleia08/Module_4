numbers = [1, 2, 3, 4, 5]
#expected = [1, 4, 9, 16, 25]
# nub_sq = []
# for i in numbers:
#     nub_sq.append(i**2)
nub_sq = [i**2 for i in numbers]
print(nub_sq)
