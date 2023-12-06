class Solution:


    def threeSum(self, nums):
        

        '''
            题目：提取列表中的三个元素，且三数之和等于0，再用二维列表存放结果
                1.先将列表进行排序，然后进行遍历
                2.需要判断 列表中第一个元素不能大于0，否则永远无法得到三数之和为0的结果。
                3.对三元组中的a元素进行去重，判断a不能等于左边相邻的数，最后得到的三元组需要去重，因为结果中允许两个值重复
                4.接着通过双指针的方式拿到b、c的值，判断三数之和是否为0，若>0，则c往左-1元素，若<0，则b往右+1元素, 最终拿到符合要求的列表，将其追加到二维列表中;
                5.由于当前三元组内三数之和为0，则再出现的 b和c, 出现重复的已经没有意义了，所以需要对b、c进行去重
                6.最后返回二维数组;
        '''

        # 1.
        result = list()
        nums.sort()
        
        for i in range(len(nums)):

            # 2.
            if nums[i] > 0 : return result
            
            
            # 3.判断a与左边相邻的数值不能相等
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 设置双指针
            left = i + 1
            right = len(nums) - 1

            # 4.
            while left < right:
                
                # 获取当前三数之和进行判断是否为0
                _nums = nums[i] + nums[left] + nums[right]

                # 若大于证明c元素过大，需要往左移动并替换
                if _nums > 0:
                    right -= 1
                elif _nums < 0:
                    left += 1
                else:
                    # 等于0
                    result.append([nums[i], nums[left], nums[right]])

                    # 对b、c左去重
                    while right > left and nums[left] == nums[left + 1]: 
                        left += 1

                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 拿到需要的结果后，需要移动b、c的坐标替换值
                    left += 1
                    right -= 1

        return result

if __name__ == '__main__':
    sol = Solution()

    res = sol.threeSum([-1,0,1,2,-1,-4])

    print(res)

    





# class Solution:
#     def threeSum(self, nums):
        

#         nums.sort()

#         result = list()


#         for i in range(len(nums)):

#             if nums[i] > 0: break

#             if i > 0 and nums[i] == nums[i + 1]:
#                 continue

#             left = i + 1
#             right = len(nums) - 1

#             while left < right:

#                 _nums = nums[i] + nums[left] + nums[right]

#                 if _nums < 0:
#                     left += 1

#                 elif _nums > 0:
#                     right -= 1

#                 else:
#                     # 找到三数之和
#                     result.append([nums[i], nums[left], nums[right]])

#                     # 给参数2、3做去重
#                     while right > left and nums[left] == nums[left + 1]:
#                         left += 1
#                     while right > left and nums[right] == nums[right - 1]:
#                         right -= 1

#                     left += 1
#                     right -= 1


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:

#         # 1.排序加遍历
#         nums.sort()

#         # 2.二维列表
#         result = list()

#         for i in range(len(nums)):
            
#             # 3.获取元素1，判断若 > 0，则结束，因为无法再计算出和为0
#             if nums[i] > 0: 
#                 return result

#             # 4.判断 当元素1的下标大于0时，元素1不能与左侧的元素相同，因为要么没有结果，要么已经拿到了想要的三元组结果
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             # 5.开始通过双指针的方式获取元素2、3
#             left = i + 1  # 元素2
#             right = len(nums) - 1  # 元素3

#             while left < right:
#                 # 获取三数之和
#                 _nums = nums[i] + nums[left] + nums[right]

#                 if _nums > 0:
#                     # 表示元素3的值过大，需要往左移动
#                     right -= 1
#                 elif _nums < 0:
#                     # 表示元素2的值过小，需要往右移动
#                     left += 1
#                 else:
#                     # 最终拿到的是三数之和为0的 元素 1、2、3 
#                     result.append([nums[i], nums[left], nums[right]])

#                     # 需要在这里对已经获取过的元素 2、3 进行去重
#                     while right > left and nums[right] == nums[right - 1]:
#                         right -= 1
                    
#                     while right > left and nums[left] == nums[left + 1]:
#                         left += 1

#                     # 提取完毕后，需要对初始的元素 1、2、3 进行移动
#                     right -= 1
#                     left += 1
                
#         return result