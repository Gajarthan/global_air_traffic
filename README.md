# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_11:18:52_UTC-green)

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

**Latest saved flight:** 2026-06-29 11:18:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-29 11:18:52 UTC

- **123,800** saved flights
- **42,428** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **123,800** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,496,992.2 tonnes** estimated CO2 emissions
- **86,782,154 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5058 |
| 2 | SkyWest Airlines | 4580 |
| 3 | EJA | 2418 |
| 4 | IndiGo | 2363 |
| 5 | American Airlines | 1913 |
| 6 | Southwest Airlines | 1855 |
| 7 | ENY | 1554 |
| 8 | Delta Air Lines | 1471 |
| 9 | Lufthansa | 1332 |
| 10 | LATAM Airlines | 1114 |
| 11 | Vueling | 1102 |
| 12 | WIF | 1096 |
| 13 | AZU | 1041 |
| 14 | AXM | 990 |
| 15 | LXJ | 960 |
| 16 | Swiss International | 873 |
| 17 | All Nippon Airways | 836 |
| 18 | Alaska Airlines | 812 |
| 19 | easyJet | 791 |
| 20 | QLK | 779 |
| 21 | EJU | 775 |
| 22 | Cathay Pacific | 693 |
| 23 | AEE | 683 |
| 24 | Air France | 675 |
| 25 | VIV | 674 |
| 26 | United Airlines | 662 |
| 27 | CXK | 654 |
| 28 | MXY | 646 |
| 29 | JetBlue | 627 |
| 30 | GLO | 619 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 105346 |
| 2 | 🇪🇸 ES | 8329 |
| 3 | 🇮🇳 IN | 7412 |
| 4 | 🇦🇺 AU | 7229 |
| 5 | 🇧🇷 BR | 6880 |
| 6 | 🇩🇪 DE | 6594 |
| 7 | 🇮🇹 IT | 6572 |
| 8 | 🇨🇦 CA | 6487 |
| 9 | 🇬🇧 GB | 5464 |
| 10 | 🇯🇵 JP | 5459 |
| 11 | 🇫🇷 FR | 4912 |
| 12 | 🇨🇴 CO | 4031 |
| 13 | 🇲🇽 MX | 3600 |
| 14 | 🇬🇷 GR | 3531 |
| 15 | 🇳🇴 NO | 3410 |
| 16 | 🇨🇭 CH | 3179 |
| 17 | 🇹🇷 TR | 2601 |
| 18 | 🇲🇾 MY | 2563 |
| 19 | 🇿🇦 ZA | 2047 |
| 20 | 🇵🇱 PL | 2033 |
| 21 | 🇳🇿 NZ | 1998 |
| 22 | 🇹🇭 TH | 1939 |
| 23 | 🇰🇷 KR | 1932 |
| 24 | 🇵🇭 PH | 1762 |
| 25 | 🇬🇹 GT | 1710 |
| 26 | 🇲🇦 MA | 1330 |
| 27 | 🇲🇪 ME | 1234 |
| 28 | 🇲🇴 MO | 1177 |
| 29 | 🇳🇱 NL | 1176 |
| 30 | 🇧🇸 BS | 1075 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2603 |
| 2 | Denver International Airport |  | US | 2078 |
| 3 | Tokyo International Airport |  | JP | 1804 |
| 4 | Indira Gandhi International Airport |  | IN | 1633 |
| 5 | Harry Reid International Airport |  | US | 1545 |
| 6 | Guaymaral Airport |  | CO | 1519 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1490 |
| 8 | Zurich Airport |  | CH | 1377 |
| 9 | La Aurora Airport |  | GT | 1321 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1319 |
| 11 | Frankfurt am Main International Airport |  | DE | 1286 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1218 |
| 13 | Chicago O'Hare International Airport |  | US | 1199 |
| 14 | Macau International Airport |  | MO | 1177 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1085 |
| 17 | Capua Airport |  | IT | 1057 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1032 |
| 19 | Madrid Barajas International Airport |  | ES | 1031 |
| 20 | Kuala Lumpur International Airport |  | MY | 996 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 989 |
| 22 | Congonhas Airport |  | BR | 967 |
| 23 | Charlotte/Douglas International Airport |  | US | 934 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 910 |
| 25 | Charles de Gaulle International Airport |  | FR | 904 |
| 26 | Bengaluru International Airport |  | IN | 890 |
| 27 | Malpensa International Airport |  | IT | 857 |
| 28 | Ninoy Aquino International Airport |  | PH | 817 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 816 |
| 30 | Daniel K Inouye International Airport |  | US | 793 |
| 31 | Barcelona International Airport |  | ES | 776 |
| 32 | Tenerife Norte Airport |  | ES | 765 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 754 |
| 34 | Calgary International Airport |  | CA | 726 |
| 35 | Vitoria/Foronda Airport |  | ES | 719 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 718 |
| 37 | Seattle-Tacoma International Airport |  | US | 713 |
| 38 | Amsterdam Airport Schiphol |  | NL | 713 |
| 39 | Scottsdale Airport |  | US | 711 |
| 40 | Don Mueang International Airport |  | TH | 701 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 450 | 21m | 244 km | 1,894.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 322 | 24m | 225 km | 1,249.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 311 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 297 | 1h 10m | 770 km | 3,945.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 297 | 1h 25m | 910 km | 4,660.6 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 242 | 26m | 275 km | 1,146.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 180 | 22m | 55 km | 171.1 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 175 | 20m | 99 km | 299.8 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 173 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 171 | 44m | 241 km | 710.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 168 | 27m | 152 km | 439.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 158 | 1h 44m | 1,423 km | 3,877.6 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 158 | 31m | 369 km | 1,005.7 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 155 | 18m | 144 km | 385.6 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 152 | 20m | 250 km | 656.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 144 | 1h 38m | 1,156 km | 2,872.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 142 | 1h 1m | 695 km | 1,702.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 141 | 1h 17m | 961 km | 2,337.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 139 | 30m | 49 km | 117.5 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 139 | 13m | - | - |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RYR6NH | Ryanair | Ciampino Airport (LIRA) | Kenitra Airport (GMMY) | 2026-06-29 08:56 UTC | 2026-06-29 11:18 UTC | 2h 22m |
| QTR58K | Qatar Airways | Imsik Airport (LTBV) | Queen Alia International Airport (OJAI) | 2026-06-29 10:16 UTC | 2026-06-29 11:16 UTC | 1h 0m |
| GBNEE | GBN | White Waltham Airfield (EGLM) | White Waltham Airfield (EGLM) | 2026-06-29 10:17 UTC | 2026-06-29 11:07 UTC | 50m |
| ISR884 | ISR | Batumi International Airport (UGSB) | Larnaca International Airport (LCLK) | 2026-06-29 09:33 UTC | 2026-06-29 11:02 UTC | 1h 29m |
| PPNBB | PPN | Congonhas Airport (SBSP) | Araxa Airport (SBAX) | 2026-06-29 10:19 UTC | 2026-06-29 11:00 UTC | 41m |
| RYR3185 | Ryanair | Barcelona International Airport (LEBL) | Kenitra Airport (GMMY) | 2026-06-29 09:37 UTC | 2026-06-29 11:00 UTC | 1h 23m |
| GAWGB | GAW | Wolverhampton Halfpenny Green Airport (EGBO) | Wolverhampton Halfpenny Green Airport (EGBO) | 2026-06-29 10:35 UTC | 2026-06-29 10:59 UTC | 23m |
| HLE06 | HLE | Long Marston Airfield (EGBL) | Long Marston Airfield (EGBL) | 2026-06-29 10:31 UTC | 2026-06-29 10:52 UTC | 20m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-06-29 10:38 UTC | 2026-06-29 10:51 UTC | 12m |
| WZZ8EU | Wizz Air | Barcelona International Airport (LEBL) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-06-29 08:13 UTC | 2026-06-29 10:50 UTC | 2h 36m |
| CPI293 | CPI | Ciampino Airport (LIRA) | Rzeszow-Jasionka Airport (EPRZ) | 2026-06-29 09:01 UTC | 2026-06-29 10:48 UTC | 1h 47m |
| NOZ41S | Norwegian Air | London Gatwick Airport (EGKK) | Trondheim Airport Vaernes (ENVA) | 2026-06-29 08:49 UTC | 2026-06-29 10:45 UTC | 1h 55m |
| AM324 |  | Melbourne Essendon Airport (YMEN) | Bairnsdale Airport (YBNS) | 2026-06-29 10:13 UTC | 2026-06-29 10:43 UTC | 30m |
| TVF25FR | TVF | Paris-Orly Airport (LFPO) | Kenitra Airport (GMMY) | 2026-06-29 08:17 UTC | 2026-06-29 10:41 UTC | 2h 24m |
| CTN2S | CTN | Zagreb Airport (LDZA) | Split Airport (LDSP) | 2026-06-29 10:15 UTC | 2026-06-29 10:41 UTC | 26m |
| EJM180 | EJM | Mikonos Airport (LGMK) | Ibiza Airport (LEIB) | 2026-06-29 08:01 UTC | 2026-06-29 10:41 UTC | 2h 39m |
| CXK555 | CXK | Concord-Padgett Regional Airport (KJQF) | Concord-Padgett Regional Airport (KJQF) | 2026-06-29 10:36 UTC | 2026-06-29 10:40 UTC | 4m |
| N257EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-06-29 09:04 UTC | 2026-06-29 10:37 UTC | 1h 33m |
| MRS1218 | MRS | Ifrane Airport (GMFI) | Kenitra Airport (GMMY) | 2026-06-29 10:01 UTC | 2026-06-29 10:35 UTC | 34m |
| N490LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-06-29 09:09 UTC | 2026-06-29 10:34 UTC | 1h 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
