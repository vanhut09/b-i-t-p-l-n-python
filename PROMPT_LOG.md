# CHECKLIST.md – KIỂM TRA HOÀN THÀNH CÔNG VIỆC

Checklist này dùng để theo dõi hai phần: **soạn bộ prompt** và **triển khai code Chapter 6**. Đánh dấu hoàn thành chỉ khi đã có file hoặc bằng chứng kiểm tra tương ứng.

---

## A. PHẦN SOẠN PROMPT

### A1. Chuẩn bị
- [ ] Đã đọc yêu cầu phân công công việc của nhóm.
- [ ] Đã xác định rõ phạm vi prompt phục vụ dự án Toán máy học.
- [ ] Đã xác định các file và quy tắc cần tuân thủ (`README.md`, `RULES.md`, cấu trúc thư mục).
- [ ] Đã có tài liệu PDF đúng chapter để làm căn cứ.

### A2. Nội dung `prompt_templates.md`
- [ ] Có prompt đọc và phân tích tài liệu chapter.
- [ ] Có prompt phân tích yêu cầu trước khi lập trình.
- [ ] Có prompt hỗ trợ viết code Chapter 6.
- [ ] Có prompt tạo bộ kiểm thử Pytest.
- [ ] Có prompt rà soát và sửa lỗi code.
- [ ] Có prompt soạn `specs.md`.
- [ ] Có prompt soạn `analyst.md` dựa trên log thực tế.
- [ ] Có prompt ghi nhật ký sử dụng AI vào `PROMPT_LOG.md`.
- [ ] Có prompt kiểm tra trước khi commit Git.
- [ ] Các prompt nêu rõ vai trò, đầu vào, nhiệm vụ và định dạng đầu ra.
- [ ] Các prompt yêu cầu không bịa công thức, số liệu, log hoặc kết quả kiểm thử.
- [ ] Có hướng dẫn thứ tự sử dụng prompt.
- [ ] Nội dung prompt đã được thành viên đọc và chỉnh sửa.

### A3. Kiểm tra và bàn giao phần prompt
- [ ] File được lưu đúng tên `prompt_templates.md`.
- [ ] File nằm tại thư mục gốc repository.
- [ ] Markdown hiển thị đúng, không lỗi code block hoặc tiêu đề.
- [ ] Đã thử ít nhất một prompt với tài liệu/code thực tế.
- [ ] Đã ghi lần sử dụng prompt vào `PROMPT_LOG.md`.
- [ ] Đã cập nhật trạng thái công việc trong checklist.

---

## B. PHẦN CODE CHAPTER 6

### B1. Đọc và xác minh tài liệu
- [ ] Đã mở đúng tài liệu PDF Chapter 6.
- [ ] Đã xác định tên chương và các đề mục thực tế trong tài liệu.
- [ ] Đã ghi lại định nghĩa, ký hiệu, công thức và điều kiện áp dụng.
- [ ] Đã xác định ví dụ/bài tập trong tài liệu có thể dùng minh họa.
- [ ] Đã phân biệt nội dung giáo trình với phần nhóm tự mở rộng.
- [ ] Những nội dung PDF không đọc được hoặc chưa rõ đã được đánh dấu để xác minh.

### B2. Đặc tả `specs.md`
- [ ] Có mục tiêu và phạm vi Chapter 6.
- [ ] Mỗi chức năng có mô tả và cơ sở lý thuyết.
- [ ] Công thức và ý nghĩa ký hiệu được trình bày chính xác.
- [ ] Có mô tả đầu vào, kiểu dữ liệu và điều kiện hợp lệ.
- [ ] Có mô tả đầu ra và kiểu dữ liệu trả về.
- [ ] Có mô tả cách xử lý dữ liệu không hợp lệ/trường hợp biên.
- [ ] Có ví dụ minh họa.
- [ ] Có tiêu chí nghiệm thu cho từng chức năng.
- [ ] Đặc tả khớp với nội dung giáo trình và code thực tế.

### B3. Lập trình
- [ ] Đã thống nhất cấu trúc thư mục Chapter 6 với nhóm.
- [ ] Code được chia thành module theo chức năng.
- [ ] Tên hàm, biến và tham số rõ ràng.
- [ ] Có docstring/chú thích cho các hàm quan trọng.
- [ ] Công thức được cài đặt đúng và có kiểm tra điều kiện áp dụng.
- [ ] Có kiểm tra kiểu dữ liệu, kích thước và giá trị đầu vào.
- [ ] Có xử lý trường hợp dữ liệu rỗng hoặc không hợp lệ khi phù hợp.
- [ ] Có thông báo lỗi dễ hiểu.
- [ ] Có chương trình demo hoặc ví dụ chạy.
- [ ] Không sửa hoặc làm ảnh hưởng code của chapter khác.

### B4. Kiểm thử
- [ ] Có file test cho các chức năng Chapter 6.
- [ ] Có test cho trường hợp đầu vào thông thường.
- [ ] Có test cho trường hợp biên.
- [ ] Có test cho đầu vào không hợp lệ.
- [ ] Kết quả mong đợi được tính/đối chiếu độc lập.
- [ ] Test kiểm tra cả giá trị trả về và exception khi cần.
- [ ] Đã chạy lệnh `pytest`.
- [ ] Đã xử lý các test fail hoặc ghi rõ lỗi còn tồn tại.
- [ ] Không ghi số lượng test pass nếu chưa có kết quả chạy thực tế.

### B5. Báo cáo `analyst.md`
- [ ] Có mục tiêu kiểm tra.
- [ ] Có môi trường chạy và phiên bản thư viện thực tế.
- [ ] Có các lệnh đã chạy.
- [ ] Có kết quả chạy demo.
- [ ] Có kết quả test thực tế.
- [ ] Có mô tả lỗi và cách khắc phục (nếu có).
- [ ] Có hạn chế còn tồn tại.
- [ ] Báo cáo không chứa số liệu hoặc kết quả tự tạo.

---

## C. KIỂM TRA CHUNG TRƯỚC KHI NỘP

- [ ] `prompt_templates.md` nằm đúng vị trí.
- [ ] `checklist.md` nằm đúng vị trí.
- [ ] Thư mục Chapter 6 nằm đúng vị trí trong `chapters/`.
- [ ] `requirements.txt` đã cập nhật đủ thư viện cần thiết, không xóa phụ thuộc của thành viên khác.
- [ ] `README.md` có hướng dẫn cài đặt và chạy phù hợp với repository.
- [ ] `PROMPT_LOG.md` ghi lại quá trình sử dụng AI.
- [ ] Không commit file cache, file tạm hoặc thông tin bí mật.
- [ ] Đã chạy lại chương trình và test từ cấu trúc repository chung.
- [ ] Đã kiểm tra trạng thái Git và xem lại các file thay đổi trước khi commit.
- [ ] Đã bàn giao cho nhóm và cập nhật tiến độ.

---

## D. THEO DÕI TIẾN ĐỘ

| Hạng mục | Người phụ trách | Trạng thái | Ghi chú |
|---|---|---|---|
| Soạn `prompt_templates.md` | [Điền tên] | Chưa bắt đầu | |
| Hoàn thiện `checklist.md` | [Điền tên] | Chưa bắt đầu | |
| Đọc tài liệu Chapter 6 | [Điền tên] | Chưa bắt đầu | |
| Viết code Chapter 6 | [Điền tên] | Chưa bắt đầu | |
| Viết test Chapter 6 | [Điền tên] | Chưa bắt đầu | |
| Viết `specs.md` | [Điền tên] | Chưa bắt đầu | |
| Viết `analyst.md` | [Điền tên] | Chưa bắt đầu | |

**Quy ước trạng thái:** `Chưa bắt đầu` / `Đang thực hiện` / `Chờ kiểm tra` / `Hoàn thành`.
