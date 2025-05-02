shopping_bag = {}
print('[구입]')
while True :
    item = input('상품명? ')
    if item != '' :
        count_item = int(input('수량은? '))
        print(f'장바구니에{item}{count_item}개가 담겼습니다')
    elif item == '' :
        break
    shopping_bag[item] = count_item
print(f'>>> 장바구니 보기 : {shopping_bag}')
print('[검색]')
k = input('장바구니에 확인하고자 하는 상품은? ')
k1= shopping_bag.get(k)
print(f'{k}은(는) {k1}개 담겨있습니다')