#!/usr/bin/python3
# Problem: Add the first the items of 2 list
# Example: list1 = [1,2,3,4,5], list2 = [1,2,3], result is [2,4,6]

class Solution:
    def sumOfThree(self, inputList1, inputList2):
        ans = list()
        firstLength = len(inputList1)
        secondLength = len(inputList2)
        # make sure each list have equal length
        diff = firstLength-secondLength if firstLength > secondLength else secondLength-firstLength
        # print(diff)
        if diff == 0:
            for i in range(len(inputList1)):
                ans.append(inputList1[i] + inputList2[i])
        elif len(inputList1) > len(inputList2):
            for _ in range(diff):
                inputList2.append(0)
            for i in range(len(inputList1)):
                ans.append(inputList1[i] + inputList2[i])
        else:
            for _ in range(diff):
                inputList1.append(0)
            for i in range(len(inputList1)):
                ans.append(inputList1[i] + inputList2[i])
            # print(inputList1)
            # print(inputList2)
        if len(ans) < 3:
            ans_diff = 3 - len(ans)
            for _ in range(ans_diff):
                ans.append(0)
        return ans[:3]
    
if __name__== '__main__':
    driver = Solution()
    print(driver.sumOfThree([0,1,2], [1,0,5,6]))
    print(driver.sumOfThree([1,2], [1,0,5,6]))
    print(driver.sumOfThree([1,2], [1,6]))
