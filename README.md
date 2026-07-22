# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--22_19:49:32_UTC-green)

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

**Latest saved flight:** 2026-07-22 19:49:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-22 19:49:32 UTC

- **144,443** saved flights
- **48,382** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **144,443** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,730,770.3 tonnes** estimated CO2 emissions
- **100,334,513 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5872 |
| 2 | SkyWest Airlines | 5284 |
| 3 | EJA | 2844 |
| 4 | IndiGo | 2623 |
| 5 | American Airlines | 2309 |
| 6 | Southwest Airlines | 2182 |
| 7 | ENY | 1794 |
| 8 | Delta Air Lines | 1714 |
| 9 | Lufthansa | 1444 |
| 10 | LATAM Airlines | 1326 |
| 11 | AZU | 1243 |
| 12 | WIF | 1237 |
| 13 | Vueling | 1236 |
| 14 | LXJ | 1108 |
| 15 | AXM | 1063 |
| 16 | Swiss International | 1028 |
| 17 | easyJet | 940 |
| 18 | All Nippon Airways | 922 |
| 19 | Alaska Airlines | 910 |
| 20 | QLK | 906 |
| 21 | EJU | 885 |
| 22 | VIV | 803 |
| 23 | CXK | 776 |
| 24 | AEE | 764 |
| 25 | Air France | 764 |
| 26 | JetBlue | 763 |
| 27 | MXY | 753 |
| 28 | United Airlines | 752 |
| 29 | Cathay Pacific | 748 |
| 30 | GLO | 740 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 124422 |
| 2 | 🇪🇸 ES | 9377 |
| 3 | 🇦🇺 AU | 8242 |
| 4 | 🇮🇳 IN | 8215 |
| 5 | 🇧🇷 BR | 8143 |
| 6 | 🇨🇦 CA | 7637 |
| 7 | 🇮🇹 IT | 7529 |
| 8 | 🇩🇪 DE | 7460 |
| 9 | 🇬🇧 GB | 6594 |
| 10 | 🇯🇵 JP | 6036 |
| 11 | 🇫🇷 FR | 5749 |
| 12 | 🇨🇴 CO | 4685 |
| 13 | 🇲🇽 MX | 4206 |
| 14 | 🇬🇷 GR | 4092 |
| 15 | 🇳🇴 NO | 3864 |
| 16 | 🇨🇭 CH | 3751 |
| 17 | 🇹🇷 TR | 3393 |
| 18 | 🇲🇾 MY | 2775 |
| 19 | 🇵🇱 PL | 2434 |
| 20 | 🇿🇦 ZA | 2350 |
| 21 | 🇳🇿 NZ | 2209 |
| 22 | 🇹🇭 TH | 2130 |
| 23 | 🇰🇷 KR | 2037 |
| 24 | 🇵🇭 PH | 1934 |
| 25 | 🇬🇹 GT | 1885 |
| 26 | 🇲🇦 MA | 1499 |
| 27 | 🇲🇪 ME | 1433 |
| 28 | 🇳🇱 NL | 1356 |
| 29 | 🇭🇷 HR | 1315 |
| 30 | 🇲🇴 MO | 1207 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2976 |
| 2 | Denver International Airport |  | US | 2422 |
| 3 | Tokyo International Airport |  | JP | 1942 |
| 4 | Indira Gandhi International Airport |  | IN | 1823 |
| 5 | Harry Reid International Airport |  | US | 1812 |
| 6 | Guaymaral Airport |  | CO | 1770 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1642 |
| 8 | Zurich Airport |  | CH | 1599 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1514 |
| 10 | La Aurora Airport |  | GT | 1460 |
| 11 | Frankfurt am Main International Airport |  | DE | 1390 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1364 |
| 13 | Chicago O'Hare International Airport |  | US | 1346 |
| 14 | Salt Lake City International Airport |  | US | 1296 |
| 15 | El Dorado International Airport |  | CO | 1281 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1261 |
| 17 | Macau International Airport |  | MO | 1207 |
| 18 | Capua Airport |  | IT | 1179 |
| 19 | Congonhas Airport |  | BR | 1157 |
| 20 | Madrid Barajas International Airport |  | ES | 1152 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1140 |
| 22 | Kuala Lumpur International Airport |  | MY | 1072 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1043 |
| 24 | Charlotte/Douglas International Airport |  | US | 1035 |
| 25 | Charles de Gaulle International Airport |  | FR | 1009 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1007 |
| 27 | Bengaluru International Airport |  | IN | 980 |
| 28 | Malpensa International Airport |  | IT | 935 |
| 29 | Ninoy Aquino International Airport |  | PH | 903 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 886 |
| 31 | Barcelona International Airport |  | ES | 877 |
| 32 | Daniel K Inouye International Airport |  | US | 876 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 861 |
| 34 | Tenerife Norte Airport |  | ES | 828 |
| 35 | Seattle-Tacoma International Airport |  | US | 822 |
| 36 | Viracopos International Airport |  | BR | 821 |
| 37 | Calgary International Airport |  | CA | 821 |
| 38 | Amsterdam Airport Schiphol |  | NL | 816 |
| 39 | Scottsdale Airport |  | US | 816 |
| 40 | Oslo Gardermoen Airport |  | NO | 793 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 746 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 525 | 21m | 244 km | 2,210.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 351 | 24m | 225 km | 1,361.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 350 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 340 | 1h 9m | 770 km | 4,516.6 t |
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
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 191 | 13m | - | - |
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
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 164 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| XBOWB | XBO | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-07-22 18:53 UTC | 2026-07-22 19:49 UTC | 55m |
| TWIST63 | TWI | Dave Eby Field (4XA5) | Ksa Orchards Airport (OK11) | 2026-07-22 19:13 UTC | 2026-07-22 19:47 UTC | 33m |
| UAV13 | UAV | Hansen Airport (11CL) | Apple Valley Airport (KAPV) | 2026-07-22 14:56 UTC | 2026-07-22 19:43 UTC | 4h 47m |
| UAL316 | United Airlines | Dublin Airport (EIDW) | Newark Liberty International Airport (KEWR) | 2026-07-22 12:48 UTC | 2026-07-22 19:42 UTC | 6h 53m |
| N893AP |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-07-22 19:02 UTC | 2026-07-22 19:38 UTC | 36m |
| N365PT |  | Blue Grass Airport (KLEX) | Rainelle Airport (WV30) | 2026-07-22 19:02 UTC | 2026-07-22 19:36 UTC | 34m |
| CGEBB | CGE | Calgary / Springbank Airport (CYBW) | Sundre Airport (CFN7) | 2026-07-22 19:07 UTC | 2026-07-22 19:35 UTC | 28m |
| N529BK |  | Pilgrim's Home Airfield (2NH5) | Lebanon Municipal Airport (KLEB) | 2026-07-22 18:38 UTC | 2026-07-22 19:32 UTC | 53m |
| CFR94 | CFR | Redding Regional Airport (KRDD) | Bodad Airport (CA11) | 2026-07-22 19:16 UTC | 2026-07-22 19:30 UTC | 14m |
| N3476J |  | Tulelake Municipal Airport (KO81) | Tulelake Municipal Airport (KO81) | 2026-07-22 19:12 UTC | 2026-07-22 19:29 UTC | 17m |
| IGO43F | IndiGo | Indira Gandhi International Airport (VIDP) | Abu Dhabi International Airport (OMAA) | 2026-07-22 16:12 UTC | 2026-07-22 19:28 UTC | 3h 15m |
| N929TG |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-07-22 18:59 UTC | 2026-07-22 19:27 UTC | 27m |
| XBPBH | XBP | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-07-22 18:56 UTC | 2026-07-22 19:24 UTC | 28m |
| Q130 |  | Montréal / St-Hubert Airport (CYHU) | Montréal / St-Hubert Airport (CYHU) | 2026-07-22 19:09 UTC | 2026-07-22 19:23 UTC | 14m |
| TKR914 | TKR | Mc Clellan Airfield (KMCC) | Mammoth Yosemite Airport (KMMH) | 2026-07-22 18:55 UTC | 2026-07-22 19:23 UTC | 27m |
| C6565 |  | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-07-22 18:14 UTC | 2026-07-22 19:23 UTC | 1h 8m |
| C6540 |  | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-07-22 18:44 UTC | 2026-07-22 19:22 UTC | 37m |
| N77ZR |  | Creve Coeur Airport (K1H0) | Blackhawk Airport (6MO0) | 2026-07-22 19:06 UTC | 2026-07-22 19:21 UTC | 15m |
| N13WT |  | Center Island Airport (78WA) | Renton Municipal Airport (KRNT) | 2026-07-22 18:44 UTC | 2026-07-22 19:21 UTC | 37m |
| N1495T |  | Rickenbacker International Airport (KLCK) | Leesburg Executive Airport (KJYO) | 2026-07-22 18:02 UTC | 2026-07-22 19:21 UTC | 1h 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
