library(SDSFoundations)
WR <- WorldRecords
MenMile <- WR[WR$Event == 'Mens Mile',]
WomenMile <- WR[WR$Event == 'Womens Mile',]
plot(MenMile$Year, MenMile$Record, main = 'Mens Mile World Record', xlab = 'Year', ylab = 'World Record(seconds)')
plot(WomenMile$Year, WomenMile$Record, main = 'Womens Mile World Record', xlab = 'Year', ylab = 'World Record(seconds)')
linFit(MenMile$Year, MenMile$Record)
linFit(WomenMile$Year, WomenMile$Record)
1/0.39347
1/0.97288
