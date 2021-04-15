from random import randint
from random import randrange
from random import sample
import time


def generate_column(column):
    out_d = randint(6, 16)  # 随机获取出度,6,16
    index = sample(range(len(column)), out_d)  # 选出d行
    for i in index:
        column[i] = 1/out_d  # 修改值
    return column


def generate_adj(N):
    # 生成迁移矩阵
    adj = []
    for i in range(N):
        n = [0 for i in range(N)]
        adj.append(generate_column(n))
    return adj


def judge(r_new, r_old, err):
    # 判断误差
    v = 0
    for i in range(len(r_new)):
        v += abs(r_new[i]-r_old[i])
    print("误差为:", v)
    if(v > err):
        # 大于误差返回False
        return False
    else:
        # 小于误差返回True
        return True


def get_value(adj, n):
    a = []
    for i in adj:
        a.append(i[n])
    return a


def count_value(adj, r_old):
    # 设置beta
    beta = 0.8
    r_new = r_old[:]
    for i in range(len(r_old)):  # 概率矩阵相乘
        v = 0
        l = get_value(adj, i)
        for n in range(len(l)):
            v += l[n]*r_old[n]  # 矩阵乘法
        r_new[i] = beta*v + (1-beta)/len(r_old)

    return r_new


def page_rank(adj, err):
    r_old = [1/len(adj) for i in range(len(adj))]  # 以1/N为值创建r矩阵
    epoch = 1
    time.process_time()
    while True:
        r_new = count_value(adj, r_old)
        if(judge(r_new, r_old, err)):
            break
        r_old = r_new[:]  # 更新r_new矩阵
        epoch += 1
    print("算法执行了", time.process_time(), "秒")
    print("执行了", epoch, "次")
    return r_new


if __name__ == "__main__":
    N = 1000
    epsilon = 0.00001  # 误差
    adj = generate_adj(N)
    print("当前实验N值:", N, ",epsilon:", epsilon)
    print("-----------pagerank-----------")
    result = page_rank(adj, epsilon)
    result.sort(reverse=True)  # 对r值进行排序
    print(result[:9])  # 输出前10个
