# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--22_16:01:44_UTC-green)

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

**Latest saved flight:** 2026-07-22 16:01:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-22 16:01:44 UTC

- **143,968** saved flights
- **48,234** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **143,968** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,725,575.0 tonnes** estimated CO2 emissions
- **100,033,335 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5849 |
| 2 | SkyWest Airlines | 5261 |
| 3 | EJA | 2835 |
| 4 | IndiGo | 2616 |
| 5 | American Airlines | 2305 |
| 6 | Southwest Airlines | 2172 |
| 7 | ENY | 1788 |
| 8 | Delta Air Lines | 1706 |
| 9 | Lufthansa | 1442 |
| 10 | LATAM Airlines | 1325 |
| 11 | AZU | 1238 |
| 12 | Vueling | 1235 |
| 13 | WIF | 1230 |
| 14 | LXJ | 1103 |
| 15 | AXM | 1063 |
| 16 | Swiss International | 1024 |
| 17 | easyJet | 939 |
| 18 | All Nippon Airways | 922 |
| 19 | Alaska Airlines | 909 |
| 20 | QLK | 906 |
| 21 | EJU | 881 |
| 22 | VIV | 801 |
| 23 | CXK | 772 |
| 24 | AEE | 764 |
| 25 | Air France | 763 |
| 26 | JetBlue | 761 |
| 27 | Cathay Pacific | 748 |
| 28 | MXY | 748 |
| 29 | United Airlines | 746 |
| 30 | GLO | 738 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 123893 |
| 2 | 🇪🇸 ES | 9359 |
| 3 | 🇦🇺 AU | 8242 |
| 4 | 🇮🇳 IN | 8199 |
| 5 | 🇧🇷 BR | 8127 |
| 6 | 🇨🇦 CA | 7608 |
| 7 | 🇮🇹 IT | 7504 |
| 8 | 🇩🇪 DE | 7441 |
| 9 | 🇬🇧 GB | 6583 |
| 10 | 🇯🇵 JP | 6036 |
| 11 | 🇫🇷 FR | 5738 |
| 12 | 🇨🇴 CO | 4642 |
| 13 | 🇲🇽 MX | 4186 |
| 14 | 🇬🇷 GR | 4083 |
| 15 | 🇳🇴 NO | 3846 |
| 16 | 🇨🇭 CH | 3740 |
| 17 | 🇹🇷 TR | 3387 |
| 18 | 🇲🇾 MY | 2775 |
| 19 | 🇵🇱 PL | 2425 |
| 20 | 🇿🇦 ZA | 2348 |
| 21 | 🇳🇿 NZ | 2209 |
| 22 | 🇹🇭 TH | 2129 |
| 23 | 🇰🇷 KR | 2037 |
| 24 | 🇵🇭 PH | 1934 |
| 25 | 🇬🇹 GT | 1883 |
| 26 | 🇲🇦 MA | 1498 |
| 27 | 🇲🇪 ME | 1428 |
| 28 | 🇳🇱 NL | 1352 |
| 29 | 🇭🇷 HR | 1310 |
| 30 | 🇲🇴 MO | 1205 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2971 |
| 2 | Denver International Airport |  | US | 2414 |
| 3 | Tokyo International Airport |  | JP | 1942 |
| 4 | Indira Gandhi International Airport |  | IN | 1817 |
| 5 | Harry Reid International Airport |  | US | 1804 |
| 6 | Guaymaral Airport |  | CO | 1758 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1639 |
| 8 | Zurich Airport |  | CH | 1595 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1509 |
| 10 | La Aurora Airport |  | GT | 1458 |
| 11 | Frankfurt am Main International Airport |  | DE | 1388 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1358 |
| 13 | Chicago O'Hare International Airport |  | US | 1341 |
| 14 | Salt Lake City International Airport |  | US | 1288 |
| 15 | El Dorado International Airport |  | CO | 1274 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1259 |
| 17 | Macau International Airport |  | MO | 1205 |
| 18 | Capua Airport |  | IT | 1171 |
| 19 | Congonhas Airport |  | BR | 1156 |
| 20 | Madrid Barajas International Airport |  | ES | 1149 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1137 |
| 22 | Kuala Lumpur International Airport |  | MY | 1072 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1043 |
| 24 | Charlotte/Douglas International Airport |  | US | 1035 |
| 25 | Charles de Gaulle International Airport |  | FR | 1008 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1006 |
| 27 | Bengaluru International Airport |  | IN | 979 |
| 28 | Malpensa International Airport |  | IT | 931 |
| 29 | Ninoy Aquino International Airport |  | PH | 903 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 882 |
| 31 | Barcelona International Airport |  | ES | 876 |
| 32 | Daniel K Inouye International Airport |  | US | 875 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 857 |
| 34 | Tenerife Norte Airport |  | ES | 827 |
| 35 | Seattle-Tacoma International Airport |  | US | 821 |
| 36 | Calgary International Airport |  | CA | 819 |
| 37 | Viracopos International Airport |  | BR | 818 |
| 38 | Amsterdam Airport Schiphol |  | NL | 813 |
| 39 | Scottsdale Airport |  | US | 812 |
| 40 | Vitoria/Foronda Airport |  | ES | 788 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 741 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 524 | 21m | 244 km | 2,206.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 351 | 24m | 225 km | 1,361.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 349 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 340 | 1h 9m | 770 km | 4,516.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 260 | 26m | 275 km | 1,232.0 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 257 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 214 | 22m | 55 km | 203.4 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 193 | 26m | 215 km | 714.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 193 | 1h 46m | 1,423 km | 4,736.5 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 192 | 44m | 241 km | 797.5 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 190 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 179 | 20m | 250 km | 773.2 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 172 | 18m | 144 km | 427.8 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 168 | 44m | 452 km | 1,309.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 168 | 1h 16m | 961 km | 2,784.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 164 | 1h 38m | 1,156 km | 3,271.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 164 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N7908L |  | Spokane International Airport (KGEG) | Deer Park Airport (KDEW) | 2026-07-22 15:16 UTC | 2026-07-22 16:01 UTC | 45m |
| BREW82 | BRE | Randolph Afb Airport (KRND) | Victoria Regional Airport (KVCT) | 2026-07-22 15:40 UTC | 2026-07-22 15:59 UTC | 19m |
| N7646G |  | Mc Clellan-Palomar Airport (KCRQ) | Ramona Airport (KRNM) | 2026-07-22 15:40 UTC | 2026-07-22 15:58 UTC | 17m |
| WIRE31 | WIR | Enid Woodring Regional Airport (KWDG) | Lariat Ranch Airport (OK42) | 2026-07-22 15:34 UTC | 2026-07-22 15:53 UTC | 19m |
| CPA337 | Cathay Pacific | Beijing Capital International Airport (ZBAA) | Zhuhai Airport (ZGSD) | 2026-07-22 13:03 UTC | 2026-07-22 15:53 UTC | 2h 49m |
| N6908B |  | Meriden Markham Municipal Airport (KMMK) | Windham Airport (KIJD) | 2026-07-22 15:19 UTC | 2026-07-22 15:53 UTC | 33m |
| CTM1232 | CTM | Zaragoza Air Base (LEZG) | Evreux-Fauville (BA 105) Air Base (LFOE) | 2026-07-22 13:57 UTC | 2026-07-22 15:42 UTC | 1h 44m |
| N894SA |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-07-22 15:11 UTC | 2026-07-22 15:41 UTC | 30m |
| N354PC |  | Merced Yosemite Regional Airport (KMCE) | Merced Yosemite Regional Airport (KMCE) | 2026-07-22 15:23 UTC | 2026-07-22 15:40 UTC | 16m |
| EPI259 | EPI | Herlong Recreational Airport (KHEG) | Cecil Airport (KVQQ) | 2026-07-22 14:33 UTC | 2026-07-22 15:37 UTC | 1h 3m |
| N83PM |  | Conroe/North Houston Regional Airport (KCXO) | Austin-Bergstrom International Airport (KAUS) | 2026-07-22 15:04 UTC | 2026-07-22 15:34 UTC | 29m |
| EFD3T | EFD | Stuttgart Airport (EDDS) | Mauterndorf Airport (LOSM) | 2026-07-22 14:57 UTC | 2026-07-22 15:32 UTC | 34m |
| DFL5710 | DFL | Stockholm-Arlanda Airport (ESSA) | Stockholm-Bromma Airport (ESSB) | 2026-07-22 15:16 UTC | 2026-07-22 15:28 UTC | 11m |
| CXK284 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-22 14:51 UTC | 2026-07-22 15:28 UTC | 36m |
| N697CA |  | Dallas Executive Airport (KRBD) | Dallas Executive Airport (KRBD) | 2026-07-22 14:07 UTC | 2026-07-22 15:27 UTC | 1h 20m |
| N51236 |  | Ragwing Acres Airport (2OK4) | Eagle Creek Airport (51OK) | 2026-07-22 15:06 UTC | 2026-07-22 15:27 UTC | 20m |
| AAH552 | AAH | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-07-22 15:06 UTC | 2026-07-22 15:26 UTC | 20m |
| N876LA |  | Washington Municipal Airport (KAWG) | 5IA7 (5IA7) | 2026-07-22 15:22 UTC | 2026-07-22 15:26 UTC | 3m |
| TIBKY | TIB | Juan Santamaria International Airport (MROC) | Portalon Airport (MRPL) | 2026-07-22 15:11 UTC | 2026-07-22 15:26 UTC | 14m |
| RNGR833 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Ingleside Regional Airport (KTFP) | 2026-07-22 14:59 UTC | 2026-07-22 15:25 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
