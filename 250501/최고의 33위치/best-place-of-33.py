n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def get_num_of_gold(row_s, col_s): # row_s + 2, col_s + 2
    gold_count = 0
    for i in range(row_s, row_s + 3):
        for j in range(col_s, col_s + 3):
            if grid[i][j] == 1:
                gold_count += 1
    return gold_count

max_gold = 0

for i in range(n-2):
    for j in range(n-2):
        max_gold = max(max_gold, get_num_of_gold(i, j))

print(max_gold)