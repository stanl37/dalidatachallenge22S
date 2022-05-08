

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

It is also worth noting, I created a `year` variable and ran a couple visualizations by year (only transactions from 2017, etc.), but didn't find much significantly novel information. I omitted these visualizations in this writeup for brevity, but they are in my STATA do-files.

#### Visualization 3: Are we growing as a business?
<img src=https://i.imgur.com/XbV2GlZ.png width=700 /> \
*Figure 3*: A bar graph, describing order volume by week, alongside a 50 day moving average, and a linear line of best fit over the entire dataset.
This visualization is important because it answers the question of **are we growing?** From this visualization, we note that cyclicity exists in our order volume. We see, by our 50-day moving average, that we generally trend upward in sales volume week by week through the year, with spikes in September (the start of school years, perhaps) and December (the holiday rush). Sales drop massively at the start of every year; this could warrant investigation. We also note, by the green linear fit, that this company's sales are growing steadily over time. This is a generally a good sign, however we may need to analyze competitors, market share, etc. for a fuller picture.

### Part 2: Free-Form Modeling

For this part of the data challenge, I decided to use Python's `pandas`, `numpy`, and `matplotlib`. I had no previous experience with these libraries, and had to learn them from scratch for this application. As such, my code for this part of the challenge is not optimized nor is it likely the best solution. However, I hope this demonstrates my open-mindedness and ability to quickly learn new technologies on the fly.

For this modelling challenge, my idea was to investigate shipping rates: answering the question, **are people becoming more impatient?** I wanted to look at changes in shipping rates over time, to find trends that may have been helpful to company administration. Claims such as, *"people are favoring same-day shipping more and more, so we should change our inventory handling strategy so people have to wait less for the products they want"* could have been made.

However, I found that over the years of data in this dataset, shipping rates remained relatively constant:
<img src=https://i.imgur.com/mdDRPMK.gif width=700/> \
*Figure 4*: An animated multi-line graph, animated in `matplotlib`, showing the usage of the company's four available shipping options (First Class, Same Day, Second Class, and Standard Class) over time.

This visualization counters my claim that people are becoming more impatient, as companies such as Amazon increase shipping speeds from 3-5 days, to 2-day, to same-day. This data shows that, from ~2014-2018 (the time range of our data), people generally have not changed their preferences. We back this claim up with rigorous statistical analysis. Using a linear regression in STATA, we find that:

A one week increase in the date (proceeding one week into the future) statistically significantly (`n=209, t=-2.27, p=0.024`) decreases percentage of orders using the standard class shipping method by ` .0000537`, or `0.00537%`. The regression is below, and my code is provided in do-files.
![STATA regression of standard class shipping method on week.](https://i.imgur.com/dsCKaSe.png)

While my findings were statistically significant at conventional alpha levels `0.1` and `0.05`, the economic significance is dubious. With a weekly decrease in standard shipping method selection of `0.00537%`, the predicted decrease over the course of a year is just `0.27924%`. This is not a large enough number to cause worry, especially given the small nature of the dataset, with only 209 weeks of observation. Further, my regression was performed using collapsed-by-week data instead of analyzing the dataset in full form, which could be a flaw in this model. Ultimately, I do not feel comfortable claiming that people are becoming more impatient.
