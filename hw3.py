def get_fixed_price(a, b) :
    k = (1/(1- a / 100)  )* b
    return int(k)

d = int(input('할인율은? ')) 
A = int(input('A상품의 할인된 가격은? '))
B = int(input('B상품의 할인된 가격은? '))
print('A상품의 정가는', get_fixed_price(d,A), '원')
print('B상품의 정가는', get_fixed_price(d,B), '원')