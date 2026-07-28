# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_23:51:08_UTC-green)

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

**Latest saved flight:** 2026-07-27 23:51:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-27 23:51:08 UTC

- **155,763** saved flights
- **51,823** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **155,763** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,868,805.9 tonnes** estimated CO2 emissions
- **108,336,571 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6261 |
| 2 | SkyWest Airlines | 5725 |
| 3 | EJA | 3095 |
| 4 | IndiGo | 2756 |
| 5 | American Airlines | 2488 |
| 6 | Southwest Airlines | 2455 |
| 7 | ENY | 1950 |
| 8 | Delta Air Lines | 1857 |
| 9 | Lufthansa | 1499 |
| 10 | LATAM Airlines | 1454 |
| 11 | AZU | 1364 |
| 12 | WIF | 1310 |
| 13 | Vueling | 1302 |
| 14 | LXJ | 1198 |
| 15 | AXM | 1098 |
| 16 | Swiss International | 1083 |
| 17 | easyJet | 1014 |
| 18 | Alaska Airlines | 978 |
| 19 | All Nippon Airways | 969 |
| 20 | QLK | 968 |
| 21 | EJU | 955 |
| 22 | VIV | 858 |
| 23 | United Airlines | 836 |
| 24 | CXK | 824 |
| 25 | GLO | 816 |
| 26 | MXY | 814 |
| 27 | AEE | 813 |
| 28 | JetBlue | 812 |
| 29 | Air France | 807 |
| 30 | Cathay Pacific | 807 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 134671 |
| 2 | 🇪🇸 ES | 10019 |
| 3 | 🇧🇷 BR | 8897 |
| 4 | 🇦🇺 AU | 8792 |
| 5 | 🇮🇳 IN | 8661 |
| 6 | 🇨🇦 CA | 8403 |
| 7 | 🇮🇹 IT | 8029 |
| 8 | 🇩🇪 DE | 7901 |
| 9 | 🇬🇧 GB | 7141 |
| 10 | 🇯🇵 JP | 6377 |
| 11 | 🇫🇷 FR | 6145 |
| 12 | 🇨🇴 CO | 5401 |
| 13 | 🇲🇽 MX | 4477 |
| 14 | 🇬🇷 GR | 4420 |
| 15 | 🇳🇴 NO | 4104 |
| 16 | 🇨🇭 CH | 4059 |
| 17 | 🇹🇷 TR | 3706 |
| 18 | 🇲🇾 MY | 2863 |
| 19 | 🇵🇱 PL | 2649 |
| 20 | 🇿🇦 ZA | 2509 |
| 21 | 🇳🇿 NZ | 2314 |
| 22 | 🇹🇭 TH | 2233 |
| 23 | 🇰🇷 KR | 2087 |
| 24 | 🇵🇭 PH | 2046 |
| 25 | 🇬🇹 GT | 2012 |
| 26 | 🇲🇦 MA | 1587 |
| 27 | 🇲🇪 ME | 1510 |
| 28 | 🇭🇷 HR | 1431 |
| 29 | 🇳🇱 NL | 1424 |
| 30 | 🇲🇴 MO | 1280 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3209 |
| 2 | Denver International Airport |  | US | 2624 |
| 3 | Tokyo International Airport |  | JP | 2021 |
| 4 | Guaymaral Airport |  | CO | 1955 |
| 5 | Indira Gandhi International Airport |  | IN | 1921 |
| 6 | Harry Reid International Airport |  | US | 1916 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1725 |
| 8 | Zurich Airport |  | CH | 1681 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1636 |
| 10 | La Aurora Airport |  | GT | 1559 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1452 |
| 12 | Frankfurt am Main International Airport |  | DE | 1448 |
| 13 | Chicago O'Hare International Airport |  | US | 1422 |
| 14 | Salt Lake City International Airport |  | US | 1407 |
| 15 | El Dorado International Airport |  | CO | 1407 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1320 |
| 17 | Macau International Airport |  | MO | 1280 |
| 18 | Congonhas Airport |  | BR | 1273 |
| 19 | Madrid Barajas International Airport |  | ES | 1235 |
| 20 | Capua Airport |  | IT | 1228 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1199 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1120 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1109 |
| 24 | Charlotte/Douglas International Airport |  | US | 1106 |
| 25 | Kuala Lumpur International Airport |  | MY | 1097 |
| 26 | Charles de Gaulle International Airport |  | FR | 1063 |
| 27 | Bengaluru International Airport |  | IN | 1033 |
| 28 | Malpensa International Airport |  | IT | 1017 |
| 29 | Ninoy Aquino International Airport |  | PH | 959 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 948 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 943 |
| 32 | Barcelona International Airport |  | ES | 924 |
| 33 | Daniel K Inouye International Airport |  | US | 922 |
| 34 | Seattle-Tacoma International Airport |  | US | 911 |
| 35 | Calgary International Airport |  | CA | 894 |
| 36 | Tenerife Norte Airport |  | ES | 891 |
| 37 | Viracopos International Airport |  | BR | 886 |
| 38 | Scottsdale Airport |  | US | 883 |
| 39 | Amsterdam Airport Schiphol |  | NL | 862 |
| 40 | Oslo Gardermoen Airport |  | NO | 854 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 821 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 561 | 21m | 244 km | 2,362.2 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 374 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 373 | 24m | 225 km | 1,447.1 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 359 | 1h 9m | 770 km | 4,769.0 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 286 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 231 | 22m | 55 km | 219.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 214 | 44m | 241 km | 888.9 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 204 | 26m | 215 km | 755.5 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 199 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 196 | 20m | 250 km | 846.6 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 184 | 1h 15m | 961 km | 3,049.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 183 | 18m | 144 km | 455.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 181 | 31m | 369 km | 1,152.1 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 181 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 176 | 50m | 556 km | 1,687.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 175 | 1h 39m | 1,156 km | 3,491.2 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 175 | 44m | 452 km | 1,363.9 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 172 | 1h 1m | 695 km | 2,061.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 50m | 1,304 km | 3,712.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N893AP |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-07-27 23:19 UTC | 2026-07-27 23:51 UTC | 31m |
| N61NG |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-07-27 23:08 UTC | 2026-07-27 23:43 UTC | 34m |
| N68810 |  | Cleveland Regional Jetport Airport (KRZR) | Cleveland Regional Jetport Airport (KRZR) | 2026-07-27 23:31 UTC | 2026-07-27 23:42 UTC | 11m |
| DAL481 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | Seattle-Tacoma International Airport (KSEA) | 2026-07-27 19:08 UTC | 2026-07-27 23:39 UTC | 4h 31m |
| N432GH |  | Norfolk International Airport (KORF) | Norfolk International Airport (KORF) | 2026-07-27 23:22 UTC | 2026-07-27 23:37 UTC | 14m |
| NRF | NRF | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-07-27 22:47 UTC | 2026-07-27 23:37 UTC | 49m |
| GTW432 | GTW | Lakeside Airport (MU65) | El Dorado Springs Memorial Airport (K87K) | 2026-07-27 22:53 UTC | 2026-07-27 23:37 UTC | 43m |
| TORA11 | TOR | Perry Municipal Airport (KF22) | Nelson High Point Airport (8OK7) | 2026-07-27 23:13 UTC | 2026-07-27 23:36 UTC | 23m |
| XSN06 | XSN | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-07-27 22:59 UTC | 2026-07-27 23:33 UTC | 34m |
| R2087 |  | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-07-27 23:16 UTC | 2026-07-27 23:33 UTC | 16m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Zhuhai Airport (ZGSD) | 2026-07-27 12:09 UTC | 2026-07-27 23:32 UTC | 11h 22m |
| CPA662 | Cathay Pacific | VGZR (VGZR) | Zhuhai Airport (ZGSD) | 2026-07-27 20:29 UTC | 2026-07-27 23:30 UTC | 3h 1m |
| AER170 | AER | Ted Stevens Anchorage International Airport (PANC) | Homer Airport (PAHO) | 2026-07-27 22:59 UTC | 2026-07-27 23:30 UTC | 31m |
| QTR8906 | Qatar Airways | Luang Namtha Airport (VLLN) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-07-27 21:49 UTC | 2026-07-27 23:30 UTC | 1h 40m |
| N774BA |  | 1AR8 (1AR8) | 1AR8 (1AR8) | 2026-07-27 23:22 UTC | 2026-07-27 23:23 UTC | 0m |
| N56DG |  | Lawrence Municipal Airport (KLWM) | Lawrence Municipal Airport (KLWM) | 2026-07-27 22:17 UTC | 2026-07-27 23:20 UTC | 1h 2m |
| THY170 | Turkish Airlines | Istanbul Airport (LTFM) | Zhuhai Airport (ZGSD) | 2026-07-27 13:52 UTC | 2026-07-27 23:20 UTC | 9h 28m |
| IGT1023 | IGT | Tbilisi International Airport (UGTB) | Zhuhai Airport (ZGSD) | 2026-07-27 15:08 UTC | 2026-07-27 23:20 UTC | 8h 12m |
| GT1128 |  | Saskatoon John G. Diefenbaker International Airport (CYXE) | Saskatoon John G. Diefenbaker International Airport (CYXE) | 2026-07-27 21:51 UTC | 2026-07-27 23:13 UTC | 1h 21m |
| N227AN |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | San Martin Airport (KE16) | 2026-07-27 22:46 UTC | 2026-07-27 23:08 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
