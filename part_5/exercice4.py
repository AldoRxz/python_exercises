class SubsetGenerator:
    def get_subsets(self, nums):
        result = []
        self.generate(nums, 0, [], result)
        return result

    def generate(self, nums, index, current_subset, result):
        result.append(list(current_subset))

        for i in range(index, len(nums)):
            current_subset.append(nums[i])
            self.generate(nums, i + 1, current_subset, result)
            current_subset.pop()

# Ejemplo de uso
subset_generator = SubsetGenerator()
input_nums = [4, 5, 6]
output_subsets = subset_generator.get_subsets(input_nums)

print("Entrada:", input_nums)
print("Salida:", output_subsets)
