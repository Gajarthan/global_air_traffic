# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_11:14:04_UTC-green)

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

**Latest saved flight:** 2026-07-28 11:14:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-28 11:14:04 UTC

- **156,152** saved flights
- **51,900** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **156,152** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,874,715.1 tonnes** estimated CO2 emissions
- **108,679,135 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6280 |
| 2 | SkyWest Airlines | 5725 |
| 3 | EJA | 3095 |
| 4 | IndiGo | 2765 |
| 5 | American Airlines | 2491 |
| 6 | Southwest Airlines | 2458 |
| 7 | ENY | 1950 |
| 8 | Delta Air Lines | 1860 |
| 9 | Lufthansa | 1501 |
| 10 | LATAM Airlines | 1455 |
| 11 | AZU | 1366 |
| 12 | WIF | 1317 |
| 13 | Vueling | 1308 |
| 14 | LXJ | 1199 |
| 15 | AXM | 1101 |
| 16 | Swiss International | 1088 |
| 17 | easyJet | 1018 |
| 18 | Alaska Airlines | 979 |
| 19 | All Nippon Airways | 973 |
| 20 | QLK | 972 |
| 21 | EJU | 956 |
| 22 | VIV | 858 |
| 23 | United Airlines | 837 |
| 24 | CXK | 826 |
| 25 | AEE | 816 |
| 26 | Cathay Pacific | 816 |
| 27 | GLO | 816 |
| 28 | MXY | 815 |
| 29 | JetBlue | 812 |
| 30 | Air France | 811 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 134811 |
| 2 | 🇪🇸 ES | 10061 |
| 3 | 🇧🇷 BR | 8903 |
| 4 | 🇦🇺 AU | 8849 |
| 5 | 🇮🇳 IN | 8694 |
| 6 | 🇨🇦 CA | 8414 |
| 7 | 🇮🇹 IT | 8053 |
| 8 | 🇩🇪 DE | 7921 |
| 9 | 🇬🇧 GB | 7162 |
| 10 | 🇯🇵 JP | 6411 |
| 11 | 🇫🇷 FR | 6169 |
| 12 | 🇨🇴 CO | 5409 |
| 13 | 🇲🇽 MX | 4479 |
| 14 | 🇬🇷 GR | 4438 |
| 15 | 🇳🇴 NO | 4127 |
| 16 | 🇨🇭 CH | 4075 |
| 17 | 🇹🇷 TR | 3727 |
| 18 | 🇲🇾 MY | 2869 |
| 19 | 🇵🇱 PL | 2657 |
| 20 | 🇿🇦 ZA | 2530 |
| 21 | 🇳🇿 NZ | 2329 |
| 22 | 🇹🇭 TH | 2253 |
| 23 | 🇰🇷 KR | 2090 |
| 24 | 🇵🇭 PH | 2064 |
| 25 | 🇬🇹 GT | 2012 |
| 26 | 🇲🇦 MA | 1590 |
| 27 | 🇲🇪 ME | 1511 |
| 28 | 🇭🇷 HR | 1434 |
| 29 | 🇳🇱 NL | 1428 |
| 30 | 🇲🇴 MO | 1289 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3211 |
| 2 | Denver International Airport |  | US | 2624 |
| 3 | Tokyo International Airport |  | JP | 2032 |
| 4 | Guaymaral Airport |  | CO | 1955 |
| 5 | Indira Gandhi International Airport |  | IN | 1933 |
| 6 | Harry Reid International Airport |  | US | 1917 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1732 |
| 8 | Zurich Airport |  | CH | 1686 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1636 |
| 10 | La Aurora Airport |  | GT | 1559 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1453 |
| 12 | Frankfurt am Main International Airport |  | DE | 1450 |
| 13 | Chicago O'Hare International Airport |  | US | 1422 |
| 14 | Salt Lake City International Airport |  | US | 1409 |
| 15 | El Dorado International Airport |  | CO | 1409 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1320 |
| 17 | Macau International Airport |  | MO | 1289 |
| 18 | Congonhas Airport |  | BR | 1274 |
| 19 | Madrid Barajas International Airport |  | ES | 1240 |
| 20 | Capua Airport |  | IT | 1229 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1200 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1124 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1109 |
| 24 | Charlotte/Douglas International Airport |  | US | 1107 |
| 25 | Kuala Lumpur International Airport |  | MY | 1099 |
| 26 | Charles de Gaulle International Airport |  | FR | 1069 |
| 27 | Bengaluru International Airport |  | IN | 1034 |
| 28 | Malpensa International Airport |  | IT | 1023 |
| 29 | Ninoy Aquino International Airport |  | PH | 967 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 950 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 944 |
| 32 | Barcelona International Airport |  | ES | 929 |
| 33 | Daniel K Inouye International Airport |  | US | 923 |
| 34 | Seattle-Tacoma International Airport |  | US | 911 |
| 35 | Calgary International Airport |  | CA | 894 |
| 36 | Tenerife Norte Airport |  | ES | 893 |
| 37 | Viracopos International Airport |  | BR | 887 |
| 38 | Scottsdale Airport |  | US | 884 |
| 39 | Amsterdam Airport Schiphol |  | NL | 863 |
| 40 | Oslo Gardermoen Airport |  | NO | 858 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 821 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 562 | 21m | 244 km | 2,366.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 376 | 24m | 225 km | 1,458.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 374 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 360 | 1h 9m | 770 km | 4,782.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 288 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 276 | 27m | 275 km | 1,307.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 231 | 22m | 55 km | 219.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 215 | 44m | 241 km | 893.1 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 209 | 1h 47m | 1,423 km | 5,129.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 205 | 26m | 215 km | 759.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 200 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 197 | 20m | 250 km | 850.9 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 184 | 1h 15m | 961 km | 3,049.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 184 | 18m | 144 km | 457.7 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 182 | 31m | 369 km | 1,158.5 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 181 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 176 | 1h 39m | 1,156 km | 3,511.1 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 176 | 44m | 452 km | 1,371.7 t |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 176 | 50m | 556 km | 1,687.1 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 173 | 1h 1m | 695 km | 2,073.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 50m | 1,304 km | 3,712.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL2282 | United Airlines | Los Angeles International Airport (KLAX) | Washington Dulles International Airport (KIAD) | 2026-07-28 06:38 UTC | 2026-07-28 11:14 UTC | 4h 35m |
| GGW22 | GGW | Charlotte/Douglas International Airport (KCLT) | Washington Dulles International Airport (KIAD) | 2026-07-28 10:08 UTC | 2026-07-28 11:13 UTC | 1h 5m |
| APACHE1 | APA | Gilze Rijen Air Base (EHGR) | EHND (EHND) | 2026-07-28 10:05 UTC | 2026-07-28 11:07 UTC | 1h 2m |
| N52522 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-07-28 10:40 UTC | 2026-07-28 11:07 UTC | 26m |
| ISR588 | ISR | Larnaca International Airport (LCLK) | Ben Gurion International Airport (LLBG) | 2026-07-28 10:29 UTC | 2026-07-28 11:06 UTC | 36m |
| N7367E |  | Animas Air Park (K00C) | Blanding Municipal Airport (KBDG) | 2026-07-28 10:29 UTC | 2026-07-28 11:05 UTC | 36m |
| FYS31VK | FYS | Muchamiel Airport (LEMU) | Muchamiel Airport (LEMU) | 2026-07-28 10:55 UTC | 2026-07-28 11:05 UTC | 10m |
| PLF105 | PLF | Szczecin-Goleniow Solidarność Airport (EPSC) | Rzeszow-Jasionka Airport (EPRZ) | 2026-07-28 10:00 UTC | 2026-07-28 10:52 UTC | 52m |
| RYR9654 | Ryanair | Luqa Airport (LMML) | Lisbon Portela Airport (LPPT) | 2026-07-28 07:58 UTC | 2026-07-28 10:52 UTC | 2h 54m |
| ZKIDH | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-07-28 10:36 UTC | 2026-07-28 10:51 UTC | 15m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-07-27 20:43 UTC | 2026-07-28 10:50 UTC | 14h 7m |
| SYERTN6 | SYE | RAF Syerston (EGXY) | RAF Syerston (EGXY) | 2026-07-28 10:46 UTC | 2026-07-28 10:48 UTC | 2m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-07-27 20:03 UTC | 2026-07-28 10:46 UTC | 14h 42m |
| N455LF |  | Easton State Airport (KESW) | Boeing Field/King County International Airport (KBFI) | 2026-07-28 10:29 UTC | 2026-07-28 10:46 UTC | 17m |
| LFA321 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Sanford International Airport (KSFB) | 2026-07-28 10:27 UTC | 2026-07-28 10:44 UTC | 17m |
| JDL2972 | JDL | VGZR (VGZR) | Kalay Airport (VYKL) | 2026-07-28 09:56 UTC | 2026-07-28 10:35 UTC | 38m |
| UAE386 | Emirates | Dubai International Airport (OMDB) | VYNT (VYNT) | 2026-07-28 05:39 UTC | 2026-07-28 10:35 UTC | 4h 55m |
| UBA812 | UBA | Mandalay International Airport (VYMD) | Naypyidaw Airport (VYEL) | 2026-07-28 10:17 UTC | 2026-07-28 10:35 UTC | 17m |
| FDX5279 | FDX | Indira Gandhi International Airport (VIDP) | LBSB (LBSB) | 2026-07-28 04:30 UTC | 2026-07-28 10:34 UTC | 6h 4m |
| VOE4KU | VOE | Ajaccio-Napoleon Bonaparte Airport (LFKJ) | Caen-Carpiquet Airport (LFRK) | 2026-07-28 08:52 UTC | 2026-07-28 10:31 UTC | 1h 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
