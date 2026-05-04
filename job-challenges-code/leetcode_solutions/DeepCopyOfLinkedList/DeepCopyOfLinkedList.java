class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;
 
        HashMap<Node, Node> oldToCopy = new HashMap<>();
        Node current = head;

        while (current != null) {
            Node copy = new Node(current.val);
            oldToCopy.put(current, copy);
            current = current.next;
        }

        current = head;

        while (current != null) {
            Node copy = oldToCopy.get(current);
            copy.next = oldToCopy.get(current.next);
            copy.random = oldToCopy.get(current.random);
            current = current.next;
        }
        
        System.out.println(oldToCopy.get(head));

        return oldToCopy.get(head);
    }
}
