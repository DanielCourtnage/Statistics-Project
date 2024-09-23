# Statistics-Project
Rolling n dice, summing results, removing nulls and repeating

This is a write up for a statistics project I did for a friend of mine. They told me they were playing a game where they roll 6 dice, remove all values of 2 and 5, summing the remaining dice, then roll the remaining dice until the sequence terminates. One friend had a roll of 121 and wanted to know the odds (0.33%) of that occurring.

I wasn't aware of a way to put that question into a formula relating to a normal distribution that I could test against, so I decided to model it using Python. As we know, the closer to infinty we get the closer it tends to a continuous distribution that we can use for analysis. 

I decided to write this so it can be manipulated for any amount of any sided dice with any numbers removed. Possibly used to see how lucky or unlucky similar rolls were in other games such as D&D, Monopoly etc. I hope anyone reading this finds it useful. 

The code and annotations can be found here
