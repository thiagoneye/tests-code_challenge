# Functions

def solution(array):
    result = 1
    max_value = max(array)
    current_values = set(array)

    if max_value <= 0:
        pass
    else:
        numbs_values = set(list(range(1, max_value)))
        inters_value = numbs_values.difference(current_values)
        if len(inters_value) == 0:
            result = max_value + 1
        else:
            result = min(list(inters_value))

    return result


# Test

array = [1, 3, 6, 4, 1, 2]
print(solution(array))

array = [1, 3, 6, 5, 4, 1, 2]
print(solution(array))

array = [-2, -1]
print(solution(array))
