#Write a program that emulates a housing loan eligibility and DSR calculator 

#YAP JIA CONG  
#276882

#input

import os # Clearing the Screen
os.system('cls') # Clearing the Screen

print("*******WELCOME TO THE HOUSING LOAN AND DSR CALCULATOR*******")

#setting up the user_password
#start=1
#end=3
#selection=1 or 2
useravailable="YJC"
userpassword = 1234

print("Choose login or Signup?:")
print("1-Login,2-Sign up")
print()
input_selection=input("What is your choice? :")
input_selection_type=int(input_selection)

#For Login
if (input_selection_type==1):
	print("******Welcome to Login System******")

	for i in range (3):
		userid=str(input("Please enter your userid:")).upper()
		userpin=int(input("Please enter your password:"))

		if userid==useravailable and userpin==userpassword:
			print("Congrats,You have sucessfully log in")
			break

		else:
			print("The userpin or userid is incorrect,Please try again")
		
	else:
		print("Your account is locked out")
		quit()

#For Registration
if (input_selection_type==2):
	print("******Welcome to Register System******")
	userID=input("Please create your userID:")
	userID_type=str(userID)

	userID_character=6
	userID_true_input=len(userID_type)

	i=1
	limit_attempt=5
	while (i<=limit_attempt):

		if (((" ") in userID_type) or len(userID_type)!=5):
			attempt_statement="no of attempt is {}"
			print(attempt_statement.format(i))
			print("Please remove blank space in the userid and must be in 5 character")
			userID=input("Please recreate your userID:")
			userID_type=str(userID)
			i+=1

			if i==limit_attempt:
				print("Failed to login after 5 attempt")
				quit()

		else:
			password=input("Please Create a password:")
			password_type=str(password)
			if userID_type in password_type:
				print("The password should not contains the username")
			elif len(password_type)!=4:
				print("Please try agains, the password must be in 4 character")
			else:
				print("Congrats,You have sucessfully registered!")
				break

#If Login or Resgister
if((input_selection_type !=2)) and (input_selection_type !=1):
	print("Please choose 1 or 2, Thank You")
	quit()

def calculate_total_amount_payable(monthly_payment, total_payments):
    # Calculate the total amount payable over the term of the loan
    total_amount_payable = monthly_payment * total_payments
    return total_amount_payable


def calculate_housing_loan_eligibility(income, age, credit_score):
    # Simplified eligibility criteria
    if age < 21 or age > 60:
        return 0  # Applicant outside typical working age range
    
    if credit_score < 650:
        return 0  # Low credit score
    
    # Calculate eligibility based on income (you may need to adjust this based on actual lending criteria)
    eligibility = income * 0.5  # Example: Eligibility is 50% of monthly income
    
    return eligibility


def calculate_dsr(gross_income, housing_expenses, other_debts):
    # Calculate Debt-Service Ratio (DSR)
    total_monthly_debts = housing_expenses + other_debts
    dsr = (total_monthly_debts / gross_income) * 100
    
    return dsr



print()


print("******PERSONAL DETAILS******")
input_name=str(input("Please provide your name :"))
print("")
print("Hello," + " " + input_name)

while True:
 input_age=int(input("What is your age:"))
 input_credit_score = int(input("Enter your credit score: "))
 input_basic_salary=float(input("How much your basic salary: RM"))
 input_fix_allowance=float(input("How much your fix allowance: RM"))
 input_principal_amount = float(input("Enter the principal loan amount: RM"))
 input_EPF=float(input("How muvh your EPF : RM"))
 input_SOCSO= float(input("How much your SOCSO : RM"))
 input_TAX=float(input("How much yout tax: RM"))
 input_monthly_commitment=float(input("How much your monthly commmitment: RM"))
 input_expenses=float(input("How much is your expenses : RM"))
 input_year=int(input("How many Year?"))
 input_interest=float(input("How much will you pay in Interest?"))


#condition
 gross_income = input_basic_salary + input_fix_allowance
 total_deduction = input_EPF + input_SOCSO + input_TAX
 Net_Income = gross_income - total_deduction
 DSR = (input_monthly_commitment/Net_Income) * 100

 print("")
 status=""

 print("Results:")
# Calculate monthly interest rate and total number of payments
 monthly_interest_rate = (input_interest / 100) / 12
 total_payments = input_year * 12

# Calculate monthly mortgage payment using the formula for a fixed-rate mortgage
 monthly_payment = (input_principal_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-total_payments))
 print(f"\nYour monthly installment: RM{monthly_payment:.2f}")

# Calculate total amount payable over the term of the loan
 total_amount_payable = calculate_total_amount_payable(monthly_payment, input_year * 12)
 print(f"Total amount payable over the term of the loan: RM{total_amount_payable:.2f}")

# Calculate Housing Loan Eligibility
 eligibility = calculate_housing_loan_eligibility(input_basic_salary, input_age, input_credit_score)
 print(f"\nYour housing loan eligibility: {eligibility:.2f}")

# Calculate Debt-Service Ratio (DSR)
 dsr = calculate_dsr(input_basic_salary, input_expenses, total_deduction)
 print("Your DSR is",DSR)
 print(f"Your Debt-Service Ratio (DSR): {dsr:.2f}%")

# Basic eligibility check
 if eligibility > 0 and dsr <= 50:
    print("Congratulations! You may be eligible for a housing loan.")
 else:
    print("Sorry, you may not meet the eligibility criteria for a housing loan.")

 user_input = input("Do you want to calculate again? (yes/no): ").lower()
 if user_input != 'yes':
        print("Thank you for using our HOUSING LOAN AND DSR CALCULATOR, Goodbye!" )
        break # Exit the loop if the user does not want to calculate again
    
    
