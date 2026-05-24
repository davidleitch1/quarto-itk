# Spot prices along the journey to a coal free NEM

## Mission impossible 

Since 2017 my mission has been to demonstrate, to my own standard of proof, that electricity prices in the NEM, post coal will be globally competitive, even bottom quartile.

In particular I wanted to show that we can run aluminium centres and data centres and other energy intensive businesses on renewable energy.

In my view the world needs to decarbonise and Australia is well placed to lead the way.

This view has been resisted at every step of the way from skeptics and vested interests. The opposition starts with:

- Climate change is fiction;
- Climate change is real but doesn't matter (the current view of BHP, RIO, WPL, STO as demonstrated by their actions)
- Renewable energy is expensive;
- Renewable energy is unreliable;
- Spinning machines are needed for;
  - Frequency control;
  - Short circuit ratios

Using social media, and a flood the zone strategy first articulated by Steve Bannon, political classes appealing to emotions and grievances have  amplified these concerns. This happens as far as I can see in every country but is strong in Australia because it can be funded by the coal, gas and LNG industries. Australia is after all, one of the three largest fossil fuel exporters in the world.

There  are many twists and turns along the way but because I was brought up in middle class Australia I believe that in the eternal struggle the good guys win. And the best strategy for winning is to keep putting the facts on the table. In the end facts matter more than emotion. In the end humans will rationally act in their best long term interests. Everyone  that saves for a house is sacrificing consumption today for a better long term future. People that think like that will consider climate change as an issue for the future generations. What's the point of having kids if you condemn them to worse world than we live in?

## Electricity prices post coal will be little different to today

In this note I show that electricity prices in real terms in 2045, assumed to be post coal, will be little different to today.

Also I find that even with wind costs being much higher than assumed by Gencost and therefore AEMO for the ISP that the lowest consumer cost system ends up with lots of wind.

Two main tools were used to get these results.

Firstly I used "Vertex" ITK dispatch machine to find the LRMC of a post coal system in 2045 using three representative AEMO weather years and  AEMO's half hourly forecast operational  demand traces, as adjusted by me.

With that end point established and with a known starting point (capacity in the NEM in 2028) its then a question of finding the lowest consumer cost path that still provides a generator returns to get from the starting to the end point.

ie: Minimise the net present value of total consumer wholesale energy
cost over 2028-2050, summed half-hourly across NEM regions, subject to
each capacity vintage (a region's MW of a technology built in a given
year) earning a lifetime internal rate of return of at least the
WACC (5% real pre-tax).

Or you can express it with fancy maths and stats symbols. Claude does a much better job with formatting than I ever could, never mind the formulation (which in concept was my idea). I include that in the Methods section

It turns out that the lowest cost comes from front loading the generation, so it's built before QLD coal is closed down. One of the assumptions I make is to extend the life of QLD coal plants by 5 years compared to AEMO's ISP assumption. There is a carbon cost in that. 

## Demand 

I started with AEMO's ISP P50 demand traces. Then  sharply reduced the out year hydrogen, modestly reduced electrification and in the end increased data centre demand in the early years with a convex curve so that by 2050 it ends up in the same place. A point that emerged during the study was the higher data centre demand the higher the firming required because the flatter the load. Data centres will need to bring their own firming, and this will benefit the system.

## ![nem_demand_itk](../media/nem_demand_itk.png)

## Capacity costs

The ISP central case and the range of 2045 capex assumptions that I used for sensitivity testing is shown in the following plot.
![capex_range_vs_gencost](../media/capex_range_vs_gencost.png)

You can see that I tested a range of wind capex much above that assumed for the Gencost Central case. The results produced here are for wind capex at the upper end of what was tested.

A plot that shows the sensitivity of the LRMC optimised capacity in 2045 for various wind, solar and battery costs is

 ![vwap_with_roi](../media/vwap_with_roi.png)

The key points I take from the plot are:

- VWAP is more sensitive to the wind capex assumption than it is to the solar or battery capex cost.
- But that sensitivity is relative. Even at high wind capex the LRMC still has plenty of of wind in the capacity mix.
- Battery capex is less important than the quantity of battery storage. That the batteries exist is what matters, not so much what they cost.

## Capacity trajectory

In this modelling BTM batteries and solar are excluded. I  "adjusted"  AEMO's  "OPSO" series for our BTM batteries and rooftop numbers. You can see the difference between ITK's series, we can ajdust our number much faster than AEMO's more rigorous process. So these numbers reflect the Bowen plan but end up at the same point. We don't alter the daily shape of charge and discharge, only the scale.

![btm_aemo_vs_itk](../media/btm_aemo_vs_itk.png)





![capacity_mix_dear_wind_2026Q2](../media/capacity_mix_dear_wind_2026Q2.png)

The process was:

From a 2028 capacity floor (representing committed projects in AEMO's Committed Development Project list, CDP4) we build a year-by-year trajectory to the 2045 endpoint using a convex front-load profile, $f(t) = 1 - (1-t)^2$ where $t = (y-2028)/(2045-2028)$, for solar and
BESS, and a wind cap of 3.5 GW/year NEM-wide.

This means that the capacity build was front loaded to avoid the problem of not building enough capacity when QLD coal was running and then QLD coal closing faster than new capacity could be built, lifting prices during those years.

The bottom line is, that even if QLD insists on running its coal generators for longer consumers would still be better off if the replacement capacity is built earlier.

The initial guess at the capacity trajectory didn't guarantee that producers would earn ROI so the model was iterated on a "Vintage WACC" That is a unit of wind or solar had to earn WACC, simply defined, over its lifetime. For each iteration over earning capacity was increased and under earning reduced until convergence defined as capacity of each fuel in every year earning a life time ROI was achieved, and subject to the build rate constraints. That took about 8 iterations.

Note that for each iteration the technologies were dispatched across  all weather years and over the horizon of 2028 to beyond 2050 and for 17, 520 half hours. If you think about it that's a lot of sums. 

The "solved" and adopted capacity buildout compared with a linear build exhibits the same convex shape but for entirely different reasons. 

![build_vs_linear_dear_wind_2026Q2](../media/build_vs_linear_dear_wind_2026Q2.png)

AEMO's ISP has typically ended up building wind before solar although for all I know the reasons might be quite different. 

Capacity was allocated to the regions roughly in ISP proportions and within a region to REZs using the sam allocation.  For each vintage we each region's tech IRR was checked and some capacity was reallocated away from under earning regions to over earning. There are limits to what can be achieved given requirements to increase capacity or at least not reduce it one year and build it the next. The rebalance reallocates capacity from regions whose lifetime IRR factor is below the
NEM mean to regions above. For dear_wind_2026Q3_bl the principal movements at year-end 2038 are: QLD solar 27.4% → 22.2% of NEM, NSW solar 44.0% → 46.6%; QLD wind 39.1% → 36.8%, NSW wind 37.0% → 38.5%; NSW BESS 8h 46.4% → 51.0%, QLD BESS 8h 21.9% → 19.5%. If there was more flexibility in where wind was located and how fast it could be built then more reallocation would have been done.

## Once capacities for each year are determined Vertex is used to calculate prices

Each iteration dispatches the LP at half-hourly resolution for all 23 forecast years (2028-2050) across all 3 weather reference years (2011, 2018, 2019)  After convergence  the
fleet was held fixed and re-dispatched across **all 13 historical
weather reference years (2011-2023)** 

### Cost parameters

| Parameter                                | Value                                   |
| ---------------------------------------- | --------------------------------------- |
| WACC (real pre-tax)                      | 5.0%                                    |
| Solar CAPEX, 2045                        | A$575/kW (GenCost NZE-by-2050 baseline) |
| **Wind CAPEX, 2045**                     | **A$3,500/kW (1.63× GenCost baseline)** |
| BESS 2h / 4h / 8h CAPEX, 2045            | A$436 / 628 / 992 /kW                   |
| Solar life                               | 30 yr                                   |
| Wind life                                | 30 yr                                   |
| BESS 2h / 4h / 8h life                   | 15 / 20 / 20 yr                         |
| Solar FOM                                | A$12,000/MW/yr                          |
| Wind FOM                                 | A$29,000/MW/yr                          |
| BESS FOM (all durations)                 | A$12,500/MW/yr                          |
| Carbon shadow price (AER)                | A$94 (2030) → A$420 (2050) /tCO₂        |
| Weather reference years (final dispatch) | 2011-2023 (all 13)                      |
| Weather reference years (iteration)      | 2011, 2018, 2019                        |
| Gas price                                | A$11/GJ                                 |
| OCGT heat rate / EF                      | ≈11.25 GJ/MWh / 0.55 tCO₂/MWh           |
| CCGT heat rate / EF                      | ≈7.5 GJ/MWh / 0.40 tCO₂/MWh             |