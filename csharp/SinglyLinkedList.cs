namespace leetcode;

public class SinglyLinkedList
{
    public ListNode? GetIntersectionNode(ListNode headA, ListNode headB)
    {
        var pa = headA;
        var pb = headB;
        
        while (pa != pb)
        {
            pa = (pa != null) ? pa.Next : headB;
            pb = (pb != null) ? pb.Next : headA;
        }
        
        return pa;
    }
}

public class ListNode(int val = 0, ListNode? next = null)
{
    public int Val { get; set; }
    public ListNode? Next { get; set; }
}