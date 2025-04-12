def read_number() :
    k = input('세 자리 정수 입력: ')
    a = k[0]
    b = k[1]
    c = k[2]
    return a, b, c

def read_single_digit(a) :
    if a == 1 :
        return '일'
    elif a == 2 :
        return '이'
    elif a == 3 :
        return '삼'
    elif a == 4 :
        return '사'
    elif a == 5 :
        return '오'
    elif a == 6 :
        return '육'
    elif a == 7 :
        return '칠'
    elif a == 8 :
        return '팔'
    elif a == 9 :
        return '구'
    else:
        return '영'
    
k = read_number()
a = int(k[0])
b = int(k[1])
c = int(k[2])
print(read_single_digit(a),read_single_digit(b),read_single_digit(c))