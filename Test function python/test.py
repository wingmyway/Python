import xlrd
import xlwt
from win32com.client import Dispatch
from datetime import *
from time import *
from xlutils.copy import copy
import time
import xlsxwriter

##New and old file Date assign
Newfile_date = (datetime.today() - timedelta(1)).strftime('%Y.%m.%d')
##Assign file 
if datetime.today().strftime("%A") == 'Monday':
	Oldfile_date = (datetime.today() - timedelta(4)).strftime('%Y.%m.%d')
else:
	Oldfile_date = (datetime.today() - timedelta(2)).strftime('%Y.%m.%d')


Location_front = '//adcompdc.office.aol.com/Public/Reports/Video/MPS Video Campaigns/MPS Video Campaigns, '
Write_file_address = 'C:/Users/zhli14/Desktop/Daily Report/New MPS ID/MPSFileMacro_updated.xlsm'
Save_file_address = 'C:/Users/zhli14/Desktop/Daily Report/New MPS ID/MPSFile/' + Newfile_date + '.xlsx'

print Save_file_address

##New and Old file month to determine which tab to use
Old_file_month = time.strftime('%B',time.strptime(Oldfile_date,'%Y.%m.%d'))
Newfile_month  = time.strftime('%B',time.strptime(Newfile_date,'%Y.%m.%d'))

NewFile_address = Location_front + Newfile_date + '.xlsx'
OldFile_address = Location_front + Oldfile_date + '.xlsx'




Old_input = xlrd.open_workbook(OldFile_address)
Old_sheet = Old_input.sheet_by_name(Old_file_month)

New_input = xlrd.open_workbook(NewFile_address)
New_sheet = New_input.sheet_by_name(Newfile_month)


## Another try
rb = xlrd.open_workbook(Write_file_address)
##rs = rb.sheet_by_index(0)

workbook = copy(rb)

sheet_old = workbook.add_sheet('OLDDATA')

for j in range(Old_sheet.nrows):
	data = [Old_sheet.cell_value(j, col) for col in range(Old_sheet.ncols)]
	for index, value in enumerate(data):
		sheet_old.write(j, index, value)

workbook.save('C:\Users\zhli14\Desktop\Result.xls')

##


'''
workbook = xlwt.Workbook()

sheet_old = workbook.add_sheet('OLDDATA')
for j in range(Old_sheet.nrows):
	data = [Old_sheet.cell_value(j, col) for col in range(Old_sheet.ncols)]
	for index, value in enumerate(data):
		sheet_old.write(j, index, value)

sheet_new = workbook.add_sheet('NEWDATA')
for j in range(New_sheet.nrows):
	data = [New_sheet.cell_value(j, col) for col in range(New_sheet.ncols)]
	for index, value in enumerate(data):
		sheet_new.write(j, index, value)


workbook.save('C:\Users\zhli14\Desktop\Result.xlsm')
'''


#sheet_old = xlwt.Worksheet('OLDDATA',Write_file_address,cell_overwrite_ok=True)
#sheet_old.write(1,1,label= 'hello')

#sheet_new = xlwt.Worksheet('NEWDATA',Write_file_address,cell_overwrite_ok=True)
#MPSNewLine = xlwt.Workbook(Write_file_address)
#sheet_old = MPSNewLine.Worksheet('OLDDATA')
#sheet_new = MPSNewLine.sheet_by_name('NEWDATA')


#sheet_old.write(1,2,1)
#for i in range (Old_sheet.nrows):
#	for j in range(Old_sheet.ncols):
		#sheet_old.write(i,j,Old_sheet.cell_value(i,j))








