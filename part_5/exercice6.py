class ThreeSumFinder:

    def find_three_sum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result


three_sum_finder = ThreeSumFinder()
input_nums = [-25, -10, -7, -3, 2, 4, 8, 10]
output_sets = three_sum_finder.find_three_sum(input_nums)

print("Entrada:", input_nums)
print("Salida:", output_sets)
