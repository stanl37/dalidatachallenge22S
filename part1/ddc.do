cap clear matrix
clear
cap log close
set more off
set scheme black_tableau

/*
Describe the dataset given with three or more data visualizations. These can be maps, histograms, line graphs, combinations of those, or anything else. It can be a time-series, or an interactive plot.

Think, if you could only show someone these graphs to describe most of the data, what graphs would you choose.

Design matters, making this beautiful matters.

The sky is the limit!
*/

cd "C:\Users\gaost\Dropbox (Dartmouth College)\22S\dali data challenge"
log using _ddc.log, replace


//// vis 1: map of total sales, total profits by zip (where buys the most stuff?)
clear
import delimited using "vis1.csv"
merge m:m statename using "US_States_LowRes_2015data_Stata11.dta", nogenerate keepusing(_ID)
drop if sales==.

// profits
colorpalette HCL pinkgreen, n(15) nograph

spmap profit using "US_States_LowRes_2015coord_Stata11.dta", ///
id(_ID) fcolor(`r(p)') ndfcolor(gray) ///
clmethod(custom) clbreaks(-30000 -20000 -15000 -12500 -10000 -5000 -2500 0 1 1250 2500 5000 10000 20000 40000 80000) ///
title("Total Profits by State")
graph save _vis1_p.gph, replace

// sales
colorpalette HSV heat, n(10) reverse nograph

spmap sales using "US_States_LowRes_2015coord_Stata11.dta", ///
id(_ID) fcolor(`r(p)') ndfcolor(gray) clmethod(kmeans) cln(10) ///
title("Total Sales by State")
graph save _vis1_s.gph, replace

// export both
set scheme gg_tableau
graph combine _vis1_s.gph _vis1_p.gph, title("Total Sales & Profits by State")
gr export _vis1.png, replace as(png)
set scheme black_tableau


//// vis 2: bar graphs by subcategory
clear
import delimited using "Sample - Superstore.csv"

// means
graph bar (mean) sales profit, ///
over(subcategory, sort(1) descending label(angle(45))) ///
legend(label(2 "Profit") label(1 "Revenue") cols(2)) ///
ytitle("Dollars USD") title("Mean Net & Gross Revenue per Order, by Subcategory") ///
legend(position(6))
graph export "_vis2_mean.png", replace

// totals/sums
graph bar (sum) sales profit, ///
over(subcategory, sort(1) descending label(angle(45))) ///
legend(label(2 "Profit") label(1 "Revenue") cols(2)) ///
ytitle("Dollars USD") title("Net & Gross Revenue, by Subcategory") ///
legend(position(6))
graph export "_vis2_sum.png", replace

// counts
graph bar (count) sales, ///
over(subcategory, sort(1) descending label(angle(45))) ///
ytitle("Orders") title("Order Volume, by Subcategory") ///
legend(position(6))
graph export "_vis2_count.png", replace


// analysis by year
/*
gen yr = year(date2)

graph bar (mean) sales profit if yr==2017, ///
over(subcategory, sort(1) descending label(angle(45))) ///
legend(label(2 "Profit") label(1 "Revenue") cols(2)) ///
ytitle("Dollars USD") title("Mean Net & Gross Revenue per Order, by Subcategory") ///
legend(position(6))

graph bar (sum) sales profit if yr==2017, ///
over(subcategory, sort(1) descending label(angle(45))) ///
legend(label(2 "Profit") label(1 "Revenue") cols(2)) ///
ytitle("Dollars USD") title("Net & Gross Revenue, by Subcategory") ///
legend(position(6))

graph bar (count) sales if yr==2017, ///
over(subcategory, sort(1) descending label(angle(45))) ///
ytitle("Orders") title("Order Volume, by Subcategory") ///
legend(position(6))
*/


//// vis 3: orders over time
clear
import delimited using "Sample - Superstore.csv"
gen date2 = date(orderdate, "MDY")
format date2 %td
gen week = date2 - dow(date2) // aggregating into weeks
format week %td

bysort week: gen orders = _N // generate weekly order total
collapse orders, by(week) // collapse data

tsset week
tssmooth ma myMA=orders, window(49 1 0)

twoway (bar orders week) (line myMA week) (lfit orders week), ///
ytitle("Orders") xtitle("") title("Orders Over Time, by Week") ///
legend(label(1 "Orders per Week") label(2 "50 Day Moving Average") label(3 "Linear Fit") cols(3)) ///
tlabel(29dec2013(91)24dec2017, angle(45)) ///
legend(position(6))
gr export "_vis3.png", replace

cap log close
