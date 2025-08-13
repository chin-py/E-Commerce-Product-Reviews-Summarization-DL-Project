from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# import json
# from pathlib import Path
# import pandas as pd



def scrape_review(SEARCH_QUERY):
    # -------- CONFIGURATION -------- #
    # SEARCH_QUERY = i 
    # CHROMEDRIVER_PATH = "chromedriver"  # 🔁 Update if different path
    
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')      # if you don't need a visible browser
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    # -------- SETUP DRIVER -------- #
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")  # newer headless mode
    options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # options.add_argument("--start-minimized")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    # -------- STEP 1: Go to Flipkart -------- #
    print("🚀 Opening Flipkart homepage...") ################################3
    # search_box=WebDriverWait(driver, 5).until(driver.get("https://www.flipkart.com/"))
    driver.get("https://www.flipkart.com/")
    print("🚀 AFTER Opening Flipkart homepage...") ################################3

    time.sleep(10)

    # Close login popup
    try:

        close_button=WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), '✕')]"))
    )
       
        # #--------------------------------
        print("🚀 found")################################
        # close_button = driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
        close_button.click()
        print("🚀 close popup...")################################
    except:
        pass  # Popup may not appear sometimes
        print("🚀 close fail popup...")################################

    # -------- STEP 2: Search Product -------- #
    search_box=WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.NAME, "q")))
    print(f"XXXXXXXXXXXXXXXX 0 ")
    # search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(SEARCH_QUERY)
    search_box.send_keys(Keys.RETURN)
    print(f"XXXXXXXXXXXXXXXX 1 ")
    time.sleep(3)

    # -------- STEP 3: Click on First Product -------- #
    try:
        product_link = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/p/') and @rel='noopener noreferrer']"))
        )
        product_url = product_link.get_attribute('href')
        driver.get(product_url)
        print(f"XXXXXXXXXXXXXXXX2 ")
    except:
        print("❌ Could not find product link. Trying next product..")
        # continue
        driver.quit()

    # -------- STEP 4: Click on 'See All Reviews' -------- #
    try:
        all_reviews_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'reviews')]"))
        )
        all_reviews_button.click()
        print(f"XXXXXXXXXXXXXXXX3 ")
    except:
        print("❌ Could not find 'View all reviews' button. Trying next product..")
        # continue
        driver.quit()

    time.sleep(2)


    # -------- STEP 5: Scrape Reviews -------- #
    reviews = []

    while len(reviews)<80:

        time.sleep(1)
        # review_block1 = driver.find_elements(By.XPATH, "//div[@class='col-4-12 F2+K4v']")
        ###################---------------###################################
        try:
            # review_block1 = driver.find_elements(By.XPATH, "//div[@class='col-4-12 F2+K4v']")

          review_block1= WebDriverWait(driver, 20).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='col-4-12 F2+K4v']")))
          print(f"Found  review blocks")
        except Exception as e:
            print(f"Could not find review blocks: {e}")
        ###################---------------###################################

        for block in review_block1:
            try:
                overall_rating =  block.find_element(By.CLASS_NAME, "ipqd2A").text
                print(f"XXXXX")##########################

            except:
                overall_rating = ""
                print("in the except of overall rating ")##########################

            try:
                total_ratings= block.find_element(By.XPATH, ".//span[contains(text(), 'Ratings')]").text
                # total_ratings_value = total_ratings_txt.split()[0] //  i can use this to clean at sourse
            except:
                total_ratings = ""

        review_block2 = driver.find_elements(By.XPATH, "//div[@class='col EPCmJX Ma1fCG']")
      
#-----------------------------------------------------------------

        # review_block2=WebDriverWait(driver, 10).until(
        #             (By.XPATH, "//div[@class='col EPCmJX Ma1fCG']"))

      #-----------------------------------------------------------------
        print(f"XXXXXXXXXXXXXXXX 4 ")
        # print(f"XXXXXXXXXXXXXXXX4 {total_ratings}")
        # print(f"XXXXXXXXXXXXXXXX4 {overall_rating}")

        time.sleep(4)
        for block in review_block2:
            try:
                User_rating = block.find_element(By.CSS_SELECTOR, ".XQDdHH.Ga3i8K").text
                print("INSIDE user rating try")###############################
            except:
                User_rating = ""
                print("INSIDE user rating except")################################
            try:
                title = block.find_element(By.CLASS_NAME, "z9E0IG").text
            except:
                title = ""
                print("INSIDE user title ")####################################################3

            try:
                comment = block.find_element(By.CLASS_NAME, "ZmyHeo").text
            except:
                comment = None
            
            reviews.append({
                "User_Rating": User_rating,
                "Title": title,
                "Comment": comment

            })
            print(f"XXXXXXXXXXXXXXXX5 {reviews}")

        # Click next page
        # try:
        #     next_btn = driver.find_element(By.XPATH, "//span[text()='Next']")
        #     next_btn.click()
        # except:
        #     print("No more pages.")
        #     break
        try:
            wait = WebDriverWait(driver, 15)  # Wait up to 10 seconds
            next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
            time.sleep(1)  # Optional: wait 2 seconds to mimic human behavior
            next_btn.click()
            print("hell00000000000000")
        except:
            print("No more pages.")
            break

    time.sleep(1)        
    #------------------STEP 6: Save to JSON-------------#
    output_data = {
        "search_query": SEARCH_QUERY,
        # "Product_name": SEARCH_QUERY,
        "total_reviews": len(reviews),
        "Overall_rating": overall_rating,
        "Total_ratings": total_ratings,
        "reviews": reviews
    }
    return output_data
    

