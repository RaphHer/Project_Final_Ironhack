# Project_Final_Ironhack
Raphaël Hersant


Short description of the project 

Given my background and interest in finance, I naturally gravitated towards this area for my final project at Ironhack. My initial question is quite simple, every day, we are bombarded by financial information that would impact the financial markets., however, do they directly influence the stock markets? Next, I wanted to know how these factors have evolved over the last few years, how they correlate with the flagship index, the S&P500, and finally, I tried to predict how the latter will develop. 

Main Steps of the project:
a. Get the data
b. Clean the data 
c. Visualization 
d. Prediction model


1. First attempt to get the data and some visualizations

In the first instance, I tried to use resources available at my former university to retrieve the data I was interested in. I used two data sources, CapitalIQ and Refinitiv.

![Alt text](../../../../../../../C:/Users/rapha/OneDrive/ironhack/projects/Project_Final_Ironhack/images/CapitalIQ_logo.png)

![Alt text](../../../../../../../C:/Users/rapha/OneDrive/ironhack/projects/Project_Final_Ironhack/images/Refinitiv_logo.png)

From these two databases, I downloaded information on the following indicators: GDP, CPI, Unemployment rate, S&P 500 index, Monthly Home Price Index, Initial Jobless Claim, Core CPI, Consumer Credit, Non-Farm Payrolls and Chicago PMI. For each of these variables, I have included in the first jupyter notebook a definition and a link to an article in case you want to learn more. Then it was a matter of cleaning up all the data collected and making some visualizations. 

However, I quickly realised that the data I had collected would be difficult to use together and that I was facing a dead end. Indeed, the data collected had very disparate start dates, with some starting in 2004 or 2008. This meant that for some indicators, the period I had available to carry out my analyses was very, very short, and therefore, the quality of my studies would be poorer. 

2. Second attempt to get the data 

So I started looking for data again, and I was surprised by the difficulty I had in finding a website that would allow me to find in one place economic indicators over a long period and ready to be downloaded. Indeed, it is easy to find websites that provide, for example, the evolution of GDP over ten years, but not over more extended periods and especially not downloadable. 

And after a bit of research, I discovered the Quandl API. Quandl is a premier publisher of alternative data for institutional investors. They have developed a tool that centralizes all the data published by different government agencies worldwide and transforms it into a time series that can be directly downloaded via an API. The Nasdaq Stock Exchange has acquired the company, and its tool is now directly accessible on the Nasdaq website. 

I recommend to anyone wishing to download economic data directly usable in python to use Quandl as the database made available is vast and also of outstanding quality. 

![Alt text](../../../../../../../C:/Users/rapha/OneDrive/ironhack/projects/Project_Final_Ironhack/images/Nasdaq_Logo.png)

![Alt text](../../../../../../../C:/Users/rapha/OneDrive/ironhack/projects/Project_Final_Ironhack/images/Quandl_logo.png)

After downloading Quandl and creating access to my jupyter notebook, I downloaded the following data set all for the US: 
- M2 - Measure of money supply
- Average GDP and GDI 
- S&P 500 inflation adjusted 
- Consumer Sentiment Index
- Big Mac Index
- Consumer Price Index
- Real Estate Loans 
- Initial Jobless Claims
- Total Revolving Credit 
- PMI Composite Index 

I did some cleaning and saved the combined DF together.

3. Visualization of the data and correlation matrix 
![Alt text](../../../../../../../C:/Users/rapha/OneDrive/ironhack/projects/Project_Final_Ironhack/images/1.%20set%20of%20visualization%20.png)  

The first graph shows the evolution of the S&P 500, the M2 money supply, the GDP and the consumer price index. It is interesting to note the exponential growth of these four indicators. 

![Alt text](../../../../../../../C:/Users/rapha/OneDrive/ironhack/projects/Project_Final_Ironhack/images/2.%20set%20of%20visualization%20.png)

In the second graph, initial job claims, PMI, consumer sentiment and the price of a Big Mac in the US are displayed. The main observations are the explosion of initial job claims during the covid, the PMI, which has fallen below 50, the consumer sentiment, which is historically low or the price of a big mac which seems to have decreased during the last semester.

![Alt text](../../../../../../../C:/Users/rapha/OneDrive/ironhack/projects/Project_Final_Ironhack/images/3.%20set%20of%20visualization%20.png)

Finally, the evolution of the two most important types of credit for US consumers. First, the hypothecary credit has been decreasing since the overheating of 2007-2008, and finally, the credits linked to credit cards are historically high. 

I then did a matrix correlation with all the observed variables, and here is the result of the correlation factors according to the S&P 500

Ranking and Metric  |  Correlation factor
------------------- | -------------
1. M2 | 0.94
2. CPI | 0.90
3. GDP | 0.93
4. Revolving Credit | 0.86
5. Big Mac | 0.8
6. RE Loan | 0.29
7. Initial Claims | 0.12
8. PMI | 0.025
9. Consumer Sentiment | 0.014