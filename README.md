# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_05:57:49_UTC-green)

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

**Latest saved flight:** 2026-07-14 05:57:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-14 05:57:49 UTC

- **141,333** saved flights
- **47,474** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **141,333** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,697,147.4 tonnes** estimated CO2 emissions
- **98,385,358 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5746 |
| 2 | SkyWest Airlines | 5175 |
| 3 | EJA | 2786 |
| 4 | IndiGo | 2585 |
| 5 | American Airlines | 2250 |
| 6 | Southwest Airlines | 2130 |
| 7 | ENY | 1756 |
| 8 | Delta Air Lines | 1675 |
| 9 | Lufthansa | 1429 |
| 10 | LATAM Airlines | 1298 |
| 11 | Vueling | 1216 |
| 12 | AZU | 1215 |
| 13 | WIF | 1212 |
| 14 | LXJ | 1086 |
| 15 | AXM | 1051 |
| 16 | Swiss International | 1005 |
| 17 | easyJet | 922 |
| 18 | All Nippon Airways | 907 |
| 19 | Alaska Airlines | 891 |
| 20 | QLK | 887 |
| 21 | EJU | 869 |
| 22 | VIV | 781 |
| 23 | AEE | 757 |
| 24 | CXK | 756 |
| 25 | Air France | 754 |
| 26 | JetBlue | 751 |
| 27 | United Airlines | 737 |
| 28 | Cathay Pacific | 732 |
| 29 | MXY | 731 |
| 30 | GLO | 723 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 121588 |
| 2 | 🇪🇸 ES | 9238 |
| 3 | 🇮🇳 IN | 8095 |
| 4 | 🇦🇺 AU | 8093 |
| 5 | 🇧🇷 BR | 7976 |
| 6 | 🇨🇦 CA | 7437 |
| 7 | 🇮🇹 IT | 7365 |
| 8 | 🇩🇪 DE | 7338 |
| 9 | 🇬🇧 GB | 6439 |
| 10 | 🇯🇵 JP | 5931 |
| 11 | 🇫🇷 FR | 5612 |
| 12 | 🇨🇴 CO | 4490 |
| 13 | 🇲🇽 MX | 4105 |
| 14 | 🇬🇷 GR | 4020 |
| 15 | 🇳🇴 NO | 3787 |
| 16 | 🇨🇭 CH | 3661 |
| 17 | 🇹🇷 TR | 3347 |
| 18 | 🇲🇾 MY | 2743 |
| 19 | 🇵🇱 PL | 2362 |
| 20 | 🇿🇦 ZA | 2308 |
| 21 | 🇳🇿 NZ | 2164 |
| 22 | 🇹🇭 TH | 2119 |
| 23 | 🇰🇷 KR | 2017 |
| 24 | 🇵🇭 PH | 1914 |
| 25 | 🇬🇹 GT | 1865 |
| 26 | 🇲🇦 MA | 1481 |
| 27 | 🇲🇪 ME | 1403 |
| 28 | 🇳🇱 NL | 1328 |
| 29 | 🇭🇷 HR | 1278 |
| 30 | 🇲🇴 MO | 1191 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2913 |
| 2 | Denver International Airport |  | US | 2363 |
| 3 | Tokyo International Airport |  | JP | 1918 |
| 4 | Indira Gandhi International Airport |  | IN | 1793 |
| 5 | Harry Reid International Airport |  | US | 1768 |
| 6 | Guaymaral Airport |  | CO | 1717 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1622 |
| 8 | Zurich Airport |  | CH | 1572 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1484 |
| 10 | La Aurora Airport |  | GT | 1442 |
| 11 | Frankfurt am Main International Airport |  | DE | 1379 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1347 |
| 13 | Chicago O'Hare International Airport |  | US | 1328 |
| 14 | Salt Lake City International Airport |  | US | 1263 |
| 15 | El Dorado International Airport |  | CO | 1248 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1228 |
| 17 | Macau International Airport |  | MO | 1191 |
| 18 | Capua Airport |  | IT | 1157 |
| 19 | Madrid Barajas International Airport |  | ES | 1142 |
| 20 | Congonhas Airport |  | BR | 1134 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1127 |
| 22 | Kuala Lumpur International Airport |  | MY | 1059 |
| 23 | Charlotte/Douglas International Airport |  | US | 1027 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1023 |
| 25 | Charles de Gaulle International Airport |  | FR | 999 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 985 |
| 27 | Bengaluru International Airport |  | IN | 970 |
| 28 | Malpensa International Airport |  | IT | 916 |
| 29 | Ninoy Aquino International Airport |  | PH | 893 |
| 30 | Daniel K Inouye International Airport |  | US | 864 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 864 |
| 32 | Barcelona International Airport |  | ES | 861 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 833 |
| 34 | Tenerife Norte Airport |  | ES | 820 |
| 35 | Calgary International Airport |  | CA | 811 |
| 36 | Viracopos International Airport |  | BR | 802 |
| 37 | Seattle-Tacoma International Airport |  | US | 802 |
| 38 | Amsterdam Airport Schiphol |  | NL | 801 |
| 39 | Scottsdale Airport |  | US | 801 |
| 40 | Vitoria/Foronda Airport |  | ES | 781 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 724 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 514 | 21m | 244 km | 2,164.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 345 | 24m | 225 km | 1,338.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 345 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 334 | 1h 9m | 770 km | 4,436.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 298 | 14m | 114 km | 584.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 207 | 22m | 55 km | 196.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 190 | 1h 46m | 1,423 km | 4,662.9 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 189 | 20m | 99 km | 323.7 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 188 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 177 | 28m | 152 km | 462.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 176 | 20m | 250 km | 760.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 172 | 31m | 369 km | 1,094.8 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 170 | 18m | 144 km | 422.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 165 | 44m | 452 km | 1,285.9 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 163 | 1h 16m | 961 km | 2,701.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 162 | 1h 1m | 695 km | 1,941.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 161 | 1h 38m | 1,156 km | 3,211.9 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 158 | 13m | - | - |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| STALK51 | STA | 50NM (50NM) | Rancho Magdalena Airport (NM01) | 2026-07-14 05:23 UTC | 2026-07-14 05:57 UTC | 34m |
| A7GQE |  | Bahrain International Airport (OBBI) | Persian Gulf International Airport (OIBP) | 2026-07-14 05:45 UTC | 2026-07-14 05:53 UTC | 8m |
| N72MZ |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-07-14 04:44 UTC | 2026-07-14 05:47 UTC | 1h 2m |
| FJHSA | FJH | Aubenasson Airport (LFJF) | Romans - Saint-Paul Airport (LFHE) | 2026-07-14 05:31 UTC | 2026-07-14 05:45 UTC | 13m |
| EJA633 | EJA | Youngberg Ranch Airport (NV17) | Oakland San Francisco Bay Airport (KOAK) | 2026-07-14 05:04 UTC | 2026-07-14 05:43 UTC | 38m |
| WWF287 | WWF | Provo Municipal Airport (KPVU) | Four Corners Regional Airport (KFMN) | 2026-07-14 03:00 UTC | 2026-07-14 05:37 UTC | 2h 36m |
| N49CG |  | Bend Municipal Airport (KBDN) | Wapinitia Airport (OR53) | 2026-07-14 04:56 UTC | 2026-07-14 05:36 UTC | 40m |
| N157U |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-07-14 04:20 UTC | 2026-07-14 05:33 UTC | 1h 13m |
| ZKIGG | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-07-14 05:22 UTC | 2026-07-14 05:31 UTC | 9m |
| YNM | YNM | Adelaide Parafield Airport (YPPF) | Adelaide Parafield Airport (YPPF) | 2026-07-14 04:59 UTC | 2026-07-14 05:29 UTC | 29m |
| FIN1HF | Finnair | Helsinki Vantaa Airport (EFHK) | Khrabrovo Airport (UMKK) | 2026-07-14 04:51 UTC | 2026-07-14 05:27 UTC | 36m |
| UAE8X | Emirates | Dubai International Airport (OMDB) | Hradec Kralove Airport (LKHK) | 2026-07-14 00:13 UTC | 2026-07-14 05:24 UTC | 5h 10m |
| N68713 |  | Roberts Field (KRDM) | Nelson Ranch Airport (19OR) | 2026-07-14 04:43 UTC | 2026-07-14 05:17 UTC | 34m |
| ANA295 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-07-14 04:34 UTC | 2026-07-14 05:16 UTC | 41m |
| CLX46C | CLX | Seattle-Tacoma International Airport (KSEA) | Calgary International Airport (CYYC) | 2026-07-14 04:14 UTC | 2026-07-14 05:16 UTC | 1h 1m |
| N912SM |  | Centennial Airport (KAPA) | Crawford Airport (K99V) | 2026-07-14 03:46 UTC | 2026-07-14 05:15 UTC | 1h 29m |
| CSN8138 | China Southern | Long Bawan Airport (WRLB) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-07-14 02:29 UTC | 2026-07-14 05:13 UTC | 2h 44m |
| JA58KB |  | Nagoya Airport (RJNA) | Nagoya Airport (RJNA) | 2026-07-14 04:29 UTC | 2026-07-14 05:10 UTC | 41m |
| SHADO75 | SHA | Portales Municipal Airport (KPRZ) | Portales Municipal Airport (KPRZ) | 2026-07-14 05:06 UTC | 2026-07-14 05:09 UTC | 2m |
| CSN8482 | China Southern | Long Bawan Airport (WRLB) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-07-14 02:31 UTC | 2026-07-14 05:09 UTC | 2h 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
