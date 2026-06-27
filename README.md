# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_23:52:38_UTC-green)

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

**Latest saved flight:** 2026-06-26 23:52:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-26 23:52:38 UTC

- **121,787** saved flights
- **41,822** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **121,787** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,472,720.9 tonnes** estimated CO2 emissions
- **85,375,124 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4983 |
| 2 | SkyWest Airlines | 4512 |
| 3 | EJA | 2361 |
| 4 | IndiGo | 2324 |
| 5 | American Airlines | 1887 |
| 6 | Southwest Airlines | 1829 |
| 7 | ENY | 1519 |
| 8 | Delta Air Lines | 1443 |
| 9 | Lufthansa | 1321 |
| 10 | LATAM Airlines | 1085 |
| 11 | Vueling | 1085 |
| 12 | WIF | 1076 |
| 13 | AZU | 1023 |
| 14 | AXM | 983 |
| 15 | LXJ | 927 |
| 16 | Swiss International | 848 |
| 17 | All Nippon Airways | 825 |
| 18 | Alaska Airlines | 802 |
| 19 | easyJet | 784 |
| 20 | QLK | 775 |
| 21 | EJU | 764 |
| 22 | Cathay Pacific | 685 |
| 23 | AEE | 672 |
| 24 | Air France | 666 |
| 25 | VIV | 665 |
| 26 | United Airlines | 659 |
| 27 | CXK | 649 |
| 28 | MXY | 637 |
| 29 | JetBlue | 608 |
| 30 | AXB | 603 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 103563 |
| 2 | 🇪🇸 ES | 8224 |
| 3 | 🇮🇳 IN | 7307 |
| 4 | 🇦🇺 AU | 7131 |
| 5 | 🇧🇷 BR | 6718 |
| 6 | 🇩🇪 DE | 6478 |
| 7 | 🇮🇹 IT | 6465 |
| 8 | 🇨🇦 CA | 6419 |
| 9 | 🇯🇵 JP | 5391 |
| 10 | 🇬🇧 GB | 5347 |
| 11 | 🇫🇷 FR | 4824 |
| 12 | 🇨🇴 CO | 4024 |
| 13 | 🇲🇽 MX | 3550 |
| 14 | 🇬🇷 GR | 3468 |
| 15 | 🇳🇴 NO | 3352 |
| 16 | 🇨🇭 CH | 3122 |
| 17 | 🇲🇾 MY | 2549 |
| 18 | 🇹🇷 TR | 2519 |
| 19 | 🇿🇦 ZA | 2027 |
| 20 | 🇵🇱 PL | 1996 |
| 21 | 🇳🇿 NZ | 1970 |
| 22 | 🇰🇷 KR | 1924 |
| 23 | 🇹🇭 TH | 1921 |
| 24 | 🇵🇭 PH | 1746 |
| 25 | 🇬🇹 GT | 1692 |
| 26 | 🇲🇦 MA | 1307 |
| 27 | 🇲🇪 ME | 1212 |
| 28 | 🇲🇴 MO | 1176 |
| 29 | 🇳🇱 NL | 1160 |
| 30 | 🇭🇷 HR | 1052 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2559 |
| 2 | Denver International Airport |  | US | 2052 |
| 3 | Tokyo International Airport |  | JP | 1784 |
| 4 | Indira Gandhi International Airport |  | IN | 1610 |
| 5 | Harry Reid International Airport |  | US | 1524 |
| 6 | Guaymaral Airport |  | CO | 1514 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1469 |
| 8 | Zurich Airport |  | CH | 1346 |
| 9 | La Aurora Airport |  | GT | 1307 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1299 |
| 11 | Frankfurt am Main International Airport |  | DE | 1276 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1198 |
| 13 | Chicago O'Hare International Airport |  | US | 1184 |
| 14 | Macau International Airport |  | MO | 1176 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1061 |
| 17 | Capua Airport |  | IT | 1040 |
| 18 | Madrid Barajas International Airport |  | ES | 1019 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1015 |
| 20 | Kuala Lumpur International Airport |  | MY | 988 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 960 |
| 22 | Congonhas Airport |  | BR | 944 |
| 23 | Charlotte/Douglas International Airport |  | US | 919 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 901 |
| 25 | Charles de Gaulle International Airport |  | FR | 892 |
| 26 | Bengaluru International Airport |  | IN | 877 |
| 27 | Malpensa International Airport |  | IT | 848 |
| 28 | Ninoy Aquino International Airport |  | PH | 809 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 791 |
| 30 | Daniel K Inouye International Airport |  | US | 784 |
| 31 | Barcelona International Airport |  | ES | 764 |
| 32 | Tenerife Norte Airport |  | ES | 762 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 748 |
| 34 | Calgary International Airport |  | CA | 714 |
| 35 | Vitoria/Foronda Airport |  | ES | 708 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 705 |
| 37 | Scottsdale Airport |  | US | 703 |
| 38 | Amsterdam Airport Schiphol |  | NL | 702 |
| 39 | Seattle-Tacoma International Airport |  | US | 700 |
| 40 | Don Mueang International Airport |  | TH | 694 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 631 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 444 | 21m | 244 km | 1,869.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 319 | 24m | 225 km | 1,237.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 309 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 293 | 1h 10m | 770 km | 3,892.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 292 | 1h 25m | 910 km | 4,582.2 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 239 | 26m | 275 km | 1,132.5 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 225 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 175 | 26m | 215 km | 648.1 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 174 | 20m | 99 km | 298.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 166 | 44m | 241 km | 689.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 165 | 27m | 152 km | 431.2 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 158 | 31m | 369 km | 1,005.7 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 154 | 44m | 452 km | 1,200.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 153 | 1h 44m | 1,423 km | 3,754.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 152 | 18m | 144 km | 378.1 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 142 | 1h 38m | 1,156 km | 2,832.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 141 | 1h 1m | 695 km | 1,690.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 138 | 1h 17m | 961 km | 2,287.4 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 137 | 29m | 49 km | 115.8 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 137 | 13m | - | - |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-06-26 23:35 UTC | 2026-06-26 23:52 UTC | 17m |
| N909SB |  | Santa Barbara Municipal Airport (KSBA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-06-26 23:27 UTC | 2026-06-26 23:51 UTC | 23m |
| AUB1350 | AUB | Auburn University Regional Airport (KAUO) | Auburn University Regional Airport (KAUO) | 2026-06-26 23:14 UTC | 2026-06-26 23:50 UTC | 35m |
| CJT3193 | CJT | Montréal (Mirabel) Airport (CYMX) | Phoenix Sky Harbor International Airport (KPHX) | 2026-06-26 18:24 UTC | 2026-06-26 23:41 UTC | 5h 17m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-06-26 23:23 UTC | 2026-06-26 23:40 UTC | 17m |
| N72NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-06-26 23:10 UTC | 2026-06-26 23:39 UTC | 28m |
| DCM6432 | DCM | Huntsville Executive Tom Sharp Jr Field (KMDQ) | Auburn University Regional Airport (KAUO) | 2026-06-26 22:57 UTC | 2026-06-26 23:38 UTC | 40m |
| MXY229 | MXY | San Francisco International Airport (KSFO) | 95IN (95IN) | 2026-06-26 19:41 UTC | 2026-06-26 23:37 UTC | 3h 56m |
| N714WP |  | Denton Enterprise Airport (KDTO) | Gainesville Municipal Airport (KGLE) | 2026-06-26 22:44 UTC | 2026-06-26 23:33 UTC | 49m |
| PPSCF | PPS | Pinto Martins International Airport (SBFZ) | SWBE (SWBE) | 2026-06-26 23:07 UTC | 2026-06-26 23:30 UTC | 22m |
| N20745 |  | Van Wert County Airport (KVNW) | Hamrick Airport (5OI5) | 2026-06-26 23:02 UTC | 2026-06-26 23:29 UTC | 26m |
| N615AJ |  | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | Palm Springs International Airport (KPSP) | 2026-06-26 22:52 UTC | 2026-06-26 23:28 UTC | 36m |
| N26WR |  | Santa Ynez/Kunkle Field (KIZA) | Santa Monica Municipal Airport (KSMO) | 2026-06-26 23:04 UTC | 2026-06-26 23:27 UTC | 23m |
| N202WG |  | Warrenton/Fauquier Airport (KHWY) | Aviacres Airport (3VA2) | 2026-06-26 23:20 UTC | 2026-06-26 23:26 UTC | 6m |
| NSH301 | NSH | Eppley Airfield (KOMA) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-06-26 21:21 UTC | 2026-06-26 23:25 UTC | 2h 3m |
| N86BJ |  | Denton Enterprise Airport (KDTO) | Teate Field (4XS2) | 2026-06-26 22:36 UTC | 2026-06-26 23:22 UTC | 46m |
| N779AZ |  | Frederick W Smith International Airport (KMEM) | Rocky Mountain Metro Airport (KBJC) | 2026-06-26 21:08 UTC | 2026-06-26 23:19 UTC | 2h 10m |
| TKR168 | TKR | Grand Junction Regional Airport (KGJT) | 01UT (01UT) | 2026-06-26 23:02 UTC | 2026-06-26 23:17 UTC | 15m |
| BOE452 | BOE | Boeing Field/King County International Airport (KBFI) | Othello Municipal Airport (KS70) | 2026-06-26 22:02 UTC | 2026-06-26 23:17 UTC | 1h 15m |
| XAFSB | XAF | General Mariano Escobedo International Airport (MMMY) | Rancho Guadalupe South Airport (MM51) | 2026-06-26 22:49 UTC | 2026-06-26 23:14 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
