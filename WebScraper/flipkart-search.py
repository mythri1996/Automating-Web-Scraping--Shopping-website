from autoscraper import AutoScraper
flipkart_url="https://www.flipkart.com/laptops-store?otracker=nmenu_sub_Electronics_0_Laptops"
wanted_list=["₹55,990","ASUS TUF Gaming F15 Core i5 10th Gen - (8 GB/512 GB SSD/Windows 10 Home/4 GB Graphics/NVIDIA GeForce GTX 1650 Ti/60 Hz) FX506LI-BQ057T Gaming Laptop",'4.5',"(730)"]
scraper=AutoScraper()
result=scraper.build(flipkart_url,wanted_list)
print(scraper.get_result_similar(flipkart_url,grouped=True))