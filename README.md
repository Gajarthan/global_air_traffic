# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_17:30:51_UTC-green)

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

**Latest saved flight:** 2026-08-09 17:30:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 17:30:51 UTC

- **181,861** saved flights
- **58,072** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **181,861** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,185,741.5 tonnes** estimated CO2 emissions
- **126,709,655 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7213 |
| 2 | SkyWest Airlines | 6602 |
| 3 | EJA | 3575 |
| 4 | IndiGo | 3192 |
| 5 | Southwest Airlines | 2851 |
| 6 | American Airlines | 2829 |
| 7 | ENY | 2262 |
| 8 | Delta Air Lines | 2149 |
| 9 | LATAM Airlines | 1699 |
| 10 | AZU | 1628 |
| 11 | Lufthansa | 1617 |
| 12 | WIF | 1506 |
| 13 | Vueling | 1505 |
| 14 | LXJ | 1417 |
| 15 | Swiss International | 1247 |
| 16 | easyJet | 1245 |
| 17 | AXM | 1226 |
| 18 | EJU | 1116 |
| 19 | QLK | 1116 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 1000 |
| 23 | GLO | 974 |
| 24 | AEE | 949 |
| 25 | CXK | 949 |
| 26 | Cathay Pacific | 947 |
| 27 | Air France | 945 |
| 28 | United Airlines | 931 |
| 29 | PGT | 920 |
| 30 | MXY | 909 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 155438 |
| 2 | 🇪🇸 ES | 11715 |
| 3 | 🇧🇷 BR | 10441 |
| 4 | 🇦🇺 AU | 10203 |
| 5 | 🇮🇳 IN | 10004 |
| 6 | 🇨🇦 CA | 9888 |
| 7 | 🇮🇹 IT | 9419 |
| 8 | 🇩🇪 DE | 9025 |
| 9 | 🇬🇧 GB | 8416 |
| 10 | 🇯🇵 JP | 7379 |
| 11 | 🇫🇷 FR | 7265 |
| 12 | 🇨🇴 CO | 6759 |
| 13 | 🇬🇷 GR | 5335 |
| 14 | 🇲🇽 MX | 5189 |
| 15 | 🇨🇭 CH | 4862 |
| 16 | 🇹🇷 TR | 4709 |
| 17 | 🇳🇴 NO | 4686 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3058 |
| 20 | 🇿🇦 ZA | 3019 |
| 21 | 🇹🇭 TH | 2804 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2410 |
| 24 | 🇬🇹 GT | 2318 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1840 |
| 27 | 🇭🇷 HR | 1813 |
| 28 | 🇲🇪 ME | 1647 |
| 29 | 🇳🇱 NL | 1636 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3757 |
| 2 | Denver International Airport |  | US | 2999 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2235 |
| 5 | Guaymaral Airport |  | CO | 2231 |
| 6 | Harry Reid International Airport |  | US | 2130 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1958 |
| 8 | Zurich Airport |  | CH | 1942 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1884 |
| 10 | La Aurora Airport |  | GT | 1779 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1653 |
| 12 | Chicago O'Hare International Airport |  | US | 1631 |
| 13 | El Dorado International Airport |  | CO | 1623 |
| 14 | Salt Lake City International Airport |  | US | 1618 |
| 15 | Frankfurt am Main International Airport |  | DE | 1584 |
| 16 | Macau International Airport |  | MO | 1518 |
| 17 | Congonhas Airport |  | BR | 1515 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1442 |
| 19 | Madrid Barajas International Airport |  | ES | 1433 |
| 20 | Capua Airport |  | IT | 1424 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1357 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1299 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1255 |
| 25 | Charles de Gaulle International Airport |  | FR | 1242 |
| 26 | Charlotte/Douglas International Airport |  | US | 1229 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1187 |
| 29 | Ninoy Aquino International Airport |  | PH | 1135 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1129 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1110 |
| 32 | Barcelona International Airport |  | ES | 1080 |
| 33 | Viracopos International Airport |  | BR | 1046 |
| 34 | Seattle-Tacoma International Airport |  | US | 1044 |
| 35 | Daniel K Inouye International Airport |  | US | 1042 |
| 36 | Reno/Tahoe International Airport |  | US | 1039 |
| 37 | Calgary International Airport |  | CA | 1030 |
| 38 | Oslo Gardermoen Airport |  | NO | 1009 |
| 39 | Tenerife Norte Airport |  | ES | 994 |
| 40 | Vitoria/Foronda Airport |  | ES | 987 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 920 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 670 | 21m | 244 km | 2,821.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 420 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 256 | 1h 48m | 1,423 km | 6,282.6 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 247 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 243 | 20m | 250 km | 1,049.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 230 | 26m | 215 km | 851.8 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 229 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 223 | 19m | 99 km | 382.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 221 | 1h 15m | 961 km | 3,663.2 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 218 | 19m | 144 km | 542.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 215 | 1h 38m | 1,156 km | 4,289.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 213 | 24m | 218 km | 802.5 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 204 | 28m | 152 km | 533.1 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N63TP |  | Martha's Vineyard Airport (KMVY) | Teterboro Airport (KTEB) | 2026-08-09 16:45 UTC | 2026-08-09 17:30 UTC | 45m |
| CAN31 | CAN | Malpensa International Airport (LIMC) | Calcinate Del Pesce Airport (LILC) | 2026-08-09 16:54 UTC | 2026-08-09 17:27 UTC | 33m |
| N9GM |  | Peter O Knight Airport (KTPF) | 6FD7 (6FD7) | 2026-08-09 17:09 UTC | 2026-08-09 17:24 UTC | 14m |
| N156U |  | Logan-Cache Airport (KLGU) | Holyoak Airport (UT29) | 2026-08-09 16:40 UTC | 2026-08-09 17:18 UTC | 37m |
| GRDWN | GRD | Lydd Airport (EGMD) | Southampton Airport (EGHI) | 2026-08-09 16:34 UTC | 2026-08-09 17:15 UTC | 40m |
| PROFH | PRO | SBMM (SBMM) | SBMM (SBMM) | 2026-08-09 16:58 UTC | 2026-08-09 17:15 UTC | 16m |
| N245DJ |  | Moffett Federal Airfield (KNUQ) | Redding Regional Airport (KRDD) | 2026-08-09 16:32 UTC | 2026-08-09 17:14 UTC | 42m |
| CFBNK | CFB | Leask Airport (CJH8) | Radisson Airport (CJL9) | 2026-08-09 15:52 UTC | 2026-08-09 17:12 UTC | 1h 20m |
| AEE866 | AEE | Eleftherios Venizelos International Airport (LGAV) | Václav Havel Airport (LKPR) | 2026-08-09 13:52 UTC | 2026-08-09 17:11 UTC | 3h 18m |
| N135RF |  | 48CN (48CN) | Lee Vining Airport (KO24) | 2026-08-09 14:45 UTC | 2026-08-09 17:10 UTC | 2h 25m |
| AA1TB |  | Boise Air Trml/Gowen Field (KBOI) | Tracy Ranch Airport (ID88) | 2026-08-09 15:52 UTC | 2026-08-09 17:10 UTC | 1h 17m |
| EAI73V | EAI | Inverness Airport (EGPE) | Dublin Airport (EIDW) | 2026-08-09 15:56 UTC | 2026-08-09 17:07 UTC | 1h 11m |
| NSZ4502 | NSZ | Munich International Airport (EDDM) | Stockholm-Arlanda Airport (ESSA) | 2026-08-09 15:22 UTC | 2026-08-09 17:07 UTC | 1h 44m |
| N63VB |  | Stockton Metro Airport (KSCK) | Livermore Municipal Airport (KLVK) | 2026-08-09 16:18 UTC | 2026-08-09 17:04 UTC | 46m |
| N53BA |  | Hickory Regional Airport (KHKY) | NC87 (NC87) | 2026-08-09 16:16 UTC | 2026-08-09 17:04 UTC | 48m |
| N123PD |  | Shannon Airport (EINN) | Bangor International Airport (KBGR) | 2026-08-09 11:05 UTC | 2026-08-09 17:02 UTC | 5h 57m |
| DHCCF | DHC | La Mole Airport (LFTZ) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-09 16:21 UTC | 2026-08-09 17:00 UTC | 39m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-09 16:43 UTC | 2026-08-09 16:59 UTC | 16m |
| PROOT | PRO | SBMM (SBMM) | SBMM (SBMM) | 2026-08-09 16:52 UTC | 2026-08-09 16:59 UTC | 7m |
| LIFELN1 | LIF | Kellogg Airstrip (2CD9) | Northern Colorado Regional Airport (KFNL) | 2026-08-09 16:46 UTC | 2026-08-09 16:57 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
