n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

def rotate(u, d):
    for i in range(n-1, 0, -1):
        u[i], d[i] = u[i-1], d[i-1]
        


# Please write your code here.
for i in range(t):
    u_target, d_target = u[-1], d[-1]
    rotate(u, d)
    u[0] = d_target
    d[0] = u_target

print(' '.join(map(str, u)))
print(' '.join(map(str, d)))
