#coding=utf-8

"""
最大连续子序列和：
    当遍历到第ｉ个元素 a[i] 的时候，如果前面的最大连续子序列和b[i-1]>0,则b[i]=b[i-1]+a[i],否则b[i]=a[i]
"""
import copy

def max_continuous_subsequence(num_list):
    max_Sequence = []
    maxSum = []

    maxSum.append(num_list[0])
    max_Sequence.append(num_list[0:1])

    for i in range(1, len(num_list)):
        if maxSum[i-1]>0:
            maxSum.append(maxSum[i-1]+num_list[i])
            newSequence = copy.deepcopy(max_Sequence[i-1])
            newSequence.append(num_list[i])
            max_Sequence.append(newSequence)
        else:
            maxSum.append(num_list[i])
            max_Sequence.append(num_list[i:i+1])
    return maxSum, max_Sequence

if __name__=="__main__":
    num_list = [1, 3, -3, 4, -6, -1]
    maxSum, max_Sequence = max_continuous_subsequence(num_list)
    print("最长连续子序列和：", maxSum)
    print("最长连续子序列：", max_Sequence)