# election_analysis

### Overview of Project
Steve wants to help his parents figure out where to invest their money. Utilizing Excel and VBA, the overall Volumes and return can be summarized for 2017 and 2018 can be visualized with the click of a button. Color coding even exists to quickly see if the return was positive or negative. The module used arrays to speed up the code.

### Results
Overall, 2017 was a much better year than 2018, as you will see in the Resources folder. In 2017 only TERP was negative on return while in 2018 10 out of 12 were negative on the return. ENPH and RUN were the only stocks that had a positive return both years. ENPH had a much higher return in 2017 while RUN was higher in 2018. I would suggest Steve’s parents do more research into those companies and decide which to invest in, or invest in both to diversify their portfolio.
![alt text](https://github.com/Betsy-Kalkwarf/election_analysis/blob/main/Resources/2017%20results.png)
![alt text](https://github.com/Betsy-Kalkwarf/election_analysis/blob/main/Resources/2018%20results.png)

The refactored code using arrays worked much faster. The 2017 run went from 0.73 to 0.13 seconds. 
![alt text](https://github.com/Betsy-Kalkwarf/election_analysis/blob/main/Resources/2017%20before.png)
![alt text](https://github.com/Betsy-Kalkwarf/election_analysis/blob/main/Resources/Refactored%202017.png)


The 2018 run went from 0.76 to .13 seconds. 
![alt text](https://github.com/Betsy-Kalkwarf/election_analysis/blob/main/Resources/2018%20before.png)
![alt text](https://github.com/Betsy-Kalkwarf/election_analysis/blob/main/Resources/Refactored%202018.png)

The arrays helped the code run in less than 20% of the original time.


### Summary
Refactoring code can be advantageous because you don’t have to start from the beginning. You can also improve code. It can be difficult, if it is someone else’s code you are refactoring. You may not understand their thought process.
I kept getting errors when trying to refactor the code. I didn’t exactly understand why the instructions were telling me what to do, without giving me background in why I was going through those steps. I think I would have rather refactored my code from the homework with an explanation behind what was being asked. Eventually I realized I misplaced a line of my code outside of an If statement, instead of within the If statement. If I had been making the code from scratch, I may not have had the issue. But the provided code did save me time creating some of the other parts of the code.


