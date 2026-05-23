# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_03:54:24_UTC-green)

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

**Latest saved flight:** 2026-05-23 03:54:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-23 03:54:24 UTC

- **92,222** saved flights
- **32,728** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **92,222** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,134,021.8 tonnes** estimated CO2 emissions
- **65,740,396 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3906 |
| 2 | SkyWest Airlines | 3425 |
| 3 | IndiGo | 1919 |
| 4 | EJA | 1750 |
| 5 | American Airlines | 1400 |
| 6 | Southwest Airlines | 1332 |
| 7 | ENY | 1139 |
| 8 | Lufthansa | 1123 |
| 9 | Delta Air Lines | 1012 |
| 10 | Vueling | 877 |
| 11 | LATAM Airlines | 824 |
| 12 | AXM | 810 |
| 13 | WIF | 806 |
| 14 | AZU | 734 |
| 15 | LXJ | 700 |
| 16 | Swiss International | 691 |
| 17 | All Nippon Airways | 686 |
| 18 | QLK | 648 |
| 19 | Alaska Airlines | 647 |
| 20 | easyJet | 603 |
| 21 | EJU | 585 |
| 22 | Cathay Pacific | 581 |
| 23 | AEE | 558 |
| 24 | VIV | 547 |
| 25 | Air France | 540 |
| 26 | Japan Airlines | 486 |
| 27 | CXK | 485 |
| 28 | MXY | 479 |
| 29 | AXB | 468 |
| 30 | AIQ | 443 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 76305 |
| 2 | 🇪🇸 ES | 6492 |
| 3 | 🇮🇳 IN | 6035 |
| 4 | 🇦🇺 AU | 5708 |
| 5 | 🇧🇷 BR | 5050 |
| 6 | 🇩🇪 DE | 5050 |
| 7 | 🇮🇹 IT | 5025 |
| 8 | 🇨🇦 CA | 4662 |
| 9 | 🇯🇵 JP | 4456 |
| 10 | 🇬🇧 GB | 3929 |
| 11 | 🇫🇷 FR | 3711 |
| 12 | 🇨🇴 CO | 3196 |
| 13 | 🇲🇽 MX | 2846 |
| 14 | 🇬🇷 GR | 2627 |
| 15 | 🇳🇴 NO | 2572 |
| 16 | 🇨🇭 CH | 2407 |
| 17 | 🇲🇾 MY | 2041 |
| 18 | 🇹🇷 TR | 1673 |
| 19 | 🇿🇦 ZA | 1667 |
| 20 | 🇳🇿 NZ | 1582 |
| 21 | 🇹🇭 TH | 1552 |
| 22 | 🇵🇱 PL | 1505 |
| 23 | 🇰🇷 KR | 1466 |
| 24 | 🇵🇭 PH | 1404 |
| 25 | 🇬🇹 GT | 1389 |
| 26 | 🇲🇦 MA | 1060 |
| 27 | 🇲🇴 MO | 1036 |
| 28 | 🇳🇱 NL | 927 |
| 29 | 🇲🇪 ME | 925 |
| 30 | 🇭🇷 HR | 830 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2005 |
| 2 | Denver International Airport |  | US | 1553 |
| 3 | Tokyo International Airport |  | JP | 1484 |
| 4 | Indira Gandhi International Airport |  | IN | 1313 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1230 |
| 6 | Harry Reid International Airport |  | US | 1189 |
| 7 | Frankfurt am Main International Airport |  | DE | 1131 |
| 8 | Guaymaral Airport |  | CO | 1107 |
| 9 | Zurich Airport |  | CH | 1079 |
| 10 | La Aurora Airport |  | GT | 1062 |
| 11 | Macau International Airport |  | MO | 1036 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1012 |
| 13 | El Dorado International Airport |  | CO | 1007 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 925 |
| 15 | Chicago O'Hare International Airport |  | US | 883 |
| 16 | Madrid Barajas International Airport |  | ES | 830 |
| 17 | Kuala Lumpur International Airport |  | MY | 809 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 779 |
| 19 | Salt Lake City International Airport |  | US | 776 |
| 20 | Capua Airport |  | IT | 768 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 743 |
| 22 | Malpensa International Airport |  | IT | 734 |
| 23 | Bengaluru International Airport |  | IN | 727 |
| 24 | Charles de Gaulle International Airport |  | FR | 718 |
| 25 | Charlotte/Douglas International Airport |  | US | 707 |
| 26 | Congonhas Airport |  | BR | 703 |
| 27 | Daniel K Inouye International Airport |  | US | 668 |
| 28 | Tenerife Norte Airport |  | ES | 663 |
| 29 | Ninoy Aquino International Airport |  | PH | 643 |
| 30 | Barcelona International Airport |  | ES | 621 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 612 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 601 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 597 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 583 |
| 35 | Vitoria/Foronda Airport |  | ES | 576 |
| 36 | Don Mueang International Airport |  | TH | 570 |
| 37 | Amsterdam Airport Schiphol |  | NL | 568 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 39 | Calgary International Airport |  | CA | 549 |
| 40 | O. R. Tambo International Airport |  | ZA | 528 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 454 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 340 | 21m | 244 km | 1,431.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 251 | 24m | 225 km | 973.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 244 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 239 | 14m | 114 km | 468.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 237 | 1h 26m | 910 km | 3,719.1 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 233 | 28m | 304 km | 1,221.5 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 212 | 1h 10m | 770 km | 2,816.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 200 | 19m | 165 km | 568.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 188 | 26m | 275 km | 890.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 151 | 21m | 99 km | 258.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 139 | 31m | 369 km | 884.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 137 | 27m | 215 km | 507.4 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 133 | 14m | 154 km | 352.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 126 | 20m | 250 km | 544.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 1m | 695 km | 1,426.5 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 119 | 18m | 144 km | 296.0 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 112 | 1h 40m | 1,156 km | 2,234.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N952JA |  | John Wayne/Orange County Airport (KSNA) | Santa Barbara Municipal Airport (KSBA) | 2026-05-23 02:38 UTC | 2026-05-23 03:54 UTC | 1h 16m |
| N110DK |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Rocky Mountain Metro Airport (KBJC) | 2026-05-23 03:18 UTC | 2026-05-23 03:54 UTC | 35m |
| N384CA |  | Logan-Cache Airport (KLGU) | Malad City Airport (KMLD) | 2026-05-23 03:33 UTC | 2026-05-23 03:47 UTC | 13m |
| N818MT |  | Denton Enterprise Airport (KDTO) | Addington Field (4TX8) | 2026-05-23 03:28 UTC | 2026-05-23 03:44 UTC | 15m |
| AAR522 | AAR | London Heathrow Airport (EGLL) | Incheon International Airport (RKSI) | 2026-05-22 15:57 UTC | 2026-05-23 03:35 UTC | 11h 37m |
| ALIFE6 | ALI | Wirth Field (CO06) | Buckley Space Force Base Airport (KBKF) | 2026-05-23 03:00 UTC | 2026-05-23 03:34 UTC | 33m |
| N797GM |  | Oakland San Francisco Bay Airport (KOAK) | Truckee-Tahoe Airport (KTRK) | 2026-05-23 02:59 UTC | 2026-05-23 03:32 UTC | 33m |
| ENT7759 | ENT | Gdańsk Lech Wałęsa Airport (EPGD) | Queen Alia International Airport (OJAI) | 2026-05-23 00:26 UTC | 2026-05-23 03:30 UTC | 3h 4m |
| N565TA |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-05-23 03:09 UTC | 2026-05-23 03:29 UTC | 20m |
| N510PR |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-23 03:05 UTC | 2026-05-23 03:28 UTC | 22m |
| N88765 |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-05-23 03:07 UTC | 2026-05-23 03:27 UTC | 20m |
| WAH | WAH | Kenai Municipal Airport (PAEN) | Nikolai Creek Airport (9AK3) | 2026-05-23 03:12 UTC | 2026-05-23 03:26 UTC | 14m |
| UAE9987 | Emirates | Shaibah Airport (OESB) | Queen Alia International Airport (OJAI) | 2026-05-23 00:31 UTC | 2026-05-23 03:26 UTC | 2h 55m |
| N2YV |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-05-23 03:00 UTC | 2026-05-23 03:21 UTC | 21m |
| SKW4291 | SkyWest Airlines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Webb Lake Airport (MN00) | 2026-05-23 02:52 UTC | 2026-05-23 03:14 UTC | 22m |
| N100BW |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-05-23 02:49 UTC | 2026-05-23 03:08 UTC | 19m |
| LLR821 | LLR | Indira Gandhi International Airport (VIDP) | Shimla Airport (VISM) | 2026-05-23 02:27 UTC | 2026-05-23 03:08 UTC | 40m |
| SN898 |  | Winnipeg James Armstrong Richardson International Airport (CYWG) | Matheson Island Airport (CJT2) | 2026-05-23 02:36 UTC | 2026-05-23 03:05 UTC | 29m |
| N79US |  | Logan-Cache Airport (KLGU) | Simko Field (1ID9) | 2026-05-23 02:12 UTC | 2026-05-23 03:01 UTC | 48m |
| N858C |  | Mc Clellan-Palomar Airport (KCRQ) | Borrego Valley Airport (KL08) | 2026-05-23 02:42 UTC | 2026-05-23 02:59 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
