# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_01:40:28_UTC-green)

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

**Latest saved flight:** 2026-09-26 01:40:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-26 01:40:28 UTC

- **269,714** saved flights
- **79,078** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **269,714** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,271,994.8 tonnes** estimated CO2 emissions
- **189,680,857 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10614 |
| 2 | SkyWest Airlines | 9389 |
| 3 | EJA | 5273 |
| 4 | IndiGo | 4513 |
| 5 | American Airlines | 4195 |
| 6 | Southwest Airlines | 3968 |
| 7 | Delta Air Lines | 3355 |
| 8 | ENY | 3169 |
| 9 | LATAM Airlines | 2600 |
| 10 | AZU | 2527 |
| 11 | Vueling | 2246 |
| 12 | WIF | 2196 |
| 13 | LXJ | 2118 |
| 14 | Lufthansa | 2047 |
| 15 | easyJet | 1808 |
| 16 | Swiss International | 1766 |
| 17 | QLK | 1738 |
| 18 | EJU | 1690 |
| 19 | AXM | 1674 |
| 20 | United Airlines | 1652 |
| 21 | Alaska Airlines | 1591 |
| 22 | All Nippon Airways | 1550 |
| 23 | PGT | 1518 |
| 24 | WMT | 1504 |
| 25 | GLO | 1502 |
| 26 | Air France | 1481 |
| 27 | VIV | 1471 |
| 28 | Wizz Air | 1464 |
| 29 | CXK | 1324 |
| 30 | AEE | 1294 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 224673 |
| 2 | 🇪🇸 ES | 16896 |
| 3 | 🇧🇷 BR | 15772 |
| 4 | 🇦🇺 AU | 15516 |
| 5 | 🇨🇦 CA | 15043 |
| 6 | 🇮🇹 IT | 14591 |
| 7 | 🇮🇳 IN | 14267 |
| 8 | 🇩🇪 DE | 12930 |
| 9 | 🇬🇧 GB | 12478 |
| 10 | 🇨🇴 CO | 12365 |
| 11 | 🇫🇷 FR | 10719 |
| 12 | 🇯🇵 JP | 10358 |
| 13 | 🇹🇷 TR | 8165 |
| 14 | 🇬🇷 GR | 7786 |
| 15 | 🇲🇽 MX | 7442 |
| 16 | 🇨🇭 CH | 7159 |
| 17 | 🇳🇴 NO | 6672 |
| 18 | 🇹🇭 TH | 4818 |
| 19 | 🇲🇾 MY | 4527 |
| 20 | 🇿🇦 ZA | 4498 |
| 21 | 🇵🇱 PL | 4411 |
| 22 | 🇳🇿 NZ | 3782 |
| 23 | 🇵🇭 PH | 3576 |
| 24 | 🇬🇹 GT | 3414 |
| 25 | 🇭🇷 HR | 3070 |
| 26 | 🇰🇷 KR | 3046 |
| 27 | 🇲🇦 MA | 2683 |
| 28 | 🇲🇪 ME | 2526 |
| 29 | 🇳🇱 NL | 2406 |
| 30 | 🇮🇩 ID | 2245 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5492 |
| 2 | Denver International Airport |  | US | 4388 |
| 3 | Indira Gandhi International Airport |  | IN | 3226 |
| 4 | Tokyo International Airport |  | JP | 3100 |
| 5 | El Dorado International Airport |  | CO | 2926 |
| 6 | Harry Reid International Airport |  | US | 2894 |
| 7 | Guaymaral Airport |  | CO | 2817 |
| 8 | Zurich Airport |  | CH | 2793 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2712 |
| 10 | La Aurora Airport |  | GT | 2595 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2594 |
| 12 | Salt Lake City International Airport |  | US | 2379 |
| 13 | Chicago O'Hare International Airport |  | US | 2305 |
| 14 | Congonhas Airport |  | BR | 2299 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2208 |
| 16 | Capua Airport |  | IT | 2094 |
| 17 | Madrid Barajas International Airport |  | ES | 2077 |
| 18 | Frankfurt am Main International Airport |  | DE | 2044 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2039 |
| 20 | Malpensa International Airport |  | IT | 1930 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1925 |
| 22 | Charles de Gaulle International Airport |  | FR | 1914 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1892 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1887 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1823 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1755 |
| 28 | Charlotte/Douglas International Airport |  | US | 1688 |
| 29 | Barcelona International Airport |  | ES | 1677 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1673 |
| 31 | Viracopos International Airport |  | BR | 1628 |
| 32 | Kuala Lumpur International Airport |  | MY | 1621 |
| 33 | Seattle-Tacoma International Airport |  | US | 1582 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1578 |
| 35 | Calgary International Airport |  | CA | 1538 |
| 36 | Don Mueang International Airport |  | TH | 1526 |
| 37 | Bengaluru International Airport |  | IN | 1519 |
| 38 | Oslo Gardermoen Airport |  | NO | 1512 |
| 39 | Vancouver International Airport |  | CA | 1509 |
| 40 | Antalya International Airport |  | TR | 1439 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1122 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1010 | 21m | 244 km | 4,252.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 744 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 680 | 1h 6m | 770 km | 9,033.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 673 | 24m | 225 km | 2,610.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 600 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 445 | 44m | 555 km | 4,261.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 432 | 27m | 275 km | 2,047.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 426 | 1h 50m | 1,423 km | 10,454.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 411 | 44m | 241 km | 1,707.2 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 385 | 24m | 218 km | 1,450.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 364 | 21m | 250 km | 1,572.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 362 | 23m | 55 km | 344.1 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 344 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 341 | 1h 6m | 706 km | 4,151.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 339 | 19m | 99 km | 580.7 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 314 | 19m | 144 km | 781.1 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 295 | 42m | 535 km | 2,724.5 t |
| 26 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 292 | 18m | 14 km | 73.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N52678 |  | Merrill Field (PAMR) | Talkeetna Airport (PATK) | 2026-09-26 00:56 UTC | 2026-09-26 01:40 UTC | 43m |
| N681DC |  | Palo Alto Airport (KPAO) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-09-26 01:10 UTC | 2026-09-26 01:24 UTC | 14m |
|  |  | CA75 (CA75) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-26 01:00 UTC | 2026-09-26 01:23 UTC | 23m |
| AFL2138 | AFL | Dubai International Airport (OMDB) | Istanbul Airport (LTFM) | 2026-09-25 12:38 UTC | 2026-09-26 01:20 UTC | 12h 42m |
| YMV | YMV | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-09-26 01:00 UTC | 2026-09-26 01:19 UTC | 18m |
| LBQ825 | LBQ | Reading Regional/Carl A Spaatz Field (KRDG) | Raleigh-Durham International Airport (KRDU) | 2026-09-25 23:54 UTC | 2026-09-26 01:18 UTC | 1h 24m |
| AAL2387 | American Airlines | San Francisco International Airport (KSFO) | Dallas-Fort Worth International Airport (KDFW) | 2026-09-25 21:47 UTC | 2026-09-26 01:16 UTC | 3h 28m |
| N302TP |  | Tulsa International Airport (KTUL) | Tulsa International Airport (KTUL) | 2026-09-26 00:57 UTC | 2026-09-26 01:13 UTC | 16m |
| N405MK |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-09-26 00:20 UTC | 2026-09-26 01:13 UTC | 52m |
| N697AM |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-09-26 00:59 UTC | 2026-09-26 01:05 UTC | 6m |
| DAL1661 | Delta Air Lines | Portland International Airport (KPDX) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-09-25 22:08 UTC | 2026-09-26 01:04 UTC | 2h 56m |
| NTR232 | NTR | Faa'a International Airport (NTAA) | Tikehau Airport (NTGC) | 2026-09-26 00:18 UTC | 2026-09-26 01:02 UTC | 43m |
| ERU852 | ERU | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-09-26 00:35 UTC | 2026-09-26 01:01 UTC | 26m |
| N36PJ |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-09-26 00:26 UTC | 2026-09-26 01:01 UTC | 35m |
| BRG652 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-09-26 00:31 UTC | 2026-09-26 00:58 UTC | 27m |
| N315WP |  | Sherman Municipal Airport (KSWI) | Aero Country Airport (KT31) | 2026-09-26 00:45 UTC | 2026-09-26 00:54 UTC | 8m |
| JST771 | JST | Adelaide International Airport (YPAD) | Melbourne International Airport (YMML) | 2026-09-25 23:37 UTC | 2026-09-26 00:54 UTC | 1h 17m |
| CGSSC | CGS | Nanaimo Airport (CYCD) | Vancouver International Airport (CYVR) | 2026-09-26 00:38 UTC | 2026-09-26 00:53 UTC | 14m |
| SKW5697 | SkyWest Airlines | Denver International Airport (KDEN) | Lake County Airport (KLXV) | 2026-09-26 00:31 UTC | 2026-09-26 00:51 UTC | 20m |
| N814SS |  | Nikolai Creek Airport (9AK3) | Trading Bay Production Airport (5AK0) | 2026-09-26 00:23 UTC | 2026-09-26 00:50 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
