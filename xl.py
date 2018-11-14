import xlsxwriter as xl

workbook = xl.Workbook('a.xlsx')
worksheet = xl.add_worksheet()

f = open('all.txt')

for i in f:
    print(i)
