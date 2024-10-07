

from datetime import date


def calculateMonths(numberMonths):
    
    months = ['', 'january', 'february', 'march','april', 'may','june','july','august','september', 'october', 'november','december']
    if numberMonths > 12 or numberMonths < 1:
        print("The declaration must be over 12 months")
        quit()
    else:
        today = date.today()
        actualMonth = int(format(today.month))
        calculateMonthNumber = 0
        calculateMonthName = ''
        for i in range(numberMonths):
            calculateMonthNumber = actualMonth - i
            if calculateMonthNumber <= 0:
                print("There's isn't more months of the actual year")
                quit()
                
            calculateMonthName = months[actualMonth - i] 
            print(calculateMonthNumber, calculateMonthName)  
            
        
calculateMonths(10)