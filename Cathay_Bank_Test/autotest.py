import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Open Chrome browser with mobile emulation settings.
mobile_emulation_android = {
    "deviceMetrics": {"width": 360, "height": 670, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
}

mobile_emulation_ios = {
    "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 2.0},  # iPhone 11 dimensions
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation_ios)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

# Configuration
screenshot_path = "C:\\Users\\USER\\Desktop\\"
base_url = "https://www.cathaybk.com.tw/cathaybk/"

def wait_and_screenshot(element_locator, screenshot_name):
    try:
        element = wait.until(EC.visibility_of_element_located(element_locator))
        save_screenshot(screenshot_name)
        return element
    except TimeoutException:
        print(f"Timeout waiting for element: {element_locator}")
        raise  # Re-raise the exception to indicate a failure

def save_screenshot(filename):
    driver.save_screenshot(f"{screenshot_path}{filename}")

try:
    # Navigate to the Cathay Bank website.
    driver.get(base_url)

    # Wait for the burger menu to be visible and take a screenshot of the initial page.
    element_burger = wait_and_screenshot((By.XPATH, "//header/div/div[1]"), "screenshot.png")

    # Click on the burger menu to open additional options.
    element_burger.click()

    # Click on the "產品介紹" (Product Introduction) link.
    element_product_intro = wait_and_screenshot((By.XPATH, "//header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]"), "screenshot_product_intro.png")
    element_product_intro.click()

    # Click on the "信用卡" (Credit Card) link.
    element_credit = wait_and_screenshot((By.XPATH, "//header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]"), "screenshot_credit_card.png")
    element_credit.click()

    # Count the number of credit card list items.
    credit_parent_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cubre-o-menuLinkList__item.is-L2open")))
    credit_lnk_links = credit_parent_element.find_elements(By.ID, "lnk_Link")
    credit_num = len(credit_lnk_links)
    print("Credit card list item: ", credit_num)

    # Take a screenshot of the credit page.
    save_screenshot("screenshot_credit_page.png")

    # Scroll to the "卡片介紹" (Card Introduction) link within the menu.
    lnk_element = wait_and_screenshot(
        (By.XPATH, '//div[contains(@class, "cubre-o-menuLinkList__item") and contains(@class, "is-L2open")]//a[contains(text(), "卡片介紹")]'),
        "screenshot_card_intro_link.png"
    )
    lnk_element.click()

    # Take screenshots of each section in a slider with pagination.
    target_element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/article/section[6]/div')))
    driver.execute_script("arguments[0].scrollIntoView(true);", target_element)

    pagination_parent = driver.find_element(By.CSS_SELECTOR, 'body > div.cubre-o-container > main > article > section:nth-child(7) > div > div.cubre-o-block__component > div > div.cubre-o-slide__page')

    pagination_bullets = pagination_parent.find_elements(By.CLASS_NAME, 'swiper-pagination-bullet')

    slide_count = 0
    for index, bullet in enumerate(pagination_bullets, start=1):
        bullet.click()
        time.sleep(0.3)
        save_screenshot(f"screenshot_stop_card_{index}.png")
        slide_count += 1

    print(f"Stop cards count: {slide_count}")

except NoSuchElementException as e:
    print(f"Element not found: {str(e)}")
except TimeoutException:
    print("Timeout waiting for an element")
except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser window after completing the tasks.
    driver.quit()
