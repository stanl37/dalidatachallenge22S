

## DALI Data Data Challenge 22X + 22S
Stanley Gao '24, May 2022

### Part 1: Describe the dataset given with three or more data visualizations. These can be maps, histograms, line graphs, combinations of those, or anything else. It can be a time-series, or an interactive plot.

For a few of the following visualizations, I created quick Python scripts to collapse and manipulate the data in a way that made it easier to model. For example, for Visualization 1, I used a Python script to sum sales figures by state. In Visualization 2, I used Python to sum, count, and find summary statistics (means and medians) for profit figures by sub-category. Both of these tasks could have been done in STATA; for Visualization 3, I used the `collapse` command in STATA instead of Python.

I approached this data from the perspective of a consultant. Given this data, I wanted to create three (general categories of) visualizations that may aid company executives in their decision-making. I answer three critical questions:

 1. Who buys the most stuff?
 2. What stuff sells?
 3. Are we growing as a business?

#### Visualization 1: Who buys the most stuff?
<img src=https://i.imgur.com/Z76OuYb.png width=700 /> \
*Figure 1*: A map of the United States of total sales and profit figures, by state. Each state is colored based on the summation of all sales/all profits over all years of the dataset. I used STATA module `spmap` to create this visualization, and coordinate datafiles from [here](https://spot.colorado.edu/~jonathug/Jonathan_E._Hughes/Map_Files.html), as well as tutorials for `spmap` from [here](https://www.stathelp.se/en/spmap_world_en.html). 

This visualization is important because it answers the question of **who buys the most stuff?** From these maps, we note that California, Texas, and New York provide high volumes of gross revenue, which we could attribute to high population counts, or perhaps regionalized interest in the products we sell. We also note that of these three states, Texas has produced a net loss over our data. Further investigation could reveal why: perhaps Texans purchases more low-margin items/items we sell at a loss than other states.

#### Visualization 2: What stuff sells?
<img src=https://i.imgur.com/yXKQXqn.png width=550 /> \
*Figure 2.1*: A bar graph, describing total order counts over the entire dataset, grouped by subcategory.
<img src=https://i.imgur.com/mr0I0b1.png width=550 /> \
*Figure 2.2*: A bar graph, describing net & gross revenue **per order** over the entire dataset, grouped by subcategory.
<img src=https://i.imgur.com/VYAjr4X.png width=550 /> \
*Figure 2.3*: A bar graph, describing total order volume over the entire dataset, grouped by subcategory.

This visualization is important because it answers the question of **what stuff sells?** From Figure 2.1, we note that binders,  paper, and furnishings were ordered the most in our dataset. This highlights high-volume goods, which may be beneficial if per-unit profit margins are high (increasing sales, or increasing price-per-unit can result in major increases in profits), but could also be detrimental (high volume goods require high spending in shipping, handling, etc., which we could look to cut out in efforts to reduce labor costs).

Figure 2.2 suggests that per order, copiers bring in both the most net and the most gross revenue. If I was a consulting firm, I would recommend this company look into developing their copier inventory and supplier connections. I would also point out that many of our high gross revenue items, such as tables and bookcases are actually sold at a loss. This is detrimental to the firm's profitability. We also could note that copiers produce a significantly higher profit per order compared to other goods. This is not to be taken out of context, however, as...

Figure 2.3 suggests that over our entire dataset, the majority of our subcategories are profitable. As a company focusing on office supplies (Staples-esque, perhaps), this fits our business model. However, we can note that we do sell tables at a loss - both per order and overall. Recommendations to raise prices or lower costs of manufacture would be in order. Investigations into ways to improve profit margins would also benefit high gross revenue categories such as phones and chairs.

#### Visualization 3: Are we growing as a business?
<img src=https://i.imgur.com/XbV2GlZ.png width=700 /> \
*Figure 3*: A bar graph, describing order volume by week, alongside a 50 day moving average, and a linear line of best fit over the entire dataset.
This visualization is important because it answers the question of **are we growing?** From this visualization, we note that cyclicity exists in our order volume. We see, by our 50-day moving average, that we generally trend upward in sales volume week by week through the year, with spikes in September (the start of school years, perhaps) and December (the holiday rush). Sales drop massively at the start of every year; this could warrant investigation. We also note, by the green linear fit, that this company's sales are growing steadily over time. This is a generally a good sign, however we may need to analyze competitors, market share, etc. for a fuller picture.

### Part 2: Free-Form Modeling

profit, with x vars state (predict profit increases if we increase customers in a certain state, segment, category, subcategory, targeted marketing)
https://towardsdatascience.com/learn-how-to-create-animated-graphs-in-python-fce780421afe
animated pie chart: shipping choice, line graph (over the years, first class has become a much more chosen option, etc.)
	- multivariable analysis including subcategory, etc.

For this part of the data challenge I ran a multivariate linear regression on the WIID dataset using STATA's `areg`, trying to predict Gini coefficients based on inputs such as income group, EU status, OECD status, exchange rates to the US Dollar, GDP PPP Per Capita, and Population. I controlled for year effects and absorbed country fixed effects. While many of my controls were rejected by STATA for collinearity, the regression I ran resulted in an R-squared of 0.7238. I cannot provide a visualization of my multivariate regression because there is no way to represent it in 3D space given the number of controls I've included. However, an `outreg2` output is shown below.

![outreg2](https://i.imgur.com/MOoWqRB.png)

This model attempts to predict a country's GINI coefficient, given its country's population, GDP, and exchange rate to the US Dollar. The coefficients of all three of our main independent variables are statistically significant. The coefficient to `exchangerate` tells us that for an additional increase in the ratio of foreign currency to US dollars (for example, 6 Chinese yuan to 1 USD becoming 7 Chinese yuan to 1 USD), the Gini coefficient is estimated to rise by 0.000227. And similarly, for every 2011 US Dollar increase in GDP PPP Per Capita, the Gini coefficient is estimated to rise by 0.000290. And finally, for every additional person added to a country's population, the Gini coefficient is estimated to rise by an incredibly small number.

All three coefficients are positive, which indicate that increasing exchange rates (having a currency that simply expresses value in greater numbers), GDP PPP PC, and population all increase the Gini coefficient – they all increase income inequality. While this association is interesting, we must make sure to avoid assuming causality. There are many third factors that may be impacting this data, and as such we have not fulfilled one of our crucial validity assumptions.
