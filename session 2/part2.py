

# México Tlaxcala Government Manager App PART #3

howManyEnterprises = int(input("How many enterprises would you take place this process to: "))

if howManyEnterprises < 1:
    print("The Entetrepise(s) number must goes from 1 afterward") 
    quit()
else:
    for i in range(howManyEnterprises):
        months = [ 'january', 'jebruary', 'march','april', 'may','june','july','august','september', 'october', 'november','december']
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
        calculatesManager = 0
        if employeesNumber < 1:
            print("The employees number must goes from 1 to 12") 
            break
        
        else: 
         
            howManyMonths = int(input(f'How many months would you take place this process for your enterprise number { i + 1 }: '))
            if howManyMonths > 12 or howManyMonths < 1:
                print("The months must goes from 1 to 12") 
                break
                
            else:
                for i in range(howManyMonths):
                    monthFacturedAmount = int(input(f'Provide the month amount over which one the calculates will be done for your enterprise number { i + 1 }, left you { howManyMonths } month(s) to indicate: '))
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
                    print(f'This month bill amount to have being paid for { nameEnterprise } with id: { idEnterprise } according the payroll tax corresponding over { percent }%, is: ${ result }')
                
