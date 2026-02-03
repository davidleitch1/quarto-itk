---
title: "Coal Generation in the NEM - GSD 2026"
author: "David Leitch"
date: 2026-02-03
categories: ["Generation"]
image: "../media/image-20260202164515745.png"
lightbox: true
format:
  html:
    include-after-body:
       - "../comment_load.html"
  docx: default
draft: false
---

# It's a pleasure to welcome this year's GSD

Global Roam is arguably the longest running and most trusted name in the supply of NEM data and certainly the best placed to provide the comprehensive DUID by DUID analysis of generator performance. Greenview have deep practical knowledge of what it takes to succeed in the Australian energy market.

Good, clean data provided by a team that understand how to present the data, how to minimise confusion and enhance clarity for users is essential to those of us that live in the world of prices that change every 5 minutes but have to be related to events and markets of years ago. Irving Fischer it was that said "coming events cast their shadows before them" and it's the history provided in the GSD that provides the context through which we can distinguish those shadows from the noise.

Coal generation has been the backbone of electricity supply in Australia since long before the formation of the NEM, which itself started in 1998 following the Hilmer recommendations and report in 1993. Almost 30 years on from the NEM formation, a combination of technology and environmental forces is leading to a changing of the guard in generation. In this note I sketch out the recent history of coal generation showing how operators have done a mighty job of adjusting to the new world but inevitably increasing risk in the process.

As is evident from the GSD, coal generators are these days prone to falling over at inconvenient times, in NSW last year the GSD shows Mt Piper unit 1 and Bayswater units 2 & 3 out of action when the price signal to operate was strongest. Although the NEM overall probably is more resilient than ever from both a generation and transmission perspective, thanks to the rooftop contribution and to solar's contribution during heatwaves, coal generation in total is less resilient because there are few spare units. 

Markets have in the end worked as they are supposed to, the high prices in the evening peak have enticed new supply in the form of batteries, purpose-built to make money from those peak prices. I expect this to weaken the economics of coal generation and for this to be quite evident in the next couple of years. 

As coal generation exits, prices will push up due to reduced supply and the cycle will repeat. There will be no shortage of batteries because there will be no shortage of solar energy to charge them.

Battery suppliers face far lower barriers to entry than coal or gas suppliers. In my view this makes the market inherently more competitive and that is to consumers' and Australia's benefit. Still it will be bumpy with renewables beating their chests in Spring and thermal still being required in Autumn and early Winter.

# Coal Generators have adjusted but economics are set to deteriorate again

Coal generation is down in all States over the past five years but amusingly it's down the least in the only State to close a major station in that time, NSW, with AGL having closed the Liddell power station in 2023, arguably for sound economic reasons.

In Victoria average generation is down about 13% over the five years but in NSW only 2.3%.

![Coal generation](../media/image-20260202164515745.png){#fig-coal-generation}

It's only when we get into the average time of day data that the real story emerges. First look at the three States together. Each shows a pronounced decline in midday production and then a pick up in the evening and overnight market.

![Coal gen by time of day](../media/image-20260202164740830.png){#fig-coal-timeofday}

Even more intriguing is that in NSW, despite the closure of Liddell, evening peak generation is now higher than in 2021.

The two stations in NSW that have made this adjustment the best are Mt Piper and Bayswater. These stations have been able to adapt output to the spot price signal. And as the plot shows, spot prices remain very elevated compared to the pre-Ukraine invasion levels.

![Bayswater, Mt Piper price following](../media/image-20260202165205858.png){#fig-bayswater-mtpiper}

The flexibility of these plants is astonishing compared to what I, a financial analyst, thought they could achieve when thinking about the issue 15 years ago.

### Flexibility comes at a cost, particularly for ageing plants

Firstly, the plants are old and they are being asked to do things they were not originally designed for and so it's no surprise to see outages. The GSD shows outages at units 2 and then 3 last year right in the period of peak demand when management likely most wanted them online.

![Bayswater Unit 2 outages](../media/image-20260203133146453.png){#fig-bayswater-unit2}

And here's Unit 3 with the visible gap in May.

![Bayswater Unit 3 outages](../media/image-20260203133253378.png){#fig-bayswater-unit3}

And here is Unit 1 of Mt Piper.
![Mt Piper Unit 1 outages](../media/image-20260203133421724.png){#fig-mtpiper-unit1}

Secondly, revenue has been squeezed into a smaller and smaller window, with 10% of revenue now earned in the 7-8 PM window.

![NSW coal revenue by time of day](../media/image-20260202170530768.png){#fig-nsw-coal-revenue}

Of course revenue and price are only part of the profitability story. Data on costs is not available in the same way the Statistical Digest provides information on capacity, revenue, FCAS, and volumes. 

### The market has provided a price signal for battery investment that will eat into profits

In Queensland and Victoria the generators typically have captive coal mines or in Qld long term arrangements, but in NSW the generators to some extent compete with the export market for coal. Typically though it's lower quality coal. Regular price data is hard to come by but with a bit of interpolation we can get a series of Indonesian 5200 kcal coal (22 GJ/Tonne). When looking at NSW there are all sorts of transport issues but I am just going to use the quoted Indonesian price.

![Indonesian coal price](../media/image-20260202172001696.png){#fig-indonesian-coal-price}

Then I need to adjust for fixed and variable operating costs, we can use AEMO numbers, and then based on what AGL and ORG disclose I add a further \$10/MWh for end of life maintenance capex. So in my opinion, and maybe it's better than this, coal generation costs are as high as \$60 or even \$70/MWh. There's a range and Bayswater is probably quite a bit lower.

Using that cost data we can then estimate spot market profitability for NSW coal generators by time of day.

![NSW coal gen profitability](../media/image-20260202172557369.png){#fig-nsw-coal-profitability}

That evening coal profitability is under threat from batteries. Despite one day of extreme temperatures and prices, average prices in Jan '26 were down. To be sure wind output was up but there was on average another 1 GW of batteries this year compared to PCP.

![NSW gen supply evening peak](../media/image-20260203000345829.png){#fig-nsw-evening-supply}

And that's only a foretaste. Total battery GW are set to triple and battery GWH to quadruple plus the rooftop batteries. The impact of this will be to provide supply competition in the evening peak supply market. That will drive down price, although gas is the price setter then, coal rides on gas's coattails and the loss of price rather than volume will hurt coal profitability.

If more wind is built, and that remains the dominant scenario, then that too will provide price insensitive competition in the evening and overnight market. The thing about wind and solar is that they generate whenever the resource is available. That makes them ill suited to managements that naturally like to build oligopoly-like structures. What's the point of being the dominant wind or solar supplier? 

![Battery pipeline](../media/image-20260203000617581.png){#fig-battery-pipeline}