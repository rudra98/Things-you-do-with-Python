
# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = ("Access_excel.xls") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
sheet.cell_value(0, 0)


print('First column: ')
for i in range(sheet.nrows): 
    print(sheet.cell_value(i, 0))  

print('First row: ')    
for i in range(sheet.ncols): 
    print(sheet.cell_value(0, i))
    
print('A particular row: ', sheet.row_values(1))
print('A particular column: ', sheet.col_values(0))

print('Single value: ', sheet.cell_value(1,1))    
