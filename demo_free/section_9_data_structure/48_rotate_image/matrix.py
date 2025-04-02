# n x n 的二维矩阵顺时针旋转 90 度 原地完成
class Solution:
    def rotate_image(self, martix: list[list[int]]):
        n = len(martix)

        # Step 1: 转置矩阵
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = \
                    martix[j][i], matrix[i][j]
        
        # Step 2: 反转每一行
        for row in matrix:
            row.reverse()

    def rotate_image_reverse(self, martix: list[list[int]]):
        n = len(martix)

        # Step 1: 转置矩阵
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = \
                    martix[j][i], matrix[i][j]
        
        # Step 2: 反转每一列
        for j in range(n):
            for i in range(n // 2):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]



matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

if __name__ == "__main__":
    solution = Solution()
    ans = solution.rotate_image(
        matrix
    )
    print(ans)