# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_17:03:35_UTC-green)

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

**Latest saved flight:** 2026-05-18 17:03:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-18 17:03:35 UTC

- **87,252** saved flights
- **31,229** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **87,252** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,080,077.7 tonnes** estimated CO2 emissions
- **62,613,198 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3736 |
| 2 | SkyWest Airlines | 3229 |
| 3 | IndiGo | 1868 |
| 4 | EJA | 1649 |
| 5 | American Airlines | 1339 |
| 6 | Southwest Airlines | 1274 |
| 7 | Lufthansa | 1102 |
| 8 | ENY | 1084 |
| 9 | Delta Air Lines | 958 |
| 10 | Vueling | 829 |
| 11 | LATAM Airlines | 788 |
| 12 | AXM | 782 |
| 13 | WIF | 746 |
| 14 | AZU | 688 |
| 15 | Swiss International | 674 |
| 16 | All Nippon Airways | 667 |
| 17 | LXJ | 642 |
| 18 | QLK | 626 |
| 19 | Alaska Airlines | 619 |
| 20 | easyJet | 575 |
| 21 | EJU | 562 |
| 22 | Cathay Pacific | 555 |
| 23 | AEE | 545 |
| 24 | VIV | 524 |
| 25 | Air France | 510 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 460 |
| 28 | AXB | 456 |
| 29 | MXY | 444 |
| 30 | AIQ | 427 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 71535 |
| 2 | 🇪🇸 ES | 6177 |
| 3 | 🇮🇳 IN | 5848 |
| 4 | 🇦🇺 AU | 5486 |
| 5 | 🇩🇪 DE | 4861 |
| 6 | 🇮🇹 IT | 4836 |
| 7 | 🇧🇷 BR | 4794 |
| 8 | 🇨🇦 CA | 4336 |
| 9 | 🇯🇵 JP | 4323 |
| 10 | 🇬🇧 GB | 3723 |
| 11 | 🇫🇷 FR | 3487 |
| 12 | 🇨🇴 CO | 2947 |
| 13 | 🇲🇽 MX | 2709 |
| 14 | 🇬🇷 GR | 2536 |
| 15 | 🇳🇴 NO | 2412 |
| 16 | 🇨🇭 CH | 2312 |
| 17 | 🇲🇾 MY | 1964 |
| 18 | 🇿🇦 ZA | 1621 |
| 19 | 🇹🇷 TR | 1582 |
| 20 | 🇳🇿 NZ | 1519 |
| 21 | 🇹🇭 TH | 1503 |
| 22 | 🇵🇱 PL | 1450 |
| 23 | 🇰🇷 KR | 1360 |
| 24 | 🇵🇭 PH | 1354 |
| 25 | 🇬🇹 GT | 1315 |
| 26 | 🇲🇴 MO | 1015 |
| 27 | 🇲🇦 MA | 1013 |
| 28 | 🇲🇪 ME | 906 |
| 29 | 🇳🇱 NL | 892 |
| 30 | 🇭🇷 HR | 785 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1915 |
| 2 | Denver International Airport |  | US | 1460 |
| 3 | Tokyo International Airport |  | JP | 1444 |
| 4 | Indira Gandhi International Airport |  | IN | 1257 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1205 |
| 6 | Harry Reid International Airport |  | US | 1111 |
| 7 | Frankfurt am Main International Airport |  | DE | 1111 |
| 8 | Zurich Airport |  | CH | 1040 |
| 9 | Macau International Airport |  | MO | 1015 |
| 10 | La Aurora Airport |  | GT | 1000 |
| 11 | Guaymaral Airport |  | CO | 997 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 967 |
| 13 | El Dorado International Airport |  | CO | 944 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 880 |
| 15 | Chicago O'Hare International Airport |  | US | 844 |
| 16 | Madrid Barajas International Airport |  | ES | 793 |
| 17 | Kuala Lumpur International Airport |  | MY | 780 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 749 |
| 19 | Capua Airport |  | IT | 735 |
| 20 | Salt Lake City International Airport |  | US | 730 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 717 |
| 22 | Malpensa International Airport |  | IT | 714 |
| 23 | Bengaluru International Airport |  | IN | 707 |
| 24 | Charles de Gaulle International Airport |  | FR | 679 |
| 25 | Charlotte/Douglas International Airport |  | US | 677 |
| 26 | Congonhas Airport |  | BR | 671 |
| 27 | Daniel K Inouye International Airport |  | US | 640 |
| 28 | Tenerife Norte Airport |  | ES | 640 |
| 29 | Ninoy Aquino International Airport |  | PH | 620 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 596 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 32 | Barcelona International Airport |  | ES | 587 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 580 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 560 |
| 35 | Vitoria/Foronda Airport |  | ES | 555 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 550 |
| 37 | Amsterdam Airport Schiphol |  | NL | 546 |
| 38 | Don Mueang International Airport |  | TH | 545 |
| 39 | Calgary International Airport |  | CA | 513 |
| 40 | O. R. Tambo International Airport |  | ZA | 510 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 409 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 325 | 21m | 244 km | 1,368.5 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 230 | 1h 26m | 910 km | 3,609.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 224 | 14m | 114 km | 439.3 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 223 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 200 | 1h 10m | 770 km | 2,656.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 193 | 19m | 165 km | 549.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 182 | 26m | 275 km | 862.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 126 | 20m | 147 km | 318.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 124 | 14m | 154 km | 328.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 123 | 23m | 55 km | 116.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 112 | 18m | 144 km | 278.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 111 | 1h 42m | 1,423 km | 2,724.1 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 111 | 13m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 106 | 1h 52m | 1,304 km | 2,384.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N252SP |  | Van Nuys Airport (KVNY) | Camarillo Airport (KCMA) | 2026-05-18 16:36 UTC | 2026-05-18 17:03 UTC | 27m |
| N867SL |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-05-18 16:46 UTC | 2026-05-18 17:02 UTC | 16m |
| N738NY |  | Lakewood Airport (KN12) | Atlantic City International Airport (KACY) | 2026-05-18 16:21 UTC | 2026-05-18 16:55 UTC | 33m |
| N21022 |  | Pompano Beach Airpark (KPMP) | Pompano Beach Airpark (KPMP) | 2026-05-18 16:32 UTC | 2026-05-18 16:50 UTC | 18m |
| AXEL10 | AXE | El Paso International Airport (KELP) | Wilderness Airport (80OR) | 2026-05-18 14:28 UTC | 2026-05-18 16:49 UTC | 2h 21m |
| N38US |  | Essex County Airport (KCDW) | Lehigh Valley International Airport (KABE) | 2026-05-18 16:20 UTC | 2026-05-18 16:48 UTC | 28m |
| N604MH |  | Harrisburg International Airport (KMDT) | Harrisburg International Airport (KMDT) | 2026-05-18 16:41 UTC | 2026-05-18 16:47 UTC | 5m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-05-18 14:59 UTC | 2026-05-18 16:45 UTC | 1h 45m |
| SPKBK | SPK | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-05-18 16:37 UTC | 2026-05-18 16:41 UTC | 3m |
| JEDDA51 | JED | Pilots Landing Airport (81TE) | J R Ranch Airport (15TA) | 2026-05-18 16:28 UTC | 2026-05-18 16:40 UTC | 11m |
| PAIN11 | PAI | Enix Airport (OK51) | Henderson Farm Airport (35OL) | 2026-05-18 15:48 UTC | 2026-05-18 16:39 UTC | 50m |
| N9010K |  | South Jersey Regional Airport (KVAY) | Ocean County Airport (KMJX) | 2026-05-18 16:22 UTC | 2026-05-18 16:39 UTC | 16m |
| VET560 | VET | Coral Creek Airport (FA54) | Ware Island Airport (01AL) | 2026-05-18 15:24 UTC | 2026-05-18 16:38 UTC | 1h 14m |
| N611AK |  | Centennial Airport (KAPA) | Limon Municipal Airport (KLIC) | 2026-05-18 16:16 UTC | 2026-05-18 16:36 UTC | 20m |
| TJT37DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-05-18 15:14 UTC | 2026-05-18 16:31 UTC | 1h 17m |
| N356DA |  | Appalachee Bluff Riverfront Airpark (67GA) | Barrow County Airport (KWDR) | 2026-05-18 15:55 UTC | 2026-05-18 16:31 UTC | 35m |
| N72HR |  | Kings Port Airport (FD72) | North Perry Airport (KHWO) | 2026-05-18 15:40 UTC | 2026-05-18 16:25 UTC | 45m |
| ASI137 | ASI | Lakeside Airpark (AZ05) | Wickenburg Municipal Airport (KE25) | 2026-05-18 15:39 UTC | 2026-05-18 16:23 UTC | 43m |
| ERU846 | ERU | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-05-18 16:16 UTC | 2026-05-18 16:22 UTC | 5m |
| WUP668 | WUP | Birmingham-Shuttlesworth International Airport (KBHM) | Hinton-Alderson Airport (WV77) | 2026-05-18 15:21 UTC | 2026-05-18 16:22 UTC | 1h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
