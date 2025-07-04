class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        from collections import defaultdict

        ball_to_color = {}
        color_count = defaultdict(int)
        result = []

        for x, y in queries:
            if x in ball_to_color:
                old_color = ball_to_color[x]
                if old_color != y:
                    color_count[old_color] -= 1
                    if color_count[old_color] == 0:
                        del color_count[old_color]
                    color_count[y] += 1
                    ball_to_color[x] = y
            else:
                ball_to_color[x] = y
                color_count[y] += 1

            result.append(len(color_count))

        return result
