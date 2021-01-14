def my_power(m,n):
    if n==0: return 1
    else:
        return my_power(m, n-1) *m
    
    
print(my_power(2,5))