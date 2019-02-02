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

# 求一个正数的各位数字之和
def summary(num):
    temp = num
    summer = 0
    while temp:
        summer += temp % 10
        temp = temp // 10
    return summer

# 将一个数字镜像翻转并与原数字拼接在一起
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


# init_num = int(input('Initial number: '))
# moves = int(input('MOVES: '))
# goal = int(input('GOAL: '))
# ops_num = int(input('Input the number of operations: '))
#
# init_ops = []
# for i in range(ops_num):
#     init_ops.append(input('Input all the operations given: '))

init_num = 4
moves    = 7
goal     = 750
ops_num  = 4
init_ops = ['+6', 'I4', '*3', 'Inv']
patrol_flag = 0
patrol_l = 4
patrol_r = 2

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
                            for w in range(ops_num):
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

store_index = []
for i in range(len(all_ops)):
    for it in all_ops[i]:
        if it == 'Store':
            store_index.append(i)
            break
for i in range(len(store_index)):   # 插入一个Store_S
    temp = copy.deepcopy(all_ops[store_index[i]])
    for index in range(len(temp)):
        temp_a = copy.deepcopy(temp)
        temp_a.insert(index, 'Store_S')
        all_ops.insert(len(all_ops), temp_a)

for i in range(len(store_index)):   # 插入两个Store_S
    temp = copy.deepcopy(all_ops[store_index[i]])
    for index in range(len(temp)-1):
        temp_a = copy.deepcopy(temp)
        temp_a.insert(index, 'Store_S')
        for ttt in range(3-index):
            temp_b = copy.deepcopy(temp_a)
            temp_b.insert(index + ttt + 2, 'Store_S')
            all_ops.insert(len(all_ops), temp_b)

for i in range(len(store_index)):
    all_ops.pop(0)
# print(all_ops)
for i in range(len(all_ops)):
    # pre process of the keyword 'Store'
    Store_num = 0
    # pre process of the keyword '[+]' or '[-]'
    influence = 0
    calc_num = copy.deepcopy(init_num)
    for j in all_ops[i]:
        if j[0] == '[':
            if j[1] == '+':
                influence += int(j[3:])
            elif j[1] == '-':
                influence -= int(j[3:])
        elif j == 'Store_S':
            Store_num = calc_num
        elif j == 'Store':
            if calc_num >= 0:
                if Store_num + influence == 0:
                    calc_num = calc_num * 10
                else:
                    calc_num = calc_num * pow(10, int(math.log10(Store_num + influence)) + 1) + Store_num+influence
            else:
                if int(j[1:]) == 0:
                    calc_num = calc_num * 10
                else:
                    calc_num = calc_num * pow(10, int(math.log10(Store_num + influence)) + 1) - Store_num-influence
        elif j == 'Inv':
            if calc_num < 0:
                calc_num = list(str(-1 * calc_num))
                for ppp in range(len(calc_num)):
                    if calc_num[ppp] == '0':
                        continue
                    calc_num[ppp] = str(10 - int(calc_num[ppp]))
                calc_num = -1 * int(''.join(calc_num))
            else:
                calc_num = list(str(calc_num))
                for ppp in range(len(calc_num)):
                    if calc_num[ppp] == '0':
                        continue
                    calc_num[ppp] = str(10 - int(calc_num[ppp]))
                calc_num = int(''.join(calc_num))
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
        if patrol_flag == 1:
            ss = calc_num//abs(calc_num)
            calc_num = list(str(abs(calc_num)))
            while len(calc_num) >= patrol_l:
                patrol_sum = (int(calc_num[len(calc_num)-patrol_l])+int(calc_num[len(calc_num)-patrol_r]))*pow(10, patrol_r-1)
                patrol_else_sum = 0
                for zzz in range(len(calc_num)):
                    if zzz != patrol_l-1 and zzz != patrol_r-1 and zzz < patrol_l:
                        patrol_else_sum += int(calc_num[len(calc_num) - zzz - 1]) * pow(10, zzz)
                    if zzz >= patrol_l:
                        patrol_else_sum += int(calc_num[len(calc_num) - zzz - 1]) * pow(10, zzz - 1)
                calc_num = patrol_sum + patrol_else_sum
                calc_num = list(str(calc_num))
            calc_num = ss * int(''.join(calc_num))
    if calc_num > 999999:   # 最多6位数
        continue
    if calc_num == goal:
        print(all_ops[i])
        break
