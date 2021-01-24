# i am really glad i can get to show the beauty of recursion through this solution

def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n - 1, A, C, B)
        print(f"{A} , {C}")
        hanoi(n - 1, B, A, C)

hanoi(3, 1,2,3)