from win32com.client import DispatchEx
from win32com.client import Dispatch
from datetime import *
from time import *
import time


##New and old file Date assign
Newfile_date = (datetime.today() - timedelta(1)).strftime('%Y.%m.%d')
Newfile_date_formated = (datetime.today() - timedelta(1)).strftime('%m-%d-%Y')
##Assign file 
if datetime.today().strftime("%A") == 'Monday':
	Oldfile_date = (datetime.today() - timedelta(4)).strftime('%Y.%m.%d')
else:
	Oldfile_date = (datetime.today() - timedelta(2)).strftime('%Y.%m.%d')


Location_front = '//adcompdc.office.aol.com/Public/Reports/Video/MPS Video Campaigns/MPS Video Campaigns, '
Write_file_address = 'Z:/O+O_Analytics/Projects/Josh/Daily Report/New MPS ID/MPSFileMacro_updated.xlsm'
Save_file_address = 'Z:\O+O_Analytics\Projects\Josh\Daily Report\New MPS ID\MPS New Line\MPS New Line ' + Newfile_date_formated + '.xls'

##print Save_file_address

##New and Old file month to determine which tab to use
Old_file_month = time.strftime('%B',time.strptime(Oldfile_date,'%Y.%m.%d'))
Newfile_month  = time.strftime('%B',time.strptime(Newfile_date,'%Y.%m.%d'))

NewFile_address = Location_front + Newfile_date + '.xlsx'
OldFile_address = Location_front + Oldfile_date + '.xlsx'


print 'Oldfile date is:		' + Oldfile_date
print 'Newfile date is:		' + Newfile_date
print 'NewFile Month is:	 ' + Newfile_month
print 'OldFile Month is:	 ' + Old_file_month



excel = DispatchEx('Excel.Application')
wbG=excel.Workbooks.Open(OldFile_address)
wbP=excel.Workbooks.Open(Write_file_address)
excel.visible  = 0
# note altered sheet name; also .Select is not required

wbG.Worksheets(Old_file_month).Copy(Before=wbP.Worksheets('CombinedData'))
wbP.Worksheets(Old_file_month).Name = 'OLDDATA'

wbX=excel.Workbooks.Open(NewFile_address)
wbX.Worksheets(Newfile_month).Copy(Before=wbP.Worksheets('CombinedData'))
wbP.Worksheets(Newfile_month).Name = 'NEWDATA'
## no running out display alets
excel.DisplayAlerts = 0


excel.RUN('FindNewMPSlines_Macro')
excel.RUN('RemoveCompanion')

wbP.SaveAs(Save_file_address)
excel.Quit()
del excel # ensure Excel process ends

print 'MPS NewLine has been composed and saved in folder :  ' + Save_file_address