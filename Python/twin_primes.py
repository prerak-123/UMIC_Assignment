def is_prime(n):
    if n == 1:
        return False
    
    if n%2 == 0:
        return False
    
    p = 3
    
    while p*p <= n:
        if n%p == 0:
            return False
        p += 2 
    
    return True
    
def main():
    n = int(input())
    
    if n == 1:
        start = 1
        end = 7
    
    else:
        start = pow(10, n-1) + 1
        end = pow(10, n) - 3
    
    file = open("myFirstFile.txt",'w')   
         
    while(start <= end):
        if is_prime(start) and is_prime(start+2):
            file.write(str(start) + " " + str(start + 2) + '\n')
        start += 2
    
    file.close()
    return 0
        
main()