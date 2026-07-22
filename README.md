# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--22_23:03:43_UTC-green)

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

**Latest saved flight:** 2026-07-22 23:03:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-22 23:03:43 UTC

- **144,902** saved flights
- **48,525** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **144,902** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,736,969.2 tonnes** estimated CO2 emissions
- **100,693,866 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5889 |
| 2 | SkyWest Airlines | 5308 |
| 3 | EJA | 2857 |
| 4 | IndiGo | 2624 |
| 5 | American Airlines | 2320 |
| 6 | Southwest Airlines | 2191 |
| 7 | ENY | 1804 |
| 8 | Delta Air Lines | 1719 |
| 9 | Lufthansa | 1444 |
| 10 | LATAM Airlines | 1336 |
| 11 | AZU | 1250 |
| 12 | WIF | 1237 |
| 13 | Vueling | 1236 |
| 14 | LXJ | 1117 |
| 15 | AXM | 1063 |
| 16 | Swiss International | 1029 |
| 17 | easyJet | 942 |
| 18 | All Nippon Airways | 922 |
| 19 | Alaska Airlines | 912 |
| 20 | QLK | 907 |
| 21 | EJU | 886 |
| 22 | VIV | 807 |
| 23 | CXK | 777 |
| 24 | AEE | 766 |
| 25 | JetBlue | 765 |
| 26 | Air France | 764 |
| 27 | MXY | 758 |
| 28 | Cathay Pacific | 757 |
| 29 | United Airlines | 752 |
| 30 | GLO | 744 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 124952 |
| 2 | 🇪🇸 ES | 9393 |
| 3 | 🇦🇺 AU | 8252 |
| 4 | 🇮🇳 IN | 8219 |
| 5 | 🇧🇷 BR | 8189 |
| 6 | 🇨🇦 CA | 7681 |
| 7 | 🇮🇹 IT | 7540 |
| 8 | 🇩🇪 DE | 7466 |
| 9 | 🇬🇧 GB | 6605 |
| 10 | 🇯🇵 JP | 6037 |
| 11 | 🇫🇷 FR | 5756 |
| 12 | 🇨🇴 CO | 4731 |
| 13 | 🇲🇽 MX | 4225 |
| 14 | 🇬🇷 GR | 4100 |
| 15 | 🇳🇴 NO | 3869 |
| 16 | 🇨🇭 CH | 3753 |
| 17 | 🇹🇷 TR | 3397 |
| 18 | 🇲🇾 MY | 2775 |
| 19 | 🇵🇱 PL | 2441 |
| 20 | 🇿🇦 ZA | 2350 |
| 21 | 🇳🇿 NZ | 2211 |
| 22 | 🇹🇭 TH | 2130 |
| 23 | 🇰🇷 KR | 2037 |
| 24 | 🇵🇭 PH | 1934 |
| 25 | 🇬🇹 GT | 1887 |
| 26 | 🇲🇦 MA | 1503 |
| 27 | 🇲🇪 ME | 1440 |
| 28 | 🇳🇱 NL | 1357 |
| 29 | 🇭🇷 HR | 1320 |
| 30 | 🇲🇴 MO | 1212 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2992 |
| 2 | Denver International Airport |  | US | 2429 |
| 3 | Tokyo International Airport |  | JP | 1942 |
| 4 | Indira Gandhi International Airport |  | IN | 1824 |
| 5 | Harry Reid International Airport |  | US | 1817 |
| 6 | Guaymaral Airport |  | CO | 1775 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1644 |
| 8 | Zurich Airport |  | CH | 1601 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1523 |
| 10 | La Aurora Airport |  | GT | 1462 |
| 11 | Frankfurt am Main International Airport |  | DE | 1392 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1369 |
| 13 | Chicago O'Hare International Airport |  | US | 1349 |
| 14 | Salt Lake City International Airport |  | US | 1300 |
| 15 | El Dorado International Airport |  | CO | 1293 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1262 |
| 17 | Macau International Airport |  | MO | 1212 |
| 18 | Capua Airport |  | IT | 1179 |
| 19 | Congonhas Airport |  | BR | 1164 |
| 20 | Madrid Barajas International Airport |  | ES | 1155 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1145 |
| 22 | Kuala Lumpur International Airport |  | MY | 1072 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1044 |
| 24 | Charlotte/Douglas International Airport |  | US | 1041 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1014 |
| 26 | Charles de Gaulle International Airport |  | FR | 1009 |
| 27 | Bengaluru International Airport |  | IN | 981 |
| 28 | Malpensa International Airport |  | IT | 936 |
| 29 | Ninoy Aquino International Airport |  | PH | 903 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 889 |
| 31 | Barcelona International Airport |  | ES | 880 |
| 32 | Daniel K Inouye International Airport |  | US | 877 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 863 |
| 34 | Tenerife Norte Airport |  | ES | 829 |
| 35 | Viracopos International Airport |  | BR | 825 |
| 36 | Seattle-Tacoma International Airport |  | US | 825 |
| 37 | Calgary International Airport |  | CA | 822 |
| 38 | Scottsdale Airport |  | US | 821 |
| 39 | Amsterdam Airport Schiphol |  | NL | 817 |
| 40 | Oslo Gardermoen Airport |  | NO | 795 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 748 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 526 | 21m | 244 km | 2,214.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 351 | 24m | 225 km | 1,361.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 351 | 9m | - | - |
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
| CFR74 | CFR | Paso Robles Municipal Airport (KPRB) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-07-22 22:47 UTC | 2026-07-22 23:03 UTC | 16m |
| N120B |  | Montgomery-Gibbs Executive Airport (KMYF) | Big Bear City Airport (KL35) | 2026-07-22 21:46 UTC | 2026-07-22 22:58 UTC | 1h 11m |
| N622PK |  | Norwood Memorial Airport (KOWD) | Worcester Regional Airport (KORH) | 2026-07-22 21:20 UTC | 2026-07-22 22:56 UTC | 1h 36m |
| CPA698 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-07-22 11:41 UTC | 2026-07-22 22:55 UTC | 11h 14m |
| N10EH |  | Salt Lake City International Airport (KSLC) | Rock & A Hard Place Ranch Airport (WY61) | 2026-07-22 22:13 UTC | 2026-07-22 22:55 UTC | 41m |
| CFGMF | CFG | Brampton Airport (CNC3) | Dundalk (Tripp Field) (CTF4) | 2026-07-22 22:22 UTC | 2026-07-22 22:54 UTC | 32m |
| AER122 | AER | Ted Stevens Anchorage International Airport (PANC) | Fairbanks International Airport (PAFA) | 2026-07-22 21:51 UTC | 2026-07-22 22:53 UTC | 1h 2m |
|  |  | Barrie-Orillia (Lake Simcoe Regional Airport) (CYLS) | Mattawa Airport (CMA2) | 2026-07-22 22:06 UTC | 2026-07-22 22:53 UTC | 47m |
| N502RP |  | Oakland County International Airport (KPTK) | Scottsdale Airport (KSDL) | 2026-07-22 19:15 UTC | 2026-07-22 22:53 UTC | 3h 37m |
| N858MG |  | Red Wing Regional Airport (KRGK) | Price County Airport (KPBH) | 2026-07-22 22:32 UTC | 2026-07-22 22:52 UTC | 19m |
| N49MR |  | Merrill Field (PAMR) | Birchwood Airport (PABV) | 2026-07-22 22:30 UTC | 2026-07-22 22:51 UTC | 21m |
| N971MB |  | Jones Airport (42NE) | Rocky Mountain Metro Airport (KBJC) | 2026-07-22 22:11 UTC | 2026-07-22 22:50 UTC | 39m |
| N542SA |  | San Martin Airport (KE16) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-07-22 22:37 UTC | 2026-07-22 22:49 UTC | 12m |
| BOE427 | BOE | Boeing Field/King County International Airport (KBFI) | Warden Airport (K2S4) | 2026-07-22 21:28 UTC | 2026-07-22 22:46 UTC | 1h 18m |
| YGW | YGW | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-07-22 21:57 UTC | 2026-07-22 22:46 UTC | 49m |
| N32EL |  | King Salmon Airport (PAKN) | Igiugig Airport (PAIG) | 2026-07-22 22:33 UTC | 2026-07-22 22:44 UTC | 11m |
| N144NE |  | Laurence G Hanscom Field (KBED) | Manchester Boston Regional Airport (KMHT) | 2026-07-22 22:26 UTC | 2026-07-22 22:40 UTC | 14m |
| PRE31 | PRE | 1NE6 (1NE6) | Reisig Brothers Airport (12NE) | 2026-07-22 22:27 UTC | 2026-07-22 22:40 UTC | 12m |
| EJA180 | EJA | San Luis Obispo County Regional Airport (KSBP) | Oakland San Francisco Bay Airport (KOAK) | 2026-07-22 22:00 UTC | 2026-07-22 22:37 UTC | 36m |
| AAL2424 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-07-22 21:12 UTC | 2026-07-22 22:35 UTC | 1h 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
