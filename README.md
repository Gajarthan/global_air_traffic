# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_21:37:10_UTC-green)

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

**Latest saved flight:** 2026-06-14 21:37:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-14 21:37:10 UTC

- **110,834** saved flights
- **38,656** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **110,834** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,355,519.6 tonnes** estimated CO2 emissions
- **78,580,848 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4583 |
| 2 | SkyWest Airlines | 4142 |
| 3 | IndiGo | 2173 |
| 4 | EJA | 2146 |
| 5 | American Airlines | 1748 |
| 6 | Southwest Airlines | 1658 |
| 7 | ENY | 1379 |
| 8 | Delta Air Lines | 1310 |
| 9 | Lufthansa | 1255 |
| 10 | Vueling | 1020 |
| 11 | LATAM Airlines | 980 |
| 12 | WIF | 978 |
| 13 | AXM | 933 |
| 14 | AZU | 917 |
| 15 | LXJ | 845 |
| 16 | Swiss International | 795 |
| 17 | All Nippon Airways | 769 |
| 18 | Alaska Airlines | 753 |
| 19 | QLK | 726 |
| 20 | easyJet | 714 |
| 21 | EJU | 706 |
| 22 | Cathay Pacific | 658 |
| 23 | AEE | 628 |
| 24 | VIV | 622 |
| 25 | Air France | 621 |
| 26 | United Airlines | 614 |
| 27 | MXY | 593 |
| 28 | CXK | 578 |
| 29 | AXB | 546 |
| 30 | Japan Airlines | 542 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 93244 |
| 2 | 🇪🇸 ES | 7613 |
| 3 | 🇮🇳 IN | 6852 |
| 4 | 🇦🇺 AU | 6569 |
| 5 | 🇧🇷 BR | 6120 |
| 6 | 🇮🇹 IT | 5980 |
| 7 | 🇩🇪 DE | 5939 |
| 8 | 🇨🇦 CA | 5809 |
| 9 | 🇯🇵 JP | 5015 |
| 10 | 🇬🇧 GB | 4753 |
| 11 | 🇫🇷 FR | 4436 |
| 12 | 🇨🇴 CO | 3773 |
| 13 | 🇲🇽 MX | 3290 |
| 14 | 🇬🇷 GR | 3157 |
| 15 | 🇳🇴 NO | 3069 |
| 16 | 🇨🇭 CH | 2834 |
| 17 | 🇲🇾 MY | 2410 |
| 18 | 🇹🇷 TR | 2198 |
| 19 | 🇿🇦 ZA | 1887 |
| 20 | 🇰🇷 KR | 1845 |
| 21 | 🇹🇭 TH | 1826 |
| 22 | 🇵🇱 PL | 1822 |
| 23 | 🇳🇿 NZ | 1807 |
| 24 | 🇵🇭 PH | 1611 |
| 25 | 🇬🇹 GT | 1583 |
| 26 | 🇲🇦 MA | 1220 |
| 27 | 🇲🇴 MO | 1150 |
| 28 | 🇲🇪 ME | 1087 |
| 29 | 🇳🇱 NL | 1084 |
| 30 | 🇭🇷 HR | 965 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2364 |
| 2 | Denver International Airport |  | US | 1875 |
| 3 | Tokyo International Airport |  | JP | 1661 |
| 4 | Indira Gandhi International Airport |  | IN | 1491 |
| 5 | Guaymaral Airport |  | CO | 1405 |
| 6 | Harry Reid International Airport |  | US | 1399 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1380 |
| 8 | Zurich Airport |  | CH | 1246 |
| 9 | Frankfurt am Main International Airport |  | DE | 1229 |
| 10 | La Aurora Airport |  | GT | 1218 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1191 |
| 12 | Macau International Airport |  | MO | 1150 |
| 13 | El Dorado International Airport |  | CO | 1134 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1110 |
| 15 | Chicago O'Hare International Airport |  | US | 1098 |
| 16 | Madrid Barajas International Airport |  | ES | 969 |
| 17 | Capua Airport |  | IT | 963 |
| 18 | Kuala Lumpur International Airport |  | MY | 940 |
| 19 | Salt Lake City International Airport |  | US | 939 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 934 |
| 21 | Charlotte/Douglas International Airport |  | US | 852 |
| 22 | Congonhas Airport |  | BR | 852 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 833 |
| 24 | Charles de Gaulle International Airport |  | FR | 832 |
| 25 | Bengaluru International Airport |  | IN | 828 |
| 26 | Malpensa International Airport |  | IT | 810 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 754 |
| 28 | Ninoy Aquino International Airport |  | PH | 742 |
| 29 | Daniel K Inouye International Airport |  | US | 736 |
| 30 | Tenerife Norte Airport |  | ES | 731 |
| 31 | Barcelona International Airport |  | ES | 727 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 724 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 710 |
| 34 | Don Mueang International Airport |  | TH | 667 |
| 35 | Amsterdam Airport Schiphol |  | NL | 667 |
| 36 | Vitoria/Foronda Airport |  | ES | 659 |
| 37 | Calgary International Airport |  | CA | 655 |
| 38 | Seattle-Tacoma International Airport |  | US | 635 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 634 |
| 40 | Viracopos International Airport |  | BR | 625 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 583 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 404 | 21m | 244 km | 1,701.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 295 | 24m | 225 km | 1,144.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 286 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 271 | 1h 25m | 910 km | 4,252.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 260 | 1h 10m | 770 km | 3,453.9 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 224 | 19m | 165 km | 637.2 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 221 | 26m | 275 km | 1,047.2 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 165 | 20m | 99 km | 282.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 161 | 27m | 215 km | 596.3 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 161 | 22m | 55 km | 153.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 157 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 152 | 27m | 152 km | 397.2 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 149 | 31m | 369 km | 948.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 147 | 44m | 452 km | 1,145.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 140 | 44m | 241 km | 581.5 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 133 | 1h 1m | 695 km | 1,594.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 132 | 1h 39m | 1,156 km | 2,633.4 t |
| 28 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 124 | 24m | 223 km | 477.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 124 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N94MN |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-06-14 19:49 UTC | 2026-06-14 21:37 UTC | 1h 47m |
| N545BC |  | Castle Airport (KMER) | Sacramento Executive Airport (KSAC) | 2026-06-14 20:32 UTC | 2026-06-14 21:30 UTC | 58m |
| N458AM |  | 4IS1 (4IS1) | Frasca Field (KC16) | 2026-06-14 21:05 UTC | 2026-06-14 21:20 UTC | 15m |
| N786MM |  | Teterboro Airport (KTEB) | Harry Reid International Airport (KLAS) | 2026-06-14 15:39 UTC | 2026-06-14 21:18 UTC | 5h 38m |
| N52858 |  | Camarillo Airport (KCMA) | Santa Ynez/Kunkle Field (KIZA) | 2026-06-14 20:35 UTC | 2026-06-14 21:16 UTC | 40m |
| N442WT |  | K7K8 (K7K8) | Wadena Municipal Airport (KADC) | 2026-06-14 20:44 UTC | 2026-06-14 21:15 UTC | 30m |
| JBU1500 | JetBlue | Daytona Beach International Airport (KDAB) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-14 18:41 UTC | 2026-06-14 21:12 UTC | 2h 31m |
| N99DQ |  | Republic Airport (KFRG) | Francis S Gabreski Airport (KFOK) | 2026-06-14 20:38 UTC | 2026-06-14 21:10 UTC | 32m |
| N7925M |  | KWSD (KWSD) | KWSD (KWSD) | 2026-06-14 20:42 UTC | 2026-06-14 21:07 UTC | 24m |
| KAP328 | KAP | MA72 (MA72) | Norwood Memorial Airport (KOWD) | 2026-06-14 20:39 UTC | 2026-06-14 21:06 UTC | 26m |
| UAL1173 | United Airlines | Luis Munoz Marin International Airport (TJSJ) | Newark Liberty International Airport (KEWR) | 2026-06-14 17:31 UTC | 2026-06-14 21:01 UTC | 3h 29m |
| N223AL |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-06-14 20:11 UTC | 2026-06-14 21:00 UTC | 49m |
| N35HF |  | Newark Liberty International Airport (KEWR) | Francis S Gabreski Airport (KFOK) | 2026-06-14 20:17 UTC | 2026-06-14 20:54 UTC | 37m |
| EJA766 | EJA | John Wayne/Orange County Airport (KSNA) | Carson City Airport (KCXP) | 2026-06-14 19:54 UTC | 2026-06-14 20:53 UTC | 59m |
| TKR181 | TKR | Chico Regional Airport (KCIC) | Susanville Municipal Airport (KSVE) | 2026-06-14 20:40 UTC | 2026-06-14 20:53 UTC | 12m |
| MNL86 | MNL | Monterey Regional Airport (KMRY) | Truckee-Tahoe Airport (KTRK) | 2026-06-14 20:11 UTC | 2026-06-14 20:53 UTC | 42m |
| XBNLT | XBN | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-06-14 20:28 UTC | 2026-06-14 20:51 UTC | 22m |
| N41101 |  | Denali Airport (AK06) | Summit Airport (PAST) | 2026-06-14 20:29 UTC | 2026-06-14 20:50 UTC | 21m |
| N974CS |  | Mc Kinley Ntl Park Airport (PAIN) | Summit Airport (PAST) | 2026-06-14 20:29 UTC | 2026-06-14 20:49 UTC | 19m |
| N9161C |  | Evergreen Sky Ranch Airport (51WA) | Renton Municipal Airport (KRNT) | 2026-06-14 20:32 UTC | 2026-06-14 20:49 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
