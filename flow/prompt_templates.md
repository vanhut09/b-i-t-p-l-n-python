# PROMPT_TEMPLATES.md

## 1. Mục đích

Tài liệu này tập hợp các mẫu prompt dùng trong dự án **Toán máy học**. Nhóm sử dụng các prompt để đọc tài liệu môn học, phân tích yêu cầu, hỗ trợ lập trình từng chapter, tạo kiểm thử và viết báo cáo. Prompt chỉ là công cụ hỗ trợ; thành viên phải kiểm tra lại công thức, mã nguồn và kết quả trước khi đưa vào Git.

## 2. Quy tắc sử dụng chung

Khi sử dụng bất kỳ prompt nào dưới đây:

- Đính kèm đúng PDF, mã nguồn hoặc yêu cầu liên quan.
- Nêu rõ chapter, tên file và chức năng cần thực hiện.
- Yêu cầu AI phân biệt nội dung có trong giáo trình với giả định hoặc kiến thức bổ sung.
- Không chấp nhận công thức, định nghĩa, kết quả chạy hoặc kết quả kiểm thử nếu chưa kiểm chứng.
- Không yêu cầu AI tự ý sửa các file ngoài phạm vi công việc.
- Không đưa mật khẩu, API key hoặc thông tin cá nhân vào prompt.
- Sau mỗi lần dùng, ghi lại prompt và kết quả đáng chú ý trong `PROMPT_LOG.md`.

---

## 3. Các mẫu prompt

### Prompt 01 – Đọc và phân tích tài liệu chapter

```text
Bạn là trợ lý học thuật cho dự án môn Toán máy học.
Hãy đọc tài liệu PDF chapter tôi cung cấp và phân tích riêng nội dung của Chapter [SỐ CHAPTER].

Yêu cầu:
1. Xác định đúng tên chapter và các đề mục theo tài liệu.
2. Tóm tắt mục tiêu và nội dung chính của từng đề mục.
3. Liệt kê định nghĩa, ký hiệu, công thức và điều kiện áp dụng.
4. Giải thích ý nghĩa các biến trong công thức.
5. Chỉ ra ví dụ/bài toán có trong tài liệu (nếu có).
6. Không tự thêm kiến thức ngoài tài liệu như thể đó là nội dung giáo trình.
7. Nếu PDF không đọc được, thiếu trang hoặc nội dung không rõ, hãy nêu chính xác phần chưa xác minh; không tự suy đoán.

Đầu ra trình bày bằng tiếng Việt, có tiêu đề và bảng công thức nếu phù hợp.
```

### Prompt 02 – Phân tích yêu cầu trước khi lập trình

```text
Bạn là người phân tích yêu cầu cho dự án Python môn Toán máy học.
Dựa trên PDF Chapter [SỐ] và yêu cầu công việc được cung cấp, hãy lập bản phân tích trước khi viết code.

Hãy trình bày:
1. Chức năng cần xây dựng.
2. Kiến thức toán học trong tài liệu làm cơ sở cho chức năng.
3. Công thức và giải thích từng ký hiệu.
4. Dữ liệu đầu vào, kiểu dữ liệu và điều kiện hợp lệ.
5. Kết quả đầu ra và kiểu dữ liệu.
6. Trường hợp biên và dữ liệu không hợp lệ.
7. Các hàm/module Python dự kiến.
8. Các trường hợp kiểm thử cần có.
9. Những điểm chưa rõ cần hỏi lại nhóm.

Chưa viết code ở bước này. Không tự đặt ra nội dung không được tài liệu hoặc yêu cầu hỗ trợ.
```

### Prompt 03 – Soạn prompt chi tiết để viết code Chapter 6

```text
Bạn là lập trình viên Python trong dự án Toán máy học.
Hãy hỗ trợ triển khai phần Chapter 6 dựa trên PDF Chapter 6, file đặc tả `specs.md` và cấu trúc repository mà tôi cung cấp.

Trước khi viết code:
- Đối chiếu từng chức năng với nội dung PDF.
- Nêu công thức toán học, ý nghĩa ký hiệu và điều kiện áp dụng.
- Nếu không tìm thấy căn cứ trong PDF hoặc specs, hãy đánh dấu là nội dung cần xác nhận, không tự coi đó là yêu cầu chính thức.

Khi viết code:
- Dùng Python và tuân thủ phiên bản/thư viện trong `requirements.txt`.
- Tổ chức code theo cấu trúc thư mục hiện có.
- Đặt tên hàm và biến rõ nghĩa; viết docstring và chú thích công thức.
- Kiểm tra đầu vào, kích thước dữ liệu, kiểu dữ liệu và trường hợp biên.
- Báo lỗi dễ hiểu bằng exception phù hợp.
- Không tự ý thay đổi giao diện hàm hoặc file của chapter khác.
- Cung cấp ví dụ sử dụng có dữ liệu cụ thể.

Đầu ra gồm: danh sách file cần tạo/sửa, nội dung code hoàn chỉnh từng file, cách chạy và các điểm cần nhóm xác minh.
```

### Prompt 04 – Tạo bộ kiểm thử Pytest

```text
Bạn là kỹ sư kiểm thử Python.
Hãy tạo bộ kiểm thử Pytest cho module [TÊN MODULE] và các hàm [TÊN HÀM], dựa trên code, `specs.md` và tài liệu môn học được cung cấp.

Với mỗi hàm, hãy kiểm tra:
1. Trường hợp đầu vào hợp lệ thông thường.
2. Trường hợp dữ liệu nhỏ nhất/lớn nhất hoặc kích thước biên phù hợp.
3. Dữ liệu rỗng hoặc thiếu dữ liệu (nếu có thể xảy ra).
4. Sai kiểu dữ liệu, sai kích thước hoặc tham số ngoài miền xác định.
5. Kết quả số học so với kết quả tính độc lập đã xác minh.
6. Exception được mong đợi đối với đầu vào không hợp lệ.

Yêu cầu:
- Dùng pytest và đặt test đúng thư mục của chapter.
- Không sửa code sản phẩm chỉ để làm test pass.
- Không dùng kết quả của chính hàm đang kiểm thử làm đáp án chuẩn.
- Ghi rõ lý do và kết quả mong đợi của từng test.
- Không tuyên bố test đã chạy thành công nếu chưa thực sự chạy.
```

### Prompt 05 – Rà soát và sửa lỗi code

```text
Bạn là người review code Python cho dự án Toán máy học.
Hãy rà soát các file sau: [DANH SÁCH FILE], đối chiếu với PDF, `specs.md`, test và quy tắc trong `RULES.md`.

Kiểm tra:
1. Code có thực hiện đúng yêu cầu không?
2. Công thức và điều kiện toán học có chính xác không?
3. Tên hàm, tham số, kiểu dữ liệu và giá trị trả về có nhất quán không?
4. Có xử lý dữ liệu rỗng, sai kích thước và đầu vào không hợp lệ không?
5. Có lỗi import, đường dẫn, phụ thuộc hoặc khả năng chạy độc lập không?
6. Test có kiểm tra đúng hành vi cần thiết không?
7. Code, specs và README có mâu thuẫn không?

Hãy liệt kê phát hiện theo mức độ: nghiêm trọng, trung bình, thấp. Với mỗi lỗi, nêu file/dòng liên quan, lý do, cách sửa và test cần chạy lại. Không tự sửa file nếu tôi chưa yêu cầu.
```

### Prompt 06 – Viết `specs.md`

```text
Bạn là người viết đặc tả kỹ thuật cho dự án Toán máy học.
Dựa trên PDF Chapter [SỐ], yêu cầu được giao và code hiện có, hãy soạn `specs.md` cho chapter này.

Mỗi chức năng cần có:
1. Tên và mục đích.
2. Cơ sở lý thuyết/công thức theo giáo trình.
3. Giải thích ký hiệu và điều kiện áp dụng.
4. Tham số đầu vào, kiểu dữ liệu, miền giá trị.
5. Kết quả trả về, kiểu dữ liệu và ý nghĩa.
6. Cách xử lý đầu vào không hợp lệ.
7. Ví dụ đầu vào – đầu ra.
8. Tiêu chí nghiệm thu và test tương ứng.

Phân biệt rõ: (A) nội dung được giáo trình nêu; (B) quyết định triển khai của nhóm; (C) nội dung còn cần xác nhận. Không mô tả chức năng chưa có trong code như thể đã hoàn thành.
```

### Prompt 07 – Viết `analyst.md` sau khi chạy chương trình

```text
Bạn là người lập báo cáo phân tích kết quả chạy chương trình.
Dựa trên log terminal, kết quả chạy demo, kết quả Pytest và code thực tế tôi cung cấp, hãy viết `analyst.md`.

Báo cáo cần có:
1. Mục tiêu kiểm tra.
2. Môi trường chạy: hệ điều hành, phiên bản Python và thư viện (chỉ ghi thông tin đã cung cấp/đo được).
3. Các lệnh đã chạy.
4. Chức năng đã thực thi.
5. Kết quả thực tế và đối chiếu kết quả mong đợi.
6. Các test pass/fail và nguyên nhân.
7. Lỗi phát sinh, cách xử lý và kết quả chạy lại.
8. Hạn chế còn tồn tại và hướng phát triển.

Không tự tạo log, số liệu, thời gian chạy hoặc số lượng test. Nếu thiếu thông tin, ghi `[CẦN BỔ SUNG]`.
```

### Prompt 08 – Cập nhật `PROMPT_LOG.md`

```text
Hãy tạo một mục ghi nhật ký sử dụng AI để bổ sung vào `PROMPT_LOG.md` dựa trên thông tin tôi cung cấp.

Ghi các trường:
- Ngày thực hiện.
- Người thực hiện (nếu được cung cấp).
- Chapter/phần công việc.
- Mục tiêu sử dụng prompt.
- Prompt đã sử dụng hoặc mô tả ngắn.
- File được tạo/thay đổi.
- Kết quả AI đề xuất.
- Phần thành viên đã kiểm tra và chỉnh sửa.
- Trạng thái: đã xác minh / cần kiểm tra / không sử dụng.

Không tự điền tên người, ngày, file hoặc kết quả nếu tôi chưa cung cấp.
```

### Prompt 09 – Kiểm tra hoàn thiện trước khi commit Git

```text
Bạn là người kiểm tra chất lượng trước khi nhóm commit code lên Git.
Hãy kiểm tra các thay đổi trong [CHAPTER/FILE] dựa trên yêu cầu, `RULES.md`, `specs.md`, test và README.

Hãy xác nhận:
- File nằm đúng thư mục.
- Không có file tạm, cache hoặc thông tin bí mật.
- Import và lệnh chạy đúng cấu trúc dự án.
- Test đã được chạy và có log thật.
- Code và tài liệu mô tả thống nhất.
- Không ghi nhận chức năng chưa làm là đã hoàn thành.

Trả về bảng gồm hạng mục, trạng thái, bằng chứng và việc cần làm. Không tự tuyên bố đạt nếu không có bằng chứng.
```

---

## 4. Quy trình sử dụng prompt đề xuất

1. Dùng Prompt 01 để đọc đúng nội dung chapter.
2. Dùng Prompt 02 để phân tích yêu cầu.
3. Dùng Prompt 03 để hỗ trợ viết code.
4. Dùng Prompt 04 để tạo test.
5. Dùng Prompt 05 để review và sửa lỗi.
6. Dùng Prompt 06 để hoàn thiện `specs.md`.
7. Chạy chương trình và test thực tế, sau đó dùng Prompt 07 để viết `analyst.md`.
8. Dùng Prompt 08 ghi lại quá trình sử dụng AI.
9. Dùng Prompt 09 trước khi commit Git.

**Lưu ý:** Prompt không thay thế việc đọc giáo trình, hiểu công thức, tự kiểm tra code và chạy thử chương trình.

