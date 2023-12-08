# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
0.86 is the R Squared coefficient for the model. It is relatively close to one however it is still a fair bit off that means that the data is mildly related. The correlation is strong however not the greatest and could b better 
2. Is your model accurate? Why or why not?
The model is accurate because the values have been standardized so the results are not too skewed in a singular direciton. Also the r squared value is not too far off from 1 meaning it is pretty accurate
3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
~8254.89 for the 10 year old car and ~2968.87 for the 20 year old car
4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
This may be occuring because the coefficient values for them are negative the older or more milage the car has the less value it is worth and therefore since this is just a predictive model it is not put incontext of actually car price per mileage and age. 