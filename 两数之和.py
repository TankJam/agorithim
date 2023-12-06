from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            1.定义一个cache缓存字典
            2.通过遍历获取nums的索引与值
            3.通过 target - 遍历的值 -> 得到另一个相加的值
            4.将该 key(得到另一个相加的值) 与 value(遍历值索引) 缓存到cache字典中
            5.判断依次遍历的值是否存在cache中，若存在证明找到了两个数相加等于target的值，最后将cache中只的index与当前遍历值index返回;
        '''
        cache = {}

        for idx, num in enumerate(nums):

            cur = target - num

            if num in cache:
                return [cache[num], idx]
            
            cache[cur] = idx
        

if __name__ == '__main__':
    result = Solution().twoSum([2,7,11,15], 9)
    print(result)
    