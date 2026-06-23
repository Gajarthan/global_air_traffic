# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_21:50:11_UTC-green)

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

**Latest saved flight:** 2026-06-23 21:50:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-23 21:50:11 UTC

- **118,425** saved flights
- **40,861** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **118,425** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,435,297.6 tonnes** estimated CO2 emissions
- **83,205,657 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4876 |
| 2 | SkyWest Airlines | 4383 |
| 3 | EJA | 2292 |
| 4 | IndiGo | 2279 |
| 5 | American Airlines | 1845 |
| 6 | Southwest Airlines | 1769 |
| 7 | ENY | 1484 |
| 8 | Delta Air Lines | 1398 |
| 9 | Lufthansa | 1300 |
| 10 | Vueling | 1071 |
| 11 | LATAM Airlines | 1049 |
| 12 | WIF | 1045 |
| 13 | AZU | 990 |
| 14 | AXM | 969 |
| 15 | LXJ | 900 |
| 16 | Swiss International | 834 |
| 17 | All Nippon Airways | 811 |
| 18 | Alaska Airlines | 787 |
| 19 | QLK | 761 |
| 20 | easyJet | 760 |
| 21 | EJU | 740 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 660 |
| 24 | VIV | 652 |
| 25 | United Airlines | 649 |
| 26 | Air France | 648 |
| 27 | CXK | 636 |
| 28 | MXY | 623 |
| 29 | AXB | 585 |
| 30 | GLO | 582 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 100229 |
| 2 | 🇪🇸 ES | 8076 |
| 3 | 🇮🇳 IN | 7165 |
| 4 | 🇦🇺 AU | 6991 |
| 5 | 🇧🇷 BR | 6544 |
| 6 | 🇮🇹 IT | 6316 |
| 7 | 🇩🇪 DE | 6305 |
| 8 | 🇨🇦 CA | 6234 |
| 9 | 🇯🇵 JP | 5294 |
| 10 | 🇬🇧 GB | 5185 |
| 11 | 🇫🇷 FR | 4706 |
| 12 | 🇨🇴 CO | 4000 |
| 13 | 🇲🇽 MX | 3479 |
| 14 | 🇬🇷 GR | 3379 |
| 15 | 🇳🇴 NO | 3248 |
| 16 | 🇨🇭 CH | 3033 |
| 17 | 🇲🇾 MY | 2519 |
| 18 | 🇹🇷 TR | 2425 |
| 19 | 🇿🇦 ZA | 1991 |
| 20 | 🇵🇱 PL | 1946 |
| 21 | 🇳🇿 NZ | 1925 |
| 22 | 🇹🇭 TH | 1900 |
| 23 | 🇰🇷 KR | 1896 |
| 24 | 🇵🇭 PH | 1706 |
| 25 | 🇬🇹 GT | 1661 |
| 26 | 🇲🇦 MA | 1281 |
| 27 | 🇲🇪 ME | 1170 |
| 28 | 🇲🇴 MO | 1170 |
| 29 | 🇳🇱 NL | 1136 |
| 30 | 🇭🇷 HR | 1026 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2497 |
| 2 | Denver International Airport |  | US | 1989 |
| 3 | Tokyo International Airport |  | JP | 1754 |
| 4 | Indira Gandhi International Airport |  | IN | 1571 |
| 5 | Guaymaral Airport |  | CO | 1490 |
| 6 | Harry Reid International Airport |  | US | 1473 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1440 |
| 8 | Zurich Airport |  | CH | 1321 |
| 9 | La Aurora Airport |  | GT | 1283 |
| 10 | Frankfurt am Main International Airport |  | DE | 1262 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1258 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1176 |
| 13 | El Dorado International Airport |  | CO | 1171 |
| 14 | Macau International Airport |  | MO | 1170 |
| 15 | Chicago O'Hare International Airport |  | US | 1161 |
| 16 | Capua Airport |  | IT | 1022 |
| 17 | Salt Lake City International Airport |  | US | 1013 |
| 18 | Madrid Barajas International Airport |  | ES | 998 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 993 |
| 20 | Kuala Lumpur International Airport |  | MY | 974 |
| 21 | Congonhas Airport |  | BR | 911 |
| 22 | Charlotte/Douglas International Airport |  | US | 900 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 893 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 878 |
| 25 | Bengaluru International Airport |  | IN | 870 |
| 26 | Charles de Gaulle International Airport |  | FR | 867 |
| 27 | Malpensa International Airport |  | IT | 833 |
| 28 | Ninoy Aquino International Airport |  | PH | 788 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 776 |
| 30 | Daniel K Inouye International Airport |  | US | 768 |
| 31 | Tenerife Norte Airport |  | ES | 760 |
| 32 | Barcelona International Airport |  | ES | 751 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 734 |
| 34 | Calgary International Airport |  | CA | 694 |
| 35 | Vitoria/Foronda Airport |  | ES | 694 |
| 36 | Amsterdam Airport Schiphol |  | NL | 690 |
| 37 | Don Mueang International Airport |  | TH | 687 |
| 38 | Seattle-Tacoma International Airport |  | US | 680 |
| 39 | Viracopos International Airport |  | BR | 673 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 672 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 619 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 430 | 21m | 244 km | 1,810.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 313 | 24m | 225 km | 1,214.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 304 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 289 | 1h 25m | 910 km | 4,535.1 t |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 7 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 285 | 1h 10m | 770 km | 3,786.0 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 234 | 26m | 275 km | 1,108.8 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 234 | 19m | 165 km | 665.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 218 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 176 | 22m | 55 km | 167.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 170 | 26m | 215 km | 629.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 170 | 20m | 99 km | 291.2 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 160 | 44m | 241 km | 664.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 160 | 27m | 152 km | 418.1 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 153 | 44m | 452 km | 1,192.4 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 148 | 1h 44m | 1,423 km | 3,632.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 148 | 20m | 250 km | 639.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 148 | 18m | 144 km | 368.1 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 138 | 1h 39m | 1,156 km | 2,753.0 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 134 | 1h 17m | 961 km | 2,221.1 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N970MB |  | Elk Park Ranch Airport (34CD) | Elk Park Ranch Airport (34CD) | 2026-06-23 20:41 UTC | 2026-06-23 21:50 UTC | 1h 8m |
| N756DN |  | Brown Field Municipal Airport (KSDM) | Brown Field Municipal Airport (KSDM) | 2026-06-23 21:31 UTC | 2026-06-23 21:48 UTC | 16m |
| FHDFI | FHD | Dax Seyresse Airport (LFBY) | Dax Seyresse Airport (LFBY) | 2026-06-23 21:14 UTC | 2026-06-23 21:42 UTC | 28m |
| N504RP |  | Oakland County International Airport (KPTK) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-06-23 20:24 UTC | 2026-06-23 21:40 UTC | 1h 16m |
| N716AP |  | Shreveport Regional Airport (KSHV) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-06-23 20:25 UTC | 2026-06-23 21:34 UTC | 1h 8m |
| N759DB |  | Creve Coeur Airport (K1H0) | Creve Coeur Airport (K1H0) | 2026-06-23 21:05 UTC | 2026-06-23 21:27 UTC | 21m |
| TKR184 | TKR | NM36 (NM36) | Biplane Ranch Airport (NM02) | 2026-06-23 21:06 UTC | 2026-06-23 21:26 UTC | 19m |
| N917JG |  | Truckee-Tahoe Airport (KTRK) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-23 20:40 UTC | 2026-06-23 21:25 UTC | 44m |
| N715ST |  | Orlando Executive Airport (KORL) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-06-23 19:59 UTC | 2026-06-23 21:25 UTC | 1h 25m |
| CFR83 | CFR | Columbia Airport (KO22) | 6CL4 (6CL4) | 2026-06-23 21:10 UTC | 2026-06-23 21:23 UTC | 13m |
| N450CA |  | Majors Airport (KGVT) | Commerce Municipal Airport (K2F7) | 2026-06-23 20:53 UTC | 2026-06-23 21:21 UTC | 28m |
| N554SC |  | Christmas Flying Service Airport (MS03) | Christmas Flying Service Airport (MS03) | 2026-06-23 20:03 UTC | 2026-06-23 21:21 UTC | 1h 18m |
| N259CA |  | Wiley Post Airport (KPWA) | Gunnison-Crested Butte Regional Airport (KGUC) | 2026-06-23 20:02 UTC | 2026-06-23 21:19 UTC | 1h 17m |
| BRG571 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-06-23 20:49 UTC | 2026-06-23 21:18 UTC | 29m |
| N427KS |  | Anacortes Airport (K74S) | 3WA1 (3WA1) | 2026-06-23 20:37 UTC | 2026-06-23 21:15 UTC | 37m |
| PSJJB | PSJ | Eurico de Aguiar Salles Airport (SBVT) | Tamboril Airport (SNTL) | 2026-06-23 19:01 UTC | 2026-06-23 21:13 UTC | 2h 12m |
| N5SH |  | Monroe County Airport (KBMG) | Eagle Creek Airpark (KEYE) | 2026-06-23 20:51 UTC | 2026-06-23 21:11 UTC | 19m |
| N795HC |  | Centennial Airport (KAPA) | Fry Canyon Field (UT74) | 2026-06-23 20:23 UTC | 2026-06-23 21:09 UTC | 46m |
| N821V |  | Mefford Field (KTLR) | Rosamond Skypark Airport (KL00) | 2026-06-23 20:25 UTC | 2026-06-23 21:05 UTC | 39m |
| SIL1504 | SIL | King Salmon Airport (PAKN) | Ted Stevens Anchorage International Airport (PANC) | 2026-06-23 19:39 UTC | 2026-06-23 21:04 UTC | 1h 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
