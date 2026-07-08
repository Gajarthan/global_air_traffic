# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_03:11:45_UTC-green)

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

**Latest saved flight:** 2026-07-08 03:11:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-08 03:11:45 UTC

- **132,727** saved flights
- **45,032** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **132,727** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,597,818.8 tonnes** estimated CO2 emissions
- **92,627,174 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5390 |
| 2 | SkyWest Airlines | 4906 |
| 3 | EJA | 2607 |
| 4 | IndiGo | 2476 |
| 5 | American Airlines | 2075 |
| 6 | Southwest Airlines | 2000 |
| 7 | ENY | 1669 |
| 8 | Delta Air Lines | 1589 |
| 9 | Lufthansa | 1379 |
| 10 | LATAM Airlines | 1223 |
| 11 | Vueling | 1163 |
| 12 | WIF | 1155 |
| 13 | AZU | 1126 |
| 14 | LXJ | 1020 |
| 15 | AXM | 1017 |
| 16 | Swiss International | 941 |
| 17 | All Nippon Airways | 869 |
| 18 | easyJet | 846 |
| 19 | Alaska Airlines | 844 |
| 20 | QLK | 828 |
| 21 | EJU | 817 |
| 22 | VIV | 734 |
| 23 | AEE | 719 |
| 24 | Air France | 718 |
| 25 | Cathay Pacific | 716 |
| 26 | CXK | 712 |
| 27 | United Airlines | 705 |
| 28 | JetBlue | 696 |
| 29 | MXY | 687 |
| 30 | GLO | 680 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 113861 |
| 2 | 🇪🇸 ES | 8813 |
| 3 | 🇮🇳 IN | 7761 |
| 4 | 🇦🇺 AU | 7653 |
| 5 | 🇧🇷 BR | 7487 |
| 6 | 🇨🇦 CA | 7026 |
| 7 | 🇩🇪 DE | 6935 |
| 8 | 🇮🇹 IT | 6914 |
| 9 | 🇬🇧 GB | 5919 |
| 10 | 🇯🇵 JP | 5697 |
| 11 | 🇫🇷 FR | 5269 |
| 12 | 🇨🇴 CO | 4167 |
| 13 | 🇲🇽 MX | 3877 |
| 14 | 🇬🇷 GR | 3792 |
| 15 | 🇳🇴 NO | 3589 |
| 16 | 🇨🇭 CH | 3426 |
| 17 | 🇹🇷 TR | 2958 |
| 18 | 🇲🇾 MY | 2636 |
| 19 | 🇵🇱 PL | 2186 |
| 20 | 🇿🇦 ZA | 2181 |
| 21 | 🇳🇿 NZ | 2093 |
| 22 | 🇹🇭 TH | 2042 |
| 23 | 🇰🇷 KR | 1970 |
| 24 | 🇵🇭 PH | 1826 |
| 25 | 🇬🇹 GT | 1808 |
| 26 | 🇲🇦 MA | 1407 |
| 27 | 🇲🇪 ME | 1315 |
| 28 | 🇳🇱 NL | 1248 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1168 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2771 |
| 2 | Denver International Airport |  | US | 2249 |
| 3 | Tokyo International Airport |  | JP | 1867 |
| 4 | Indira Gandhi International Airport |  | IN | 1716 |
| 5 | Harry Reid International Airport |  | US | 1649 |
| 6 | Guaymaral Airport |  | CO | 1621 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1556 |
| 8 | Zurich Airport |  | CH | 1475 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1412 |
| 10 | La Aurora Airport |  | GT | 1396 |
| 11 | Frankfurt am Main International Airport |  | DE | 1336 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1281 |
| 13 | Chicago O'Hare International Airport |  | US | 1275 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1184 |
| 16 | Salt Lake City International Airport |  | US | 1181 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1145 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1088 |
| 19 | Madrid Barajas International Airport |  | ES | 1085 |
| 20 | Capua Airport |  | IT | 1083 |
| 21 | Congonhas Airport |  | BR | 1061 |
| 22 | Kuala Lumpur International Airport |  | MY | 1024 |
| 23 | Charlotte/Douglas International Airport |  | US | 986 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 964 |
| 25 | Charles de Gaulle International Airport |  | FR | 957 |
| 26 | Bengaluru International Airport |  | IN | 935 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 911 |
| 28 | Malpensa International Airport |  | IT | 881 |
| 29 | Ninoy Aquino International Airport |  | PH | 848 |
| 30 | Daniel K Inouye International Airport |  | US | 828 |
| 31 | Barcelona International Airport |  | ES | 817 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 812 |
| 33 | Tenerife Norte Airport |  | ES | 797 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 781 |
| 35 | Calgary International Airport |  | CA | 775 |
| 36 | Seattle-Tacoma International Airport |  | US | 765 |
| 37 | Scottsdale Airport |  | US | 761 |
| 38 | Viracopos International Airport |  | BR | 756 |
| 39 | Vitoria/Foronda Airport |  | ES | 755 |
| 40 | Amsterdam Airport Schiphol |  | NL | 750 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 681 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 481 | 21m | 244 km | 2,025.4 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 333 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 332 | 24m | 225 km | 1,288.0 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 321 | 1h 10m | 770 km | 4,264.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 285 | 14m | 114 km | 559.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 250 | 26m | 275 km | 1,184.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 241 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 194 | 22m | 55 km | 184.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 185 | 44m | 241 km | 768.5 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 184 | 26m | 215 km | 681.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 184 | 20m | 99 km | 315.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 179 | 13m | - | - |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 178 | 1h 46m | 1,423 km | 4,368.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 165 | 31m | 369 km | 1,050.3 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 162 | 18m | 144 km | 403.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 159 | 44m | 452 km | 1,239.2 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 156 | 1h 1m | 695 km | 1,870.0 t |
| 26 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 151 | 1h 38m | 1,156 km | 3,012.4 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
|  |  | Hakodate Airport (RJCH) | Hakodate Airport (RJCH) | 2026-07-08 02:45 UTC | 2026-07-08 03:11 UTC | 26m |
| EJA471 | EJA | Harry Reid International Airport (KLAS) | Santa Monica Municipal Airport (KSMO) | 2026-07-08 02:28 UTC | 2026-07-08 03:10 UTC | 42m |
| QTR643 | Qatar Airways | VGZR (VGZR) | Arzanah Airport (OMAR) | 2026-07-07 22:50 UTC | 2026-07-08 03:10 UTC | 4h 20m |
| C6521 |  | Mobile Regional Airport (KMOB) | Bay Minette Municipal Airport (K1R8) | 2026-07-08 01:36 UTC | 2026-07-08 03:09 UTC | 1h 33m |
| EQV | EQV | Watts Bridge Airport (YWSG) | Sunshine Coast Airport (YBMC) | 2026-07-08 02:42 UTC | 2026-07-08 03:05 UTC | 22m |
| TIGER63 | TIG | 2TX3 (2TX3) | Anacacho Ranch Airport (0XS7) | 2026-07-08 02:49 UTC | 2026-07-08 03:04 UTC | 14m |
| TKR12 | TKR | Roberts Field (KRDM) | Collins Landing Strip (04OR) | 2026-07-08 02:52 UTC | 2026-07-08 03:03 UTC | 10m |
|  |  | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-08 02:59 UTC | 2026-07-08 03:00 UTC | 0m |
| LBQ791 | LBQ | Alexander Salamon Airport (KAMT) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-08 02:48 UTC | 2026-07-08 02:59 UTC | 10m |
| YHT | YHT | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-08 02:40 UTC | 2026-07-08 02:57 UTC | 17m |
| WL51 |  | Atsugi Naval Air Facility (RJTA) | Kisarazu Airport (RJTK) | 2026-07-08 01:59 UTC | 2026-07-08 02:55 UTC | 56m |
| KYOTE36 | KYO | Phoenix Sky Harbor International Airport (KPHX) | Phoenix Sky Harbor International Airport (KPHX) | 2026-07-08 02:38 UTC | 2026-07-08 02:50 UTC | 12m |
| SGA2565 | SGA | Lashio Airport (VYLS) | Zhuhai Airport (ZGSD) | 2026-07-08 00:54 UTC | 2026-07-08 02:47 UTC | 1h 52m |
| VOZ1349 | Virgin Australia | Sydney Kingsford Smith International Airport (YSSY) | Darwin International Airport (YPDN) | 2026-07-07 22:03 UTC | 2026-07-08 02:43 UTC | 4h 39m |
| N559SH |  | Gold King Creek Airport (PAAN) | Healy River Airport (PAHV) | 2026-07-08 02:36 UTC | 2026-07-08 02:41 UTC | 5m |
| TKR137 | TKR | Roberts Field (KRDM) | Six Springs Ranch Airport (OG51) | 2026-07-08 02:35 UTC | 2026-07-08 02:41 UTC | 5m |
| AM312 |  | Melbourne Essendon Airport (YMEN) | RAAF Base East Sale (YMES) | 2026-07-08 02:09 UTC | 2026-07-08 02:38 UTC | 28m |
| FD478 |  | Brisbane International Airport (YBBN) | Oakey Airport (YBOK) | 2026-07-08 02:16 UTC | 2026-07-08 02:36 UTC | 20m |
| GH12 |  | Imperial Beach Nolf (Ream Field) Airport (KNRS) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-07-08 01:33 UTC | 2026-07-08 02:36 UTC | 1h 3m |
| AIC8PB | Air India | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-07-08 02:10 UTC | 2026-07-08 02:32 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
