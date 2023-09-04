#Program for Personal Finance
# Gives: Income Sheet, CashFlow sheet, Balance Sheet

#Income Sheet

streamsofincome= dict()

def getincomestreaminfo():
    job = input("What Job: " )

#   TAX

    tax= input("What is your tax withholding rate ? ")

    while tax.isdigit() == False:
        print("That was not a number try again :)")
        tax= (input("What is your tax withholding rate ? "))
    else:
        tax=int(tax)
        print(type(tax))

##  Type of Pay

    typeofpay=input("Is it Salary or Hourly ? ").upper()
    if typeofpay == "SALARY":
        salary= input("Whats the Gross Salary ? ")
        while salary.isdigit() == False:
            print("Opps that was NOT a number please try again :) ")
            salary= input("Whats the Gross Salary ? ")
        else:
            salary= int(salary)
            netincome(salary,tax)

    if typeofpay == "COMMISSION":
        commission = input("Whats the Year to Date Commission ? ")
        netincome(commission,tax)
    else:
        hourly=input("Whats the Hourly Rate ? ")
        while hourly.isdigit() == False:
            print("opps not a number try again")
            hourly=input("Whats the Hourly Rate ? ")
        else:
            hourly = int(hourly)

        monthhours=input("What are your Total Monthly Hours ?")
        while monthhours.isdigit() == False:
            print("opps not a number try again")
            monthhours=input("What are your Total Monthly Hours ?")
        else:
            monthhours = int(monthhours)

        income= hourly*monthhours
        netincome(income,tax)


##  Another Stream ?
    anotherstream= input("Do you have another stream of income ?").upper()
    if anotherstream == "Y":
        getincomestreaminfo()
    else:
        displayincomeinfo(streamsofincome)


# FIX TAXRATE TURN TO PERCENTAGE EXAMPLE 10 TO 0.10
def netincome(income,taxrate):
    print(income,taxrate)
    trueincome= income - (income*taxrate)
    print(trueincome)

def displayincomeinfo(jobs):
    print(jobs)


def main():
    getincomestreaminfo()


main()

#Balance Sheet


#CashFlow
