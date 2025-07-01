#import 
import xlwings as xw

#value
BName = "BOOK.xlsx"
wb = xw.Book(BName)
sht = wb.sheets['sheet1']
A_pos = 'A'
pos = 0
ID = 10000
#loop
for i in range(2,2321):
    pos = A_pos + str(i)
    sht[pos].value = str(ID)
    ID += 1
    print(i)

a = input("wait")
wb.save(BName)
wb.close()
