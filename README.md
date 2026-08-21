# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_15:37:25_UTC-green)

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

**Latest saved flight:** 2026-08-21 15:37:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 15:37:25 UTC

- **222,518** saved flights
- **69,564** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **222,518** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,679,349.6 tonnes** estimated CO2 emissions
- **155,324,614 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8928 |
| 2 | SkyWest Airlines | 7895 |
| 3 | EJA | 4295 |
| 4 | IndiGo | 3776 |
| 5 | American Airlines | 3674 |
| 6 | Southwest Airlines | 3494 |
| 7 | Delta Air Lines | 2854 |
| 8 | ENY | 2731 |
| 9 | LATAM Airlines | 2118 |
| 10 | AZU | 2045 |
| 11 | Vueling | 1877 |
| 12 | Lufthansa | 1840 |
| 13 | WIF | 1782 |
| 14 | LXJ | 1748 |
| 15 | easyJet | 1541 |
| 16 | Swiss International | 1481 |
| 17 | AXM | 1466 |
| 18 | QLK | 1405 |
| 19 | EJU | 1394 |
| 20 | United Airlines | 1394 |
| 21 | Alaska Airlines | 1353 |
| 22 | All Nippon Airways | 1333 |
| 23 | PGT | 1221 |
| 24 | GLO | 1217 |
| 25 | VIV | 1210 |
| 26 | Air France | 1207 |
| 27 | WMT | 1184 |
| 28 | Wizz Air | 1146 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1110 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186673 |
| 2 | 🇪🇸 ES | 14264 |
| 3 | 🇧🇷 BR | 12872 |
| 4 | 🇦🇺 AU | 12653 |
| 5 | 🇨🇦 CA | 12280 |
| 6 | 🇮🇹 IT | 11867 |
| 7 | 🇮🇳 IN | 11777 |
| 8 | 🇩🇪 DE | 10986 |
| 9 | 🇬🇧 GB | 10446 |
| 10 | 🇨🇴 CO | 9161 |
| 11 | 🇯🇵 JP | 9054 |
| 12 | 🇫🇷 FR | 8872 |
| 13 | 🇬🇷 GR | 6495 |
| 14 | 🇹🇷 TR | 6459 |
| 15 | 🇲🇽 MX | 6167 |
| 16 | 🇨🇭 CH | 5863 |
| 17 | 🇳🇴 NO | 5541 |
| 18 | 🇲🇾 MY | 3885 |
| 19 | 🇿🇦 ZA | 3839 |
| 20 | 🇹🇭 TH | 3772 |
| 21 | 🇵🇱 PL | 3698 |
| 22 | 🇳🇿 NZ | 3089 |
| 23 | 🇵🇭 PH | 3018 |
| 24 | 🇬🇹 GT | 2808 |
| 25 | 🇰🇷 KR | 2656 |
| 26 | 🇭🇷 HR | 2486 |
| 27 | 🇲🇦 MA | 2241 |
| 28 | 🇲🇪 ME | 1980 |
| 29 | 🇳🇱 NL | 1978 |
| 30 | 🇮🇩 ID | 1909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4655 |
| 2 | Denver International Airport |  | US | 3618 |
| 3 | Tokyo International Airport |  | JP | 2714 |
| 4 | Indira Gandhi International Airport |  | IN | 2704 |
| 5 | Guaymaral Airport |  | CO | 2618 |
| 6 | Harry Reid International Airport |  | US | 2446 |
| 7 | Zurich Airport |  | CH | 2306 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2276 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2257 |
| 10 | La Aurora Airport |  | GT | 2139 |
| 11 | El Dorado International Airport |  | CO | 2078 |
| 12 | Chicago O'Hare International Airport |  | US | 2027 |
| 13 | Salt Lake City International Airport |  | US | 1949 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1911 |
| 15 | Congonhas Airport |  | BR | 1881 |
| 16 | Frankfurt am Main International Airport |  | DE | 1804 |
| 17 | Madrid Barajas International Airport |  | ES | 1741 |
| 18 | Capua Airport |  | IT | 1701 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1662 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1641 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1588 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1561 |
| 25 | Charles de Gaulle International Airport |  | FR | 1534 |
| 26 | Charlotte/Douglas International Airport |  | US | 1473 |
| 27 | Ninoy Aquino International Airport |  | PH | 1437 |
| 28 | Kuala Lumpur International Airport |  | MY | 1418 |
| 29 | Barcelona International Airport |  | ES | 1372 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1348 |
| 31 | Bengaluru International Airport |  | IN | 1334 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1316 |
| 33 | Seattle-Tacoma International Airport |  | US | 1313 |
| 34 | Viracopos International Airport |  | BR | 1307 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1259 |
| 36 | Calgary International Airport |  | CA | 1258 |
| 37 | Oslo Gardermoen Airport |  | NO | 1241 |
| 38 | Don Mueang International Airport |  | TH | 1239 |
| 39 | Vitoria/Foronda Airport |  | ES | 1234 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1198 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1069 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 801 | 21m | 244 km | 3,372.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 556 | 1h 7m | 770 km | 7,386.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 508 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 501 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 375 | 27m | 275 km | 1,777.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 353 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 330 | 1h 50m | 1,423 km | 8,098.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 325 | 44m | 241 km | 1,350.0 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 297 | 21m | 250 km | 1,282.9 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 280 | 1h 39m | 1,156 km | 5,585.9 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 277 | 24m | 218 km | 1,043.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 19 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 274 | 44m | 555 km | 2,623.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 274 | 19m | 99 km | 469.3 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 262 | 1h 14m | 961 km | 4,342.8 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 253 | 19m | 144 km | 629.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 241 | 1h 50m | 1,304 km | 5,421.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 235 | 28m | 152 km | 614.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N98EG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-21 15:24 UTC | 2026-08-21 15:37 UTC | 12m |
| GAYJR | GAY | Oxford (Kidlington) Airport (EGTK) | Oxford (Kidlington) Airport (EGTK) | 2026-08-21 14:57 UTC | 2026-08-21 15:32 UTC | 34m |
| CXK455 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | Rocky Mountain Metro Airport (KBJC) | 2026-08-21 14:43 UTC | 2026-08-21 15:30 UTC | 47m |
| N240GS |  | Old Sarum Airfield (EGLS) | Old Sarum Airfield (EGLS) | 2026-08-21 15:10 UTC | 2026-08-21 15:27 UTC | 17m |
| N3552C |  | Plant City Airport (KPCM) | Brooksville-Tampa Bay Regional Airport (KBKV) | 2026-08-21 15:08 UTC | 2026-08-21 15:26 UTC | 18m |
| RNGR736 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | XS10 (XS10) | 2026-08-21 15:02 UTC | 2026-08-21 15:23 UTC | 20m |
| DSU24 | DSU | Cleveland Municipal Airport (KRNV) | Greenville Mid-Delta Airport (KGLH) | 2026-08-21 14:46 UTC | 2026-08-21 15:22 UTC | 36m |
| DEZOM | DEZ | Uetersen/Heist Airport (EDHE) | Uetersen/Heist Airport (EDHE) | 2026-08-21 15:07 UTC | 2026-08-21 15:20 UTC | 13m |
| CAN10 | CAN | L'Aquila / Preturo Airport (LIAP) | Pescara International Airport (LIBP) | 2026-08-21 14:56 UTC | 2026-08-21 15:18 UTC | 22m |
| FXC11 | FXC | Bridgeport/Sikorsky Airport (KBDR) | Teterboro Airport (KTEB) | 2026-08-21 14:52 UTC | 2026-08-21 15:12 UTC | 20m |
| N15044 |  | Kansas City/Lee's Summit Regional Airport (KLXT) | Kansas City/Lee's Summit Regional Airport (KLXT) | 2026-08-21 14:25 UTC | 2026-08-21 15:11 UTC | 46m |
|  |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-21 14:57 UTC | 2026-08-21 15:11 UTC | 14m |
| ECOFS | ECO | Ibiza Airport (LEIB) | Ibiza Airport (LEIB) | 2026-08-21 14:54 UTC | 2026-08-21 15:10 UTC | 16m |
| STY743 | STY | Republic Airport (KFRG) | 3NY5 (3NY5) | 2026-08-21 14:44 UTC | 2026-08-21 15:10 UTC | 25m |
| ZSXTR | ZSX | Starshire Farm Airport (2KS9) | Converse Farm Airport (SN47) | 2026-08-21 14:53 UTC | 2026-08-21 15:10 UTC | 16m |
| N595JW |  | Newton-City-County Airport (KEWK) | Taylor Airport (SN46) | 2026-08-21 14:22 UTC | 2026-08-21 15:09 UTC | 46m |
| EPI197 | EPI | Colorado City Municipal Airport (KAZC) | Colorado City Municipal Airport (KAZC) | 2026-08-21 14:21 UTC | 2026-08-21 15:09 UTC | 47m |
| N261PJ |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-08-21 14:33 UTC | 2026-08-21 15:09 UTC | 35m |
| WDK37 | WDK | Southampton Airport (EGHI) | London City Airport (EGLC) | 2026-08-21 14:37 UTC | 2026-08-21 15:09 UTC | 31m |
| FTO381 | FTO | Essex County Airport (KCDW) | Newark Liberty International Airport (KEWR) | 2026-08-21 14:56 UTC | 2026-08-21 15:09 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
