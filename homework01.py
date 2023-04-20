number = abs(int(input("Введите число N: ")))
if number > 1:
    fibonachi = [1, 1]
    for _ in range(2, number):
        fibonachi.append(fibonachi[-1] + fibonachi[-2])
else:
    fibonachi = [1]
print(fibonachi)