class TwoSumFinder:
    def find_two_sum(self, nums, target):
        num_indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i
        return None

# Ejemplo de uso
two_sum_finder = TwoSumFinder()
input_nums = [10, 20, 10, 40, 50, 60, 70]
target_sum = 50
output_indices = two_sum_finder.find_two_sum(input_nums, target_sum)

print("Entrada:", input_nums)
print("Objetivo:", target_sum)
print("Salida:", output_indices)
