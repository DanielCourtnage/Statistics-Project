# Statistics-Project
## Rolling **n** dice, summing results, removing nulls and repeating

This is a write up for a statistics project I did for a friend of mine. They told me they were playing a game where they roll 6 dice, remove all values of 2 and 5, summing the remaining dice, then roll the remaining dice until the sequence terminates. One friend had a roll of 121 and wanted to know the odds (0.33%) of that occurring.

I wasn't aware of a way to put that question into a formula relating to a normal distribution that I could test against, so I decided to model it using Python. As we know, the closer to infinty we get the closer it tends to a continuous distribution that we can use for analysis. 

I decided to write this so it can be manipulated for any amount of any sided dice with any numbers removed. Possibly used to see how lucky or unlucky similar rolls were in other games such as D&D, Monopoly etc. I hope anyone reading this finds it useful. 

The full code can be found [here](https://github.com/DanielCourtnage/Statistics-Project/blob/main/Code.python). While below I've written out explanations for each stage.


### Part 1: [Imports and Variables](https://github.com/DanielCourtnage/Statistics-Project/blob/main/Imports%20and%20Variable.py)
I start with importing Python packages. **Random** allows me to randomly generate random numbers, **numpy** and **matploblib** will allow me to analyse and plot our results later. The variable **biglist** is created which will store multiple iterations of our function. **x** and **y** are the specific dice rolls we're removing from the pile. If you wish to add or remove more or less dice each time you'll need add another line to the function later on. **test** is the mumber we are testing against. In the original question from my friend they rolled 121 and wanted to know the probability of it (0.33%). Iterations is simply how many times we want to run the function. The closer this number is to infinity, the closer we are to perfectly modelling the probabilty density function. I chose 1,000,000 because that's the highest number my laptop can handle. 

### Part 2: [MyFunction](https://github.com/DanielCourtnage/Statistics-Project/blob/main/MyFunction.py)
This next section focuses on the main function. This simulates 6 dice rolls, removing values we don't need, summing up the remaining die, rerolling the remaining die and repeating until there are no dice left. First we tell the function we are using 6 dice. We then use the random import from earlier to generate 6 random numbers between 1 and 6. These integers are stored in an empty list called **list** which we will talk about later. We then use the function **count** to count how many 2's and 5's are in the array and remove them from **list** using the remove function. We then update the **dice** variable to minus the amount of 2's and 5's. While the **dice** function is greater than 0 the function repeats. When the **dice** variable reaches 0 it stops.

### Part 3: [Iterations](https://github.com/DanielCourtnage/Statistics-Project/blob/main/Iterations.py)
This next part is the function above repeating 1,000,000 times to create a larger array that we can use for analysis. It simply creates an empty list called **list** which we are then able to put our dice rolls into. We then run the function and sum the list we've just created to get our **score** for the game. We add it to **biglist** and repeat 1,000,000 times. 

### Part 4: [Analysis](https://github.com/DanielCourtnage/Statistics-Project/blob/main/Analysis.py)
This next part is the analysis. We convert **biglist** into an array and then find how many **values** are higher than our test number from earlier. We then display useful information about what the % was of our test, the mean of the data and the standard deviation. The last part is a simple histogram to visualise our data.
