mat_vec_mul_result = np.dot(matrix_A, vector_x)
print(mat_vec_mul_result)


def solution(mat_A, mat_B):
    answer = [ len(mat_B[0])*[0] for i in range (len(mat_A)) ]
    for i in range (len(answer) ):
        for j in range ( len(answer[i]) ):
            for k in range ( len(mat_A[i] ) ):
                answer[i][j] += mat_A[i][k] * mat_B[k][j]
    return answer