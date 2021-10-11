from bs4 import BeautifulSoup
import sqlite3
import requests as req

import re;

def search():
    txt = input("Введите : ")
    txt1 = txt.capitalize()
    flag=0
    with con:    
        cur = con.cursor()    
        cur.execute("SELECT * FROM coinmarket")
        while True:
            row = cur.fetchone()
        
            if row == None:
                break
             
            if re.search(txt1, row[1].capitalize()):
                print(row)
                flag=1 
    if flag==0:
        print("Ничего не найдено")



db = sqlite3.connect("coinmarket.db")
resp = req.get("https://coinmarketcap.com")
soup = BeautifulSoup(resp.text, 'lxml')
i=0
list1=[]
type(list1)
for tag in soup.find_all('td'):
    
    
    if i%11==4:
        i=i+1
        continue
    if i%11==5:
        i=i+1
        continue
    if i%11==0:
        i=i+1
        continue
    if i%11<7:
        list1.append(format(tag.text))
    
    i=i+1
    if i>108:
        break
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS coinmarket(
    id INT,
    name TEXT,
    marketcap text,
    price text
)""")

db.commit()

   
j=0
for i in range(0,10):
    if j%4==0:
        coinmarket_id=list1[j]
        j=j+1
    if j%4==1:
        coinmarket_name=list1[j]
        j=j+1
    if j%4==2:
        coinmarket_marketcap=list1[j]
        j=j+1
    if j%4==3:
        coinmarket_price=list1[j]
        j=j+1
    sql.execute("INSERT INTO coinmarket VALUES (?,?,?,?)",(coinmarket_id, coinmarket_name, coinmarket_marketcap, coinmarket_price))
    db.commit()
    i=i+1

con = sqlite3.connect('coinmarket.db')
 
with con:    
    cur = con.cursor()    
    cur.execute("SELECT * FROM coinmarket")
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
            
        print (row[0],")", row[1],"\n\t",row[2],"\t", row[3])
search()
sql.execute("DROP TABLE coinmarket")