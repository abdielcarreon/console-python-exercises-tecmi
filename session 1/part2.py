

# TOY STORE PART 2

months = [ 'January', 'February', 'March','April', 'May','June','July','August','September', 'October', 'November','December']
priceByDolls = 150
priceByCar = 160
priceBySpinningTop = 200
dollsResult = 0
carsResult = 0
spinningTopResult = 0
totalByMonth = 0
total = 0
for month in months:
    print(f'------ { month } ------')
    dollsResult = int(input(f"How many cars in the { month } month?: ")) * priceByDolls
    carsResult = int(input(f"How many dolls in the { month } month?: ")) * priceByCar
    spinningTopResult = int(input(f"How many spinning tops in the { month } month?: ")) * priceBySpinningTop
    totalByMonth = dollsResult + carsResult + spinningTopResult
    total += dollsResult + carsResult + spinningTopResult
    print(f"*** The total in the { month } month is: { totalByMonth } ***\n")
    

total
print(f"The bill total to pay is: ${ total } (from part2)")