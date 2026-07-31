# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_07:18:07_UTC-green)

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

**Latest saved flight:** 2026-07-31 07:18:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-31 07:18:07 UTC

- **161,993** saved flights
- **53,424** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **161,993** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,942,771.5 tonnes** estimated CO2 emissions
- **112,624,436 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6471 |
| 2 | SkyWest Airlines | 5910 |
| 3 | EJA | 3210 |
| 4 | IndiGo | 2836 |
| 5 | American Airlines | 2562 |
| 6 | Southwest Airlines | 2539 |
| 7 | ENY | 2018 |
| 8 | Delta Air Lines | 1923 |
| 9 | Lufthansa | 1525 |
| 10 | LATAM Airlines | 1523 |
| 11 | AZU | 1422 |
| 12 | WIF | 1370 |
| 13 | Vueling | 1344 |
| 14 | LXJ | 1261 |
| 15 | AXM | 1125 |
| 16 | Swiss International | 1113 |
| 17 | easyJet | 1058 |
| 18 | Alaska Airlines | 1007 |
| 19 | QLK | 1002 |
| 20 | All Nippon Airways | 996 |
| 21 | EJU | 996 |
| 22 | VIV | 892 |
| 23 | CXK | 865 |
| 24 | United Airlines | 855 |
| 25 | Cathay Pacific | 854 |
| 26 | GLO | 850 |
| 27 | AEE | 849 |
| 28 | MXY | 840 |
| 29 | Air France | 837 |
| 30 | JetBlue | 827 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 139997 |
| 2 | 🇪🇸 ES | 10365 |
| 3 | 🇧🇷 BR | 9252 |
| 4 | 🇦🇺 AU | 9192 |
| 5 | 🇮🇳 IN | 8926 |
| 6 | 🇨🇦 CA | 8813 |
| 7 | 🇮🇹 IT | 8339 |
| 8 | 🇩🇪 DE | 8155 |
| 9 | 🇬🇧 GB | 7419 |
| 10 | 🇯🇵 JP | 6565 |
| 11 | 🇫🇷 FR | 6395 |
| 12 | 🇨🇴 CO | 5756 |
| 13 | 🇲🇽 MX | 4651 |
| 14 | 🇬🇷 GR | 4649 |
| 15 | 🇳🇴 NO | 4275 |
| 16 | 🇨🇭 CH | 4242 |
| 17 | 🇹🇷 TR | 3858 |
| 18 | 🇲🇾 MY | 2923 |
| 19 | 🇵🇱 PL | 2746 |
| 20 | 🇿🇦 ZA | 2609 |
| 21 | 🇳🇿 NZ | 2380 |
| 22 | 🇹🇭 TH | 2296 |
| 23 | 🇵🇭 PH | 2130 |
| 24 | 🇰🇷 KR | 2115 |
| 25 | 🇬🇹 GT | 2077 |
| 26 | 🇲🇦 MA | 1630 |
| 27 | 🇲🇪 ME | 1529 |
| 28 | 🇭🇷 HR | 1511 |
| 29 | 🇳🇱 NL | 1480 |
| 30 | 🇲🇴 MO | 1348 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3312 |
| 2 | Denver International Airport |  | US | 2694 |
| 3 | Tokyo International Airport |  | JP | 2072 |
| 4 | Guaymaral Airport |  | CO | 2035 |
| 5 | Indira Gandhi International Airport |  | IN | 1985 |
| 6 | Harry Reid International Airport |  | US | 1967 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1789 |
| 8 | Zurich Airport |  | CH | 1724 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1701 |
| 10 | La Aurora Airport |  | GT | 1613 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1507 |
| 12 | El Dorado International Airport |  | CO | 1483 |
| 13 | Frankfurt am Main International Airport |  | DE | 1474 |
| 14 | Chicago O'Hare International Airport |  | US | 1468 |
| 15 | Salt Lake City International Airport |  | US | 1458 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1353 |
| 17 | Macau International Airport |  | MO | 1348 |
| 18 | Congonhas Airport |  | BR | 1345 |
| 19 | Madrid Barajas International Airport |  | ES | 1280 |
| 20 | Capua Airport |  | IT | 1274 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1238 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1157 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1149 |
| 24 | Charlotte/Douglas International Airport |  | US | 1140 |
| 25 | Kuala Lumpur International Airport |  | MY | 1115 |
| 26 | Charles de Gaulle International Airport |  | FR | 1104 |
| 27 | Malpensa International Airport |  | IT | 1071 |
| 28 | Bengaluru International Airport |  | IN | 1060 |
| 29 | Ninoy Aquino International Airport |  | PH | 1000 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 991 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 984 |
| 32 | Barcelona International Airport |  | ES | 961 |
| 33 | Daniel K Inouye International Airport |  | US | 952 |
| 34 | Seattle-Tacoma International Airport |  | US | 941 |
| 35 | Calgary International Airport |  | CA | 928 |
| 36 | Viracopos International Airport |  | BR | 922 |
| 37 | Scottsdale Airport |  | US | 908 |
| 38 | Tenerife Norte Airport |  | ES | 907 |
| 39 | Oslo Gardermoen Airport |  | NO | 900 |
| 40 | Reno/Tahoe International Airport |  | US | 889 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 853 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 591 | 21m | 244 km | 2,488.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 387 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 386 | 24m | 225 km | 1,497.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 371 | 1h 9m | 770 km | 4,928.4 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 296 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 283 | 27m | 275 km | 1,341.0 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 239 | 22m | 55 km | 227.2 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 238 | 19m | 165 km | 677.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 234 | 44m | 241 km | 972.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 222 | 1h 47m | 1,423 km | 5,448.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 204 | 20m | 250 km | 881.2 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 204 | 20m | 99 km | 349.4 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 198 | 30m | 49 km | 167.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 193 | 1h 15m | 961 km | 3,199.1 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 193 | 28m | 152 km | 504.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 191 | 18m | 144 km | 475.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 182 | 1h 39m | 1,156 km | 3,630.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 180 | 1h 1m | 695 km | 2,157.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 178 | 44m | 452 km | 1,387.3 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 173 | 1h 49m | 1,304 km | 3,892.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LBQ790 | LBQ | Teterboro Airport (KTEB) | Manassas Regional/Harry P Davis Field (KHEF) | 2026-07-31 06:10 UTC | 2026-07-31 07:18 UTC | 1h 7m |
| CPA256 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-07-30 20:06 UTC | 2026-07-31 07:16 UTC | 11h 9m |
| CPA750 | Cathay Pacific | Suvarnabhumi Airport (VTBS) | Chek Lap Kok International Airport (VHHH) | 2026-07-31 04:49 UTC | 2026-07-31 07:14 UTC | 2h 24m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-07-30 19:23 UTC | 2026-07-31 07:03 UTC | 11h 40m |
| IXD | IXD | Nowra Airport (YSNW) | Sydney Bankstown Airport (YSBK) | 2026-07-31 06:33 UTC | 2026-07-31 07:03 UTC | 30m |
| CPA3295 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-07-30 16:08 UTC | 2026-07-31 06:59 UTC | 14h 50m |
| DLH796 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-07-30 20:21 UTC | 2026-07-31 06:56 UTC | 10h 35m |
| ASD0291 | ASD | Sfax Thyna International Airport (DTTX) | Sfax Thyna International Airport (DTTX) | 2026-07-31 06:43 UTC | 2026-07-31 06:55 UTC | 11m |
| SPLFD | SPL | Piotrkow Trybunalski-Bujny Airport (EPPT) | Piotrkow Trybunalski-Bujny Airport (EPPT) | 2026-07-31 06:08 UTC | 2026-07-31 06:53 UTC | 45m |
| VLG2SK | Vueling | Barcelona International Airport (LEBL) | Decimomannu Airport (LIED) | 2026-07-31 05:57 UTC | 2026-07-31 06:50 UTC | 52m |
| QTR8022 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-07-30 22:50 UTC | 2026-07-31 06:47 UTC | 7h 56m |
| EZY605D | easyJet | Glasgow International Airport (EGPF) | Belfast International Airport (EGAA) | 2026-07-30 19:59 UTC | 2026-07-31 06:46 UTC | 10h 46m |
| WIF4X | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-07-31 06:07 UTC | 2026-07-31 06:44 UTC | 37m |
| KAL2002 | Korean Air | Chek Lap Kok International Airport (VHHH) | Taipei Songshan Airport (RCSS) | 2026-07-31 05:29 UTC | 2026-07-31 06:43 UTC | 1h 13m |
| N7488W |  | Ed Carlson Memorial Field/South Lewis County Airport (KTDO) | Olympia Regional Airport (KOLM) | 2026-07-31 06:22 UTC | 2026-07-31 06:40 UTC | 18m |
| RYR20NM | Ryanair | Poznań-Ławica Airport (EPPO) | Luqa Airport (LMML) | 2026-07-31 04:10 UTC | 2026-07-31 06:39 UTC | 2h 29m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-07-31 05:48 UTC | 2026-07-31 06:39 UTC | 50m |
| RYR976 | Ryanair | Faro Airport (LPFR) | Kenitra Airport (GMMY) | 2026-07-31 05:55 UTC | 2026-07-31 06:35 UTC | 39m |
| GBA619 | GBA | Auckland International Airport (NZAA) | Dargaville Aerodrome (NZDA) | 2026-07-31 05:56 UTC | 2026-07-31 06:34 UTC | 38m |
| ASD0291 | ASD | Sfax Thyna International Airport (DTTX) | Sfax Thyna International Airport (DTTX) | 2026-07-31 06:08 UTC | 2026-07-31 06:33 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
