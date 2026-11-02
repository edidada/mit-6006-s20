# MIT 6.006 Spring2020 PS1 编程题

分支edidada/ps1-programming，填充原Doubly_Linked_List_Seq六个方法。头尾插入/删除更新双向指针，空表和单节点维持head/tail一致。remove给定有序边界节点，常数次指针写入剥离闭区间，不复制或遍历；splice给定节点后接入L2整链并清空L2，保留节点身份。由题意预条件保证节点属于对应列表；不额外遍历校验以保持O(1)。自拼接拒绝。

每种操作额外空间O(1)，移除区间长度或插入链长度不影响指针操作次数。删除后游离节点断开关联，支持空表重新使用。

独立ps1-programming.yml执行原5个unittest及额外随机1000次链表/Python-list对照。每步检查双向链接、head/tail、无环、节点身份、移除后独立性、splice源表清空和空表异常。原tests.py未改，通过unittest模块运行以确保失败传播退出码。只在Actions测试。

仅验收PS1编程题；其他书面问题未解答，未称完整PS1满分，未向课程网站提交。
