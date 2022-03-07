# Functions

def solution(N):
    for i in range(1, N+1):
        if i == N:
            n_string = ['L' for i in range(N)]
            n_string = ''.join(n_string)
            print(n_string)
        else:
            print('L')


# Test

solution(4)
