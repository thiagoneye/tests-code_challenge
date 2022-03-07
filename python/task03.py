# Functions

def solution(D, S):
    numbs_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    return D*numbs_dict[S]


# Test

print(solution(4, 'two'))
