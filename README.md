# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_21:09:50_UTC-green)

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

**Latest saved flight:** 2026-08-15 21:09:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 21:09:50 UTC

- **199,925** saved flights
- **62,403** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **199,925** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,388,742.9 tonnes** estimated CO2 emissions
- **138,477,851 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7967 |
| 2 | SkyWest Airlines | 7180 |
| 3 | EJA | 3923 |
| 4 | IndiGo | 3446 |
| 5 | Southwest Airlines | 3097 |
| 6 | American Airlines | 3085 |
| 7 | ENY | 2471 |
| 8 | Delta Air Lines | 2364 |
| 9 | LATAM Airlines | 1884 |
| 10 | AZU | 1820 |
| 11 | Lufthansa | 1708 |
| 12 | Vueling | 1681 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1587 |
| 15 | easyJet | 1379 |
| 16 | Swiss International | 1349 |
| 17 | AXM | 1308 |
| 18 | EJU | 1240 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1107 |
| 23 | GLO | 1086 |
| 24 | Air France | 1065 |
| 25 | PGT | 1058 |
| 26 | AEE | 1030 |
| 27 | United Airlines | 1016 |
| 28 | CXK | 1010 |
| 29 | WMT | 1009 |
| 30 | Wizz Air | 991 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 169447 |
| 2 | 🇪🇸 ES | 12932 |
| 3 | 🇧🇷 BR | 11540 |
| 4 | 🇦🇺 AU | 11150 |
| 5 | 🇨🇦 CA | 10932 |
| 6 | 🇮🇳 IN | 10764 |
| 7 | 🇮🇹 IT | 10502 |
| 8 | 🇩🇪 DE | 9923 |
| 9 | 🇬🇧 GB | 9391 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇫🇷 FR | 7988 |
| 12 | 🇨🇴 CO | 7984 |
| 13 | 🇬🇷 GR | 5904 |
| 14 | 🇲🇽 MX | 5653 |
| 15 | 🇹🇷 TR | 5567 |
| 16 | 🇨🇭 CH | 5414 |
| 17 | 🇳🇴 NO | 5077 |
| 18 | 🇲🇾 MY | 3428 |
| 19 | 🇿🇦 ZA | 3370 |
| 20 | 🇵🇱 PL | 3304 |
| 21 | 🇹🇭 TH | 3131 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2641 |
| 24 | 🇬🇹 GT | 2550 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2132 |
| 27 | 🇲🇦 MA | 2029 |
| 28 | 🇳🇱 NL | 1798 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1633 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4170 |
| 2 | Denver International Airport |  | US | 3250 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2474 |
| 5 | Indira Gandhi International Airport |  | IN | 2441 |
| 6 | Harry Reid International Airport |  | US | 2276 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2115 |
| 8 | Zurich Airport |  | CH | 2109 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2066 |
| 10 | La Aurora Airport |  | GT | 1953 |
| 11 | El Dorado International Airport |  | CO | 1846 |
| 12 | Salt Lake City International Airport |  | US | 1777 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1777 |
| 14 | Chicago O'Hare International Airport |  | US | 1756 |
| 15 | Congonhas Airport |  | BR | 1689 |
| 16 | Frankfurt am Main International Airport |  | DE | 1680 |
| 17 | Madrid Barajas International Airport |  | ES | 1579 |
| 18 | Capua Airport |  | IT | 1539 |
| 19 | Macau International Airport |  | MO | 1536 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1515 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1471 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1446 |
| 23 | Malpensa International Airport |  | IT | 1396 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1383 |
| 25 | Charles de Gaulle International Airport |  | FR | 1376 |
| 26 | Charlotte/Douglas International Airport |  | US | 1318 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1256 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1249 |
| 30 | Ninoy Aquino International Airport |  | PH | 1249 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1219 |
| 32 | Barcelona International Airport |  | ES | 1205 |
| 33 | Viracopos International Airport |  | BR | 1166 |
| 34 | Seattle-Tacoma International Airport |  | US | 1143 |
| 35 | Calgary International Airport |  | CA | 1137 |
| 36 | Reno/Tahoe International Airport |  | US | 1126 |
| 37 | Oslo Gardermoen Airport |  | NO | 1120 |
| 38 | Vitoria/Foronda Airport |  | ES | 1117 |
| 39 | Daniel K Inouye International Airport |  | US | 1102 |
| 40 | Tenerife Norte Airport |  | ES | 1095 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 488 | 1h 7m | 770 km | 6,482.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 465 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 379 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 341 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 340 | 27m | 275 km | 1,611.1 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 292 | 1h 49m | 1,423 km | 7,166.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 286 | 22m | 55 km | 271.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 251 | 24m | 218 km | 945.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 244 | 1h 14m | 961 km | 4,044.4 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 244 | 19m | 99 km | 418.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 238 | 1h 37m | 1,156 km | 4,748.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 234 | 19m | 144 km | 582.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 217 | 1h 48m | 1,304 km | 4,881.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N83FE |  | Humphreys County Airport (K0M5) | Humphreys County Airport (K0M5) | 2026-08-15 20:59 UTC | 2026-08-15 21:09 UTC | 10m |
| N945RF |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-15 20:37 UTC | 2026-08-15 20:55 UTC | 18m |
| N45DG |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-08-15 19:43 UTC | 2026-08-15 20:54 UTC | 1h 11m |
| N469TS |  | Orange County Airport (KOMH) | Orange County Airport (KOMH) | 2026-08-15 20:13 UTC | 2026-08-15 20:53 UTC | 39m |
| BOE449 | BOE | Renton Municipal Airport (KRNT) | Christensen Field (8WA6) | 2026-08-15 19:02 UTC | 2026-08-15 20:53 UTC | 1h 51m |
| N545BB |  | Corpus Christi International Airport (KCRP) | Easterwood Field (KCLL) | 2026-08-15 19:42 UTC | 2026-08-15 20:48 UTC | 1h 5m |
| JPR09 | JPR | Easton State Airport (KESW) | Easton State Airport (KESW) | 2026-08-15 20:38 UTC | 2026-08-15 20:48 UTC | 9m |
| N330V |  | Kintail Farm Airport (GA00) | Cy Nunnally Memorial Airport (KD73) | 2026-08-15 20:36 UTC | 2026-08-15 20:47 UTC | 10m |
| N888YW |  | San Gabriel Valley Airport (KEMT) | Hemet-Ryan Airport (KHMT) | 2026-08-15 19:56 UTC | 2026-08-15 20:36 UTC | 40m |
| N233S |  | Minden-Tahoe Airport (KMEV) | Desert Creek Airport (NV97) | 2026-08-15 19:32 UTC | 2026-08-15 20:30 UTC | 58m |
| N562JL |  | Reno/Tahoe International Airport (KRNO) | Grupe Ranch Airport (5CL0) | 2026-08-15 19:30 UTC | 2026-08-15 20:30 UTC | 59m |
| N100JF |  | Plantation Airpark (KJYL) | Plantation Airpark (KJYL) | 2026-08-15 20:09 UTC | 2026-08-15 20:28 UTC | 19m |
| PXT504 | PXT | Reno/Tahoe International Airport (KRNO) | Palm Springs International Airport (KPSP) | 2026-08-15 19:18 UTC | 2026-08-15 20:27 UTC | 1h 9m |
| N38EE |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-08-15 19:28 UTC | 2026-08-15 20:26 UTC | 58m |
| N7277F |  | Guaymaral Airport (SKGY) | SKAN (SKAN) | 2026-08-15 19:41 UTC | 2026-08-15 20:19 UTC | 37m |
| EFY6915 | EFY | Enrique Olaya Herrera Airport (SKMD) | Alfonso Bonilla Aragon International Airport (SKCL) | 2026-08-15 19:38 UTC | 2026-08-15 20:17 UTC | 39m |
| MSR688 | EgyptAir | Cairo International Airport (HECA) | HE13 (HE13) | 2026-08-15 14:15 UTC | 2026-08-15 20:17 UTC | 6h 2m |
|  |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-08-15 20:15 UTC | 2026-08-15 20:15 UTC | 0m |
| HK2978G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-15 19:50 UTC | 2026-08-15 20:14 UTC | 24m |
| JUMP16 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-15 18:48 UTC | 2026-08-15 20:14 UTC | 1h 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
