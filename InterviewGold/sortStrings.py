# -*- coding:utf-8 -*-
class SortString:
    #第一步：找出变位词
    #每个变位词集合排序，找出最小的一个
    #取每个变位词集合中最小的一个，组成一个list,再对list进行排序
    #需要借用dict{chat　序列: [变为词]}
    def sortStrings(self, s, n):
        str_dict = {}
        #初始化
        for i in s:
            str_dict["".join(sorted(list(i)))]=[]   #以后千万不要把list作为自己的变量名
        #每一种变位词的集合
        for i in s:
            str_dict["".join(sorted(list(i)))].append(i)
        #取每一个排好序的变位词的集合的第一个字符串，即最小的一个串
        for key in str_dict.keys():
            str_dict[key] = sorted(str_dict[key])[0]
        return_list = []
        for key in str_dict.keys():
            return_list.append(str_dict[key])
        return sorted(return_list)

if __name__=="__main__":
    mySort = SortString()
    result_list = mySort.sortStrings(["emmaldzsvjggzfoda","skmjhsm","zjwmkgufsvwrwyvrhk","vyksgrwwjmwrhzfvuk","wfszrykvjrmuwhkvgw","kwrwuwjvksyvhmrzfg","kom","mko","mko","nezrxmdjgjqexmqz","gjmqdrzqzjeemxxn","qqxedgjjmrznmxez","xxgmjezerjnqmzdq","vwcmmngdsvzx","xvmdvwscgnmz","msnvvczxdgwm","izmvzrhltsiubcukc","cslnzuenr","rznulsenc","lnsnucrez","gkyfvvni","gikvvynf","ivkfyvng","vygfvikn","nwxkeyhnvniquhpapw","wnhyknvanhepwquxip","rrpujexoukmmrnmpdzcf","ksirghrnjx","ixrhgkrnjs","kup","kpu","kpu","emnetqjwnfwi","qpozvklf","qpvkolfz","flpkvoqz","zlkpvfoq","zldjqciktnevrkb","vklqjdrktcebizn","ntrqkvebiljczkd","nkktcebjirqvldz","mytegbucud","gbtcyuemud","gctmuedybu","ahgeomesgcehvk","oamshhecevggek","gmcekevoehsahg","gvgeacmheeoksh","ma","am","am","wxdyddyrenzsylfwx","syedwdylxrwfyxzdn","dwsddyelxywrxyfnz","rdrrfuowxukryfmli","qdjzmdobajs","ymysuotfxpboc","awzccscrkozbhygrkvv","ovrgybhswrczzkcacvk","zcrwkyhrzkgacvsocbv","vzwgzosrkvkcrcybahc","ftytv","ttvyf","tfyvt","vtytf","pggunxuyduy","qijygauutkt","aytqutkugji","itjutqugaky","nfoenumvnmannkkhmueo","ounmkhknefvemnmannou","eonmenfkhmuaonnnumvk","mvnouemekonfamnnnhku","a"],74)
    print(result_list)