# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--16_06:46:54_UTC-green)

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

**Latest saved flight:** 2026-07-16 06:46:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-16 06:46:54 UTC

- **141,891** saved flights
- **47,613** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **141,891** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,702,871.0 tonnes** estimated CO2 emissions
- **98,717,161 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5772 |
| 2 | SkyWest Airlines | 5185 |
| 3 | EJA | 2791 |
| 4 | IndiGo | 2595 |
| 5 | American Airlines | 2260 |
| 6 | Southwest Airlines | 2136 |
| 7 | ENY | 1759 |
| 8 | Delta Air Lines | 1678 |
| 9 | Lufthansa | 1433 |
| 10 | LATAM Airlines | 1304 |
| 11 | Vueling | 1220 |
| 12 | AZU | 1216 |
| 13 | WIF | 1216 |
| 14 | LXJ | 1088 |
| 15 | AXM | 1053 |
| 16 | Swiss International | 1009 |
| 17 | easyJet | 923 |
| 18 | All Nippon Airways | 912 |
| 19 | Alaska Airlines | 894 |
| 20 | QLK | 894 |
| 21 | EJU | 876 |
| 22 | VIV | 786 |
| 23 | AEE | 759 |
| 24 | CXK | 757 |
| 25 | Air France | 755 |
| 26 | JetBlue | 755 |
| 27 | United Airlines | 739 |
| 28 | Cathay Pacific | 735 |
| 29 | MXY | 734 |
| 30 | GLO | 726 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 121955 |
| 2 | 🇪🇸 ES | 9264 |
| 3 | 🇦🇺 AU | 8152 |
| 4 | 🇮🇳 IN | 8130 |
| 5 | 🇧🇷 BR | 7998 |
| 6 | 🇨🇦 CA | 7460 |
| 7 | 🇮🇹 IT | 7403 |
| 8 | 🇩🇪 DE | 7371 |
| 9 | 🇬🇧 GB | 6472 |
| 10 | 🇯🇵 JP | 5966 |
| 11 | 🇫🇷 FR | 5642 |
| 12 | 🇨🇴 CO | 4518 |
| 13 | 🇲🇽 MX | 4117 |
| 14 | 🇬🇷 GR | 4038 |
| 15 | 🇳🇴 NO | 3805 |
| 16 | 🇨🇭 CH | 3672 |
| 17 | 🇹🇷 TR | 3358 |
| 18 | 🇲🇾 MY | 2747 |
| 19 | 🇵🇱 PL | 2377 |
| 20 | 🇿🇦 ZA | 2320 |
| 21 | 🇳🇿 NZ | 2174 |
| 22 | 🇹🇭 TH | 2122 |
| 23 | 🇰🇷 KR | 2026 |
| 24 | 🇵🇭 PH | 1924 |
| 25 | 🇬🇹 GT | 1866 |
| 26 | 🇲🇦 MA | 1488 |
| 27 | 🇲🇪 ME | 1407 |
| 28 | 🇳🇱 NL | 1335 |
| 29 | 🇭🇷 HR | 1291 |
| 30 | 🇲🇴 MO | 1191 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2917 |
| 2 | Denver International Airport |  | US | 2371 |
| 3 | Tokyo International Airport |  | JP | 1925 |
| 4 | Indira Gandhi International Airport |  | IN | 1802 |
| 5 | Harry Reid International Airport |  | US | 1777 |
| 6 | Guaymaral Airport |  | CO | 1728 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1627 |
| 8 | Zurich Airport |  | CH | 1577 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1487 |
| 10 | La Aurora Airport |  | GT | 1443 |
| 11 | Frankfurt am Main International Airport |  | DE | 1382 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1348 |
| 13 | Chicago O'Hare International Airport |  | US | 1329 |
| 14 | Salt Lake City International Airport |  | US | 1269 |
| 15 | El Dorado International Airport |  | CO | 1254 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1241 |
| 17 | Macau International Airport |  | MO | 1191 |
| 18 | Capua Airport |  | IT | 1163 |
| 19 | Madrid Barajas International Airport |  | ES | 1144 |
| 20 | Congonhas Airport |  | BR | 1137 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1128 |
| 22 | Kuala Lumpur International Airport |  | MY | 1060 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1034 |
| 24 | Charlotte/Douglas International Airport |  | US | 1028 |
| 25 | Charles de Gaulle International Airport |  | FR | 1000 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 990 |
| 27 | Bengaluru International Airport |  | IN | 972 |
| 28 | Malpensa International Airport |  | IT | 919 |
| 29 | Ninoy Aquino International Airport |  | PH | 898 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 868 |
| 31 | Daniel K Inouye International Airport |  | US | 867 |
| 32 | Barcelona International Airport |  | ES | 863 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 837 |
| 34 | Tenerife Norte Airport |  | ES | 820 |
| 35 | Calgary International Airport |  | CA | 811 |
| 36 | Seattle-Tacoma International Airport |  | US | 804 |
| 37 | Viracopos International Airport |  | BR | 803 |
| 38 | Amsterdam Airport Schiphol |  | NL | 803 |
| 39 | Scottsdale Airport |  | US | 803 |
| 40 | Vitoria/Foronda Airport |  | ES | 782 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 728 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 517 | 21m | 244 km | 2,176.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 349 | 24m | 225 km | 1,354.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 345 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 336 | 1h 9m | 770 km | 4,463.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 259 | 26m | 275 km | 1,227.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 208 | 22m | 55 km | 197.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 191 | 1h 46m | 1,423 km | 4,687.4 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 189 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 189 | 20m | 99 km | 323.7 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 177 | 20m | 250 km | 764.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 177 | 28m | 152 km | 462.6 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 172 | 31m | 369 km | 1,094.8 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 170 | 18m | 144 km | 422.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 167 | 44m | 452 km | 1,301.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 163 | 1h 1m | 695 km | 1,953.9 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 163 | 1h 16m | 961 km | 2,701.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 159 | 13m | - | - |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JLK | JLK | Goulburn Airport (YGLB) | Sydney Kingsford Smith International Airport (YSSY) | 2026-07-16 06:11 UTC | 2026-07-16 06:46 UTC | 35m |
| DFSWW | DFS | Herning Airport (EKHG) | Herning Airport (EKHG) | 2026-07-16 06:07 UTC | 2026-07-16 06:37 UTC | 30m |
| GEC8460 | GEC | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-07-15 19:35 UTC | 2026-07-16 06:23 UTC | 10h 48m |
| KITE50 | KIT | Ellison Onizuka Kona International At Keahole Airport (PHKO) | HI13 (HI13) | 2026-07-16 05:54 UTC | 2026-07-16 06:23 UTC | 28m |
| LOT3805 | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Rzeszow-Jasionka Airport (EPRZ) | 2026-07-16 05:35 UTC | 2026-07-16 06:15 UTC | 39m |
| N611GV |  | Kenai Municipal Airport (PAEN) | Ted Stevens Anchorage International Airport (PANC) | 2026-07-16 05:48 UTC | 2026-07-16 06:14 UTC | 26m |
| CPA740 | Cathay Pacific | Kep Air Base (VVKP) | Zhuhai Airport (ZGSD) | 2026-07-16 04:55 UTC | 2026-07-16 06:05 UTC | 1h 10m |
| ST728 |  | Mandalay International Airport (VYMD) | Pinlebu Airport (VYPL) | 2026-07-16 05:25 UTC | 2026-07-16 06:03 UTC | 37m |
| DAL2456 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-07-16 05:59 UTC | 2026-07-16 06:02 UTC | 2m |
| A7GAC |  | Doha International Airport (OTBD) | Al Khawr Airport (OTBK) | 2026-07-16 04:54 UTC | 2026-07-16 06:01 UTC | 1h 7m |
| RYR9418 | Ryanair | Václav Havel Airport (LKPR) | Skiathos Island National Airport (LGSK) | 2026-07-16 04:06 UTC | 2026-07-16 05:57 UTC | 1h 51m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-07-16 05:16 UTC | 2026-07-16 05:56 UTC | 40m |
| DLH8HW | Lufthansa | Munich International Airport (EDDM) | Munster Osnabruck Airport (EDDG) | 2026-07-16 05:04 UTC | 2026-07-16 05:56 UTC | 52m |
| AEE348 | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-07-16 05:35 UTC | 2026-07-16 05:56 UTC | 20m |
| VOE76TX | VOE | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Olbia / Costa Smeralda Airport (LIEO) | 2026-07-16 04:57 UTC | 2026-07-16 05:53 UTC | 55m |
| N374YJ |  | Yokota Air Base (RJTY) | Yokota Air Base (RJTY) | 2026-07-16 05:10 UTC | 2026-07-16 05:51 UTC | 40m |
| SEJYV | SEJ | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-07-16 04:43 UTC | 2026-07-16 05:48 UTC | 1h 5m |
| CARD40 | CAR | Seoul Air Base (RKSM) | Seoul Air Base (RKSM) | 2026-07-16 05:43 UTC | 2026-07-16 05:44 UTC | 0m |
| N330PH |  | Mckinney Ntl Airport (KTKI) | Addison Airport (KADS) | 2026-07-16 05:28 UTC | 2026-07-16 05:43 UTC | 15m |
| RXA2125 | RXA | Perth International Airport (YPPH) | Frankland Airport (YFRK) | 2026-07-16 04:59 UTC | 2026-07-16 05:43 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
