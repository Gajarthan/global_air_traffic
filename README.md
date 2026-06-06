# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_20:27:07_UTC-green)

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

**Latest saved flight:** 2026-06-06 20:27:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-06 20:27:07 UTC

- **104,645** saved flights
- **36,891** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **104,645** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,279,115.8 tonnes** estimated CO2 emissions
- **74,151,641 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4307 |
| 2 | SkyWest Airlines | 3940 |
| 3 | IndiGo | 2088 |
| 4 | EJA | 2002 |
| 5 | American Airlines | 1685 |
| 6 | Southwest Airlines | 1579 |
| 7 | ENY | 1308 |
| 8 | Delta Air Lines | 1240 |
| 9 | Lufthansa | 1201 |
| 10 | Vueling | 965 |
| 11 | LATAM Airlines | 924 |
| 12 | WIF | 914 |
| 13 | AXM | 897 |
| 14 | AZU | 839 |
| 15 | LXJ | 788 |
| 16 | Swiss International | 755 |
| 17 | All Nippon Airways | 734 |
| 18 | Alaska Airlines | 727 |
| 19 | QLK | 697 |
| 20 | easyJet | 680 |
| 21 | EJU | 656 |
| 22 | Cathay Pacific | 623 |
| 23 | AEE | 605 |
| 24 | VIV | 603 |
| 25 | Air France | 602 |
| 26 | United Airlines | 579 |
| 27 | MXY | 568 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 522 |
| 30 | AXB | 515 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 88076 |
| 2 | 🇪🇸 ES | 7214 |
| 3 | 🇮🇳 IN | 6595 |
| 4 | 🇦🇺 AU | 6310 |
| 5 | 🇧🇷 BR | 5709 |
| 6 | 🇩🇪 DE | 5622 |
| 7 | 🇮🇹 IT | 5565 |
| 8 | 🇨🇦 CA | 5433 |
| 9 | 🇯🇵 JP | 4819 |
| 10 | 🇬🇧 GB | 4419 |
| 11 | 🇫🇷 FR | 4151 |
| 12 | 🇨🇴 CO | 3622 |
| 13 | 🇲🇽 MX | 3138 |
| 14 | 🇬🇷 GR | 2982 |
| 15 | 🇳🇴 NO | 2903 |
| 16 | 🇨🇭 CH | 2672 |
| 17 | 🇲🇾 MY | 2296 |
| 18 | 🇹🇷 TR | 1998 |
| 19 | 🇿🇦 ZA | 1804 |
| 20 | 🇳🇿 NZ | 1744 |
| 21 | 🇹🇭 TH | 1723 |
| 22 | 🇰🇷 KR | 1722 |
| 23 | 🇵🇱 PL | 1694 |
| 24 | 🇵🇭 PH | 1532 |
| 25 | 🇬🇹 GT | 1521 |
| 26 | 🇲🇦 MA | 1160 |
| 27 | 🇲🇴 MO | 1099 |
| 28 | 🇳🇱 NL | 1029 |
| 29 | 🇲🇪 ME | 995 |
| 30 | 🇭🇷 HR | 915 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2277 |
| 2 | Denver International Airport |  | US | 1791 |
| 3 | Tokyo International Airport |  | JP | 1599 |
| 4 | Indira Gandhi International Airport |  | IN | 1432 |
| 5 | Harry Reid International Airport |  | US | 1339 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1328 |
| 7 | Guaymaral Airport |  | CO | 1320 |
| 8 | Frankfurt am Main International Airport |  | DE | 1198 |
| 9 | Zurich Airport |  | CH | 1185 |
| 10 | La Aurora Airport |  | GT | 1169 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1130 |
| 12 | El Dorado International Airport |  | CO | 1103 |
| 13 | Macau International Airport |  | MO | 1099 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1059 |
| 15 | Chicago O'Hare International Airport |  | US | 1051 |
| 16 | Madrid Barajas International Airport |  | ES | 916 |
| 17 | Kuala Lumpur International Airport |  | MY | 900 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 894 |
| 19 | Salt Lake City International Airport |  | US | 892 |
| 20 | Capua Airport |  | IT | 881 |
| 21 | Charlotte/Douglas International Airport |  | US | 811 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 803 |
| 23 | Charles de Gaulle International Airport |  | FR | 798 |
| 24 | Congonhas Airport |  | BR | 793 |
| 25 | Bengaluru International Airport |  | IN | 792 |
| 26 | Malpensa International Airport |  | IT | 783 |
| 27 | Daniel K Inouye International Airport |  | US | 717 |
| 28 | Tenerife Norte Airport |  | ES | 715 |
| 29 | Ninoy Aquino International Airport |  | PH | 700 |
| 30 | Barcelona International Airport |  | ES | 687 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 677 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 676 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 670 |
| 34 | Amsterdam Airport Schiphol |  | NL | 637 |
| 35 | Don Mueang International Airport |  | TH | 630 |
| 36 | Vitoria/Foronda Airport |  | ES | 630 |
| 37 | Calgary International Airport |  | CA | 618 |
| 38 | Seattle-Tacoma International Airport |  | US | 606 |
| 39 | Netaji Subhash Chandra Bose International Airport |  | IN | 603 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 596 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 545 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 385 | 21m | 244 km | 1,621.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 280 | 1h 7m | 706 km | 3,409.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 276 | 24m | 225 km | 1,070.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 274 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 265 | 14m | 114 km | 519.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 257 | 1h 25m | 910 km | 4,032.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 256 | 28m | 304 km | 1,342.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 241 | 1h 10m | 770 km | 3,201.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 209 | 26m | 275 km | 990.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 152 | 27m | 215 km | 562.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 144 | 31m | 369 km | 916.6 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 136 | 18m | 144 km | 338.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 122 | 1h 43m | 1,423 km | 2,994.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 29 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 119 | 44m | 241 km | 494.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9529G |  | Middletown Regional/Hook Field (KMWO) | Middletown Regional/Hook Field (KMWO) | 2026-06-06 20:06 UTC | 2026-06-06 20:27 UTC | 20m |
| UHAUL99 | UHA | Kelly Field (KSKF) | Ingalls Municipal Airport (K30K) | 2026-06-06 19:00 UTC | 2026-06-06 20:12 UTC | 1h 12m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-06-06 06:09 UTC | 2026-06-06 20:08 UTC | 13h 59m |
| SCHNR66 | SCH | Los Alamitos Army Air Field (KSLI) | Los Alamitos Army Air Field (KSLI) | 2026-06-06 19:27 UTC | 2026-06-06 20:04 UTC | 36m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-06-06 19:47 UTC | 2026-06-06 20:00 UTC | 13m |
| N343KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-06 19:37 UTC | 2026-06-06 19:59 UTC | 21m |
| N424KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-06 19:23 UTC | 2026-06-06 19:58 UTC | 35m |
| AWH91A | AWH | Hannover Airport (EDDV) | Eelde Airport (EHGG) | 2026-06-06 19:33 UTC | 2026-06-06 19:58 UTC | 25m |
| N471CB |  | Tulsa International Airport (KTUL) | Mc Alester Regional Airport (KMLC) | 2026-06-06 19:28 UTC | 2026-06-06 19:54 UTC | 25m |
| N88765 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-06 19:34 UTC | 2026-06-06 19:54 UTC | 19m |
| JBU1366 | JetBlue | Cancun International Airport (MMUN) | Tampa International Airport (KTPA) | 2026-06-06 18:26 UTC | 2026-06-06 19:52 UTC | 1h 26m |
| N828SK |  | Tucson International Airport (KTUS) | Johnson County Airport (KBYG) | 2026-06-06 18:07 UTC | 2026-06-06 19:50 UTC | 1h 43m |
| AAL1538 | American Airlines | Miami International Airport (KMIA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-06 16:57 UTC | 2026-06-06 19:49 UTC | 2h 51m |
| RYR4YT | Ryanair | Vienna International Airport (LOWW) | Valbrembo Airport (LILV) | 2026-06-06 18:50 UTC | 2026-06-06 19:48 UTC | 58m |
| N275LA |  | Boerne Stage Airfield (K5C1) | 81NM (81NM) | 2026-06-06 17:57 UTC | 2026-06-06 19:42 UTC | 1h 45m |
| RYR51PE | Ryanair | Liverpool John Lennon Airport (EGGP) | Luqa Airport (LMML) | 2026-06-06 16:47 UTC | 2026-06-06 19:41 UTC | 2h 54m |
| DAL1254 | Delta Air Lines | Salt Lake City International Airport (KSLC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-06 18:06 UTC | 2026-06-06 19:40 UTC | 1h 33m |
| ISR888 | ISR | Batumi International Airport (UGSB) | LLBO (LLBO) | 2026-06-06 18:05 UTC | 2026-06-06 19:40 UTC | 1h 35m |
| RHODY34 | RHO | Quonset State Airport (KOQU) | Westover Arb/Metro Airport (KCEF) | 2026-06-06 19:17 UTC | 2026-06-06 19:39 UTC | 22m |
| N410UV |  | Fort Lauderdale Executive Airport (KFXE) | Duda Airstrip (FA69) | 2026-06-06 19:20 UTC | 2026-06-06 19:38 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
