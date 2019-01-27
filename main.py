import copy
import math
import re


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


def summary(num):
    temp = num
    summer = 0
    while temp:
        summer += temp % 10
        temp = temp // 10
    return summer


def M(num):
    if num < 0:
        num = -1 * num
        num = list(str(num))
        temp = copy.deepcopy(num)
        for enum in range(len(temp)):
            num.insert(len(num), temp[len(temp) - enum - 1])
        return -1*int(''.join(num))
    else:
        num = list(str(num))
        temp = copy.deepcopy(num)
        for enum in range(len(temp)):
            num.insert(len(num), temp[len(temp)-enum-1])
        return int(''.join(num))


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
    if moves - ops_num == 4:
        for i in range(ops_num):
            for j in range(ops_num):
                for k in range(ops_num):
                    for q in range(ops_num):
                        ops = copy.copy(init_ops)
                        ops.append(init_ops[i])
                        ops.append(init_ops[j])
                        ops.append(init_ops[k])
                        ops.append(init_ops[q])
                        Permutation(ops, beg, endl, all_ops)
    if moves - ops_num == 5:
        for i in range(ops_num):
            for j in range(ops_num):
                for k in range(ops_num):
                    for q in range(ops_num):
                        for p in range(ops_num):
                            ops = copy.copy(init_ops)
                            ops.append(init_ops[i])
                            ops.append(init_ops[j])
                            ops.append(init_ops[k])
                            ops.append(init_ops[q])
                            ops.append(init_ops[p])
                            Permutation(ops, beg, endl, all_ops)
    if moves - ops_num == 6:
        for i in range(ops_num):
            for j in range(ops_num):
                for k in range(ops_num):
                    for q in range(ops_num):
                        for p in range(ops_num):
                            for w in  range(ops_num):
                                ops = copy.copy(init_ops)
                                ops.append(init_ops[i])
                                ops.append(init_ops[j])
                                ops.append(init_ops[k])
                                ops.append(init_ops[q])
                                ops.append(init_ops[p])
                                ops.append(init_ops[w])
                                Permutation(ops, beg, endl, all_ops)
elif moves == ops_num:
    Permutation(init_ops, beg, endl, all_ops)

for i in range(len(all_ops)):
    calc_num = copy.deepcopy(init_num)
    influence = 0
    for j in all_ops[i]:
        if j[0] == '[':
            if j[1] == '+':
                influence += int(j[3:])
            elif j[1] == '-':
                influence -= int(j[3:])
        elif j == 'Sign':
            calc_num *= -1
        elif j == 'Mirror':
            calc_num = M(calc_num)
        elif j == 'SUM':
            if calc_num < 0:
                calc_num = -1 * summary(-1 * calc_num)
            else:
                calc_num = summary(calc_num)
        elif j == 'Cube':
            calc_num = calc_num * calc_num * calc_num
        elif j == 'LS':
            if calc_num < 0:
                calc_num = list(str(-1 * calc_num))
                calc_num.insert(len(calc_num), calc_num[0])
                calc_num.remove(calc_num[0])
                calc_num = -1 * int(''.join(calc_num))
            else:
                calc_num = list(str(calc_num))
                calc_num.insert(len(calc_num), calc_num[0])
                calc_num.remove(calc_num[0])
                calc_num = int(''.join(calc_num))
        elif j == 'RS':
            if calc_num < 0:
                calc_num = list(str(-1 * calc_num))
                calc_num.insert(0, calc_num.pop())
                calc_num = -1 * int(''.join(calc_num))
            else:
                calc_num = list(str(calc_num))
                calc_num.insert(0, calc_num.pop())
                calc_num = int(''.join(calc_num))
        elif j == 'Re':
            if calc_num < 0:
                calc_num = list(str(-1 * calc_num))
                calc_num.reverse()
                calc_num = -1 * int(''.join(calc_num))
            else:
                calc_num = list(str(calc_num))
                calc_num.reverse()
                calc_num = int(''.join(calc_num))
        elif j == 'D':
            if calc_num >= 0:
                calc_num = calc_num // 10
            else:
                calc_num = calc_num // 10 + 1
        elif j[0] == 'C':
            arowPos = j.index('>')
            if calc_num < 0:
                calc_num = str(-1 * calc_num)
                calc_num = calc_num.replace(j[1:arowPos], j[(arowPos+1):])
                calc_num = -1 * int(''.join(calc_num))
            else:
                calc_num = str(calc_num)
                calc_num = calc_num.replace(j[1:arowPos], j[(arowPos+1):])
                calc_num = int(''.join(calc_num))
        elif j[0] == 'I':
            if calc_num >= 0:
                if int(j[1:]) + influence == 0:
                    calc_num = calc_num * 10
                else:
                    calc_num = calc_num * pow(10, int(math.log10(int(j[1:]) + influence)) + 1) + int(j[1:])+influence
            else:
                if int(j[1:]) == 0:
                    calc_num = calc_num * 10
                else:
                    calc_num = calc_num * pow(10, int(math.log10(int(j[1:]) + influence)) + 1) - int(j[1:])-influence
        elif j[0] == '+':
            calc_num += (int(j[1:]) + influence)
        elif j[0] == '-':
            calc_num -= (int(j[1:]) + influence)
        elif j[0] == '*':
            calc_num *= (int(j[1:]) + influence)
        elif j[0] == '/':
            if math.modf(calc_num/(int(j[1:])+influence))[0] != 0:
                break
            calc_num = calc_num // (int(j[1:])+influence)
    if calc_num == goal:
        print(all_ops[i])
        break
