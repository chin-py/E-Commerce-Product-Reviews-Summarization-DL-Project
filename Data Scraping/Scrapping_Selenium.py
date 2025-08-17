from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from pathlib import Path
import pandas as pd


#----------------Models list-------------#
import re
#iphones
text="iPhone 16e	iPhone 16 Pro Max	iPhone 16 Pro	iPhone 16 Plus	iPhone 16	iPhone 15 Pro Max	iPhone 15 Pro	iPhone 15 Plus	iPhone 15   iPhone 14 Pro Max	iPhone 14 Pro	iPhone 14 Plus	iPhone 14	iPhone SE	iPhone 13 Pro Max	iPhone 13 Pro	iPhone 13	iPhone 13 Mini	iPhone 12 Pro Max	iPhone 12 Pro	iPhone 12	iPhone 12 Mini	iPhone SE	iPhone 11 Pro Max	iPhone 11 Pro	iPhone 11	iPhone XR	iPhone XS Max	iPhone XS"
# new= text.replace("\u00a0"," ")

# new = re.sub(r'\s+', ' ', text)
# new1=new.replace(" iPhone",", iPhone")

#samsung
text2= "Samsung Galaxy S25 5G	Samsung Galaxy S25 Plus 5G	Samsung Galaxy S25 Ultra 5G	Samsung Galaxy S24 Plus 5G	Samsung Galaxy A35 5G	Samsung Galaxy S22 5G	Samsung Galaxy S24 Ultra 5G	Samsung Galaxy F16	Samsung Galaxy Z Flip 5 256	Samsung Galaxy Z Fold 5	Samsung Galaxy F22	Samsung Galaxy F41	Samsung Galaxy F62	Samsung A21s	Samsung Galaxy F02s	Samsung Galaxy A31	Samsung Galaxy A32	Samsung Galaxy A52	Samsung Galaxy A72	Samsung Galaxy S20 FE 5G"
# new = re.sub(r'\s+', ' ',text2)
# new1=new.replace(" Samsung",", Samsung")

# Motorola
# text3= "Motorola Moto G96	Motorola g22	Motorola g32	Motorola g72	Motorola g24	Motorola Edge 60	Motorola Edge 60 Pro	Motorola Edge 60 Stylus	Motorola one power	Motorola Edge 60 Fusion	Motorola Moto E7 power	Motorola Moto G8 power	Motorola Moto G05	Motorola Edge 50 Neo	Motorola Moto G35	Motorola Moto G31	Motorola Moto G45	Motorola Moto G64	Motorola Edge 50	Motorola Moto G54 Power 5G	Motorola Moto G85 5G	Motorola Moto G84 5G	Motorola Moto G14	Motorola Edge 40	Motorola Edge 30	Motorola Moto G13	Motorola Edge 30 Fusion	Motorola Edge 30 Ultra	Motorola Moto G73	Motorola Moto G62 5G	Motorola Moto G82"
# new = re.sub(r'\s+', ' ',text3)
# new1=new.replace(" Motorola",", Motorola")


#vivo
text4="Vivo IQOO Neo 10 (Global)	Vivo Y300 GT	Vivo iQOO Z9s	Vivo iQOO Z10x	Vivo iQOO Z10	Vivo T3 Lite 5G	Vivo T4x 5G	Vivo V50 5G	Vivo Y200 4G	Vivo iQOO Z9	Vivo X200 Pro	Vivo v50e	Vivo v40e  Vivo iQOO Z9  Vivo iQOO Z9 lite	Vivo T3 Ultra	Vivo T3 Pro 5G	Vivo iQOO Z9s	Vivo iQOO Z9s Pro	Vivo V40 Pro	Vivo V40	Vivo X100s	Vivo x100 Pro	Vivo Y18	Vivo iQOO Z9x	Vivo T3x	Vivo T3 5G	Vivo V30 Pro	Vivo V29 Pro	Vivo V29	Vivo V27 Pro	Vivo X90 Pro Vivo V27"
# new = re.sub(r'\s+', ' ',text4)
# new1=new.replace(" Vivo",", Vivo")


#boAt
text5="boAt Airdopes 181 Pro	BoAt Airdopes 161	BOAT Rockerz 255 Pro+	boAt Rockerz 109	boAt Rockerz 111	boat Airdopes Prime 701 ANC	boAt Nirvana Ion ANC	BoAt Airdopes 148	Bassheads 110	boAt Rockerz 110	boAt Airdopes 161 (Metallic)	boAt Rockerz 413	boAt Bassheads 104	boAt Airdopes 163	boAt Airdopes 141 ANC	boAt Airdopes 138	boAt Rockerz 425	boAt Rockerz 333 Pro	boAt Rockerz 333	boAt Rockerz Trinity	TRebel Airdopes 141	boAt Rockerz 421	boAt Nirvana Iris	boAt Airdopes 141 Gen 2	boAt Rockerz 150 Pro	boAt Nirvana Ivy Pro	boAt Airdopes 213	boAt Rockerz 650 Pro	Bassheads 162v2	boAt Rockerz 551 ANC Pro	boAt Rockerz 411	boAt Airdopes 207	boAt Rockerz 245 V2 Pro	boAt Airdopes 138 PRO	boAt Rockerz 412	boAt Airdopes 141 Elite ANC	boAt Nirvana Ion	boAt Nirvana Ion ANC Pro	boAt Airdopes 393 ANC	boAt Nirvana Crystl	boAt Rockerz 202	boAt Nirvana X TWS	boAt Airdopes Plus 318	boAt Rockerz 460	boAt Rockerz 203	boAt Nirvana Zenith Pro"
# new = re.sub(r'\s+', ' ',text5)
# new1 = re.sub(r'\bboat\b','boAt',new,flags=re.IGNORECASE)
# new1 = re.sub(' boAt',', boAt',new1)
#Oppo
text7="OPPO K12x 5G | OPPO A3x 5G | OPPO A3 5G | OPPO F27 Pro+ | OPPO Reno 12 Pro 5G | OPPO Reno 12 5G | OPPO Find X8 5G | OPPO Reno8T 5G | OPPO Reno 10 5G | OPPO A78 | OPPO A3x | OPPO A3 Pro 5G | OPPO F19s | OPPO A55 | OPPO A78 5G | OPPO F27 Pro+ | OPPO A79 | OPPO Find N2 | OPPO A36 | OPPO A96 5G | OPPO Reno6 Lite | OPPO A76 | OPPO Reno7 Z | OPPO A16e | OPPO A96 | OPPO K10 | OPPO Find N2 | OPPO Reno13 | OPPO Reno13 Pro | OPPO Reno14 | OPPO Reno14 Pro | OPPO Reno12 | OPPO Find X8 Pro | OPPO Find N5"
# new= re.sub(r' \| OPPO',', Oppo',text7)



#Boult
text6="Boult Ammo earbuds	Boult Curve Buds Pro	Boult Curve Max earphone	Boult probass EQCharge	Boult Ember Bluetooth	Boult Escape	Boult probass fcharge neckband	Boult ProBass EQCharge neckband	Boult ProBass Xcharge neckband	Boult boult k10  50H	Boult X45	Boult y1 with zen earbuds	Boult y1 pro zen earbuds	Boult w20 zen enc mic earbuds	Boult Ycharge with Pro+ calling earphone	Boult z60 	Boult Z40	Boult Rcharge 30H playtime neckband	Boult klarity 1	Boult astra earbuds	Boult X1 pro	Boult X10 earbuds	Boult X45 earbuds	Boult X50 earbuds	Boult X60 earbuds	Boult z40 pro earbuds	Boult Z35 earbuds	Boult Z60 earbuds"
# new = re.sub(r'\s+', ' ',text6)
# new1 = re.sub(' boult',', Boult',new)

#fire-boltt
text8="Fire-Boltt Talk	Fire-Boltt Legacy	Fire-Boltt Ring 	Fire-Boltt Hurricane 	Fire-Boltt Ninja Calling Pro Plus	Fire-Boltt Rise	Fire-Boltt Hunter Nyluxe	Fire-Boltt Nnja Talk	Fire-Boltt Clickk	Fire-Boltt Rise Luxe	Fire-Boltt Ring X	Fire-Boltt Spacewatch	Fire-Boltt Oracle	Fire-Boltt Hurricane	Fire-Boltt Legacy	Fire-Boltt Dream WristPhone	Fire-Boltt Brillia	Fire-Boltt 4G Pro Volte	Fire-Boltt Lumos	Fire-Boltt Astra Luxury	Fire-Boltt Brillia Pro	Fire-Boltt Xelor Luxury	Fire-Boltt Obsidian	Fire-Boltt Reto"
new = re.sub(r'\s+', ' ',text8)
new1 = re.sub(' Fire-Boltt',', Fire-Boltt',new)



list_models=[]
list_models= new1.split(", ")
list_models_batch =list_models[11:]
print(list_models_batch)


for i in list_models_batch:
    # -------- CONFIGURATION -------- #
    SEARCH_QUERY = i 
    CHROMEDRIVER_PATH = "D:\\CDAC\\1. PG DBDA\\project cdac\\Data scrapping\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"  # 🔁 Update if different path

    # -------- SETUP DRIVER -------- #
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)

    # -------- STEP 1: Go to Flipkart -------- #
    driver.get("https://www.flipkart.com/")
    time.sleep(6)

    # Close login popup
    try:
        close_button = driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
        close_button.click()
    except:
        pass  # Popup may not appear sometimes

    # -------- STEP 2: Search Product -------- #
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(SEARCH_QUERY)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    # -------- STEP 3: Click on First Product -------- #
    try:
        product_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/p/') and @rel='noopener noreferrer']"))
        )
        product_url = product_link.get_attribute('href')
        driver.get(product_url)
    except:
        print("Could not find product link. Trying next product..")
        continue
        # driver.quit()

    # -------- STEP 4: Click on 'See All Reviews' -------- #
    try:
        all_reviews_button = WebDriverWait(driver, 11).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'reviews')]"))
        )
        all_reviews_button.click()
    except:
        print("Could not find 'View all reviews' button. Trying next product..")
        continue
        # driver.quit()

    time.sleep(5)

    # -------- STEP 5: Scrape Reviews -------- #
    reviews = []

    while True:
        time.sleep(4)
        review_block1 = driver.find_elements(By.XPATH, "//div[@class='col-4-12 F2+K4v']")



        for block in review_block1:
            try:

                overall_rating =  block.find_element(By.CLASS_NAME, "ipqd2A").text
            except:
                overall_rating = ""

            try:
                total_ratings= block.find_element(By.XPATH, ".//span[contains(text(), 'Ratings')]").text
                # total_ratings_value = total_ratings_txt.split()[0] //  i can use this to clean at source
            except:
                total_ratings = ""


        review_block2 = driver.find_elements(By.XPATH, "//div[@class='col EPCmJX Ma1fCG']")

        time.sleep(1)
        for block in review_block2:
            try:
                User_rating = block.find_element(By.CSS_SELECTOR, ".XQDdHH.Ga3i8K").text
            except:
                User_rating = ""
            try:
                title = block.find_element(By.CLASS_NAME, "z9E0IG").text
            except:
                title = ""
            try:
                comment = block.find_element(By.CLASS_NAME, "ZmyHeo").text
            except:
                comment = ""
            
            reviews.append({
                "User_Rating": User_rating,
                "Title": title,
                "Comment": comment

            })

        # Click next page
        # try:
        #     next_btn = driver.find_element(By.XPATH, "//span[text()='Next']")
        #     next_btn.click()
        # except:
        #     print("No more pages.")
        #     break
        try:
            wait = WebDriverWait(driver, 5)  # Wait up to 5 seconds
            next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
            time.sleep(2)  # Optional: wait 2 seconds to mimic human behavior
            next_btn.click()
        except:
            print("No more pages.")
            break

    time.sleep(1)        
    #------------------STEP 6: Save to JSON-------------#
    output_data = {
        "search_query": SEARCH_QUERY, # Product_name
        "total_reviews": len(reviews),
        "Overall_rating": overall_rating,
        "Total_ratings": total_ratings,
        "reviews": reviews
    }

    

    # path_to_save = Path(r"D:\CDAC\1. PG DBDA\project cdac\Reviews_scrapped") # location to save the scrapped reviews
    # path_to_save = Path(r"D:\CDAC\1. PG DBDA\project cdac\Reviews_scrapped\Samsung_reviews") # samsung
    # path_to_save = Path(r"D:\CDAC\1. PG DBDA\project cdac\Reviews_scrapped\Motorola_reviews") # Motorola
    # path_to_save = Path(r"D:\CDAC\1. PG DBDA\project cdac\Reviews_scrapped\Vivo_reviews") # vivo
    # path_to_save = Path(r"D:\CDAC\1. PG DBDA\project cdac\Reviews_scrapped\Boult_reviews") # boult
    path_to_save = Path(r"D:\CDAC\1. PG DBDA\project cdac\Reviews_scrapped\Fire-Boltt_reviews") # fire-boltt
    # path_to_save = Path(r"D:\CDAC\1. PG DBDA\project cdac\Reviews_scrapped\boAt_reviews") # boult
    filename = path_to_save / f"{SEARCH_QUERY}_flipkart_reviews.json"
    # filename = f"{SEARCH_QUERY}_flipkart_reviews.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Scrapped Data saved to '{filename}'")
    driver.quit()

