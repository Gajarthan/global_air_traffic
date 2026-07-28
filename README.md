# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_03:21:26_UTC-green)

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

**Latest saved flight:** 2026-07-28 03:21:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-28 03:21:26 UTC

- **155,851** saved flights
- **51,843** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **155,851** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,869,834.0 tonnes** estimated CO2 emissions
- **108,396,174 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6261 |
| 2 | SkyWest Airlines | 5725 |
| 3 | EJA | 3095 |
| 4 | IndiGo | 2758 |
| 5 | American Airlines | 2491 |
| 6 | Southwest Airlines | 2456 |
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
| 18 | Alaska Airlines | 979 |
| 19 | All Nippon Airways | 970 |
| 20 | QLK | 969 |
| 21 | EJU | 955 |
| 22 | VIV | 858 |
| 23 | United Airlines | 836 |
| 24 | CXK | 826 |
| 25 | GLO | 816 |
| 26 | MXY | 815 |
| 27 | AEE | 813 |
| 28 | JetBlue | 812 |
| 29 | Cathay Pacific | 809 |
| 30 | Air France | 807 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 134759 |
| 2 | 🇪🇸 ES | 10019 |
| 3 | 🇧🇷 BR | 8897 |
| 4 | 🇦🇺 AU | 8809 |
| 5 | 🇮🇳 IN | 8668 |
| 6 | 🇨🇦 CA | 8403 |
| 7 | 🇮🇹 IT | 8030 |
| 8 | 🇩🇪 DE | 7902 |
| 9 | 🇬🇧 GB | 7141 |
| 10 | 🇯🇵 JP | 6383 |
| 11 | 🇫🇷 FR | 6146 |
| 12 | 🇨🇴 CO | 5409 |
| 13 | 🇲🇽 MX | 4479 |
| 14 | 🇬🇷 GR | 4420 |
| 15 | 🇳🇴 NO | 4106 |
| 16 | 🇨🇭 CH | 4059 |
| 17 | 🇹🇷 TR | 3710 |
| 18 | 🇲🇾 MY | 2863 |
| 19 | 🇵🇱 PL | 2650 |
| 20 | 🇿🇦 ZA | 2509 |
| 21 | 🇳🇿 NZ | 2319 |
| 22 | 🇹🇭 TH | 2233 |
| 23 | 🇰🇷 KR | 2087 |
| 24 | 🇵🇭 PH | 2050 |
| 25 | 🇬🇹 GT | 2012 |
| 26 | 🇲🇦 MA | 1587 |
| 27 | 🇲🇪 ME | 1510 |
| 28 | 🇭🇷 HR | 1431 |
| 29 | 🇳🇱 NL | 1424 |
| 30 | 🇲🇴 MO | 1283 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3211 |
| 2 | Denver International Airport |  | US | 2624 |
| 3 | Tokyo International Airport |  | JP | 2024 |
| 4 | Guaymaral Airport |  | CO | 1955 |
| 5 | Indira Gandhi International Airport |  | IN | 1922 |
| 6 | Harry Reid International Airport |  | US | 1916 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1725 |
| 8 | Zurich Airport |  | CH | 1681 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1636 |
| 10 | La Aurora Airport |  | GT | 1559 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1453 |
| 12 | Frankfurt am Main International Airport |  | DE | 1448 |
| 13 | Chicago O'Hare International Airport |  | US | 1422 |
| 14 | El Dorado International Airport |  | CO | 1409 |
| 15 | Salt Lake City International Airport |  | US | 1407 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1320 |
| 17 | Macau International Airport |  | MO | 1283 |
| 18 | Congonhas Airport |  | BR | 1273 |
| 19 | Madrid Barajas International Airport |  | ES | 1235 |
| 20 | Capua Airport |  | IT | 1228 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1200 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1120 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1109 |
| 24 | Charlotte/Douglas International Airport |  | US | 1106 |
| 25 | Kuala Lumpur International Airport |  | MY | 1097 |
| 26 | Charles de Gaulle International Airport |  | FR | 1064 |
| 27 | Bengaluru International Airport |  | IN | 1033 |
| 28 | Malpensa International Airport |  | IT | 1017 |
| 29 | Ninoy Aquino International Airport |  | PH | 961 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 949 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 944 |
| 32 | Barcelona International Airport |  | ES | 924 |
| 33 | Daniel K Inouye International Airport |  | US | 923 |
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
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 562 | 21m | 244 km | 2,366.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 374 | 24m | 225 km | 1,450.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 374 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 360 | 1h 9m | 770 km | 4,782.3 t |
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
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 173 | 1h 1m | 695 km | 2,073.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 50m | 1,304 km | 3,712.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N719LS |  | Knoxville Downtown Island Airport (KDKX) | Knoxville Downtown Island Airport (KDKX) | 2026-07-28 03:09 UTC | 2026-07-28 03:21 UTC | 11m |
| N907RD |  | Santa Barbara Municipal Airport (KSBA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-07-28 02:52 UTC | 2026-07-28 03:17 UTC | 25m |
| WXQ | WXQ | RAAF Williams Point Cook Base (YMPC) | Melbourne Moorabbin Airport (YMMB) | 2026-07-28 03:03 UTC | 2026-07-28 03:15 UTC | 12m |
| N52789 |  | Oakland San Francisco Bay Airport (KOAK) | Sacramento Executive Airport (KSAC) | 2026-07-28 02:34 UTC | 2026-07-28 03:11 UTC | 37m |
| CCA101 | Air China | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-07-28 00:22 UTC | 2026-07-28 03:03 UTC | 2h 41m |
| N901NM |  | Seidel Ranch Airport (02XS) | Austin-Bergstrom International Airport (KAUS) | 2026-07-28 02:30 UTC | 2026-07-28 02:59 UTC | 29m |
| CLX1081 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-07-27 16:16 UTC | 2026-07-28 02:58 UTC | 10h 42m |
| N840JA |  | 3CL2 (3CL2) | Red Bluff Municipal Airport (KRBL) | 2026-07-28 02:53 UTC | 2026-07-28 02:54 UTC | 0m |
| CXK406 | CXK | Jacksonville Executive At Craig Airport (KCRG) | Jacksonville Executive At Craig Airport (KCRG) | 2026-07-28 02:32 UTC | 2026-07-28 02:51 UTC | 18m |
| N815PZ |  | Des Moines International Airport (KDSM) | Ames Municipal Airport (KAMW) | 2026-07-28 02:28 UTC | 2026-07-28 02:44 UTC | 15m |
| N32GA |  | Josephine Ranch Airport (2ID3) | Josephine Ranch Airport (2ID3) | 2026-07-28 02:19 UTC | 2026-07-28 02:44 UTC | 24m |
| CXK308 | CXK | Jacksonville Executive At Craig Airport (KCRG) | Jacksonville Executive At Craig Airport (KCRG) | 2026-07-28 01:51 UTC | 2026-07-28 02:36 UTC | 45m |
| S38 |  | Gaziemir Airport (LTBK) | Adnan Menderes International Airport (LTBJ) | 2026-07-28 02:19 UTC | 2026-07-28 02:32 UTC | 13m |
| T73 |  | San Bernardino International Airport (KSBD) | San Bernardino International Airport (KSBD) | 2026-07-28 01:29 UTC | 2026-07-28 02:31 UTC | 1h 2m |
| CFR72 | CFR | San Bernardino International Airport (KSBD) | San Bernardino International Airport (KSBD) | 2026-07-28 02:15 UTC | 2026-07-28 02:30 UTC | 14m |
| TRP1 | TRP | Forest Hill Airport (MD31) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-07-28 02:17 UTC | 2026-07-28 02:28 UTC | 10m |
| QLK322D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-07-28 01:52 UTC | 2026-07-28 02:21 UTC | 28m |
| BNOL | BNO | Bodø Airport (ENBO) | Bardufoss Airport (ENDU) | 2026-07-28 01:46 UTC | 2026-07-28 02:19 UTC | 32m |
| IGO638Y | IndiGo | Indira Gandhi International Airport (VIDP) | Hosur Airport (VO95) | 2026-07-27 23:50 UTC | 2026-07-28 02:18 UTC | 2h 28m |
| CFRT71 | CFR | Ramona Airport (KRNM) | San Bernardino International Airport (KSBD) | 2026-07-28 01:45 UTC | 2026-07-28 02:17 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
