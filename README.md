# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_00:41:18_UTC-green)

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

**Latest saved flight:** 2026-09-15 00:41:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-15 00:41:18 UTC

- **258,899** saved flights
- **76,920** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **258,899** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,135,307.2 tonnes** estimated CO2 emissions
- **181,756,941 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10263 |
| 2 | SkyWest Airlines | 9030 |
| 3 | EJA | 5024 |
| 4 | IndiGo | 4341 |
| 5 | American Airlines | 4087 |
| 6 | Southwest Airlines | 3809 |
| 7 | Delta Air Lines | 3237 |
| 8 | ENY | 3070 |
| 9 | LATAM Airlines | 2489 |
| 10 | AZU | 2427 |
| 11 | Vueling | 2189 |
| 12 | WIF | 2076 |
| 13 | LXJ | 2024 |
| 14 | Lufthansa | 2018 |
| 15 | easyJet | 1763 |
| 16 | Swiss International | 1727 |
| 17 | QLK | 1672 |
| 18 | AXM | 1647 |
| 19 | EJU | 1641 |
| 20 | United Airlines | 1597 |
| 21 | Alaska Airlines | 1537 |
| 22 | All Nippon Airways | 1501 |
| 23 | WMT | 1462 |
| 24 | GLO | 1443 |
| 25 | PGT | 1438 |
| 26 | VIV | 1419 |
| 27 | Air France | 1415 |
| 28 | Wizz Air | 1409 |
| 29 | TKR | 1252 |
| 30 | AEE | 1250 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 215007 |
| 2 | 🇪🇸 ES | 16404 |
| 3 | 🇧🇷 BR | 15130 |
| 4 | 🇦🇺 AU | 14774 |
| 5 | 🇨🇦 CA | 14408 |
| 6 | 🇮🇹 IT | 14097 |
| 7 | 🇮🇳 IN | 13647 |
| 8 | 🇩🇪 DE | 12585 |
| 9 | 🇬🇧 GB | 12057 |
| 10 | 🇨🇴 CO | 11635 |
| 11 | 🇫🇷 FR | 10395 |
| 12 | 🇯🇵 JP | 10074 |
| 13 | 🇹🇷 TR | 7804 |
| 14 | 🇬🇷 GR | 7532 |
| 15 | 🇲🇽 MX | 7142 |
| 16 | 🇨🇭 CH | 6941 |
| 17 | 🇳🇴 NO | 6389 |
| 18 | 🇹🇭 TH | 4647 |
| 19 | 🇲🇾 MY | 4433 |
| 20 | 🇿🇦 ZA | 4392 |
| 21 | 🇵🇱 PL | 4284 |
| 22 | 🇳🇿 NZ | 3578 |
| 23 | 🇵🇭 PH | 3475 |
| 24 | 🇬🇹 GT | 3270 |
| 25 | 🇭🇷 HR | 2967 |
| 26 | 🇰🇷 KR | 2959 |
| 27 | 🇲🇦 MA | 2597 |
| 28 | 🇲🇪 ME | 2437 |
| 29 | 🇳🇱 NL | 2323 |
| 30 | 🇮🇩 ID | 2194 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5310 |
| 2 | Denver International Airport |  | US | 4189 |
| 3 | Indira Gandhi International Airport |  | IN | 3126 |
| 4 | Tokyo International Airport |  | JP | 3006 |
| 5 | Guaymaral Airport |  | CO | 2767 |
| 6 | Harry Reid International Airport |  | US | 2749 |
| 7 | Zurich Airport |  | CH | 2713 |
| 8 | El Dorado International Airport |  | CO | 2711 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2609 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2523 |
| 11 | La Aurora Airport |  | GT | 2484 |
| 12 | Salt Lake City International Airport |  | US | 2287 |
| 13 | Chicago O'Hare International Airport |  | US | 2250 |
| 14 | Congonhas Airport |  | BR | 2215 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2118 |
| 16 | Capua Airport |  | IT | 2025 |
| 17 | Madrid Barajas International Airport |  | ES | 2013 |
| 18 | Frankfurt am Main International Airport |  | DE | 1992 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1947 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1867 |
| 21 | Malpensa International Airport |  | IT | 1862 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1825 |
| 23 | Charles de Gaulle International Airport |  | FR | 1823 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1788 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1760 |
| 26 | Macau International Airport |  | MO | 1714 |
| 27 | Ninoy Aquino International Airport |  | PH | 1703 |
| 28 | Barcelona International Airport |  | ES | 1623 |
| 29 | Charlotte/Douglas International Airport |  | US | 1621 |
| 30 | Kuala Lumpur International Airport |  | MY | 1595 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1591 |
| 32 | Viracopos International Airport |  | BR | 1563 |
| 33 | Seattle-Tacoma International Airport |  | US | 1520 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1509 |
| 35 | Don Mueang International Airport |  | TH | 1486 |
| 36 | Calgary International Airport |  | CA | 1482 |
| 37 | Bengaluru International Airport |  | IN | 1469 |
| 38 | Oslo Gardermoen Airport |  | NO | 1458 |
| 39 | Vancouver International Airport |  | CA | 1452 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1392 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 966 | 21m | 244 km | 4,067.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 698 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 648 | 1h 6m | 770 km | 8,608.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 646 | 24m | 225 km | 2,506.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 578 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 419 | 27m | 275 km | 1,985.5 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 419 | 44m | 555 km | 4,012.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 392 | 44m | 241 km | 1,628.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 364 | 24m | 218 km | 1,371.3 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 356 | 21m | 250 km | 1,537.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 345 | 23m | 55 km | 327.9 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 326 | 1h 6m | 706 km | 3,969.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 322 | 19m | 99 km | 551.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 321 | 26m | 215 km | 1,188.8 t |
| 19 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 316 | 12m | - | - |
| 20 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 310 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 298 | 1h 14m | 961 km | 4,939.5 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 279 | 1h 50m | 1,304 km | 6,276.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 274 | 42m | 535 km | 2,530.6 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9055F |  | Red Dog Airport (PADG) | Kivalina Airport (PAVL) | 2026-09-15 00:15 UTC | 2026-09-15 00:41 UTC | 25m |
| BRG644 | BRG | Buckland Airport (PABL) | Deering Airport (PADE) | 2026-09-15 00:18 UTC | 2026-09-15 00:34 UTC | 16m |
| ZKSBJ | ZKS | Hood Airport (NZMS) | Hood Airport (NZMS) | 2026-09-15 00:10 UTC | 2026-09-15 00:34 UTC | 23m |
| N59BF |  | California Pines Airport (KA24) | Chiloquin State Airport (K2S7) | 2026-09-14 22:09 UTC | 2026-09-15 00:31 UTC | 2h 22m |
| N72MZ |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-09-14 23:13 UTC | 2026-09-15 00:25 UTC | 1h 11m |
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-09-14 22:39 UTC | 2026-09-15 00:25 UTC | 1h 45m |
| N384CA |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-09-14 23:56 UTC | 2026-09-15 00:21 UTC | 24m |
| PQE | PQE | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-09-14 23:33 UTC | 2026-09-15 00:19 UTC | 46m |
| C2714 |  | Mc Clellan Airfield (KMCC) | Lake Tahoe Airport (KTVL) | 2026-09-14 23:52 UTC | 2026-09-15 00:16 UTC | 23m |
| VAMPYR01 | VAM | Somerton Airport (54AZ) | Somerton Airport (54AZ) | 2026-09-14 23:15 UTC | 2026-09-15 00:07 UTC | 52m |
| N756DN |  | Brown Field Municipal Airport (KSDM) | Brown Field Municipal Airport (KSDM) | 2026-09-14 23:46 UTC | 2026-09-15 00:04 UTC | 18m |
| IFL531 | IFL | Laredo International Airport (KLRD) | Plan De Guadalupe International Airport (MMIO) | 2026-09-14 23:34 UTC | 2026-09-15 00:03 UTC | 28m |
| RXA6518 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Cudal Airport (YCUA) | 2026-09-14 23:22 UTC | 2026-09-14 23:58 UTC | 35m |
| TKR102 | TKR | Boyd Airport (TX36) | Boyd Airport (TX36) | 2026-09-14 23:28 UTC | 2026-09-14 23:58 UTC | 30m |
| ICY99 | ICY | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-09-14 23:23 UTC | 2026-09-14 23:53 UTC | 30m |
| QTR8406 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-09-14 16:17 UTC | 2026-09-14 23:53 UTC | 7h 35m |
| LPE2482 | LPE | Jorge Chavez International Airport (SPJC) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-09-14 17:15 UTC | 2026-09-14 23:52 UTC | 6h 36m |
| VOZ1316 | Virgin Australia | Melbourne International Airport (YMML) | Jericho Airport (YJCO) | 2026-09-14 23:04 UTC | 2026-09-14 23:51 UTC | 47m |
| QLK28D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-09-14 23:17 UTC | 2026-09-14 23:47 UTC | 30m |
| CLX1631 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-09-14 13:04 UTC | 2026-09-14 23:45 UTC | 10h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
