def calucate(s):
    stack = []
    opers = ['+', '-', '*', '/','[',']']
    for c in s:
        if c not in opers:
            aux=int(c)
            stack.append(aux)
        else:
            top1 = stack.pop()
            top2 = stack.pop()
            if c == '+':
                stack.append(top2 + top1)
            elif c == '-':
                stack.append(top2 - top1)
            elif c == '*':
                stack.append(top2 * top1)
            elif c == '/':
                stack.append(int(top2 / top1))
    return stack
 
if __name__ == '__main__':
    # s = input().split()
    s = [2, 1 ,'+', 3, '*']
    print(calucate(s))