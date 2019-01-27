import copy
import math


# 递归全排列
def Permutation(l, beg, endl, result):
    if beg == endl - 1:
        res = l[:]
        result.append(res)
        return
    for i in range(beg, endl):
        if l[i] in l[beg:i]:
            continue
        l[i], l[beg] = l[beg], l[i]
        Permutation(l, beg+1, endl, result)
        l[beg], l[i] = l[i], l[beg]


# def is_float(str):
#     if str.count('.') == 1:  # 小数有且仅有一个小数点
#         left = str.split('.')[0]  # 小数点左边（整数位，可为正或负）
#         right = str.split('.')[1]  # 小数点右边（小数位，一定为正）
#         lright = ''  # 取整数位的绝对值（排除掉负号）
#         if str.count('-') == 1 and str[0] == '-':  # 如果整数位为负，则第一个元素一定是负号
#             lright = left.split('-')[1]
#         elif str.count('-') == 0:
#             lright = left
#         else:
#             print('%s 不是小数'%str)
#         if right.isdigit() and lright.isdigit():  # 判断整数位的绝对值和小数位是否全部为数字
#             print('%s 是小数'%str)
#         else:
#             print('%s 不是小数'%str)
#     else:
#         print('%s 不是小数'%str)


init_num = int(input('Input the initial number: '))
moves = int(input('Input the moves number: '))
goal = int(input('Input the GOAL: '))
ops_num = int(input('Input the number of operations: '))

init_ops = []
for i in range(ops_num):
    init_ops.append(input('Input all the operations given: '))

beg = 0
endl = moves
all_ops = []
if moves > ops_num:
    if moves - ops_num == 1:
        for i in range(ops_num):
            ops = copy.copy(init_ops)
            ops.append(init_ops[i])
            Permutation(ops, beg, endl, all_ops)
    if moves - ops_num == 2:
        for i in range(ops_num):
            for j in range(ops_num):
                ops = copy.copy(init_ops)
                ops.append(init_ops[i])
                ops.append(init_ops[j])
                Permutation(ops, beg, endl, all_ops)
    if moves - ops_num == 3:
        for i in range(ops_num):
            for j in range(ops_num):
                for k in range(ops_num):
                    ops = copy.copy(init_ops)
                    ops.append(init_ops[i])
                    ops.append(init_ops[j])
                    ops.append(init_ops[k])
                    Permutation(ops, beg, endl, all_ops)
elif moves == ops_num:
    Permutation(init_ops, beg, endl, all_ops)

for i in range(len(all_ops)):
    calc_num = copy.deepcopy(init_num)
    for j in all_ops[i]:
        if j == 'S':
            calc_num *= -1
        if j == 'Re':
            if calc_num < 0:
                calc_num = list(str(-1 * calc_num))
                calc_num.reverse()
                calc_num = -1 * int(''.join(calc_num))
            else:
                calc_num = list(str(calc_num))
                calc_num.reverse()
                calc_num = int(''.join(calc_num))
        if j == 'D':
            if calc_num >= 0:
                calc_num = calc_num // 10
            else:
                calc_num = calc_num // 10 + 1
        if j[0] == 'I':
            if calc_num >= 0:
                calc_num = calc_num * pow(10, int(math.log10(int(j[1:]))) + 1) + int(j[1:])
            else:
                calc_num = calc_num * pow(10, int(math.log10(int(j[1:]))) + 1) - int(j[1:])
        if j[0] == '+':
            calc_num += int(j[1:])
        if j[0] == '-':
            calc_num -= int(j[1:])
        if j[0] == '*':
            calc_num *= int(j[1:])
        if j[0] == '/':
            if math.modf(calc_num/int(j[1:]))[0] != 0:
                break
            calc_num = calc_num // int(j[1:])
    if calc_num == goal:
        print(all_ops[i])
        break
