#We assume that this is to calculate the Price of a Zero Coupon Bond Given a Yield Curve
def getBondPrice_Z(face, couponRate, times, yc):
    rate = yc[times - 1]
    final_payment = face * (1 + couponRate)
    return final_payment / ((1 + rate) ** times)
