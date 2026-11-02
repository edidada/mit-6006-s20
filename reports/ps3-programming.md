# MIT 6.006 Spring2020 PS3 编程题

分支edidada/ps3-programming，实现count_anagram_substrings。将字符映射到固定序频次向量，异位词当且仅当向量相同。滑动窗口只减去离开字符并加上进入字符，构建全部窗口签名计数；查询模式只需查签名，重复模式共享计数并保留输出顺序。额外兼容空模式、超长模式、无模式与Unicode，不以排序整窗替代计数。

字母表大小为sigma，文本长n、m个长度k模式，时间O(n*sigma+m*(k+sigma))，最多O(n*sigma)签名存储；课程固定字母表时为O(n+mk)，不能把任意Unicode字母表也称为常数。

独立ps3-programming.yml执行原5测试及二元字母表长度0..6文本、模式长度0..3全部组合的Counter暴力窗口对照，额外验证重复查询/Unicode/不存在字符。原tests.py不变，仅Actions运行。仅编程题验收，书面题未完成。
