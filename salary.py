basic = float(input('Enter the basic salary: '))
da = 0.75 * basic
hra = 0.2 * basic

if basic < 10000:
	gross = basic + da
elif basic < 20000:
	gross = basic + da + 0.2 * hra
else:
	gross = basic + da + hra
	
print('Gross Salary is:', gross)
