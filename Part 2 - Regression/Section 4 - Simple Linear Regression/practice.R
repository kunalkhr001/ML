# Simple Linear Regression

dataset= read.csv('Salary_Data.csv')
library(caTools)
set.seed(123)
split= sample.split(dataset$Salary, SplitRatio= 2/3)
training_set= subset(dataset, split == TRUE)
test_set= subset(dataset, split == FALSE)

# Fitting Simple Linear Regression to training set
regressor = lm(formula = Salary ~ YearsExperience, data = training_set)

y_pred = predict(regressor, newdata = test_set) 
cat(y_pred)
# Visualising training set results
library(ggplot2)
ggplot() + 
	geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary), colour= 'red') + 
	geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)), colour = 'blue') + 
	ggtitle('Salary vs Experience(training set)') + 	xlab('Years of Experience') + ylab('Salary')


# Visualising test set results
ggplot() + 
	geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary), colour= 'red') + 
	geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)), colour = 'blue') + 
	ggtitle('Salary vs Experience(test set)') + 	xlab('Years of Experience') + ylab('Salary')


