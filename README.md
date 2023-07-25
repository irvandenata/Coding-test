# Coding-test

## Question #1 (maintenance)
●	What is wrong with the above code?
answer : the code give worng result if we give x with under zero value or negative value

●	If you find it wrong, please fix the code above without using the “*” or “/”  operator or Absolute call?

●	As part of our development process we test all methods at a code level. Which input values would you use to do the testing?
Answer : 
to test that code we can give 4 scenario

1. x and y is a positive value

2. x and y is a negative value

3. x is a positive value and y is a negative value

4. x is a negative value and y is a positive value


## Question #2 (SQL)

● Select USA.NAME, EU.NAME From USA, EU Where USA.ID = EU.ID

NAME	NAME

Thomas	Thomas

● Select USA.NAME, EU.NAME From USA left join EU on (USA.ID = EU.ID)

NAME	NAME

Thomas	Thomas

Cindy	NULL


● Select USA.NAME, EU.NAME From USA, EU

NAME	NAME

Cindy	Francois

Thomas	Francois

Cindy	Thomas

Thomas	Thomas

## Question #4 (performance)

Case 1 has a longer execution time than case 2, because if bagA has a large number of elements, the loop becomes much better




