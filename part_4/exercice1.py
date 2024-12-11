def cumulative_sum(numbers):
    cumulative_result = []
    current_sum = 0

    for number in numbers:
        current_sum += number
        cumulative_result.append(current_sum)

    return cumulative_result


numbers = [1, 2, 3]
result = cumulative_sum(numbers)
print(result)
