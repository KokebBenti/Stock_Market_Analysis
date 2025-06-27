# Stock_Market_Analysis
**Introduction**  
This week, we worked on behalf of Nova Financial Solutions to increase its financial forecasting accuracy by analyzing data from the news. We tried to find the connection the news and stock market prices. We explored the concepts Data Engineering, Financial Analytics, and Machine Learning Engineering.

**Methodology**  
To complete the project and find the necessary answers, we followed the following steps.  
**1.	Sentiment Analysis**    
This is the process of using computational techniques to analyze digital text and determine the emotional tone expressed within it to classify it as positive, negative, or neutral. This process leverages natural language processing (NLP), machine learning (ML), and text analysis to identify, extract, and quantify subjective information.    

For our project, we performed analysis on the headline of financial news using NLP to derive sentiment scores. We analyzed the text to find trends over time and analyze the publishers. This includes:  
	Using text analysis to identify common keywords.  
	Trying to find trends over time.  
	Finding out the most active publishers and what they publish.  

Time series graph for the news data looks like below.
 

**2.	Quantitative Analysis**  
Quantitative analysis is the process of using statistical methods to collect, evaluate, and interpret data such as market share, stock prices, or financial ratio to understand behavior, assess performance, and predict outcomes in finance. In finance, quantitative analysis is used to analyze financial markets, develop trading strategies, forecast market movements, optimize investment portfolios, and manage risk by quantifying the volatility and relationships among different assets. 
For our project, we conducted quantitative analysis to find more insight into our stock prices data. The data had columns such as Open, High, Low, Close, and Volume.   
 
We then:  
	Cleaned the data.  
	Used to calculate technical indicators like as moving averages, Relative Strength Index, and Moving Average Convergence Divergence.  
	Visualized the data to understand it better like a candlestick charts.  
  
**3.	Correlation Analysis**
Correlation analysis is a statistical method used to measure and evaluate the strength and direction of the relationship between two or more variables. It helps us determine whether changes in one variable are associated with changes in another, and quantifies this association using a correlation coefficient.  
This includes:  
	Ensuring that the news and the stock data are aligned by date.  
	Computing percentage changes in price to see the effect of the news.   
	Conduct correlation analysis to find correlation between sentiments and stock returns.  
 
**Challenges and Recommendations**  
•	One challenge that was faced during this week was the news data covering news from 2020 or earlier. Having a more recent news data can help us predict the prices more accurately in the future.  
•	Pandas-ta was used instead of pynance and TaLib was used to conduct quantitative analysis as it was easier to install.  

**Conclusion**  
This week, we performed quantitative analysis on the stock prices of companies like Amazon and Apple. We also tried to calculate the sentiment from news headlines and find if there is a correlation between the stock prices of the companies and the news related to the companies. The challenge taught us Data Engineering, Financial Analytics, and Machine Learning Engineering.
