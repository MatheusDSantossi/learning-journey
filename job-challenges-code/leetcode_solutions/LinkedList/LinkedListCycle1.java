/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
// !IMPORTANT: This solution solved 25/29 problems, we stuck in the part where the numbers repeat
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }

        if (head.next == null) {
            return false;
        }

        ListNode current = head;
        ArrayList<Integer> numbers = new ArrayList<Integer>();

        System.out.println("current: " + current.val);
        while (current.next != null) {
            System.out.println("current: " + current.val);
            System.out.println("current.next: " + current.next.val);
            // if (current.val > current.next.val) {
            // } else {
            // if(numbers.contains(current.val)) {
            if(numbers.contains(current.val) && numbers.contains(current.next.val)) {
                return true;
            } 
            numbers.add(current.val);
            current = current.next;
              
            }
        // }

        return false;
    }
}

public class TutorialSolution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
}
