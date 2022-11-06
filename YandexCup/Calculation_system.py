def convertor(data):
    if data == "-" or data == "+":
        return data
    return int(data) if data.isdigit() else int(ord(data) - 55)


def calculator(data, cs):
    translate = []
    for elem in data:
        temp = elem
        if elem != "-" and elem != "+":
            temp = 0
            for i, value in enumerate(elem):
                temp = temp * cs ** i + convertor(value) 
        translate.append(str(temp))
    return translate


def main():
    left, right = map(str, input().split("="))
    first = []
    second = []
    temp = ""

    for elem in left:
        if elem == "-" or elem == "+":
            first.append(temp)
            first.append(elem)
            temp = ""
        elif elem != " ":
            temp += elem
    first.append(temp)
    temp = ""
    for elem in right:
        if elem == "-" or elem == "+":
            second.append(temp)
            second.append(elem)
            temp = ""
        elif elem != " ":
            temp += elem
    second.append(temp)
    calc_system = max([int(i) + 1 if i.isdigit() else ord(i) - 54 for elem in first + second for i in elem if i != '-' or i != '+'])
    while True:
        one = calculator(first, calc_system)
        two = calculator(second, calc_system)
        if eval(' '.join(str(i) for i in one if i is not None)) == eval(' '.join(str(i) for i in two if i is not None)):
            return calc_system
        if max([int(elem) for elem in one + two if elem != '-' and elem != '+']) < calc_system or calc_system >= 35:
            break
        calc_system += 1
    return -1

if __name__ == "__main__":
    print(main())