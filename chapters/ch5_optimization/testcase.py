import chapter5 as cl
import numpy as np


def run_all_tests():
    # ==========================================
    # MỤC 1: Định nghĩa tập lồi (đoạn thẳng)[cite: 1]
    # ==========================================
    disk = lambda p: p[0] ** 2 + p[1] ** 2 <= 25
    print("--- Mục 1: Tập lồi ---")
    print("TC1 (2 điểm trong hình tròn):", cl.is_segment_in_set([3, 0], [0, 4], disk))
    print("TC2 (1 điểm ngoài hình tròn):", cl.is_segment_in_set([3, 0], [6, 0], disk))
    print("TC3 (tổ hợp lồi lam=0.5):", cl.convex_combination([0, 0], [4, 6], 0.5))

    # ==========================================
    # MỤC 2: Siêu phẳng D1 = {x : a^T x = b}[cite: 2]
    # ==========================================
    a2, b2 = [1, 2], 5
    print("\n--- Mục 2: Siêu phẳng ---")
    print("TC1 (điểm [1, 2] thuộc):", cl.in_hyperplane([1, 2], a2, b2))
    print("TC2 (điểm [3, 1] thuộc):", cl.in_hyperplane([3, 1], a2, b2))
    print("TC3 (điểm [0, 0] không thuộc):", cl.in_hyperplane([0, 0], a2, b2))

    # ==========================================
    # MỤC 3: Nửa không gian D2 = {x : a^T x <= (>=) b}[cite: 3]
    # ==========================================
    a3, b3 = [2, 1], 6
    print("\n--- Mục 3: Nửa không gian ---")
    print("TC1 ([1, 1] <= 6):", cl.in_halfspace([1, 1], a3, b3, "<="))
    print("TC2 ([4, 0] >= 6):", cl.in_halfspace([4, 0], a3, b3, ">="))
    print("TC3 ([5, 5] <= 6):", cl.in_halfspace([5, 5], a3, b3, "<="))

    # ==========================================
    # MỤC 4: Hình cầu đóng B(a, r) = {x : ||x - a||_2 <= r}[cite: 4]
    # ==========================================
    tam4, r4 = [1, 1], 5
    print("\n--- Mục 4: Hình cầu đóng ---")
    print("TC1 (điểm [4, 5] trên biên):", cl.in_closed_ball([4, 5], tam4, r4))
    print("TC2 (điểm [2, 2] bên trong):", cl.in_closed_ball([2, 2], tam4, r4))
    print("TC3 (điểm [10, 10] bên ngoài):", cl.in_closed_ball([10, 10], tam4, r4))

    # ==========================================
    # MỤC 5: Tổ hợp lồi tổng quát x = sum(t_i * x^i)[cite: 4]
    # ==========================================
    pts5 = [[0, 0], [6, 0], [0, 6]]
    print("\n--- Mục 5: Tổ hợp lồi tổng quát ---")
    print("TC1 (trọng số đều):", cl.general_convex_combination(pts5, [1 / 3, 1 / 3, 1 / 3]))
    print("TC2 (trọng số lệch):", cl.general_convex_combination(pts5, [0.5, 0.25, 0.25]))
    print("TC3 (tại đỉnh x^2):", cl.general_convex_combination(pts5, [0.0, 1.0, 0.0]))

    # ==========================================
    # MỤC 6: Bất đẳng thức Jensen[cite: 5]
    # ==========================================
    f6 = lambda x: x**2
    print("\n--- Mục 6: Bất đẳng thức Jensen ---")
    print("TC1 (u=1, v=5, t=0.5):", cl.check_jensen(f6, 1, 5, 0.5))
    print("TC2 (u=-2, v=4, t=0.2):", cl.check_jensen(f6, -2, 4, 0.2))
    print("TC3 (u=0, v=10, t=0.8):", cl.check_jensen(f6, 0, 10, 0.8))

    # ==========================================
    # MỤC 7: Đạo hàm bậc 1[cite: 5]
    # ==========================================
    f7 = lambda x: x[0] ** 2 + x[1] ** 2
    g7 = lambda x: np.array([2 * x[0], 2 * x[1]])
    print("\n--- Mục 7: Đạo hàm bậc 1 ---")
    print("TC1 (u=[2, 2], v=[1, 1]):", cl.check_first_order_convex(f7, g7, [2, 2], [1, 1]))
    print("TC2 (u=[0, 0], v=[3, 4]):", cl.check_first_order_convex(f7, g7, [0, 0], [3, 4]))
    print("TC3 (u=[-1, 2], v=[1, -1]):", cl.check_first_order_convex(f7, g7, [-1, 2], [1, -1]))

    # ==========================================
    # MỤC 8: Đạo hàm bậc 2 (Hessian)[cite: 5]
    # ==========================================
    h8 = lambda x: np.array([[4.0, 0.0], [0.0, 6.0]])
    print("\n--- Mục 8: Đạo hàm bậc 2 ---")
    print("TC1 (lồi tại [0, 0]):", cl.check_second_order_convex(h8, [0, 0], strict=False))
    print("TC2 (lồi chặt tại [1, 1]):", cl.check_second_order_convex(h8, [1, 1], strict=True))
    print("TC3 (lồi chặt tại [-5, 3]):", cl.check_second_order_convex(h8, [-5, 3], strict=True))

    # ==========================================
    # MỤC 9: QHTT dạng tổng quát[cite: 6]
    # ==========================================
    print("\n--- Mục 9: QHTT tổng quát ---")
    print("TC1:", cl.solve_lp_general([-2, -3], G=[[1, 1], [-1, 0], [0, -1]], h=[4, 0, 0]))
    print("TC2:", cl.solve_lp_general([-1, -2], d=10, G=[[2, 1], [-1, 0], [0, -1]], h=[6, 0, 0]))
    print("TC3:", cl.solve_lp_general([3, 4], G=[[-1, 0], [0, -1]], h=[0, 0], A=[[1, 1]], b=[2]))

    # ==========================================
    # MỤC 10: QHTT dạng chuẩn[cite: 6]
    # ==========================================
    print("\n--- Mục 10: QHTT dạng chuẩn ---")
    print("TC1:", cl.solve_lp_standard([1, 2], A=[[1, 1]], b=[4]))
    print("TC2:", cl.solve_lp_standard([3, 1], d=5, A=[[1, 2]], b=[6]))
    print("TC3:", cl.solve_lp_standard([2, 5], A=[[1, 1]], b=[3]))

    # ==========================================
    # MỤC 11: QP dạng tổng quát[cite: 6]
    # ==========================================
    P11 = [[2.0, 0.0], [0.0, 2.0]]
    print("\n--- Mục 11: QP tổng quát ---")
    print("TC1:", cl.solve_qp_general(P11, [-4, -4]))
    print("TC2:", cl.solve_qp_general(P11, [-2, -6], G=[[1, 1]], h=[2]))
    print("TC3:", cl.solve_qp_general(P11, [0, 0], c=1, A=[[1, 1]], b=[4]))

    # ==========================================
    # MỤC 12: Khoảng cách ngắn nhất tới đa diện lồi[cite: 6]
    # ==========================================
    G12, h12 = [[1, 0], [-1, 0], [0, 1], [0, -1]], [2, 0, 2, 0]  # Hình vuông [0, 2] x [0, 2]
    print("\n--- Mục 12: Khoảng cách ngắn nhất tới đa diện lồi ---")
    print("TC1 (điểm [1, 1] trong miền):", cl.min_distance_polyhedron([1, 1], G12, h12))
    print("TC2 (điểm [5, 1] ngoài miền):", cl.min_distance_polyhedron([5, 1], G12, h12))
    print("TC3 (điểm [-2, 4] ngoài miền):", cl.min_distance_polyhedron([-2, 4], G12, h12))

    # ==========================================
    # MỤC 13: Công thức cập nhật Gradient Descent[cite: 7]
    # ==========================================
    g13 = lambda x: np.array([2 * (x[0] - 1), 2 * (x[1] - 1)])
    print("\n--- Mục 13: Gradient Descent ---")
    print("TC1 (1 bước từ [0, 0], eta=0.1):", cl.gd_step([0, 0], g13, eta=0.1))
    print("TC2 (50 bước từ [5, 5], eta=0.1):", np.round(cl.gradient_descent([5, 5], g13, eta=0.1, steps=50), 3))
    print("TC3 (100 bước từ [-4, 6], eta=0.05):", np.round(cl.gradient_descent([-4, 6], g13, eta=0.05, steps=100), 3))

    # ==========================================
    # MỤC 14: Công thức cập nhật Newton[cite: 7]
    # ==========================================
    g14 = lambda x: np.array([2 * (x[0] - 3), 2 * (x[1] + 2)])
    h14 = lambda x: np.array([[2.0, 0.0], [0.0, 2.0]])
    print("\n--- Mục 14: Phương pháp Newton ---")
    print("TC1 (1 bước từ [0, 0]):", cl.newton_step([0, 0], g14, h14))
    print("TC2 (3 bước từ [10, -10]):", np.round(cl.newton_method([10, -10], g14, h14, steps=3), 3))
    print("TC3 (5 bước từ [-7, 8]):", np.round(cl.newton_method([-7, 8], g14, h14, steps=5), 3))


if __name__ == "__main__":
    run_all_tests()