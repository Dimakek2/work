



def  convert():
 print("Какие система кодирования?\n"
      
      "Кодирование звука - 1\n"
      "Кодирование инофрмации - 2\n"
      "Введите цифру:")
 r = int(input(""))

 if r == 2:
    print("Какие данные нужно найти?\n"
          "Напоминание:\n"
          "a - число страниц в тексте\n"
          "b - число строк на странице\n"
          "с - число символов в строке\n"
          "k - число символов в тексте\n"
          "I - информационный объём\n"
          "i - информационный вес символа\n"
          "N - мощность алфавита\n"
          "Впишите данные которые необходимо найти в вашей задаче, например: N\n"
          "Введите то что нужно найти:")

    z = str(input(""))
    if z=='N' or z== 'n':
        print("Если данные из списка ниже нет в задачие, пишите 0, например:\n"
              "i=0\n")
        i = int(input("i ="))
        I = int(input("I ="))
        k = int(input("k ="))
        a = int(input("a ="))
        b = int(input("b ="))
        c = int(input("c ="))
        if i>0:
            N=pow(2,i)
            print("Ответ: N=",N)


        elif I>0 and k>0:
                i = I//k
                N=pow(2,i)
                print("Ответ: N=",N)


        elif I>0 and a>0 and b>0 and c>0:
                k = a*b*c
                i=I//k
                N= pow(2,i)
                print("Ответ: N=",N)

    if z=='I':
        print("Если данные из списка ниже нет в задачие, пишите 0, например:\n"
              "i=0\n")

        i = int(input("i ="))
        k = int(input("k ="))
        N = int(input("N ="))
        a = int(input("a ="))
        b = int(input("b ="))
        c = int(input("c ="))
        if  i>0 and k>0:
                I=k*i
                print("Ответ: I=",I)
        elif N>0 and k>0:
                import math
                i = (math.log2(N))
                I = k * i
                print("Ответ: I=",I)
        elif  i>0 and a>0 and b>0 and c>0:

                k = a * b * c
                I= k*i
                print("Ответ: I=",I)

    if z=='k':
                print("Если данные из списка ниже нет в задачие, пишите 0, например:\n"
                "i=0\n")
                a = int(input("a ="))
                b = int(input("b ="))
                c = int(input("c ="))
                i = int(input("i ="))
                I = int(input("I ="))
                if a>0 and b>0 and c>0:

                    k = a * b * c
                    print("Ответ: k=",k)
                elif I>0 and i>0:

                    k=I//i
                    print("Ответ: k=",k)

    if z=='i':
                    print("Если данные из списка ниже нет в задачие, пишите 0, например:\n"
                    "i=0\n")
                    I = int(input("I ="))
                    k = int(input("k ="))
                    a = int(input("a ="))
                    b = int(input("b ="))
                    c = int(input("c ="))
                    if I>0 and k>0:

                        i=I//k
                        print("Ответ: i=",i)
                    elif I>0 and a>0 and b>0 and c>0:

                        k=a*b*c
                        i = I//k
                        print("Ответ: i=",i)
                    elif N>0:
                        import math

                        print("Ответ: i=",math.log2(N))
 if r==1:
    print("Какие данные нужно найти?\n"
          "Напоминание:\n"
          "H - частота дисикридитации (Секунда делить на шаг дискредитации)\n"
          "T - шаг дискредитации(изменение амплитуды сигналы через одинаковые промежутки вермени)\n"
          "K - квантование звука\n"
          "b - битовая глубина\n"
          "I - длина цифрового кода\n"
          "t - время записи звука\n"
          
          "Введите данные, которые вам необхадимо найти, напрмер: H\n"
          "Введите данные:")
    t=str(input())


    if t=='h' or t=='H':
        print("Если данные из списка ниже нет в задачие, пишите 0, например:\n"
              "i=0\n")
        T = int(input("введите T ="))
        I = int(input("Введите I ="))
        t = int(input("Введите t = "))
        b = int(input("Введиет b ="))
        K = int(input("Введиет K ="))
        if T>0:

            H = 1/T
            print("Ответ: H=",H)
        elif I>0 and t>0 and b>0 :

            H = I/(t*b)
            print("Ответ: H=",H)
        elif b>0 and I>0 and t>0 and b>0:

            import math

            b = (math.log2(K))
            H = I/(t*b)
            print("Ответ: H=",H)
    if t == 'T' :
        print("Если данные из списка ниже нет в задачие, пишите 0, например:\n"
              "i=0\n")
        H = int(input("Введите H ="))
        T = int(input("введите T ="))
        I = int(input("Введите I ="))
        t = int(input("Введите t = "))
        b = int(input("Введиет b ="))
        K = int(input("Введиет K ="))
        if H>0:

            T =1/H
            print("Ответ: T=",T)
        elif T>0 and b>0 and I>0:
                H = I / (t * b)
                T = 1 / H
                print("Ответ: H=",H)
        elif I>0 and t>0 and K>0:

                import math

                b = (math.log2(K))
                H = I / (t * b)
                T = 1 / H
                print("Ответ: H=",H)
    if t == 'I'or t=="i":
        print("Если данные из списка ниже нет в задачие, пишите 0, например:\n"
              "i=0\n")
        H = int(input("Введите H ="))
        T = int(input("введите T ="))
        I = int(input("Введите I ="))
        t = int(input("Введите t = "))
        b = int(input("Введиет b ="))
        K = int(input("Введиет K ="))
        if H>0 and t>0 and b>0 :

            I = b*t*H
            print("Ответ: I=",I)
        elif H>0 and t>0 and K>0:

            import math

            b = (math.log2(K))
            I = b * t * H
            print("Ответ: I=",I)
    if t == 't':
        print("Если данные из списка ниже нет в задачие, пишите 0, например:\n"
              "i=0\n")
        H = int(input("Введите H ="))
        T = int(input("введите T ="))
        I = int(input("Введите I ="))
        t = int(input("Введите t = "))
        b = int(input("Введиет b ="))
        K = int(input("Введиет K ="))
        if H>0 and I>0 and b>0 :

            t = I/(H*b)
            print("Ответ: t=",t)
        elif I>0 and b>0 and T>0:

            H = 1 / T
            t = I / (H * b)
            print("Ответ: t=",t)
        elif I>0 and T>0 and K>0:

            import math

            b = (math.log2(K))
            H = 1 / T
            t = I / (H * b)
            print("Ответ: t=",t)
        elif f == ("H I k") or f == ("H k I") or f == ("H I k") or f == ("H k I") or f == ("k H I") or f == ("k H I"):
            H = int(input("Введите H ="))
            I = int(input("Введите I ="))
            K = int(input("Введиет K ="))
            import math

            b = (math.log2(K))
            t = I / (H * b)
            print("Ответ: t=",t)
    if t == 'k':
        print("Если данные из списка ниже нет в задачие, пишите 0, например:\n"
              "i=0\n")
        H = int(input("Введите H ="))
        T = int(input("введите T ="))
        I = int(input("Введите I ="))
        t = int(input("Введите t = "))
        b = int(input("Введиет b ="))
        K = int(input("Введиет K ="))
        if b>0:

            K =pow(2,b)
            print("Ответ: K=",K)
        elif H>0 and I>0 and t>0:

            b = I/(H*t)
            K = pow(2, b)
            print("Ответ: K=",K)
        elif T>0 and I>0 and t>0:

            H = 1 / T
            b = I / (H * t)
            K = pow(2, b)
            print("Ответ: K=",K)
    if t == 'b':
        print("Если данные из списка ниже нет в задачие, пишите 0, например:\n"
              "i=0\n")
        H = int(input("Введите H ="))
        T = int(input("введите T ="))
        I = int(input("Введите I ="))
        t = int(input("Введите t = "))
        b = int(input("Введиет b ="))
        K = int(input("Введиет K ="))
        if H>0 and I>0 and t>0:

            b = I / (H * t)
            print("Ответ: b=",b)



        elif I>0 and t>0 and T>0:
            H = 1 / T
            b = I / (H * t)

            print("Ответ: b=",b)
        elif K>0:
            K = int(input("Введиет K ="))
            import math
            b = (math.log2(K))
            print("Ответ: b=",b)
convert()
while True:
    print("                               \n"
          "Введите 1 если хотите вернуться в начало или нажмите enter для выхода из программы\n"
          )
    flag = int(input())

    if flag == 1:
        convert()
    else:
        break
input()