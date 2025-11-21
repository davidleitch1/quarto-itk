## Electricity prices will likely be less volatile than expected post coal closures  under a plausible storage buildout

Future Energy^[Disclosure: I am a Director of Future Energy] has developed software to forecast spot market electricity prices on a half hourly basis 2026-2040. We built a dispatch engine complete with major constraints and taking a set of supply inputs by fuel class and year and then  runs a linear program to solve for half hourly prices across the NEM.

In contrast to text book approaches which identify the next marginal unit of supply and gradually build capacity in that way Future Energy's supply is external to the model and is essentially a spread sheet of annual capacit installed. Our fuel classes include coal, open and combined cycle gas, short and longer duration batteries, long duration storage, onshore and offshore wind, rooftop and utility solar.

Our demand profiles are taken from AEMO models but modified, mostly to remove the bulk of hydrogen demand, but also a slower pace of electrification.

We used the ISP as a point of departure for our supply assumptions. We also rely on AEMO for our half hourly forecasts of wind and solar output.  AEMO provides those forecasts for every REZ and provides enough data for us to model good (lots of wind and sun) and bad weather outcomes.

## What the spot market will look like in a post coal world 

For the longest time I have had a view that as the share of wind and solar increases price volatility would increase and that this would result in missing revenue for wind and solar. Either prices would be very low when the wind and solar share was high or the price would be low when there was no wind and solar and dispatchible resources, essentially hydro, gas and storage, 

Future Energy's model is good at capturing volatility. As such we are able to see how much of the average flat load price, and note its flat load not time weighted, is due to price spikes. As readers will know over the past couple of years the average price has been heavily influenced by very high prices which might happen less than 1% of the time and in contrast to the relatively small effect of negative prices even though they can occur upto 30% of all half hours in a year.

In our view its not just wind and solar variability that is responsible for price spikes but there is an influence of market structure and our software actually doesn't explicitly manage this parameter, but we do expect that renewable energy including storage is actually less easy to oligopolise (a new verb for us) than assets like coal and gas.

What we find is that, once sufficient storage is in place and its bidding reflects rational profit-maximising behaviour, both average prices and volatility seem to be manageable.

On an annual basis for this particular run and weather reference year what we see is that average annual price varies from \$120 to \$85 
![image-20251112102051514](../media/image-20251112102051514.png)

Monthly volatility does increase but not in a way that drives average prices up.
![image-20251109120233415](../media/image-20251109120233415.png)



Bidding behaviour of variable energy drives off peak prices and helps with annual prices. If price spikes are manageable thanks to sufficiently storage then the overall average flat load price is also steady. Even so there may be good opportunities for scarcity assets to earn returns, driving down the average spike price and its duration even further than shown above.

However different weather reference years could easily produce "spikier" results, driving up average prices in that particular year.

The software makes it easy for us and for other users to see what is driving prices for any given time frame.

![image-20251106134613587](../media/image-20251106134613587.png)

## Capacity driven by wind, solar, and batteries

In the case of NSW the assumption is basically the build out of the REZs. We installed capacity into the REZs in roughly the same proportion as in AEMO's ISP does, but the total installed capacity represents our own forecast. Of course these forecasts are reviewed regularly and equally you need to take a view on whether we really are going to decarbonise electricity and how long it will take.



![image-20251106151342719](../media/image-20251106151342719.png)

In this introductory piece I don't show demand but obviously to the extent that demand is stronger or lesser than our forecast so supply will change. The supply above is enough to keep prices significantly lower in real terms than today's prices and still cater for 30% increase in underlying demand.

## Its hard for every fuel to make a return

An almost universal finding of the many variations of  our forecasts is that utility solar typically struggles to earn its WACC.  Clearly we are in a position today in 2025 where prices are often negative in the middle of the day. This indicates that right now there is no marginal value for more solar MW of capacity. This could change if must run thermal capacity was reduced, and it is being reduced in NSW and in South Australia and to a lesser extent in other States, or if demand increases during solar production hours, and specifically if more storage is built.

In practice though increases in behind the meter solar as well as new solar built promoted under the CIS or other State based schemes mean that a solar surplus is likely to continue. In a simple marginal value expansion model, new solar wouldn't be built until it is forecast to earn a return. However in Future Energy's model we expect that some production won't earn a return from the spot market but will instead get the support from eg the CIS. Were offshore wind to built in Victoria its exactly the same. Once built the wind would contribute to supply and tend to result in lower spot prices but consumers end up paying via taxes or Govt borrowing costs.

## Expectations, risk analysis, policy modelling, volatility studies

Our software produces firstly the prices that we actually expect to eventuate on a flat load, time weighted and fuel dispatched weighted basis.

Secondly we can look at the risk to our forecasts. That risk falls in three main areas (1) Different capacity assumptions, eg slow coal, high solar etc. Of course it's not just a matter of changing numbers in the spreadsheet because (2) the dispatch model itself has risk that we increasingly understand and (3) Capacity costs. We model different scenarios but each new scenario, if its significantly different, is a lot of work.

For instance what if there was a storage class, an alternative to open cycle gas, that simply didn't dispatch unless spot prices were over \$1000/MWh. Could it earn WACC, what would be the optimal duration?

Thirdly we think our software is useful to storage investors and traders. However in saying that we don't model FCAS revenues at all.

Fourthly we can identify the value of constraint relief, at least for the main constraints that drive the major changes in value for consumers and producers.

Fifthly because we focus on the future rather than the past we like to think that our analysis perspective is deeply grounded. And if anyone was to ask, we give a generous benefit of the doubt in our work to renewable energy based on, and I paraphrase an investments market dictum "If something should happen it probably will". Notwithstanding a very stop start renewables industry in Australia we do now already get over 50%. Will the next 50% be as hard or take as long as the first 50%? That's not our belief but we'd be happy to model a slow change for you. 

Of course we are a tiny team and to model and understand change takes time and skill.

## Model efficiency and VRE focus

Our model currently runs a half-hourly price forecast for years 2026-2040 using a single weather reference year on a consumer-grade laptop in under 1 minute. Runtime is drastically reduced on a commercial system. Essentially a scencario can be modelled across all weather years in a time that allows multiple scenarios to be tested over a day. The model can display prices for any chosen weather reference year, allowing comparison of interval and average prices across periods of high and low renewable generation. This provides deeper insight into how weather-driven variability affects market volatility.
