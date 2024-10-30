def check(row, col, num, paper):
    start = paper[row][col]
    for i in range(row, row + num):
        for j in range(col, col + num):
            if start != paper[i][j]:
                return False
    return True

#divide
def divide(row, col, num, paper, result):
    if check(row, col, num, paper):
        result[paper[row][col]] += 1
    else:
        size = num // 3
        for i in range(3):
            for j in range(3):
                divide(row + size * i, col + size * j, size, paper, result)

N = int(input())
paper = []
for i in range(N):
    row = list(map(int, input().split()))
    row = [x + 1 for x in row]  # -1, 0, 1을 0, 1, 2로 변환
    paper.append(row)

result = [0, 0, 0]
divide(0, 0, N, paper, result)
print(result[0])
print(result[1])
print(result[2])
