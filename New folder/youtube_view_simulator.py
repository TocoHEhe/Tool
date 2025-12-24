"""
YouTube View Simulator - Educational Purpose Only
==================================================

⚠️ CẢNH BÁO QUAN TRỌNG:
- Tool này chỉ dành cho mục đích giáo dục và nghiên cứu
- Việc tăng view YouTube giả mạo VI PHẠM Terms of Service của YouTube
- Có thể dẫn đến việc tài khoản bị khóa vĩnh viễn
- Không sử dụng tool này cho mục đích thương mại hoặc lừa đảo

Mục đích học tập:
- Hiểu cách các bot view hoạt động (để phòng chống)
- Nghiên cứu về web automation
- Học về Selenium và web scraping
"""

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
import logging

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class YouTubeViewSimulator:
    """
    Class mô phỏng việc xem video YouTube
    CHỈ DÀNH CHO MỤC ĐÍCH GIÁO DỤC
    """
    
    def __init__(self, headless=False, use_proxy=False):
        """
        Khởi tạo simulator
        
        Args:
            headless: Chạy browser ở chế độ ẩn (True) hoặc hiển thị (False)
            use_proxy: Có sử dụng proxy hay không
        """
        self.driver = None
        self.headless = headless
        self.use_proxy = use_proxy
        self.view_count = 0
        
    def setup_driver(self):
        """Thiết lập Chrome WebDriver với các tùy chọn"""
        chrome_options = Options()
        
        if self.headless:
            chrome_options.add_argument('--headless')
        
        # Các tùy chọn để tránh bị phát hiện
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        # Tắt thông báo
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.media_stream": 2,
        }
        chrome_options.add_experimental_option("prefs", prefs)
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            # Ẩn webdriver property
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            logger.info("WebDriver đã được khởi tạo thành công")
            return True
        except Exception as e:
            logger.error(f"Lỗi khi khởi tạo WebDriver: {e}")
            return False
    
    def simulate_human_behavior(self, duration_min=30, duration_max=120):
        """
        Mô phỏng hành vi người dùng thực
        
        Args:
            duration_min: Thời gian xem tối thiểu (giây)
            duration_max: Thời gian xem tối đa (giây)
        """
        if not self.driver:
            logger.error("WebDriver chưa được khởi tạo")
            return False
        
        try:
            # Cuộn trang ngẫu nhiên
            scroll_pause = random.uniform(2, 5)
            time.sleep(scroll_pause)
            
            # Cuộn xuống một chút
            scroll_amount = random.randint(100, 500)
            self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            time.sleep(random.uniform(1, 3))
            
            # Đôi khi di chuyển chuột (nếu không headless)
            if not self.headless:
                from selenium.webdriver.common.action_chains import ActionChains
                actions = ActionChains(self.driver)
                try:
                    video_element = self.driver.find_element(By.TAG_NAME, "video")
                    actions.move_to_element(video_element).perform()
                except:
                    pass
            
            # Thời gian xem video
            watch_duration = random.randint(duration_min, duration_max)
            logger.info(f"Đang xem video trong {watch_duration} giây...")
            
            # Xem video với các hành động ngẫu nhiên
            elapsed = 0
            while elapsed < watch_duration:
                sleep_time = random.uniform(5, 15)
                time.sleep(min(sleep_time, watch_duration - elapsed))
                elapsed += sleep_time
                
                # Đôi khi tạm dừng/play (mô phỏng)
                if random.random() < 0.1:  # 10% khả năng
                    try:
                        self.driver.execute_script(
                            "var video = document.querySelector('video');"
                            "if (video) { video.paused ? video.play() : video.pause(); }"
                        )
                        time.sleep(random.uniform(1, 3))
                        self.driver.execute_script(
                            "var video = document.querySelector('video');"
                            "if (video && video.paused) video.play();"
                        )
                    except:
                        pass
            
            logger.info("Hoàn thành xem video")
            return True
            
        except Exception as e:
            logger.error(f"Lỗi khi mô phỏng hành vi: {e}")
            return False
    
    def watch_video(self, video_url, watch_duration_min=30, watch_duration_max=120):
        """
        Xem một video YouTube
        
        Args:
            video_url: URL của video YouTube
            watch_duration_min: Thời gian xem tối thiểu (giây)
            watch_duration_max: Thời gian xem tối đa (giây)
        """
        if not self.driver:
            if not self.setup_driver():
                return False
        
        try:
            logger.info(f"Đang mở video: {video_url}")
            self.driver.get(video_url)
            
            # Đợi video load
            wait = WebDriverWait(self.driver, 10)
            try:
                wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))
            except TimeoutException:
                logger.warning("Không tìm thấy video element, tiếp tục...")
            
            # Đợi một chút để page load hoàn toàn
            time.sleep(random.uniform(2, 5))
            
            # Bấm play nếu video chưa tự động play
            try:
                play_button = self.driver.find_element(
                    By.CSS_SELECTOR, 
                    "button[aria-label*='Play'], button[aria-label*='Phát']"
                )
                if play_button:
                    play_button.click()
                    time.sleep(1)
            except:
                # Thử cách khác
                try:
                    self.driver.execute_script(
                        "var video = document.querySelector('video');"
                        "if (video && video.paused) video.play();"
                    )
                except:
                    pass
            
            # Mô phỏng hành vi người dùng
            success = self.simulate_human_behavior(watch_duration_min, watch_duration_max)
            
            if success:
                self.view_count += 1
                logger.info(f"Đã xem video thành công. Tổng số view: {self.view_count}")
            
            return success
            
        except Exception as e:
            logger.error(f"Lỗi khi xem video: {e}")
            return False
    
    def watch_multiple_videos(self, video_urls, delay_between_views=60):
        """
        Xem nhiều video
        
        Args:
            video_urls: Danh sách URL video
            delay_between_views: Thời gian chờ giữa các lần xem (giây)
        """
        logger.info(f"Bắt đầu xem {len(video_urls)} video...")
        
        for i, url in enumerate(video_urls, 1):
            logger.info(f"\n--- Video {i}/{len(video_urls)} ---")
            self.watch_video(url)
            
            if i < len(video_urls):
                wait_time = random.randint(delay_between_views, delay_between_views * 2)
                logger.info(f"Đợi {wait_time} giây trước khi xem video tiếp theo...")
                time.sleep(wait_time)
    
    def close(self):
        """Đóng browser"""
        if self.driver:
            self.driver.quit()
            logger.info("Đã đóng browser")
    
    def __enter__(self):
        """Context manager entry"""
        self.setup_driver()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()


def main():
    """
    Hàm main - Ví dụ sử dụng
    """
    print("=" * 60)
    print("YouTube View Simulator - Educational Purpose Only")
    print("=" * 60)
    print("\n⚠️  CẢNH BÁO:")
    print("Tool này chỉ dành cho mục đích giáo dục và nghiên cứu.")
    print("Việc sử dụng để tăng view giả mạo VI PHẠM Terms of Service của YouTube.")
    print("=" * 60)
    
    # Ví dụ URL (thay bằng URL video của bạn)
    video_url = input("\nNhập URL video YouTube (hoặc Enter để dùng ví dụ): ").strip()
    if not video_url:
        video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Ví dụ
    
    # Số lần xem
    try:
        num_views = int(input("Số lần xem (mặc định 1): ") or "1")
    except ValueError:
        num_views = 1
    
    # Sử dụng context manager
    with YouTubeViewSimulator(headless=False) as simulator:
        for i in range(num_views):
            print(f"\n--- Lần xem {i+1}/{num_views} ---")
            simulator.watch_video(
                video_url,
                watch_duration_min=30,
                watch_duration_max=120
            )
            
            if i < num_views - 1:
                delay = random.randint(30, 60)
                print(f"\nĐợi {delay} giây trước lần xem tiếp theo...")
                time.sleep(delay)
    
    print("\n" + "=" * 60)
    print("Hoàn thành! Đây chỉ là mô phỏng cho mục đích giáo dục.")
    print("=" * 60)


if __name__ == "__main__":
    main()

