from calendar import prcal
def printyear():
	while True:
		try:
			year = int(input("\nEnter the year(1..9999) : "))
			if year>9999 or year<1:
				print("year is out of range!!")
				raise Exception("Error!")
			else:
				break
		except:
			print("Please enter a valid value within 1 to 9999!!")
	print("\n")
	print("="*20,"<<< PRINTING CALENDAR>>>","="*20,"\n")
	prcal(year)
import time
print("\n","="*20,"<<CALENDAR>>","="*20,"\n")
printyear()
while True:
	try:
		print("\n","-"*20,"<<CHECKPOINT>>","-"*20,"\n")
		check = int(input("Enter 0 to exit and 1 to run again :"))
		if check == 0:
			print("\n","-"*20,"<<EXIT>>","-"*20,"\n")
			time.sleep(3)
			break
		elif check == 1:
			print("\n","-"*20,"<<STARTING AGAIN>>","-"*20,"\n")
			printyear()
		else:
			raise Exception("Error!")
	except:
		print("Please enter a valid value 0 or 1!!")
		