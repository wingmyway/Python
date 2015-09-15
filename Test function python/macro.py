from win32com.client import Dispatch

def RunExcelMacro():
    myExcel = Dispatch('Excel.Application')
    myExcel.Visible = 1
    myExcel.Workbooks.Add('C:\Users\zhli14\Desktop\Daily Report\MTD files\loaded.xlsm')
    myExcel.Run('Prepare_MTD')
    myExcel.Run('Find_New_Lines_and_Check_Campaigns')
    myExcel.DisplayAlerts = 1
    myExcel.Save()
    myExcel.Quit()


RunExcelMacro()