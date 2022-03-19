def main():
    n = str(input())
    digits = len(n)
    
    output = []
    for digit in n:
        output.append(int(digit))
                
    ptr1 = digits//2
    ptr2 = digits - ptr1 - 1
    
    while ptr2 >= 0 and n[ptr2] == '9':
        output[ptr1] = 0
        output[ptr2] = 0
        ptr1 += 1
        ptr2 -= 1

    if ptr2 < 0:
        print(pow(10, digits) + 1)
    
    else:
        if ptr1 == ptr2:
            output[ptr1] += 1
        else:
            output[ptr1] += 1
            output[ptr2] += 1
        print(*output, sep='')
        
    return 0

main()