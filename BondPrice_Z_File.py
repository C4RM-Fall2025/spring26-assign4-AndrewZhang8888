#We assume that this is to calculate the Price of a Bond Given the zero spot yield
def getBondPrice_Z(face, couponRate, times, yc):
    price = 0
    coupon = face * couponRate
    for i in range(len(times)):
        price += coupon / ((1 + yc[i]) ** times[i])
    price += face / ((1 + yc[-1]) ** times[-1])
    return price
