# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_18:01:27_UTC-green)

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

**Latest saved flight:** 2026-08-26 18:01:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 18:01:27 UTC

- **239,247** saved flights
- **72,744** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **239,247** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,881,734.9 tonnes** estimated CO2 emissions
- **167,057,094 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9612 |
| 2 | SkyWest Airlines | 8403 |
| 3 | EJA | 4627 |
| 4 | IndiGo | 4038 |
| 5 | American Airlines | 3864 |
| 6 | Southwest Airlines | 3615 |
| 7 | Delta Air Lines | 3042 |
| 8 | ENY | 2893 |
| 9 | LATAM Airlines | 2296 |
| 10 | AZU | 2227 |
| 11 | Vueling | 2060 |
| 12 | Lufthansa | 1935 |
| 13 | WIF | 1900 |
| 14 | LXJ | 1857 |
| 15 | easyJet | 1667 |
| 16 | Swiss International | 1611 |
| 17 | AXM | 1591 |
| 18 | EJU | 1535 |
| 19 | QLK | 1527 |
| 20 | United Airlines | 1506 |
| 21 | Alaska Airlines | 1431 |
| 22 | All Nippon Airways | 1422 |
| 23 | WMT | 1345 |
| 24 | GLO | 1334 |
| 25 | VIV | 1315 |
| 26 | Air France | 1310 |
| 27 | PGT | 1305 |
| 28 | Wizz Air | 1283 |
| 29 | AEE | 1187 |
| 30 | JetBlue | 1185 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 198122 |
| 2 | 🇪🇸 ES | 15399 |
| 3 | 🇧🇷 BR | 13957 |
| 4 | 🇦🇺 AU | 13575 |
| 5 | 🇨🇦 CA | 13270 |
| 6 | 🇮🇹 IT | 13095 |
| 7 | 🇮🇳 IN | 12576 |
| 8 | 🇩🇪 DE | 11830 |
| 9 | 🇬🇧 GB | 11302 |
| 10 | 🇨🇴 CO | 10220 |
| 11 | 🇯🇵 JP | 9652 |
| 12 | 🇫🇷 FR | 9647 |
| 13 | 🇹🇷 TR | 7110 |
| 14 | 🇬🇷 GR | 7053 |
| 15 | 🇲🇽 MX | 6616 |
| 16 | 🇨🇭 CH | 6424 |
| 17 | 🇳🇴 NO | 5923 |
| 18 | 🇹🇭 TH | 4338 |
| 19 | 🇲🇾 MY | 4264 |
| 20 | 🇿🇦 ZA | 4207 |
| 21 | 🇵🇱 PL | 3985 |
| 22 | 🇵🇭 PH | 3294 |
| 23 | 🇳🇿 NZ | 3291 |
| 24 | 🇬🇹 GT | 3002 |
| 25 | 🇰🇷 KR | 2842 |
| 26 | 🇭🇷 HR | 2771 |
| 27 | 🇲🇦 MA | 2422 |
| 28 | 🇲🇪 ME | 2239 |
| 29 | 🇳🇱 NL | 2167 |
| 30 | 🇮🇩 ID | 2103 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4946 |
| 2 | Denver International Airport |  | US | 3858 |
| 3 | Indira Gandhi International Airport |  | IN | 2926 |
| 4 | Tokyo International Airport |  | JP | 2873 |
| 5 | Guaymaral Airport |  | CO | 2692 |
| 6 | Harry Reid International Airport |  | US | 2545 |
| 7 | Zurich Airport |  | CH | 2509 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2447 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2389 |
| 10 | El Dorado International Airport |  | CO | 2303 |
| 11 | La Aurora Airport |  | GT | 2291 |
| 12 | Chicago O'Hare International Airport |  | US | 2138 |
| 13 | Salt Lake City International Airport |  | US | 2100 |
| 14 | Congonhas Airport |  | BR | 2034 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1990 |
| 16 | Frankfurt am Main International Airport |  | DE | 1898 |
| 17 | Capua Airport |  | IT | 1889 |
| 18 | Madrid Barajas International Airport |  | ES | 1878 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1803 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1760 |
| 21 | Malpensa International Airport |  | IT | 1717 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1685 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1680 |
| 24 | Charles de Gaulle International Airport |  | FR | 1675 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1598 |
| 27 | Kuala Lumpur International Airport |  | MY | 1541 |
| 28 | Charlotte/Douglas International Airport |  | US | 1533 |
| 29 | Barcelona International Airport |  | ES | 1524 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1513 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1446 |
| 32 | Viracopos International Airport |  | BR | 1427 |
| 33 | Don Mueang International Airport |  | TH | 1400 |
| 34 | Bengaluru International Airport |  | IN | 1399 |
| 35 | Seattle-Tacoma International Airport |  | US | 1392 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1390 |
| 37 | Calgary International Airport |  | CA | 1373 |
| 38 | Oslo Gardermoen Airport |  | NO | 1344 |
| 39 | Vancouver International Airport |  | CA | 1314 |
| 40 | O. R. Tambo International Airport |  | ZA | 1312 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1090 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 880 | 21m | 244 km | 3,705.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 612 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 609 | 24m | 225 km | 2,362.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 607 | 1h 6m | 770 km | 8,063.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 541 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 396 | 27m | 275 km | 1,876.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 375 | 1h 50m | 1,423 km | 9,203.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 365 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 361 | 44m | 555 km | 3,456.7 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 346 | 44m | 241 km | 1,437.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 324 | 24m | 218 km | 1,220.6 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 319 | 22m | 55 km | 303.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 318 | 1h 40m | 1,156 km | 6,344.0 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 297 | 19m | 99 km | 508.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 292 | 27m | 215 km | 1,081.4 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 277 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 270 | 19m | 144 km | 671.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 256 | 1h 50m | 1,304 km | 5,759.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N267FG |  | Trenton Mercer Airport (KTTN) | Solberg/Hunterdon Airport (KN51) | 2026-08-26 17:05 UTC | 2026-08-26 18:01 UTC | 55m |
| N8380C |  | 16PA (16PA) | Rostraver Airport (KFWQ) | 2026-08-26 17:31 UTC | 2026-08-26 17:54 UTC | 23m |
| N8116B |  | Lake In The Hills Airport (K3CK) | Lake In The Hills Airport (K3CK) | 2026-08-26 17:33 UTC | 2026-08-26 17:54 UTC | 20m |
| N305DG |  | Brown Field Municipal Airport (KSDM) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-26 17:06 UTC | 2026-08-26 17:53 UTC | 47m |
| N700JV |  | Chartres Champhol Airport (LFOR) | Lyon-Bron Airport (LFLY) | 2026-08-26 16:48 UTC | 2026-08-26 17:49 UTC | 1h 0m |
| CPA040 | Cathay Pacific | Juhu Aerodrome (VAJJ) | Zhuhai Airport (ZGSD) | 2026-08-26 12:47 UTC | 2026-08-26 17:49 UTC | 5h 1m |
| ACA1100 | Air Canada | Vancouver International Airport (CYVR) | Regina International Airport (CYQR) | 2026-08-26 16:01 UTC | 2026-08-26 17:46 UTC | 1h 45m |
| EXS2 | EXS | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-26 17:12 UTC | 2026-08-26 17:42 UTC | 30m |
| STAB11 | STA | Enid Woodring Regional Airport (KWDG) | Ramey 1 Airport (0OK8) | 2026-08-26 17:16 UTC | 2026-08-26 17:40 UTC | 24m |
|  |  | Montréal (Mirabel) Airport (CYMX) | Montréal (Mirabel) Airport (CYMX) | 2026-08-26 17:29 UTC | 2026-08-26 17:40 UTC | 10m |
| N24AM |  | Sky Ranch At Carefree Airport (18AZ) | Pleasant Valley Airstrip (24AZ) | 2026-08-26 17:12 UTC | 2026-08-26 17:37 UTC | 24m |
| N280U |  | Ohio University Airport (KUNI) | Ohio University Airport (KUNI) | 2026-08-26 17:31 UTC | 2026-08-26 17:35 UTC | 3m |
| RNGR765 | RNG | Green Lake Ranch Airport (69TX) | San Jose Island Airport (XS67) | 2026-08-26 17:15 UTC | 2026-08-26 17:35 UTC | 19m |
| N945FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-08-26 17:00 UTC | 2026-08-26 17:34 UTC | 34m |
| N225WS |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-08-26 16:57 UTC | 2026-08-26 17:30 UTC | 32m |
| DEMFZ | DEM | Frankfurt-Egelsbach Airport (EDFE) | Frankfurt-Egelsbach Airport (EDFE) | 2026-08-26 16:33 UTC | 2026-08-26 17:27 UTC | 54m |
| XSN25 | XSN | Gooding Municipal Airport (KGNG) | Tracy Municipal Airport (KTCY) | 2026-08-26 15:34 UTC | 2026-08-26 17:27 UTC | 1h 52m |
| N18TF |  | 92MI (92MI) | 84MI (84MI) | 2026-08-26 17:09 UTC | 2026-08-26 17:26 UTC | 17m |
| N907KW |  | Healy River Airport (PAHV) | Nugget Bench Airport (33AK) | 2026-08-26 16:34 UTC | 2026-08-26 17:26 UTC | 51m |
| RYR687J | Ryanair | Niederrhein Airport (EDLV) | Palma De Mallorca Airport (LEPA) | 2026-08-26 15:14 UTC | 2026-08-26 17:26 UTC | 2h 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
