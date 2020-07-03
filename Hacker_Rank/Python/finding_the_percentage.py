if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l = student_marks[query_name]
    sum = 0
    for i in range(3):
        sum += l[i]
    sum = float(sum/3)
    print('%.2f'%sum)
