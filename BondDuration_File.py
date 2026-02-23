def getBondDuration(y, face, couponRate, m, ppy=1):
    periods = m * ppy
    period_yield = y / ppy
    coupon = face * couponRate / ppy
    price = 0
    weighted_sum = 0
    
    for t in range(1, periods + 1):
        if t == periods:
            cash_flow = coupon + face
        else:
            cash_flow = coupon
        
        discount_factor = (1 + period_yield) ** t
        pv = cash_flow / discount_factor
        
        price += pv
        weighted_sum += t * pv
    
    macaulay_duration = weighted_sum / price
    
    # Return Duration in years
    return macaulay_duration / ppy
