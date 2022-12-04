def first_format_stroki(stroka:str)->str:
    stroka = stroka.strip()
    while '  ' in stroka:
        stroka = stroka.replace('  ',' ')
    stroka = stroka.replace(' .', '.')
    stroka = stroka.replace(' ,', ',')
    stroka = stroka.replace('.','. ')
    stroka = stroka.replace(',', ', ')

    return stroka

def second_palindrom(stroka:str)->str:
    stroka = stroka.strip()
    new_stroka = ''
    for bukva in stroka:
        if bukva.isalpha():
            new_stroka= new_stroka + bukva.lower()
    rev_list = list(new_stroka)
    i = 1
    for bukva in new_stroka:
        if bukva != rev_list[len(rev_list)-i]:
            return 'NO'
        i+=1
    return 'YES'

def third_ryad(number,final_num,stroka:str):
    number+=1
    last_ch = stroka[0::]
    counter = 1
    new_string = ''
    for charact in stroka:
        if charact == last_ch:
            last_ch = charact
            counter +=1
        else:
            new_string = new_string + str(counter) + last_ch
            counter = 0
            last_ch = charact

    return new_string

def main():
    print(first_format_stroki(' fsfd  ,  lkl  . pop  . pilka       ,'))
    print(second_palindrom('Was.it.a.rat.I.saw?'))
    #print(third_ryad(1,4,'111221'))
    pass


if __name__ == "__main__":
    main()