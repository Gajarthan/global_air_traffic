# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_19:45:01_UTC-green)

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

**Latest saved flight:** 2026-09-02 19:45:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-02 19:45:01 UTC

- **245,123** saved flights
- **74,102** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **245,123** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,952,946.2 tonnes** estimated CO2 emissions
- **171,185,288 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9839 |
| 2 | SkyWest Airlines | 8577 |
| 3 | EJA | 4730 |
| 4 | IndiGo | 4104 |
| 5 | American Airlines | 3938 |
| 6 | Southwest Airlines | 3671 |
| 7 | Delta Air Lines | 3117 |
| 8 | ENY | 2941 |
| 9 | LATAM Airlines | 2354 |
| 10 | AZU | 2279 |
| 11 | Vueling | 2100 |
| 12 | Lufthansa | 1962 |
| 13 | WIF | 1961 |
| 14 | LXJ | 1894 |
| 15 | easyJet | 1705 |
| 16 | Swiss International | 1654 |
| 17 | AXM | 1613 |
| 18 | EJU | 1580 |
| 19 | QLK | 1566 |
| 20 | United Airlines | 1546 |
| 21 | Alaska Airlines | 1463 |
| 22 | All Nippon Airways | 1443 |
| 23 | WMT | 1383 |
| 24 | GLO | 1368 |
| 25 | PGT | 1343 |
| 26 | Air France | 1342 |
| 27 | VIV | 1340 |
| 28 | Wizz Air | 1328 |
| 29 | AEE | 1210 |
| 30 | JetBlue | 1209 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 203044 |
| 2 | 🇪🇸 ES | 15748 |
| 3 | 🇧🇷 BR | 14290 |
| 4 | 🇦🇺 AU | 13917 |
| 5 | 🇨🇦 CA | 13645 |
| 6 | 🇮🇹 IT | 13447 |
| 7 | 🇮🇳 IN | 12796 |
| 8 | 🇩🇪 DE | 12098 |
| 9 | 🇬🇧 GB | 11562 |
| 10 | 🇨🇴 CO | 10631 |
| 11 | 🇫🇷 FR | 9901 |
| 12 | 🇯🇵 JP | 9751 |
| 13 | 🇹🇷 TR | 7293 |
| 14 | 🇬🇷 GR | 7232 |
| 15 | 🇲🇽 MX | 6753 |
| 16 | 🇨🇭 CH | 6592 |
| 17 | 🇳🇴 NO | 6088 |
| 18 | 🇹🇭 TH | 4429 |
| 19 | 🇲🇾 MY | 4324 |
| 20 | 🇿🇦 ZA | 4259 |
| 21 | 🇵🇱 PL | 4116 |
| 22 | 🇳🇿 NZ | 3360 |
| 23 | 🇵🇭 PH | 3352 |
| 24 | 🇬🇹 GT | 3073 |
| 25 | 🇰🇷 KR | 2870 |
| 26 | 🇭🇷 HR | 2825 |
| 27 | 🇲🇦 MA | 2478 |
| 28 | 🇲🇪 ME | 2294 |
| 29 | 🇳🇱 NL | 2220 |
| 30 | 🇮🇩 ID | 2137 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5049 |
| 2 | Denver International Airport |  | US | 3951 |
| 3 | Indira Gandhi International Airport |  | IN | 2985 |
| 4 | Tokyo International Airport |  | JP | 2906 |
| 5 | Guaymaral Airport |  | CO | 2718 |
| 6 | Harry Reid International Airport |  | US | 2610 |
| 7 | Zurich Airport |  | CH | 2577 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2495 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2441 |
| 10 | El Dorado International Airport |  | CO | 2421 |
| 11 | La Aurora Airport |  | GT | 2338 |
| 12 | Salt Lake City International Airport |  | US | 2169 |
| 13 | Chicago O'Hare International Airport |  | US | 2163 |
| 14 | Congonhas Airport |  | BR | 2093 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2024 |
| 16 | Frankfurt am Main International Airport |  | DE | 1933 |
| 17 | Capua Airport |  | IT | 1929 |
| 18 | Madrid Barajas International Airport |  | ES | 1927 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1843 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1801 |
| 21 | Malpensa International Airport |  | IT | 1756 |
| 22 | Charles de Gaulle International Airport |  | FR | 1726 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 1724 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1714 |
| 25 | Ninoy Aquino International Airport |  | PH | 1632 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1582 |
| 28 | Charlotte/Douglas International Airport |  | US | 1563 |
| 29 | Kuala Lumpur International Airport |  | MY | 1558 |
| 30 | Barcelona International Airport |  | ES | 1552 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1484 |
| 32 | Viracopos International Airport |  | BR | 1455 |
| 33 | Seattle-Tacoma International Airport |  | US | 1436 |
| 34 | Don Mueang International Airport |  | TH | 1424 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1420 |
| 36 | Bengaluru International Airport |  | IN | 1416 |
| 37 | Calgary International Airport |  | CA | 1411 |
| 38 | Oslo Gardermoen Airport |  | NO | 1383 |
| 39 | Vancouver International Airport |  | CA | 1365 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1341 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 906 | 21m | 244 km | 3,814.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 637 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 623 | 24m | 225 km | 2,416.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 615 | 1h 6m | 770 km | 8,169.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 550 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 405 | 27m | 275 km | 1,919.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 387 | 1h 50m | 1,423 km | 9,497.6 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 376 | 44m | 555 km | 3,600.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 361 | 44m | 241 km | 1,499.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 348 | 21m | 250 km | 1,503.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 337 | 24m | 218 km | 1,269.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 328 | 1h 39m | 1,156 km | 6,543.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 325 | 22m | 55 km | 308.9 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 303 | 19m | 99 km | 519.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 300 | 27m | 215 km | 1,111.1 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 289 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 284 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 282 | 1h 14m | 961 km | 4,674.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 278 | 19m | 144 km | 691.5 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 263 | 1h 50m | 1,304 km | 5,916.8 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 252 | 28m | 152 km | 658.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N301CH |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-09-02 19:28 UTC | 2026-09-02 19:45 UTC | 16m |
| WIRE31 | WIR | Enix Airport (OK51) | Enix Airport (OK51) | 2026-09-02 18:59 UTC | 2026-09-02 19:35 UTC | 36m |
| LY729 |  | Spencer Nolf Airport (KNRQ) | Spencer Nolf Airport (KNRQ) | 2026-09-02 19:18 UTC | 2026-09-02 19:31 UTC | 12m |
| SMGLR31 | SMG | Pardubice Airport (LKPD) | Pardubice Airport (LKPD) | 2026-09-02 19:06 UTC | 2026-09-02 19:28 UTC | 21m |
| N480E |  | Mid-Way Regional Airport (KJWY) | Mid-Way Regional Airport (KJWY) | 2026-09-02 19:24 UTC | 2026-09-02 19:27 UTC | 3m |
| N200NW |  | St Cloud Sky Central Airport (KSTC) | St Cloud Sky Central Airport (KSTC) | 2026-09-02 19:24 UTC | 2026-09-02 19:27 UTC | 2m |
| N551PG |  | Gillespie County Airport (KT82) | Fall Creek Ranch Airport (XA43) | 2026-09-02 18:54 UTC | 2026-09-02 19:26 UTC | 31m |
| N420XE |  | Greenville Downtown Airport (KGMU) | MS28 (MS28) | 2026-09-02 18:08 UTC | 2026-09-02 19:24 UTC | 1h 16m |
| N715SJ |  | Ted Stevens Anchorage International Airport (PANC) | Sparrevohn Lrrs Airport (PASV) | 2026-09-02 18:40 UTC | 2026-09-02 19:24 UTC | 43m |
| PGT39EA | PGT | Trabzon International Airport (LTCG) | Yalova Airport (LTBP) | 2026-09-02 18:08 UTC | 2026-09-02 19:24 UTC | 1h 15m |
| N1308T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-09-02 18:13 UTC | 2026-09-02 19:23 UTC | 1h 9m |
|  |  | Toulouse-Blagnac Airport (LFBO) | Toulouse-Blagnac Airport (LFBO) | 2026-09-02 18:59 UTC | 2026-09-02 19:22 UTC | 23m |
| N218BJ |  | Montgomery-Gibbs Executive Airport (KMYF) | Santa Monica Municipal Airport (KSMO) | 2026-09-02 18:32 UTC | 2026-09-02 19:21 UTC | 48m |
| HAWK286 | HAW | Kingsville Nas Airport (KNQI) | Seven C's Ranch Airport (0XA4) | 2026-09-02 18:56 UTC | 2026-09-02 19:20 UTC | 24m |
| XBMFB | XBM | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-09-02 18:38 UTC | 2026-09-02 19:20 UTC | 41m |
| N958MG |  | Dubuque Regional Airport (KDBQ) | 8II3 (8II3) | 2026-09-02 18:28 UTC | 2026-09-02 19:20 UTC | 51m |
| N117AA |  | Nine Mile Airport (MT52) | Boeing Field/King County International Airport (KBFI) | 2026-09-02 18:20 UTC | 2026-09-02 19:15 UTC | 55m |
| MSR706 | EgyptAir | Malpensa International Airport (LIMC) | HE12 (HE12) | 2026-09-02 16:07 UTC | 2026-09-02 19:10 UTC | 3h 2m |
| N172BF |  | Lewis University Airport (KLOT) | Lewis University Airport (KLOT) | 2026-09-02 19:01 UTC | 2026-09-02 19:10 UTC | 8m |
| WSN2 | WSN | Albuquerque International Sunport Airport (KABQ) | Casas Adobes Airpark (NM69) | 2026-09-02 18:28 UTC | 2026-09-02 19:08 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
