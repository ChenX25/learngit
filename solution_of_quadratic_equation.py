#!/usr/bin/env python
#coding:utf-8

from math import sqrt

def main():
    print("求解一元二次方程 ax**2 + bx + c = 0 ?\n")

    a = input("请输入a的值(a!=0)：")
    while not a.lstrip('-').replace('.','', 1).isdigit() or float(a)==0:
        a = input("请重新输入非零数值a：")   
    b = input("请输入b的值：")
    while not b.lstrip('-').replace('.','', 1).isdigit():
        b = input("请重新输入数值b：")
    c = input("请输入c的值：")
    while not c.lstrip('-').replace('.','', 1).isdigit():
        b = input("请重新输入数值c：")
    
    print("\n您所输入的数值分别为：a = %s, b = %s, c = %s" % (a, b, c))
    
    a, b, c = float(a), float(b), float(c)
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b-sqrt(delta))/(2*a)
        x2 = (-b+sqrt(delta))/(2*a)
        print("该方程有两个解，分别为：%.2f 和 %.2f 。" % (x1, x2))
    elif delta == 0:
        x = -b/(2*a)
        print("该方程仅有一个解：%.2f 。" % x)
    else:
        print("该方程没有解。")

if __name__ == '__main__':
    main()
