# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_20:32:07_UTC-green)

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

**Latest saved flight:** 2026-05-15 20:32:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-15 20:32:07 UTC

- **83,613** saved flights
- **30,224** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **83,613** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,028,800.1 tonnes** estimated CO2 emissions
- **59,640,584 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3578 |
| 2 | SkyWest Airlines | 3096 |
| 3 | IndiGo | 1809 |
| 4 | EJA | 1573 |
| 5 | American Airlines | 1288 |
| 6 | Southwest Airlines | 1224 |
| 7 | Lufthansa | 1069 |
| 8 | ENY | 1042 |
| 9 | Delta Air Lines | 914 |
| 10 | Vueling | 793 |
| 11 | LATAM Airlines | 755 |
| 12 | AXM | 751 |
| 13 | WIF | 726 |
| 14 | AZU | 657 |
| 15 | All Nippon Airways | 652 |
| 16 | Swiss International | 648 |
| 17 | QLK | 615 |
| 18 | LXJ | 612 |
| 19 | Alaska Airlines | 590 |
| 20 | easyJet | 548 |
| 21 | EJU | 534 |
| 22 | AEE | 529 |
| 23 | Cathay Pacific | 519 |
| 24 | VIV | 500 |
| 25 | Air France | 490 |
| 26 | Japan Airlines | 468 |
| 27 | AXB | 444 |
| 28 | CXK | 442 |
| 29 | MXY | 419 |
| 30 | United Airlines | 413 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 68515 |
| 2 | 🇪🇸 ES | 5925 |
| 3 | 🇮🇳 IN | 5658 |
| 4 | 🇦🇺 AU | 5324 |
| 5 | 🇩🇪 DE | 4664 |
| 6 | 🇮🇹 IT | 4619 |
| 7 | 🇧🇷 BR | 4610 |
| 8 | 🇯🇵 JP | 4195 |
| 9 | 🇨🇦 CA | 4161 |
| 10 | 🇬🇧 GB | 3560 |
| 11 | 🇫🇷 FR | 3321 |
| 12 | 🇨🇴 CO | 2788 |
| 13 | 🇲🇽 MX | 2542 |
| 14 | 🇬🇷 GR | 2426 |
| 15 | 🇳🇴 NO | 2332 |
| 16 | 🇨🇭 CH | 2217 |
| 17 | 🇲🇾 MY | 1889 |
| 18 | 🇿🇦 ZA | 1574 |
| 19 | 🇹🇷 TR | 1483 |
| 20 | 🇳🇿 NZ | 1463 |
| 21 | 🇹🇭 TH | 1453 |
| 22 | 🇵🇱 PL | 1391 |
| 23 | 🇵🇭 PH | 1308 |
| 24 | 🇰🇷 KR | 1272 |
| 25 | 🇬🇹 GT | 1268 |
| 26 | 🇲🇦 MA | 971 |
| 27 | 🇲🇴 MO | 959 |
| 28 | 🇲🇪 ME | 885 |
| 29 | 🇳🇱 NL | 858 |
| 30 | 🇭🇷 HR | 750 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1834 |
| 2 | Denver International Airport |  | US | 1406 |
| 3 | Tokyo International Airport |  | JP | 1406 |
| 4 | Indira Gandhi International Airport |  | IN | 1202 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1179 |
| 6 | Frankfurt am Main International Airport |  | DE | 1081 |
| 7 | Harry Reid International Airport |  | US | 1041 |
| 8 | Zurich Airport |  | CH | 993 |
| 9 | La Aurora Airport |  | GT | 962 |
| 10 | Macau International Airport |  | MO | 959 |
| 11 | Guaymaral Airport |  | CO | 943 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 929 |
| 13 | El Dorado International Airport |  | CO | 896 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 839 |
| 15 | Chicago O'Hare International Airport |  | US | 811 |
| 16 | Madrid Barajas International Airport |  | ES | 763 |
| 17 | Kuala Lumpur International Airport |  | MY | 751 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 724 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 699 |
| 20 | Salt Lake City International Airport |  | US | 697 |
| 21 | Malpensa International Airport |  | IT | 697 |
| 22 | Bengaluru International Airport |  | IN | 695 |
| 23 | Capua Airport |  | IT | 679 |
| 24 | Charles de Gaulle International Airport |  | FR | 654 |
| 25 | Charlotte/Douglas International Airport |  | US | 651 |
| 26 | Congonhas Airport |  | BR | 649 |
| 27 | Tenerife Norte Airport |  | ES | 605 |
| 28 | Daniel K Inouye International Airport |  | US | 604 |
| 29 | Ninoy Aquino International Airport |  | PH | 598 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 589 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 564 |
| 32 | Barcelona International Airport |  | ES | 560 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 558 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 539 |
| 35 | Vitoria/Foronda Airport |  | ES | 531 |
| 36 | Don Mueang International Airport |  | TH | 523 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 522 |
| 38 | Amsterdam Airport Schiphol |  | NL | 519 |
| 39 | O. R. Tambo International Airport |  | ZA | 494 |
| 40 | Calgary International Airport |  | CA | 490 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 393 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 302 | 21m | 244 km | 1,271.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 237 | 24m | 225 km | 919.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 222 | 28m | 304 km | 1,163.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 221 | 1h 26m | 910 km | 3,468.0 t |
| 7 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 215 | 9m | - | - |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 213 | 14m | 114 km | 417.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 197 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 189 | 19m | 165 km | 537.6 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 188 | 1h 11m | 770 km | 2,497.4 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 175 | 26m | 275 km | 829.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 139 | 44m | 452 km | 1,083.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 125 | 27m | 215 km | 462.9 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 125 | 27m | 152 km | 326.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 123 | 20m | 147 km | 311.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 119 | 14m | 154 km | 315.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 118 | 23m | 55 km | 112.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 118 | 20m | 250 km | 509.7 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 107 | 13m | - | - |
| 27 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 106 | 18m | 144 km | 263.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 100 | 1h 41m | 1,156 km | 1,995.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GEL1911 | GEL | Tbilisi International Airport (UGTB) | Macau International Airport (VMMC) | 2026-05-15 12:28 UTC | 2026-05-15 20:32 UTC | 8h 3m |
| WF11 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-05-15 18:14 UTC | 2026-05-15 20:31 UTC | 2h 16m |
| N7308G |  | Blairstown Airport (K1N7) | Monmouth Executive Airport (KBLM) | 2026-05-15 19:55 UTC | 2026-05-15 20:30 UTC | 35m |
| N113SG |  | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | Big Bear City Airport (KL35) | 2026-05-15 19:59 UTC | 2026-05-15 20:28 UTC | 29m |
| N14WG |  | Livermore Municipal Airport (KLVK) | Sacramento Mather Airport (KMHR) | 2026-05-15 19:49 UTC | 2026-05-15 20:28 UTC | 39m |
| N24189 |  | Santa Fe Regional Airport (KSAF) | Santa Fe Regional Airport (KSAF) | 2026-05-15 20:07 UTC | 2026-05-15 20:28 UTC | 21m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Macau International Airport (VMMC) | 2026-05-15 06:02 UTC | 2026-05-15 20:26 UTC | 14h 24m |
| N4723P |  | Denton Enterprise Airport (KDTO) | Flying D Ranch Airport (TX94) | 2026-05-15 20:05 UTC | 2026-05-15 20:26 UTC | 21m |
| N224JA |  | KU77 (KU77) | KU77 (KU77) | 2026-05-15 20:10 UTC | 2026-05-15 20:25 UTC | 14m |
| N950RH |  | Jennrich Field (MN45) | Jennrich Field (MN45) | 2026-05-15 19:50 UTC | 2026-05-15 20:24 UTC | 33m |
| N922AZ |  | Regeneration Airport (5AZ9) | Phoenix Sky Harbor International Airport (KPHX) | 2026-05-15 19:53 UTC | 2026-05-15 20:17 UTC | 24m |
| SW12 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-05-15 18:15 UTC | 2026-05-15 20:15 UTC | 2h 0m |
| ETH3753 | Ethiopian Airlines | Madrid Barajas International Airport (LEMD) | Macau International Airport (VMMC) | 2026-05-15 08:29 UTC | 2026-05-15 20:11 UTC | 11h 42m |
| N1330N |  | Centennial Airport (KAPA) | Limon Municipal Airport (KLIC) | 2026-05-15 19:35 UTC | 2026-05-15 20:11 UTC | 35m |
| N707FB |  | San Martin Airport (KE16) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-15 19:59 UTC | 2026-05-15 20:10 UTC | 11m |
| N377KH |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-05-15 19:46 UTC | 2026-05-15 20:09 UTC | 23m |
| N299MK |  | Salt Lake City International Airport (KSLC) | Morgan County Airport (K42U) | 2026-05-15 19:57 UTC | 2026-05-15 20:05 UTC | 7m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-05-15 08:38 UTC | 2026-05-15 20:03 UTC | 11h 24m |
| N773SP |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-15 19:50 UTC | 2026-05-15 20:02 UTC | 11m |
| BOX556 | BOX | Bengaluru International Airport (VOBL) | Macau International Airport (VMMC) | 2026-05-15 15:26 UTC | 2026-05-15 20:01 UTC | 4h 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
