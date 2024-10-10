from bs4 import BeautifulSoup
import psycopg2
import time
from datetime import datetime



def insertData(news, tableName):
   conn = psycopg2.connect(
      database="postgres",
      user="admin",
      password="P@ssw0rd",
      host="192.168.90.12",
      port="5432"
   )
   
   cur = conn.cursor()
   
   # Konversi string menjadi objek datetime
   #news_date = datetime.strptime(news[2], "%Y-%m-%d %H:%M:%S")
   
   # Mengonversi nilai BeautifulSoup Tag menjadi string
   news_content_str = str(news[4])

   # Konversi nilai news[2] (newsdate) menjadi string sesuai dengan format yang diinginkan
   # news_date_str = onMedScrape_new.news[2].strftime("%Y-%m-%d %H:%M:%S")

   insertSql = """
               INSERT INTO public.newsonmed (onmed_source, title, newsdate, author, newscontent, newsimage, newslink)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
               """
 # %s, %s, %s, %s, %s, %s, %s, %s
 # '{news[0]}', '{news[0]}', '{news[0]}', '{news[0]}', '{news[0]}', '{news[0]}'
 #(insertSql, (news[0], news[1], news[2], news[3], news[4], news[5], news[6]))
 # (insertSql, (news["source"], news["title"], news["newsdate"], news["author"], news["content"], news["image_src"], news["link"]))
 # (insertSql, (news[0], news[1], news[2], news[3], news_content_str, news[5], news[6])) 
 
   cur.execute(insertSql, (news["source"], news["title"], news["newsdate"], news["author"], news["content"], news["image_src"], news["link"]))
   conn.commit()
   cur.close() 
   conn.close()
z