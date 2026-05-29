# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_04:22:16_UTC-green)

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

**Latest saved flight:** 2026-05-29 04:22:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-29 04:22:16 UTC

- **96,263** saved flights
- **33,854** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **96,263** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,179,814.2 tonnes** estimated CO2 emissions
- **68,395,026 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4040 |
| 2 | SkyWest Airlines | 3582 |
| 3 | IndiGo | 1991 |
| 4 | EJA | 1822 |
| 5 | American Airlines | 1457 |
| 6 | Southwest Airlines | 1402 |
| 7 | ENY | 1185 |
| 8 | Lufthansa | 1150 |
| 9 | Delta Air Lines | 1053 |
| 10 | Vueling | 910 |
| 11 | LATAM Airlines | 864 |
| 12 | AXM | 850 |
| 13 | WIF | 847 |
| 14 | AZU | 772 |
| 15 | LXJ | 734 |
| 16 | Swiss International | 716 |
| 17 | All Nippon Airways | 709 |
| 18 | Alaska Airlines | 672 |
| 19 | QLK | 668 |
| 20 | easyJet | 632 |
| 21 | EJU | 613 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 579 |
| 24 | Air France | 566 |
| 25 | VIV | 566 |
| 26 | CXK | 514 |
| 27 | MXY | 510 |
| 28 | Japan Airlines | 494 |
| 29 | AXB | 488 |
| 30 | AIQ | 463 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 79627 |
| 2 | 🇪🇸 ES | 6724 |
| 3 | 🇮🇳 IN | 6290 |
| 4 | 🇦🇺 AU | 5906 |
| 5 | 🇧🇷 BR | 5286 |
| 6 | 🇩🇪 DE | 5269 |
| 7 | 🇮🇹 IT | 5202 |
| 8 | 🇨🇦 CA | 4896 |
| 9 | 🇯🇵 JP | 4586 |
| 10 | 🇬🇧 GB | 4122 |
| 11 | 🇫🇷 FR | 3900 |
| 12 | 🇨🇴 CO | 3343 |
| 13 | 🇲🇽 MX | 2954 |
| 14 | 🇬🇷 GR | 2773 |
| 15 | 🇳🇴 NO | 2694 |
| 16 | 🇨🇭 CH | 2527 |
| 17 | 🇲🇾 MY | 2159 |
| 18 | 🇹🇷 TR | 1784 |
| 19 | 🇿🇦 ZA | 1723 |
| 20 | 🇳🇿 NZ | 1649 |
| 21 | 🇹🇭 TH | 1629 |
| 22 | 🇰🇷 KR | 1584 |
| 23 | 🇵🇱 PL | 1569 |
| 24 | 🇵🇭 PH | 1450 |
| 25 | 🇬🇹 GT | 1439 |
| 26 | 🇲🇦 MA | 1091 |
| 27 | 🇲🇴 MO | 1039 |
| 28 | 🇳🇱 NL | 968 |
| 29 | 🇲🇪 ME | 946 |
| 30 | 🇭🇷 HR | 871 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2085 |
| 2 | Denver International Airport |  | US | 1630 |
| 3 | Tokyo International Airport |  | JP | 1521 |
| 4 | Indira Gandhi International Airport |  | IN | 1363 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1271 |
| 6 | Harry Reid International Airport |  | US | 1240 |
| 7 | Guaymaral Airport |  | CO | 1184 |
| 8 | Frankfurt am Main International Airport |  | DE | 1160 |
| 9 | Zurich Airport |  | CH | 1122 |
| 10 | La Aurora Airport |  | GT | 1103 |
| 11 | El Dorado International Airport |  | CO | 1041 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1039 |
| 13 | Macau International Airport |  | MO | 1039 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 966 |
| 15 | Chicago O'Hare International Airport |  | US | 925 |
| 16 | Kuala Lumpur International Airport |  | MY | 855 |
| 17 | Madrid Barajas International Airport |  | ES | 853 |
| 18 | Salt Lake City International Airport |  | US | 811 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 809 |
| 20 | Capua Airport |  | IT | 799 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 768 |
| 22 | Bengaluru International Airport |  | IN | 755 |
| 23 | Malpensa International Airport |  | IT | 753 |
| 24 | Charles de Gaulle International Airport |  | FR | 748 |
| 25 | Congonhas Airport |  | BR | 733 |
| 26 | Charlotte/Douglas International Airport |  | US | 730 |
| 27 | Daniel K Inouye International Airport |  | US | 686 |
| 28 | Tenerife Norte Airport |  | ES | 682 |
| 29 | Ninoy Aquino International Airport |  | PH | 661 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 644 |
| 31 | Barcelona International Airport |  | ES | 643 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 622 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 616 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Amsterdam Airport Schiphol |  | NL | 596 |
| 36 | Don Mueang International Airport |  | TH | 595 |
| 37 | Vitoria/Foronda Airport |  | ES | 594 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 570 |
| 39 | Calgary International Airport |  | CA | 567 |
| 40 | O. R. Tambo International Airport |  | ZA | 548 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 487 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 356 | 21m | 244 km | 1,499.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 261 | 24m | 225 km | 1,012.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 256 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 245 | 14m | 114 km | 480.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 242 | 1h 26m | 910 km | 3,797.5 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 241 | 28m | 304 km | 1,263.4 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 221 | 1h 10m | 770 km | 2,935.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 208 | 19m | 165 km | 591.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 192 | 26m | 275 km | 909.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 154 | 21m | 99 km | 263.8 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 144 | 27m | 215 km | 533.3 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 138 | 22m | 55 km | 131.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 138 | 27m | 152 km | 360.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 130 | 20m | 250 km | 561.5 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 125 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 123 | 1h 1m | 695 km | 1,474.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 123 | 18m | 144 km | 306.0 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 122 | 1h 39m | 1,156 km | 2,433.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 52m | 1,304 km | 2,609.7 t |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 114 | 1h 18m | 961 km | 1,889.6 t |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WXQ | WXQ | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-05-29 03:59 UTC | 2026-05-29 04:22 UTC | 22m |
| ZKHJM | ZKH | Christchurch International Airport (NZCH) | West Melton Aerodrome (NZWL) | 2026-05-29 03:32 UTC | 2026-05-29 04:21 UTC | 48m |
| ELY223 | ELY | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-05-29 03:53 UTC | 2026-05-29 04:16 UTC | 22m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-29 03:46 UTC | 2026-05-29 03:57 UTC | 10m |
| QLK22D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Woodville Airport (YWVL) | 2026-05-29 03:07 UTC | 2026-05-29 03:47 UTC | 39m |
| OME11 | OME | Coppersmith Airport (2NE6) | Judy Ranch Airport (OK39) | 2026-05-29 03:10 UTC | 2026-05-29 03:46 UTC | 35m |
| ELY393 | ELY | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-05-29 03:13 UTC | 2026-05-29 03:36 UTC | 23m |
| N959UA |  | Merrill Field (PAMR) | Talkeetna Airport (PATK) | 2026-05-29 02:50 UTC | 2026-05-29 03:36 UTC | 46m |
| CVA650 | CVA | Auckland International Airport (NZAA) | Hood Airport (NZMS) | 2026-05-29 02:33 UTC | 2026-05-29 03:34 UTC | 1h 0m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-29 03:21 UTC | 2026-05-29 03:32 UTC | 11m |
| RXA6828 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-05-29 02:53 UTC | 2026-05-29 03:28 UTC | 34m |
| SWA2966 | Southwest Airlines | Long Beach (Daugherty Field) Airport (KLGB) | Reno/Tahoe International Airport (KRNO) | 2026-05-29 02:29 UTC | 2026-05-29 03:22 UTC | 52m |
| WUJ | WUJ | Romsey (Riddell/Penfield) Airport (YRSY) | Melbourne Essendon Airport (YMEN) | 2026-05-29 03:00 UTC | 2026-05-29 03:21 UTC | 20m |
| ELY319 | ELY | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-05-29 03:08 UTC | 2026-05-29 03:18 UTC | 10m |
| QLK623D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-05-29 02:45 UTC | 2026-05-29 03:18 UTC | 33m |
| ELY2365 | ELY | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-05-29 02:46 UTC | 2026-05-29 03:16 UTC | 30m |
| VUAVS | VUA | Indira Gandhi International Airport (VIDP) | Jallowal Airport (VI88) | 2026-05-29 02:31 UTC | 2026-05-29 03:14 UTC | 43m |
| MTNG101 | MTN | Kamphaeng Saen Airport (VTBK) | Prachuap Khiri Khan Airport (VTBN) | 2026-05-28 05:46 UTC | 2026-05-29 03:09 UTC | 21h 23m |
| ASA1092 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-05-29 02:49 UTC | 2026-05-29 03:08 UTC | 18m |
| ZKNZO | ZKN | Glenorchy Airport (NZGY) | Queenstown International Airport (NZQN) | 2026-05-29 02:55 UTC | 2026-05-29 03:06 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
