# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_19:59:42_UTC-green)

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

**Latest saved flight:** 2026-06-12 19:59:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-12 19:59:42 UTC

- **108,970** saved flights
- **38,128** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **108,970** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,332,299.4 tonnes** estimated CO2 emissions
- **77,234,745 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4483 |
| 2 | SkyWest Airlines | 4081 |
| 3 | IndiGo | 2151 |
| 4 | EJA | 2101 |
| 5 | American Airlines | 1726 |
| 6 | Southwest Airlines | 1635 |
| 7 | ENY | 1356 |
| 8 | Delta Air Lines | 1290 |
| 9 | Lufthansa | 1236 |
| 10 | Vueling | 1000 |
| 11 | LATAM Airlines | 966 |
| 12 | WIF | 959 |
| 13 | AXM | 926 |
| 14 | AZU | 896 |
| 15 | LXJ | 826 |
| 16 | Swiss International | 790 |
| 17 | All Nippon Airways | 757 |
| 18 | Alaska Airlines | 744 |
| 19 | QLK | 723 |
| 20 | easyJet | 701 |
| 21 | EJU | 694 |
| 22 | Cathay Pacific | 654 |
| 23 | AEE | 619 |
| 24 | VIV | 618 |
| 25 | Air France | 613 |
| 26 | United Airlines | 603 |
| 27 | MXY | 585 |
| 28 | CXK | 573 |
| 29 | Japan Airlines | 537 |
| 30 | AXB | 536 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 91760 |
| 2 | 🇪🇸 ES | 7484 |
| 3 | 🇮🇳 IN | 6782 |
| 4 | 🇦🇺 AU | 6512 |
| 5 | 🇧🇷 BR | 6010 |
| 6 | 🇩🇪 DE | 5845 |
| 7 | 🇮🇹 IT | 5817 |
| 8 | 🇨🇦 CA | 5721 |
| 9 | 🇯🇵 JP | 4953 |
| 10 | 🇬🇧 GB | 4625 |
| 11 | 🇫🇷 FR | 4331 |
| 12 | 🇨🇴 CO | 3750 |
| 13 | 🇲🇽 MX | 3264 |
| 14 | 🇬🇷 GR | 3088 |
| 15 | 🇳🇴 NO | 3016 |
| 16 | 🇨🇭 CH | 2773 |
| 17 | 🇲🇾 MY | 2371 |
| 18 | 🇹🇷 TR | 2132 |
| 19 | 🇿🇦 ZA | 1861 |
| 20 | 🇰🇷 KR | 1818 |
| 21 | 🇳🇿 NZ | 1796 |
| 22 | 🇹🇭 TH | 1792 |
| 23 | 🇵🇱 PL | 1788 |
| 24 | 🇵🇭 PH | 1597 |
| 25 | 🇬🇹 GT | 1564 |
| 26 | 🇲🇦 MA | 1197 |
| 27 | 🇲🇴 MO | 1145 |
| 28 | 🇳🇱 NL | 1074 |
| 29 | 🇲🇪 ME | 1052 |
| 30 | 🇭🇷 HR | 953 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2341 |
| 2 | Denver International Airport |  | US | 1842 |
| 3 | Tokyo International Airport |  | JP | 1640 |
| 4 | Indira Gandhi International Airport |  | IN | 1476 |
| 5 | Guaymaral Airport |  | CO | 1385 |
| 6 | Harry Reid International Airport |  | US | 1385 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1360 |
| 8 | Zurich Airport |  | CH | 1232 |
| 9 | Frankfurt am Main International Airport |  | DE | 1217 |
| 10 | La Aurora Airport |  | GT | 1204 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1168 |
| 12 | Macau International Airport |  | MO | 1145 |
| 13 | El Dorado International Airport |  | CO | 1133 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1092 |
| 15 | Chicago O'Hare International Airport |  | US | 1084 |
| 16 | Madrid Barajas International Airport |  | ES | 950 |
| 17 | Capua Airport |  | IT | 934 |
| 18 | Kuala Lumpur International Airport |  | MY | 930 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 925 |
| 20 | Salt Lake City International Airport |  | US | 923 |
| 21 | Charlotte/Douglas International Airport |  | US | 842 |
| 22 | Congonhas Airport |  | BR | 831 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 830 |
| 24 | Charles de Gaulle International Airport |  | FR | 820 |
| 25 | Bengaluru International Airport |  | IN | 819 |
| 26 | Malpensa International Airport |  | IT | 800 |
| 27 | Ninoy Aquino International Airport |  | PH | 734 |
| 28 | Daniel K Inouye International Airport |  | US | 731 |
| 29 | Tenerife Norte Airport |  | ES | 727 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 718 |
| 31 | Barcelona International Airport |  | ES | 716 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 708 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 701 |
| 34 | Amsterdam Airport Schiphol |  | NL | 664 |
| 35 | Don Mueang International Airport |  | TH | 655 |
| 36 | Vitoria/Foronda Airport |  | ES | 648 |
| 37 | Calgary International Airport |  | CA | 642 |
| 38 | Seattle-Tacoma International Airport |  | US | 626 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 625 |
| 40 | Viracopos International Airport |  | BR | 616 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 574 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 399 | 21m | 244 km | 1,680.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 292 | 24m | 225 km | 1,132.8 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 283 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 264 | 1h 25m | 910 km | 4,142.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 253 | 1h 10m | 770 km | 3,360.9 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 223 | 19m | 165 km | 634.3 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 218 | 26m | 275 km | 1,033.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 208 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 160 | 22m | 55 km | 152.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 158 | 27m | 215 km | 585.2 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 152 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 151 | 27m | 152 km | 394.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 148 | 31m | 369 km | 942.1 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 141 | 18m | 144 km | 350.7 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 140 | 20m | 250 km | 604.7 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 132 | 1h 1m | 695 km | 1,582.3 t |
| 25 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 132 | 44m | 241 km | 548.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 129 | 1h 43m | 1,423 km | 3,165.9 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 29 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 122 | 1h 2m | 611 km | 1,286.7 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N8034Z |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-06-12 19:41 UTC | 2026-06-12 19:59 UTC | 18m |
| N350KA |  | Van Nuys Airport (KVNY) | Meadows Field (KBFL) | 2026-06-12 19:26 UTC | 2026-06-12 19:55 UTC | 29m |
| N465CW |  | Frontier Airpark (WN53) | Arlington Municipal Airport (KAWO) | 2026-06-12 18:53 UTC | 2026-06-12 19:48 UTC | 55m |
| N70727 |  | John Wayne/Orange County Airport (KSNA) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-06-12 19:07 UTC | 2026-06-12 19:45 UTC | 38m |
| N928KE |  | CL35 (CL35) | Banning Municipal Airport (KBNG) | 2026-06-12 18:34 UTC | 2026-06-12 19:44 UTC | 1h 9m |
| N4922D |  | San Bernardino International Airport (KSBD) | Hemet-Ryan Airport (KHMT) | 2026-06-12 19:19 UTC | 2026-06-12 19:43 UTC | 23m |
| N609TS |  | Platteville Municipal Airport (KPVB) | Platteville Municipal Airport (KPVB) | 2026-06-12 19:29 UTC | 2026-06-12 19:35 UTC | 6m |
| N4953G |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-06-12 19:21 UTC | 2026-06-12 19:34 UTC | 13m |
| N926EN |  | St Louis Regional Airport (KALN) | Prairie Airport (83IS) | 2026-06-12 19:08 UTC | 2026-06-12 19:33 UTC | 25m |
| N565HT |  | Waterbury-Oxford Airport (KOXC) | Laguardia Airport (KLGA) | 2026-06-12 19:07 UTC | 2026-06-12 19:33 UTC | 26m |
| N300ZT |  | La Aurora Airport (MGGT) | Santa Cruz del Quiche Airport (MGQC) | 2026-06-12 19:13 UTC | 2026-06-12 19:31 UTC | 17m |
| N3739W |  | Lincoln Regional/Karl Harder Field (KLHM) | Sacramento Mather Airport (KMHR) | 2026-06-12 19:18 UTC | 2026-06-12 19:30 UTC | 12m |
| N1221S |  | 9LL0 (9LL0) | 23IS (23IS) | 2026-06-12 19:18 UTC | 2026-06-12 19:29 UTC | 10m |
| N83FE |  | Humphreys County Airport (K0M5) | Humphreys County Airport (K0M5) | 2026-06-12 18:58 UTC | 2026-06-12 19:29 UTC | 30m |
| N217MJ |  | Aurora State Airport (KUAO) | Chiloquin State Airport (K2S7) | 2026-06-12 18:54 UTC | 2026-06-12 19:25 UTC | 30m |
| HK5463X |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-12 19:06 UTC | 2026-06-12 19:23 UTC | 17m |
| N5161U |  | Brown Field Municipal Airport (KSDM) | General Abelardo L. Rodriguez International Airport (MMTJ) | 2026-06-12 19:03 UTC | 2026-06-12 19:23 UTC | 20m |
| N565TA |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-12 19:01 UTC | 2026-06-12 19:23 UTC | 21m |
| N972PA |  | Mc Clellan-Palomar Airport (KCRQ) | Hemet-Ryan Airport (KHMT) | 2026-06-12 18:41 UTC | 2026-06-12 19:23 UTC | 42m |
| N619AG |  | City Of Colorado Springs Municipal Airport (KCOS) | Limon Municipal Airport (KLIC) | 2026-06-12 18:53 UTC | 2026-06-12 19:21 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
