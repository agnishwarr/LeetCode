class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None
        current = root

        while current:
            if not current.left:
                if prev and prev.val > current.val:
                    if not first:
                        first = prev
                    second = current
                prev = current
                current = current.right
            else:
                pred = current.left
                while pred.right and pred.right != current:
                    pred = pred.right
                if not pred.right:
                    pred.right = current
                    current = current.left
                else:
                    pred.right = None
                    if prev and prev.val > current.val:
                        if not first:
                            first = prev
                        second = current
                    prev = current
                    current = current.right

        if first and second:
            first.val, second.val = second.val, first.val
