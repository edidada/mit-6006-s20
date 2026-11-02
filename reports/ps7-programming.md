# MIT 6.006 Spring 2020 PS7 编程题

实现 Shorting Stocks。以每个价格为结尾的最优长度作为状态，前驱只允许同一天的更早价格或前一天，且严格递减；允许从任意一天开始或结束。记录前驱重建序列，再跨公司选最长者。每个状态最多检查 2k 个前驱，时间 O(snk²)，逐公司空间 O(nk)。这与普通最长下降子序列不同，不能跨过整天。

题意依据官方 PS7 第 7-5 题：
https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/3dff7a1ecbc241e9b91b48e69a1588d4_MIT6_006S20_ps7_questions.pdf

独立 ps7-programming.yml 在 GitHub Actions 运行原测试及独立枚举子集的随机 oracle（350 组、两家公司、重复价格、不同日界）。补充测试检查原评分器未明确检查的“不跳天”约束，以及从后一天开始的最优序列。原评分器未修改。本地未执行实验测试。PS7 其余书面题尚未完成。
