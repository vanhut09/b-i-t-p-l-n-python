import numpy as np
import pytest
from chapters.ch1_linear_algebra.src.ch1 import (
    transpose,
    mat_mul,
    mat_pow,
    identify_matrix_types,
    det_laplace,
    det_gauss,
    matrix_rank,
    inverse_gauss_jordan,
    inverse_adjugate,
    solve_linear_regression_normal_eq,
)


def test_basic_ops():
    A = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    B = np.array([[7.0, 8.0], [9.0, 1.0], [2.0, 3.0]])
    assert np.allclose(transpose(A), A.T)
    assert np.allclose(mat_mul(A, B), A @ B)

    S = np.array([[2.0, 1.0], [1.0, 2.0]])
    assert np.allclose(mat_pow(S, 0), np.eye(2))
    assert np.allclose(mat_pow(S, 4), np.linalg.matrix_power(S, 4))


def test_identify_matrix_types():
    D = np.diag([1.0, -2.0, 5.0])
    info = identify_matrix_types(D)
    assert info["square"] and info["diagonal"] and info["symmetric"] and info["echelon"]


def test_determinant_methods():
    rng = np.random.default_rng(10)
    A = rng.normal(size=(4, 4))
    B = rng.normal(size=(4, 4))
    expected = np.linalg.det(A)
    assert np.isclose(det_laplace(A), expected)
    assert np.isclose(det_gauss(A), expected)
    # Tính chất det(A*B) = det(A)*det(B)
    assert np.isclose(det_gauss(mat_mul(A, B)), det_gauss(A) * det_gauss(B))


def test_rank_and_inverse():
    # Đề mẫu bài giảng
    A = np.array([[1.0, 2.0, -1.0], [1.0, 2.0, 1.0], [2.0, 3.0, 0.0]])
    assert np.isclose(det_gauss(A), 2.0)
    assert matrix_rank(A) == 3

    inv_gj = inverse_gauss_jordan(A)
    inv_adj = inverse_adjugate(A)
    assert np.allclose(inv_gj, np.linalg.inv(A))
    assert np.allclose(inv_adj, np.linalg.inv(A))
    assert np.allclose(mat_mul(A, inv_gj), np.eye(3))


def test_edge_cases():
    # Ma trận cần hoán vị hàng (pivot đầu = 0)
    P = np.array([[0.0, 1.0], [1.0, 0.0]])
    assert np.allclose(inverse_gauss_jordan(P), P)

    # Ma trận suy biến (det = 0)
    S = np.array([[1.0, 2.0, 3.0], [2.0, 4.0, 6.0], [1.0, 0.0, 1.0]])
    assert matrix_rank(S) == 2
    with pytest.raises(ValueError):
        inverse_gauss_jordan(S)


def test_ml_application_linear_regression():
    # Dữ liệu tự đặt: y = 3 + 2*x1 - 1.5*x2
    X = np.array([
        [1.0, 1.0, 2.0],
        [1.0, 2.0, 1.0],
        [1.0, 3.0, 4.0],
        [1.0, 4.0, 2.0],
        [1.0, 5.0, 3.0],
    ])
    y = np.array([2.0, 5.5, 3.0, 8.0, 8.5])
    w_custom = solve_linear_regression_normal_eq(X, y)
    w_oracle = np.linalg.lstsq(X, y, rcond=None)[0]
    assert np.allclose(w_custom, w_oracle, atol=1e-8)
