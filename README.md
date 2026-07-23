# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_04:06:55_UTC-green)

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

**Latest saved flight:** 2026-07-23 04:06:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-23 04:06:55 UTC

- **145,122** saved flights
- **48,582** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **145,122** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,739,035.3 tonnes** estimated CO2 emissions
- **100,813,643 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5889 |
| 2 | SkyWest Airlines | 5317 |
| 3 | EJA | 2862 |
| 4 | IndiGo | 2627 |
| 5 | American Airlines | 2322 |
| 6 | Southwest Airlines | 2194 |
| 7 | ENY | 1808 |
| 8 | Delta Air Lines | 1720 |
| 9 | Lufthansa | 1444 |
| 10 | LATAM Airlines | 1338 |
| 11 | AZU | 1250 |
| 12 | WIF | 1237 |
| 13 | Vueling | 1236 |
| 14 | LXJ | 1117 |
| 15 | AXM | 1064 |
| 16 | Swiss International | 1029 |
| 17 | easyJet | 942 |
| 18 | All Nippon Airways | 927 |
| 19 | Alaska Airlines | 915 |
| 20 | QLK | 913 |
| 21 | EJU | 886 |
| 22 | VIV | 809 |
| 23 | CXK | 779 |
| 24 | AEE | 766 |
| 25 | JetBlue | 766 |
| 26 | Air France | 764 |
| 27 | MXY | 760 |
| 28 | Cathay Pacific | 757 |
| 29 | United Airlines | 755 |
| 30 | GLO | 744 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 125151 |
| 2 | 🇪🇸 ES | 9393 |
| 3 | 🇦🇺 AU | 8315 |
| 4 | 🇮🇳 IN | 8229 |
| 5 | 🇧🇷 BR | 8193 |
| 6 | 🇨🇦 CA | 7713 |
| 7 | 🇮🇹 IT | 7540 |
| 8 | 🇩🇪 DE | 7468 |
| 9 | 🇬🇧 GB | 6605 |
| 10 | 🇯🇵 JP | 6070 |
| 11 | 🇫🇷 FR | 5756 |
| 12 | 🇨🇴 CO | 4745 |
| 13 | 🇲🇽 MX | 4231 |
| 14 | 🇬🇷 GR | 4100 |
| 15 | 🇳🇴 NO | 3869 |
| 16 | 🇨🇭 CH | 3753 |
| 17 | 🇹🇷 TR | 3402 |
| 18 | 🇲🇾 MY | 2777 |
| 19 | 🇵🇱 PL | 2441 |
| 20 | 🇿🇦 ZA | 2350 |
| 21 | 🇳🇿 NZ | 2222 |
| 22 | 🇹🇭 TH | 2130 |
| 23 | 🇰🇷 KR | 2043 |
| 24 | 🇵🇭 PH | 1937 |
| 25 | 🇬🇹 GT | 1887 |
| 26 | 🇲🇦 MA | 1503 |
| 27 | 🇲🇪 ME | 1440 |
| 28 | 🇳🇱 NL | 1357 |
| 29 | 🇭🇷 HR | 1320 |
| 30 | 🇲🇴 MO | 1212 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2999 |
| 2 | Denver International Airport |  | US | 2431 |
| 3 | Tokyo International Airport |  | JP | 1950 |
| 4 | Indira Gandhi International Airport |  | IN | 1828 |
| 5 | Harry Reid International Airport |  | US | 1822 |
| 6 | Guaymaral Airport |  | CO | 1777 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1644 |
| 8 | Zurich Airport |  | CH | 1601 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1524 |
| 10 | La Aurora Airport |  | GT | 1462 |
| 11 | Frankfurt am Main International Airport |  | DE | 1392 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1371 |
| 13 | Chicago O'Hare International Airport |  | US | 1350 |
| 14 | Salt Lake City International Airport |  | US | 1305 |
| 15 | El Dorado International Airport |  | CO | 1298 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1262 |
| 17 | Macau International Airport |  | MO | 1212 |
| 18 | Capua Airport |  | IT | 1179 |
| 19 | Congonhas Airport |  | BR | 1166 |
| 20 | Madrid Barajas International Airport |  | ES | 1155 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1145 |
| 22 | Kuala Lumpur International Airport |  | MY | 1073 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1053 |
| 24 | Charlotte/Douglas International Airport |  | US | 1041 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1014 |
| 26 | Charles de Gaulle International Airport |  | FR | 1009 |
| 27 | Bengaluru International Airport |  | IN | 982 |
| 28 | Malpensa International Airport |  | IT | 936 |
| 29 | Ninoy Aquino International Airport |  | PH | 905 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 890 |
| 31 | Barcelona International Airport |  | ES | 880 |
| 32 | Daniel K Inouye International Airport |  | US | 879 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 866 |
| 34 | Tenerife Norte Airport |  | ES | 829 |
| 35 | Seattle-Tacoma International Airport |  | US | 827 |
| 36 | Viracopos International Airport |  | BR | 825 |
| 37 | Calgary International Airport |  | CA | 824 |
| 38 | Scottsdale Airport |  | US | 823 |
| 39 | Amsterdam Airport Schiphol |  | NL | 817 |
| 40 | Oslo Gardermoen Airport |  | NO | 795 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 749 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 528 | 21m | 244 km | 2,223.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 352 | 24m | 225 km | 1,365.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 351 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 341 | 1h 9m | 770 km | 4,529.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 261 | 26m | 275 km | 1,236.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 257 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 217 | 22m | 55 km | 206.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 193 | 1h 46m | 1,423 km | 4,736.5 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 193 | 44m | 241 km | 801.7 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 192 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 179 | 20m | 250 km | 773.2 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 173 | 18m | 144 km | 430.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 168 | 44m | 452 km | 1,309.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 168 | 1h 16m | 961 km | 2,784.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 165 | 1h 39m | 1,156 km | 3,291.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 165 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OXJ | OXJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-07-23 03:56 UTC | 2026-07-23 04:06 UTC | 10m |
| YKI | YKI | Adelaide Parafield Airport (YPPF) | Adelaide Parafield Airport (YPPF) | 2026-07-23 03:37 UTC | 2026-07-23 04:00 UTC | 22m |
| CXK246 | CXK | Ellington Airport (KEFD) | Ellington Airport (KEFD) | 2026-07-23 02:37 UTC | 2026-07-23 03:56 UTC | 1h 18m |
| N354WC |  | Camarillo Airport (KCMA) | Camarillo Airport (KCMA) | 2026-07-23 03:33 UTC | 2026-07-23 03:47 UTC | 14m |
| OUA8 | OUA | University Of Oklahoma Westheimer Airport (KOUN) | Gregg Airport (7OK1) | 2026-07-23 02:48 UTC | 2026-07-23 03:47 UTC | 59m |
| QFA765 | Qantas | Melbourne International Airport (YMML) | Lake Varley Airport (YLVY) | 2026-07-23 00:33 UTC | 2026-07-23 03:41 UTC | 3h 8m |
| SWA342 | Southwest Airlines | John Wayne/Orange County Airport (KSNA) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-23 02:41 UTC | 2026-07-23 03:32 UTC | 51m |
| ANA964 | All Nippon Airways | Tokyo International Airport (RJTT) | Tokyo International Airport (RJTT) | 2026-07-22 08:45 UTC | 2026-07-23 03:29 UTC | 18h 44m |
| VOI3316 | VOI | General Abelardo L. Rodriguez International Airport (MMTJ) | General Jose Maria Yanez International Airport (MMGM) | 2026-07-23 02:21 UTC | 2026-07-23 03:28 UTC | 1h 6m |
| CEB897 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-07-23 02:59 UTC | 2026-07-23 03:23 UTC | 24m |
| N515MV |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-07-23 02:46 UTC | 2026-07-23 03:20 UTC | 34m |
| QLK1573 | QLK | Gold Coast Airport (YBCG) | Melbourne International Airport (YMML) | 2026-07-23 01:05 UTC | 2026-07-23 03:20 UTC | 2h 14m |
| SFJ96 | SFJ | Sendai Airport (RJSS) | Ashiya Airport (RJFA) | 2026-07-23 01:53 UTC | 2026-07-23 03:19 UTC | 1h 25m |
| N450PD |  | Ellison Onizuka Kona International At Keahole Airport (PHKO) | Buhl Municipal Airport (KU03) | 2026-07-22 22:18 UTC | 2026-07-23 03:19 UTC | 5h 0m |
| LICHEN9 | LIC | Nenana Municipal Airport (PANN) | Ladd Army Air Field (PAFB) | 2026-07-23 02:24 UTC | 2026-07-23 03:17 UTC | 52m |
| ARR680 | ARR | La Crosse Regional Airport (KLSE) | Marian Airpark (KF06) | 2026-07-23 01:38 UTC | 2026-07-23 03:16 UTC | 1h 38m |
| ANA793 | All Nippon Airways | Tokyo International Airport (RJTT) | Hiroshima Airport (RJOA) | 2026-07-23 02:17 UTC | 2026-07-23 03:16 UTC | 58m |
| RXA6174 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-07-23 02:44 UTC | 2026-07-23 03:13 UTC | 28m |
| FD607 |  | Perth Jandakot Airport (YPJT) | Kojonup Airport (YKOJ) | 2026-07-23 02:11 UTC | 2026-07-23 03:13 UTC | 1h 2m |
| N22QT |  | Oakland San Francisco Bay Airport (KOAK) | Tracy Municipal Airport (KTCY) | 2026-07-23 02:43 UTC | 2026-07-23 03:13 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
