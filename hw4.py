n1 = ' Welcome to Seoul.'
n2 = input('Input his/her name:' )

def draw_line_string(n1, n2):
    if len(n1)>len(n2):
        nstr = len(n1)
    else:
        nstr = len(n2)+9
    l = nstr
    mult = '-'*l 
    print('-'*l ,f'\n Hello {n2},',f' \n{n1}',f"\n{mult}")

draw_line_string(n1, n2)