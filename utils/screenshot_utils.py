import os
import time


def capture_screenshot(driver, test_name, screenshot_dir="screenshots"):
    """
    Captures a screenshot of the current browser state.
    """
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_filename = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")
    return screenshot_path

