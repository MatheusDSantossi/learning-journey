public class BinaryTreePostOrderTraversal {
    class Solution {
        public List<Integer> postorderTraversal(TreeNode root) {
            List<Integer> result = new ArrayList<>();

            return postorder(root, result);
        }

        private List<Integer> postorder(TreeNode node, List<Integer> result) {
            if (node == null) {
                return result;
            }

            postorder(node.left, result);
            postorder(node.right, result);
            result.add(node.val);

            return result;
        }
    }
}
