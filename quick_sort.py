#!/usr/bin/local/python
# encoding: utf-8

def quick_sort(lists, low, high):
    if low >= high:return lists   # low >= lt-1 或 rt+1 >= high
    lt = low                      # 从左到右移动
    rt = high                     # 从右到左移动
    key = lists[low]              # 保存支点值
    while lt < rt:                # 遍历未结束...
        while lt < rt and lists[rt] >= key:
            rt -= 1               # 过～
        lists[lt] = lists[rt]     # 较小值移到左侧
        while lt < rt and lists[lt] < key:
            lt += 1               # 过～
        lists[rt] = lists[lt]     # 较大值移到右侧
        
    lists[rt] = key               # 支点值替换最后一个被复制的值
    quick_sort(lists, low, lt-1)     # 对支点左侧进行排序
    quick_sort(lists, lt+1, high)    # 对支点右侧进行排序
    
    return lists


if __name__ == '__main__':
    lists = [3, 15, 6, 8, 43, 67, 22]
    quick_sort(lists, 0, len(lists)-1)
    print(lists)
