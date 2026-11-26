import numpy as np
from chapters.ch1_linear_algebra.src.ch1 import (
    transpose,
    mat_mul,
    det_gauss,
    inverse_gauss_jordan,
)


def _rref(A: np.ndarray, tol: float = 1e-12) -> tuple[np.ndarray, list[int]]:
    """Đưa ma trận về dạng bậc thang rút gọn (RREF) và trả về danh sách chỉ số cột pivot."""
    M = np.array(A, dtype=float, copy=True)
    m, n = M.shape
    pivot_cols: list[int] = []
    row = 0
    for col in range(n):
        if row >= m:
            break
        pivot_row = row + int(np.argmax(np.abs(M[row:, col])))
        if abs(M[pivot_row, col]) < tol:
            continue
        M[[row, pivot_row]] = M[[pivot_row, row]]
        M[row] = M[row] / M[row, col]
        for r in range(m):
            if r != row:
                M[r] -= M[r, col] * M[row]
        pivot_cols.append(col)
        row += 1
    return M, pivot_cols


def is_linearly_independent(vectors: np.ndarray, tol: float = 1e-12) -> bool:
    """Kiểm tra hệ các vector cột có độc lập tuyến tính hay không."""
    V = np.asarray(vectors, dtype=float)
    if V.ndim != 2:
        raise ValueError("Đầu vào phải là ma trận 2D (mỗi cột là một vector).")
    _, pivot_cols = _rref(V, tol=tol)
    return len(pivot_cols) == V.shape[1]


def extract_basis(vectors: np.ndarray, tol: float = 1e-12) -> tuple[np.ndarray, int]:
    """Trích cơ sở từ hệ sinh (các cột của ma trận vectors) và trả về (cơ sở, số chiều)."""
    V = np.asarray(vectors, dtype=float)
    if V.ndim != 2:
        raise ValueError("Đầu vào phải là ma trận 2D.")
    _, pivot_cols = _rref(V, tol=tol)
    basis = V[:, pivot_cols].copy()
    return basis, len(pivot_cols)


def vector_norm(x: np.ndarray, p: float = 2) -> float:
    """Tính chuẩn vector: Euclid (p=2), Max (p=np.inf), và chuẩn l_p tổng quát."""
    v = np.asarray(x, dtype=float).ravel()
    if v.size == 0:
        raise ValueError("Vector không được rỗng.")
    if p == np.inf:
        return float(np.max(np.abs(v)))
    if p < 1:
        raise ValueError("Bậc chuẩn p phải >= 1.")
    return float(np.sum(np.abs(v) ** p) ** (1.0 / p))


def frobenius_norm(A: np.ndarray) -> float:
    """Tính chuẩn Frobenius ||A||_F = sqrt(sum_{i,j} |A_{ij}|^2)."""
    M = np.asarray(A, dtype=float)
    if M.ndim != 2:
        raise ValueError("Đầu vào phải là ma trận 2D.")
    return float(np.sqrt(np.sum(np.abs(M) ** 2)))


def change_of_basis_matrix(B: np.ndarray, S: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    """Tìm ma trận chuyển P(B->S) bằng thuật toán (B | S) -> (I | P), sao cho [u]_B = P @ [u]_S."""
    B_mat = np.array(B, dtype=float, copy=True)
    S_mat = np.array(S, dtype=float, copy=True)
    if B_mat.ndim != 2 or B_mat.shape != S_mat.shape or B_mat.shape[0] != B_mat.shape[1]:
        raise ValueError("B và S phải là hai ma trận vuông cùng kích thước.")
    n = B_mat.shape[0]
    aug = np.hstack([B_mat, S_mat])
    rref_aug, pivot_cols = _rref(aug, tol=tol)
    if len(pivot_cols) < n or pivot_cols[-1] >= n:
        raise ValueError("Hệ vector B không phải là cơ sở (ma trận suy biến).")
    return rref_aug[:, n:]


def gram_schmidt(V: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    """Trực chuẩn hóa hệ vector cột độc lập tuyến tính V bằng Gram-Schmidt."""
    A = np.array(V, dtype=float, copy=True)
    if A.ndim != 2:
        raise ValueError("Đầu vào phải là ma trận 2D.")
    m, n = A.shape
    Q = np.zeros((m, n), dtype=float)
    for j in range(n):
        u = A[:, j].copy()
        for i in range(j):
            q_i = Q[:, i]
            proj = float(np.sum(q_i * u))
            u -= proj * q_i
        norm_u = vector_norm(u, p=2)
        if norm_u < tol:
            raise ValueError("Hệ vector đầu vào phụ thuộc tuyến tính.")
        Q[:, j] = u / norm_u
    return Q


def linear_map_analysis(A: np.ndarray, tol: float = 1e-12) -> dict:
    """Phân tích ánh xạ tuyến tính f(x) = Ax: tìm cơ sở Im(f), Ker(f) và kiểm tra định lý số chiều."""
    M = np.array(A, dtype=float, copy=True)
    if M.ndim != 2:
        raise ValueError("Ma trận ánh xạ phải là 2 chiều.")
    m, n = M.shape
    rref_M, pivot_cols = _rref(M, tol=tol)
    im_basis = M[:, pivot_cols].copy()

    # Tìm cơ sở của Ker(f) từ các biến tự do
    free_cols = [c for c in range(n) if c not in pivot_cols]
    ker_vectors = []
    for free_c in free_cols:
        vec = np.zeros(n, dtype=float)
        vec[free_c] = 1.0
        for r_idx, p_col in enumerate(pivot_cols):
            vec[p_col] = -rref_M[r_idx, free_c]
        ker_vectors.append(vec)

    ker_basis = np.column_stack(ker_vectors) if ker_vectors else np.zeros((n, 0), dtype=float)
    dim_im = im_basis.shape[1]
    dim_ker = ker_basis.shape[1]

    return {
        "im_basis": im_basis,
        "ker_basis": ker_basis,
        "dim_im": dim_im,
        "dim_ker": dim_ker,
        "rank_nullity_holds": (dim_im + dim_ker == n),
    }


def similar_matrix(A: np.ndarray, P: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    """Tính ma trận đồng dạng A' = P^{-1} A P."""
    P_inv = inverse_gauss_jordan(P, tol=tol)
    return mat_mul(mat_mul(P_inv, A), P)


def eigen_symmetric_jacobi(
    A: np.ndarray, tol: float = 1e-12, max_iter: int = 1000
) -> tuple[np.ndarray, np.ndarray]:
    """Chéo hóa trực giao ma trận đối xứng thực A = P D P^T bằng phương pháp quay Jacobi."""
    M = np.array(A, dtype=float, copy=True)
    if M.ndim != 2 or M.shape[0] != M.shape[1]:
        raise ValueError("Ma trận phải vuông.")
    if not np.allclose(M, transpose(M), atol=tol):
        raise ValueError("Phương pháp Jacobi yêu cầu ma trận đối xứng thực.")
    n = M.shape[0]
    P = np.eye(n, dtype=float)
    if n == 1:
        return np.array([M[0, 0]]), P

    for _ in range(max_iter):
        # Tìm phần tử ngoài đường chéo có trị tuyệt đối lớn nhất
        off_diag = np.abs(M - np.diag(np.diag(M)))
        p, q = np.unravel_index(np.argmax(off_diag), M.shape)
        if off_diag[p, q] < tol:
            break

        if abs(M[p, p] - M[q, q]) < tol:
            theta = np.pi / 4.0
        else:
            theta = 0.5 * np.arctan2(2.0 * M[p, q], M[p, p] - M[q, q])

        c, s = np.cos(theta), np.sin(theta)
        J = np.eye(n, dtype=float)
        J[p, p], J[q, q] = c, c
        J[p, q], J[q, p] = -s, s

        M = mat_mul(mat_mul(transpose(J), M), J)
        P = mat_mul(P, J)

    eigenvalues = np.diag(M).copy()
    # Sắp xếp trị riêng và vector riêng giảm dần
    idx = np.argsort(eigenvalues)[::-1]
    return eigenvalues[idx], P[:, idx]


def is_positive_definite_sylvester(A: np.ndarray, tol: float = 1e-12) -> bool:
    """Kiểm tra ma trận đối xứng xác định dương bằng tiêu chuẩn Sylvester."""
    M = np.asarray(A, dtype=float)
    if M.ndim != 2 or M.shape[0] != M.shape[1]:
        return False
    if not np.allclose(M, transpose(M), atol=tol):
        return False
    n = M.shape[0]
    for k in range(1, n + 1):
        if det_gauss(M[:k, :k], tol=tol) <= tol:
            return False
    return True


def cholesky_decomposition(A: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    """Tự cài khai triển Cholesky A = L @ L^T cho ma trận đối xứng xác định dương."""
    M = np.asarray(A, dtype=float)
    if not is_positive_definite_sylvester(M, tol=tol):
        raise ValueError("Ma trận không đối xứng xác định dương, không thể khai triển Cholesky.")
    n = M.shape[0]
    L = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i + 1):
            sum_val = float(np.sum(L[i, :j] * L[j, :j]))
            if i == j:
                val = M[i, i] - sum_val
                if val <= tol:
                    raise ValueError("Ma trận không xác định dương.")
                L[i, j] = np.sqrt(val)
            else:
                L[i, j] = (M[i, j] - sum_val) / L[j, j]
    return L


def pca_from_scratch(X: np.ndarray, n_components: int) -> tuple[np.ndarray, np.ndarray]:
    """Bài ứng dụng ML: Giảm chiều dữ liệu PCA từ đầu dùng chéo hóa trực giao."""
    X_arr = np.asarray(X, dtype=float)
    n_samples, n_features = X_arr.shape
    if not (1 <= n_components <= n_features):
        raise ValueError("Số thành phần chính không hợp lệ.")
    mean_vec = np.mean(X_arr, axis=0)
    X_centered = X_arr - mean_vec
    cov_matrix = mat_mul(transpose(X_centered), X_centered) / (n_samples - 1)
    eigvals, eigvecs = eigen_symmetric_jacobi(cov_matrix)
    components = eigvecs[:, :n_components]
    X_projected = mat_mul(X_centered, components)
    return X_projected, eigvals[:n_components]
