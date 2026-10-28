# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:44:14 2026

@author: hmosa
"""


print(30*'=')
Customer_Name=input('Customer Name:').strip().title()
Product_Name=input('Product Name:').strip().title()
Product_Code=int(input('Product Code:'))
Price=float(input('Product Price:'))
Order_Count=int(input('Order Count:'))
Total=Price*Order_Count
Discount=input('Discount Code:').upper()

Product_Information={'CName':Customer_Name,'Name':Product_Name,'Code':Product_Code,'Price':Price,'Order':Order_Count,'Total':Total}
Product_Information.items()
if Discount=='VIP':
    Product_Information['Total']=0.85*Product_Information['Total']

print(Product_Information.values())

Confirm=(input('Confirm Order?(yes/no)')).strip().upper()
if Confirm=='YES':
    print('Order Registered')