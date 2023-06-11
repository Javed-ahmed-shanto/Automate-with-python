from openpyxl import load_workbook


wb = load_workbook('report.xlsx')
sheet = wb['Report']

sheet['A1'] = 'Sales_Report'
sheet['A2'] = 'January'
sheet['A1'].fomt = Font('Arial', bold=True, size=20)
sheet['A2'].font = Font('Arial', bold=True, size=10)

WB.SAVE('REPORT_JANUARY.xlsx')