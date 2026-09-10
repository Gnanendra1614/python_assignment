from itertools import combinations

N = int(input())
letters = input().split()
K = int(input())

total = 0
contains_a = 0

for combo in combinations(letters, K):
    total += 1
    if 'a' in combo:
        contains_a += 1

probability = contains_a / total

print(f"{probability:.4f}")