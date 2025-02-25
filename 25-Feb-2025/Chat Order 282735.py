# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n= int(input())
arr=[]
for _ in range(n):
    arr.append(input())
seen = set()
for item in reversed(arr):  
    if item not in seen:
        seen.add(item)
        print(item)