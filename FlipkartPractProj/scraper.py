import requests
import pandas as pd
from bs4 import BeautifulSoup


Product_Name = []
Reviews = []
Description = []
Price=[]



for i in range(1,11):
    url = "https://www.flipkart.com/search?q=mobile+phones+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_11_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_11_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+phones+under+50000&requestId=ca6f0259-f07a-498c-a203-1341f7a45400&as-backfill=on&page="+str(i)

    web = requests.get(url)

    soup = BeautifulSoup(web.text , "lxml")
    cards = soup.find_all("div" , class_="jIjQ8S")
    for card in cards:        
        #EXTRACTING Product Price
        price = card.find("div" , class_="hZ3P6w DeU9vF")
        if (price):
            Price.append(price.text)
        else:
            Price.append("N/A")
        #EXTRACTING Product Names    
        name = card.find("div" , class_="RG5Slk")
        if(name):
            Product_Name.append(name.text)
        else:
            Product_Name.append("N/A")
        #EXTRACTING REVIEWS
        review= card.find("div" , class_="MKiFS6")
        if(review):
          Reviews.append(review.text)
        else:
            Reviews.append("N/A")    
        #Extracting Product Description
        desc = card.find("div" , class_="CMXw7N")    
        if(desc):
          Description.append(desc.text)
        else:
            Description.append("N/A")
        
df = pd.DataFrame({"Product_Name":Product_Name , 
                    "Product_Price":Price , 
                    "Product_Reviews" :Reviews , 
                    "Product_Description":Description})
#replace the , and INR rupee sign with empty string
df["Product_Price"] = df["Product_Price"].str.replace("₹" , "").str.replace("," , "")
df.to_csv("C:/Users/fa/Desktop/python/Filpkart_Under50000_Phones.csv" , index=False )



#?THESE ARE PREVIOUS VERSIONS OF THE CODE
# for i in range(2,12):
#     url = "https://www.flipkart.com/search?q=mobile+phones+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_17_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_17_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+phones+under+50000&requestId=820ed649-a671-4c98-8faa-3a319e3138a1&as-backfill=on&page="+str(i)

#     r = requests.get(url)

#     soup = BeautifulSoup(r.text , "lxml")
    
#     np = soup.find("a" , class_="jgg0SZ").get("href")
#     cnp = "https://flipkart.com"+np
#     print(cnp)
    

 #------CHATGPT GIVEN CODE , WORKS SAME 
# def check_for_next(t):
#     if t:
#         if "Next" in t:
#             return True
#         else:
#             return False
#     else:
#         return False


# url = "https://www.flipkart.com/search?q=mobile+phones+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_17_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_17_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+phones+under+50000&requestId=820ed649-a671-4c98-8faa-3a319e3138a1&as-backfill=on&page=1"

# web = requests.get(url)
# print(f"this is the first page link/url----> {web.url}")
# # Start loop from 1 so you don't miss the first page data
# for i in range(1, 10):
#     url = "https://www.flipkart.com/search?q=mobile+phones+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_17_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_17_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+phones+under+50000&requestId=820ed649-a671-4c98-8faa-3a319e3138a1&as-backfill=on&page="+str(i)

#     r = requests.get(url)
#     soup = BeautifulSoup(r.text , "lxml")
    
#     # ---------------------------------------------------------
#     # CORRECTED LOGIC:
#     # We search for the <a> tag where the text is exactly "Next"
#     # or contains "Next" within its span.
#     # ---------------------------------------------------------
    
#     # This finds the specific 'a' tag that has 'Next' inside it
#     next_link = soup.find("a", string=lambda t: "Next" in t if t else False)

#     # Fallback: Sometimes the text is inside a <span> tag inside the <a> tag
#     if not next_link:
#         # We find all links with your class, and pick the one with 'Next' text
#         buttons = soup.find_all("a", class_="jgg0SZ")
#         for btn in buttons:
#             if "Next" in btn.text:
#                 next_link = btn
#                 break

#     if next_link:
#         cnp = "https://flipkart.com" + next_link.get("href")
#         print(f"Page {i} -> Next Page Link: {cnp}")
#     else:
#         print(f"Page {i} -> No 'Next' link found (Last Page).")




