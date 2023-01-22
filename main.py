# Yashenko Dmitry lab 1
import random
def printStars():
    print("**********")

def task1():
    number = random.randint(1,100)
    print(number)
    iterationCounter = 0
    answer = 0
    intAnswer = int(answer)
    while answer != number:
        iterationCounter +=1
        print("Введите число:")
        answer = input()
        intAnswer = int(answer)
        difference = intAnswer - number
        print(abs(difference))
        if intAnswer == number:
            print("Правильно!" + " \n Количество попыток = " + str(iterationCounter))
            break
        elif  abs(difference) <= 33:
            st = "Горячо"
            print(st)
        elif abs(difference) <= 34 | abs(difference) <= 50:
            st = "Тепло"
            print(st)
        elif abs(difference) >= 51:
            st = "Холодно"
            print(st)

def task2():  # task2
    counterIteration = 0
    # print("Введите минимальное число")
    minNum = 1
    # print("Введите максимальное число")
    maxNum = 99
    answer = ""
    middleNum = (maxNum + minNum) / 2

    for i in range(7):
        print("Ваше число - " + str(middleNum) + "?\n" +
              "Нажмите \"+\", если загаданное число больше \n " +
              "\"-\" если загаданное число меньше \n " +
              "\"=\" если это загаданное число")
        answer = input()
        if (answer == "+"):
            minNum = middleNum
            middleNum = (maxNum + minNum) / 2
            counterIteration += 1
        elif (answer == "-"):
            maxNum = middleNum
            middleNum = (maxNum + minNum) / 2
            counterIteration += 1
        elif (answer == "="):
            print("Ваше число = " + str(middleNum) + "\n Понадобилось " + str(counterIteration) + " итераций")
        elif (answer != "+" | answer != "-" | answer != "="):
            print("Попробуйте еще раз! Вы ввели неправильный символ") #

def task3():
    print("Введите шестизначное число")
    try:
        startNumber = int(input())
    except ValueError:
        print("Вы читать умеете? Вам сказано было: Ч И С Л О")
        number = random.randint(1, 10000)
    print(startNumber)
    number = startNumber
    max = 0
    for i in range(7):
            i = 0
            div = number % 10
            if div > max:
                max = div
          #  multip *= 10
            print("div is " + str(div))
            number //= 10
            print("num is " + str(number))
            printStars()
           # i+=1
          #  if i == 7:
           #     for j in range(6):
           #         div = number % 10
           #         if div == max:
           #             max = div


#def task4():


def task5():
    jellysJuice = ["Вишневый", "Кола", "Яблочный", "Ананас", "Пиво"]
    jellysForm = ["Мишка", "Бутылка", "Червяк", "Панда", "Звездочка"]
    juice = random.randint(1,5)
    form = random.randint(1, 5)
    print("Вкус: " + jellysJuice[juice])
    print("Форма: " + jellysForm[form])

task5()