class Solution:
    def maxProduct(self, nums):

        # run kadane from front and back

        maxi = float('-inf')
        prod = 1

        for i in range(len(nums)):
            prod *= nums[i]
            maxi = max(prod, maxi)

            if prod == 0:
                prod = 1

        prod = 1
        maxi2 = float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            maxi2 = max(prod, maxi2)

            if prod == 0:
                prod = 1

        return max(maxi, maxi2)