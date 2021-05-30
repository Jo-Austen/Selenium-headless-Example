from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

chrome_options.add_argument('--window-size=1920,1050')

# 创建浏览器对象
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Chrome()  # 不加 chrome_options 参数就是正常的打开一个浏览器，进行操作
driver.implicitly_wait(10)  

# 访问URL
driver.get('https://app.77hub.com/cn-global/login')
username = driver.find_element_by_css_selector("#root > div > div._3PTQO6SSLkfkhgUDSNnMsG > div._11shczH-kuHWdF4aBACbNJ > div._3gtWl95XzmToV3rB8ytqiX > div > div > div.D2N9CcrtDp7Re5jCZU7qj > div.ms-LayoutGroup.css-1 > div.ms-LayoutGroup-item.css-0 > div > div.atx-input-group__bundle > div > input")
username.send_keys('18267526839')
password = driver.find_element_by_css_selector("#root > div > div._3PTQO6SSLkfkhgUDSNnMsG > div._11shczH-kuHWdF4aBACbNJ > div._3gtWl95XzmToV3rB8ytqiX > div > div > div.D2N9CcrtDp7Re5jCZU7qj > div.ms-LayoutGroup.css-1 > div:nth-child(2) > div > div.atx-input-group__bundle > div > input")
password.send_keys("Zj3032476110")

driver.find_element_by_css_selector("#root > div > div._3PTQO6SSLkfkhgUDSNnMsG > div._11shczH-kuHWdF4aBACbNJ > div._3gtWl95XzmToV3rB8ytqiX > div > div > div.D2N9CcrtDp7Re5jCZU7qj > button > span").click()

time.sleep(5)

close_button = driver.find_element_by_css_selector("body > div:nth-child(17) > div > div.bp3-dialog-container.bp3-overlay-content.bp3-overlay-enter-done > div > div.bp3-dialog.atx-dialog._1ydevlj2oOiyYgwpjV-YQZ.css-1lz4uyl > div > div.advance-dialog-footer._131YhmYtWVPNjmPxq8T1WB > button.bp3-button.bp3-minimal.atx-button.atx-button--raised.atx-button-secondary > span")
close_button.click()

driver.find_element_by_css_selector("body > div.bp3-portal > div > div._31ajromK3XvJ7oOYpi4M1J.bp3-overlay-content.bp3-overlay-enter-done > div > div.custom-swiper-control > div.custom-swiper-control__action.custom-swiper-control__action--right").click()
driver.find_element_by_css_selector("body > div.bp3-portal > div > div._31ajromK3XvJ7oOYpi4M1J.bp3-overlay-content.bp3-overlay-enter-done > div > div.custom-swiper-control > div.custom-swiper-control__action.custom-swiper-control__action--right").click()

driver.find_element_by_css_selector("body > div.bp3-portal > div > div._31ajromK3XvJ7oOYpi4M1J.bp3-overlay-content.bp3-overlay-enter-done > div > div.swiper-container.swiper-container-initialized.swiper-container-horizontal.swiper-container-pointer-events > div.swiper-wrapper > div.swiper-slide.swiper-slide-active > div > div._-3jkSXRG9I4shaOd6H1v > div > a:nth-child(1)").click()

layer_frist = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[1]/div/div[2]/div[1]')
layer_frist.click()

time.sleep(2)
driver.save_screenshot("screenshot01.png")
# print(driver.page_source)

# daily_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[2]/div/div[2]")
driver.find_elements_by_css_selector("body > div.bp3-portal")
daily_button = driver.find_element_by_css_selector("body > div.bp3-portal > div > div > div > div > div > div._1PGk-m9ck6DowacnraCWLP > div > div:nth-child(2)")

daily_button.click()

# print("跳转到填写页面")

time.sleep(3)

#开始填写
item_input = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div[7]/div[2]/div/span/span/div/div[1]/div/input')
item_input.click()
item_input.send_keys("ELC_Y20 Event Procurement Sys I_CO_PROD_20200916")
ActionChains(driver).send_keys(Keys.ENTER).perform()
time.sleep(2)
driver.save_screenshot("screenshot01.png")

item_progess = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]')
item_progess.click()
time.sleep(2)

# item_progess.send_keys("d")
ActionChains(driver).double_click(item_progess).perform()
time.sleep(2)
ActionChains(driver).send_keys(Keys.ENTER).perform()
driver.save_screenshot("screenshot02.png")

time_len = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[8]')
                                        
time_len.click()
time.sleep(2)
time_len.send_keys("8")
driver.save_screenshot("screenshot03.png")

work_info = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[9]')                               
work_info.click()
work_info.send_keys("这次会成功吗")

# work_info.send_keys("这次会成功吗")

time.sleep(5)
driver.save_screenshot("screenshot04.png")

# driver.save_screenshot("screenshot03.png")

submit = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[3]/div/div[2]/span[2]/span/button/span')
# submit.click()
time.sleep(10)
driver.save_screenshot("screenshot05.png")
# driver.quit()

# driver.save_screenshot("screenshot.png")