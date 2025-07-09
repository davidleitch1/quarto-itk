---
title: "IRR models"
author: "David Leitch"
date: "2024-11-15"
categories: [analysis, wind]
image: "../media/image-20241105161719005.png"
lightbox: true
format:
  html:
    include-after-body:
       - "../comment_load.html"
  docx: default
draft: true
---



# Introducing ITK's VRE NPV IRR generic models

## Summary

## Introduction

In the electricity industry the LCOE (Levelised Cost of Electricity) is commonly  represents the average price required for a new generation unit to recover its capital and operating costs and earn its Weighted Average Cost of Capital (WACC).  In finance its equivalent is an asset that has a Net Present Value (NPV) of zero or put yet another way its Internal Rate of Return (IRR) exactly equals WACC.

LCOE/IRR/NPV models of a generic desciptiion are available from a range of sources. These include NREL [Annual Techniology Baseline](https://atb.nrel.gov/electricity/2023/land-based_wind) which provide good documentation of assumptions but which are USA based,  Lazards also produce a similar USA based  [analysis](https://www.lazard.com/research-insights/levelized-cost-of-energyplus/) but with less assumption discussion. IRENA produces a understandably global [report](https://www.irena.org/Publications/2024/Sep/Renewable-Power-Generation-Costs-in-2023)

In Australia the most well known and heavily analysed report is the CSIRO [Gencost report](https://www.csiro.au/en/research/technology-space/energy/gencost). However in my opinion the CSIRO diminished the reliability of its report by trying to include system LCOE as well as asset LCOE data.

In addition investment banks and many others produce asset and or project specific NPV analysis. 

However the estimates of LCOE and inputs show considerable variation. In the following table where an organisation has provided 2 or more estimates of a parameter I have taken a simple average of the high and the low. Figures presented in \$US have been converted to \$A at 1.43.

For instance to compare four estimates of onshore wind:

![image-20241105161719005](../media/image-20241105161719005.png)

Note, NREL provides far more detail but for the USA only. I have used the 2025 projection. IRENA's estimates go only to 2023 and are based on the average data across a range of countries within which there may be significant variation in wind speeds and costs.

And for solar, where its immediately clear the IRENA data is for fixed rather than tracking solar.
![image-20241105201059642](../media/image-20241105201059642.png)

- The NREL data is for the USA for an assumed 2025  and the assumptions are spelled out in detail. NREL provides forecasts out to 2050 with the cost falling due to a learning rate assumption.
- IRENA is a global data base average, but really the coverage is fairly minimal compared to say what the IEA covers. The IRENA data is backward looking with the last year as 2023.
- Lazard's numbers are expressed as high and low range which I have converted to a simple average. There is some assumption discussion but not enough to really dig in. Lazard's numbers are a survey of costs, in the USA.
- CSIRO's Gencost outcomes are expressed as a range and again I have taken an average. CSIRO does project forward and I have used the 2025 numbers. 

For NREL wind has a lower LCOE than solar in the USA. In Australia it's the reverse. Australia is good at building solar and we are assisted by not having tariffs on imported panels.

Other numbers are also superficially at odds. Lazard has similar capex and opex as NREL for onshore wind but as the table shows arrives at an LCOE 34% higher. 

CSIRO does not provide rooftop LCOE analysis. That is a shame given its cumulative share of capacity and the 2.5 GW of capacity added every year. If CSIRO did provide the LCOE analysis we would see that Australia's rooftop capex  expressed as \$/MW works out to less than 1/3 of that in the USA. Capex for rooftop solar in the USA is about US\$2.5m/MW or about A\$3.5 m/MW . In Australia with the SREC subsidy its around A\$0.85m/MW and adding back SREC the cost would still not be that much more than say A\$1.1m/MW

## The global variation emphasises the reason for ITK to provide its own estimates.

Even a casual glance at the variation and limitations within external providers emphasises the need for "owning" the numbers. The interesting thing is that the variation of results between forecasts occurs 

Our estimates of NPV are informed by estimates of capital costs based on our 'channel checks' for capital and operating costs. We do our own capacity factor analysis and then adjust for MLFs.

Other items that drive LCOE are the length of the  project life, we use 25 years, and the discount rate, or more formally the weighted average cost of capital (WACC)

We also allow for an assumed marginal loss factor (MLF) 

Rather than provide an LCOE ITK shows our estimate of  the IRR that a wind or solar asset is expected to achieve given our forecast electricity prices and estimates of costs.

### Windturbine capacity factors theory references

ITK makes its models as simple as we can. Within reason this is most fundamentally driven by a view that the margin of error for an external party in calculating LCOE or IRR is sufficiently high that only a false sense of improvement is gained by making the model more complex and having more bells and whistles. Equally the possibilities for errors and the maintenance requirements are also higher. 

Nevertheless it helps when making an assumption that a wind farm capacity factor is say 35% (before MLF and other system related constraints) to appreciate at least some of the factors driving the capacity factor.

The following discussion is taken from [thundersaidenergy](https://thundersaidenergy.com/downloads/wind-power-impacts-of-larger-turbines/#:~:text=The%20best%20overall%20formula%20for,(in%20meters%20per%20second).). 

> "The best overall formula for the power derived from a wind turbine (in Watts) is P = 0.5 Cp ρ π R2 V3, where Cp is the coefficient of performance (efficiency factor, in percent), ρ is air density (in kg/m3), R is the blade length (in meters) and V is the wind speed (in meters per second)."

The formula shows that power is a cube function of wind speed and a square function of blade length. Equally no wind turbine can ever capture more than 59.3% of incoming wind energy due to the horizontal wake. (The wind spreads out after passing through the turbine)

ITK also uses both the wind capacity factors provided by AEMO per REZ, although we also understand that both a high and low factor are provided and individual wind farms may not get either. Equally the AEMO factors are also based on a representative hub height, that is the wind is measured at 100 metres and for a representative power curve. ITK has adopted the REZ by REZ half hourly capacity factors for both wind and solar.

## Turbine prices







