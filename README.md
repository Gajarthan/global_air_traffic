# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_08:13:54_UTC-green)

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

**Latest saved flight:** 2026-05-10 08:13:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-10 08:13:54 UTC

- **76,665** saved flights
- **28,081** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **76,665** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **949,299.7 tonnes** estimated CO2 emissions
- **55,031,865 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3287 |
| 2 | SkyWest Airlines | 2847 |
| 3 | IndiGo | 1706 |
| 4 | EJA | 1410 |
| 5 | American Airlines | 1201 |
| 6 | Southwest Airlines | 1118 |
| 7 | Lufthansa | 998 |
| 8 | ENY | 961 |
| 9 | Delta Air Lines | 793 |
| 10 | Vueling | 736 |
| 11 | AXM | 718 |
| 12 | LATAM Airlines | 708 |
| 13 | WIF | 655 |
| 14 | All Nippon Airways | 619 |
| 15 | AZU | 611 |
| 16 | QLK | 590 |
| 17 | Swiss International | 580 |
| 18 | LXJ | 564 |
| 19 | Alaska Airlines | 541 |
| 20 | easyJet | 504 |
| 21 | Cathay Pacific | 497 |
| 22 | AEE | 496 |
| 23 | EJU | 493 |
| 24 | VIV | 458 |
| 25 | Japan Airlines | 448 |
| 26 | Air France | 444 |
| 27 | AXB | 424 |
| 28 | CXK | 391 |
| 29 | AIQ | 385 |
| 30 | MXY | 376 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 61891 |
| 2 | 🇪🇸 ES | 5480 |
| 3 | 🇮🇳 IN | 5355 |
| 4 | 🇦🇺 AU | 5015 |
| 5 | 🇩🇪 DE | 4314 |
| 6 | 🇧🇷 BR | 4278 |
| 7 | 🇮🇹 IT | 4208 |
| 8 | 🇯🇵 JP | 3993 |
| 9 | 🇨🇦 CA | 3815 |
| 10 | 🇬🇧 GB | 3278 |
| 11 | 🇫🇷 FR | 3029 |
| 12 | 🇨🇴 CO | 2696 |
| 13 | 🇲🇽 MX | 2357 |
| 14 | 🇬🇷 GR | 2258 |
| 15 | 🇳🇴 NO | 2098 |
| 16 | 🇨🇭 CH | 2073 |
| 17 | 🇲🇾 MY | 1790 |
| 18 | 🇿🇦 ZA | 1464 |
| 19 | 🇳🇿 NZ | 1390 |
| 20 | 🇹🇷 TR | 1376 |
| 21 | 🇹🇭 TH | 1374 |
| 22 | 🇵🇱 PL | 1277 |
| 23 | 🇵🇭 PH | 1234 |
| 24 | 🇰🇷 KR | 1204 |
| 25 | 🇬🇹 GT | 1199 |
| 26 | 🇲🇦 MA | 904 |
| 27 | 🇲🇴 MO | 904 |
| 28 | 🇲🇪 ME | 817 |
| 29 | 🇳🇱 NL | 798 |
| 30 | 🇭🇷 HR | 660 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1707 |
| 2 | Tokyo International Airport |  | JP | 1341 |
| 3 | Denver International Airport |  | US | 1287 |
| 4 | Indira Gandhi International Airport |  | IN | 1130 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1107 |
| 6 | Frankfurt am Main International Airport |  | DE | 996 |
| 7 | Harry Reid International Airport |  | US | 953 |
| 8 | Macau International Airport |  | MO | 904 |
| 9 | Zurich Airport |  | CH | 902 |
| 10 | La Aurora Airport |  | GT | 900 |
| 11 | Guaymaral Airport |  | CO | 890 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 768 |
| 14 | Chicago O'Hare International Airport |  | US | 751 |
| 15 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 750 |
| 16 | Kuala Lumpur International Airport |  | MY | 719 |
| 17 | Madrid Barajas International Airport |  | ES | 716 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 681 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 668 |
| 20 | Bengaluru International Airport |  | IN | 664 |
| 21 | Malpensa International Airport |  | IT | 662 |
| 22 | Salt Lake City International Airport |  | US | 628 |
| 23 | Charlotte/Douglas International Airport |  | US | 604 |
| 24 | Congonhas Airport |  | BR | 604 |
| 25 | Capua Airport |  | IT | 599 |
| 26 | Charles de Gaulle International Airport |  | FR | 595 |
| 27 | Tenerife Norte Airport |  | ES | 569 |
| 28 | Ninoy Aquino International Airport |  | PH | 561 |
| 29 | Daniel K Inouye International Airport |  | US | 560 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 549 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 523 |
| 32 | Barcelona International Airport |  | ES | 519 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 517 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 503 |
| 35 | Don Mueang International Airport |  | TH | 487 |
| 36 | Vitoria/Foronda Airport |  | ES | 483 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 480 |
| 38 | Amsterdam Airport Schiphol |  | NL | 479 |
| 39 | O. R. Tambo International Airport |  | ZA | 459 |
| 40 | Calgary International Airport |  | CA | 457 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 370 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 275 | 21m | 244 km | 1,157.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 223 | 24m | 225 km | 865.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 214 | 28m | 304 km | 1,121.8 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 208 | 1h 27m | 910 km | 3,264.0 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 195 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 183 | 19m | 165 km | 520.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 182 | 31m | - | - |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 169 | 1h 12m | 770 km | 2,245.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 165 | 26m | 275 km | 781.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 139 | 20m | 99 km | 238.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 135 | 44m | 452 km | 1,052.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 123 | 31m | 369 km | 782.9 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 114 | 27m | 215 km | 422.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 114 | 20m | 147 km | 288.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 113 | 20m | 250 km | 488.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 110 | 14m | 154 km | 291.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 103 | 1h 2m | 695 km | 1,234.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 102 | 1h 42m | 1,423 km | 2,503.2 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 102 | 57m | 493 km | 867.8 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 100 | 23m | 55 km | 95.0 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 97 | 12m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 95 | 1h 19m | 961 km | 1,574.7 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 95 | 52m | 556 km | 910.7 t |
| 30 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 94 | 18m | 144 km | 233.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TMN24 | TMN | Chek Lap Kok International Airport (VHHH) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-09 23:43 UTC | 2026-05-10 08:13 UTC | 8h 30m |
| N429CF |  | Dallas Executive Airport (KRBD) | Beulah Field (01TX) | 2026-05-10 07:54 UTC | 2026-05-10 08:06 UTC | 12m |
| SIS927 | SIS | Van Nuys Airport (KVNY) | Harry Reid International Airport (KLAS) | 2026-05-10 07:00 UTC | 2026-05-10 08:04 UTC | 1h 3m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-05-10 07:16 UTC | 2026-05-10 08:01 UTC | 45m |
| AIC217 | Air India | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-05-10 06:40 UTC | 2026-05-10 08:00 UTC | 1h 20m |
| CLX4806 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-05-09 21:00 UTC | 2026-05-10 07:57 UTC | 10h 56m |
| QTR818 | Qatar Airways | King Fahd International Airport (OEDF) | Macau International Airport (VMMC) | 2026-05-09 05:56 UTC | 2026-05-10 07:45 UTC | 25h 48m |
| SAS661 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Dingolfing Airport (EDPD) | 2026-05-10 06:13 UTC | 2026-05-10 07:37 UTC | 1h 24m |
| DMDGD | DMD | Eggenfelden Airport (EDME) | Pfarrkirchen Airport (EDNP) | 2026-05-10 07:12 UTC | 2026-05-10 07:34 UTC | 21m |
| VOE3931 | VOE | Francisco de Sá Carneiro Airport (LPPR) | La Morgal Airport (LEMR) | 2026-05-10 06:54 UTC | 2026-05-10 07:27 UTC | 33m |
| DAL1471 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 07:03 UTC | 2026-05-10 07:24 UTC | 21m |
| AAR8707 | AAR | Gimpo International Airport (RKSS) | G 710 Airport (RK6D) | 2026-05-10 06:51 UTC | 2026-05-10 07:18 UTC | 26m |
| ISR889 | ISR | Ben Gurion International Airport (LLBG) | Batumi International Airport (UGSB) | 2026-05-10 05:23 UTC | 2026-05-10 07:17 UTC | 1h 53m |
| CEB508 | CEB | Ninoy Aquino International Airport (RPLL) | RP14 (RP14) | 2026-05-10 06:54 UTC | 2026-05-10 07:17 UTC | 22m |
| EJU31CM | EJU | Paris-Orly Airport (LFPO) | Capua Airport (LIAU) | 2026-05-10 05:33 UTC | 2026-05-10 07:16 UTC | 1h 42m |
| LHX02A | LHX | Madrid Barajas International Airport (LEMD) | Munich International Airport (EDDM) | 2026-05-10 05:17 UTC | 2026-05-10 07:16 UTC | 1h 58m |
| TRA71L | TRA | Eindhoven Airport (EHEH) | Ibiza Airport (LEIB) | 2026-05-10 05:05 UTC | 2026-05-10 07:14 UTC | 2h 9m |
| JJP584 | JJP | Fukuoka Airport (RJFF) | Akeno Airport (RJOE) | 2026-05-10 06:25 UTC | 2026-05-10 07:11 UTC | 46m |
| AIQ3514 | AIQ | Don Mueang International Airport (VTBD) | Nam Phung Dam Airport (VTUZ) | 2026-05-10 06:32 UTC | 2026-05-10 07:11 UTC | 38m |
| APG223 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-05-10 06:46 UTC | 2026-05-10 07:10 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
