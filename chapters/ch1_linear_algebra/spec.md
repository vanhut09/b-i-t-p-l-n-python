# Đặc tả Chương 1: Ma trận – Định thức (`ch1_linear_algebra`)

## 1. Mục tiêu & Ràng buộc chung
- Cài đặt các phép toán ma trận, định thức, hạng và ma trận nghịch đảo từ đầu bằng Python 3.10+ và NumPy cơ bản.
- **Hàm bị cấm trong `src/`:** `@`, `np.dot`, `np.matmul`, `np.linalg.det`, `np.linalg.matrix_rank`, `np.linalg.inv`, `np.linalg.solve`, `np.linalg.lstsq`.
- **An toàn số học:** Sử dụng ngưỡng dung sai `tol = 1e-12` thay cho `== 0`; không sửa đổi trực tiếp mảng đầu vào (`copy=True`).

## 2. Đặc tả các hàm cài đặt bắt buộc (`src/ch1.py`)

### 2.1. Phép toán ma trận cơ bản
- `transpose(A)`: Chuyển vị $A^T$ ($m \times n \to n \times m$).
- `conjugate_transpose(A)`: Chuyển vị liên hợp $A^H = \overline{A}^T$.
- `mat_add(A, B)`: Cộng hai ma trận cùng kích thước $C_{ij} = A_{ij} + B_{ij}$.
- `mat_mul(A, B)`: Nhân ma trận $(m \times p) \times (p \times n) \to (m \times n)$ theo công thức $C_{ij} = \sum_{k=1}^p A_{ik} B_{kj}$.
- `mat_pow(A, k)`: Lũy thừa ma trận vuông $A^k$ ($k \in \mathbb{N}$, $A^0 = I$) dùng bình phương nhanh (binary exponentiation).

### 2.2. Nhận dạng dạng ma trận
- `identify_matrix_types(A, tol=1e-12) -> dict[str, bool]`: Kiểm tra và trả về từ điển các tính chất: `square`, `echelon` (bậc thang), `upper_triangular`, `lower_triangular`, `diagonal`, `symmetric` ($A = A^T$), `hermitian` ($A = A^H$).

### 2.3. Định thức (2 phương pháp)
- `det_laplace(A) -> float`: Khai triển Laplace đệ quy theo hàng đầu tiên, độ phức tạp $O(n!)$.
- `det_gauss(A, tol=1e-12) -> float`: Biến đổi sơ cấp đưa về dạng tam giác trên có chọn pivot lớn nhất theo cột (partial pivoting), theo dõi dấu $(-1)^s$ sau $s$ lần hoán vị hàng, độ phức tạp $O(n^3)$.

### 2.4. Hạng & Nghịch đảo
- `matrix_rank(A, tol=1e-12) -> int`: Đưa về dạng bậc thang bằng khử Gauss có partial pivoting, đếm số hàng khác không (chuẩn lớn hơn `tol`).
- `inverse_gauss_jordan(A, tol=1e-12) -> np.ndarray`: Lập ma trận bổ sung $(A \mid I)$, khử Gauss-Jordan về $(I \mid A^{-1})$. Ném `ValueError("Ma trận không khả nghịch")` nếu gặp pivot $< \text{tol}$.
- `inverse_adjugate(A, tol=1e-12) -> np.ndarray`: Tính $A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$ qua ma trận phần phụ đại số.

## 3. Đề bài tự đặt (2 bài) & Oracle kiểm chứng
1. **Bài cơ bản (Khảo sát nghiệm & tham số):** Giải hệ phương trình tuyến tính $Ax = b$ thông qua khử Gauss-Jordan cho 3 trường hợp: nghiệm duy nhất, vô nghiệm, vô số nghiệm; và khảo sát tính khả nghịch của ma trận $4 \times 4$ chứa tham số $m$.
2. **Bài ứng dụng ML (Hồi quy tuyến tính qua phương trình chuẩn):**
   - **Bài toán:** Tìm vector trọng số $w = (w_0, w_1, w_2)^T$ dự đoán giá nhà từ diện tích ($x_1$) và số phòng ($x_2$) bằng phương trình chuẩn $(X^T X)w = X^T y$, sử dụng các hàm tự cài `transpose`, `mat_mul`, `inverse_gauss_jordan`.
   - **Oracle kiểm chứng:** Đối chiếu $w$ với `np.linalg.lstsq(X, y, rcond=None)[0]`, kiểm tra sai số tương đối $< 10^{-8}$.
