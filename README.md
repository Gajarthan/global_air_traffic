# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_23:41:55_UTC-green)

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

**Latest saved flight:** 2026-08-16 23:41:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 23:41:55 UTC

- **206,645** saved flights
- **65,881** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **206,645** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,485,437.5 tonnes** estimated CO2 emissions
- **144,083,336 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8147 |
| 2 | SkyWest Airlines | 7445 |
| 3 | EJA | 4029 |
| 4 | IndiGo | 3523 |
| 5 | American Airlines | 3448 |
| 6 | Southwest Airlines | 3322 |
| 7 | Delta Air Lines | 2660 |
| 8 | ENY | 2583 |
| 9 | LATAM Airlines | 1949 |
| 10 | AZU | 1872 |
| 11 | Lufthansa | 1749 |
| 12 | Vueling | 1709 |
| 13 | WIF | 1657 |
| 14 | LXJ | 1637 |
| 15 | easyJet | 1428 |
| 16 | Swiss International | 1376 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1304 |
| 19 | Alaska Airlines | 1280 |
| 20 | QLK | 1266 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1137 |
| 24 | GLO | 1121 |
| 25 | Air France | 1103 |
| 26 | PGT | 1102 |
| 27 | JetBlue | 1061 |
| 28 | AEE | 1052 |
| 29 | WMT | 1040 |
| 30 | CXK | 1018 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 175748 |
| 2 | 🇪🇸 ES | 13186 |
| 3 | 🇧🇷 BR | 11867 |
| 4 | 🇦🇺 AU | 11519 |
| 5 | 🇨🇦 CA | 11431 |
| 6 | 🇮🇳 IN | 10996 |
| 7 | 🇮🇹 IT | 10768 |
| 8 | 🇩🇪 DE | 10208 |
| 9 | 🇬🇧 GB | 9628 |
| 10 | 🇯🇵 JP | 8456 |
| 11 | 🇨🇴 CO | 8230 |
| 12 | 🇫🇷 FR | 8167 |
| 13 | 🇬🇷 GR | 6069 |
| 14 | 🇹🇷 TR | 5855 |
| 15 | 🇲🇽 MX | 5817 |
| 16 | 🇨🇭 CH | 5513 |
| 17 | 🇳🇴 NO | 5138 |
| 18 | 🇲🇾 MY | 3529 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3404 |
| 21 | 🇹🇭 TH | 3247 |
| 22 | 🇳🇿 NZ | 2849 |
| 23 | 🇵🇭 PH | 2733 |
| 24 | 🇬🇹 GT | 2645 |
| 25 | 🇰🇷 KR | 2505 |
| 26 | 🇭🇷 HR | 2209 |
| 27 | 🇲🇦 MA | 2082 |
| 28 | 🇳🇱 NL | 1839 |
| 29 | 🇲🇪 ME | 1743 |
| 30 | 🇮🇩 ID | 1686 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4360 |
| 2 | Denver International Airport |  | US | 3385 |
| 3 | Tokyo International Airport |  | JP | 2550 |
| 4 | Indira Gandhi International Airport |  | IN | 2495 |
| 5 | Guaymaral Airport |  | CO | 2494 |
| 6 | Harry Reid International Airport |  | US | 2337 |
| 7 | Zurich Airport |  | CH | 2154 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2151 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2148 |
| 10 | La Aurora Airport |  | GT | 2015 |
| 11 | Chicago O'Hare International Airport |  | US | 1915 |
| 12 | El Dorado International Airport |  | CO | 1891 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1846 |
| 14 | Salt Lake City International Airport |  | US | 1829 |
| 15 | Congonhas Airport |  | BR | 1728 |
| 16 | Frankfurt am Main International Airport |  | DE | 1706 |
| 17 | Madrid Barajas International Airport |  | ES | 1618 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1577 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1573 |
| 20 | Capua Airport |  | IT | 1568 |
| 21 | Macau International Airport |  | MO | 1542 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1503 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1440 |
| 24 | Malpensa International Airport |  | IT | 1425 |
| 25 | Charles de Gaulle International Airport |  | FR | 1413 |
| 26 | Charlotte/Douglas International Airport |  | US | 1412 |
| 27 | Kuala Lumpur International Airport |  | MY | 1309 |
| 28 | Ninoy Aquino International Airport |  | PH | 1295 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1282 |
| 30 | Bengaluru International Airport |  | IN | 1276 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1250 |
| 32 | Seattle-Tacoma International Airport |  | US | 1231 |
| 33 | Barcelona International Airport |  | ES | 1229 |
| 34 | Viracopos International Airport |  | BR | 1200 |
| 35 | Calgary International Airport |  | CA | 1172 |
| 36 | Reno/Tahoe International Airport |  | US | 1142 |
| 37 | Oslo Gardermoen Airport |  | NO | 1139 |
| 38 | Vitoria/Foronda Airport |  | ES | 1136 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1107 |
| 40 | Tenerife Norte Airport |  | ES | 1105 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 471 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 297 | 1h 49m | 1,423 km | 7,288.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 257 | 24m | 218 km | 968.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 256 | 19m | 99 km | 438.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 244 | 1h 37m | 1,156 km | 4,867.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 237 | 19m | 144 km | 589.5 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 235 | 31m | 369 km | 1,495.8 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 225 | 28m | 152 km | 588.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 223 | 1h 49m | 1,304 km | 5,016.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG622 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-08-16 22:55 UTC | 2026-08-16 23:41 UTC | 46m |
| QTR15R | Qatar Airways | Indira Gandhi International Airport (VIDP) | Hamad International Airport (OTHH) | 2026-08-16 20:39 UTC | 2026-08-16 23:34 UTC | 2h 55m |
| N459WM |  | Wilding Farm Airport (6WA5) | Boeing Field/King County International Airport (KBFI) | 2026-08-16 22:59 UTC | 2026-08-16 23:29 UTC | 30m |
| N429LF |  | Port Angeles Cgas Airport (KNOW) | Kimshan Ranch Airport (WN00) | 2026-08-16 22:55 UTC | 2026-08-16 23:19 UTC | 24m |
| FTO382 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-16 22:53 UTC | 2026-08-16 23:19 UTC | 26m |
| TKR136 | TKR | Roberts Field/Redmond Municipal Airport (KRDM) | OG05 (OG05) | 2026-08-16 23:08 UTC | 2026-08-16 23:19 UTC | 11m |
| N54983 |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-08-16 22:36 UTC | 2026-08-16 23:15 UTC | 39m |
| N80790 |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-16 22:44 UTC | 2026-08-16 23:08 UTC | 23m |
| N20AW |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-16 22:34 UTC | 2026-08-16 23:04 UTC | 30m |
| N217SW |  | Carson City Airport (KCXP) | Gansner Field (K2O1) | 2026-08-16 22:24 UTC | 2026-08-16 23:03 UTC | 38m |
| N432ER |  | 0IL8 (0IL8) | Ruder Airport (59IL) | 2026-08-16 22:52 UTC | 2026-08-16 23:02 UTC | 9m |
| QLK9D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-16 22:42 UTC | 2026-08-16 23:02 UTC | 19m |
| CMK | CMK | Sunshine Coast Airport (YBMC) | Childers Airport (YCDS) | 2026-08-16 22:40 UTC | 2026-08-16 23:02 UTC | 21m |
| TKR914 | TKR | Chiloquin State Airport (K2S7) | Rogue Valley International/Medford Airport (KMFR) | 2026-08-16 22:47 UTC | 2026-08-16 23:01 UTC | 14m |
| AM270 |  | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-08-16 22:15 UTC | 2026-08-16 22:53 UTC | 37m |
| TAM3688 | LATAM Airlines | Galeao - Antonio Carlos Jobim International Airport (SBGL) | Eurico de Aguiar Salles Airport (SBVT) | 2026-08-16 22:08 UTC | 2026-08-16 22:50 UTC | 42m |
| CXK556 | CXK | Riverside Airport (KRAL) | Whiteman Airport (KWHP) | 2026-08-16 22:03 UTC | 2026-08-16 22:49 UTC | 45m |
| N43VM |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Lake Tahoe Airport (KTVL) | 2026-08-16 22:13 UTC | 2026-08-16 22:48 UTC | 34m |
| N805FA |  | Truckee-Tahoe Airport (KTRK) | Santa Monica Municipal Airport (KSMO) | 2026-08-16 21:22 UTC | 2026-08-16 22:48 UTC | 1h 26m |
| RAIDR10 | RAI | Miramar Mcas (Joe Foss Field) Airport (KNKX) | 59CL (59CL) | 2026-08-16 22:27 UTC | 2026-08-16 22:48 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
