print("Если все цифры введены напишите: готово")
print("Введите количесвто пременных:")
x = int(input())
print("Введите переменных которые нужно отсортировать:")

sob = []
for z in range(x):
    sob.append(int(input()))
    for i in range(len(sob)-1):
        for i in range(len(sob) - 1):
                if sob[i]>sob[i+1]:
                    count = sob[i]
                    sob[i] = sob[i+1]
                    sob[i+1] = count
print (sob)
print()
