library(tidyverse)

spx = read_csv("C:/Users/Lee Sak Park/Desktop/Python Finance/SPX.csv")

spx[(dim(spx)[1]+1),] = c("6/8/2020", 3199.92, 3233.13, 3196.00, 3232.39)


spx$Close = spx$Close %>% as.numeric

# examplary is the last 15 trading days

e_data = tail(spx, 15)


e_data['days'] = 1:length(e_data$Date)

e_data['Close'] = e_data['Close']/e_data$Close[[1]]*1000

model = lm(Close ~ days + I(days^2), data = e_data)
summary(model)

model1 = lm(Close ~ days, data= e_data)
summary(model1)


beta1 = model1[[1]][[2]]
beta2 = model[[1]][[3]]
r_sq = summary(model)$adj.r.squared
r = summary(model1)$r.squared

## Let's run the loops to find the most close ones
slope = c()
acceleration = c()
rs = c()
r_sqs = c()


for(i in 1:(dim(spx)[1]-50)){
 df = spx[i:(i+14),]
 df['days']=1:15
 df$Close = df$Close/df$Close[1]*1000
 
 model_trial = lm(Close ~ days + I(days^2), data = df)
 model_trial1 = lm(Close ~ days, data = df)
 slope[i] = model_trial1[[1]][[2]]
 acceleration[i] = model_trial[[1]][[3]]
 r_sqs[i] = summary(model_trial)$adj.r.squared
 rs[i] = summary(model_trial1)$r.squared
}


# Now, we are interested in 50 similar cases and will sort out with the big r-sq numbers

index = 1:length(r_sqs)
results = cbind(index, slope, acceleration, r_sqs, r)

results = results[(slope > beta1-summary(model1)$coefficients[2,2]),]
results = results %>% as.data.frame
results= results[results$acceleration > beta2-1*summary(model)$coefficients[3,2],]
results = results[results$r > .8,]
results = results[results$r_sqs > .8,]
similar_days = results$index

# let's see how they moved next 5 days after the close


index_1 = similar_days + 1
index_2 = similar_days + 2
index_3 = similar_days + 3
index_4 = similar_days + 4
index_5 = similar_days + 5
index_10 = similar_days + 10
index_15 = similar_days + 15



day1 = spx$Close[index_1]/spx$Close[similar_days]*100
day2 = spx$Close[index_2]/spx$Close[similar_days]*100
day3 = spx$Close[index_3]/spx$Close[similar_days]*100
day4 = spx$Close[index_4]/spx$Close[similar_days]*100
day5 = spx$Close[index_5]/spx$Close[similar_days]*100
day10 = spx$Close[index_10]/spx$Close[similar_days]*100
day15 = spx$Close[index_15]/spx$Close[similar_days]*100

dates = spx[similar_days,"Date"]
df = cbind(dates,day1, day2, day3, day4, day5, day10, day15)

boxplot(df[,2:8])
