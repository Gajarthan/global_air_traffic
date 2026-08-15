# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_21:43:43_UTC-green)

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

**Latest saved flight:** 2026-08-15 21:43:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 21:43:43 UTC

- **199,997** saved flights
- **62,420** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **199,997** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,389,759.1 tonnes** estimated CO2 emissions
- **138,536,760 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7971 |
| 2 | SkyWest Airlines | 7186 |
| 3 | EJA | 3924 |
| 4 | IndiGo | 3446 |
| 5 | Southwest Airlines | 3099 |
| 6 | American Airlines | 3088 |
| 7 | ENY | 2472 |
| 8 | Delta Air Lines | 2365 |
| 9 | LATAM Airlines | 1885 |
| 10 | AZU | 1820 |
| 11 | Lufthansa | 1708 |
| 12 | Vueling | 1682 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1588 |
| 15 | easyJet | 1381 |
| 16 | Swiss International | 1349 |
| 17 | AXM | 1308 |
| 18 | EJU | 1240 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1175 |
| 22 | VIV | 1108 |
| 23 | GLO | 1087 |
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
| 1 | 🇺🇸 US | 169521 |
| 2 | 🇪🇸 ES | 12934 |
| 3 | 🇧🇷 BR | 11544 |
| 4 | 🇦🇺 AU | 11150 |
| 5 | 🇨🇦 CA | 10941 |
| 6 | 🇮🇳 IN | 10764 |
| 7 | 🇮🇹 IT | 10506 |
| 8 | 🇩🇪 DE | 9923 |
| 9 | 🇬🇧 GB | 9396 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇨🇴 CO | 7995 |
| 12 | 🇫🇷 FR | 7989 |
| 13 | 🇬🇷 GR | 5905 |
| 14 | 🇲🇽 MX | 5657 |
| 15 | 🇹🇷 TR | 5569 |
| 16 | 🇨🇭 CH | 5414 |
| 17 | 🇳🇴 NO | 5077 |
| 18 | 🇲🇾 MY | 3428 |
| 19 | 🇿🇦 ZA | 3370 |
| 20 | 🇵🇱 PL | 3305 |
| 21 | 🇹🇭 TH | 3131 |
| 22 | 🇳🇿 NZ | 2776 |
| 23 | 🇵🇭 PH | 2641 |
| 24 | 🇬🇹 GT | 2550 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2135 |
| 27 | 🇲🇦 MA | 2029 |
| 28 | 🇳🇱 NL | 1798 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1633 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4174 |
| 2 | Denver International Airport |  | US | 3253 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2474 |
| 5 | Indira Gandhi International Airport |  | IN | 2441 |
| 6 | Harry Reid International Airport |  | US | 2276 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2115 |
| 8 | Zurich Airport |  | CH | 2109 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2066 |
| 10 | La Aurora Airport |  | GT | 1953 |
| 11 | El Dorado International Airport |  | CO | 1848 |
| 12 | Salt Lake City International Airport |  | US | 1779 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1777 |
| 14 | Chicago O'Hare International Airport |  | US | 1758 |
| 15 | Congonhas Airport |  | BR | 1691 |
| 16 | Frankfurt am Main International Airport |  | DE | 1680 |
| 17 | Madrid Barajas International Airport |  | ES | 1579 |
| 18 | Capua Airport |  | IT | 1539 |
| 19 | Macau International Airport |  | MO | 1536 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1516 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1472 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1446 |
| 23 | Malpensa International Airport |  | IT | 1398 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1383 |
| 25 | Charles de Gaulle International Airport |  | FR | 1376 |
| 26 | Charlotte/Douglas International Airport |  | US | 1319 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1256 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1250 |
| 30 | Ninoy Aquino International Airport |  | PH | 1249 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1220 |
| 32 | Barcelona International Airport |  | ES | 1206 |
| 33 | Viracopos International Airport |  | BR | 1166 |
| 34 | Seattle-Tacoma International Airport |  | US | 1145 |
| 35 | Calgary International Airport |  | CA | 1140 |
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
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 382 | 8m | - | - |
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
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 244 | 19m | 99 km | 418.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 238 | 1h 37m | 1,156 km | 4,748.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 234 | 19m | 144 km | 582.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 218 | 1h 48m | 1,304 km | 4,904.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JUMP16 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-15 20:24 UTC | 2026-08-15 21:43 UTC | 1h 18m |
| N403TD |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-15 21:25 UTC | 2026-08-15 21:38 UTC | 12m |
| ERU882 | ERU | Daytona Beach International Airport (KDAB) | KXFL (KXFL) | 2026-08-15 20:22 UTC | 2026-08-15 21:34 UTC | 1h 11m |
| JCY504 | JCY | Chiloquin State Airport (K2S7) | William R Fairchild International Airport (KCLM) | 2026-08-15 20:08 UTC | 2026-08-15 21:30 UTC | 1h 22m |
| N223AL |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-08-15 20:15 UTC | 2026-08-15 21:28 UTC | 1h 13m |
| N499AE |  | Lambert Airport (24LL) | St Louis Downtown Airport (KCPS) | 2026-08-15 21:04 UTC | 2026-08-15 21:27 UTC | 22m |
| ABY842 | ABY | Umm Al Quwain (OMUQ) | Hulwan (HE15) | 2026-08-15 18:24 UTC | 2026-08-15 21:24 UTC | 2h 59m |
| N99519 |  | Merrill Field (PAMR) | Birchwood Airport (PABV) | 2026-08-15 20:45 UTC | 2026-08-15 21:24 UTC | 38m |
| N258JS |  | Santa Monica Municipal Airport (KSMO) | San Gabriel Valley Airport (KEMT) | 2026-08-15 21:09 UTC | 2026-08-15 21:21 UTC | 12m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-15 18:39 UTC | 2026-08-15 21:18 UTC | 2h 39m |
| N981MH |  | Boeing Field/King County International Airport (KBFI) | Boeing Field/King County International Airport (KBFI) | 2026-08-15 21:10 UTC | 2026-08-15 21:12 UTC | 1m |
| N83FE |  | Humphreys County Airport (K0M5) | Humphreys County Airport (K0M5) | 2026-08-15 20:59 UTC | 2026-08-15 21:09 UTC | 10m |
| SKW5324 | SkyWest Airlines | Denver International Airport (KDEN) | Okc Will Rogers International Airport (KOKC) | 2026-08-15 19:49 UTC | 2026-08-15 20:59 UTC | 1h 9m |
| PDT6129 | PDT | Charlotte/Douglas International Airport (KCLT) | Mills Field (KK22) | 2026-08-15 20:17 UTC | 2026-08-15 20:57 UTC | 39m |
| HK1053 |  | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-08-15 20:48 UTC | 2026-08-15 20:57 UTC | 8m |
| N945RF |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-15 20:37 UTC | 2026-08-15 20:55 UTC | 18m |
| SWA2259 | Southwest Airlines | William P Hobby Airport (KHOU) | MS24 (MS24) | 2026-08-15 20:12 UTC | 2026-08-15 20:55 UTC | 42m |
| N45DG |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-08-15 19:43 UTC | 2026-08-15 20:54 UTC | 1h 11m |
| N469TS |  | Orange County Airport (KOMH) | Orange County Airport (KOMH) | 2026-08-15 20:13 UTC | 2026-08-15 20:53 UTC | 39m |
| BOE449 | BOE | Renton Municipal Airport (KRNT) | Christensen Field (8WA6) | 2026-08-15 19:02 UTC | 2026-08-15 20:53 UTC | 1h 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
