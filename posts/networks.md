---
title: "It is still wires and poles"
author: "David Leitch"
date: "2025-03-24"
categories: [analysis, networks]
image: "../media/image-20250322151955794.png"
lightbox: true
format:
  html:
    include-after-body:
       - "../comment_load.html"
  docx: default
draft: false
---



#  Its still not clear where networks will get volume growth

Recently chatting on an EnergyInsiders podcast I felt like I didn't know what I was talking about. Its not an uncommon feeling and although its hard to do on a podcast when in a hole, stop digging.

Afterwards I felt it was time to do some revision on the numbers. After running the numbers I'm still not sure who it was who  didn't know what they were talking about. However I learned that despite a lot of practice I still make mistakes when asking questions and getting questions in the right order.

Ausgrid, and I presume Essential and Endeavour don't disclose their financial result. Makes me grumpy. These are very substantial businesses.  Ausgrid's market capitalisation, if it was listed, would be probably 30%-50% higher than that of AGL but likely still below Origin. Ausgrid's enterprise value  (equity + debt) would make it the biggest individual electricity business in Australia if Energex and Ergon its two Qld cousins are counted separately.

Ausgrid is largely owned by Australians. The NSW Govt retains 49.6%, IFM has 25.2% and AusSuper 8.4%. But as usual neither the NSW Govt or big Super funds feel any need to disclose anything.   Over the last  20 years the NSW Govt's disclosures around its electricity assets  have been abysmal but at least the generators used to release annual reports. Aus Super I think is far too big for its boots. I l started distrusting them when they took advice from Frontier Economics during the Origin takeover. Aus Super probably has as much invested in Australian electricity as the next super fund but from what I can gather couldn't give a rats about decarbonisation. Future generations be dammed. REST on the other hand has put \$1 bn into Quinbrook. Anyhow I'll leave it to the likes of Anne Lampe to talk about Superfunds. My point is that the only reason we know anything about Ausgrid's performance at an asset level is because its regulated. And because its regulated we see AER deliberations and the AER requires annual RIN spreadsheets to be submitted. over the 20 years I've looked at them

There is a lot of data in the spreadsheets and even a nerd like me cant be bothered with all of it. Still I downloaded spread sheets for 13 network business, for the years FY19 to FY24 and started extracting a few numbers. Despite the AER's best efforts there is a bit of data cleansing to do. Ausnet has about 4 different names and upper and lower case spelling across its different spreadsheets and years. So when you try to write some Python to read it all in, it isn't straight forward (That's code for saying I might have made some mistakes). Use at your own risk and check for yourself.

For about 20 years I have been amazed, whether looking at gas or electricity networks, to see that volume never changes but the regulated asset base (RAB) goes up every year and so mostly does revenue. That's why investors have historically loved these businesses. You get a 99 year lease with a guaranteed return. Often you can juice the return a bit. These assets are not as good as tollroads or airports. The latter are the creme de creme. With tollroads you get a toll increase typically the higher of inflation or x% where x = say 4% and the volume grows every year.  Over 24 years the Citylink toll tripled, a compound growth rate of 4.6%.  Even gas  prices haven't done much better. Leaves humble electricity back at the starter's gun. However the toll road franchise does't last as long as electricity networks.

As a result when the owner of one of these network  assets sells the asset,  they expect to get a price in excess of what the regulator values the asset at. The regulator allows a "fair" return on the asset. If the regulators return were too high the asset would be worth more than its regulated value and vice versa. And the prima facie evidence is the regulator does allow too high a return. Like with banks I do believe its in the best interests of Australians that returns be a bit on the high side. We are better off with well financed stress free assets. For the alternate view see Healthscope. Still there are limits.

Over many years investors have consistently valued these wires and poles networks at a 20%-40% premium. This premium is expressed in value:rab ratio which  is typically around 1.4. But actually in that scenario investors are paying more like 100% premium for the equity as compared to equity value from the regulator's perspective.



![Source:ITK](../media/image-20250322143500463.png)

So actually the equity does carry a risk. The equity will generally always be at least the regulated value but the premium is a matter of valuation opinion, the familiar willing buyer/willing seller scenario.

## Lets look at the data.

Assuming for the moment that I did the calculations correctly, please check, then I get the following overall summary of the sector.



![RAB indicators, Data:RIN disclosures](../media/image-20250322143947973.png)

This well illustrates what I said at the beginning. The regulated asset value increases through heaven, hell and high water. Volumes rarely if ever move. Revenue went down, because of lower inflation and interest rates operating with a decent lag and revenue (prices) is now well on the growth path.

When you think about it 25% overall sector growth in RAB, that is the value of the assets adjusted for inflation, capex and depreciation, it's  nothing short of incredible. Leaving inflation aside the main source of growth is new connections. And disaggregating RAB growth to show the individual franchises we can see its  regional Australia. Ergon (regional QLD)'s growth is astonishing. One might ask why hardworking South Eastern Queenslanders should continue to subsidise such a fast growing area. Anyway....



![RABs by network. Data:RIN disclosures](../media/image-20250322144530839.png)

Casually speaking QLD is growing faster than NSW and NSW is growing faster than Victoria or South Australia. 

The amount of RAB growth in regional Australia surprised me but more interesting was the energy volume split by customer class.



![Enegy deliveries. Data:RIN disclosures](../media/image-20250322144901044.png)

For residential the point is that the number of connected households has and will continue to grow. This means the network keeps investing in new connection wires and poles  which adds to the RAB but those customers then complain about high prices, get smart and add solar to their roofs and increasingly (20% of new solar customers last year) decide to whack a battery in as well. Those customers with solar and a battery don't use the grid that much. The average size of a new residential solar system is getting up to 10 kw. 

Once EVs become a real thing, that is there are enough of them to start ah driving overall grid economics, we will have to see what happens. More electricity will be consumed charging the EVs but customers, and I know some personally, will then decide lets put enough solar on so we can charge the car in the day. Those same customers would, if they could, happily run the house at night on the car battery. After all if you consume 10 kWh over night that's only a car battery discharge of say 15%. Easy to pick up the next day. So why do you need the grid? Why do you want to be part of a VPP? You live in your own happy place. Note that the plot below cannot be directly translated to utility supply to the household sector because some of what households consume will come from the next door neighbour's solar plant. Equally nor does it measure gross household consumption because some of that is solar self consumption. It measures volumes delivered by the distributors to residential customers no matter where sourced from. And it's declining which means that either prices have to go up or pricing has to be driven on a non volumetric basis. But customers, correctly in my view, hate demand charges.

![Residential customer evolution. Data:RIN disclosures](../media/image-20250322151955794.png)

On the other hand the growth of business volumes, which as a very, very broad statement have less opportunity to add solar, is the hope of networks. Business volumes, that is non residential, low voltage connections whether on a demand tariff or not, grow with population and the economic cycle. On balance they are likely to keep growing.  The same with industrial volumes.

## When distribution companies build overhead lines noone complains.

I'd have to dig deeper into the data, and it is available, to get the circuit km of overhead lines, but you can get the general picture by looking at the invested dollars by RAB category. The fastest growing category is overhead wires and transformers. There are two observations about this. (1) Voters don't care about overhead wires and poles when it's their house and community that ends up being connected. And of course most of this new overhead infrastructure is in regional/rural areas and (2) Overhead wires are much more subject to storm damage and interruptions generally, so the fact that we are still installing more overhead than underground infrastructure does tell you something about economics.

I mean in six years there is about \$6 bn of new overhead wires and poles without a single complaint I've read.

![RAB composition. Data:RIN disclosures](../media/image-20250323080227798.png)

## Batteries

Notwithstanding all the investment the broader media still don't pay enough attention to batteries. These days you don't hear idiotic comments like "South Australia's big battery can only  runs South Australia for 15 minutes". Those kind of comments always indicated a genuine or deliberate misunderstanding of the role of batteries. However battery belief has expanded so much that today almost anything seems possible. And that's despite a few fires. In fact I would argue that fires at utility batteries have been managed so well with the exception of "Moss Landing" its now consensus that they wont be a show stopper.

Everyone now understands that batteries are a prize worth fighting for.

As a reminder there are, right now, three main battery categories. Household/Vehicle, Community/Network, Utility. These categories are in a fight or a race which few fully appreciate. That is basically competition for the houshold sector's excess solar generation, and I guess we should include utility solar here as well.

Never mind frequency control, never mind seasonal storage, the battery game is pretty much about charging in the middle of the day and discharging in the evening and morning peaks, and if there is anything left over discharging through the night. To play in this game you want to charge at the lowest price possible. To my mind that gives two categories an advantage. If the rule makers, and arguably I would include AEMO and the outcome of the Nelson report as rule makers,  if the rule makers stay out of the way and let households control their own destiny then they will nearly always be able to charge their batteries from their own solar. And when they cant use their own solar, they can rely on simple tariff based software, such as that available from Evergen, to charge their batteries from the grid and what on average will be a cost effective time.

Secondly utility batteries that are connected whether AC or DC to their own solar farm will have a more or less guaranteed supply of daytime solar for charging.

Not making a big deal of it but community/network batteries will depend on network solar imports or buying from the grid to charge. There is a bit less certainty. 

Batteries have a big value stack and it's hard to get paid for all the services they provide. The  pathfinder study on batteries was written in 2015 the ["State of Charge"](https://www.mass.gov/info-details/energy-storage-study) for the State of Massachusetts..  That study was a model of clarity and we interviewed one of the study authors in a precursor to EnergyInsiders.  Early work in Ireland as discussed with Marek Kubik  showed some of the use case in practice. We can summarise the battery use cases into three categories, frequency control, network support and energy storage/trading. 

If you combine those services you can run your own grid. Household batteries demonstrate that at the household level. My Powerwall runs a phase of my house circuit to the point where I don't notice a blackout. Probably better designed inverters/software could run all three phases anyhow....

If a battery can run a house, it stands to reason that with a bit more frequency management a bigger battery can run a street, particularly if there is lots of solar in the street. Sophisticated software , infinitely beyond the capabilities of our wires and poles network should mean that the individual household batteries could combine and act as a street level battery, probably in an entirely autonomous fashion. As I say I have no doubts about the theoretical capability even though I have never seen it and no nothing about it. Anyhow...

In the absence of 21st century metering and software, and the debate about the economics of paying to develop such software is unthinkable, batteries installed at distribution or zone substations provide an alternative. So then it's about winners and losers. In my mind the argument is only partly about relative economics, and relative economics are a moveable feast. In my view policy makers would do well to avoid locking the system into one view of economics. John Pierce's "power of choice" metering policy was one of his dumber ideas but the idea of empowering consumers to make choices is one I generally support. We need to return to culture but, anyway....

The best information on network battery costs comes from the ARENA funding. Although this slide doesn't say it all and I'm not sure I agree with the conclusion. I didn't write it and the headline in big letters is fairly clear.



![Community batteries. Source: ARENA](../media/image-20250323110134945.png)

Why might the headline be wrong? The most likely reason is it's probably the first time networks have ever had to compete in the market. As regulated monopolies normally all they do is tell the regulator the capex is needed and go home to dinner. Now they are quelle horreur in competition with others. So in round 2 I expect networks to sharpen their pencils.

Another problem for the networks is that they haven't got a clue about demonstrating their value to the public.  I've already shown that big networks don't even disclose their financial results. So hiding stuff is how you build distrust. The early mantra of Macquarie bank was disclose everything.  Disclosure builds trust. Anyone who has ever been in a relationship understands that, maybe network owners dont have relationships. Anyhow...

So if they can't disclose financial results, can't provide a study showing that connecting a solar or wind farm at 133 kV to the distribution grid rather than the transmission grid results in better consumer outcomes, can't provide a study or evidence showing that community batteries provide better outcomes and lower total costs to consumers why should anyone believe them?

As Mark England points out in a forthcoming EnergyInsiders interview networks potentially have great relationships with consumers at the ground level. It's network operatives who maintain and fix the network and live in the community. A gentailer's relationship with a customer is through a call centre, the internet and a billing system. No humans required, I imagine that having AI run the call centre, chatbots anyone, is well in process.

But the benefits to networks of the community relationship become a distant dream as we move into the economics, the regulator, and the monopoly. 

And as the study above shows the cost per KWh in the above figure is typically well over \$1000\kWh which compares with recent average costs of \$600/kWh for utility batteries, and less than \$1000/kWh maybe much less  for household batteries, never mind car batteries. And with a household battery, speaking personally, I have control, I have blackout protection etc. I would need a big price discount to give up those advantages. 

So because networks are so bad at doing their own selling, not having any sales people other than to the regulator, ARENA is encouraging them:

![Networks need to communicate. Source:ARENA](../media/image-20250323094109096.png)

I expect the selling part to be at least as challenging as sharpening the pencil. And if I was ARENA I would have made it a criterion that winners commit to a well  published  demonstration of benefits rather than knowledge sharing, which noone but stakeholders ever looks at. The sort of webinar that a listed company or an Energyco runs. 

But the network industry is more interested in running a sailing regatta on Sydney Harbour. Anyway....

I put the following table together for battery location and ownership model considerations but really it's not a good effort and something I will revisit more thoroughly at a later point. Anyhow....

![Battery ownership models. Source:ITK](../media/image-20250323114242680.png)

