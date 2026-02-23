#Assume Standard Bond Price Calculation Given Payments Per Year 
def getBondPrice(y, face, couponRate, m, ppy=1):
    periodicYield = y / ppy
    periodicCoupon = (face * couponRate) / ppy
    totalPeriods = int(m * ppy)
    
    bondPrice = 0
    
    for t in range(1, totalPeriods + 1):
        bondPrice += periodicCoupon / ((1 + periodicYield) ** t)
        
    bondPrice += face / ((1 + periodicYield) ** totalPeriods)
    
    return round(bondPrice)
