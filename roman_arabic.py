def convert(num):
    if num == 1:
        return "I"
    elif num == 5:
        return "V"
    elif num == 10:
        return "X"
    elif num == 50:
        return "L"
    elif num == 100:
        return "C"
    elif num == 500:
        return "D"
    elif num == 1000:
        return "M"
    return None


 
def convertor(num):
    if num == "I":
        return 1
    elif num == "V":
        return 5
    elif num == "X":
        return 10
    elif num == "L":
        return 50
    elif num == "C":
        return 100
    elif num == "D":
        return 500
    elif num == "M":
        return 1000
    return None


def nearNum(num, bias, o_rank):
    answer1 = answer2 = None
    if convert(num) == None and num > 0:
        if bias <= 0 and num <= 1000:
            answer1 = nearNum(num + 1 * o_rank, bias - 1 * o_rank, o_rank)
        if bias >= 0:
            answer2 = nearNum(num - 1 * o_rank, bias + 1 * o_rank, o_rank)
        if answer1 is not None: 
            return answer1 
        return answer2
    else:
        val = bias // 10**(len(str(bias)) - 1)
        answer = convert(num)
        if bias > 3 * o_rank or bias < -1 * o_rank:
            return None
        elif num == 0:
            return ""
        elif bias >= 0:
            if bias != 0:
                return answer + convert(bias // val) * val
            return answer
        return convert(bias // val) + answer
 

def arabToRome(number):
    try:
        if type(int(number)) == int and 0 < int(number) < 4000:
            answer = ""
            count = len(number) - 1
            for num in number:
                answer += nearNum(int(num) * 10**count, 0, 10**(len(str(int(num) * 10**count)) - 1))
                count -= 1
            return answer
        if int(number) >= 4000:
            return "Максимальное число 3999"
        if int(number) < 0:
            return "Минимальное число 0"
        if int(number) == 0:
            return "N"
    except:
        return "Не число"


def romeToArab(number):
    try:
        numbers = list()
        answer = 0
        for num in number:
            numbers.append(convertor(num.upper()))
        for index, num in enumerate(numbers):
            if index > 0:
                if num <= numbers[index - 1]:
                    answer += num
                elif index > 1:
                    if num > numbers[index - 1] and numbers[index - 1] * 10 == num and num <= numbers[index - 2]:
                        answer = answer - numbers[index - 1] * 2 + num
                    else:
                        return "Это не римское число"
                elif num > numbers[index - 1] and numbers[index - 1] * 10 == num:
                    answer = answer - numbers[index - 1] * 2 + num
                else:
                    return "Это не римское число"
                    
            else:
                answer += num
        return answer if answer is not None else "Это не римское число!"
    except:
        return "Это не римское число"


def main():
    try:
        while True:
            programm = input("\n\nКонвертор арабских и римских чисел! \
                \nРежимы работы\n1 - арабские в римские \
                \n2 - римские в арабские\n3 - выход\nВыберите режим: ")
            if programm == '1':
                try:
                    while True:
                        print(arabToRome(input("\nВведите число: ")))
                except:
                    pass
            elif programm == '2': 
                try:
                    while True:
                        print(romeToArab(input("\nВведите число: ")))
                except:
                    pass
            elif programm == '3':
                break

    except:
        pass


if __name__ == "__main__":
    main()

