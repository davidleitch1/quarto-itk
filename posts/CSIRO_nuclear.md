---
title: "Gencost"
author: "David Leitch"
date: "2024-06-13"
categories: ["Emerging Tech", "Economics & Investment", "Policy & Regulation"]
image: "../media/image-20240613111756278.png"
lightbox: true
format:
  html: default
  docx: default
draft: false
---



![Reducing the negatives](../media/image-20240613111756278.png){width=80%}

## Good to see the  AFR getting into electricity modelling

Its great to see  that  John Kehoe,  economics editor at the AFR now wants to [write](https://www.afr.com/policy/energy-and-climate/the-flaws-in-csiro-s-anti-nuclear-pro-renewables-report-20240611-p5jktp) about the CSIRO Gencost report. Kehoe implys or states  that the CSIRO report is biased and makes incorrect assumptions. Specifically he quotes others as saying that coal generation is cheaper than renewable generation and that the CSIRO report underplays the advantages of always on dispatchible power. In my opinion the article gets quite a few things wrong, probably most importantly the assumption that always on power is somehow "better" than power that is not always on and that this should be allowed for in the Gencost report.In my opinion this reflects the usual naive biases of someone that hasn't put much work into the topic.

In this note I seek to show that LCOE capacity factor assumptions can be done on a number of bases and that there is no single right or wrong answer. As with all modelling the suitability of the assumptions comes down to the question that is being answered.  Gencost style LCOE modelling does not suit my own taste because it trys to go beyond the individual asset into the system cost, a task far better left to the ISP. However even in the stricter view of LCOE that I espouse there is an inescapable need to choose between technical and economic capacity factor assumptions for dispatchible plant. At the least within the context of what I see as a "potshot" article Kehoe could have acknowledged the issue. 

 The AFR is a fine paper  that I have been reading for more than 50 years. but on electricity and decarbonisation, in my opinion as a long term reader and professional analyst, its been garbage from the beginning. It could take some lessons on how to do it from "The Economist". One of my great pleasures and dailly motiviations was when Angela Macdonald Smith wrote as if was an insult "David Leitch analyst at UBS - a greenie". It was an insult to be a labelled a "greenie", and from within the investment banking research community no less.  For the record I do not personally support the "Greens". There was no concept then at the AFR  and so far as I can tell,  still isn't, that global warming is an existensial style problem which will massively impact Australia's economy and that denial or dismissal wasn't going to cut it. Indeed my own investment philsophy is based around the concept that there is money to be made because most investors will react to slowly to the changing world. And that the sluggishness of their views will be confirmed by reading  mainstream media such as the "AFR"

 The entire reason why I reached out to Giles Parkinson in the very early days of Reneweconomy when I was still at UBS was because Reneweconomy offered a fresh voice in a sea of garbage.

So its no surprise to see an article that just "doesn't get it" in the AFR. That's normal. They don't get it there. Fair enough. However what is surprising is to see such a value ridden biased piece of research from Kehoe.

Hiistorically Kehoe's research has been balanced and reasonable, even enjoyable.  This article, it seems to me is not balanced.

Kehoe writes:

> "GenCost bizarrely assumes coal is more expensive than renewables"

That statement is both biased and  flat out incorrect. An outcome of the Gencost  process is to find that a new coal plant built under the Gencost assumptions has a higher LCOE than a wind or solar plant. That's of course even  ignoring the carbon cost. There is no "bizarre assumption" its an outcome of the model assumptions. By all means have at the modelling assumptions, but please avoid assuming the conclusion. 

Kehoe then quotes Aidan Morrison with seeming approval:

> "Renewables are definitely not cheaper than coal". 

In fact numerous studies find renewables to be cheaper than coal. Kehoe does absolutely nothing in the article to check the validity or otherwise of that statement.

 I might add I do my own modelling but I'm not shy of checking my numbers against those that others use. 

Globally, in my opinion, there are at least two publishers of LCOE that are a source of authority. The first is Lazard who published Version 17.0 of the their annual Gencost study  just recently. The numbers are for the USA in $US

![Lazard LCOE. Source: Lazard 2024](../media/image-20240612145055949.png)



Every estimate of LCOE has several assumptions.  Here I  draw attention to  Lazard's use of:
60% debt at 8% and 40% equity at 12% and the assumption that a nuclear plant operates at 97% capacity utilisation for 80 years.

![LCOE sensitivity to WACC. Source:Lazards 2024](../media/image-20240612145416346.png)

The other major source is BNEF. BNEF almost certainly have the industry's largest global team of full time energy related analysts. However most of their work is highly paywalled reflecting the value added. 

This figure is taken from an early 2022 publication.
![Low cost energy by country. Source:BNEF](../media/image-20240612145958923.png)



To summarise no global analyst would be in the least bit surprised to find a report stating that in Australia the LCOE of wind and solar is less than coal. To be honest I'd have been very  suprised at anything else. its been that way for years and even if wind costs are much higher then its likely that new coal generaion costs have risen as much.

## What is LCOE and should we care?

I've been calculated LCOEs for 30 years and more and I am here to tell you there is no definitive "right" answer. No two people doing the sums will use the same assumptions.  Also unsurprisingly the assumptions going into an LCOE calculation can generally be changed to to give a different answer. 

I doubt that people in the industry really spend a lot of time on published  LCOEs. Personally I have never paid any more attention to Gencost numbers than to Lazard numbers. Every financial analyst there has ever been is basically fine calculating their own NPV estimates of a generation asset  and it takes only the slightest amount of rearranging to turn that NPV calculation into an LCOE. As such why use someone else's numbers when you can use your own. Where the skill comes is understanding the assumptions and why you would choose one and not another and how sensitive the result is to an assumption choice.

Its also important to appreciate that costs change in the real world as well as in the spreadsheet. A few years ago onshore wind LCOEs could be calculated in the A\$40/MWh area. Today the numbers are double that. 

LCOE = Levelised Cost of Energy essentially represents the price required for an electricity plant to exactly earn its cost of capital over its life. The origin of the term is unclear but it appears to have been first used in the 1980s. I understand it to be the same as  Long Run Marginal Cost (LRMC) in the microeconomics lexicon.

To calculate the LCOE an analyst is required to forecast all costs of an asset over its life and then find a price for the annual output that will recover the present value of those costs.

To calculate the present value we make use of the time value of money. That is for example \$1 to be received in one year's time is worth less than \$1 received today. 

In short to calculate the LRMC:

- A discount rate must be chosen. In strict theory, and in practice not all technologies "should" have the same discount rate because some technolgies have riskier cash flows than others. For instance a gas generator may be subject to the market price of gas. In general higher discount rates will more heavily penalise technologies with longer term cash flows compared to those getting their cash back more quickly.

- The useful life of the technology must be assumed. However it is very widespread practice to calculate the net present value  of a project for a finite life. Typically one of 20, 25 or 30 years is chosen. Due to the magic of discounting the value today of a life longer than 30 years is a small part of the total value. For instance at a discount rate of 10% years 30-60 add 6% to the value of a project and years 60-90 add nothing to the present value today. So making a nucleare plant 80 years instead of 30 changes the answer by 6-13%.  Not trivial but not all that big. Equally if you are going to do that for one technology you have to do it for every technology. Pumped hydro developers are always complaining that us analysts don't give them enough credit for long life.

  ![PV of $1. Source:ITK](../media/image-20240612152926614.png)

  Of course these discount calculations take no account of the technology and uncertainty that the future bring, just the time value calculation.

- The capacity factor needs to be estimated. Capacity factor is expected output/output if operated every hour of the year. Solar plants have a low capacity factor, they only operate in daylight hours. The industry even has a term for plants that are dispatchible but only expected to operate occassionally and that's "peakers". In fact the entire concept of the "merit order"  presupposes that capital intensive plant will need a higher capacity factor than capital light but higher operating cost plant.

  Mr Kehoe is on safer ground than in most places in his article when he observes that cost and value are not the same.  Consumers every where will be grateful for this epiphany.

- Capital cost needs to be estimated. In the case where lots of a technology is being built capital costs are not that hard. For technologies like coal and nuclear capital cost estimates in Australia are pretty much a guess.  Another associated assumption is generally that the piece of kit can be built "overnight". That is a nuclear plant can be built in the same time as a solar plant or coal plant or offshore wind plant. I am reasonably confident that if the construction time was factored into a nuclear plant then from an NPV estimate it would likely take care of the continuing life assumption. If we factored in carbon costs between now and 2030 this overnight cost assumption would look like a bigger miss than the continuing value. 

- Fuel costs need to be estimated. It should be obvious that thermal fuel costs, including perhaps future carbon costs are uncertain in some cases. For some coal generation you can assume an owned or "captivee" coal mine in other cases less so. In the end someone has to take the risk around the cost of the fuel, either the generator or further upstream.

  

  ## System cost v technology cost, the true weakness of Gencost

  In the past exercises such as Gencost  or LAZARD 17,  LCOE estimates served a limited purpose of calculating the price required to justify the investment in one piece of kit. It was never the case that a piece of kit can operate in isolation from a system. A coal  plant or a nuclear plant needs transmission as much as a wind or a solar plant. Its a matter of historical record that the pumped hydro industry in the USA was developed to back up nuclear plants.

  However in the past noone cared that the LCOE of a coal plant was only part of the total system cost. And in my opinion the preferred view should be that LCOE estimates, Gencost included, should in general confine them selves to the price required for the individual asset.

  Its the job of system builders, the job of the ISP designers, to put the bits of kit together and create a system and estimate the system LCOE. That is the cost required to build and operate a system, such as the NEM. 

  The ISP uses a complex modelling methodology, orders of magnitutde above what can be provided in any LCOE individual asset analysis.

  ![ISP methodology. Source:AEMO](../media/image-20240612161350826.png)

  The ISP has its own strengths and weaknesses like any other model, but the point here is that within its assumptions it builds the lowest cost system capable of keeping the lights on and meeting policy objectives.

  Certainly the ISP takes account of capacity factors.

  ## Dispatchible power capacity factors require a viewpoint

  Capacity factors were briefly discussed above. Even for wind and solar plant capacity factor is not as simple in the real world as is sometimes assumed in the spreadsheet. For instance should "spillage " be allowed for, should capacity factor be before or after an MLF assumption? For single axis solar there is an assumption about the DC:AC ratio. 

  Where the question becomes a double or nothing kind of thing is for dispatchible power. Specifically gas, coal and nuclear. The question is whether to use technical or economic capacity factor. Its not a question that I've worried much about in the past, but its a legitimate question.

  Its most obvious to think about this in the context of open cycle gas. I imagine that an open cycle gas plant is technically capable of operating at about a 70% capacity factor. Maybe more. That is even allowing for blade maintenance if there was enough gas, noone cared about carbon emissions and the price was right you could run it about 70% of all the hours in the year. I don't really know what the technical capacity factor is because generally open cycle gas plants are not run like that. They are run to provide peak capacity and because of the prices they receive can sometimes earn their cost of capital on capacity factors less than 10%.

  From the point of LCOE if you assumed a capacity factor of 70% the gas plant would require a much lower price than if you assume a capacity factor of 10%.

  The plant is technically capable of 70% but in use won't run more than 10% of the time. What capacity factor should the modeller use? I am going to suggest that a modeller that uses 70% won't be taken all that seriously.

  

  ## Nuclear capacity factor in Australia

  In summary: Nuclear is very expensive even when modelled at full capacity factor. Using the latest  recently published Lazard estimate for the USA which itself employes a capacity factor of 97%  its around US\$190/MWh or A$280/MWh. However even though nuclear is technically capable of being ramped up and down it ruins the economics. 

  Consider the changing look of  coal generation in the NEM,

  ![Coal generation NEM wide](../media/image-20240613102753516.png)

  This is a year long average by time of day and why I used 2023 rather than 2024.

  In another 5 years there will be at least another 10 GW of solar, actually counting behind the meter and utility very likely there will be another 15 GW of solar. In the middle of the day that will ON AVERAGE FOR THE ENTIRE YEAR just about reduce demand for any other source of generation to zero in the middle of the day.

  Its hard to see why any rational policy maker would want to run a nuclear plant in the middle of the day, let alone 5-10 of them. Its an utter waste of resource. 

  Generation technology choices do not live in isolation from the system in which they operate. For those not already tired of the debate around small, modular reactors (SMR) the fact is that they are a technology designed to deal with the reality of a system that has lots of renewables and specifically lots of solar. 

  It is a fact that a nuclear plant built in Australia that sold its electricity into the spot market would, for the forseeable future get pretty much zero for that electricity during daylight hours. Rationally it would be turned off, or alternatively like wind and solar plants operating at the same time the energy can be spilled.

  Although apparently not appreciated by John Kehoe this was explained by Steve Hamilton and Luke Heeney in the SMH back on [18 March](https://www.smh.com.au/politics/federal/nuclear-is-ok-if-it-makes-economic-sense-but-mr-dutton-in-australia-it-doesn-t-20240317-p5fd1s.html),. It would be tedious for readers for me to repeat the discussion but the whole reason that coal plants are going away is because they lose money in the middle of the day, more than they can recover in the evening.  Consultants have been writing reports about this for years.

  As Hamilton and Feeney write:

  > "The trouble is that nuclear is a *terrible* companion to renewables. The defining characteristic of being “compatible” with renewables is the ability to scale up and down as needed to “firm” renewables. Countries like France can only make nuclear work by exporting large amounts of energy when it’s surplus to demand. "

  This then is the problem that the CSIRO faces when  thinking about a new coal or nuclear plant, what is the appropriate capacity factor to use?

  In short there is nothing wrong with using 97% as the capacity factor for a nuclear plant, but if you are looking at it from an economic viability point of view neither is there anything wrong with using say 50%.  And if you use 50% you end up with far higher cost.

  More to the point, nuclear has two advantages for Australia. First it is carbon free, second to some extent it can make use of existing transmission. 

  Against that it has massive disadvantages. Its incredibly expensive, the potential construction delay risk is totally unacceptable  and the technology is fundamentally unsuited to Australia's generation mix.