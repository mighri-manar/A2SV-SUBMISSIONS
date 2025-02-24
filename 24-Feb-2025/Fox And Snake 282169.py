# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n, m = map(int, input().split())
print("#" * m)
print("." * (m - 1) + "#")
print("#" * m)
for j in range(4, n + 1):
    print("#" * m if j % 2 else "#" + "." * (m - 1) if j % 4 == 0 else "." * (m - 1) + "#")
