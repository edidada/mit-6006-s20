# MIT 6.006 Spring2020 PS4 编程题

分支edidada/ps4-programming。保留原AVL_Tree/Set_AVL_Tree，仅扩充Part_B_Node与Part_B_Tree并实现tastiest_slice。每个子树维护总和total、最大非空前缀best及其终点best_key。前缀只能在左子树结束、在根结束、或包含左子树和根再接右子树前缀，取三种最大值即可；原旋转调用subtree_update，扩充量随重平衡维护。查询根的best为O(1)，允许空前缀得0。

按x升序扫描，逐个把y对应权值累加进AVL。同x的所有点先全部加入再查询，避免切片边界错误地只包含同x的部分点。每步最大y前缀即所有px<=X且py<=Y的最大得分，严格提高全局最优时记录坐标。n点排序和插入总时间O(n log n)、空间O(n)。

原5测试保留。额外500组含重复坐标/负权的随机点，与枚举所有坐标边界暴力对照；另随机插入300节点逐步对照排序前缀，验证AVL旋转后的扩充量。仅Actions运行，单独ps4-programming.yml。书面题未完成，不宣称完整PS4验收。
