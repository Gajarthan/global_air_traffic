# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_00:20:16_UTC-green)

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

**Latest saved flight:** 2026-08-07 00:20:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 00:20:16 UTC

- **174,387** saved flights
- **56,436** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **174,387** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,099,482.6 tonnes** estimated CO2 emissions
- **121,709,136 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6910 |
| 2 | SkyWest Airlines | 6389 |
| 3 | EJA | 3457 |
| 4 | IndiGo | 3047 |
| 5 | Southwest Airlines | 2753 |
| 6 | American Airlines | 2733 |
| 7 | ENY | 2173 |
| 8 | Delta Air Lines | 2066 |
| 9 | LATAM Airlines | 1615 |
| 10 | Lufthansa | 1577 |
| 11 | AZU | 1542 |
| 12 | WIF | 1461 |
| 13 | Vueling | 1431 |
| 14 | LXJ | 1367 |
| 15 | AXM | 1190 |
| 16 | Swiss International | 1186 |
| 17 | easyJet | 1183 |
| 18 | QLK | 1065 |
| 19 | EJU | 1064 |
| 20 | All Nippon Airways | 1060 |
| 21 | Alaska Airlines | 1059 |
| 22 | VIV | 960 |
| 23 | Cathay Pacific | 943 |
| 24 | CXK | 926 |
| 25 | GLO | 921 |
| 26 | AEE | 909 |
| 27 | United Airlines | 905 |
| 28 | Air France | 893 |
| 29 | MXY | 882 |
| 30 | JetBlue | 869 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 150219 |
| 2 | 🇪🇸 ES | 11139 |
| 3 | 🇧🇷 BR | 9941 |
| 4 | 🇦🇺 AU | 9797 |
| 5 | 🇮🇳 IN | 9563 |
| 6 | 🇨🇦 CA | 9551 |
| 7 | 🇮🇹 IT | 8985 |
| 8 | 🇩🇪 DE | 8630 |
| 9 | 🇬🇧 GB | 8065 |
| 10 | 🇯🇵 JP | 7014 |
| 11 | 🇫🇷 FR | 6910 |
| 12 | 🇨🇴 CO | 6419 |
| 13 | 🇬🇷 GR | 5057 |
| 14 | 🇲🇽 MX | 4989 |
| 15 | 🇨🇭 CH | 4600 |
| 16 | 🇳🇴 NO | 4542 |
| 17 | 🇹🇷 TR | 4274 |
| 18 | 🇲🇾 MY | 3093 |
| 19 | 🇵🇱 PL | 2912 |
| 20 | 🇿🇦 ZA | 2808 |
| 21 | 🇹🇭 TH | 2562 |
| 22 | 🇳🇿 NZ | 2533 |
| 23 | 🇵🇭 PH | 2300 |
| 24 | 🇬🇹 GT | 2223 |
| 25 | 🇰🇷 KR | 2192 |
| 26 | 🇲🇦 MA | 1752 |
| 27 | 🇭🇷 HR | 1687 |
| 28 | 🇲🇪 ME | 1593 |
| 29 | 🇳🇱 NL | 1571 |
| 30 | 🇲🇴 MO | 1503 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3604 |
| 2 | Denver International Airport |  | US | 2891 |
| 3 | Tokyo International Airport |  | JP | 2191 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2127 |
| 6 | Harry Reid International Airport |  | US | 2086 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1891 |
| 8 | Zurich Airport |  | CH | 1845 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1828 |
| 10 | La Aurora Airport |  | GT | 1712 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1605 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1576 |
| 14 | Salt Lake City International Airport |  | US | 1564 |
| 15 | Frankfurt am Main International Airport |  | DE | 1541 |
| 16 | Macau International Airport |  | MO | 1503 |
| 17 | Congonhas Airport |  | BR | 1439 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1421 |
| 19 | Capua Airport |  | IT | 1358 |
| 20 | Madrid Barajas International Airport |  | ES | 1356 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1306 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1231 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1217 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Charles de Gaulle International Airport |  | FR | 1181 |
| 26 | Malpensa International Airport |  | IT | 1179 |
| 27 | Kuala Lumpur International Airport |  | MY | 1166 |
| 28 | Bengaluru International Airport |  | IN | 1135 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1083 |
| 30 | Ninoy Aquino International Airport |  | PH | 1082 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1076 |
| 32 | Barcelona International Airport |  | ES | 1028 |
| 33 | Daniel K Inouye International Airport |  | US | 1004 |
| 34 | Seattle-Tacoma International Airport |  | US | 1004 |
| 35 | Calgary International Airport |  | CA | 991 |
| 36 | Reno/Tahoe International Airport |  | US | 990 |
| 37 | Viracopos International Airport |  | BR | 989 |
| 38 | Oslo Gardermoen Airport |  | NO | 970 |
| 39 | Tenerife Norte Airport |  | ES | 963 |
| 40 | Scottsdale Airport |  | US | 946 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 636 | 21m | 244 km | 2,678.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 411 | 24m | 225 km | 1,594.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 396 | 1h 8m | 770 km | 5,260.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 321 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 294 | 27m | 275 km | 1,393.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 262 | 22m | 55 km | 249.0 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 262 | 44m | 241 km | 1,088.3 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 239 | 1h 48m | 1,423 km | 5,865.4 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 225 | 20m | 250 km | 971.9 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 223 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 213 | 20m | 99 km | 364.9 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 207 | 19m | 144 km | 514.9 t |
| 24 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 206 | 8m | - | - |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 203 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 202 | 1h 38m | 1,156 km | 4,029.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 202 | 31m | 369 km | 1,285.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 195 | 24m | 218 km | 734.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 190 | 43m | 452 km | 1,480.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N8385Q |  | Buffalo Municipal Airport (KCFE) | St Paul Downtown Holman Field (KSTP) | 2026-08-07 00:02 UTC | 2026-08-07 00:20 UTC | 17m |
| GH11 |  | San Clemente Island Nalf Airport (KNUC) | CA84 (CA84) | 2026-08-06 23:13 UTC | 2026-08-07 00:15 UTC | 1h 2m |
| RFS731 | RFS | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-08-06 23:54 UTC | 2026-08-07 00:13 UTC | 19m |
| ZKHVH | ZKH | Invercargill Airport (NZNV) | Invercargill Airport (NZNV) | 2026-08-07 00:02 UTC | 2026-08-07 00:13 UTC | 10m |
| ADI | ADI | Adelaide Parafield Airport (YPPF) | Adelaide Parafield Airport (YPPF) | 2026-08-06 23:52 UTC | 2026-08-07 00:12 UTC | 20m |
| N901VU |  | Humphreys County Airport (K0M5) | John C Tune Airport (KJWN) | 2026-08-06 23:43 UTC | 2026-08-07 00:05 UTC | 21m |
| HER13 | HER | Woodbourne Airport (NZWB) | Wellington International Airport (NZWN) | 2026-08-06 23:45 UTC | 2026-08-07 00:03 UTC | 18m |
| N472LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Bob Hope Airport (KBUR) | 2026-08-06 22:49 UTC | 2026-08-07 00:02 UTC | 1h 13m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-06 23:33 UTC | 2026-08-07 00:02 UTC | 28m |
| YNR | YNR | Adelaide Parafield Airport (YPPF) | Adelaide Parafield Airport (YPPF) | 2026-08-06 23:51 UTC | 2026-08-07 00:02 UTC | 10m |
| KXL | KXL | Moree Airport (YMOR) | South Grafton Airport (YSGR) | 2026-08-06 23:34 UTC | 2026-08-07 00:00 UTC | 26m |
| TBL3 | TBL | Lake Tahoe Airport (KTVL) | Henderson Executive Airport (KHND) | 2026-08-06 23:08 UTC | 2026-08-07 00:00 UTC | 52m |
| AEE930 | AEE | Eleftherios Venizelos International Airport (LGAV) | HE42 (HE42) | 2026-08-06 22:28 UTC | 2026-08-06 23:52 UTC | 1h 23m |
| N855AV |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-08-06 23:24 UTC | 2026-08-06 23:51 UTC | 26m |
| N3772M |  | Ionia County Airport (KY70) | Minikey Airport (MI13) | 2026-08-06 23:41 UTC | 2026-08-06 23:48 UTC | 7m |
| N471TM |  | Platteville Municipal Airport (KPVB) | Platteville Municipal Airport (KPVB) | 2026-08-06 23:38 UTC | 2026-08-06 23:47 UTC | 8m |
| DLH584 | Lufthansa | Frankfurt am Main International Airport (EDDF) | HE12 (HE12) | 2026-08-06 20:18 UTC | 2026-08-06 23:45 UTC | 3h 26m |
| ZFH | ZFH | Bacchus Marsh Airport (YBSS) | Melbourne Moorabbin Airport (YMMB) | 2026-08-06 23:20 UTC | 2026-08-06 23:43 UTC | 23m |
| N76WA |  | 3WA1 (3WA1) | 3WA1 (3WA1) | 2026-08-06 22:21 UTC | 2026-08-06 23:43 UTC | 1h 21m |
| N256AA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-06 22:56 UTC | 2026-08-06 23:43 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
