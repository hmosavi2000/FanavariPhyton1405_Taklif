# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:58:54 2026

@author: hamed mousavi
"""
#capitalize()
name='hamed'
new_name=name.capitalize()
print(new_name) #Hamed
#این تابع اول کلمه بزرگ می کند
#=========================================
#Converts 
name='hamed'
new_name=name.Converts()*******
print(new_name) 
#=========================================
#casefold 
name='HAMED'
new_name=name.casefold()
print(new_name) #hamed
# این تابع همه حروف کوچک می کند

#=========================================
#center() 
name='HAMED'
new_name=name.center(20)
print(new_name) #       HAMED        
#کلمه بین 20 space وسط قرار داده می شود
#=========================================
#count() 
name='be name khoda be'
new_name=name.count('be')
print(new_name) #2
# تعداد تکرار رشته داده شده 
#=========================================
#count() 
name='hamed'
new_name=name.encode()******
print(new_name) #b'hamed'

#=========================================
#endswith() 
name='hamed'
new_name=name.endswith('d')
print(new_name) #True
# اگر با حرف داده شده پایان شده باشد true یا false پاسخ میده

#=========================================
#count() 
name='ham\ted mou\tsavi'
new_name=name.expandtabs()
print(new_name) #ham     ed mou  savi
	#به جای \t تب می زند
#=========================================
#find() 
name='hamed mousavi'
new_name=name.find('mo',0)
print(new_name) #6
# ایندکس مکان حرف داده شده بر می گرداند

#=========================================
#format() 
name='hamed mousavi {tedad}'
new_name=name.format(tedad=5)
print(new_name) #hamed mousavi 5
#روش جاگذاری

#=========================================
#format() 
m={'sal':'1345','mah':'mordad'}
name='hamed mousavi {sal} {mah}'
new_name=name.format_map(m)	
print(new_name) #hamed mousavi 1345 mordad
# جا گذاری از لیست

#=========================================
#index()
name='hamed mousavi'
new_name=name.index('o',1)
print(new_name) #7
# ایندکس مکان حرف داده شده بر می گرداند

#=========================================
#isalnum()
name='hamed mousavi'
new_name=name.isalnum()
print(new_name) #False
name='1234'
new_name=name.isalnum()
print(new_name) #True
name='1hamed 123'
new_name=name.isalnum()
print(new_name) #False
#چک می کنه آیا همه متن عدد هست یا خیر

#=========================================
#isalpha()
name='hamedmousavi'
new_name=name.isalpha()
print(new_name) #True
name='1234'
new_name=name.isalpha()
print(new_name) #False
name='hamed 123'
new_name=name.isalpha()
print(new_name) #False
# چک می کنه آیا همه رشته حرف هست یا خیر اگه فاصله هم باشه False میزنه
#=========================================
#isascii()
name='hamedmousavi'
new_name=name.isascii()
print(new_name) #True
name='1234'
new_name=name.isascii()
print(new_name) #True
name='hamed 123'
new_name=name.isascii()
print(new_name) #True
#چک می کنه آیا حروف جزو ascii هست یا خیر
#=========================================
#isdecimal()
name='hamedmousavi'
new_name=name.isdecimal()
print(new_name) #False
name='1234.5'
new_name=name.isdecimal()
print(new_name) #True
name='hamed 123'
new_name=name.isdecimal()
print(new_name) #False
name='1.5'
new_name=name.isdecimal()
print(new_name) #False
#چک میکنه آیا عدد هست یا خیر حتی اگه ممیز باشه قبول می کنه
#=========================================
#isdigit()
name='hamedmousavi'
new_name=name.isdigit()
print(new_name) #False
name='1234'
new_name=name.isdigit()
print(new_name) #True
name='hamed 123'
new_name=name.isdigit()
print(new_name) #False
name='1.5'
new_name=name.isdigit()
print(new_name) #False
#چک میکنه آیا عدد هست یا خیر ممیز قبول نمی کنه
#=========================================
#isidentifier()
name='hamedmousavi'
new_name=name.isidentifier()*******
print(new_name) #True
name='1234'
new_name=name.isidentifier()
print(new_name) #False
name='hamed 123'
new_name=name.isidentifier()
print(new_name) #False
name='1.5'
new_name=name.isidentifier()
print(new_name) #False
#=========================================
#islower()
name='hamedmousavi'
new_name=name.islower()
print(new_name) #True
name='Hamed'
new_name=name.islower()
print(new_name) #False
name='HAMED'
new_name=name.islower()
print(new_name) #False
# چک می کنه آیا همه کاراکترها کوچک هستن یا خیر
#=========================================
#isnumeric()
name='hamedmousavi'
new_name=name.isnumeric()
print(new_name) #False
name='1234'
new_name=name.isnumeric()
print(new_name) #True
name='hamed 123'
new_name=name.isnumeric()
print(new_name) #False
name='1.5'
new_name=name.isnumeric()
print(new_name) #False
#چک میکنه آیا عدد هست یا خیر ممیز قبول نمی کنه

#=========================================
#isprintable()
name='hamedmousavi'
new_name=name.isprintable()*******
print(new_name) #True
name='1234'
new_name=name.isprintable()
print(new_name) #True
name='hamed 123'
new_name=name.isprintable()
print(new_name) #True
name='1.5'
new_name=name.isprintable()
print(new_name) #True


#=========================================
#isspace()
name='hamedmousavi'
new_name=name.isspace()
print(new_name) #False
name='   '
new_name=name.isspace()
print(new_name) #True
name='hamed 123'
new_name=name.isspace()
print(new_name) #False
# چک می کنه آیا همه رشته فاصله هستن یا خیر
#=========================================
#istitle()
name='hamed Mousavi'
new_name=name.istitle()
print(new_name) #False
name='Hamed Mousavi'
new_name=name.istitle()
print(new_name) #True
name='hamed 123'
new_name=name.istitle()
print(new_name) #False
# چک می کنه اول هر رشته بزرگ هست یا خیر
#=========================================
#isupper()
name='hamed Mousavi'
new_name=name.isupper()
print(new_name) #False
name='Hamed Mousavi'
new_name=name.isupper()
print(new_name) #False
name='HAMED'
new_name=name.isupper()
print(new_name) #True
#چک می کنه آیا همه حروف بزرگ هست یا خیر
#=========================================
#join()
name=('hamed',' Mousavi','Baladeh')
new_name='-'.join(name)
print(new_name) #hamed- Mousavi-Baladeh
#رشته های داخل لیست با نشانه تعریف شده به هم می چسباند
#=========================================
#ljust()
name='hamed Mousavi'
new_name=name.ljust(20)
print(new_name,'baladeh') #hamed Mousavi        baladeh
#به تعداد تعریف شده فاصله ایجاد می کنه
#=========================================
#lower()
name='Hamed Mousavi'
new_name=name.lower()
print(new_name) #hamed mousavi
# همه حروف کوچک می شوند
#=========================================
#lstrip()
name='   Hamed Mousavi   '
new_name=name.lstrip()
print(new_name) #Hamed Mousavi  
# فضای خالی چپ حذف میشه

#=========================================
#partition()
name='   Hamed Mousavi  baladeh '
new_name=name.partition('baladeh')
print(new_name) #('   Hamed Mousavi  ', 'baladeh', ' ') 
#متن را بر اساس رشته تعریف شده جداسازی می کنه
#=========================================
#replace()
name='   Hamed Mousavi   '
new_name=name.replace('H','o')
print(new_name) # oamed Mousavi    
# کاراکتر جدید و قدیم با هم عوض می کند

#=========================================
#rfind()
name='   Hamed Mousavi   '
new_name=name.rfind('d',0)
print(new_name) #7
# ایندکس جای حرف نمایش میده  
#=========================================
#rindex()
name='   Hamed Mousavi   '
new_name=name.rindex('a',0)
print(new_name) #13
# آخرین ایندکس در رشته بر می گزدانذ

#=========================================
#rsplit()
name='   Hamed/ Mousavi   '
new_name=name.rsplit('/')
print(new_name) #['   Hamed', ' Mousavi   ']
# بر اساس جدا کننده داده شده رشته تقسیم می شود

#=========================================
#rstrip()
name='   Hamed Mousavi   '
new_name=name.rstrip()
print(new_name) #   Hamed Mousavi
#فضای خالی سمت راست حذف می شه

#=========================================
#split()
name='   Hamed/ Mou/savi   '
new_name=name.split('/')
print(new_name) #['   Hamed', ' Mou', 'savi   ']
# بر اساس جدا کننده داده شده رشته تقسیم می شود

#=========================================
#splitlines()
name='   Hamed/ Mou\nsavi   '
new_name=name.splitlines('/')
print(new_name) #['   Hamed/ Mou\n', 'savi   ']
# بر اساس نشانه خط تقسیم می کنه

#=========================================
#startswith()
name='   Hamed Mousavi   '
new_name=name.startswith('H')
print(new_name) #False

name='Hamed Mousavi   '
new_name=name.startswith('H')
print(new_name) #True
# اگر با کلمه داده شده شروع شده باشه True False میده
#=========================================
#strip()
name='   Hamed Mousavi   '
new_name=name.strip()
print(new_name) #Hamed Mousavi
#فاصله اول و آخر حذف میشه

#=========================================
#swapcase()
name='   Hamed Mousavi   '
new_name=name.swapcase()
print(new_name) #hAMED mOUSAVI  
#حروف کوچک بزرگ و حروف بزرگ کوچک میشه

#=========================================
#title()
name='hamed mousavi'
new_name=name.title()
print(new_name) #Hamed Mousavi 
#اول هر کلمه بزرگ میشه

#=========================================
#translate()
name='hamed mousavi'
new_name=name.translate()
print(new_name) #Hamed Mousavi 

#=========================================
#upper()
name='hamed mousavi'
new_name=name.upper()
print(new_name) #HAMED MOUSAVI
#همه حروف بزرگ میشن
#=========================================
#zfill()
name='hamed mousavi'
new_name=name.zfill()
print(new_name) #HAMED MOUSAVI



