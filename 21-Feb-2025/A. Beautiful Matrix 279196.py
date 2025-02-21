# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

arr = []
remember_i, remember_j = 0, 0
for i in range(5):
    row = list(map(int, input().split()))  
    arr.append(row)
    if 1 in row:  
        remember_i, remember_j = i, row.index(1)
        break
print(abs(remember_i - 2) + abs(remember_j - 2))
