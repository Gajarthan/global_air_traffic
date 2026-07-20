# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20_22:20:28_UTC-green)

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

**Latest saved flight:** 2026-07-20 22:20:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-20 22:20:28 UTC

- **142,853** saved flights
- **47,907** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **142,853** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,713,450.5 tonnes** estimated CO2 emissions
- **99,330,466 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5815 |
| 2 | SkyWest Airlines | 5225 |
| 3 | EJA | 2818 |
| 4 | IndiGo | 2599 |
| 5 | American Airlines | 2285 |
| 6 | Southwest Airlines | 2153 |
| 7 | ENY | 1772 |
| 8 | Delta Air Lines | 1693 |
| 9 | Lufthansa | 1435 |
| 10 | LATAM Airlines | 1317 |
| 11 | AZU | 1229 |
| 12 | Vueling | 1227 |
| 13 | WIF | 1220 |
| 14 | LXJ | 1097 |
| 15 | AXM | 1055 |
| 16 | Swiss International | 1014 |
| 17 | easyJet | 933 |
| 18 | All Nippon Airways | 913 |
| 19 | Alaska Airlines | 901 |
| 20 | QLK | 895 |
| 21 | EJU | 879 |
| 22 | VIV | 793 |
| 23 | CXK | 765 |
| 24 | AEE | 763 |
| 25 | JetBlue | 760 |
| 26 | Air France | 759 |
| 27 | MXY | 743 |
| 28 | United Airlines | 743 |
| 29 | Cathay Pacific | 737 |
| 30 | GLO | 731 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 122948 |
| 2 | 🇪🇸 ES | 9309 |
| 3 | 🇦🇺 AU | 8166 |
| 4 | 🇮🇳 IN | 8142 |
| 5 | 🇧🇷 BR | 8065 |
| 6 | 🇨🇦 CA | 7525 |
| 7 | 🇮🇹 IT | 7440 |
| 8 | 🇩🇪 DE | 7391 |
| 9 | 🇬🇧 GB | 6544 |
| 10 | 🇯🇵 JP | 5974 |
| 11 | 🇫🇷 FR | 5672 |
| 12 | 🇨🇴 CO | 4588 |
| 13 | 🇲🇽 MX | 4148 |
| 14 | 🇬🇷 GR | 4068 |
| 15 | 🇳🇴 NO | 3820 |
| 16 | 🇨🇭 CH | 3690 |
| 17 | 🇹🇷 TR | 3376 |
| 18 | 🇲🇾 MY | 2751 |
| 19 | 🇵🇱 PL | 2403 |
| 20 | 🇿🇦 ZA | 2326 |
| 21 | 🇳🇿 NZ | 2194 |
| 22 | 🇹🇭 TH | 2128 |
| 23 | 🇰🇷 KR | 2027 |
| 24 | 🇵🇭 PH | 1928 |
| 25 | 🇬🇹 GT | 1874 |
| 26 | 🇲🇦 MA | 1492 |
| 27 | 🇲🇪 ME | 1414 |
| 28 | 🇳🇱 NL | 1345 |
| 29 | 🇭🇷 HR | 1301 |
| 30 | 🇲🇴 MO | 1194 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2941 |
| 2 | Denver International Airport |  | US | 2391 |
| 3 | Tokyo International Airport |  | JP | 1928 |
| 4 | Indira Gandhi International Airport |  | IN | 1805 |
| 5 | Harry Reid International Airport |  | US | 1794 |
| 6 | Guaymaral Airport |  | CO | 1738 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1637 |
| 8 | Zurich Airport |  | CH | 1585 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1501 |
| 10 | La Aurora Airport |  | GT | 1450 |
| 11 | Frankfurt am Main International Airport |  | DE | 1385 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1352 |
| 13 | Chicago O'Hare International Airport |  | US | 1336 |
| 14 | Salt Lake City International Airport |  | US | 1277 |
| 15 | El Dorado International Airport |  | CO | 1266 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1257 |
| 17 | Macau International Airport |  | MO | 1194 |
| 18 | Capua Airport |  | IT | 1166 |
| 19 | Madrid Barajas International Airport |  | ES | 1147 |
| 20 | Congonhas Airport |  | BR | 1145 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1132 |
| 22 | Kuala Lumpur International Airport |  | MY | 1062 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1034 |
| 24 | Charlotte/Douglas International Airport |  | US | 1030 |
| 25 | Charles de Gaulle International Airport |  | FR | 1004 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 999 |
| 27 | Bengaluru International Airport |  | IN | 972 |
| 28 | Malpensa International Airport |  | IT | 921 |
| 29 | Ninoy Aquino International Airport |  | PH | 900 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 875 |
| 31 | Daniel K Inouye International Airport |  | US | 870 |
| 32 | Barcelona International Airport |  | ES | 869 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 847 |
| 34 | Tenerife Norte Airport |  | ES | 825 |
| 35 | Calgary International Airport |  | CA | 814 |
| 36 | Seattle-Tacoma International Airport |  | US | 813 |
| 37 | Viracopos International Airport |  | BR | 811 |
| 38 | Amsterdam Airport Schiphol |  | NL | 808 |
| 39 | Scottsdale Airport |  | US | 806 |
| 40 | Vitoria/Foronda Airport |  | ES | 786 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 732 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 520 | 21m | 244 km | 2,189.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 349 | 24m | 225 km | 1,354.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 346 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 338 | 1h 9m | 770 km | 4,490.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 259 | 26m | 275 km | 1,227.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 211 | 22m | 55 km | 200.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 192 | 1h 46m | 1,423 km | 4,712.0 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 190 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 177 | 20m | 250 km | 764.5 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 172 | 18m | 144 km | 427.8 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 167 | 44m | 452 km | 1,301.5 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 166 | 1h 16m | 961 km | 2,751.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 1m | 695 km | 1,977.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 163 | 13m | - | - |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N607RJ |  | Chipola Airpark (5FL8) | Addison Airport (KADS) | 2026-07-20 20:52 UTC | 2026-07-20 22:20 UTC | 1h 28m |
| CXK294 | CXK | Arlington Municipal Airport (KGKY) | Arlington Municipal Airport (KGKY) | 2026-07-20 21:20 UTC | 2026-07-20 22:19 UTC | 58m |
| URSA75 | URS | Lakloey Air Park (AK22) | Ladd Army Air Field (PAFB) | 2026-07-20 22:05 UTC | 2026-07-20 22:18 UTC | 12m |
| N622TP |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-07-20 21:40 UTC | 2026-07-20 22:11 UTC | 30m |
| N928FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-07-20 21:15 UTC | 2026-07-20 22:08 UTC | 53m |
| N828WW |  | Dupage Airport (KDPA) | Morris Municipal/James R Washburn Field (KC09) | 2026-07-20 21:43 UTC | 2026-07-20 22:08 UTC | 25m |
| ZKLFA | ZKL | Hamilton International Airport (NZHN) | Whakatane Airport (NZWK) | 2026-07-20 20:56 UTC | 2026-07-20 22:07 UTC | 1h 10m |
| N1507X |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-07-20 21:28 UTC | 2026-07-20 22:07 UTC | 38m |
| N82BH |  | Fremont County Airport (K1V6) | Ak Su Airport (CO61) | 2026-07-20 21:35 UTC | 2026-07-20 22:06 UTC | 30m |
| N130AG |  | Atlanta Regional Falcon Field (KFFC) | Thomaston-Upson County Airport (KOPN) | 2026-07-20 21:04 UTC | 2026-07-20 22:04 UTC | 1h 0m |
| CPA294 | Cathay Pacific | Melsbroek Air Base (EBMB) | Macau International Airport (VMMC) | 2026-07-20 11:16 UTC | 2026-07-20 22:03 UTC | 10h 47m |
| EJA137 | EJA | Teterboro Airport (KTEB) | Mc Clellan Airfield (KMCC) | 2026-07-20 16:51 UTC | 2026-07-20 21:55 UTC | 5h 3m |
| N408GG |  | Linden Airport (KLDJ) | Laguardia Airport (KLGA) | 2026-07-20 21:01 UTC | 2026-07-20 21:54 UTC | 53m |
| N406KT |  | Fremont County Airport (K1V6) | Silver West Airport (KC08) | 2026-07-20 21:21 UTC | 2026-07-20 21:53 UTC | 32m |
| URSA75 | URS | Chena Hot Springs Airport (AK13) | Lakloey Air Park (AK22) | 2026-07-20 21:26 UTC | 2026-07-20 21:52 UTC | 26m |
| ZKPDZ | ZKP | Omarama Glider Airport (NZOA) | Queenstown International Airport (NZQN) | 2026-07-20 21:37 UTC | 2026-07-20 21:48 UTC | 11m |
| N115GK |  | Provincetown Municipal Airport (KPVC) | Laguardia Airport (KLGA) | 2026-07-20 20:28 UTC | 2026-07-20 21:46 UTC | 1h 17m |
| N922CA |  | Portsmouth International At Pease Airport (KPSM) | Back Acres Airport (ME46) | 2026-07-20 21:10 UTC | 2026-07-20 21:43 UTC | 32m |
| JANET27 | JAN | Harry Reid International Airport (KLAS) | KDRA (KDRA) | 2026-07-20 21:30 UTC | 2026-07-20 21:42 UTC | 12m |
| N570FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-07-20 21:19 UTC | 2026-07-20 21:42 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
