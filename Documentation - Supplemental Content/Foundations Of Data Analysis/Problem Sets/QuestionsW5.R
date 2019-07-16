library(SDSFoundations)
WR <- WorldRecords
MPvWR <- WR[WR$Event == 'Mens Polevault',]
max(MPvWR$Record)
mp70wr <- MPvWR[MPvWR$Year >= '1970',]
linFit(mp70wr$Year, mp70wr$Record)
####SLOPE IS AVERAGE INCREASE/DECREASE PER UNIT####
cvar <-c(140,280,420,560)
hvar <-c(0,2,4,6)
linFit(hvar, cvar)
# If each member of the band earned $175 for the night and profits
#were split evenly among them, how many hours did the band perform?
75*4
(700-140)/70
#These questions are wrong in the course, dollar cost should be dollars/100 to match answer
#Instead of 970, 970/100 = 9.70; Instead of 1450, 1450/100 = 14.5
dollars = 9.70
predicted_GPA = 2.84 + (0.04*dollars)
#Residual of GPA above expected
3.71 - 2.84
