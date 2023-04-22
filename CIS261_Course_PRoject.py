# AlexCrider - CIS261 - Course Project Phase 1: Create and Call Functions with Parameters
#
#
### Create function GetEmpName that will input a value into variable empname and return the value
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

### This function shows how to enter a value that is numeric and return the value.
def GetHoursWorked():
    hours = float(input("Enter amount of hours worked:  "))
    return hours

### Create a function GetHourlyRate that will input a numeric value into variable hourlyrate and return the value
def GetHourlyRate():
    hourlyrate = int(input("Enter hourly rate: "))
    return hourlyrate


### Create a function GetTaxRate that will input a numeric value into variable taxrate and return the value
def GetTaxRate():
    taxrate = int(input("Enter tax rate: "))
    return taxrate


def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    ## complete the code to calculate grosspay, incometax, and net pay
    
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours:,.2f}")
    ## complete the code to display hourlyrate, grosspay, taxrate, incometax, and netpay with appropriate labels and formatting

    print()

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    ## complete the code to display TotGrossPay, TotTax, and TotNetPay with appropriate lables and formatting


if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        ## call the function GetEmpName and assign the return value to empname
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        ## call the function GetHoursWorked and assign the return value to hours
        hours = GetHoursWorked()
        if (hours.upper() == "END"):
            break
        
        ## call the function GetHourlyRate and assign the return value to hourlyrate
        hourlyrate = GetHourlyRate()
        if (hourlyrate.upper() = "END"):
            break

        ## call the function GetTaxRate and assign the return value to taxrate
        taxrate = GetTaxRate()
        if (taxrate.upper() == "END"):
            break
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)

        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
    ## call the function PrintTotals and pass in  TotEmployees, TotHours, TotGrossPay, TotTax, and TotNetPay
    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
