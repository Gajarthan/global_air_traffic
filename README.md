# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_22:44:42_UTC-green)

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

**Latest saved flight:** 2026-05-14 22:44:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-14 22:44:42 UTC

- **82,493** saved flights
- **29,876** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **82,493** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,015,071.8 tonnes** estimated CO2 emissions
- **58,844,741 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3532 |
| 2 | SkyWest Airlines | 3061 |
| 3 | IndiGo | 1800 |
| 4 | EJA | 1548 |
| 5 | American Airlines | 1274 |
| 6 | Southwest Airlines | 1207 |
| 7 | Lufthansa | 1062 |
| 8 | ENY | 1031 |
| 9 | Delta Air Lines | 902 |
| 10 | Vueling | 781 |
| 11 | LATAM Airlines | 748 |
| 12 | AXM | 746 |
| 13 | WIF | 716 |
| 14 | AZU | 650 |
| 15 | All Nippon Airways | 646 |
| 16 | Swiss International | 641 |
| 17 | QLK | 608 |
| 18 | LXJ | 599 |
| 19 | Alaska Airlines | 584 |
| 20 | easyJet | 546 |
| 21 | EJU | 529 |
| 22 | AEE | 524 |
| 23 | Cathay Pacific | 513 |
| 24 | VIV | 492 |
| 25 | Air France | 484 |
| 26 | Japan Airlines | 464 |
| 27 | AXB | 442 |
| 28 | CXK | 431 |
| 29 | MXY | 409 |
| 30 | United Airlines | 408 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 67454 |
| 2 | 🇪🇸 ES | 5838 |
| 3 | 🇮🇳 IN | 5625 |
| 4 | 🇦🇺 AU | 5269 |
| 5 | 🇩🇪 DE | 4615 |
| 6 | 🇧🇷 BR | 4564 |
| 7 | 🇮🇹 IT | 4556 |
| 8 | 🇯🇵 JP | 4171 |
| 9 | 🇨🇦 CA | 4110 |
| 10 | 🇬🇧 GB | 3517 |
| 11 | 🇫🇷 FR | 3274 |
| 12 | 🇨🇴 CO | 2750 |
| 13 | 🇲🇽 MX | 2499 |
| 14 | 🇬🇷 GR | 2399 |
| 15 | 🇳🇴 NO | 2308 |
| 16 | 🇨🇭 CH | 2203 |
| 17 | 🇲🇾 MY | 1874 |
| 18 | 🇿🇦 ZA | 1550 |
| 19 | 🇹🇷 TR | 1464 |
| 20 | 🇳🇿 NZ | 1450 |
| 21 | 🇹🇭 TH | 1438 |
| 22 | 🇵🇱 PL | 1372 |
| 23 | 🇵🇭 PH | 1302 |
| 24 | 🇬🇹 GT | 1256 |
| 25 | 🇰🇷 KR | 1252 |
| 26 | 🇲🇦 MA | 960 |
| 27 | 🇲🇴 MO | 943 |
| 28 | 🇲🇪 ME | 878 |
| 29 | 🇳🇱 NL | 849 |
| 30 | 🇭🇷 HR | 735 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1813 |
| 2 | Tokyo International Airport |  | JP | 1398 |
| 3 | Denver International Airport |  | US | 1387 |
| 4 | Indira Gandhi International Airport |  | IN | 1193 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1172 |
| 6 | Frankfurt am Main International Airport |  | DE | 1072 |
| 7 | Harry Reid International Airport |  | US | 1029 |
| 8 | Zurich Airport |  | CH | 981 |
| 9 | La Aurora Airport |  | GT | 951 |
| 10 | Macau International Airport |  | MO | 943 |
| 11 | Guaymaral Airport |  | CO | 925 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 923 |
| 13 | El Dorado International Airport |  | CO | 886 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 829 |
| 15 | Chicago O'Hare International Airport |  | US | 801 |
| 16 | Madrid Barajas International Airport |  | ES | 753 |
| 17 | Kuala Lumpur International Airport |  | MY | 748 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 718 |
| 19 | Malpensa International Airport |  | IT | 694 |
| 20 | Bengaluru International Airport |  | IN | 691 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 689 |
| 22 | Salt Lake City International Airport |  | US | 680 |
| 23 | Capua Airport |  | IT | 673 |
| 24 | Charles de Gaulle International Airport |  | FR | 646 |
| 25 | Charlotte/Douglas International Airport |  | US | 644 |
| 26 | Congonhas Airport |  | BR | 640 |
| 27 | Tenerife Norte Airport |  | ES | 600 |
| 28 | Daniel K Inouye International Airport |  | US | 597 |
| 29 | Ninoy Aquino International Airport |  | PH | 596 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 587 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 554 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 552 |
| 33 | Barcelona International Airport |  | ES | 552 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 533 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 519 |
| 36 | Don Mueang International Airport |  | TH | 518 |
| 37 | Vitoria/Foronda Airport |  | ES | 517 |
| 38 | Amsterdam Airport Schiphol |  | NL | 512 |
| 39 | O. R. Tambo International Airport |  | ZA | 489 |
| 40 | Calgary International Airport |  | CA | 484 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 385 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 297 | 21m | 244 km | 1,250.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 236 | 24m | 225 km | 915.6 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 220 | 1h 26m | 910 km | 3,452.3 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 219 | 28m | 304 km | 1,148.1 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 212 | 14m | 114 km | 415.8 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 211 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 196 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 188 | 19m | 165 km | 534.8 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 186 | 1h 11m | 770 km | 2,470.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 172 | 26m | 275 km | 815.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 124 | 27m | 152 km | 324.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 123 | 27m | 215 km | 455.5 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 121 | 20m | 147 km | 306.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 118 | 14m | 154 km | 312.7 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 21 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 115 | 23m | 55 km | 109.3 t |
| 22 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 112 | 1h 2m | 695 km | 1,342.5 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 104 | 13m | - | - |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 104 | 18m | 144 km | 258.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N485AE |  | Cochran Airport (K48A) | Perry-Houston County Airport (KPXE) | 2026-05-14 22:34 UTC | 2026-05-14 22:44 UTC | 10m |
| CGXBW | CGX | Pitt Meadows Airport (CYPK) | Pitt Meadows Airport (CYPK) | 2026-05-14 22:32 UTC | 2026-05-14 22:44 UTC | 11m |
| LICHEN9 | LIC | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-05-14 22:27 UTC | 2026-05-14 22:43 UTC | 15m |
| OAI | OAI | Tyagarah Airport (YTYH) | Ballina Byron Gateway Airport (YBNA) | 2026-05-14 22:29 UTC | 2026-05-14 22:40 UTC | 10m |
| TNKR140 | TNK | Huntington Municipal Airport (K69V) | Sanpete County Regional Airport (K41U) | 2026-05-14 22:29 UTC | 2026-05-14 22:39 UTC | 10m |
| N942RM |  | Livingston County/Spencer J Hardy Airport (KOZW) | Livingston County/Spencer J Hardy Airport (KOZW) | 2026-05-14 22:30 UTC | 2026-05-14 22:38 UTC | 8m |
| ES803 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-05-14 21:36 UTC | 2026-05-14 22:36 UTC | 1h 0m |
| N5439K |  | Cartersville Airport (05KY) | Cartersville Airport (05KY) | 2026-05-14 22:33 UTC | 2026-05-14 22:35 UTC | 1m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-05-14 11:54 UTC | 2026-05-14 22:34 UTC | 10h 39m |
| DCM2113 | DCM | Cottonwood Airport (0MT5) | Joe Foss Field (KFSD) | 2026-05-14 21:21 UTC | 2026-05-14 22:32 UTC | 1h 10m |
| XLJ411 | XLJ | City Of Colorado Springs Municipal Airport (KCOS) | Scottsdale Airport (KSDL) | 2026-05-14 21:09 UTC | 2026-05-14 22:28 UTC | 1h 18m |
| N247LT |  | Chicago Midway International Airport (KMDW) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-14 21:44 UTC | 2026-05-14 22:24 UTC | 40m |
| N749DS |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-05-14 22:02 UTC | 2026-05-14 22:21 UTC | 19m |
| N271E |  | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-05-14 21:38 UTC | 2026-05-14 22:21 UTC | 43m |
| VVHV555 | VVH | Mayport Ns (Adm David L Mcdonald Field) Airport (KNRB) | Mayport Ns (Adm David L Mcdonald Field) Airport (KNRB) | 2026-05-14 22:20 UTC | 2026-05-14 22:20 UTC | 0m |
| PAT30 | PAT | Davison Army Air Field (KDAA) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-05-14 21:55 UTC | 2026-05-14 22:19 UTC | 24m |
| N619GV |  | Teterboro Airport (KTEB) | Santa Barbara Municipal Airport (KSBA) | 2026-05-14 17:09 UTC | 2026-05-14 22:17 UTC | 5h 8m |
| N152RE |  | Denton Enterprise Airport (KDTO) | TX39 (TX39) | 2026-05-14 21:23 UTC | 2026-05-14 22:15 UTC | 51m |
| N860MB |  | Falcon Field (KFFZ) | Mesa Gateway Airport (KIWA) | 2026-05-14 22:01 UTC | 2026-05-14 22:07 UTC | 6m |
| SCRCH54 | SCR | North Island Nas (Halsey Field) Airport (KNZY) | Iron Mountain Pumping Plant Airport (72CL) | 2026-05-14 20:31 UTC | 2026-05-14 22:07 UTC | 1h 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
