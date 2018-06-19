#coding=utf-8
import copy
"""
最长公共子序列：
    i:  1-->len(num_list)
    j:  0-->i
    longest[i]=max(longest[j]+1), if num_list[i]>=num_list[j]
    longest[0] = 1
    先仅仅求长度
    以实现拿到单个最长公共序列
"""
def longest_increase_subsequence(num_list):
    if num_list is None:
        return None
    longest = []
    longest_sequence = []

    longest.append(1)   #即longest[0]=1
    longest_sequence.append(num_list[0:1])

    for i in range(1, len(num_list)):
        max_len = 0
        max_subsequence = [num_list[i]]
        for j in range(i):
            if longest[j] > max_len and num_list[i] > num_list[j]:
                max_len = longest[j]
                max_subsequence = copy.deepcopy(longest_sequence[j])
        if max_len > 0:
            longest.append(max_len + 1)
            max_subsequence.append(num_list[i])             #把一行分开成两行了，就没问题了，很奇怪
            longest_sequence.append(max_subsequence)
        else:
            longest.append(1)
            longest_sequence.append(max_subsequence)
    return longest, longest_sequence

if __name__ == "__main__":
    num_list = [2, 3, 5, 3, 1, 5, 6, 2, 1, 4]

    longest, longest_sequence = longest_increase_subsequence(num_list)
    max_len = max(longest)
    print("最长递增子序列：", max_len)
    print("所有的最长递增子序列：")
    #print(longest_sequence)
    for i in range(len(longest)):
        if longest[i] == max_len:
            print(longest_sequence[i])
