# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_21:00:40_UTC-green)

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

**Latest saved flight:** 2026-08-29 21:00:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-29 21:00:40 UTC

- **241,300** saved flights
- **73,226** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **241,300** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,904,406.6 tonnes** estimated CO2 emissions
- **168,371,399 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9683 |
| 2 | SkyWest Airlines | 8465 |
| 3 | EJA | 4668 |
| 4 | IndiGo | 4068 |
| 5 | American Airlines | 3887 |
| 6 | Southwest Airlines | 3632 |
| 7 | Delta Air Lines | 3073 |
| 8 | ENY | 2909 |
| 9 | LATAM Airlines | 2314 |
| 10 | AZU | 2242 |
| 11 | Vueling | 2071 |
| 12 | Lufthansa | 1941 |
| 13 | WIF | 1909 |
| 14 | LXJ | 1869 |
| 15 | easyJet | 1684 |
| 16 | Swiss International | 1627 |
| 17 | AXM | 1597 |
| 18 | EJU | 1546 |
| 19 | QLK | 1538 |
| 20 | United Airlines | 1515 |
| 21 | Alaska Airlines | 1442 |
| 22 | All Nippon Airways | 1429 |
| 23 | WMT | 1358 |
| 24 | GLO | 1346 |
| 25 | VIV | 1322 |
| 26 | Air France | 1320 |
| 27 | PGT | 1318 |
| 28 | Wizz Air | 1302 |
| 29 | AEE | 1194 |
| 30 | JetBlue | 1193 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 199977 |
| 2 | 🇪🇸 ES | 15515 |
| 3 | 🇧🇷 BR | 14063 |
| 4 | 🇦🇺 AU | 13676 |
| 5 | 🇨🇦 CA | 13427 |
| 6 | 🇮🇹 IT | 13201 |
| 7 | 🇮🇳 IN | 12661 |
| 8 | 🇩🇪 DE | 11911 |
| 9 | 🇬🇧 GB | 11399 |
| 10 | 🇨🇴 CO | 10379 |
| 11 | 🇫🇷 FR | 9731 |
| 12 | 🇯🇵 JP | 9686 |
| 13 | 🇹🇷 TR | 7159 |
| 14 | 🇬🇷 GR | 7111 |
| 15 | 🇲🇽 MX | 6659 |
| 16 | 🇨🇭 CH | 6471 |
| 17 | 🇳🇴 NO | 5950 |
| 18 | 🇹🇭 TH | 4380 |
| 19 | 🇲🇾 MY | 4278 |
| 20 | 🇿🇦 ZA | 4217 |
| 21 | 🇵🇱 PL | 4046 |
| 22 | 🇵🇭 PH | 3311 |
| 23 | 🇳🇿 NZ | 3310 |
| 24 | 🇬🇹 GT | 3031 |
| 25 | 🇰🇷 KR | 2849 |
| 26 | 🇭🇷 HR | 2788 |
| 27 | 🇲🇦 MA | 2438 |
| 28 | 🇲🇪 ME | 2255 |
| 29 | 🇳🇱 NL | 2187 |
| 30 | 🇮🇩 ID | 2112 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4980 |
| 2 | Denver International Airport |  | US | 3892 |
| 3 | Indira Gandhi International Airport |  | IN | 2947 |
| 4 | Tokyo International Airport |  | JP | 2883 |
| 5 | Guaymaral Airport |  | CO | 2701 |
| 6 | Harry Reid International Airport |  | US | 2562 |
| 7 | Zurich Airport |  | CH | 2530 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2467 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2405 |
| 10 | El Dorado International Airport |  | CO | 2350 |
| 11 | La Aurora Airport |  | GT | 2311 |
| 12 | Chicago O'Hare International Airport |  | US | 2147 |
| 13 | Salt Lake City International Airport |  | US | 2124 |
| 14 | Congonhas Airport |  | BR | 2055 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1999 |
| 16 | Frankfurt am Main International Airport |  | DE | 1910 |
| 17 | Capua Airport |  | IT | 1903 |
| 18 | Madrid Barajas International Airport |  | ES | 1900 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1813 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1774 |
| 21 | Malpensa International Airport |  | IT | 1728 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1699 |
| 23 | Charles de Gaulle International Airport |  | FR | 1690 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1689 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1608 |
| 27 | Charlotte/Douglas International Airport |  | US | 1546 |
| 28 | Kuala Lumpur International Airport |  | MY | 1545 |
| 29 | Enrique Olaya Herrera Airport |  | CO | 1537 |
| 30 | Barcelona International Airport |  | ES | 1537 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1456 |
| 32 | Viracopos International Airport |  | BR | 1434 |
| 33 | Don Mueang International Airport |  | TH | 1410 |
| 34 | Seattle-Tacoma International Airport |  | US | 1408 |
| 35 | Bengaluru International Airport |  | IN | 1407 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1403 |
| 37 | Calgary International Airport |  | CA | 1385 |
| 38 | Oslo Gardermoen Airport |  | NO | 1354 |
| 39 | Vancouver International Airport |  | CA | 1330 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1319 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1094 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 888 | 21m | 244 km | 3,739.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 621 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 612 | 24m | 225 km | 2,374.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 610 | 1h 6m | 770 km | 8,103.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 546 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 398 | 27m | 275 km | 1,886.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 380 | 1h 50m | 1,423 km | 9,325.8 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 367 | 44m | 555 km | 3,514.2 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 366 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 350 | 44m | 241 km | 1,453.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 328 | 24m | 218 km | 1,235.7 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 321 | 1h 40m | 1,156 km | 6,403.8 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 299 | 19m | 99 km | 512.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 294 | 26m | 215 km | 1,088.9 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 282 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 279 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 275 | 1h 14m | 961 km | 4,558.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 271 | 19m | 144 km | 674.1 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 258 | 1h 50m | 1,304 km | 5,804.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LAE1821 | LAE | Miami International Airport (KMIA) | El Dorado International Airport (SKBO) | 2026-08-29 17:55 UTC | 2026-08-29 21:00 UTC | 3h 5m |
| N407CM |  | Bonny Doon Airport (CL77) | Bonny Doon Airport (CL77) | 2026-08-29 20:24 UTC | 2026-08-29 21:00 UTC | 35m |
| N984BK |  | Indianapolis Executive Airport (KTYQ) | Lincoln Airport (KLNK) | 2026-08-29 19:40 UTC | 2026-08-29 20:59 UTC | 1h 18m |
| N543TH |  | Trenton Mercer Airport (KTTN) | Central Jersey Regional Airport (K47N) | 2026-08-29 19:59 UTC | 2026-08-29 20:51 UTC | 52m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-08-29 20:35 UTC | 2026-08-29 20:50 UTC | 14m |
| DRAG971 | DRA | Martinique Aime Cesaire International Airport (TFFF) | Martinique Aime Cesaire International Airport (TFFF) | 2026-08-29 20:45 UTC | 2026-08-29 20:49 UTC | 3m |
| N951S |  | Washington County Airport (KAFJ) | Wayne County Airport (KBJJ) | 2026-08-29 19:57 UTC | 2026-08-29 20:46 UTC | 48m |
| CGLII | CGL | Tofield Airport (CEV7) | Tofield Airport (CEV7) | 2026-08-29 20:43 UTC | 2026-08-29 20:44 UTC | 1m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-29 19:17 UTC | 2026-08-29 20:43 UTC | 1h 25m |
| CAP424 | CAP | 6CL6 (6CL6) | 6CL4 (6CL4) | 2026-08-29 18:25 UTC | 2026-08-29 20:39 UTC | 2h 14m |
| N94810 |  | Sunriver Airport (KS21) | Prospect State Airport (K64S) | 2026-08-29 20:16 UTC | 2026-08-29 20:37 UTC | 21m |
| CFHOS | CFH | Prince George Airport (CYXS) | Courtenay (Smit Field) Airport (CCS6) | 2026-08-29 19:51 UTC | 2026-08-29 20:37 UTC | 45m |
| N606KA |  | Roche Harbor Airport (WA09) | Clam Harbor Airport (WA35) | 2026-08-29 20:32 UTC | 2026-08-29 20:34 UTC | 1m |
| N144BF |  | ME66 (ME66) | Concord Municipal Airport (KCON) | 2026-08-29 19:43 UTC | 2026-08-29 20:31 UTC | 47m |
| N5355P |  | Rostraver Airport (KFWQ) | Rostraver Airport (KFWQ) | 2026-08-29 20:23 UTC | 2026-08-29 20:30 UTC | 6m |
| N888CM |  | Hanover County Municipal Airport (KOFP) | Hanover County Municipal Airport (KOFP) | 2026-08-29 20:08 UTC | 2026-08-29 20:29 UTC | 21m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-29 20:17 UTC | 2026-08-29 20:28 UTC | 10m |
| CWA922 | CWA | Calgary International Airport (CYYC) | Bow Island Airport (CEF3) | 2026-08-29 19:54 UTC | 2026-08-29 20:25 UTC | 30m |
| N888NC |  | Los Angeles International Airport (KLAX) | Teterboro Airport (KTEB) | 2026-08-29 16:04 UTC | 2026-08-29 20:25 UTC | 4h 20m |
| N459MM |  | Cape May County Airport (KWWD) | Millville Municipal Airport (KMIV) | 2026-08-29 19:22 UTC | 2026-08-29 20:24 UTC | 1h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
