# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_04:39:45_UTC-green)

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

**Latest saved flight:** 2026-08-19 04:39:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 04:39:45 UTC

- **214,326** saved flights
- **67,723** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **214,326** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,575,985.6 tonnes** estimated CO2 emissions
- **149,332,498 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8487 |
| 2 | SkyWest Airlines | 7695 |
| 3 | EJA | 4184 |
| 4 | IndiGo | 3655 |
| 5 | American Airlines | 3579 |
| 6 | Southwest Airlines | 3429 |
| 7 | Delta Air Lines | 2766 |
| 8 | ENY | 2660 |
| 9 | LATAM Airlines | 2026 |
| 10 | AZU | 1960 |
| 11 | Vueling | 1791 |
| 12 | Lufthansa | 1784 |
| 13 | WIF | 1713 |
| 14 | LXJ | 1693 |
| 15 | easyJet | 1483 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1400 |
| 18 | United Airlines | 1360 |
| 19 | QLK | 1331 |
| 20 | Alaska Airlines | 1320 |
| 21 | EJU | 1316 |
| 22 | All Nippon Airways | 1295 |
| 23 | VIV | 1182 |
| 24 | GLO | 1163 |
| 25 | PGT | 1156 |
| 26 | Air France | 1154 |
| 27 | WMT | 1103 |
| 28 | JetBlue | 1091 |
| 29 | AEE | 1080 |
| 30 | Wizz Air | 1069 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181325 |
| 2 | 🇪🇸 ES | 13682 |
| 3 | 🇧🇷 BR | 12337 |
| 4 | 🇦🇺 AU | 12062 |
| 5 | 🇨🇦 CA | 11846 |
| 6 | 🇮🇳 IN | 11386 |
| 7 | 🇮🇹 IT | 11268 |
| 8 | 🇩🇪 DE | 10542 |
| 9 | 🇬🇧 GB | 9971 |
| 10 | 🇯🇵 JP | 8816 |
| 11 | 🇨🇴 CO | 8743 |
| 12 | 🇫🇷 FR | 8490 |
| 13 | 🇬🇷 GR | 6264 |
| 14 | 🇹🇷 TR | 6138 |
| 15 | 🇲🇽 MX | 6020 |
| 16 | 🇨🇭 CH | 5656 |
| 17 | 🇳🇴 NO | 5312 |
| 18 | 🇲🇾 MY | 3698 |
| 19 | 🇿🇦 ZA | 3606 |
| 20 | 🇵🇱 PL | 3528 |
| 21 | 🇹🇭 TH | 3464 |
| 22 | 🇳🇿 NZ | 2987 |
| 23 | 🇵🇭 PH | 2868 |
| 24 | 🇬🇹 GT | 2730 |
| 25 | 🇰🇷 KR | 2595 |
| 26 | 🇭🇷 HR | 2326 |
| 27 | 🇲🇦 MA | 2154 |
| 28 | 🇳🇱 NL | 1903 |
| 29 | 🇲🇪 ME | 1849 |
| 30 | 🇮🇩 ID | 1790 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4513 |
| 2 | Denver International Airport |  | US | 3508 |
| 3 | Tokyo International Airport |  | JP | 2646 |
| 4 | Indira Gandhi International Airport |  | IN | 2600 |
| 5 | Guaymaral Airport |  | CO | 2561 |
| 6 | Harry Reid International Airport |  | US | 2394 |
| 7 | Zurich Airport |  | CH | 2223 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2212 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2200 |
| 10 | La Aurora Airport |  | GT | 2076 |
| 11 | El Dorado International Airport |  | CO | 1998 |
| 12 | Chicago O'Hare International Airport |  | US | 1979 |
| 13 | Salt Lake City International Airport |  | US | 1899 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1889 |
| 15 | Congonhas Airport |  | BR | 1798 |
| 16 | Frankfurt am Main International Airport |  | DE | 1741 |
| 17 | Madrid Barajas International Airport |  | ES | 1667 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1617 |
| 19 | Capua Airport |  | IT | 1617 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1605 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1572 |
| 22 | Macau International Airport |  | MO | 1556 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1504 |
| 24 | Malpensa International Airport |  | IT | 1491 |
| 25 | Charles de Gaulle International Airport |  | FR | 1473 |
| 26 | Charlotte/Douglas International Airport |  | US | 1442 |
| 27 | Kuala Lumpur International Airport |  | MY | 1364 |
| 28 | Ninoy Aquino International Airport |  | PH | 1361 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1319 |
| 30 | Bengaluru International Airport |  | IN | 1308 |
| 31 | Barcelona International Airport |  | ES | 1305 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1288 |
| 33 | Seattle-Tacoma International Airport |  | US | 1279 |
| 34 | Viracopos International Airport |  | BR | 1253 |
| 35 | Calgary International Airport |  | CA | 1216 |
| 36 | Oslo Gardermoen Airport |  | NO | 1182 |
| 37 | Vitoria/Foronda Airport |  | ES | 1176 |
| 38 | Reno/Tahoe International Airport |  | US | 1161 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1152 |
| 40 | Don Mueang International Airport |  | TH | 1144 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1047 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 766 | 21m | 244 km | 3,225.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 530 | 1h 7m | 770 km | 7,040.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 502 | 24m | 225 km | 1,947.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 483 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 458 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 353 | 27m | 275 km | 1,672.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 315 | 1h 49m | 1,423 km | 7,730.6 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 312 | 44m | 241 km | 1,296.0 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 281 | 21m | 250 km | 1,213.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 267 | 1h 38m | 1,156 km | 5,326.5 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 266 | 19m | 99 km | 455.6 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 261 | 27m | 215 km | 966.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 254 | 1h 14m | 961 km | 4,210.2 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 250 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 248 | 31m | 369 km | 1,578.6 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 231 | 1h 49m | 1,304 km | 5,196.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N81034 |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-08-19 03:48 UTC | 2026-08-19 04:39 UTC | 51m |
| WZZ51PW | Wizz Air | Gdańsk Lech Wałęsa Airport (EPGD) | Khrabrovo Airport (UMKK) | 2026-08-19 04:14 UTC | 2026-08-19 04:37 UTC | 23m |
| WIF5E | WIF | Geilo Airport Dagali (ENDI) | Sogndal Airport (ENSG) | 2026-08-18 20:08 UTC | 2026-08-19 04:14 UTC | 8h 5m |
| N3648Z |  | Skypark Airport (KBTF) | Wendover Airport (KENV) | 2026-08-19 02:38 UTC | 2026-08-19 04:14 UTC | 1h 35m |
| ZKIME | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-08-19 04:02 UTC | 2026-08-19 04:13 UTC | 11m |
| EVA621 | EVA Air | Los Angeles International Airport (KLAX) | Hsinchu Air Base (RCPO) | 2026-08-18 15:34 UTC | 2026-08-19 04:09 UTC | 12h 35m |
| N830CA |  | North Las Vegas Airport (KVGT) | Cottonwood Airport (KP52) | 2026-08-19 02:51 UTC | 2026-08-19 04:03 UTC | 1h 11m |
| CFH23 | CFH | Newcastle Airport (YWLM) | Nambucca Heads Airport (YNHS) | 2026-08-19 03:23 UTC | 2026-08-19 04:01 UTC | 38m |
| WGTL13 | WGT | Newcastle Airport (YWLM) | Nambucca Heads Airport (YNHS) | 2026-08-19 03:32 UTC | 2026-08-19 03:57 UTC | 25m |
| EFC18F | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-19 03:43 UTC | 2026-08-19 03:55 UTC | 11m |
| ANA859 | All Nippon Airways | Chek Lap Kok International Airport (VHHH) | Chek Lap Kok International Airport (VHHH) | 2026-08-19 03:51 UTC | 2026-08-19 03:52 UTC | 0m |
| N8191P |  | Pleasant Valley Airstrip (24AZ) | Yav'Pe Ma'Ta Airport (16AZ) | 2026-08-19 01:51 UTC | 2026-08-19 03:48 UTC | 1h 56m |
| CVA718 | CVA | Auckland International Airport (NZAA) | Waiouru Airport (NZRU) | 2026-08-19 03:00 UTC | 2026-08-19 03:44 UTC | 44m |
| SFJ77 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-08-19 02:40 UTC | 2026-08-19 03:41 UTC | 1h 1m |
| CEB901 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-08-19 03:15 UTC | 2026-08-19 03:41 UTC | 25m |
| N907KW |  | Healy River Airport (PAHV) | Helio Airport (2AK7) | 2026-08-19 02:36 UTC | 2026-08-19 03:40 UTC | 1h 3m |
| IGO7719 | IndiGo | Chandigarh Airport (VICG) | Jaipur International Airport (VIJP) | 2026-08-19 02:42 UTC | 2026-08-19 03:37 UTC | 54m |
| N54BF |  | KU77 (KU77) | Wendover Airport (KENV) | 2026-08-19 02:30 UTC | 2026-08-19 03:37 UTC | 1h 6m |
| N898MT |  | Easterwood Field (KCLL) | Easterwood Field (KCLL) | 2026-08-19 03:33 UTC | 2026-08-19 03:35 UTC | 1m |
| ASA1092 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-08-19 03:12 UTC | 2026-08-19 03:33 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
