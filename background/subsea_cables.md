---
title: "Subsea cables"
author: "Leitch - ChatGPT"
date: "2025-07-6"
format: html
draft: false
category: "datacentres"
lightbox: true
---

## 




# **Australia’s Subsea Cable Connectivity Overview**

This report is from ChatGPT. Although I am not knowledgeable on the topic I have reviewed the article and checked out some of the sources. However there is no guaratee that either I or ChatGPT have identified the critical issues.

If you look at Google its servers can require hundreds of Terabits per second.

Hyperscale data centers have two distinct bandwidth needs:

1. **Internal (East–West) Capacity for Training**

   - Modern ML training jobs move massive datasets among thousands of servers. To support this, hyperscale centers deploy building-wide networks with **Petabits-per-second** aggregate bandwidth.
   - **Example**: Google’s “Jupiter” fabric within a single data center supports over **6 Pb/s** of aggregate bandwidth, using uniform 100 Gb/s–400 Gb/s links to tens of thousands of servers and optical circuit switching for non-blocking scale-out .

2. **External (North–South) Capacity for Inference & Delivery**

   - Outbound traffic (API responses, content delivery, model inference) relies on high-capacity fiber links to the internet and other regions. Hyperscale DCs therefore provision **tens to hundreds of Terabits per second** of lit fiber capacity.
   - **Google FASTER Cable (USA)**: At its Oregon landing site, Google has exclusive access to **100×100 Gb/s wavelengths** (one 100-strand for send, one for receive), yielding **10 Tb/s** per direction on the FASTER trans-Pacific cable to Japan .
   - Google Cloud’s private backbone uses over **3.2 million km** of terrestrial and subsea fiber, connecting its global regions with multi-Tb/s links .

   The Australian subsea capacity is over 350 Tbps which is enough for a mega datacentre on its own. But of course the capacity is required for more than datacentres.

   - **Aggregate International Capacity**

     The combined lit capacity of Australia’s major subsea cables exceeds 350 Tbps:

     - Southern Cross (92 Tbps) + Southern Cross NEXT (72 Tbps)
     - Australia–Singapore (60 Tbps)
     - Indigo West/Central (~36 Tbps) + Hawaiki (30 Tbps) + Oman–Australia (48 Tbps)
     - Other systems (AJC, JGA-S, SEA-ME-WE 3, PPC-1, Tasman Global, Coral Sea, Gondwana-1): aggregate ~60 Tbps.

     **Assessment:** Tens to hundreds of Tbps per DC is typical for hyperscale external links. Australia’s >350 Tbps international capacity provides ample headroom for a single hyperscale campus.

   - **Latency**

     - Sydney ↔ Los Angeles: ~70 ms one-way via Southern Cross NEXT (lowest-latency route)
     - Sydney ↔ Singapore: ~40 ms one-way via ASC/Indigo

     

     **Assessment:** These figures meet user-facing service requirements. New cables marginally reduce both latency and route variability.

   - **Domestic Backbone**

     

     - Current inter-capital traffic relies mainly on terrestrial links; subsea gaps create longer routes.
     - Planned East Coast Cable System (2025) and SMAP (2026) will add ~6,600 km of subsea links between Brisbane, Sydney, Melbourne, Adelaide, Perth, improving capacity and cutting domestic latency.

     

     **Assessment:** Upcoming domestic cables will support multi-site deployments and disaster-recovery architectures by lowering intra-Australia latency and adding redundancy.

   - **Future Growth**

     - Google-backed ACC1 (2027), Hawaiki Nui (2026), Google’s Bosun & West Australia Link, Tabua & Honomoana (2025–26) will further diversify routes and boost capacity.

     **Assessment:** Ongoing projects align with hyperscale growth needs, ensuring continuous capacity and resilience expansion.

### Capacity utilisation is not a barrier

Publicly disclosed, cable-specific utilization rates are rare. Operators treat usage data as proprietary. However, broad industry and related network figures provide useful benchmarks:

- **Global Averages (all routes):**

  TeleGeography reports that, in 2022, international long-haul networks ran at an **average utilization of 26%**, with **peak utilization of 44%** . While this covers all submarine routes worldwide, similar patterns typically apply to Australia’s major cables.

- **FASTER (Trans-Pacific, Google-owned):**

  At Google’s Oregon landing, FASTER is lit at **10 Tbps per direction** of a **60 Tbps design**. That implies **≈17%** utilization of its design capacity .

- **Indigo (Perth–Singapore & Perth–Sydney, AARNet spectrum):**

  AARNet trialled **400 Gbps** on Indigo’s 36 Tbps system (two fibre pairs each direction), indicating **<1.2%** utilization during the trial. AARNet describes this link as having “no congestion” and ample headroom for bursts .

- **Industry Commentary:**

  Analysts note that new or upgraded cables often operate at **20–30% average utilization**, with **peak loads up to 50–60%** on high-traffic routes before further capacity is lit .

**Conclusion:**

Even at peak periods, Australia’s major subsea cables typically run well below full capacity, leaving substantial headroom. This utilization profile supports the bandwidth demands of a hyperscale data center, both for training (east–west) and for north–south internet connectivity, provided operators continue lit-capacity upgrades in line with demand growth.

## **International Submarine Cable Systems**

- **Southern Cross Cable Network (SCCN)** – ~30,500 km dual-cable ring linking Sydney (NSW) to the U.S. via New Zealand, Fiji, and Hawaii. Currently lit at ~92 Tbps capacity ; a new **Southern Cross NEXT** branch (13,700 km) adds 72 Tbps and the lowest-latency path between Australia and Los Angeles . Owned by a consortium including Spark (NZ), Telstra, Singtel (Optus), and Verizon .
- **Australia-Japan Cable (AJC)** – 12,700 km cable connecting Sydney (Oxford Falls, NSW) to Japan via Guam. Initial design capacity was 320 Gbps  (since upgraded above 1 Tbps). It lands in Sydney and is owned by a telco consortium (Telstra, NTT, AT&T, Verizon/BT, SoftBank) .
- **Australia-Singapore Cable (ASC)** – 4,600 km fibre route from Perth (WA) to Singapore (via Christmas Island and Indonesia) . Consists of four fiber pairs and now delivers up to 60 Tbps of capacity after 2019–2020 upgrades . Owned and operated by Vocus (since 2018).
- **Indigo West & Central** – A two-part cable system (2019) jointly owned by Telstra, Google, Singtel, AARNet and others. **Indigo West** runs ~4,600 km from Perth to Singapore (via Jakarta), and **Indigo Central** runs 4,850 km from Perth to Sydney  . The open design with 2 fiber pairs per segment supports up to ~36 Tbps on each route . Indigo provides an alternate high-capacity, lower-latency path between Australia and Southeast Asia .
- **Hawaiki Cable** – ~15,000 km cable (RFS 2018) linking Sydney (landing in NSW) to the US West Coast via New Zealand, American Samoa, and Hawaii. Designed for ~30 Tbps capacity . Originally built by Hawaiki Submarine Cable LP, it was acquired by BW Digital in 2022.
- **Telstra Endeavour** – 9,125 km cable owned by Telstra, connecting Sydney to Hawaii. In service since 2008, it provides a direct trans-Pacific link with improved latency compared to older routes . Often used for additional US connectivity and diversity.
- **Japan–Guam–Australia South (JGA-S)** – 7,081 km system landing in Sydney (Brookvale, NSW) and Maroochydore (Queensland) and terminating in Guam . Co-owned by RTI, Google, and AARNet, JGA-S went live in 2020 to enhance Australia–Asia/U.S. connectivity. (Connects onward to Japan via a separate JGA-N segment.)
- **SEA-ME-WE 3** – A 39,000 km intercontinental cable (in service since 2000) linking Western Europe to Australia. It lands in Perth (WA) as the final leg of its route . This legacy system is consortially owned by 48 telecom operators (including Telstra and Optus)  and originally provided Australia’s first direct link to Southeast Asia and Europe.
- **Oman Australia Cable (OAC)** – 9,800 km new cable (launched Oct 2022) directly connecting Perth (WA) to Muscat, Oman (with branches to the Cocos (Keeling) Islands and Diego Garcia). It has 3 fiber pairs and was upgraded to a **total capacity of 48 Tbps** (initially lit with 39 Tbps) . Built by SUB.CO, OAC establishes the first express route from Australia to the Middle East/Europe, designed for high capacity and avoiding congested Asian waters .
- **PIPE Pacific Cable-1 (PPC-1)** – 6,900 km cable connecting Sydney to Guam with a spur to Papua New Guinea . Operational since 2009, it’s owned by TPG Telecom (Pipe Networks) and provides an additional route from Australia into East Asia and the trans-Pacific hub at Guam.
- **Tasman Global Access (TGA)** – 2,288 km subsea cable between Sydney (landing at Oxford Falls, NSW) and Raglan, New Zealand . Opened in 2017, it offers ~20 Tbps design capacity and is co-owned by Spark NZ, Telstra, and Vodafone. This augments the older **Southern Cross** Tasman link, reducing congestion on Australia–NZ traffic.
- **Other Regional Cables** – Australia also connects to its Pacific neighbors via dedicated cables. The **Coral Sea Cable System** (4,700 km, since 2019) links Sydney to Papua New Guinea and the Solomon Islands  (an Australian government-funded project for Pacific connectivity). The **Gondwana-1** cable (2,151 km, since 2008) connects Sydney to Nouméa, New Caledonia  (owned by OPT New Caledonia). These regional links, though smaller in length and capacity, are strategic for connecting nearby islands to Australia’s internet backbone.

## **Domestic Subsea Cables (Australia)**

While most domestic backbone connectivity is terrestrial, a few submarine cables link Australian regions and offshore territories:

- **Bass Strait Cables** – A pair of submarine fiber cables (~240 km each) connecting Tasmania to mainland Australia across Bass Strait. In service for over 20 years, they link Tasmanian networks to Victoria; both are Telstra-owned and run parallel paths . Additionally, the **Basslink Telecoms** cable (298 km) was deployed to provide alternate Tasmania–Victoria capacity .
- **North-West Cable System (NWCS)** – 2,100 km subsea cable linking Darwin (Northern Territory) to Port Hedland (WA) along Australia’s north-west shelf . Completed in 2016 by Vocus, it was built to serve remote mining/oil & gas regions. NWCS consists of 2 fiber pairs (currently 12 Tbps capacity)  and creates a high-capacity link from Darwin into the national network. (Vocus has since interconnected NWCS with ASC, enabling the first direct Darwin–Asia route .)
- **Domestic Coastal Systems** – To improve east-coast connectivity, Vocus is laying a new **East Coast Cable System** (planned for service in 2025) running ~1,600 km offshore between Brisbane, Sydney, and Melbourne . This festoon-style cable (up to 24 fiber pairs) will shorten inter-capital routes and add diversity versus land cables . Another project, **Sydney–Melbourne–Adelaide–Perth (SMAP)**, a 5,000 km subsea network linking four capitals, is slated for 2026  to bolster west-east links. (These initiatives aim to reduce latency and improve resiliency of Australia’s core domestic routes, which today rely on longer terrestrial paths .)

## **New and Upcoming Cable Projects**

Australia’s subsea connectivity is expanding with several new cables under construction or planning:

- **Asia Connect Cable-1 (ACC1)** – A 19,000 km Google-backed system (expected 2027) that will link Darwin (NT) northward through Indonesia, Timor-Leste, the Philippines and Singapore, and then across the Pacific to Hermosa Beach, California . This cable will establish a direct Darwin-to-US route via Southeast Asia, enhancing route diversity.
- **Hawaiki Nui** – A superscale ~25,000 km cable proposed by BW Digital (target service 2026) as a follow-on to Hawaiki. It plans multiple landings in Australia (four locations) and will connect to New Zealand, Indonesia, Singapore and the US, significantly increasing multi-route capacity in the region .
- **Google “Bosun” and West Australia Link** – Announced in late 2024, Google and partners (Vocus, SUB.CO, NextDC) are deploying two cables: **Bosun**, connecting Darwin to Christmas Island in the Indian Ocean, and a separate link from Melbourne to Perth, then up to Christmas Island and on to Singapore  . These systems will create new westward paths from Australia to Asia. Combined with associated Pacific projects (e.g. **Tabua** and **Honomoana** below), they form part of an integrated network spanning ~42,500 km from the US through Australia to Asia . The Australian government highlights that such projects will *“expand and strengthen the resilience”* of national connectivity via diversified routes .
- **Tabua Cable** – A new U.S.–Australia–Fiji cable led by Google and partners, due ~2025–26. It will land in Sydney and Fiji, providing another trans-Pacific path (complementing Southern Cross and Hawaiki) . In parallel, Google’s **Honomoana** cable (planned 2026) will link Australia to French Polynesia and then to the U.S. , further boosting South Pacific capacity.
- *Note:* These upcoming systems, along with smaller bilateral cables (e.g. a potential additional PNG-Australia link under discussion), are aimed at both increasing overall international bandwidth and improving network redundancy. They reflect collaboration between cloud providers and carriers to meet rising demand.



## **Capacity and Latency for Hyperscale Data Centers**

Australia’s international cable infrastructure now provides **signficiant aggregate capacity** and improved latency routes, critical for hyperscale data centers (the likes of AWS, Google, Microsoft, etc.). Modern high-bandwidth cables typically offer on the order of tens of terabits per second each – for example, the Perth–Singapore ASC system carries up to 60 Tbps , and the new trans-Pacific Southern Cross NEXT delivers 72 Tbps . With multiple systems in service, Australia has **substantial headroom** to handle hyper-scale cloud traffic. Industry experts note that recent investments focus on *“latency, diversity, resilience, and hyperscale capacity”* to satisfy cloud and content providers’ requirements . Indeed, content and cloud operators are the largest consumers of international bandwidth, and many have co-invested in these cables to secure capacity.



In terms of latency, physical distance remains the limiting factor. The fastest optical path from Sydney to Los Angeles (via Southern Cross) has a one-way latency of roughly 70 milliseconds  (around 140 ms round-trip). Routes to Asia are shorter (Sydney to Singapore is ~7,000 km, yielding ~40–50 ms one-way). Such latencies are largely dictated by fiber distance and cannot be fully eliminated. However, **new cables have shaved off latency** by more direct routing – for instance, Southern Cross NEXT offers the lowest latency between Australia and the U.S. by avoiding extra transit hops , and Vocus’s planned East Coast Cable will shorten Sydney–Brisbane/Melbourne paths . For hyperscale data centers, these latencies are generally acceptable for distributed operations (they align with physics-bound expectations), and the focus is on **mitigating variability and outages**.



Overall, Australia’s connectivity profile is significantly strengthened by the recent and forthcoming cable additions. The total international bandwidth into Australia has expanded dramatically (Southern Cross’s new cable alone increased transpacific capacity by 500% ), and multiple redundant links now exist on every major route. This growth in capacity and route diversity is viewed as a strategic asset: analysts suggest Australia is *“well positioned to secure its role as a regional digital hub”* for cloud and data traffic in the Indo-Pacific . In summary, current subsea infrastructure – combined with ongoing upgrades – is on track to support hyperscale data centres’ needs in Australia, providing high throughput and reasonable latency, **so long as continued investment maintains ahead-of-demand capacity and resiliency**.



------



**Key Sources:**

- Google Cloud Blog. “Jupiter Evolving: Reflecting on Google’s Data Center Network Transformation.” August 23, 2022. https://cloud.google.com/blog/topics/systems/the-evolution-of-googles-jupiter-data-center-network
- Alan Chin-Lun Cheung. “Google Cloud customers run at the speed of light with new FASTER undersea pipe.” June 29, 2016. https://cloud.google.com/blog/products/gcp/google-cloud-customers-run-at-the-speed-of-light-with-new-faster-undersea-pipe
- Google Cloud. “Global Locations – Regions & Zones.” https://cloud.google.com/about/locations/

- https://www.comparebroadband.com.au/broadband-articles/latest-news-id3/a-full-list-of-australia-s-underwater-cables-id738/
- https://www.interest.co.nz/technology/126212/new-data-cross-tasman-data-cable-land-invercargill
- https://www.itnews.com.au/news/oman-australia-cable-gets-extra-capacity-601127
- https://www.itnews.com.au/news/vocus-ready-for-project-highclere-cable-lay-585001
- https://www.reuters.com/technology/google-build-subsea-cable-linking-australias-darwin-christmas-island-2024-11-25/
- https://www.vocus.com.au/why-vocus/our-network-and-expertise/australia-singapore-cable
- https://www.capacitymedia.com/article/29ot42ikril15nn1ojseq/news/indigo-cable-goes-live-and-rfs