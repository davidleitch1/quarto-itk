---
title: "The Changing Shape of the NEM"
author: "David Leitch"
date: "2026-02-11"
categories: ["Storage", "Generation"]
image: "../media/image-20260211144602497.png"
lightbox: true
format:
  html:
    include-after-body:
       - "../comment_load.html"
  docx: default
draft: false
---

## Summary

- Demand is up 8% in the past year compared to 2022—quite respectable really.
- Demand has grown most strongly in the middle of the day and in QLD.
- On the numbers there will be enough battery energy available to significantly impact volumes, both charging and discharging. Battery power (at least 15 GW) is equal to more than 50% of average NEM demand. Those batteries will want to charge and be dispatched. 
- However:-  batteries are visible in the supply numbers but not as prominent as their operating capacity would suggest.
- Also, existing gentailers are adding battery capacity the fastest, and their owners will work hard to manage spot prices to their advantage. So we need not just more batteries but more independent batteries, more actual competition in the evening peak market.
- Finally, as everyone knows, the pace of new wind and solar development remains abysmal. We are already in February 2026 and there is nothing obvious happening with new wind farms in NSW.



## Demand has responded to price at least modestly

The following plot shows NEM wide demand for the past year compared to the Feb 2022-23 period on a time-of-day basis and the time-of-day, region-share-of-demand-weighted, NEM-wide spot price for both years.

![image-20260211144602497](../media/image-20260211144602497.png){#fig-demand-timeofday}

The takeaways are:

- 8% increase in average demand. That actually surprised me.
- The demand increase is concentrated in the middle of the day. That's pleasing because it shows that contrary to what engineers think, economists do know what they are talking about and demand has shifted to where the price is lower.
- This probably reflects an increase in self-consumption for those households that have solar and where  feed-in tariffs have fallen.  More midday behind the meter consumption such as hot water storage, pool pumps, home battery charging, etc.I have no data to support that, but in general consumers don't see spot price signals. And between networks focused on fixed pricing and gentailers with their own motivations, the chances of a spot price signal being passed on to the average punter are low.
- Of course, more demand in the middle of the day might be partly due to temperature, but that should have led to higher early evening peak demand, so I am inclined to think the price driver is dominant. 
- I should also note that business customers probably are more able to respond to spot price signals. They can buy solar PPAs in some cases, and often tender just for energy.
- No doubt the solar saver will increase this. But the point is it was already happening. 

For what it's worth it's most obvious in QLD.  That's natural because QLD is most exposed to rising temperatures and has the best solar resource. .

![image-20260211145844007](../media/image-20260211145844007.png){#fig-qld-demand}

The 2022 price plot is saw-toothed because it uses a trimmed mean to avoid spikes.

## Batteries will cut into evening peak volume as well as impacting price

I received a bunch of pushback on my note saying batteries would impact coal volumes as well as prices. But I reckon the facts are fairly clear even if you need good eyes to observe them right now. I am reminded of the economist who predicted three of the last one recessions. There will be at least 15 GW of batteries when all that have started construction are operating. As you can see from the first plot that's enough to meet more than half the NEM demand for 2 hours, actually 2.5 hours. Plus there was probably closer to 8 than 7 GWh of cumulative household battery installed capacity. I estimate that's about 1 GW of power if they all ran at once, though information on inverters is limited. Some of that will be outside the NEM.

![image-20260211151446206](../media/image-20260211151446206.png){#fig-battery-capacity}

More batteries are certain to be developed—in the end they will be needed. Meantime, about half that capacity is nominally installed. But as we know some is not yet commissioned and Waratah has 2/3 of its capacity out of action.

![image-20260211152500329](../media/image-20260211152500329.png){#fig-battery-ownership}

This plot also indicates that the big gentailers remain major players in the market, particularly in NSW with the Liddell and Eraring batteries both of which are to some extent still commissioning. It's unlikely consumers will see the full benefit of the battery capacity without adequate competition.

## Peak demand and price developments?

It's interesting that even though there are notionally 7.5 GW of battery capacity and probably 5 GW in full service battery output is only a fraction of this on average. This analysis focuses on the evening peak because that is where the market share and spot price competition from batteries will be focussed. So that's broadly 6 pm to 10 pm in the QLD timezone the NEM uses.  

The average output over the past 90 days in the NEM is just 1.2 GW. That's up on last year but not as much as I might expect. My plot does exclude Kidston.

![image-20260211155433491](../media/image-20260211155433491.png){#fig-battery-output}

Once again QLD is the state where the most disruption is going on, due to wind as well as batteries, but this is masked by the increase in demand.

![image-20260211155714600](../media/image-20260211155714600.png){#fig-qld-peak}

## New wind projects remain thin on the ground

It's good batteries are doing something, because new wind projects remain thin on the ground.

![image-20260211160315208](../media/image-20260211160315208.png){#fig-wind-pipeline}

Although once again, and including MacIntyre, QLD has the biggest pipeline. Eventually even MacIntyre will end up being fully commissioned.