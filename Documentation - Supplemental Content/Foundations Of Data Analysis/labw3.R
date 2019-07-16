library(SDSFoundations)
brs <- BullRiders
nb12 <- brs[brs$Events12 > 0,]
hist(nb12$Earnings12)
median(nb12$Earnings12)
max(nb12$Earnings12)
plot(nb12$RidePer12,nb12$Earnings12)
cor(nb12$Earnings12,nb12$RidePer12)
hist(nb12$CupPoints12)
plot(nb12$CupPoints12,nb12$Earnings12)
cor(nb12$Earnings12,nb12$CupPoints12)
# identify specific case
which(nb12$Earnings12 == max(nb12$Earnings12))
nb12[4,]
#Subset the data
nooutlier <- nb12[nb12$Earnings12 < 1000000 ,] 
myvar <-c("Earnings12", "CupPoints12", "RidePer12")
cor(nb12[,myvar])
cor(nooutlier[,myvar])
nb14 <- brs[brs$Events14 > 0,]
rpe14 <- nb14$Rides14/nb14$Events14
median(rpe14)
hist(rpe14)
fivenum(rpe14)
min(rpe14)
plot(rpe14,nb14$Rank14)
abline(lm(nb14$Rank14~rpe14))
cor(rpe14,nb14$Rank14)
xvar <-c(30,45,180,95,130,140,30,80,60,110,0,80)
yvar <-c(74,68,87,90,94,84,92,88,82,93,65,90)
plot(xvar,yvar)
abline(lm(yvar~xvar))
xvar <-c(30,45,180,95,130,140,80,60,110,0,80)
yvar <-c(74,68,87,90,94,84,88,82,93,65,90)
plot(xvar,yvar)
abline(lm(yvar~xvar))
cor(xvar,yvar)
0.5967026^2
