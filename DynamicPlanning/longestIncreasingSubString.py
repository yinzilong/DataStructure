#coding=utf-8

"""
先只求长度
最长递增子串：
    从左到右遍历
    num_list[i] >= num_list[i-1]:  longest_substring_len[i] = longest_substring_len[i-1]+1
    num_list[i] < num_list[i-1]:   longest_substring_len[i] = 1
"""
def longest_increase_subString(num_list):
    if num_list is None:
        return None
    longest_substring_len = []
    longest_substring_len.append(1)    #即longest_substring[0] = 1
    for i in range(1, len(num_list)):
        if num_list[i] >= num_list[i-1]:
            longest_substring_len.append(longest_substring_len[i-1]+1)
        else:
            longest_substring_len.append(1)
    return longest_substring_len

if __name__ == "__main__":
    num_list = [2, 3, 5, 3, 1, 5, 6, 2, 1, 4]

    longest_substring_len = longest_increase_subString(num_list)
    max_len = max(longest_substring_len)
    print("最长递增子串长度：", max_len)
    print("所有的最长递增子串：")
    for i in range(len(longest_substring_len)):
        if longest_substring_len[i] == max_len:
            print(num_list[i-max_len+1:i+1])



