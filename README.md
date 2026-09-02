# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_13:32:42_UTC-green)

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

**Latest saved flight:** 2026-09-02 13:32:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-02 13:32:42 UTC

- **244,683** saved flights
- **74,021** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **244,683** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,949,045.9 tonnes** estimated CO2 emissions
- **170,959,182 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9816 |
| 2 | SkyWest Airlines | 8566 |
| 3 | EJA | 4721 |
| 4 | IndiGo | 4103 |
| 5 | American Airlines | 3930 |
| 6 | Southwest Airlines | 3665 |
| 7 | Delta Air Lines | 3112 |
| 8 | ENY | 2939 |
| 9 | LATAM Airlines | 2351 |
| 10 | AZU | 2273 |
| 11 | Vueling | 2097 |
| 12 | Lufthansa | 1960 |
| 13 | WIF | 1954 |
| 14 | LXJ | 1887 |
| 15 | easyJet | 1703 |
| 16 | Swiss International | 1651 |
| 17 | AXM | 1613 |
| 18 | EJU | 1577 |
| 19 | QLK | 1566 |
| 20 | United Airlines | 1539 |
| 21 | Alaska Airlines | 1462 |
| 22 | All Nippon Airways | 1443 |
| 23 | WMT | 1381 |
| 24 | GLO | 1367 |
| 25 | PGT | 1339 |
| 26 | Air France | 1337 |
| 27 | VIV | 1337 |
| 28 | Wizz Air | 1327 |
| 29 | AEE | 1208 |
| 30 | JetBlue | 1206 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 202603 |
| 2 | 🇪🇸 ES | 15724 |
| 3 | 🇧🇷 BR | 14265 |
| 4 | 🇦🇺 AU | 13915 |
| 5 | 🇨🇦 CA | 13609 |
| 6 | 🇮🇹 IT | 13422 |
| 7 | 🇮🇳 IN | 12790 |
| 8 | 🇩🇪 DE | 12077 |
| 9 | 🇬🇧 GB | 11546 |
| 10 | 🇨🇴 CO | 10604 |
| 11 | 🇫🇷 FR | 9882 |
| 12 | 🇯🇵 JP | 9751 |
| 13 | 🇹🇷 TR | 7277 |
| 14 | 🇬🇷 GR | 7221 |
| 15 | 🇲🇽 MX | 6735 |
| 16 | 🇨🇭 CH | 6582 |
| 17 | 🇳🇴 NO | 6069 |
| 18 | 🇹🇭 TH | 4429 |
| 19 | 🇲🇾 MY | 4324 |
| 20 | 🇿🇦 ZA | 4253 |
| 21 | 🇵🇱 PL | 4113 |
| 22 | 🇳🇿 NZ | 3360 |
| 23 | 🇵🇭 PH | 3352 |
| 24 | 🇬🇹 GT | 3070 |
| 25 | 🇰🇷 KR | 2870 |
| 26 | 🇭🇷 HR | 2819 |
| 27 | 🇲🇦 MA | 2474 |
| 28 | 🇲🇪 ME | 2287 |
| 29 | 🇳🇱 NL | 2217 |
| 30 | 🇮🇩 ID | 2137 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5038 |
| 2 | Denver International Airport |  | US | 3939 |
| 3 | Indira Gandhi International Airport |  | IN | 2983 |
| 4 | Tokyo International Airport |  | JP | 2906 |
| 5 | Guaymaral Airport |  | CO | 2714 |
| 6 | Harry Reid International Airport |  | US | 2604 |
| 7 | Zurich Airport |  | CH | 2572 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2490 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2438 |
| 10 | El Dorado International Airport |  | CO | 2413 |
| 11 | La Aurora Airport |  | GT | 2335 |
| 12 | Salt Lake City International Airport |  | US | 2165 |
| 13 | Chicago O'Hare International Airport |  | US | 2161 |
| 14 | Congonhas Airport |  | BR | 2088 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2024 |
| 16 | Frankfurt am Main International Airport |  | DE | 1930 |
| 17 | Capua Airport |  | IT | 1927 |
| 18 | Madrid Barajas International Airport |  | ES | 1923 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1842 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1799 |
| 21 | Malpensa International Airport |  | IT | 1751 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1721 |
| 23 | Charles de Gaulle International Airport |  | FR | 1721 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1714 |
| 25 | Ninoy Aquino International Airport |  | PH | 1632 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1574 |
| 28 | Charlotte/Douglas International Airport |  | US | 1560 |
| 29 | Kuala Lumpur International Airport |  | MY | 1558 |
| 30 | Barcelona International Airport |  | ES | 1551 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1477 |
| 32 | Viracopos International Airport |  | BR | 1453 |
| 33 | Seattle-Tacoma International Airport |  | US | 1432 |
| 34 | Don Mueang International Airport |  | TH | 1424 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1418 |
| 36 | Bengaluru International Airport |  | IN | 1416 |
| 37 | Calgary International Airport |  | CA | 1408 |
| 38 | Oslo Gardermoen Airport |  | NO | 1381 |
| 39 | Vancouver International Airport |  | CA | 1364 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1339 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1099 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 904 | 21m | 244 km | 3,806.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 634 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 623 | 24m | 225 km | 2,416.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 615 | 1h 6m | 770 km | 8,169.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 549 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 403 | 27m | 275 km | 1,909.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 387 | 1h 50m | 1,423 km | 9,497.6 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 376 | 44m | 555 km | 3,600.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 361 | 44m | 241 km | 1,499.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 347 | 21m | 250 km | 1,498.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 335 | 24m | 218 km | 1,262.1 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 327 | 1h 39m | 1,156 km | 6,523.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 325 | 22m | 55 km | 308.9 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 303 | 19m | 99 km | 519.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 299 | 26m | 215 km | 1,107.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 289 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 283 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 281 | 1h 14m | 961 km | 4,657.7 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 277 | 19m | 144 km | 689.0 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 262 | 1h 50m | 1,304 km | 5,894.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N63LU |  | Marana Regional Airport (KAVQ) | Marana Regional Airport (KAVQ) | 2026-09-02 13:14 UTC | 2026-09-02 13:32 UTC | 18m |
| N229FG |  | Raleigh-Durham International Airport (KRDU) | Triangle North Executive Airport (KLHZ) | 2026-09-02 12:52 UTC | 2026-09-02 13:31 UTC | 39m |
| N945TC |  | Dothan Regional Airport (KDHN) | Geneva Municipal Airport (K33J) | 2026-09-02 13:04 UTC | 2026-09-02 13:28 UTC | 24m |
| PGT264P | PGT | Stockholm-Arlanda Airport (ESSA) | Samandira Air Base (LTBX) | 2026-09-02 10:35 UTC | 2026-09-02 13:28 UTC | 2h 52m |
| EIN93T | Aer Lingus | Faro Airport (LPFR) | Dublin Airport (EIDW) | 2026-09-02 10:59 UTC | 2026-09-02 13:28 UTC | 2h 29m |
| IBIS1 | IBI | Frankfurt-Egelsbach Airport (EDFE) | Mainz-Finthen Airport (EDFZ) | 2026-09-02 12:02 UTC | 2026-09-02 13:27 UTC | 1h 24m |
| LEONE04 | LEO | Pratica Di Mare Airport (LIRE) | Pratica Di Mare Airport (LIRE) | 2026-09-02 12:45 UTC | 2026-09-02 13:25 UTC | 40m |
| PRE54 | PRE | Dallas Executive Airport (KRBD) | Garden County/King Rhiley Field (KOKS) | 2026-09-02 11:35 UTC | 2026-09-02 13:20 UTC | 1h 45m |
| MGMKM | MGM | Karlsruhe Baden-Baden Airport (EDSB) | Stuttgart Airport (EDDS) | 2026-09-02 12:52 UTC | 2026-09-02 13:12 UTC | 20m |
| CFHXU | CFH | Calgary International Airport (CYYC) | Calgary International Airport (CYYC) | 2026-09-02 12:59 UTC | 2026-09-02 13:10 UTC | 10m |
| N261NX |  | 11TX (11TX) | Mid-Way Regional Airport (KJWY) | 2026-09-02 12:45 UTC | 2026-09-02 13:08 UTC | 23m |
| N4632F |  | Rocky Mountain Metro Airport (KBJC) | Laramie Regional Airport (KLAR) | 2026-09-02 12:12 UTC | 2026-09-02 13:04 UTC | 51m |
| N529LF |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-09-02 12:27 UTC | 2026-09-02 13:01 UTC | 34m |
| ANA868 | All Nippon Airways | Gimpo International Airport (RKSS) | Tokyo International Airport (RJTT) | 2026-09-02 11:12 UTC | 2026-09-02 12:59 UTC | 1h 47m |
| DENTS62 | DEN | Enterprise Municipal Airport (KEDN) | Weedon Field (KEUF) | 2026-09-02 12:00 UTC | 2026-09-02 12:58 UTC | 58m |
| IGO7603 | IndiGo | Hosur Airport (VO95) | Mysore Airport (VOMY) | 2026-09-02 10:36 UTC | 2026-09-02 12:54 UTC | 2h 17m |
| WIF8GH | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-09-02 12:23 UTC | 2026-09-02 12:52 UTC | 28m |
|  |  | Rzeszow-Jasionka Airport (EPRZ) | Rzeszow-Jasionka Airport (EPRZ) | 2026-09-02 12:51 UTC | 2026-09-02 12:51 UTC | 0m |
| AFR34MZ | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-09-02 12:04 UTC | 2026-09-02 12:51 UTC | 47m |
| CAN14 | CAN | Pescara International Airport (LIBP) | Pescara International Airport (LIBP) | 2026-09-02 12:37 UTC | 2026-09-02 12:48 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
