class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1.判断链表不能为空
        if head == None or head.next == None or k ==0:
            return head

        # 2.链式赋值: 定义初始 链表长度、tail(用于遍历获取链表真实长度，以及链表的最后一个值)
        length, tail = 1, head
        # 3.开始遍历
        while tail.next:
            length, tail = length + 1, tail.next

        # 4.通过取余，获取需要截断的新链表末尾索引位置
        k %= length
        # 若k等于0则无需旋转
        if k == 0:
            return head

        # 5.先将旧链表赋值给pivot，pivot用于作遍历得到最后的要截断的位置
        pivot = head

        # 6.通过遍历到需要截断的位置，遍历赋值给pivot（length - k - 1） 当前k已取余
        # [1, 2, 3, 4, 5]   5 - 2 - 1  === 2
        # pivot = 2 ([1, 2, 3, 4, 5].next)
        # pivot = 3 ([1, 2, 3, 4, 5].next.next)
        # pivot = 3  ---> 3作为末尾的值
        for _ in range(length - k - 1):
            pivot = pivot.next  # 每次遍历更新pivot，获取到最终要截断的位置

        # 7.将老链表末尾的值的下一个，赋值给new_head，作为新链表的head头部
        new_head = pivot.next
        # 8.将老链表头部链接到末尾tail.next后
        tail.next = head
        # 9.最后将截断的pivot末尾的指针赋值为None，完成旋转链表
        pivot.next = None
        return new_head