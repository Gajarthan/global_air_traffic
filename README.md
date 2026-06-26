# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_14:27:48_UTC-green)

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

**Latest saved flight:** 2026-06-26 14:27:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-26 14:27:48 UTC

- **121,010** saved flights
- **41,570** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **121,010** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,462,745.6 tonnes** estimated CO2 emissions
- **84,796,847 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4967 |
| 2 | SkyWest Airlines | 4467 |
| 3 | EJA | 2336 |
| 4 | IndiGo | 2323 |
| 5 | American Airlines | 1873 |
| 6 | Southwest Airlines | 1803 |
| 7 | ENY | 1509 |
| 8 | Delta Air Lines | 1428 |
| 9 | Lufthansa | 1319 |
| 10 | Vueling | 1083 |
| 11 | LATAM Airlines | 1075 |
| 12 | WIF | 1072 |
| 13 | AZU | 1011 |
| 14 | AXM | 983 |
| 15 | LXJ | 919 |
| 16 | Swiss International | 846 |
| 17 | All Nippon Airways | 825 |
| 18 | Alaska Airlines | 797 |
| 19 | easyJet | 779 |
| 20 | QLK | 774 |
| 21 | EJU | 760 |
| 22 | Cathay Pacific | 678 |
| 23 | AEE | 672 |
| 24 | Air France | 664 |
| 25 | VIV | 662 |
| 26 | United Airlines | 659 |
| 27 | CXK | 649 |
| 28 | MXY | 635 |
| 29 | JetBlue | 602 |
| 30 | AXB | 601 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 102584 |
| 2 | 🇪🇸 ES | 8200 |
| 3 | 🇮🇳 IN | 7299 |
| 4 | 🇦🇺 AU | 7126 |
| 5 | 🇧🇷 BR | 6663 |
| 6 | 🇩🇪 DE | 6456 |
| 7 | 🇮🇹 IT | 6442 |
| 8 | 🇨🇦 CA | 6348 |
| 9 | 🇯🇵 JP | 5389 |
| 10 | 🇬🇧 GB | 5316 |
| 11 | 🇫🇷 FR | 4809 |
| 12 | 🇨🇴 CO | 4020 |
| 13 | 🇲🇽 MX | 3525 |
| 14 | 🇬🇷 GR | 3460 |
| 15 | 🇳🇴 NO | 3341 |
| 16 | 🇨🇭 CH | 3111 |
| 17 | 🇲🇾 MY | 2548 |
| 18 | 🇹🇷 TR | 2497 |
| 19 | 🇿🇦 ZA | 2023 |
| 20 | 🇵🇱 PL | 1991 |
| 21 | 🇳🇿 NZ | 1960 |
| 22 | 🇹🇭 TH | 1921 |
| 23 | 🇰🇷 KR | 1917 |
| 24 | 🇵🇭 PH | 1740 |
| 25 | 🇬🇹 GT | 1680 |
| 26 | 🇲🇦 MA | 1304 |
| 27 | 🇲🇪 ME | 1210 |
| 28 | 🇲🇴 MO | 1174 |
| 29 | 🇳🇱 NL | 1151 |
| 30 | 🇭🇷 HR | 1050 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2538 |
| 2 | Denver International Airport |  | US | 2035 |
| 3 | Tokyo International Airport |  | JP | 1784 |
| 4 | Indira Gandhi International Airport |  | IN | 1606 |
| 5 | Guaymaral Airport |  | CO | 1510 |
| 6 | Harry Reid International Airport |  | US | 1505 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1468 |
| 8 | Zurich Airport |  | CH | 1343 |
| 9 | La Aurora Airport |  | GT | 1297 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1283 |
| 11 | Frankfurt am Main International Airport |  | DE | 1273 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1193 |
| 13 | Chicago O'Hare International Airport |  | US | 1178 |
| 14 | Macau International Airport |  | MO | 1174 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1047 |
| 17 | Capua Airport |  | IT | 1035 |
| 18 | Madrid Barajas International Airport |  | ES | 1014 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1006 |
| 20 | Kuala Lumpur International Airport |  | MY | 987 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 944 |
| 22 | Congonhas Airport |  | BR | 934 |
| 23 | Charlotte/Douglas International Airport |  | US | 913 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 900 |
| 25 | Charles de Gaulle International Airport |  | FR | 889 |
| 26 | Bengaluru International Airport |  | IN | 877 |
| 27 | Malpensa International Airport |  | IT | 843 |
| 28 | Ninoy Aquino International Airport |  | PH | 806 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 788 |
| 30 | Daniel K Inouye International Airport |  | US | 778 |
| 31 | Barcelona International Airport |  | ES | 762 |
| 32 | Tenerife Norte Airport |  | ES | 762 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 743 |
| 34 | Calgary International Airport |  | CA | 705 |
| 35 | Vitoria/Foronda Airport |  | ES | 705 |
| 36 | Amsterdam Airport Schiphol |  | NL | 696 |
| 37 | Don Mueang International Airport |  | TH | 694 |
| 38 | Seattle-Tacoma International Airport |  | US | 694 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 693 |
| 40 | Scottsdale Airport |  | US | 688 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 629 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 439 | 21m | 244 km | 1,848.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 318 | 24m | 225 km | 1,233.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 308 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 293 | 1h 10m | 770 km | 3,892.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 292 | 1h 25m | 910 km | 4,582.2 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 238 | 26m | 275 km | 1,127.8 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 225 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 175 | 26m | 215 km | 648.1 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 173 | 20m | 99 km | 296.3 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 166 | 44m | 241 km | 689.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 161 | 27m | 152 km | 420.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 156 | 31m | 369 km | 993.0 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 154 | 44m | 452 km | 1,200.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 151 | 1h 44m | 1,423 km | 3,705.8 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 151 | 18m | 144 km | 375.6 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 141 | 1h 38m | 1,156 km | 2,812.9 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 141 | 1h 1m | 695 km | 1,690.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 137 | 1h 17m | 961 km | 2,270.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK1009 | CXK | Manassas Regional/Harry P Davis Field (KHEF) | Dogwood Airpark (VA42) | 2026-06-26 13:13 UTC | 2026-06-26 14:27 UTC | 1h 14m |
| QTR88E | Qatar Airways | Mikonos Airport (LGMK) | Doha International Airport (OTBD) | 2026-06-26 10:43 UTC | 2026-06-26 14:25 UTC | 3h 42m |
| CPA742 | Cathay Pacific | Gia Lam Air Base (VVGL) | Zhuhai Airport (ZGSD) | 2026-06-26 13:10 UTC | 2026-06-26 14:17 UTC | 1h 7m |
| CXK390 | CXK | Jacksonville Executive At Craig Airport (KCRG) | Stafford Airport (GA20) | 2026-06-26 13:32 UTC | 2026-06-26 14:14 UTC | 42m |
| OXF3571 | OXF | Falcon Field (KFFZ) | Scottsdale Airport (KSDL) | 2026-06-26 13:37 UTC | 2026-06-26 14:12 UTC | 35m |
| N4877J |  | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-06-26 13:43 UTC | 2026-06-26 14:10 UTC | 27m |
| INCVL | INC | Bolzano Airport (LIPB) | Lodrino Air Base (LSML) | 2026-06-26 13:19 UTC | 2026-06-26 14:08 UTC | 48m |
| HBZNH | HBZ | St Stephan Airport (LSTS) | St Stephan Airport (LSTS) | 2026-06-26 13:57 UTC | 2026-06-26 14:08 UTC | 10m |
| N5128N |  | Sunrise Dusters Airport (CA18) | Beale Afb Airport (KBAB) | 2026-06-26 13:15 UTC | 2026-06-26 14:04 UTC | 49m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-06-26 13:46 UTC | 2026-06-26 14:04 UTC | 17m |
| BRW151 | BRW | Flying Cloud Airport (KFCM) | Glencoe Municipal Airport (KGYL) | 2026-06-26 13:33 UTC | 2026-06-26 14:02 UTC | 29m |
| N737EM |  | Albuquerque International Sunport Airport (KABQ) | Ohkay Owingeh Airport (KE14) | 2026-06-26 13:24 UTC | 2026-06-26 14:02 UTC | 38m |
| N353BG |  | Wood County Airport (K1G0) | 72OI (72OI) | 2026-06-26 13:48 UTC | 2026-06-26 14:02 UTC | 13m |
| N4347R |  | Wade Airport (56LL) | Wade Airport (56LL) | 2026-06-26 13:57 UTC | 2026-06-26 13:57 UTC | 0m |
| 2PINK |  | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-06-26 13:52 UTC | 2026-06-26 13:57 UTC | 5m |
| N75600 |  | Phoenix Deer Valley Airport (KDVT) | 42AZ (42AZ) | 2026-06-26 13:27 UTC | 2026-06-26 13:55 UTC | 28m |
| WMT1LH | WMT | Henri Coanda International Airport (LROP) | Craiova Airport (LRCV) | 2026-06-26 13:36 UTC | 2026-06-26 13:53 UTC | 16m |
| RYR46CZ | Ryanair | Sofia Airport (LBSF) | Trstenik Airport (LYTR) | 2026-06-26 13:34 UTC | 2026-06-26 13:53 UTC | 18m |
| GPX6CU | GPX | Munich International Airport (EDDM) | Cemovsko Polje Airport (LYPO) | 2026-06-26 12:46 UTC | 2026-06-26 13:52 UTC | 1h 6m |
| BRW1 | BRW | Flying Cloud Airport (KFCM) | Glencoe Municipal Airport (KGYL) | 2026-06-26 13:13 UTC | 2026-06-26 13:52 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
