import time
import numpy as np


def transpose(A: np.ndarray) -> np.ndarray:
    """Tính ma trận chuyển vị A^T theo định nghĩa (A^T)_{ij} = A_{ji}."""
    A = np.asarray(A)
    if A.ndim != 2:
        raise ValueError("Đầu vào phải là ma trận 2 chiều.")
    m, n = A.shape
    res = np.zeros((n, m), dtype=A.dtype)
    for i in range(m):
        for j in range(n):
            res[j, i] = A[i, j]
    return res


def conjugate_transpose(A: np.ndarray) -> np.ndarray:
    """Tính ma trận chuyển vị liên hợp A^H = conj(A)^T."""
    A = np.asarray(A)
    if A.ndim != 2:
        raise ValueError("Đầu vào phải là ma trận 2 chiều.")
    m, n = A.shape
    res = np.zeros((n, m), dtype=np.complex128 if np.iscomplexobj(A) else A.dtype)
    for i in range(m):
        for j in range(n):
            res[j, i] = np.conjugate(A[i, j])
    return res


def mat_add(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Cộng hai ma trận cùng kích thước C_{ij} = A_{ij} + B_{ij}."""
    A, B = np.asarray(A), np.asarray(B)
    if A.ndim != 2 or B.ndim != 2 or A.shape != B.shape:
        raise ValueError("Hai ma trận phải có cùng kích thước 2 chiều.")
    m, n = A.shape
    res = np.zeros((m, n), dtype=np.result_type(A, B))
    for i in range(m):
        for j in range(n):
            res[i, j] = A[i, j] + B[i, j]
    return res


def mat_mul(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Nhân hai ma trận C_{ij} = sum_k A_{ik} * B_{kj} (không dùng @ hay np.dot)."""
    A, B = np.asarray(A), np.asarray(B)
    if A.ndim != 2 or B.ndim != 2:
        raise ValueError("Đầu vào phải là ma trận 2 chiều.")
    m, p1 = A.shape
    p2, n = B.shape
    if p1 != p2:
        raise ValueError(f"Kích thước không khớp để nhân: {A.shape} và {B.shape}.")
    res = np.zeros((m, n), dtype=np.result_type(A, B, float))
    for i in range(m):
        for k in range(p1):
            a_ik = A[i, k]
            if a_ik != 0:
                for j in range(n):
                    res[i, j] += a_ik * B[k, j]
    return res


def mat_pow(A: np.ndarray, k: int) -> np.ndarray:
    """Tính lũy thừa ma trận vuông A^k (k >= 0) bằng bình phương nhanh."""
    A = np.asarray(A)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("Ma trận phải là ma trận vuông.")
    if not isinstance(k, int) or k < 0:
        raise ValueError("Số mũ k phải là số nguyên không âm.")
    n = A.shape[0]
    res = np.eye(n, dtype=float)
    base = A.astype(float, copy=True)
    while k > 0:
        if k % 2 == 1:
            res = mat_mul(res, base)
        base = mat_mul(base, base)
        k //= 2
    return res


def identify_matrix_types(A: np.ndarray, tol: float = 1e-12) -> dict[str, bool]:
    """Nhận dạng các tính chất đặc biệt của ma trận A."""
    A = np.asarray(A)
    if A.ndim != 2:
        raise ValueError("Đầu vào phải là ma trận 2 chiều.")
    m, n = A.shape
    is_square = (m == n)

    # Kiểm tra bậc thang (echelon)
    is_echelon = True
    last_pivot_col = -1
    zero_row_seen = False
    for i in range(m):
        non_zeros = [j for j in range(n) if abs(A[i, j]) > tol]
        if not non_zeros:
            zero_row_seen = True
        else:
            if zero_row_seen or non_zeros[0] <= last_pivot_col:
                is_echelon = False
                break
            last_pivot_col = non_zeros[0]

    is_upper = is_square and all(abs(A[i, j]) <= tol for i in range(m) for j in range(i))
    is_lower = is_square and all(abs(A[i, j]) <= tol for i in range(m) for j in range(i + 1, n))
    is_diag = is_upper and is_lower
    is_sym = is_square and bool(np.all(np.abs(A - transpose(A)) <= tol))
    is_herm = is_square and bool(np.all(np.abs(A - conjugate_transpose(A)) <= tol))

    return {
        "square": is_square,
        "echelon": is_echelon,
        "upper_triangular": is_upper,
        "lower_triangular": is_lower,
        "diagonal": is_diag,
        "symmetric": is_sym,
        "hermitian": is_herm,
    }


def det_laplace(A: np.ndarray) -> float:
    """Tính định thức bằng khai triển Laplace đệ quy theo hàng 0. Độ phức tạp O(n!)."""
    A = np.asarray(A, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("Ma trận phải vuông để tính định thức.")
    n = A.shape[0]
    if n == 1:
        return float(A[0, 0])
    if n == 2:
        return float(A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0])
    det_val = 0.0
    for j in range(n):
        if A[0, j] != 0:
            sub = np.delete(np.delete(A, 0, axis=0), j, axis=1)
            sign = -1.0 if (j % 2 == 1) else 1.0
            det_val += sign * A[0, j] * det_laplace(sub)
    return float(det_val)


def det_gauss(A: np.ndarray, tol: float = 1e-12) -> float:
    """Tính định thức bằng khử Gauss về dạng tam giác trên có chọn pivot lớn nhất. Độ phức tạp O(n^3)."""
    M = np.array(A, dtype=float, copy=True)
    if M.ndim != 2 or M.shape[0] != M.shape[1]:
        raise ValueError("Ma trận phải vuông để tính định thức.")
    n = M.shape[0]
    sign = 1.0
    for col in range(n):
        pivot_row = col + int(np.argmax(np.abs(M[col:, col])))
        if abs(M[pivot_row, col]) < tol:
            return 0.0
        if pivot_row != col:
            M[[col, pivot_row]] = M[[pivot_row, col]]
            sign = -sign
        for row in range(col + 1, n):
            factor = M[row, col] / M[col, col]
            M[row, col:] -= factor * M[col, col:]
    det_val = sign
    for i in range(n):
        det_val *= M[i, i]
    return float(det_val)


def matrix_rank(A: np.ndarray, tol: float = 1e-12) -> int:
    """Tính hạng của ma trận bằng biến đổi sơ cấp về dạng bậc thang."""
    M = np.array(A, dtype=float, copy=True)
    if M.ndim != 2:
        raise ValueError("Đầu vào phải là ma trận 2 chiều.")
    m, n = M.shape
    rank = 0
    for col in range(n):
        if rank >= m:
            break
        pivot_row = rank + int(np.argmax(np.abs(M[rank:, col])))
        if abs(M[pivot_row, col]) < tol:
            continue
        M[[rank, pivot_row]] = M[[pivot_row, rank]]
        for row in range(rank + 1, m):
            factor = M[row, col] / M[rank, col]
            M[row, col:] -= factor * M[rank, col:]
        rank += 1
    return rank


def inverse_gauss_jordan(A: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    """Tìm ma trận nghịch đảo A^{-1} bằng thuật toán Gauss-Jordan trên (A | I) có partial pivoting."""
    M_in = np.array(A, dtype=float, copy=True)
    if M_in.ndim != 2 or M_in.shape[0] != M_in.shape[1]:
        raise ValueError("Ma trận phải vuông.")
    n = M_in.shape[0]
    aug = np.hstack([M_in, np.eye(n, dtype=float)])

    for col in range(n):
        pivot_row = col + int(np.argmax(np.abs(aug[col:, col])))
        if abs(aug[pivot_row, col]) < tol:
            raise ValueError("Ma trận không khả nghịch (suy biến).")
        if pivot_row != col:
            aug[[col, pivot_row]] = aug[[pivot_row, col]]
        aug[col] = aug[col] / aug[col, col]
        for row in range(n):
            if row != col:
                aug[row] -= aug[row, col] * aug[col]

    return aug[:, n:]


def inverse_adjugate(A: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    """Tìm ma trận nghịch đảo qua công thức A^{-1} = adj(A) / det(A)."""
    M = np.array(A, dtype=float, copy=True)
    if M.ndim != 2 or M.shape[0] != M.shape[1]:
        raise ValueError("Ma trận phải vuông.")
    d = det_gauss(M, tol=tol)
    if abs(d) < tol:
        raise ValueError("Ma trận không khả nghịch (det(A) = 0).")
    n = M.shape[0]
    if n == 1:
        return np.array([[1.0 / M[0, 0]]])
    cofactors = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            sub = np.delete(np.delete(M, i, axis=0), j, axis=1)
            sign = -1.0 if ((i + j) % 2 == 1) else 1.0
            cofactors[i, j] = sign * det_gauss(sub, tol=tol)
    adj = transpose(cofactors)
    return adj / d


def solve_linear_regression_normal_eq(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Bài ứng dụng ML: Giải hệ phương trình chuẩn (X^T X)w = X^T y bằng hàm tự cài."""
    Xt = transpose(X)
    XtX = mat_mul(Xt, X)
    XtX_inv = inverse_gauss_jordan(XtX)
    Xty = mat_mul(Xt, y.reshape(-1, 1))
    w = mat_mul(XtX_inv, Xty)
    return w.ravel()


if __name__ == "__main__":
    # So sánh tốc độ O(n!) vs O(n^3) cho n = 9
    rng = np.random.default_rng(42)
    A_bench = rng.normal(size=(9, 9))
    t0 = time.perf_counter()
    d1 = det_laplace(A_bench)
    t_laplace = time.perf_counter() - t0

    t0 = time.perf_counter()
    d2 = det_gauss(A_bench)
    t_gauss = time.perf_counter() - t0
    print(f"n=9 | Laplace: {t_laplace:.5f}s | Gauss: {t_gauss:.6f}s | Sai lệch: {abs(d1 - d2):.2e}")
