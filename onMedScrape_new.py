from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests 
import pandas as pd
import psycopg2
import SQLinsertion
import timestampFunc

link_list = [#"https://news.detik.com/indeks",
             #"https://finance.detik.com/indeks",
             "https://news.kompas.com/search/"]

def onMedScrape(link):
  tableName = "public.newsonmed"
  req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
  webpage = urlopen(req).read()
  soup = BeautifulSoup(webpage, 'html.parser')    

  with requests.Session() as c:
      soup = BeautifulSoup(webpage, 'html.parser')
      def onmedScrapingKompasNews(link):
          news = []
          try:
                resp = requests.get(link)
                
                # Check link respond
                if resp.status_code == 200:
                    soup = BeautifulSoup(resp.text, "html.parser")
                    
                    # News Source
                    source = "Kompas News"
                    
                    # Titile
                    title = soup.find("h1").get_text(strip=True)
                    
                    # Newsdate
                    newsdate = soup.find("div", class_="read__time").get_text(strip=True)
                    newsdate = timestampFunc.formattedNewsDetik(newsdate)

                    # Author
                    author = soup.find("div", class_="credit-title").get_text(strip=True)
                    
                    # Content
                    content = soup.find("div", class_="clearfix")
                    if content:
                        content = content.text.strip()
                    else:
                        print("Content not found.")
                        
                    # Image
                    image = soup.find("img", class_="p_img_zoomin img-zoomin")

                    # News link
                    link = link
                        
          except Exception as e:
                pass
          
          data = {
          'Source' : "Kompas News",
          'Title': [title],
          'Author': [author],
          'Date': [newsdate],
          'Content': [content],
          'Image' : [image],
          'Link' : [link]
          }

          df = pd.DataFrame(data)
          print(df)
          
          df.to_csv('data_kompas_news.csv', index=True)
          
          #SQLinsertion.insertData(news,tableName)  
              
      def onmedScrapingFinanceDetik(link):
          news = []
          try:
              resp = requests.get(link)
              
              # Check link respond
              if resp.status_code == 200:
                  soup = BeautifulSoup(resp.text, "html.parser")
                  
                  # News Source
                  source = "Finance Detik"

                  # Titile
                  title = soup.find("h1").get_text(strip=True)
                  
                  # Newsdate
                  newsdate = soup.find("div", class_="detail__date").get_text(strip=True)
                  #newsdate = timestampFunc.formattedNewsDetik(newsdate)

                  # Author
                  author = soup.find("div", class_="detail__author").get_text(strip=True)

                  # Content
                  content = soup.find("div", class_="detail__body-text itp_bodycontent")
                  if content:
                      content = content.text.strip()
                  else:
                      print("Content not found.")
                      
                  # Image
                  image = soup.find("img", class_="p_img_zoomin img-zoomin")
                  image_src = image['src'] if image else None

                
                  # News link
                  link = link
        
                  news.append(source)
                  news.append(title)
                  news.append(newsdate)
                  news.append(author)
                  news.append(content)
                  news.append(image_src)
                  news.append(link)
          
          except Exception as e:
                print(f"An error occurred in onmedScrapingDetik: {e}")
                pass
            
          #SQLinsertion.insertData(news,tableName)  
               
                            
      def onmedScraping20Detik(link):
          news = []
          try:
              resp = requests.get(link)
              
              # Check link respond
              if resp.status_code == 200:
                  soup = BeautifulSoup(resp.text, "html.parser")
                  
                  # News Source
                  source = "Detik News"
                  
                  # Titile
                  title = soup.find("h1").get_text(strip=True)
                  
                  # Newsdate
                  newsdate = soup.find("div", class_="detail__date mg-0").get_text(strip=True)
                  #newsdate = timestampFunc.formattedNewsDetik(newsdate)

                  # Author
                  author = soup.find("div", class_="color-gray-light-1 font-xs").get_text(strip=True)

                  # Content
                  content = soup.find("div", class_="detail__body-text")
                  if content:
                      content = content.text.strip()
                  else:
                      print("Content not found.")
                      
                  # Image
                  image = soup.find("img", class_="p_img_zoomin img-zoomin")
                  image_src = image['src'] if image else None

                
                  # News link
                  link = link
                  
                  news.append(source)
                  news.append(title)
                  news.append(newsdate)
                  news.append(author)
                  news.append(content)
                  news.append(image_src)
                  news.append(link)
                  
                  #SQLinsertion.insertData(news,tableName)
                  
          except Exception as e:
                print(f"An error occurred in onmedScrapingDetik: {e}")
                pass
            
          #SQLinsertion.insertData(news, tableName)
    
                                   
      def onmedScrapingDetik(link):
          news = []
          try:
              resp = requests.get(link)
              
              # Check link respond
              if resp.status_code == 200:
                  soup = BeautifulSoup(resp.text, "html.parser")

                  # News Source
                  source = "Detik News"

                  # Titile
                  title = soup.find("h1").get_text(strip=True)
                  
                  # Newsdate
                  newsdate = soup.find("div", class_="detail__date").get_text(strip=True)
                  #newsdate = timestampFunc.formattedNewsDetik(newsdate)

                  # Author
                  author = soup.find("div", class_="detail__author").get_text(strip=True)

                  # Content
                  content = soup.find("div", class_="detail__body-text itp_bodycontent")
                  if content:
                    content = content.text.strip()
                  else:
                      print("Content not found.")
                      
                  # Image
                  image = soup.find("img", class_="p_img_zoomin img-zoomin")
                  image_src = image['src'] if image else None

                      
                  # News link
                  link = link
                  
                  news.append(source)
                  news.append(title)
                  news.append(newsdate)
                  news.append(author)
                  news.append(content)
                  news.append(image_src)
                  news.append(link)
                  
                  #SQLinsertion.insertData(news,tableName)
                  
          except Exception as e:
                print(f"An error occurred in onmedScrapingDetik: {e}")
                pass
         
          #SQLinsertion.insertData(news,tableName)
          
                          
  if 'news.detik' in link:
    for item in soup.find_all('h3', attrs={'class' : 'media__title'}):
          #news = []
          link = (item.find('a', href=True)['href'])
          if '20.detik' in link:
              onmedScraping20Detik(link)
          else:
              onmedScrapingDetik(link)
       
  elif "finance.detik" in link:
    for item in soup.find_all('h3', attrs={'class' : 'media__title'}):
          #news = []
          link = (item.find('a', href=True)['href'])
          onmedScrapingFinanceDetik(link)
          
  else:
    for item in soup.find_all('h3', attrs={'class' : 'article__title article__title--medium'}):
          #news = []
          link = (item.find('a', href=True)['href'])
          onmedScrapingKompasNews(link)
          
## Insert empty data frame, then append scrape data into it
## news = []
                          
for link in link_list:
  onMedScrape(link)
  print(f"news {link} done")
