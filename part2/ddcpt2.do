cap clear matrix
clear
cap log close
set more off
set scheme black_tableau

cd "C:\Users\gaost\Dropbox (Dartmouth College)\22S\dali data challenge"
log using _ddcpt2.log, replace


clear
import delimited using "Sample - Superstore.csv"
gen date2 = date(orderdate, "MDY")
format date2 %td
gen week = date2 - dow(date2) // aggregating into weeks
format week %td

gen yr = year(date2)

bysort week: gen orders = _N // generate weekly order total

gen stdc = 1 if shipmode == "Standard Class"
replace stdc = 0 if stdc == .

collapse orders stdc, by(week) // collapse data

reg stdc week

cap log close
