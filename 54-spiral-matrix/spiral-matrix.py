# LeetCode: Spiral Matrix
# Return all elements of a 2D matrix in spiral order

from typing import List  # import typing for type hints

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Handle empty input quickly
        if not matrix or not matrix[0]:  # if matrix is empty or rows are empty
            return []  # nothing to traverse

        res = []  # this will collect the spiral order

        # Initialize the four boundaries of the current layer
        top = 0  # index of the current top row
        bottom = len(matrix) - 1  # index of the current bottom row
        left = 0  # index of the current left column
        right = len(matrix[0]) - 1  # index of the current right column

        # Continue while the boundaries are valid and not crossed
        while top <= bottom and left <= right:
            # Traverse from left to right along the current top row
            for c in range(left, right + 1):  # columns from left to right inclusive
                res.append(matrix[top][c])  # add each element in the top row
            top += 1  # move the top boundary down since top row is consumed

            # Traverse from top to bottom along the current right column
            for r in range(top, bottom + 1):  # rows from new top to bottom inclusive
                res.append(matrix[r][right])  # add each element in the right column
            right -= 1  # move the right boundary left

            # Traverse from right to left along the current bottom row
            if top <= bottom:  # ensure there is still a row left to traverse
                for c in range(right, left - 1, -1):  # columns from right down to left inclusive
                    res.append(matrix[bottom][c])  # add each element in the bottom row
                bottom -= 1  # move the bottom boundary up

            # Traverse from bottom to top along the current left column
            if left <= right:  # ensure there is still a column left to traverse
                for r in range(bottom, top - 1, -1):  # rows from bottom up to top inclusive
                    res.append(matrix[r][left])  # add each element in the left column
                left += 1  # move the left boundary right

        return res  # final spiral order list