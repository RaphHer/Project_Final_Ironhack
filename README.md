# Project_Final_Ironhack
Raphaël Hersant


Short description of the project 

Given my background and interest in finance, I naturally gravitated towards this area for my final project at Ironhack. My initial question is quite simple, every day, we are bombarded by financial information that would impact the financial markets., however, do they directly influence the stock markets? Next, I wanted to know how these factors have evolved over the last few years, how they correlate with the flagship index, the S&P500, and finally, I tried to predict how the latter will develop. 

Main Steps of the project:
a. Get the data
b. Clean the data 
c. Viszualisation 
d. Prediction model


1. First attempt to get the data and some visualizations

In the first instance, I tried to use resources available at my former university to retrieve the data I was interested in. I used two data sources, CapitalIQ and Refinitiv.

![Alt text](../../../../../../../C:/Users/rapha/OneDrive/ironhack/projects/Project_Final_Ironhack/images/CapitalIQ_logo.png)

![Alt text](../../../../../../../C:/Users/rapha/OneDrive/ironhack/projects/Project_Final_Ironhack/images/Refinitiv_logo.png)

From these two databases, I downloaded information on the following indicators: GDP, CPI, Unemployment rate, S&P 500 index, Monthly Home Price Index, Initial Jobless Claim, Core CPI, Consumer Credit, Non-Farm Payrolls and Chicago PMI. For each of these variables, I have included in the first jupyter notebook a definition and a link to an article in case you want to learn more. Then it was a matter of cleaning up all the data collected and making some visualizations. 

However, I quickly realised that the data I had collected would be difficult to use together and that I was facing a dead end. Indeed, the data collected had very disparate start dates, with some starting in 2004 or 2008. This meant that for some indicators, the period I had available to carry out my analyses was very, very short, and therefore, the quality of my studies would be poorer. 

2. Second attempt to get the data 
Je me suis donc remis à la recherche de données et j'ai été étonné car j'ai eu de la peine à trouver un endroit permettant télécharger de nombreux indicateurs économiques et sur une longue période. En effet, il est facile de trouver ici et là des données sur 10-20 ans mais pas plus et de trouver un endroit qui centralise et rend facilement utilisable ces données économiques. 

Et c'est là ou j'ai découvert l'API Quandl. Quandl is a premier publisher of alternative data for institutional investors. Ils ont developé un outil qui centralise l'ensemble des données publiés par difféerentes agecnes gouvernementales À travers le monde et le transofrment en time series directement téléchargeable via un API. La société a été racheté par la bourse Nasdaq et leur outil est désormais directement accessible via le site internet du Nasdaq. 

Je recommande vivement à toute personne souhaitant télécharger des données économiques directement exploitable dans python d'utiliser Quandl tant la base de données mise a diposition est vaste et aussi d'extrement bonne qualité. 

![Alt text](../../../../../../../C:/Users/rapha/OneDrive/ironhack/projects/Project_Final_Ironhack/images/Nasdaq_Logo.png)

![Alt text](../../../../../../../C:/Users/rapha/OneDrive/ironhack/projects/Project_Final_Ironhack/images/Quandl_logo.png)
