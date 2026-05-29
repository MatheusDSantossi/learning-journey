/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
// Didn't solve, because I was missing the reorder of the last value, instead of
// altering the ListNode, I decided to use an Array list first for testing
class Solution {
    public void reorderList(ListNode head) {
        ListNode cur = head.next;
        List<Integer> nums = new ArrayList<>();
        Integer count = 0;
        nums.add(head.val);
        while (cur.next != null) {
            count++;
            if (cur.next.next == null) {
                nums.add(1, cur.next.val);
                nums.add(cur.val);
            }
            if (count == 2) {
                nums.add(2, cur.val);

            } else {
                nums.add(cur.val);
            }
            cur = cur.next;
        }
        nums.remove(2);
        System.out.println("nums: " + nums);
        // return nums;
    }
}

class CommunitySolution {
    public void reorderList(ListNode head) {
       if (head == null) {
        return;
       }

    //    Find the middle node
    ListNode slow = head, fast = head.next;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Reverse the second hald
    ListNode head2 = reverse(slow.next);
    slow.next = null;

    // Link the two halves together
    while (head != null && head2 != null) {
        ListNode tmp1 = head.next;
        ListNode tmp2 = head2.next;
        head2.next = head.next;
        head.next = head2;
        head = tmp1;
        head2 = tmp2;
    }
    }

    private ListNode reverse(ListNode n) {
        ListNode prev = null;
        ListNode cur = n;
        while (cur != null) {
            ListNode tmp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = tmp;
        }

        return prev;
    }
}
