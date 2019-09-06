#!/usr/bin/local/python
# coding:utf-8

def adjust_heap(lists, i, size):    # 调整堆
    lchild = 2*i +1                 # 左子节点
    rchild = 2*i +2                 # 右子节点
    max_i = i
    if i < size//2:
        if lchild < size and lists[lchild] > lists[max_i]:
            max_i = lchild
        if rchild < size and lists[rchild] > lists[max_i]:
            max_i = rchild
        if max_i != i:              # 最大值，与父节点交换
            lists[max_i], lists[i] = lists[i], lists[max_i]
            adjust_heap(lists, max_i, size)

def heap_sort(lists):
    print('排序前：%s' % lists)
    size = len(lists)
    for i in range(0, size//2)[::-1]:  # 建堆：从最后一个父节点开始调整
        adjust_heap(lists, i, size)
    for i in range(0, size)[::-1]:     # 排序：根结点最大值逐个从后往前
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    print('排序后：%s' % lists)
    

if __name__ == '__main__':
    lists = [3, 5, 8, 1, 66, 23, 9, 15]
    heap_sort(lists)
