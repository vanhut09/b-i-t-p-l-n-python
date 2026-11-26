# Đặc tả Chương 2: Không gian vector, ánh xạ tuyến tính (`ch2_vector_spaces`)

## 1. Mục tiêu & Ràng buộc chung
- Cài đặt các phép toán không gian vector, chuẩn, đổi cơ sở, trực giao hóa Gram–Schmidt, ánh xạ tuyến tính, trị riêng/vector riêng, chéo hóa trực giao và khai triển Cholesky từ đầu bằng Python 3.10+ và NumPy cơ bản.
- **Hàm bị cấm trong `src/`:** `np.linalg.norm`, `np.linalg.qr`, `np.linalg.eig`, `np.linalg.eigh`, `np.linalg.cholesky`, `np.linalg.inv`, `np.linalg.matrix_rank`, `scipy.linalg.null_space`.
- **An toàn số học:** Dùng ngưỡng dung sai `tol = 1e-12`; không sửa đổi trực tiếp mảng đầu vào (`copy=True`).

## 2. Đặc tả các hàm cài đặt bắt buộc (`src/ch2.py`)

### 2.1. Độc lập tuyến tính, cơ sở, số chiều & Chuẩn
- `is_linearly_independent(vectors, tol=1e-12) -> bool`: Kiểm tra hệ vector có độc lập tuyến tính không bằng cách đưa ma trận cột về dạng bậc thang và so sánh hạng với số vector.
- `extract_basis(vectors, tol=1e-12) -> tuple[np.ndarray, int]`: Trích ra một cơ sở từ hệ sinh và trả về `(basis_matrix, dimension)`.
- `vector_norm(x, p=2) -> float`: Tính chuẩn Euclid (`p=2`), chuẩn Max (`p=np.inf`), và chuẩn $\ell_p$ tổng quát $\|x\|_p = (\sum |x_i|^p)^{1/p}$ ($p \ge 1$).
- `frobenius_norm(A) -> float`: Tính chuẩn Frobenius $\|A\|_F = \sqrt{\sum_{i,j} |A_{ij}|^2}$.

### 2.2. Đổi cơ sở & Trực giao hóa Gram–Schmidt
- `change_of_basis_matrix(B, S, tol=1e-12) -> np.ndarray`: Tìm ma trận chuyển $P_{B \to S}$ sao cho $[u]_B = P_{B \to S} [u]_S$ bằng thuật toán khử Gauss–Jordan trên ma trận ghép $(B \mid S) \to (I \mid B^{-1}S)$.
- `gram_schmidt(V, tol=1e-12) -> np.ndarray`: Trực chuẩn hóa hệ vector cột độc lập tuyến tính $V$ thành ma trận trực giao $Q$ ($Q^T Q = I$).

### 2.3. Ánh xạ tuyến tính ($f: \mathbb{R}^n \to \mathbb{R}^m$)
- `linear_map_analysis(A, tol=1e-12) -> dict`: Từ ma trận biểu diễn $A$ của ánh xạ tuyến tính trong cơ sở chính tắc, tìm cơ sở của $\text{Im}(f)$ (các cột pivot của $A$), cơ sở của $\text{Ker}(f)$ (nghiệm cơ bản của $Ax = 0$), và kiểm tra định lý số chiều $\dim \text{Im}(f) + \dim \text{Ker}(f) = n$.
- `similar_matrix(A, P, tol=1e-12) -> np.ndarray`: Tính ma trận đồng dạng $A' = P^{-1} A P$ trong cơ sở mới $P$.

### 2.4. Trị riêng, Vector riêng, Chéo hóa & Cholesky
- `eigen_symmetric_jacobi(A, tol=1e-12, max_iter=1000) -> tuple[np.ndarray, np.ndarray]`: Tìm toàn bộ trị riêng và vector riêng trực chuẩn của ma trận đối xứng thực bằng phép quay Jacobi ($P^T A P = D$), từ đó tính $A^k = P D^k P^T$.
- `is_positive_definite_sylvester(A, tol=1e-12) -> bool`: Kiểm tra ma trận đối xứng xác định dương bằng tiêu chuẩn Sylvester (tất cả định thức con chính dẫn đầu $\Delta_k > 0$).
- `cholesky_decomposition(A, tol=1e-12) -> np.ndarray`: Tự cài khai triển Cholesky $A = L L^T$ (với $L$ là ma trận tam giác dưới có đường chéo dương).

## 3. Đề bài tự đặt (2 bài) & Oracle kiểm chứng
1. **Bài cơ bản (Ánh xạ tuyến tính & Chéo hóa trong $\mathbb{R}^4$):** Cho ánh xạ $f: \mathbb{R}^4 \to \mathbb{R}^3$ với ma trận $A$, tìm cơ sở $\text{Im}(f)$, $\text{Ker}(f)$, kiểm nghiệm $\dim \text{Im}(f) + \dim \text{Ker}(f) = 4$; đồng thời chéo hóa trực giao ma trận đối xứng $3 \times 3$ từ đề mẫu bài giảng $B = [[3, -2, 0], [-2, 3, 0], [0, 0, 5]]$.
2. **Bài ứng dụng ML (PCA từ đầu – Principal Component Analysis):**
   - **Bài toán:** Cho tập dữ liệu $X \in \mathbb{R}^{N \times d}$, chuẩn hóa về trung bình 0, tự lập ma trận hiệp phương sai $\Sigma = \frac{1}{N-1} X_c^T X_c$, kiểm tra tính xác định dương bằng tiêu chuẩn Sylvester, chéo hóa trực giao $\Sigma$ để lấy $k$ thành phần chính có trị riêng lớn nhất và chiếu dữ liệu xuống không gian $k$ chiều.
   - **Oracle kiểm chứng:** Đối chiếu phương sai giải thích được và dữ liệu sau chiếu (sai khác dấu vector riêng) với `np.linalg.eigh` và `sklearn.decomposition.PCA`.
