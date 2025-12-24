# YouTube View Simulator - Educational Purpose Only

⚠️ **CẢNH BÁO QUAN TRỌNG**

Tool này được tạo ra **CHỈ DÀNH CHO MỤC ĐÍCH GIÁO DỤC VÀ NGHIÊN CỨU**.

## ⚠️ Lưu ý quan trọng:

1. **Vi phạm Terms of Service**: Việc tăng view YouTube giả mạo **VI PHẠM** Terms of Service của YouTube
2. **Rủi ro tài khoản**: Có thể dẫn đến việc tài khoản YouTube bị khóa vĩnh viễn
3. **Hợp pháp**: Có thể vi phạm pháp luật về gian lận trực tuyến
4. **Không khuyến khích**: Không sử dụng tool này cho mục đích thương mại hoặc lừa đảo

## 📚 Mục đích học tập:

- Hiểu cách các bot view hoạt động (để phòng chống)
- Nghiên cứu về web automation với Selenium
- Học về web scraping và browser automation
- Nghiên cứu về phát hiện bot và anti-bot systems

## 🛠️ Cài đặt:

1. Cài đặt Python 3.7+
2. Cài đặt dependencies:

```bash
pip install -r requirements.txt
```

3. Tải ChromeDriver:
   - Tự động: Selenium sẽ tự động tải nếu dùng webdriver-manager
   - Thủ công: Tải từ https://chromedriver.chromium.org/ và đặt trong PATH

## 📖 Cách sử dụng:

### Sử dụng cơ bản:

```python
from youtube_view_simulator import YouTubeViewSimulator

# Tạo simulator
simulator = YouTubeViewSimulator(headless=False)

# Xem một video
simulator.watch_video(
    "https://www.youtube.com/watch?v=VIDEO_ID",
    watch_duration_min=30,
    watch_duration_max=120
)

# Đóng browser
simulator.close()
```

### Sử dụng với Context Manager:

```python
with YouTubeViewSimulator(headless=False) as simulator:
    simulator.watch_video("https://www.youtube.com/watch?v=VIDEO_ID")
```

### Xem nhiều video:

```python
video_urls = [
    "https://www.youtube.com/watch?v=VIDEO_ID_1",
    "https://www.youtube.com/watch?v=VIDEO_ID_2",
]

with YouTubeViewSimulator() as simulator:
    simulator.watch_multiple_videos(video_urls, delay_between_views=60)
```

### Chạy script:

```bash
python youtube_view_simulator.py
```

## 🔧 Tính năng:

- ✅ Mô phỏng hành vi người dùng thực (cuộn trang, di chuyển chuột)
- ✅ Thời gian xem ngẫu nhiên
- ✅ Tự động play video
- ✅ Tránh phát hiện bot (user-agent, ẩn automation flags)
- ✅ Logging chi tiết
- ✅ Xử lý lỗi

## ⚙️ Tùy chọn:

- `headless`: Chạy browser ở chế độ ẩn (True/False)
- `use_proxy`: Sử dụng proxy (chưa implement đầy đủ)
- `watch_duration_min/max`: Thời gian xem video (giây)

## 📝 Lưu ý kỹ thuật:

1. **ChromeDriver**: Cần ChromeDriver tương thích với phiên bản Chrome
2. **Tốc độ**: Xem quá nhiều video trong thời gian ngắn sẽ bị phát hiện
3. **IP Address**: YouTube có thể theo dõi IP address
4. **Cookies/Session**: Cần đăng nhập để view được tính (tùy chọn)

## 🎓 Bài học:

Tool này giúp bạn hiểu:
- Cách Selenium hoạt động
- Web automation cơ bản
- Cách các platform phát hiện bot
- Tầm quan trọng của việc tuân thủ Terms of Service

## ⚖️ Trách nhiệm:

Người sử dụng tool này chịu hoàn toàn trách nhiệm về việc sử dụng. Tác giả không chịu trách nhiệm cho bất kỳ hậu quả nào phát sinh từ việc sử dụng tool này.

## 📄 License:

Educational Purpose Only - Không sử dụng cho mục đích thương mại hoặc vi phạm ToS.

