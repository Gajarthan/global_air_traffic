# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_21:38:48_UTC-green)

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

**Latest saved flight:** 2026-06-05 21:38:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-05 21:38:48 UTC

- **103,074** saved flights
- **36,481** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **103,074** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,258,174.3 tonnes** estimated CO2 emissions
- **72,937,640 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4237 |
| 2 | SkyWest Airlines | 3876 |
| 3 | IndiGo | 2059 |
| 4 | EJA | 1972 |
| 5 | American Airlines | 1663 |
| 6 | Southwest Airlines | 1555 |
| 7 | ENY | 1280 |
| 8 | Delta Air Lines | 1214 |
| 9 | Lufthansa | 1191 |
| 10 | Vueling | 951 |
| 11 | LATAM Airlines | 913 |
| 12 | WIF | 907 |
| 13 | AXM | 886 |
| 14 | AZU | 828 |
| 15 | LXJ | 778 |
| 16 | Swiss International | 744 |
| 17 | All Nippon Airways | 727 |
| 18 | Alaska Airlines | 721 |
| 19 | QLK | 692 |
| 20 | easyJet | 668 |
| 21 | EJU | 645 |
| 22 | Cathay Pacific | 616 |
| 23 | AEE | 600 |
| 24 | VIV | 591 |
| 25 | Air France | 590 |
| 26 | United Airlines | 572 |
| 27 | MXY | 558 |
| 28 | CXK | 553 |
| 29 | Japan Airlines | 511 |
| 30 | AXB | 506 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 86734 |
| 2 | 🇪🇸 ES | 7086 |
| 3 | 🇮🇳 IN | 6504 |
| 4 | 🇦🇺 AU | 6266 |
| 5 | 🇧🇷 BR | 5638 |
| 6 | 🇩🇪 DE | 5538 |
| 7 | 🇮🇹 IT | 5469 |
| 8 | 🇨🇦 CA | 5368 |
| 9 | 🇯🇵 JP | 4752 |
| 10 | 🇬🇧 GB | 4347 |
| 11 | 🇫🇷 FR | 4087 |
| 12 | 🇨🇴 CO | 3541 |
| 13 | 🇲🇽 MX | 3096 |
| 14 | 🇬🇷 GR | 2935 |
| 15 | 🇳🇴 NO | 2872 |
| 16 | 🇨🇭 CH | 2639 |
| 17 | 🇲🇾 MY | 2259 |
| 18 | 🇹🇷 TR | 1950 |
| 19 | 🇿🇦 ZA | 1790 |
| 20 | 🇳🇿 NZ | 1731 |
| 21 | 🇹🇭 TH | 1701 |
| 22 | 🇰🇷 KR | 1677 |
| 23 | 🇵🇱 PL | 1648 |
| 24 | 🇬🇹 GT | 1507 |
| 25 | 🇵🇭 PH | 1502 |
| 26 | 🇲🇦 MA | 1138 |
| 27 | 🇲🇴 MO | 1076 |
| 28 | 🇳🇱 NL | 1017 |
| 29 | 🇲🇪 ME | 970 |
| 30 | 🇭🇷 HR | 903 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2235 |
| 2 | Denver International Airport |  | US | 1766 |
| 3 | Tokyo International Airport |  | JP | 1577 |
| 4 | Indira Gandhi International Airport |  | IN | 1411 |
| 5 | Harry Reid International Airport |  | US | 1323 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1316 |
| 7 | Guaymaral Airport |  | CO | 1286 |
| 8 | Frankfurt am Main International Airport |  | DE | 1191 |
| 9 | Zurich Airport |  | CH | 1173 |
| 10 | La Aurora Airport |  | GT | 1160 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1114 |
| 12 | El Dorado International Airport |  | CO | 1083 |
| 13 | Macau International Airport |  | MO | 1076 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1042 |
| 15 | Chicago O'Hare International Airport |  | US | 1029 |
| 16 | Madrid Barajas International Airport |  | ES | 899 |
| 17 | Kuala Lumpur International Airport |  | MY | 891 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 884 |
| 19 | Salt Lake City International Airport |  | US | 872 |
| 20 | Capua Airport |  | IT | 856 |
| 21 | Charlotte/Douglas International Airport |  | US | 801 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 799 |
| 23 | Charles de Gaulle International Airport |  | FR | 784 |
| 24 | Congonhas Airport |  | BR | 782 |
| 25 | Bengaluru International Airport |  | IN | 779 |
| 26 | Malpensa International Airport |  | IT | 774 |
| 27 | Daniel K Inouye International Airport |  | US | 710 |
| 28 | Tenerife Norte Airport |  | ES | 703 |
| 29 | Ninoy Aquino International Airport |  | PH | 686 |
| 30 | Barcelona International Airport |  | ES | 676 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 668 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 665 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 660 |
| 34 | Amsterdam Airport Schiphol |  | NL | 629 |
| 35 | Don Mueang International Airport |  | TH | 623 |
| 36 | Vitoria/Foronda Airport |  | ES | 621 |
| 37 | Calgary International Airport |  | CA | 613 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 597 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 584 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 531 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 378 | 21m | 244 km | 1,591.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 272 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 270 | 24m | 225 km | 1,047.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 257 | 14m | 114 km | 504.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 251 | 1h 26m | 910 km | 3,938.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 249 | 28m | 304 km | 1,305.3 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 237 | 1h 10m | 770 km | 3,148.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 134 | 18m | 144 km | 333.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 132 | 20m | 147 km | 334.0 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 129 | 1h 39m | 1,156 km | 2,573.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |
| 28 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 118 | 44m | 241 km | 490.1 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 118 | 12m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FDX6092 | FDX | Cologne Bonn Airport (EDDK) | Norvenich Airport (ETNN) | 2026-06-05 20:53 UTC | 2026-06-05 21:38 UTC | 45m |
| JSD576 | JSD | Warsaw Chopin Airport (EPWA) | Nannhausen Airport (EDRN) | 2026-06-05 19:33 UTC | 2026-06-05 21:38 UTC | 2h 5m |
| EJU76NZ | EJU | Berlin Brandenburg Airport (EDDB) | Cologne Bonn Airport (EDDK) | 2026-06-05 20:16 UTC | 2026-06-05 21:38 UTC | 1h 21m |
| N682AC |  | Hidden Valley Ranch Airport (TS90) | Bb Airpark (TE88) | 2026-06-05 21:19 UTC | 2026-06-05 21:32 UTC | 13m |
| N87RM |  | Skydive New England Airport (ME64) | Skydive New England Airport (ME64) | 2026-06-05 21:06 UTC | 2026-06-05 21:23 UTC | 17m |
| N607FJ |  | Ted Stevens Anchorage International Airport (PANC) | Fairbanks International Airport (PAFA) | 2026-06-05 19:18 UTC | 2026-06-05 21:20 UTC | 2h 2m |
| ANVIL97 | ANV | West Virginia International Yeager Airport (KCRW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-06-05 20:50 UTC | 2026-06-05 21:20 UTC | 29m |
| N333WR |  | Gwinnett County/Briscoe Field (KLZU) | Savannah/Hilton Head International Airport (KSAV) | 2026-06-05 20:09 UTC | 2026-06-05 21:18 UTC | 1h 9m |
| AFL1861 | AFL | Yerevan Yegvard Airport (UD21) | Chkalovskiy Airport (UUMU) | 2026-06-05 17:49 UTC | 2026-06-05 21:17 UTC | 3h 28m |
| N220BL |  | Johnston Regional Airport (KJNX) | Wayne Executive Jetport Airport (KGWW) | 2026-06-05 20:47 UTC | 2026-06-05 21:14 UTC | 27m |
| ZOOM41 | ZOO | Danaher Airport (7TX0) | Munday Municipal Airport (K37F) | 2026-06-05 20:55 UTC | 2026-06-05 21:10 UTC | 15m |
| BOE451 | BOE | Renton Municipal Airport (KRNT) | Rnr Farms Airport (79WA) | 2026-06-05 19:30 UTC | 2026-06-05 21:09 UTC | 1h 39m |
| DHC96 | DHC | Calgary International Airport (CYYC) | Calgary International Airport (CYYC) | 2026-06-05 20:47 UTC | 2026-06-05 21:07 UTC | 20m |
| RYR299Q | Ryanair | Alicante International Airport (LEAL) | Grefrath-Niershorst Airport (EDLF) | 2026-06-05 18:58 UTC | 2026-06-05 21:07 UTC | 2h 8m |
| SPTN885 | SPT | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-06-05 20:54 UTC | 2026-06-05 21:05 UTC | 10m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-06-05 20:39 UTC | 2026-06-05 20:58 UTC | 19m |
| N227VC |  | Austin Executive Airport (KEDC) | Henderson Executive Airport (KHND) | 2026-06-05 18:24 UTC | 2026-06-05 20:58 UTC | 2h 34m |
| N5168A |  | Greeley-Weld County Airport (KGXY) | CO81 (CO81) | 2026-06-05 20:26 UTC | 2026-06-05 20:57 UTC | 30m |
| VTE3344 | VTE | Phoenix Sky Harbor International Airport (KPHX) | Happy Canyon Airport (UT97) | 2026-06-05 20:06 UTC | 2026-06-05 20:56 UTC | 49m |
| N551AP |  | Miami Executive Airport (KTMB) | Sarasota/Bradenton International Airport (KSRQ) | 2026-06-05 18:52 UTC | 2026-06-05 20:55 UTC | 2h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
