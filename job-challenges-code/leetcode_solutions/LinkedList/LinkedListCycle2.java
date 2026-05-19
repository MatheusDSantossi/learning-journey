// !IMPORTANT: It worked, but it tooks 5ms to solve it
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }
        System.out.println("head.val: " + head.val);
        
        ListNode cur = head;
        HashMap<ListNode, Integer> nodeMap = new HashMap<>();
        while (cur.next != null) {
            if(nodeMap.get(cur) != null) {
                return cur;
            }
            nodeMap.put(cur, cur.val);
            cur = cur.next;
        }
        return null;
    }
}

public class CommunitySolution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) break;
        }
        if (fast == null || fast.next == null) return null;
        while (head != slow) {
            head = head.next;
            slow = slow.next;
        }
        return head;
    }
}
