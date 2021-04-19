# PageRank
pagerank-google based on python  
PageRank.py实现了google无死胡同的pagerank算法,M数组于r数组存于内存中，无法计算大型数据集，因此对算法进行优化  
# 优化  
new_PageRank1.py在原有的基础上使用表存储，分别存储节点名、节点度大小、节点出度的target。  
将表写入本地的json文件，每2000/100个节点的信息存为一个json文件（根据节点的多少修改）。  
在算法执行的loop阶段使用函数对json文件进行读写。  
原算法执行10000个节点运算需要大概几个小时，优化后10000个节点只需要26s.
# 关于数据集  
随机生成使用1000/10000/100000个节点的图，每个节点随机地赋予6-16个出度
