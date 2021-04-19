from random import randint
from random import randrange
from random import sample
import time
import json
import math


def reload(d):
    # 解决从json load字典时字典key被转化为str类型导致出错的问题
    d_new = {}
    for i in d.keys():
        d_new[int(i)] = d[i]
    return d_new


def generate_adj_json(N, per_size):
    # 将degree和destination存到json中
    data = {}
    data["degree"] = {}
    data["destination"] = {}
    for i in range(N):
        out_d = randint(6, 16)
        index = sample(range(N), out_d)
        data["degree"][i] = out_d
        data["destination"][i] = index
        if((i+1) % per_size == 0):
            with open(str(i+1)+".json", "w") as f:
                json.dump(data, f)
            f.close()
            data.clear()
            data["degree"] = {}
            data["destination"] = {}


def get_destination(node, per_size):
    num = math.ceil((node+1)/per_size)*per_size
    # 读取json文件中的degree和destination
    with open(str(num)+".json", "r")as f:
        data = json.load(f)
        node = str(node)
        degree = data["degree"][node]
        destination = data["destination"][node]
    return degree, destination


def generate_r_old(N, beta):
    # 生成r_old矩阵
    data = {}
    for i in range(N):
        data[i] = 1/N
    with open("r_old.json", "w")as f:
        json.dump(data, f)
    return data


def save_r(r_old):
    # 保存新的r矩阵
    with open("r_old.json", "w")as f:
        json.dump(r_old, f)


def read_r():
    # 读取r矩阵
    with open("r_old.json", "r")as f:
        r = json.load(f)
        r = reload(r)
    return r


def judge(r_old, r_new, err):
    # 判断err是否满足条件
    v = 0
    for i in r_new.keys():
        v += abs(r_new[i]-r_old[i])
    if(v > err):
        return False
    else:
        return True


def page_rank(N, beta, err):
    generate_r_old(N, beta)
    time.process_time()
    epoch = 0
    while(True):
        print("第", epoch, "次")
        r_old = read_r()
        # initialize all entries of r_new
        r_new = {}
        for i in range(N):
            r_new[i] = (1-beta)/N
        for i in range(N):
            degree, destination = get_destination(
                i, per_size)  # read d,dest into memory
            for k in destination:
                r_new[k] += beta*r_old[i]/degree
        if(judge(r_old, r_new, err)):
            # output result
            result = sorted(
                r_new.items(), key=lambda x: x[1], reverse=True)[:10]
            print(result)
            print("算法执行了", time.process_time(), "秒")
            print("执行了", epoch, "次")
            break
        save_r(r_new)
        epoch += 1
    return r_new


N = 10000
beta = 0.8
err = 0.000001
print("当前实验N值:", N, ",epsilon:", err)
print("-----------pagerank-----------")
if N == 100000:
    per_size = 2000
if N == 1000 or N == 10000:
    per_size = 100
generate_adj_json(N, per_size)
page_rank(N, beta, err)
