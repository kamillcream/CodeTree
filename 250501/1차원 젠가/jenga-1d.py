n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
s1, e1 = s1-1, e1-1
s2, e2 = s2-1, e2-1

del(blocks[s1:e1+1])
del(blocks[s2:e2+1])

print(len(blocks))
for i in blocks:
    print(i)