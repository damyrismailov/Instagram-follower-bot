from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

instagram_password = "your_password"
instagram_email = "email@gmail.com"
similar_acc = "thegeology"


class InstagramFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 3)
    def login(self):
        self.driver.get("https://www.instagram.com/?flo=true")
        sleep(5)
        email_input = self.driver.find_element(By.XPATH, "//*[@id='_R_32d9lplcldcpbn6b5ipamH1_']")
        email_input.send_keys(instagram_email)
        password_input = self.driver.find_element(By.XPATH, "//*[@id='_R_33d9lplcldcpbn6b5ipamH1_']")
        password_input.send_keys(instagram_password, Keys.ENTER)
        sleep(15)
        # save_login_never_button =  self.driver.find_element(By.XPATH, "//*[@id='mount_0_0_b9']/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div")
        # save_login_never_button.click()
        button = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if button:
            button.click()
        sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{similar_acc}")
        sleep(5)
        followers_button =  self.wait.until(ec.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/followers/')]")))
        if followers_button:
            followers_button.click()
        sleep(5)
        scroll = "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        modal = self.driver.find_element(by=By.XPATH, value=scroll)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)
    def follow_user(self):
        num = 1
        for i in range(20):
             sleep(3)
             follow_or_not = self.driver.find_element(By.XPATH, f"/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{num}]/div/div/div/div[3]/div/button/div/div")
             username= self.driver.find_element(By.XPATH, f"/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{num}]/div/div/div/div[2]/div/div/div/div/span/div/a/div/div/span").text
             if follow_or_not.text == "Following" or follow_or_not.text == "Requested":
                print(f"Following {username} already, skipping this person")
                num += 1
             elif follow_or_not.text == "Follow":
                 print(f"Following {username} at num {num}")
                 follow_button = self.driver.find_element(By.XPATH, f"/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{num}]/div/div/div/div[3]/div/button")
                 sleep(2)
                 follow_button.click()
                 num += 1
    # def follow(self):
    #     all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
    #     for button in all_buttons:
    #         try:
    #             button.click()
    #             sleep(1.5)
    #         except ElementClickInterceptedException:
    #             cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
    #             cancel_button.click()

instagram_follower = InstagramFollower()
try:
    instagram_follower.login()
except NoSuchElementException:
    instagram_follower.login()
instagram_follower.find_followers()
instagram_follower.follow_user()
