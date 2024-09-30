# importing modules 
import re
import datetime
from tabulate import tabulate
from texttable import Texttable
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors

raw_salary_entry = input("Enter the Zambian Kwacha monthly salary equivalent IN FULL: ")

if not type(raw_salary_entry) is str:
  raise TypeError("Your input is NOT valid, Please enter a Valid input - empty space, non-numeric characters or NO input are not valid")
  
else:
	# create a regular expression to handle the following cases:
	# check if the raw_salary_entry starts with non numeric character and remove it e.g. ZMW 3000 -> 3000
	# check if raw_salary_entry ends with non numeric character and remove it e.g. 3000 Kwacha only -> 3000
	# check if raw_salary_entry has a space and remove it e.g 30 000 -> 30000
	# check if raw_salary_entry has a comma and remove it e.g 30,000 -> 30000
	# check if raw_salary_entry has a special character such as !;:? and remove it

	numeric_salary = re.sub("[^\d.]+", "", raw_salary_entry)

	#remove all characters after the last digit at the end e.g. 3000. and remove it
	numeric_salary = re.sub(r'(\d)\D+$', r'\1', numeric_salary)

	try:
		salary = float(numeric_salary)
	except ValueError:
		print("Your input is NOT valid")
	else:
		
		def tax_payer(salary):
			gross_pay = (salary)
			gross_pay = (round(salary,5))
			
			#NAPSA
			napsa_due = gross_pay * 0.05
			napsa_due = round(napsa_due,5)
					
			#NHIMA
			nihma_due = gross_pay * 0.01
			nihma_due = round(nihma_due, 5)
						
			#TOTAL CONTRIBUTIONS
			total_contributions = napsa_due + nihma_due
			total_contributions = round(total_contributions, 5)
			
			#GROSS PAY
			def tb1(gross_pay):
				chargeable_income = gross_pay
				tax_rate_1 = 0.00
				tax_band_1 = chargeable_income * tax_rate_1
				return tax_band_1

			def tb2(gross_pay):
				chargeable_income = 7100.00 - 5100.00
				tax_rate_2 = 0.20
				tax_band_2 = chargeable_income * tax_rate_2
				return tax_band_2

			def tb3(gross_pay):	
				chargeable_income = 9200.00 - 7100.00
				tax_rate_3 = 0.30
				tax_band_3 = chargeable_income * tax_rate_3
				return tax_band_3

			def tb4(gross_pay):
				chargeable_income = gross_pay - 9200.00
				tax_rate_4 = 0.37
				tax_band_4 = chargeable_income * tax_rate_4		
				return tax_band_4


			if (gross_pay<=5100.00):
				tb1(gross_pay)
			else:
				if (5100.01<gross_pay<=7100.00):
					tb2(gross_pay)
				elif (7100.01<gross_pay<=9200.00):
					tb3(gross_pay)
				elif (gross_pay>9200.01):
					tb4(gross_pay)
		
			#TOTAL DEDUCTIONS
			total_tax_deductions = tb1(gross_pay) + tb2(gross_pay) + tb3(gross_pay) + tb4(gross_pay)
			total_tax_deductions = round(total_tax_deductions, 5)
			
			#TOTAL TAX
			tax_due = total_contributions + total_tax_deductions
			tax_due = round(tax_due, 5)
			
			#NET SALARY
			net_salary = gross_pay - tax_due
			net_salary = round(net_salary, 5)
			

			# TIME STAMP
			# using datetime module
			
			# ct stores current time
			ct = datetime.datetime.now()

			# ts store timestamp of current time
			ts = ct.timestamp()


			# PRINT A TABLE FOR RESULTS
			data = [gross_pay, napsa_due, nihma_due, total_contributions, total_tax_deductions, tax_due, net_salary]
			t = Texttable()
			t.add_rows([["Gross monthly Salary", "NAPSA monthly Contribution @ 5%", "NIHMA monthly Contribution @ 1%", "Total monthly Contributions", "Total monthly Tax Deductions", "monthly Taxes due", "monthly Net Salary"], data])
			print("\n")
			print(t.draw())


			#GENERATE PDF
			# initializing variables with values 
			fileName = 'taxes.pdf'
			documentTitle = 'taxes'
			title = 'Total Monthly Tax Contributions'
			subTitle = 'Tax payer\'s monthly taxes due'
			textLines = [ 
				"Tax payer's Gross monthly Salary is: ZMW " + str(gross_pay),
				" " ,
				"Tax payer's NAPSA monthly Contribution @ 5% is: ZMW " + str(napsa_due),
				"Tax payer's NIHMA monthly Contribution @ 1% is: ZMW " + str(nihma_due),
				"Tax payer's Total monthly Contributions are: ZMW " + str(total_contributions),
				"Tax payer's Total monthly Tax Deductions: ZMW " + str(total_tax_deductions),
				"Tax payer's monthly Taxes due are: ZMW " + str(tax_due),
				" ",
				"Tax payer's monthly Net Salary is: ZMW " + str(net_salary),
				" ", " ", " ", " ", " ",
				"Current Time: " + str(ct),
				"Timestamp: " + str(ts)
			] 
			image = 'zra.png'

			# creating a pdf object 
			pdf = canvas.Canvas(fileName) 

			# setting the title of the document 
			pdf.setTitle(documentTitle) 

			# registering a external font in python 
			pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
			pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
			pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
			pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

			# creating the title by setting it's font 
			# and putting it on the canvas 
			pdf.setFont('Vera', 32) 
			pdf.drawCentredString(300, 570, title) 

			# creating the subtitle by setting it's font, 
			# colour and putting it on the canvas 
			pdf.setFillColorRGB(0, 0, 255) 
			pdf.setFont("Courier-Bold", 24) 
			pdf.drawCentredString(290, 520, subTitle) 

			# drawing a line 
			pdf.line(30, 510, 550, 510) 

			# creating a multiline text using 
			# textline and for loop 
			text = pdf.beginText(20, 400) 
			text.setFont("Courier", 15) 
			text.setFillColor(colors.black) 
			for line in textLines: 
				text.textLine(line) 
			pdf.drawText(text) 

			# drawing a image at the 
			# specified (x.y) position 
			pdf.drawInlineImage(image, 130, 640) 

			# saving the pdf 
			pdf.save()

			return net_salary
			
		tax_payer(salary)
