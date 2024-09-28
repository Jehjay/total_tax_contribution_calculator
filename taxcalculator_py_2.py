import re

raw_salary_entry = raw_input("Enter the Zambian Kwacha monthly salary equivalent IN FULL: ")

if not type(raw_salary_entry) is str:
  raise TypeError("Your input is NOT valid, Please enter a Valid input - empty space, non-numeric characters or NO input are not valid")
  
else:
	# create a regular expression to handle the following cases:
	# check if the raw_salary_entry starts with non numeric character e.g. ZMW 3000 and remove it
	# check if raw_salary_entry ends with non numeric character e.g. 3000 Kwacha only and remove it
	# check if raw_salary_entry has a space e.g 30 000 and remove it
	# check if raw_salary_entry has a comma e.g 30,000 and remove it
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
			print("Tax payer's Gross monthly Salary is: ZMW " + str(gross_pay) + "\n")
			
			#NAPSA
			napsa_due = gross_pay * 0.05
			print("Tax payer's NAPSA monthly Contribution @ 5% is: ZMW " + str(napsa_due))
			
			#NHIMA
			nihma_due = gross_pay * 0.01
			print("Tax payer's NIHMA monthly Contribution @ 1% is: ZMW " + str(nihma_due))
			
			#TOTAL CONTRIBUTIONS
			total_contributions = napsa_due + nihma_due
			print("Tax payer's Total monthly Contributions are: ZMW " + str(total_contributions))

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
			print("Tax payer's Total monthly Tax Deductions: ZMW " + str(total_tax_deductions))

			#TOTAL TAX
			tax_due = total_contributions + total_tax_deductions
			print("Tax payer's monthly Taxes due are: ZMW " + str(tax_due) + "\n")

			#NET SALARY
			net_salary = gross_pay - tax_due
			print("Tax payer's monthly Net Salary is: ZMW " + str(net_salary) + "\n")

			return net_salary

		tax_payer(salary)
