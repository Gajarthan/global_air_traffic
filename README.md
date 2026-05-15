# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_23:27:15_UTC-green)

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

**Latest saved flight:** 2026-05-15 23:27:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-15 23:27:15 UTC

- **83,967** saved flights
- **30,318** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **83,967** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,033,079.1 tonnes** estimated CO2 emissions
- **59,888,644 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3595 |
| 2 | SkyWest Airlines | 3121 |
| 3 | IndiGo | 1809 |
| 4 | EJA | 1585 |
| 5 | American Airlines | 1294 |
| 6 | Southwest Airlines | 1232 |
| 7 | Lufthansa | 1069 |
| 8 | ENY | 1051 |
| 9 | Delta Air Lines | 921 |
| 10 | Vueling | 795 |
| 11 | LATAM Airlines | 760 |
| 12 | AXM | 751 |
| 13 | WIF | 726 |
| 14 | AZU | 659 |
| 15 | All Nippon Airways | 652 |
| 16 | Swiss International | 648 |
| 17 | LXJ | 617 |
| 18 | QLK | 615 |
| 19 | Alaska Airlines | 593 |
| 20 | easyJet | 551 |
| 21 | EJU | 534 |
| 22 | AEE | 529 |
| 23 | Cathay Pacific | 525 |
| 24 | VIV | 503 |
| 25 | Air France | 490 |
| 26 | Japan Airlines | 468 |
| 27 | CXK | 446 |
| 28 | AXB | 444 |
| 29 | MXY | 420 |
| 30 | United Airlines | 413 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 68941 |
| 2 | 🇪🇸 ES | 5936 |
| 3 | 🇮🇳 IN | 5659 |
| 4 | 🇦🇺 AU | 5336 |
| 5 | 🇩🇪 DE | 4667 |
| 6 | 🇮🇹 IT | 4633 |
| 7 | 🇧🇷 BR | 4629 |
| 8 | 🇯🇵 JP | 4197 |
| 9 | 🇨🇦 CA | 4196 |
| 10 | 🇬🇧 GB | 3571 |
| 11 | 🇫🇷 FR | 3323 |
| 12 | 🇨🇴 CO | 2815 |
| 13 | 🇲🇽 MX | 2556 |
| 14 | 🇬🇷 GR | 2429 |
| 15 | 🇳🇴 NO | 2334 |
| 16 | 🇨🇭 CH | 2218 |
| 17 | 🇲🇾 MY | 1890 |
| 18 | 🇿🇦 ZA | 1574 |
| 19 | 🇹🇷 TR | 1490 |
| 20 | 🇳🇿 NZ | 1475 |
| 21 | 🇹🇭 TH | 1453 |
| 22 | 🇵🇱 PL | 1393 |
| 23 | 🇵🇭 PH | 1310 |
| 24 | 🇰🇷 KR | 1280 |
| 25 | 🇬🇹 GT | 1272 |
| 26 | 🇲🇦 MA | 976 |
| 27 | 🇲🇴 MO | 963 |
| 28 | 🇲🇪 ME | 886 |
| 29 | 🇳🇱 NL | 860 |
| 30 | 🇭🇷 HR | 752 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1844 |
| 2 | Denver International Airport |  | US | 1415 |
| 3 | Tokyo International Airport |  | JP | 1407 |
| 4 | Indira Gandhi International Airport |  | IN | 1203 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1179 |
| 6 | Frankfurt am Main International Airport |  | DE | 1081 |
| 7 | Harry Reid International Airport |  | US | 1049 |
| 8 | Zurich Airport |  | CH | 994 |
| 9 | La Aurora Airport |  | GT | 965 |
| 10 | Macau International Airport |  | MO | 963 |
| 11 | Guaymaral Airport |  | CO | 948 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 937 |
| 13 | El Dorado International Airport |  | CO | 906 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 844 |
| 15 | Chicago O'Hare International Airport |  | US | 815 |
| 16 | Madrid Barajas International Airport |  | ES | 765 |
| 17 | Kuala Lumpur International Airport |  | MY | 751 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 727 |
| 19 | Salt Lake City International Airport |  | US | 700 |
| 20 | Malpensa International Airport |  | IT | 700 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 699 |
| 22 | Bengaluru International Airport |  | IN | 695 |
| 23 | Capua Airport |  | IT | 683 |
| 24 | Charlotte/Douglas International Airport |  | US | 654 |
| 25 | Charles de Gaulle International Airport |  | FR | 654 |
| 26 | Congonhas Airport |  | BR | 654 |
| 27 | Daniel K Inouye International Airport |  | US | 606 |
| 28 | Tenerife Norte Airport |  | ES | 606 |
| 29 | Ninoy Aquino International Airport |  | PH | 599 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 589 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 567 |
| 32 | Barcelona International Airport |  | ES | 562 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 561 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 540 |
| 35 | Vitoria/Foronda Airport |  | ES | 531 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 526 |
| 37 | Don Mueang International Airport |  | TH | 523 |
| 38 | Amsterdam Airport Schiphol |  | NL | 521 |
| 39 | O. R. Tambo International Airport |  | ZA | 494 |
| 40 | Calgary International Airport |  | CA | 492 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 393 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 304 | 21m | 244 km | 1,280.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 274 | 1h 8m | 706 km | 3,336.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 237 | 24m | 225 km | 919.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 222 | 28m | 304 km | 1,163.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 221 | 1h 26m | 910 km | 3,468.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 216 | 14m | 114 km | 423.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 215 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 197 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 189 | 19m | 165 km | 537.6 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 188 | 1h 11m | 770 km | 2,497.4 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 175 | 26m | 275 km | 829.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 143 | 20m | 99 km | 244.9 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 139 | 44m | 452 km | 1,083.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 129 | 31m | 369 km | 821.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 126 | 27m | 152 km | 329.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 125 | 27m | 215 km | 462.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 123 | 20m | 147 km | 311.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 119 | 14m | 154 km | 315.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 119 | 23m | 55 km | 113.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 118 | 20m | 250 km | 509.7 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 107 | 13m | - | - |
| 27 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 106 | 18m | 144 km | 263.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 101 | 1h 18m | 961 km | 1,674.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| THY6205 | Turkish Airlines | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-05-15 10:04 UTC | 2026-05-15 23:27 UTC | 13h 23m |
| KYW | KYW | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-05-15 23:01 UTC | 2026-05-15 23:20 UTC | 18m |
| BRG682 | BRG | Noatak Airport (PAWN) | Kivalina Airport (PAVL) | 2026-05-15 22:52 UTC | 2026-05-15 23:11 UTC | 18m |
| N855AV |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-05-15 22:49 UTC | 2026-05-15 23:08 UTC | 18m |
| OAI | OAI | Tyagarah Airport (YTYH) | Ballina Byron Gateway Airport (YBNA) | 2026-05-15 22:57 UTC | 2026-05-15 23:07 UTC | 10m |
| N232JS |  | Aurora State Airport (KUAO) | Centennial Airport (KAPA) | 2026-05-15 21:04 UTC | 2026-05-15 23:06 UTC | 2h 2m |
| N807GK |  | Buchanan Field (KCCR) | Buchanan Field (KCCR) | 2026-05-15 20:45 UTC | 2026-05-15 23:02 UTC | 2h 16m |
|  |  | Manapouri Airport (NZMO) | Manapouri Airport (NZMO) | 2026-05-15 22:56 UTC | 2026-05-15 22:56 UTC | 0m |
| N4397Q |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-05-15 22:42 UTC | 2026-05-15 22:54 UTC | 11m |
| MAX210 | MAX | Billy Bishop Toronto City Airport (CYTZ) | South River/Sundridge Airport & Float Plane Base (CPE6) | 2026-05-15 22:10 UTC | 2026-05-15 22:51 UTC | 41m |
| N917JG |  | Norman Y Mineta San Jose International Airport (KSJC) | Riverside Airport (KRAL) | 2026-05-15 21:34 UTC | 2026-05-15 22:51 UTC | 1h 16m |
| N455PC |  | Scottsdale Airport (KSDL) | Carson City Airport (KCXP) | 2026-05-15 19:31 UTC | 2026-05-15 22:50 UTC | 3h 19m |
| N7797R |  | Pine Island Airport (7NC2) | First Flight Airport (KFFA) | 2026-05-15 22:11 UTC | 2026-05-15 22:50 UTC | 39m |
| QFA6150 | Qantas | Melbourne International Airport (YMML) | Avalon Airport (YMAV) | 2026-05-15 22:35 UTC | 2026-05-15 22:50 UTC | 14m |
| WAH | WAH | Beluga Airport (PABG) | Nikolai Creek Airport (9AK3) | 2026-05-15 22:36 UTC | 2026-05-15 22:45 UTC | 9m |
| CGVFG | CGV | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-05-15 22:11 UTC | 2026-05-15 22:41 UTC | 30m |
| ASP642 | ASP | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Rouyn-Noranda Airport (CYUY) | 2026-05-15 21:53 UTC | 2026-05-15 22:40 UTC | 47m |
| VIV7434 | VIV | Abraham Gonzalez International Airport (MMCS) | Atizapan De Zaragoza Airport (MMJC) | 2026-05-15 20:44 UTC | 2026-05-15 22:40 UTC | 1h 56m |
| SWA3871 | Southwest Airlines | John Wayne/Orange County Airport (KSNA) | Harry Reid International Airport (KLAS) | 2026-05-15 21:47 UTC | 2026-05-15 22:36 UTC | 49m |
| SNJ91 | SNJ | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-05-15 21:40 UTC | 2026-05-15 22:36 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
