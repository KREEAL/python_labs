def input_list() -> list:
    n = int(input())
    l = []
    for _ in range(0, n):
        list.append(int(input()))
    return l


def first_task(l: list) -> int:
    max_el = max(l)
    counter = 0
    max_count = 0
    for element in l:
        if element == max_el:
            counter = counter + 1
            if counter > max_count:
                max_count = counter
        else:
            if counter > max_count:
                max_count = counter
            counter = 0
    return max_count

def second_task(l:list)->int:
    counter=0
    max_len = 0
    bool_up = True
    pass

def compare_mid_left(left: int, middle: int, right=0, isTwo=True) -> bool:
    if isTwo:
        return middle > left
    else:
        return left < middle < right


def third_task(l: list) -> int:
    counter = 0
    locals = []
    for i in range(0, len(l)):
        if i == 0:
            if l[i] > l[i + 1]:
                counter += 1
        if i == len(l) - 1:
            if l[i] > l[i - 1]:
                counter += 1
        if 0 < i < len(l) - 1:
            if l[i - 1] < l[i] > l[i + 1]:
                counter += 1
    return counter


def fourth_task(l: list) -> int:
    localc_maxs = []
    for i in range(0, len(l)):
        if i == 0:
            if l[i] > l[i + 1]:
                localc_maxs.append(i)
        if i == len(l) - 1:
            if l[i] > l[i - 1]:
                localc_maxs.append(i)
        if 0 < i < len(l) - 1:
            if l[i - 1] < l[i] > l[i + 1]:
                localc_maxs.append(i)
    min_len = 0
    current_len = len(localc_maxs)
    for i in range(0, len(localc_maxs)):
        for j in range(i, len(localc_maxs)):
            current_len = localc_maxs[j] - localc_maxs[i]
            if min_len < current_len:
                min_len = current_len

    return min_len


def main():
    # l=input_list()
    l = [1, 2, 3, 6, 8, 6, 6, 5, 3, 6]
    print(first_task(l))
    # print(second_task(l))
    print(third_task(l))
    print(fourth_task(l))


if __name__ == '__main__':
    main()
