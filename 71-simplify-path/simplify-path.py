class Solution:
    def simplifyPath(self, path: str) -> str:
        # Use a list as a stack to build the canonical path step by step
        stack = []  # holds valid directory names in order

        # Split by slash to process tokens between slashes
        for part in path.split('/'):
            # Skip empty tokens created by consecutive slashes
            # Skip single dot that means current directory
            if part == '' or part == '.':
                continue

            # Double dot means go to parent directory if possible
            if part == '..':
                if stack:          # only pop if there is a parent
                    stack.pop()
                # if stack is empty we are at root, nothing to pop
                continue

            # Any other token is a valid directory name, push to stack
            stack.append(part)

        # Join the stack with single slashes and ensure leading slash
        # If stack is empty return root
        return '/' + '/'.join(stack)