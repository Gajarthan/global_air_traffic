# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_00:45:59_UTC-green)

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

**Latest saved flight:** 2026-07-04 00:45:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-04 00:45:59 UTC

- **128,447** saved flights
- **43,768** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **128,447** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,549,329.3 tonnes** estimated CO2 emissions
- **89,816,193 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5215 |
| 2 | SkyWest Airlines | 4769 |
| 3 | EJA | 2522 |
| 4 | IndiGo | 2413 |
| 5 | American Airlines | 1982 |
| 6 | Southwest Airlines | 1934 |
| 7 | ENY | 1612 |
| 8 | Delta Air Lines | 1532 |
| 9 | Lufthansa | 1355 |
| 10 | LATAM Airlines | 1168 |
| 11 | Vueling | 1134 |
| 12 | WIF | 1127 |
| 13 | AZU | 1089 |
| 14 | AXM | 1002 |
| 15 | LXJ | 997 |
| 16 | Swiss International | 889 |
| 17 | All Nippon Airways | 854 |
| 18 | Alaska Airlines | 831 |
| 19 | easyJet | 817 |
| 20 | QLK | 808 |
| 21 | EJU | 795 |
| 22 | VIV | 710 |
| 23 | Cathay Pacific | 708 |
| 24 | AEE | 702 |
| 25 | Air France | 699 |
| 26 | CXK | 694 |
| 27 | United Airlines | 685 |
| 28 | MXY | 672 |
| 29 | JetBlue | 661 |
| 30 | GLO | 649 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 110100 |
| 2 | 🇪🇸 ES | 8534 |
| 3 | 🇮🇳 IN | 7561 |
| 4 | 🇦🇺 AU | 7475 |
| 5 | 🇧🇷 BR | 7190 |
| 6 | 🇨🇦 CA | 6773 |
| 7 | 🇩🇪 DE | 6747 |
| 8 | 🇮🇹 IT | 6725 |
| 9 | 🇬🇧 GB | 5676 |
| 10 | 🇯🇵 JP | 5578 |
| 11 | 🇫🇷 FR | 5081 |
| 12 | 🇨🇴 CO | 4072 |
| 13 | 🇲🇽 MX | 3750 |
| 14 | 🇬🇷 GR | 3646 |
| 15 | 🇳🇴 NO | 3501 |
| 16 | 🇨🇭 CH | 3258 |
| 17 | 🇹🇷 TR | 2755 |
| 18 | 🇲🇾 MY | 2598 |
| 19 | 🇿🇦 ZA | 2126 |
| 20 | 🇵🇱 PL | 2097 |
| 21 | 🇳🇿 NZ | 2069 |
| 22 | 🇹🇭 TH | 1990 |
| 23 | 🇰🇷 KR | 1959 |
| 24 | 🇵🇭 PH | 1806 |
| 25 | 🇬🇹 GT | 1763 |
| 26 | 🇲🇦 MA | 1375 |
| 27 | 🇲🇪 ME | 1272 |
| 28 | 🇳🇱 NL | 1207 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇭🇷 HR | 1109 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2681 |
| 2 | Denver International Airport |  | US | 2182 |
| 3 | Tokyo International Airport |  | JP | 1838 |
| 4 | Indira Gandhi International Airport |  | IN | 1664 |
| 5 | Harry Reid International Airport |  | US | 1606 |
| 6 | Guaymaral Airport |  | CO | 1559 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1521 |
| 8 | Zurich Airport |  | CH | 1407 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1369 |
| 10 | La Aurora Airport |  | GT | 1363 |
| 11 | Frankfurt am Main International Airport |  | DE | 1312 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1255 |
| 13 | Chicago O'Hare International Airport |  | US | 1236 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1147 |
| 17 | Capua Airport |  | IT | 1067 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1066 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1057 |
| 20 | Madrid Barajas International Airport |  | ES | 1048 |
| 21 | Kuala Lumpur International Airport |  | MY | 1010 |
| 22 | Congonhas Airport |  | BR | 1009 |
| 23 | Charlotte/Douglas International Airport |  | US | 968 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 939 |
| 25 | Charles de Gaulle International Airport |  | FR | 932 |
| 26 | Bengaluru International Airport |  | IN | 916 |
| 27 | Malpensa International Airport |  | IT | 874 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 865 |
| 29 | Ninoy Aquino International Airport |  | PH | 837 |
| 30 | Daniel K Inouye International Airport |  | US | 813 |
| 31 | Barcelona International Airport |  | ES | 799 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 786 |
| 33 | Tenerife Norte Airport |  | ES | 781 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 758 |
| 35 | Calgary International Airport |  | CA | 752 |
| 36 | Seattle-Tacoma International Airport |  | US | 743 |
| 37 | Scottsdale Airport |  | US | 742 |
| 38 | Vitoria/Foronda Airport |  | ES | 739 |
| 39 | Viracopos International Airport |  | BR | 734 |
| 40 | Amsterdam Airport Schiphol |  | NL | 728 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 652 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 466 | 21m | 244 km | 1,962.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 324 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 310 | 1h 10m | 770 km | 4,118.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 244 | 26m | 275 km | 1,156.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 236 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 181 | 26m | 215 km | 670.3 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 179 | 44m | 241 km | 743.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 166 | 1h 45m | 1,423 km | 4,073.9 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 162 | 31m | 369 km | 1,031.2 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 158 | 18m | 144 km | 393.0 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 157 | 20m | 250 km | 678.1 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 152 | 1h 1m | 695 km | 1,822.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 149 | 1h 17m | 961 km | 2,469.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 146 | 54m | 136 km | 342.3 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 143 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JBU2459 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | Philadelphia International Airport (KPHL) | 2026-07-03 22:58 UTC | 2026-07-04 00:45 UTC | 1h 47m |
| N1507X |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Sacramento Mather Airport (KMHR) | 2026-07-03 23:57 UTC | 2026-07-04 00:42 UTC | 45m |
| JPR14 | JPR | Hillside Airstrip (7AK0) | Fairbanks International Airport (PAFA) | 2026-07-04 00:12 UTC | 2026-07-04 00:41 UTC | 29m |
| JBU22 | JetBlue | Palm Beach International Airport (KPBI) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-03 22:02 UTC | 2026-07-04 00:41 UTC | 2h 38m |
| BRG605 | BRG | Ralph Wien Memorial Airport (PAOT) | Deering Airport (PADE) | 2026-07-04 00:14 UTC | 2026-07-04 00:41 UTC | 26m |
| UAL274 | United Airlines | San Francisco International Airport (KSFO) | Philadelphia International Airport (KPHL) | 2026-07-03 18:44 UTC | 2026-07-04 00:41 UTC | 5h 56m |
| CUL546 | CUL | City Of Colorado Springs Municipal Airport (KCOS) | Mann Ranch Airport (95CO) | 2026-07-03 22:00 UTC | 2026-07-04 00:40 UTC | 2h 40m |
| N100BW |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-03 23:51 UTC | 2026-07-04 00:39 UTC | 47m |
| N510PR |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-03 23:46 UTC | 2026-07-04 00:33 UTC | 47m |
| N |  | Campbell River Airport (CYBL) | Vancouver International Airport (CYVR) | 2026-07-03 23:52 UTC | 2026-07-04 00:33 UTC | 40m |
| N88765 |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-03 23:57 UTC | 2026-07-04 00:28 UTC | 30m |
| MMA846 | MMA | Yangon International Airport (VYYY) | Heho Airport (VYHH) | 2026-07-03 23:30 UTC | 2026-07-04 00:26 UTC | 55m |
| N80945 |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-03 23:51 UTC | 2026-07-04 00:22 UTC | 31m |
| JST972 | JST | Melbourne International Airport (YMML) | Perth International Airport (YPPH) | 2026-07-03 20:48 UTC | 2026-07-04 00:20 UTC | 3h 31m |
| N426NC |  | Ban Farm Airport (AL88) | Shields Airport (AL55) | 2026-07-03 23:56 UTC | 2026-07-04 00:12 UTC | 15m |
| FAG142 | FAG | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-07-04 00:02 UTC | 2026-07-04 00:11 UTC | 9m |
| RPA3699 | Republic Airways | MS00 (MS00) | Philadelphia International Airport (KPHL) | 2026-07-03 21:30 UTC | 2026-07-04 00:10 UTC | 2h 39m |
| N444AM |  | Quad Cities International Airport (KMLI) | Crawford County Airport (KRSV) | 2026-07-03 23:36 UTC | 2026-07-04 00:09 UTC | 32m |
| TKR806 | TKR | Oasis Airpark (1ID4) | Harrington Airport (20ID) | 2026-07-03 23:52 UTC | 2026-07-04 00:08 UTC | 15m |
| TKR169 | TKR | Animas Air Park (K00C) | Animas Air Park (K00C) | 2026-07-03 23:35 UTC | 2026-07-04 00:04 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
