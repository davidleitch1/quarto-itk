# Diesel Electrification Note: Next Steps

## Completed sections

1. **Summary** — headline diesel budget framing
2. **Transport Emissions by Sub-Sector** — CCA 90 Mt breakdown (Table T.1)
3. **Road Transport Diesel: By Vehicle Type** — ABS SMVU 2020 full table
4. **Road Transport Diesel: By State** — ABS SMVU 2020 state breakdown
5. **Off-Road Diesel** — mining, agriculture, construction estimates
6. **Total Diesel Budget** — combined ~30 BL table
7. **Electrification Implications** — sector-by-sector framing
8. **Trucks: The Largest Road Diesel Consumer** — weight class + area of operation + electrification implications
9. **International Comparison** — China, EU, UK, Australia, Vietnam
10. **Charging Infrastructure for Heavy Trucks** — battery-swap vs MCS vs Tesla Megacharger vs Windrose
11. **Long-Haul Electric Trucks: The Contenders** — eActros 600, Volvo FH Aero/FH Electric, Scania R 450e, DAF, Windrose E1400, Tesla Semi, B-double problem
12. **Bus Kilometres by State** — ABS SMVU 2020
13. **Light Commercial Vehicles** — PHEV utes, BEV utes, electric vans (eSprinter, E-Transit, E-Transit Custom reviews), barriers, UK/EU as leading indicators, policy levers
14. **Data Gaps** — 8 items
15. **European sales: who is winning?** — EU ZE truck registrations 2025 rankings table (eActros 600 #1)

### Separate background documents
- **`etruck_economics.md`** — diesel consumption per km, electric equivalent kWh/km, operating cost $/km, payback periods for all 11 vehicle classes plus mining (Section 11). Includes summary table, diesel-to-electricity conversion analysis, policy prioritisation scorecard, and China NE commercial vehicle validation data.

## Remaining work

### Content gaps to fill
- ~~**Mining electrification**~~ — DONE, added as Section 11 to `etruck_economics.md`. Covers 9.6 BL diesel budget, equipment breakdown, BEV haul trucks (Cat 793 XE, Liebherr T 264, XCMG), trolley-assist, underground BEV (Sandvik, Epiroc), Australian deployments (Fortescue, BHP, Rio Tinto)
- **Agricultural electrification** — electric tractors (Monarch, John Deere SESAM), solar+battery for irrigation, timeline
- **Hydrogen vs battery for long-haul** — brief treatment of FCEV trucks (Hyundai XCIENT, Nikola Tre FCEV), likely role for road trains >100t
- **Policy comparison table** — Australia vs EU vs China vs US policy instruments side by side
- ~~**Policy prioritisation scorecard**~~ — DONE, added to `etruck_economics.md`

### Charts to create
- Treemap of 30 BL total diesel budget (already have PNG 1 from diesel_drilldown_charts.py)
- Truck diesel by weight class (already have PNG 2)
- Consider: stacked area chart of projected BEV truck share by segment to 2040

### Editorial
- Review all sections for consistent citation style
- Cross-check all numbers against primary sources
- Run through research-standards checklist
- Remove `draft: true` from YAML when ready to publish
