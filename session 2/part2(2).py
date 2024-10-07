

from datetime import date

# México Tlaxcala Government Manager App PART #3

howManyEnterprises = int(input("How many enterprises would you take place this process to: "))

if howManyEnterprises < 1:
    print("The Entetrepise(s) number must goes from 1 afterward") 
    quit()
else:
    for i in range(howManyEnterprises):
        enterpriseNumber = i + 1
        percent = 0
        tenPercent = .10
        twelvePercent = .12
        fourteenPercent = .14
        sixteenPercent = .16
        eighteenPercent = .18  
        twentyPercent = .20
        twentyTwoPercent = .22
        idEnterprise = input(f'Supply your Enterprise ID number { i + 1 }: ')
        nameEnterprise = input(f'Supply your Enterprise Name number { i + 1 }: ')
        employeesNumber = int(input(f'Supply your Enterprise Employees Number of your enterprise number { i + 1 }: '))
        if employeesNumber < 1:
            print("The employees number must goes from 1 to 12") 
            break
        howManyMonths = int(input(f'How many months would you take place this process for your enterprise number { i + 1 }?, the taxes declaration are from present month rearward, according to month(s) number chose: '))
        
        
        # ******************************* ***************************************  
    
        if howManyMonths > 12 or howManyMonths < 1:
            print("The declaration must be over 12 months")
            break
        else:
            today = date.today()
            actualMonth = int(format(today.month))
            calculateMonthNumber = 0
            monthName = ''
            calculatesManager = 0
            for i in range(howManyMonths):
                months = ['', 'january', 'february', 'march','april', 'may','june','july','august','september', 'october', 'november','december']
                calculateMonthNumber = actualMonth - i
                if calculateMonthNumber <= 0:
                    print("There's isn't more months of the actual year")
                    break
                else:
                    monthName = months[actualMonth - i] 
                    monthName
                    
                monthFacturedAmount = int(input(f'Provide the { monthName } month amount to to declare for your enterprise number { enterpriseNumber } with id - { idEnterprise }: '))
                howManyMonths = howManyMonths - 1
                if employeesNumber < 11:
                    if monthFacturedAmount < 1000:
                        percent = tenPercent
                        calculatesManager = (monthFacturedAmount * percent)
                    elif monthFacturedAmount > 1000 and monthFacturedAmount < 100001:
                        percent = twelvePercent
                        calculatesManager = (monthFacturedAmount * percent)
                    elif monthFacturedAmount > 100000 and monthFacturedAmount < 500001:
                        percent = fourteenPercent
                        calculatesManager = (monthFacturedAmount * percent)
                    elif monthFacturedAmount > 500001:
                        percent = sixteenPercent
                        calculatesManager = (monthFacturedAmount * percent)
                    
                        
                elif employeesNumber > 10 and employeesNumber < 31:
                    if monthFacturedAmount < 1000:
                        percent = twelvePercent
                        calculatesManager = (monthFacturedAmount * percent)
                    elif monthFacturedAmount > 1000 and monthFacturedAmount < 100001:
                        percent = fourteenPercent
                        calculatesManager = (monthFacturedAmount * percent)
                    elif monthFacturedAmount > 100000 and monthFacturedAmount < 500001:
                        percent = sixteenPercent
                        calculatesManager = (monthFacturedAmount * percent)
                    elif monthFacturedAmount > 500001:
                        percent = eighteenPercent
                        calculatesManager = (monthFacturedAmount * percent)
                        
                elif employeesNumber > 30 and employeesNumber < 51:
                    if monthFacturedAmount < 1000:
                        percent = fourteenPercent
                        calculatesManager = (monthFacturedAmount * percent)
                    elif monthFacturedAmount > 1000 and monthFacturedAmount < 100001:
                        percent = sixteenPercent
                        calculatesManager = (monthFacturedAmount * percent)
                    elif monthFacturedAmount > 100000 and monthFacturedAmount < 500001:
                        percent = eighteenPercent
                        calculatesManager = (monthFacturedAmount * percent)
                    elif monthFacturedAmount > 500001:
                        percent = twentyPercent
                        calculatesManager = (monthFacturedAmount * percent)
                else:
                    if monthFacturedAmount < 1000:
                        percent = sixteenPercent
                        calculatesManager = (monthFacturedAmount * percent)
                    elif monthFacturedAmount > 1000 and monthFacturedAmount < 100001:
                        percent = eighteenPercent
                        calculatesManager = (monthFacturedAmount * percent)
                    elif monthFacturedAmount > 100000 and monthFacturedAmount < 500001:
                        percent = twentyPercent
                        calculatesManager = (monthFacturedAmount * percent)
                    elif monthFacturedAmount > 500001:
                        percent = twentyTwoPercent
                        calculatesManager = (monthFacturedAmount * percent)
                result = float(calculatesManager)
                print(f'{ monthName.capitalize() } month bill amount to have being paid for { nameEnterprise } with id: { idEnterprise } according the payroll tax corresponding over { percent }%, is: ${ result }')
                