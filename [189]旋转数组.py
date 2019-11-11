#给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。 
#
# 示例 1: 
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
#输出: [5,6,7,1,2,3,4]
#解释:
#向右旋转 1 步: [7,1,2,3,4,5,6]
#向右旋转 2 步: [6,7,1,2,3,4,5]
#向右旋转 3 步: [5,6,7,1,2,3,4]
# 
#
# 示例 2: 
#
# 输入: [-1,-100,3,99] 和 k = 2
#输出: [3,99,-1,-100]
#解释: 
#向右旋转 1 步: [99,-1,-100,3]
#向右旋转 2 步: [3,99,-1,-100] 
#
# 说明: 
#
# 
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。 
# 要求使用空间复杂度为 O(1) 的 原地 算法。 
# 
# Related Topics 数组
#leetcode submit region begin(Prohibit modification and deletion)


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        朴素
        时间复杂度 O(n)
        空间复杂度 O(1)
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = [nums[j-k] for j, num in enumerate(nums)]
        return nums


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        拼接
        时间复杂度 O(1)
        空间复杂度 O(1)
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums


class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        翻转
        时间复杂度 O(1)
        空间复杂度 O(1)
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums


class Solution4:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        插入
        时间复杂度 O(k)
        空间复杂度 O(1)
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        for i in range(k):
            nums[:] = nums.insert(0, nums.pop())
        return nums
        
#leetcode submit region end(Prohibit modification and deletion)
