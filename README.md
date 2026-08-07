# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_06:27:54_UTC-green)

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

**Latest saved flight:** 2026-08-07 06:27:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 06:27:54 UTC

- **174,669** saved flights
- **56,489** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **174,669** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,101,918.1 tonnes** estimated CO2 emissions
- **121,850,324 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6914 |
| 2 | SkyWest Airlines | 6391 |
| 3 | EJA | 3458 |
| 4 | IndiGo | 3056 |
| 5 | Southwest Airlines | 2755 |
| 6 | American Airlines | 2735 |
| 7 | ENY | 2173 |
| 8 | Delta Air Lines | 2068 |
| 9 | LATAM Airlines | 1616 |
| 10 | Lufthansa | 1577 |
| 11 | AZU | 1544 |
| 12 | WIF | 1462 |
| 13 | Vueling | 1431 |
| 14 | LXJ | 1369 |
| 15 | AXM | 1191 |
| 16 | Swiss International | 1187 |
| 17 | easyJet | 1184 |
| 18 | QLK | 1072 |
| 19 | Alaska Airlines | 1065 |
| 20 | All Nippon Airways | 1064 |
| 21 | EJU | 1064 |
| 22 | VIV | 963 |
| 23 | Cathay Pacific | 943 |
| 24 | CXK | 927 |
| 25 | GLO | 921 |
| 26 | AEE | 912 |
| 27 | United Airlines | 907 |
| 28 | Air France | 893 |
| 29 | MXY | 882 |
| 30 | JetBlue | 869 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 150395 |
| 2 | 🇪🇸 ES | 11144 |
| 3 | 🇧🇷 BR | 9946 |
| 4 | 🇦🇺 AU | 9895 |
| 5 | 🇮🇳 IN | 9581 |
| 6 | 🇨🇦 CA | 9564 |
| 7 | 🇮🇹 IT | 8997 |
| 8 | 🇩🇪 DE | 8638 |
| 9 | 🇬🇧 GB | 8068 |
| 10 | 🇯🇵 JP | 7038 |
| 11 | 🇫🇷 FR | 6914 |
| 12 | 🇨🇴 CO | 6423 |
| 13 | 🇬🇷 GR | 5071 |
| 14 | 🇲🇽 MX | 5003 |
| 15 | 🇨🇭 CH | 4605 |
| 16 | 🇳🇴 NO | 4545 |
| 17 | 🇹🇷 TR | 4281 |
| 18 | 🇲🇾 MY | 3105 |
| 19 | 🇵🇱 PL | 2912 |
| 20 | 🇿🇦 ZA | 2816 |
| 21 | 🇹🇭 TH | 2582 |
| 22 | 🇳🇿 NZ | 2549 |
| 23 | 🇵🇭 PH | 2308 |
| 24 | 🇬🇹 GT | 2227 |
| 25 | 🇰🇷 KR | 2194 |
| 26 | 🇲🇦 MA | 1752 |
| 27 | 🇭🇷 HR | 1691 |
| 28 | 🇲🇪 ME | 1593 |
| 29 | 🇳🇱 NL | 1572 |
| 30 | 🇲🇴 MO | 1503 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3606 |
| 2 | Denver International Airport |  | US | 2891 |
| 3 | Tokyo International Airport |  | JP | 2198 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2130 |
| 6 | Harry Reid International Airport |  | US | 2089 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1897 |
| 8 | Zurich Airport |  | CH | 1846 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1829 |
| 10 | La Aurora Airport |  | GT | 1714 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1605 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1576 |
| 14 | Salt Lake City International Airport |  | US | 1565 |
| 15 | Frankfurt am Main International Airport |  | DE | 1542 |
| 16 | Macau International Airport |  | MO | 1503 |
| 17 | Congonhas Airport |  | BR | 1439 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1422 |
| 19 | Capua Airport |  | IT | 1362 |
| 20 | Madrid Barajas International Airport |  | ES | 1358 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1306 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1232 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1228 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Malpensa International Airport |  | IT | 1182 |
| 26 | Charles de Gaulle International Airport |  | FR | 1181 |
| 27 | Kuala Lumpur International Airport |  | MY | 1170 |
| 28 | Bengaluru International Airport |  | IN | 1139 |
| 29 | Ninoy Aquino International Airport |  | PH | 1087 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1083 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1079 |
| 32 | Barcelona International Airport |  | ES | 1029 |
| 33 | Daniel K Inouye International Airport |  | US | 1008 |
| 34 | Seattle-Tacoma International Airport |  | US | 1007 |
| 35 | Calgary International Airport |  | CA | 992 |
| 36 | Reno/Tahoe International Airport |  | US | 991 |
| 37 | Viracopos International Airport |  | BR | 990 |
| 38 | Oslo Gardermoen Airport |  | NO | 971 |
| 39 | Tenerife Norte Airport |  | ES | 963 |
| 40 | Scottsdale Airport |  | US | 947 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 640 | 21m | 244 km | 2,694.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 412 | 24m | 225 km | 1,598.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 399 | 1h 8m | 770 km | 5,300.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 322 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 294 | 27m | 275 km | 1,393.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 262 | 22m | 55 km | 249.0 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 262 | 44m | 241 km | 1,088.3 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 240 | 1h 48m | 1,423 km | 5,890.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 227 | 20m | 250 km | 980.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 223 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 215 | 20m | 99 km | 368.3 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 207 | 19m | 144 km | 514.9 t |
| 24 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 206 | 8m | - | - |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 205 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 203 | 1h 38m | 1,156 km | 4,049.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 202 | 31m | 369 km | 1,285.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 196 | 24m | 218 km | 738.4 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 190 | 43m | 452 km | 1,480.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FJJJY | FJJ | Saint-Nazaire-Montoir Airport (LFRZ) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-08-07 06:16 UTC | 2026-08-07 06:27 UTC | 11m |
| AEE932 | AEE | Eleftherios Venizelos International Airport (LGAV) | HE12 (HE12) | 2026-08-07 04:48 UTC | 2026-08-07 06:11 UTC | 1h 23m |
| SEJYV | SEJ | Raron Airport (LSTA) | Aosta Airport (LIMW) | 2026-08-07 05:27 UTC | 2026-08-07 06:10 UTC | 43m |
| N5427X |  | Ted Stevens Anchorage International Airport (PANC) | Beluga Airport (PABG) | 2026-08-07 05:47 UTC | 2026-08-07 06:07 UTC | 20m |
| ZKIDU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-08-07 05:56 UTC | 2026-08-07 05:58 UTC | 1m |
| HBLVB | HBL | Mollis Airport (LSZM) | Friedrichshafen Airport (EDNY) | 2026-08-07 04:21 UTC | 2026-08-07 05:53 UTC | 1h 32m |
| JMU | JMU | Ballarat Airport (YBLT) | Bamawm Airport (YBMM) | 2026-08-07 05:21 UTC | 2026-08-07 05:42 UTC | 20m |
| NIU | NIU | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-08-07 04:53 UTC | 2026-08-07 05:39 UTC | 45m |
| AEE348 | AEE | Eleftherios Venizelos International Airport (LGAV) | Kalymnos Airport (LGKY) | 2026-08-07 05:17 UTC | 2026-08-07 05:37 UTC | 20m |
| ZKIDH | ZKI | Invercargill Airport (NZNV) | Taieri Airport (NZTI) | 2026-08-07 04:46 UTC | 2026-08-07 05:37 UTC | 51m |
| VAA010 | VAA | Mukhrani Airport (UGMM) | UGMS (UGMS) | 2026-08-07 05:03 UTC | 2026-08-07 05:35 UTC | 31m |
| N53FF |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-08-07 03:01 UTC | 2026-08-07 05:31 UTC | 2h 30m |
| GAC872P | GAC | Bologna / Borgo Panigale Airport (LIPE) | Otocac Airport (LDRO) | 2026-08-07 04:56 UTC | 2026-08-07 05:30 UTC | 34m |
| EZY825P | easyJet | Glasgow International Airport (EGPF) | Belfast International Airport (EGAA) | 2026-08-07 05:06 UTC | 2026-08-07 05:29 UTC | 23m |
| SFJ13 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-08-07 04:23 UTC | 2026-08-07 05:27 UTC | 1h 3m |
| OXW | OXW | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-07 05:14 UTC | 2026-08-07 05:27 UTC | 12m |
| CYP4RD | CYP | Queen Alia International Airport (OJAI) | Diagoras Airport (LGRP) | 2026-08-07 04:35 UTC | 2026-08-07 05:25 UTC | 50m |
| ZKIDU | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-08-07 05:05 UTC | 2026-08-07 05:25 UTC | 19m |
| FR140 |  | Al Ain International Airport (OMAL) | Al Ain International Airport (OMAL) | 2026-08-07 04:44 UTC | 2026-08-07 05:25 UTC | 40m |
| N229LJ |  | Bentonville Municipal/Louise M Thaden Field (KVBT) | Benoit Airfield (77AR) | 2026-08-07 05:03 UTC | 2026-08-07 05:25 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
