'''

'''


def first_task() -> int:
    with open('D:\pythonProject\Kharchenko\lab6\Files Python\input1.txt') as file:
        return len(set(file.read().split()))


def second_task() -> list:
    with open('D:\pythonProject\Kharchenko\lab6\Files Python\input2.txt') as file:
        lines_list = list()
        for line in file.readlines():
            numbers = line.strip().split()
            sum = 0
            for number in numbers:
                sum += int(number)
            lines_list.append(sum)
        return lines_list


def third_task():
    words_freq = {}
    with open('D:\pythonProject\Kharchenko\lab6\Files Python\input3.txt') as file:
        words = file.read().split()
        for word in words:
            if word in words_freq:
                words_freq[word] += 1
            else:
                words_freq[word] = 1

    print(words_freq)


def fourth_task() -> list:
    with open('D:\pythonProject\Kharchenko\lab6\Files Python\input4.txt') as file:
        lines = file.readlines().reverse()
        return lines


def fifth_task():
    with open('D:\pythonProject\Kharchenko\lab6\Files Python\input6.txt') as file:
        lines = file.readlines()
        chars_file = list(file.read())
        symbols = list(".,/-—_(){}[]'@!?^*%$#<>\"")
        without_any_symbols = [word for word in chars_file if not word in symbols]
        chars = 0
        words_all = 0
        print('Строк: ',len(lines))
        for line in lines:
            words = line.strip().split()
            for word in words:
                for char in word:
                    if char.isalpha():
                        chars+=1
                words_all+=1
        print('Слов',words_all)
        print('Букав',chars)
        print('Потеряли 496 слов')

def sixth_task():
    with open('D:\pythonProject\Kharchenko\lab6\Files Python\input6.txt') as file:
        readed = list(file.read())
        readed.reverse()
        s = ''.join(readed)
        return s

def main():
    # print(first_task())
    # print(second_task())
    # print(third_task())
    # print(fourth_task())
     print(fifth_task())
     #print(sixth_task())


if __name__ == "__main__":
    main()
