#Utilize formula for calculating the price of an explicit bond.
def getBondPrice_E(face, couponRate, yc):
    bond_price = 0
    coupon = face * couponRate
    
    # We use enumerate(yc, 1) to generate a changepoint 
    for t, rate in enumerate(yc, 1):
        if t == len(yc):
            cash_flow = coupon + face
        else:
            cash_flow = coupon
        bond_price += cash_flow / ((1 + rate) ** t)
        
    return round(bond_price)

