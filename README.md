# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_18:03:27_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-09-29 18:03:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-29 18:03:27 UTC

- **272,457** saved flights
- **79,632** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **272,457** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,301,382.2 tonnes** estimated CO2 emissions
- **191,384,476 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10715 |
| 2 | SkyWest Airlines | 9490 |
| 3 | EJA | 5337 |
| 4 | IndiGo | 4551 |
| 5 | American Airlines | 4227 |
| 6 | Southwest Airlines | 4010 |
| 7 | Delta Air Lines | 3388 |
| 8 | ENY | 3198 |
| 9 | LATAM Airlines | 2630 |
| 10 | AZU | 2559 |
| 11 | Vueling | 2265 |
| 12 | WIF | 2217 |
| 13 | LXJ | 2147 |
| 14 | Lufthansa | 2060 |
| 15 | easyJet | 1820 |
| 16 | Swiss International | 1783 |
| 17 | QLK | 1755 |
| 18 | EJU | 1702 |
| 19 | AXM | 1679 |
| 20 | United Airlines | 1666 |
| 21 | Alaska Airlines | 1606 |
| 22 | All Nippon Airways | 1561 |
| 23 | PGT | 1538 |
| 24 | GLO | 1521 |
| 25 | WMT | 1517 |
| 26 | Air France | 1499 |
| 27 | VIV | 1493 |
| 28 | Wizz Air | 1480 |
| 29 | CXK | 1345 |
| 30 | AEE | 1304 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 227080 |
| 2 | 🇪🇸 ES | 17052 |
| 3 | 🇧🇷 BR | 15987 |
| 4 | 🇦🇺 AU | 15688 |
| 5 | 🇨🇦 CA | 15180 |
| 6 | 🇮🇹 IT | 14715 |
| 7 | 🇮🇳 IN | 14401 |
| 8 | 🇩🇪 DE | 13058 |
| 9 | 🇬🇧 GB | 12582 |
| 10 | 🇨🇴 CO | 12550 |
| 11 | 🇫🇷 FR | 10818 |
| 12 | 🇯🇵 JP | 10420 |
| 13 | 🇹🇷 TR | 8260 |
| 14 | 🇬🇷 GR | 7853 |
| 15 | 🇲🇽 MX | 7528 |
| 16 | 🇨🇭 CH | 7242 |
| 17 | 🇳🇴 NO | 6728 |
| 18 | 🇹🇭 TH | 4879 |
| 19 | 🇲🇾 MY | 4549 |
| 20 | 🇿🇦 ZA | 4537 |
| 21 | 🇵🇱 PL | 4463 |
| 22 | 🇳🇿 NZ | 3833 |
| 23 | 🇵🇭 PH | 3597 |
| 24 | 🇬🇹 GT | 3426 |
| 25 | 🇭🇷 HR | 3103 |
| 26 | 🇰🇷 KR | 3074 |
| 27 | 🇲🇦 MA | 2700 |
| 28 | 🇲🇪 ME | 2554 |
| 29 | 🇳🇱 NL | 2445 |
| 30 | 🇮🇩 ID | 2264 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5547 |
| 2 | Denver International Airport |  | US | 4439 |
| 3 | Indira Gandhi International Airport |  | IN | 3254 |
| 4 | Tokyo International Airport |  | JP | 3121 |
| 5 | El Dorado International Airport |  | CO | 2986 |
| 6 | Harry Reid International Airport |  | US | 2926 |
| 7 | Guaymaral Airport |  | CO | 2828 |
| 8 | Zurich Airport |  | CH | 2826 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2733 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2614 |
| 11 | La Aurora Airport |  | GT | 2604 |
| 12 | Salt Lake City International Airport |  | US | 2416 |
| 13 | Congonhas Airport |  | BR | 2325 |
| 14 | Chicago O'Hare International Airport |  | US | 2316 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2231 |
| 16 | Capua Airport |  | IT | 2107 |
| 17 | Madrid Barajas International Airport |  | ES | 2098 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2067 |
| 19 | Frankfurt am Main International Airport |  | DE | 2056 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1935 |
| 21 | Charles de Gaulle International Airport |  | FR | 1935 |
| 22 | Malpensa International Airport |  | IT | 1934 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1926 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1906 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1828 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1767 |
| 28 | Charlotte/Douglas International Airport |  | US | 1704 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1696 |
| 30 | Barcelona International Airport |  | ES | 1685 |
| 31 | Viracopos International Airport |  | BR | 1637 |
| 32 | Kuala Lumpur International Airport |  | MY | 1630 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1599 |
| 34 | Seattle-Tacoma International Airport |  | US | 1596 |
| 35 | Calgary International Airport |  | CA | 1548 |
| 36 | Don Mueang International Airport |  | TH | 1543 |
| 37 | Bengaluru International Airport |  | IN | 1530 |
| 38 | Oslo Gardermoen Airport |  | NO | 1527 |
| 39 | Vancouver International Airport |  | CA | 1523 |
| 40 | Reno/Tahoe International Airport |  | US | 1464 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1125 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1022 | 21m | 244 km | 4,303.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 756 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 686 | 1h 6m | 770 km | 9,113.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 682 | 24m | 225 km | 2,645.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 456 | 44m | 555 km | 4,366.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 438 | 27m | 275 km | 2,075.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 431 | 1h 50m | 1,423 km | 10,577.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 418 | 44m | 241 km | 1,736.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 391 | 24m | 218 km | 1,473.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 379 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 369 | 21m | 250 km | 1,593.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 365 | 23m | 55 km | 346.9 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 349 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 345 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 337 | 26m | 215 km | 1,248.1 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 317 | 19m | 144 km | 788.5 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 308 | 1h 14m | 961 km | 5,105.3 t |
| 24 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 303 | 18m | 14 km | 75.8 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 302 | 42m | 535 km | 2,789.2 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 295 | 1h 50m | 1,304 km | 6,636.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AIC4218 | Air India | Dubai International Airport (OMDB) | Pune Airport (VAPO) | 2026-09-29 15:13 UTC | 2026-09-29 18:03 UTC | 2h 49m |
| N814U |  | Flying W Airport (KN14) | Flying W Airport (KN14) | 2026-09-29 17:51 UTC | 2026-09-29 18:02 UTC | 11m |
| HBZYW | HBZ | Wangen-Lachen Airport (LSPV) | Zurich Airport (LSZH) | 2026-09-29 17:44 UTC | 2026-09-29 18:01 UTC | 16m |
| CGMEC | CGM | Prince George Airport (CYXS) | Prince George Airport (CYXS) | 2026-09-29 17:35 UTC | 2026-09-29 17:55 UTC | 20m |
| N3023T |  | Sebastian Municipal Airport (KX26) | Sebastian Municipal Airport (KX26) | 2026-09-29 17:32 UTC | 2026-09-29 17:53 UTC | 20m |
| SHA227 | SHA | Tribhuvan International Airport (VNKT) | Langtang Airport (VNLT) | 2026-09-29 15:15 UTC | 2026-09-29 17:52 UTC | 2h 37m |
| N403TD |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-09-29 17:33 UTC | 2026-09-29 17:51 UTC | 18m |
| N18841 |  | K4A7 (K4A7) | K4A7 (K4A7) | 2026-09-29 17:27 UTC | 2026-09-29 17:43 UTC | 15m |
| ASP869 | ASP | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Toronto Pearson International Airport (CYYZ) | 2026-09-29 16:56 UTC | 2026-09-29 17:42 UTC | 46m |
| N488GB |  | 2OL2 (2OL2) | Russellville Regional Airport (KRUE) | 2026-09-29 17:20 UTC | 2026-09-29 17:40 UTC | 19m |
| N670PC |  | Gillespie Field (KSEE) | On The Rocks Airport (1CA6) | 2026-09-29 17:19 UTC | 2026-09-29 17:39 UTC | 20m |
| N113FD |  | Mc Clellan Airfield (KMCC) | Bacchi Valley Industries Airport (80CA) | 2026-09-29 17:24 UTC | 2026-09-29 17:36 UTC | 12m |
| N7580 |  | Glendale Regional Airport (KGEU) | AZ86 (AZ86) | 2026-09-29 17:07 UTC | 2026-09-29 17:35 UTC | 28m |
| CXK169 | CXK | Columbus Municipal Airport (KBAK) | Columbus Municipal Airport (KBAK) | 2026-09-29 17:30 UTC | 2026-09-29 17:33 UTC | 2m |
| N7317 |  | Abbotsford Airport (CYXX) | Fort St. John Airport (CYXJ) | 2026-09-29 16:15 UTC | 2026-09-29 17:33 UTC | 1h 17m |
| N51216 |  | CA84 (CA84) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-29 17:21 UTC | 2026-09-29 17:31 UTC | 10m |
| N383AA |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-09-29 17:12 UTC | 2026-09-29 17:28 UTC | 15m |
| N2464H |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-09-29 17:01 UTC | 2026-09-29 17:26 UTC | 24m |
| OXF6250 | OXF | Falcon Field (KFFZ) | Montezuma Airport (19AZ) | 2026-09-29 16:44 UTC | 2026-09-29 17:25 UTC | 40m |
| OXF4955 | OXF | Falcon Field (KFFZ) | Rimrock Airport (48AZ) | 2026-09-29 16:44 UTC | 2026-09-29 17:24 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
