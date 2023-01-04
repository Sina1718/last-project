class hoghoogh():
    
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate
payment = hoghoogh(int(input("please enter hours : ")), 15)
if payment.hours > 40 :
    result = (payment.hours - 40) * (15) + 400
    print("payment will be : " , result )     
else :
    print ("payment will be : " , payment.hours * payment.rate)