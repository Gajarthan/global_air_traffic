# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_18:22:35_UTC-green)

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

**Latest saved flight:** 2026-06-23 18:22:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-23 18:22:35 UTC

- **118,118** saved flights
- **40,761** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **118,118** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,432,034.1 tonnes** estimated CO2 emissions
- **83,016,470 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4866 |
| 2 | SkyWest Airlines | 4370 |
| 3 | EJA | 2287 |
| 4 | IndiGo | 2279 |
| 5 | American Airlines | 1838 |
| 6 | Southwest Airlines | 1764 |
| 7 | ENY | 1479 |
| 8 | Delta Air Lines | 1392 |
| 9 | Lufthansa | 1300 |
| 10 | Vueling | 1069 |
| 11 | LATAM Airlines | 1047 |
| 12 | WIF | 1041 |
| 13 | AZU | 986 |
| 14 | AXM | 969 |
| 15 | LXJ | 899 |
| 16 | Swiss International | 834 |
| 17 | All Nippon Airways | 811 |
| 18 | Alaska Airlines | 782 |
| 19 | QLK | 759 |
| 20 | easyJet | 753 |
| 21 | EJU | 739 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 660 |
| 24 | VIV | 650 |
| 25 | Air France | 648 |
| 26 | United Airlines | 647 |
| 27 | CXK | 635 |
| 28 | MXY | 622 |
| 29 | AXB | 585 |
| 30 | GLO | 578 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 99845 |
| 2 | 🇪🇸 ES | 8058 |
| 3 | 🇮🇳 IN | 7165 |
| 4 | 🇦🇺 AU | 6985 |
| 5 | 🇧🇷 BR | 6520 |
| 6 | 🇮🇹 IT | 6308 |
| 7 | 🇩🇪 DE | 6298 |
| 8 | 🇨🇦 CA | 6213 |
| 9 | 🇯🇵 JP | 5294 |
| 10 | 🇬🇧 GB | 5172 |
| 11 | 🇫🇷 FR | 4701 |
| 12 | 🇨🇴 CO | 4000 |
| 13 | 🇲🇽 MX | 3467 |
| 14 | 🇬🇷 GR | 3373 |
| 15 | 🇳🇴 NO | 3240 |
| 16 | 🇨🇭 CH | 3032 |
| 17 | 🇲🇾 MY | 2519 |
| 18 | 🇹🇷 TR | 2415 |
| 19 | 🇿🇦 ZA | 1991 |
| 20 | 🇵🇱 PL | 1939 |
| 21 | 🇳🇿 NZ | 1921 |
| 22 | 🇹🇭 TH | 1900 |
| 23 | 🇰🇷 KR | 1896 |
| 24 | 🇵🇭 PH | 1706 |
| 25 | 🇬🇹 GT | 1661 |
| 26 | 🇲🇦 MA | 1279 |
| 27 | 🇲🇪 ME | 1170 |
| 28 | 🇲🇴 MO | 1170 |
| 29 | 🇳🇱 NL | 1136 |
| 30 | 🇭🇷 HR | 1026 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2489 |
| 2 | Denver International Airport |  | US | 1980 |
| 3 | Tokyo International Airport |  | JP | 1754 |
| 4 | Indira Gandhi International Airport |  | IN | 1571 |
| 5 | Guaymaral Airport |  | CO | 1490 |
| 6 | Harry Reid International Airport |  | US | 1471 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1438 |
| 8 | Zurich Airport |  | CH | 1321 |
| 9 | La Aurora Airport |  | GT | 1283 |
| 10 | Frankfurt am Main International Airport |  | DE | 1262 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1253 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1171 |
| 14 | Macau International Airport |  | MO | 1170 |
| 15 | Chicago O'Hare International Airport |  | US | 1157 |
| 16 | Capua Airport |  | IT | 1021 |
| 17 | Salt Lake City International Airport |  | US | 1010 |
| 18 | Madrid Barajas International Airport |  | ES | 996 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 988 |
| 20 | Kuala Lumpur International Airport |  | MY | 974 |
| 21 | Congonhas Airport |  | BR | 908 |
| 22 | Charlotte/Douglas International Airport |  | US | 898 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 886 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 878 |
| 25 | Bengaluru International Airport |  | IN | 870 |
| 26 | Charles de Gaulle International Airport |  | FR | 867 |
| 27 | Malpensa International Airport |  | IT | 833 |
| 28 | Ninoy Aquino International Airport |  | PH | 788 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 774 |
| 30 | Daniel K Inouye International Airport |  | US | 766 |
| 31 | Tenerife Norte Airport |  | ES | 760 |
| 32 | Barcelona International Airport |  | ES | 750 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 734 |
| 34 | Vitoria/Foronda Airport |  | ES | 694 |
| 35 | Calgary International Airport |  | CA | 693 |
| 36 | Amsterdam Airport Schiphol |  | NL | 690 |
| 37 | Don Mueang International Airport |  | TH | 687 |
| 38 | Seattle-Tacoma International Airport |  | US | 674 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 671 |
| 40 | Viracopos International Airport |  | BR | 670 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 619 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 428 | 21m | 244 km | 1,802.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 313 | 24m | 225 km | 1,214.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 304 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 289 | 1h 25m | 910 km | 4,535.1 t |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 7 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 285 | 1h 10m | 770 km | 3,786.0 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 234 | 26m | 275 km | 1,108.8 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 234 | 19m | 165 km | 665.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 218 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 176 | 22m | 55 km | 167.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 170 | 20m | 99 km | 291.2 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 169 | 26m | 215 km | 625.9 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 160 | 27m | 152 km | 418.1 t |
| 18 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 159 | 44m | 241 km | 660.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 153 | 44m | 452 km | 1,192.4 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 148 | 1h 44m | 1,423 km | 3,632.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 148 | 20m | 250 km | 639.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 138 | 1h 39m | 1,156 km | 2,753.0 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 133 | 1h 17m | 961 km | 2,204.5 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGIEZ | CGI | Rockton Airport (CPT3) | CNQ4 (CNQ4) | 2026-06-23 16:06 UTC | 2026-06-23 18:22 UTC | 2h 15m |
| RYR4799 | Ryanair | Sepurine Training Base (LD57) | Jonava Airport (EYRU) | 2026-06-23 16:43 UTC | 2026-06-23 18:14 UTC | 1h 31m |
| HAWK211 | HAW | Kingsville Nas Airport (KNQI) | Triple B Ranch Airport (42XS) | 2026-06-23 18:03 UTC | 2026-06-23 18:14 UTC | 10m |
| N1287E |  | John Wayne/Orange County Airport (KSNA) | Hemet-Ryan Airport (KHMT) | 2026-06-23 17:38 UTC | 2026-06-23 18:14 UTC | 36m |
| SKW4708 | SkyWest Airlines | San Francisco International Airport (KSFO) | Rohnerville Airport (KFOT) | 2026-06-23 17:39 UTC | 2026-06-23 18:09 UTC | 30m |
| CGFCG | CGF | Three Hills Airport (CEN3) | Three Hills Airport (CEN3) | 2026-06-23 17:05 UTC | 2026-06-23 18:09 UTC | 1h 4m |
| N737MH |  | Chino Airport (KCNO) | Chino Airport (KCNO) | 2026-06-23 17:30 UTC | 2026-06-23 18:06 UTC | 36m |
| CFVZR | CFV | Squamish Airport (CYSE) | Squamish Airport (CYSE) | 2026-06-23 17:50 UTC | 2026-06-23 18:01 UTC | 11m |
| THA325 | Thai Airways | Suvarnabhumi Airport (VTBS) | Bengaluru International Airport (VOBL) | 2026-06-23 15:04 UTC | 2026-06-23 17:59 UTC | 2h 55m |
| BPX270 | BPX | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-06-23 17:41 UTC | 2026-06-23 17:59 UTC | 17m |
| DESERT7 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-06-23 17:47 UTC | 2026-06-23 17:58 UTC | 10m |
| N7670F |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-06-23 17:18 UTC | 2026-06-23 17:56 UTC | 38m |
| N411AK |  | 97MO (97MO) | MO52 (MO52) | 2026-06-23 17:44 UTC | 2026-06-23 17:55 UTC | 10m |
| N513LF |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-06-23 17:37 UTC | 2026-06-23 17:55 UTC | 18m |
| CGYVJ | CGY | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-06-23 17:25 UTC | 2026-06-23 17:54 UTC | 29m |
| N741SM |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-06-23 16:10 UTC | 2026-06-23 17:54 UTC | 1h 43m |
| N929TG |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-06-23 17:31 UTC | 2026-06-23 17:54 UTC | 22m |
| N296CB |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-06-23 17:31 UTC | 2026-06-23 17:53 UTC | 22m |
| N208JK |  | Flying Cloud Airport (KFCM) | Molnau Airpark (1MN5) | 2026-06-23 17:43 UTC | 2026-06-23 17:53 UTC | 9m |
| N407GX |  | Fuller Airport (TS00) | Fuller Airport (TS00) | 2026-06-23 17:35 UTC | 2026-06-23 17:52 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
