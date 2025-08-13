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

    # -------- SETUP DRIVER -------- #
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # newer headless mode
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    # options.add_argument("--start-minimized")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument('--disable-dev-shm-usage')
    # Spoof a real user-agent (pick a common Chrome UA from your own machine)
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    )
    
    # Remove obvious automation flags
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)


    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
    """
        })  


    # -------- STEP 1: Go to Flipkart -------- #
    print("🚀 Opening Flipkart homepage...") #
    # search_box=WebDriverWait(driver, 5).until(driver.get("https://www.flipkart.com/"))
    driver.get("https://www.flipkart.com/")
    print("🚀 AFTER Opening Flipkart homepage...") ###

    time.sleep(7)

#--------------------------------
         # Close login popup
    try:
        close_button = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '✕')] | //span[@role='button' and contains(@class, '_30XB9F')]"))
        )
        close_button.click()
        print("🚀 Closed popup...")
        time.sleep(2)
    except:
        print("🚀 No popup to close...")

    # -------- STEP 2: Search Product -------- #
    search_box=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "q")))
    print(f"XXXXXXXXXXXXXXXX 0 ")
    # search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(SEARCH_QUERY)
    search_box.send_keys(Keys.RETURN)

    
    print(f"XXXXXXXXXXXXXXXX 1 ")
    time.sleep(2)

    # -------- STEP 3: Click on First Product -------- #
    try:
        time.sleep(1)

        product_link = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/p/') and @rel='noopener noreferrer']"))
        )
        product_url = product_link.get_attribute('href')
        driver.get(product_url)
        print(f"XXXXXXXXXXXXXXXX 2 ")
    except:
        print("❌ Could not find product link. Trying next product..")
        # continue
        driver.quit()

    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0);")

    # -------- STEP 4: Click on 'See All Reviews' -------- #
    try:
        all_reviews_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'reviews')]"))
        )
        time.sleep(1)
        all_reviews_button.click()
        print(f"XXXXXXXXXXXXXXXX 3 ")

    except:
        print("❌ Could not find 'View all reviews' button. Trying next product..")
        # continue
        driver.quit()

    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0);")


    # -------- STEP 5: Scrape Reviews -------- #
    reviews = []

    while len(reviews)<150:

        time.sleep(2)
        # review_block1 = driver.find_elements(By.XPATH, "//div[@class='col-4-12 F2+K4v']")

        ####"//div[contains(@class, 'col-4-12')]"
        
        review_block1 = []  # default empty list
        try:
            review_block1 = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH,"//div[@class='col-4-12 F2+K4v']"))
            )
            print("Found review blocks")
        except Exception as e:
                print("❌ No review_block1 found.")
                break



        for block in review_block1:
            try:
                print(f"xxx 0")
                overall_rating =  block.find_element(By.CLASS_NAME, "ipqd2A").text
                print(f"XXx 1")

            except:
                overall_rating = ""
                print("in the except of overall rating ")

            try:
                total_ratings= block.find_element(By.XPATH, ".//span[contains(text(), 'Ratings')]").text
                # total_ratings_value = total_ratings_txt.split()[0] //  i can use this to clean at sourse
            except:
                total_ratings = ""
#---------------------------------------------------------------------------------

        review_block2 = driver.find_elements(By.XPATH, "//div[@class='col EPCmJX Ma1fCG']")
    
        print(f"XXXXXXXXXXXXXXXX 4 ")


        time.sleep(4)
        for block in review_block2:
            try:
                User_rating = block.find_element(By.CSS_SELECTOR, ".XQDdHH.Ga3i8K").text
                print("INSIDE user rating try")
            except:
                User_rating = ""
                print("INSIDE user rating except")
            try:
                title = block.find_element(By.CLASS_NAME, "z9E0IG").text
            except:
                title = ""
                print("INSIDE user title ")

            try:
                comment = block.find_element(By.CLASS_NAME, "ZmyHeo").text
            except:
                comment = None
            
            reviews.append({
                "User_Rating": User_rating,
                "Title": title,
                "Comment": comment

            })
            print(f"XXXXXXXXXXXXXXXX 5")

    #------- Click next page --------#
        try:
            wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
            next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
            time.sleep(1)  # Optional: wait 1 seconds to mimic human behavior
            next_btn.click()
            print("xxxxxxxxxxxxx 6")
        except:
            print("No more pages.")
            break

    time.sleep(1)        
    #------------------STEP 6: Save -------------#
    output_data = {
        "search_query": SEARCH_QUERY,
        # "Product_name": SEARCH_QUERY,
        "total_reviews": len(reviews),
        "Overall_rating": overall_rating,
        "Total_ratings": total_ratings,
        "reviews": reviews
    }
    return output_data
    

