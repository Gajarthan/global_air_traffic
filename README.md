# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_19:52:48_UTC-green)

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

**Latest saved flight:** 2026-07-28 19:52:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-28 19:52:48 UTC

- **157,144** saved flights
- **52,169** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **157,144** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,884,126.5 tonnes** estimated CO2 emissions
- **109,224,726 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6319 |
| 2 | SkyWest Airlines | 5753 |
| 3 | EJA | 3111 |
| 4 | IndiGo | 2775 |
| 5 | American Airlines | 2506 |
| 6 | Southwest Airlines | 2469 |
| 7 | ENY | 1962 |
| 8 | Delta Air Lines | 1867 |
| 9 | Lufthansa | 1507 |
| 10 | LATAM Airlines | 1466 |
| 11 | AZU | 1374 |
| 12 | WIF | 1327 |
| 13 | Vueling | 1317 |
| 14 | LXJ | 1213 |
| 15 | AXM | 1102 |
| 16 | Swiss International | 1090 |
| 17 | easyJet | 1025 |
| 18 | Alaska Airlines | 983 |
| 19 | All Nippon Airways | 973 |
| 20 | QLK | 972 |
| 21 | EJU | 965 |
| 22 | VIV | 862 |
| 23 | United Airlines | 837 |
| 24 | CXK | 833 |
| 25 | AEE | 824 |
| 26 | GLO | 824 |
| 27 | Cathay Pacific | 819 |
| 28 | MXY | 817 |
| 29 | Air France | 816 |
| 30 | JetBlue | 816 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 135629 |
| 2 | 🇪🇸 ES | 10132 |
| 3 | 🇧🇷 BR | 8953 |
| 4 | 🇦🇺 AU | 8857 |
| 5 | 🇮🇳 IN | 8727 |
| 6 | 🇨🇦 CA | 8490 |
| 7 | 🇮🇹 IT | 8107 |
| 8 | 🇩🇪 DE | 7968 |
| 9 | 🇬🇧 GB | 7222 |
| 10 | 🇯🇵 JP | 6420 |
| 11 | 🇫🇷 FR | 6216 |
| 12 | 🇨🇴 CO | 5503 |
| 13 | 🇲🇽 MX | 4512 |
| 14 | 🇬🇷 GR | 4484 |
| 15 | 🇳🇴 NO | 4154 |
| 16 | 🇨🇭 CH | 4114 |
| 17 | 🇹🇷 TR | 3758 |
| 18 | 🇲🇾 MY | 2871 |
| 19 | 🇵🇱 PL | 2682 |
| 20 | 🇿🇦 ZA | 2546 |
| 21 | 🇳🇿 NZ | 2329 |
| 22 | 🇹🇭 TH | 2261 |
| 23 | 🇰🇷 KR | 2091 |
| 24 | 🇵🇭 PH | 2066 |
| 25 | 🇬🇹 GT | 2020 |
| 26 | 🇲🇦 MA | 1602 |
| 27 | 🇲🇪 ME | 1515 |
| 28 | 🇭🇷 HR | 1450 |
| 29 | 🇳🇱 NL | 1434 |
| 30 | 🇲🇴 MO | 1293 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3230 |
| 2 | Denver International Airport |  | US | 2636 |
| 3 | Tokyo International Airport |  | JP | 2035 |
| 4 | Guaymaral Airport |  | CO | 1974 |
| 5 | Indira Gandhi International Airport |  | IN | 1942 |
| 6 | Harry Reid International Airport |  | US | 1922 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1741 |
| 8 | Zurich Airport |  | CH | 1691 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1648 |
| 10 | La Aurora Airport |  | GT | 1566 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1466 |
| 12 | Frankfurt am Main International Airport |  | DE | 1457 |
| 13 | Chicago O'Hare International Airport |  | US | 1429 |
| 14 | El Dorado International Airport |  | CO | 1426 |
| 15 | Salt Lake City International Airport |  | US | 1415 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1321 |
| 17 | Macau International Airport |  | MO | 1293 |
| 18 | Congonhas Airport |  | BR | 1287 |
| 19 | Madrid Barajas International Airport |  | ES | 1249 |
| 20 | Capua Airport |  | IT | 1235 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1205 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1124 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1118 |
| 24 | Charlotte/Douglas International Airport |  | US | 1112 |
| 25 | Kuala Lumpur International Airport |  | MY | 1099 |
| 26 | Charles de Gaulle International Airport |  | FR | 1078 |
| 27 | Bengaluru International Airport |  | IN | 1037 |
| 28 | Malpensa International Airport |  | IT | 1033 |
| 29 | Ninoy Aquino International Airport |  | PH | 968 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 954 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 949 |
| 32 | Barcelona International Airport |  | ES | 938 |
| 33 | Daniel K Inouye International Airport |  | US | 927 |
| 34 | Seattle-Tacoma International Airport |  | US | 915 |
| 35 | Calgary International Airport |  | CA | 901 |
| 36 | Tenerife Norte Airport |  | ES | 894 |
| 37 | Viracopos International Airport |  | BR | 889 |
| 38 | Scottsdale Airport |  | US | 889 |
| 39 | Oslo Gardermoen Airport |  | NO | 868 |
| 40 | Amsterdam Airport Schiphol |  | NL | 865 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 829 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 566 | 21m | 244 km | 2,383.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 376 | 24m | 225 km | 1,458.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 376 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 361 | 1h 9m | 770 km | 4,795.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 288 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 277 | 27m | 275 km | 1,312.6 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 219 | 44m | 241 km | 909.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 213 | 1h 47m | 1,423 km | 5,227.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 206 | 26m | 215 km | 762.9 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 202 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 199 | 20m | 250 km | 859.6 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 188 | 30m | 49 km | 158.9 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 187 | 18m | 144 km | 465.2 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 185 | 1h 15m | 961 km | 3,066.5 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 182 | 31m | 369 km | 1,158.5 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 181 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 177 | 50m | 556 km | 1,696.7 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 176 | 1h 39m | 1,156 km | 3,511.1 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 176 | 44m | 452 km | 1,371.7 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 174 | 1h 1m | 695 km | 2,085.7 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 50m | 1,304 km | 3,734.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PGT1576 | PGT | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-07-28 16:46 UTC | 2026-07-28 19:52 UTC | 3h 6m |
| N871DG |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-07-28 19:05 UTC | 2026-07-28 19:41 UTC | 36m |
| UCM472 | UCM | 1MU4 (1MU4) | 4MO0 (4MO0) | 2026-07-28 19:17 UTC | 2026-07-28 19:40 UTC | 22m |
| N6966M |  | Enumclaw Airport (WA77) | Auburn Municipal Airport (KS50) | 2026-07-28 18:16 UTC | 2026-07-28 19:38 UTC | 1h 21m |
| HNW200 | HNW | Cochise County Airport (KP33) | Cochise County Airport (KP33) | 2026-07-28 19:24 UTC | 2026-07-28 19:35 UTC | 10m |
| N76KA |  | Roche Harbor Airport (WA09) | Boeing Field/King County International Airport (KBFI) | 2026-07-28 18:55 UTC | 2026-07-28 19:35 UTC | 39m |
| N821TN |  | Kansas City Downtown/Wheeler Field (KMKC) | Jesse Viertel Memorial Airport (KVER) | 2026-07-28 19:17 UTC | 2026-07-28 19:33 UTC | 15m |
| N735FT |  | Banning Municipal Airport (KBNG) | Whiteman Airport (KWHP) | 2026-07-28 18:55 UTC | 2026-07-28 19:30 UTC | 35m |
| CRN101T | CRN | Kelowna Airport (CYLW) | Princeton Airport (CYDC) | 2026-07-28 19:09 UTC | 2026-07-28 19:28 UTC | 18m |
| MNL99 | MNL | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-07-28 18:46 UTC | 2026-07-28 19:23 UTC | 37m |
| LANCE51 | LAN | Joseph Of Cupertino Stolport Airport (TS20) | Joseph Of Cupertino Stolport Airport (TS20) | 2026-07-28 19:10 UTC | 2026-07-28 19:21 UTC | 11m |
| N931T |  | Magee Municipal Airport (K17M) | Mobile International Airport (KBFM) | 2026-07-28 18:49 UTC | 2026-07-28 19:19 UTC | 29m |
| MHF309 | MHF | Soldotna Airport (PASX) | Alaska Airpark (AK01) | 2026-07-28 19:06 UTC | 2026-07-28 19:18 UTC | 12m |
| N565TA |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-28 18:45 UTC | 2026-07-28 19:17 UTC | 32m |
| PAT299 | PAT | Truckee-Tahoe Airport (KTRK) | Sacramento Mather Airport (KMHR) | 2026-07-28 16:28 UTC | 2026-07-28 19:16 UTC | 2h 48m |
| N685PS |  | Pensacola International Airport (KPNS) | KNUN (KNUN) | 2026-07-28 18:55 UTC | 2026-07-28 19:15 UTC | 19m |
| N5581G |  | Laurel Municipal Airport (K6S8) | Laurel Municipal Airport (K6S8) | 2026-07-28 18:48 UTC | 2026-07-28 19:14 UTC | 25m |
| XSN06 | XSN | San Luis Obispo County Regional Airport (KSBP) | Sacramento Mather Airport (KMHR) | 2026-07-28 18:22 UTC | 2026-07-28 19:14 UTC | 51m |
| N622TP |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-07-28 18:41 UTC | 2026-07-28 19:09 UTC | 27m |
| DOC03 | DOC | Aarhus Airport (EKAH) | Endelave West Airport (EKEL) | 2026-07-28 18:56 UTC | 2026-07-28 19:08 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
