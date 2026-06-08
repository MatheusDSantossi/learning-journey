/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// Example in Python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

result = []

def inorder(root):
    if not root:
        return []

    inorder(root.left)
    result.append(root.val)
    inorder(root.right)
    return result

def preorder(root):
    if not root:
        return []
    
    result.append(root.val)
    preorder(root.left)
    preorder(root.right)
    return result

def postorder(root):
    if not root:
        return []

    postorder(root.left)
    postorder(root.right)
    result.append(root.val)
    return result

// ===============
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> nums = new ArrayList<>();
        if (root == null || (root.left == null && root.right == null)) {
            return nums;
        }

        nums.add(root.val);
        TreeNode cur = root;
        while (root.left != null) {
            nums.add(root.left.val);
            cur = root.left;
            break;
        }
        return nums;
    }
}

class YouTubeSolution {
    public List<Integer>  preorderTraversal(TreeNode root) {
        res = [];

        public List<Integer> preorder(node) {
            if (!node) {
                return;
            }

            res.add(node.val);
            preorder(node.left);
            preoder(node.right)
        }
        preorder(root);

        return res;
    }
}


class YouTubeSolution2 {
    List<Integer> preorderTraversal(TreeNode root) {
         List<Integer> res = new ArrayList<>();
        // Stack to simulate recursion. Using ArrayList as a stack
        List<TreeNode> st = new ArrayList<>();

        if(root == null) {
            return res;
        }

        st.add(root);

        while (!st.isEmpty()) {
            TreeNode node = st.remove(st.size() - 1);
            res.add(node.val);

            if (node.right != null) {
                st.add(node.right);
            }

            if (node.left != null) {
                st.add(node.left);
            }

        }

        return res;
    }
}

