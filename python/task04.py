# Functions

def solution(S, K):
    name_numb_dict = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    numb_name_dict = {value: key for (key, value) in name_numb_dict.items()}
    day = name_numb_dict[S]
    new_day = numb_name_dict[(day + K) % 7]
    return new_day


# Test

S = 'Wed'
K = 2
print(solution(S, K))

S = 'Sat'
K = 23
print(solution(S, K))
