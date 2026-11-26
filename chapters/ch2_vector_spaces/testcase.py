import numpy as np
import pytest
from chapters.ch2_vector_spaces.src.ch2 import (
    is_linearly_independent,
    extract_basis,
    vector_norm,
    frobenius_norm,
    change_of_basis_matrix,
    gram_schmidt,
    linear_map_analysis,
    similar_matrix,
    eigen_symmetric_jacobi,
    is_positive_definite_sylvester,
    cholesky_decomposition,
    pca_from_scratch,
)


def test_independence_and_basis():
    # Hệ 3 vector trong R^3 nhưng phụ thuộc tuyến tính (v3 = v1 + v2)
    V = np.array([[1.0, 0.0, 1.0], [0.0, 1.0, 1.0], [1.0, 1.0, 2.0]])
    assert not is_linearly_independent(V)
    basis, dim = extract_basis(V)
    assert dim == 2
    assert basis.shape == (3, 2)


def test_norms():
    x = np.array([3.0, -4.0, 0.0])
    assert np.isclose(vector_norm(x, p=2), np.linalg.norm(x, 2))
    assert np.isclose(vector_norm(x, p=np.inf), np.linalg.norm(x, np.inf))
    assert np.isclose(vector_norm(x, p=1), np.linalg.norm(x, 1))

    A = np.array([[1.0, -2.0], [3.0, 4.0]])
    assert np.isclose(frobenius_norm(A), np.linalg.norm(A, "fro"))


def test_change_of_basis_and_gram_schmidt():
    # Đề mẫu Gram-Schmidt: {(1,1,1), (1,1,0), (0,1,1)}
    V = np.array([[1.0, 1.0, 0.0], [1.0, 1.0, 1.0], [1.0, 0.0, 1.0]])
    Q = gram_schmidt(V)
    assert np.allclose(Q.T @ Q, np.eye(3), atol=1e-10)

    # Đổi cơ sở: [u]_B = P(B->S) @ [u]_S
    B = np.array([[1.0, 1.0], [0.0, 1.0]])
    S = np.array([[2.0, 0.0], [1.0, 3.0]])
    P_B_S = change_of_basis_matrix(B, S)
    u_S = np.array([[2.0], [-1.0]])
    u_B = P_B_S @ u_S
    assert np.allclose(B @ u_B, S @ u_S)


def test_linear_map():
    # Đề mẫu f(x,y,z) = (2x, x+y, x-y, x+z)
    A = np.array([
        [2.0, 0.0, 0.0],
        [1.0, 1.0, 0.0],
        [1.0, -1.0, 0.0],
        [1.0, 0.0, 1.0],
    ])
    res = linear_map_analysis(A)
    assert res["dim_im"] == 3
    assert res["dim_ker"] == 0
    assert res["rank_nullity_holds"]

    # Ánh xạ có Ker != {0}
    A2 = np.array([[1.0, 2.0, 3.0], [2.0, 4.0, 6.0]])
    res2 = linear_map_analysis(A2)
    assert res2["dim_im"] == 1 and res2["dim_ker"] == 2
    assert np.allclose(A2 @ res2["ker_basis"], 0.0)


def test_eigen_and_cholesky():
    # Đề mẫu ma trận B = [[3, -2, 0], [-2, 3, 0], [0, 0, 5]]
    B = np.array([[3.0, -2.0, 0.0], [-2.0, 3.0, 0.0], [0.0, 0.0, 5.0]])
    assert is_positive_definite_sylvester(B)

    eigvals, P = eigen_symmetric_jacobi(B)
    expected_vals, _ = np.linalg.eigh(B)
    assert np.allclose(np.sort(eigvals), np.sort(expected_vals))
    assert np.allclose(P.T @ B @ P, np.diag(eigvals), atol=1e-10)

    # Kiểm tra Cholesky L @ L^T = B
    L = cholesky_decomposition(B)
    assert np.allclose(L, np.linalg.cholesky(B))
    assert np.allclose(L @ L.T, B)

    # Trường hợp biên: ma trận không xác định dương
    not_pd = np.array([[1.0, 2.0], [2.0, 1.0]])
    assert not is_positive_definite_sylvester(not_pd)
    with pytest.raises(ValueError):
        cholesky_decomposition(not_pd)


def test_ml_application_pca():
    rng = np.random.default_rng(42)
    X = rng.normal(loc=[10.0, -5.0, 2.0], scale=[3.0, 1.0, 0.5], size=(50, 3))
    X_proj, top_vals = pca_from_scratch(X, n_components=2)

    # Đối chiếu với np.linalg.eigh
    X_c = X - np.mean(X, axis=0)
    cov = (X_c.T @ X_c) / (len(X) - 1)
    oracle_vals, oracle_vecs = np.linalg.eigh(cov)
    oracle_vals = oracle_vals[::-1][:2]
    oracle_vecs = oracle_vecs[:, ::-1][:, :2]
    oracle_proj = X_c @ oracle_vecs

    assert np.allclose(top_vals, oracle_vals, atol=1e-8)
    # Vector riêng có thể ngược dấu nên so sánh trị tuyệt đối của tọa độ chiếu
    assert np.allclose(np.abs(X_proj), np.abs(oracle_proj), atol=1e-8)
