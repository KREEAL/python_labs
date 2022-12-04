def find_all_potomki(chel,slovar):
    if chel not in slovar.keys():
        return 1
    else:
        for person in slovar[chel]:
            return len(slovar[chel]) + find_all_potomki(person,slovar)


def main():
    n= int(input())
    kids_dict = {}
    all_guys_dict= {}
    for _ in range(n-1):
        kid,parent = input().split()
        all_guys_dict[kid]=0
        all_guys_dict[parent] = 0
        if parent not in kids_dict.keys():
            kids_dict[parent] = list()
            kids_dict[parent].append(kid)
        else:
            kids_dict[parent].append(kid)

    for key in kids_dict.keys():
        for kid in kids_dict[key]:
            all_guys_dict[key]=all_guys_dict[key]+find_all_potomki(kid,kids_dict)

    sorted_guys = dict(sorted(all_guys_dict.items()))
    print(sorted_guys)


if __name__ == "__main__":
    main()