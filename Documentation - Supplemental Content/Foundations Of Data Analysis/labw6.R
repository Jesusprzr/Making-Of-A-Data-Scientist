library(SDSFoundations)

wbd <- WorldBankData

dnk <- wbd[wbd$Country.Code == 'DNK',]

dnk90s <- dnk[dnk$year >= 1990,]

zero90s <- dnk90s$year - 1990

netprop <- (dnk90s$internet.users / dnk90s$population)

expFit(zero90s, netprop)

logisticFit(zero90s, netprop)

#solve for 70% netprop with exp equation:
0.7 = 0.00585(1.34666)^t
log(119.6581197)/log(1.34666) = 16.07593194
#16 = in 2006 70% of population will be using internet.

#Solve for 70% netprop with logistic equation:

0.7 = 0.89668/(1 + 308.8322*1.73123^-t)
(1 + 308.8322*1.73123^-t)0.7 = 0.89668
(1 + 308.8322*1.73123^-t) =0.89668/0.7
(1 + 308.8322*1.73123^-t) = 1.280971
1.73123^-t = (1.280971/308.8322) -1

1.73123^t = (308.8322/1.280971) + 1
log(1.73123)t = log(242.0923)
t = log(242.0923)/log(1.73123)
10.00182 #<- Wrong answer, should be 13 = 2003

0.7 = 0.89668/(1 + 308.8322*1.73123^-t)
(1 + 308.8322*1.73123^-t)0.7 = 0.89668
(1 + 308.8322*1.73123^-t) =0.89668/0.7
(1 + 308.8322*1.73123^-t) = 1.280971
308.8322*1.73123^-t = 1.280971 - 1
1.73123^-t = 0.280971/308.8322
1.73123^-t = 0.0009097853
ln(1.73123)(-t) = ln(0.0009097853)
-t = log(0.0009097853)/log(1.73123)
-t = -12.75855
t = 12.75855 #<- That's the answer.





