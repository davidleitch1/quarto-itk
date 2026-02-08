---
title: "Data centre in Riverina"
author: "David Leitch"
date: "2025-07-9"
categories: ["Demand"]
image: "../media/image-20250709174704767.png"
lightbox: true
format:
  html:
    include-after-body:
       - "../comment_load.html"
  docx: default
draft: false
---

# If datacentres are built in Canberra why not the Riverina

Recent discussions have indicated two problems which put together may represent an opportunity.

1. There is not enough transmission to utilise all the potential supply of VRE in the Riverina. ITK has several times over the past two years pointed out that credible developers have upwards of 10 GW of projects that can be built in an area centred on say Balranald. That energy could go either to Victoria via VNI West or to Sydney via Humelink but neither transmission line has enough capacity. Moreover Victoria doesn't have the stomach to build onshore and would rather build offshore wind no matter how expensive it is. 

2. Datacentre developers, particularly NextDC, are just starting to build 100 MW and larger Datacentres in Australia. Naturally like everything else datacentres are built in Capital cities. Naturally like everything else primarily Sydney with Melbourne and Brisbane fighting for second place and Melbourne usually winning. However the point here is that the cost of power is a big deal for megascale datacentres. In the USA it's lead to development near the generation. 

   In this note I do a thought experiment of looking at the potential power cost for a datacentre located adjacent to a renewable project in the Riverina. Because I am a humble desktop warrior I am in my element doing desktop studies. Because we can use LLMs as coding and research assistants it's possible for a very small team (me) to be seemingly productive. In addition although I am not a datacentre expert I am a follower of trends and have been writing computer code since attending a course at Armidale tech while in high school. Again at university I remember doing an extra curricula course on "basic" via the UNSW radio channel and how thrilling it was to realise I could actually do the work. And then there was the port of 6502 assembler code from the Apple 2E to the Commodore Pet. I digress as usual.

   Finally in terms of motivation and credentials growing up in regional NSW in the 60s I was often hearing about the benefits of decentralisation.  However for a variety of reasons it mostly hasn't happened. The share of Australia's population in the 8 major capitals is now 68% up from 65% 30 years ago. Most electricity demand is in those same capital cities. According to infrastructure Australia about 70% of Australian GDP is earned in the big cities with 45%-50% coming from Melbourne and Sydney combined. 

   I would argue that the fact that the regions are the smaller group is a problem for decarbonisation. Smaller groups may have a stronger identity to protect, may see differentiation as more important and in the case of regional Australia will tend to be older and face other challenges. Decentralisation cannot be forced, we have learned that, but nevertheless opportunities to diversify and grow the regions should be welcomed. 

   All that said outsiders rarely understand what's going from the insider perspective. We are like spectators at a football game full of advice for the manager and the players but not charged with delivering a result on the field.

## Australian cost and location factors

Data centres in Australia are relatively small by global standards and are all located in Capital cities or areas of heavy population. Location is driven by proximity to cable infrastructure, good quality power connection capacity and the availability of skilled labour. Property rental cost is a disadvantage but so far has not been the major driver. 

For a mega (100 MW and bigger) datacentre the power cost and the availability of cable infrastructure and the land and facility cost become more important. Also cooling becomes a bigger deal.

In the USA some large data centres are located regionally. This appears to be for access to power and cheap land as much as for any other reason. ChatGPT summarised it thus:

> "These massive facilities (20-100+ MW) prioritize low operating costs and scalability. Cheap power is paramount, making remote locations near renewable energy sources attractive. AI training workloads can be located "where people are scarce but energy is plentiful" since latency isn't critical. Companies like Meta and Google built in rural Pacific Northwest for cheap hydro power and cool climate."

This to my mind suggests that if an entity wanted to build a mega centre in Australia that there may be reasons to locate it close to cheap power. It's much easier to bring the fibre optic cable to the datacentre than power transmission.

## Existing data centres are mostly in Capital Cities but also in Canberra

My point is if you can make a data centre in Canberra work surely you can also make one work in the Riverina. I put a little dashboard together based on digging round but as usual I'd not guarantee the accuracy. I am not a data centre expert by any means. 

![data centre locations. Source:web](../media/image-20250709154849387.png)

Looking at the detailed tables NextDC plans a 300 MW site in Sydney and is building a 150 MW site in [Melbourne](https://www.nextdc.com/news/nextdc-announces-2-billion-ai-factory-and-technology-campus-at-fishermans-bend). The Melbourne site will be using Nvidia Blackwell chips and water cooling. All I can say is good luck with the power cost when Yallourn closes and someone is picking up the offshore wind tab. Why not build it in the Riverina right next to the generation?



![Tier IV centres. Source:web](../media/image-20250709155215426.png)

## It's a sin to waste the Riverina potential

Equally the Riverina has a potential ability to generate far more power and energy than there is transmission to move it.

To get a sense of the geography I of course turn to www.renewmap.com.au a tool as transformative in its way in this sector as AI. Well perhaps that gilds the lily but it's pretty useful.

![SW REZ. Source:www.renewmap.com.au](../media/image-20250708105245192.png)

In the map there are about 10 GW of mostly wind projects, mostly with high quality developers and owners capable of financing the projects and to date with a community that can see the benefits as well as the cost.

Despite having Project Energy Connect (PEC), eventually VNI West and the PEC to Humelink connection there isn't nearly enough transmission capacity to move even half that power. I've already written that in my view it's not too late to make the Western Renewables Link and VNI West larger and to use the Riverina as  a cheaper source of power for Victorians than the likely excessively expensive offshore wind, but Victoria is not for changing.

So it seems to me the only way to get more use of the relatively cheap wind resource is to bring the load to the power.

A data centre located around say the Dinawan wind farm site (near the Dinawan substation) would be about 2 hours from Wagga airport.

## Delivered power cost maybe A\$107/MWh

Wind in the region likely costs around A$100/MWh at the wind site with a  capacity factor of say 40%. Solar capacity factors are also likely to be good maybe 25%. Firming power would be taken from the grid. Maybe you need a battery to act as a buffer. 

Experience is showing that LLMs doing training can suddenly stop even if only briefly basically because their information input needs to be coordinated and there is a coordination issue. So the grid can experience an immediate, no warning, loss of load. As in examples, like transmission failure or a coal generator tripping, a battery acts as a shock absorber. Such a battery may be necessary no matter where a datacentre of 100 MW or larger is located.

In this exercise I took the wind and solar traces from the 2024 ISP. However the Riverina wind trace comes to a capacity factor of 28%. It's widely believed that this is an underestimate given higher hub heights and the flat terrain, which means few wind obstructions. So I gross up the wind capacity factor to 39% by multiplying the half hourly traces by a scaling factor. This retains all the variability but lifts the mean. 39% is high by the standards of operating wind farms but they are impacted by economic and network curtailment. The whole idea of taking load to generation is to minimise curtailment and transmission costs.

Given the wind and solar output I did an  optimisation to find the combination of wind and solar which would deliver on average 100 MW. **That turned out to require 280 MW (198 MW wind and 83 MW solar)** for a minimum variance portfolio if it was coming from the one REZ



![solar wind trade. Source:ITK](../media/image-20250709125711025.png)

![100MW average production. Source:ITK](../media/image-20250709125907945.png)

The next step was to look at the actual half hourly traces of wind and solar using the ISP 11 reference years and assigning LCOEs to wind and solar, the cost of purchased electricity when there is a short fall and the price received for excess generation when there is a surplus. In this limited desktop study I came up with about $107/MWh as shown in the following waterfall chart.

![weighted average cost electricity in Riverina, 100 MW flat load. Source:ITK](../media/image-20250709130123407.png)

In this exercise no allowance is made for transmission other than the transmission cost implied in buying power from the grid for \$140/MWh. If you look at the over the day average output you can see that the short fall tends to occur in the evening peak and so the cost of buying power then may well be over \$140/MWh and therefore you might have a case for adding a battery into the mix. The battery would earn a return by storing excess power to minimise grid purchases and maybe getting a better price than \$70 for sales to the grid. I haven't done that analysis. Additionally the battery provides some insurance capability and acts as discussed earlier as a buffer. Because of this secondary role I might prefer a 100 MW /1 hour battery rather than a 25 MW/4 hour battery. Again that's separate analysis.

I don't really know that much about exactly how all these factors work together in determining where to build a data centre but I do think you could get a relatively cheap by global standards price. After all that's about US\$70 /MWh. New combined cycle gas generation in the USA has a capital cost of US\$2-\$2.5 m/MW and the gas isn't free and the capacity factor isn't 100% and you still have to back it up.

You would have to factor in the cost of getting the fibre optical cable there, but according to the research I read, latency in a data centre particularly an LLM style one is not a deal breaker.

## LLM research

ITK used ChatGPT's research tools to prepare 

1.  [report](https://itkservices3.com/background/subsea_cables.html) on subsea optical cable connections and capacity
2. [report](https://itkservices3.com/background/datacentre_locationfactors.html) on data centre location factors in particular why some mega centres are located remotely but most centres are located around or in capital cities 

I am no expert on data centres so these reports should be treated with caution. However I did verify some content from the references provided and I'm satisfied that for a brief on the topics they are ok



![Illustration](../media/image-20250709174704767.png)
