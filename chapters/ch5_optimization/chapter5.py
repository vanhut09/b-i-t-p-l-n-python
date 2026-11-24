import numpy as np


# Tập lồi 
def convex_combination(x, y, lam):
    if not (0 <= lam <= 1):
        raise ValueError("lambda phải nằm trong đoạn [0, 1]")
    return lam * np.array(x) + (1 - lam) * np.array(y)


def is_segment_in_set(x, y, in_set_func):
    if not (in_set_func(x) and in_set_func(y)):
        return False
    for lam in np.linspace(0, 1, 20):
        point = convex_combination(x, y, lam)
        if not in_set_func(point):
            return False
    return True


# Mục 2: Siêu phẳng 
def in_hyperplane(x, a, b):
    return bool(np.isclose(np.dot(a, x), b))


# Mục 3: Nửa không gian
def in_halfspace(x, a, b, sign="<="):
    val = np.dot(a, x)
    if sign == "<=":
        return bool(val <= b)
    elif sign == ">=":
        return bool(val >= b)
    else:
        raise ValueError("Tham số sign chỉ nhận '<=' hoặc '>='")


# Mục 4: Hình cầu đóng
def in_closed_ball(x, a, r):
    if r <= 0:
        raise ValueError("Bán kính r phải lớn hơn 0")
    distance = np.linalg.norm(np.array(x) - np.array(a))
    return bool(distance <= r)


# Mục 5: Tổ hợp lồi tổng quát
def general_convex_combination(points, t):
    points = np.array(points)
    t = np.array(t)
    if np.any(t < 0) or not np.isclose(np.sum(t), 1.0):
        raise ValueError("Các trọng số t_i phải >= 0 và có tổng bằng 1")
    return np.dot(t, points)


# Mục 6: Bất đẳng thức Jensen
def check_jensen(f, u, v, t):
    if not (0 <= t <= 1):
        raise ValueError("t phải nằm trong đoạn [0, 1]")
    u, v = np.array(u), np.array(v)
    ve_trai = f(t * u + (1 - t) * v)
    ve_phai = t * f(u) + (1 - t) * f(v)
    return bool(ve_trai <= ve_phai + 1e-9)


# Mục 7: Đạo hàm bậc 1
def check_first_order_convex(f, grad_f, u, v):
    u, v = np.array(u), np.array(v)
    ve_trai = f(u)
    ve_phai = f(v) + np.dot(grad_f(v), u - v)
    return bool(ve_trai >= ve_phai - 1e-9)


# Mục 8: Đạo hàm bậc 2 (Hessian)
def check_second_order_convex(hessian_f, x, strict=False):
    H = np.array(hessian_f(x))
    eigenvalues = np.linalg.eigvalsh(H)
    if strict:
        return bool(np.all(eigenvalues > 1e-9))
    return bool(np.all(eigenvalues >= -1e-9))


# Tối ưu bằng NumPy (Gradient Descent + Phạt)
def _solve_gd(grad_f, n, G=None, h=None, A=None, b=None, lr=0.001, steps=20000, rho=1000.0):
    x = np.zeros(n)
    for _ in range(steps):
        grad = grad_f(x)
        if G is not None:
            G_arr, h_arr = np.array(G, dtype=float), np.array(h, dtype=float)
            vi_pham = np.maximum(0, G_arr @ x - h_arr)
            grad = grad + rho * (G_arr.T @ vi_pham)
        if A is not None:
            A_arr, b_arr = np.array(A, dtype=float), np.array(b, dtype=float)
            grad = grad + rho * (A_arr.T @ (A_arr @ x - b_arr))
        x = x - lr * grad
    return x


def solve_lp_general(c, d=0, G=None, h=None, A=None, b=None):
    c = np.array(c, dtype=float)
    x = _solve_gd(lambda x: c, len(c), G, h, A, b)
    return x, float(c @ x + d)


def solve_lp_standard(c, d=0, A=None, b=None):
    c = np.array(c, dtype=float)
    n = len(c)
    x = _solve_gd(lambda x: c, n, G=-np.eye(n), h=np.zeros(n), A=A, b=b)
    return x, float(c @ x + d)


def solve_qp_general(P, q, c=0, G=None, h=None, A=None, b=None):
    P, q = np.array(P, dtype=float), np.array(q, dtype=float)
    x = _solve_gd(lambda x: P @ x + q, len(q), G, h, A, b)
    val = 0.5 * (x.T @ P @ x) + q @ x + c
    return x, float(val)


def min_distance_polyhedron(a, G, h):
    a = np.array(a, dtype=float)
    x = _solve_gd(lambda x: 2 * (x - a), len(a), G=G, h=h)
    dist_sq = np.sum((x - a) ** 2)
    return x, float(dist_sq)


# Gradient Descent
def gd_step(x, grad_f, eta=0.01):
    x = np.array(x, dtype=float)
    return x - eta * np.array(grad_f(x), dtype=float)


def gradient_descent(x0, grad_f, eta=0.01, steps=1000):
    x = np.array(x0, dtype=float)
    for _ in range(steps):
        x = gd_step(x, grad_f, eta)
    return x


# Mục 14: Phương pháp Newtonn
def newton_step(x, grad_f, hessian_f):
    x = np.array(x, dtype=float)
    grad = np.array(grad_f(x), dtype=float)
    H = np.array(hessian_f(x), dtype=float)
    delta = np.linalg.solve(H, grad)
    return x - delta


def newton_method(x0, grad_f, hessian_f, steps=20):
    x = np.array(x0, dtype=float)
    for _ in range(steps):
        x = newton_step(x, grad_f, hessian_f)
    return x