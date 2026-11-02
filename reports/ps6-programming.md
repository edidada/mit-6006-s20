# MIT 6.006 Spring2020 PS6 编程题

分支edidada/ps6-programming，实现Johnson全点对最短路。势能初始化全0等价于增加到所有顶点的零边超级源；Bellman-Ford全局松弛，第n轮仍变化即存在负环，包括不连通分量中的负环。重赋权w'=w+h[u]-h[v]非负，逐源Dijkstra后还原距离d=d'-h[source]+h[target]。

内部无穷用float inf，避免原外部INF=99999被重赋权中间路径越过而误判不可达；仅最终输出不可达时转换为题目INF。边表保留平行边，不在字典中静默丢失较优边。原提供bellman_ford/dijkstra/PriorityQueue不改，本实现使用heapq跳过陈旧条目。二叉堆允许重复入队，时间O(VE+V(E+V)log(E+V))，空间含输出O(V²+E)。

独立ps6-programming.yml运行原5测试，加500个小随机含负边图对照独立Floyd-Warshall，覆盖负自环、不连通负环、平行边、空图与不可达。只在Actions运行，其他书面题未完成。
