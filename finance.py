#Program for Personal Finance
# Gives: Income Sheet, CashFlow sheet, Balance Sheet

#Income Sheet

streamsofincome= dict()

def getincomestreaminfo():
    job = input("What Job: " ).capitalize()

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

## Salary
    if typeofpay == "SALARY":
        salary= input("Whats the Gross Salary ? ")
        while salary.isdigit() == False:
            print("Opps that was NOT a number please try again :) ")
            salary= input("Whats the Gross Salary ? ")
        else:
            salary= int(salary)
            trueincome=netincome(salary,tax)

## Commission
    if typeofpay == "COMMISSION":
        commission = input("Whats the Year to Date Commission ? ")
        trueincome=netincome(commission,tax)
## Hourly
    if typeofpay == "HOURLY":
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
        trueincome=netincome(income,tax)

    streamsofincome[job]= trueincome
##  Another Stream ?
    anotherstream= input("Do you have another stream of income ?").upper()
    if anotherstream == "Y":
        getincomestreaminfo()
    else:
        displayincomeinfo(streamsofincome)


# FIX : turn income to string and show dollar sign
def netincome(income,taxrate):
    taxrate= taxrate/100
    trueincome= income - (income*taxrate)

    trueincome= "$ " + str(trueincome)

    return trueincome

# fix on jobs every value is a string convert it to integer here
def displayincomeinfo(jobs):
    for i in jobs:
        print(i.capitalize() + ': '+jobs[i])
    totalincome= list(jobs.values())
    totalincome = [float(i.strip('$')) for i in totalincome]
    totalincome= sum(totalincome)
    totalincome = '$' + str(totalincome)
    print("Total Income: " + totalincome)

def main():
    getincomestreaminfo()


main()

#Balance Sheet


#CashFlow
