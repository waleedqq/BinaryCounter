
x = 5
finalDayPayment = (2)**(x-1)
print("Payment on Final Day only: %s" % finalDayPayment)



total = None
runningTotal = 0

# Method 1
for y in range(x):
    runningTotal = (runningTotal) + (2**y)
    #print ("Running Total %s" % runningTotal)
else:
    total = runningTotal




#####################Method 2    
Method2 = ( (2)**(x) ) - 1
print("Print Method 2: %s" % Method2)



    
print("Sum of all the payments: %s" % total)


