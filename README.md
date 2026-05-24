# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_23:48:20_UTC-green)

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

**Latest saved flight:** 2026-05-23 23:48:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-23 23:48:20 UTC

- **93,375** saved flights
- **33,047** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **93,375** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,148,163.7 tonnes** estimated CO2 emissions
- **66,560,213 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3938 |
| 2 | SkyWest Airlines | 3474 |
| 3 | IndiGo | 1936 |
| 4 | EJA | 1771 |
| 5 | American Airlines | 1423 |
| 6 | Southwest Airlines | 1357 |
| 7 | ENY | 1159 |
| 8 | Lufthansa | 1130 |
| 9 | Delta Air Lines | 1026 |
| 10 | Vueling | 886 |
| 11 | LATAM Airlines | 835 |
| 12 | AXM | 819 |
| 13 | WIF | 809 |
| 14 | AZU | 742 |
| 15 | LXJ | 707 |
| 16 | Swiss International | 695 |
| 17 | All Nippon Airways | 691 |
| 18 | Alaska Airlines | 653 |
| 19 | QLK | 648 |
| 20 | easyJet | 610 |
| 21 | EJU | 598 |
| 22 | Cathay Pacific | 581 |
| 23 | AEE | 566 |
| 24 | VIV | 555 |
| 25 | Air France | 546 |
| 26 | CXK | 501 |
| 27 | MXY | 495 |
| 28 | Japan Airlines | 487 |
| 29 | AXB | 473 |
| 30 | AIQ | 449 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 77366 |
| 2 | 🇪🇸 ES | 6541 |
| 3 | 🇮🇳 IN | 6106 |
| 4 | 🇦🇺 AU | 5733 |
| 5 | 🇧🇷 BR | 5114 |
| 6 | 🇩🇪 DE | 5114 |
| 7 | 🇮🇹 IT | 5065 |
| 8 | 🇨🇦 CA | 4736 |
| 9 | 🇯🇵 JP | 4480 |
| 10 | 🇬🇧 GB | 3974 |
| 11 | 🇫🇷 FR | 3755 |
| 12 | 🇨🇴 CO | 3250 |
| 13 | 🇲🇽 MX | 2877 |
| 14 | 🇬🇷 GR | 2680 |
| 15 | 🇳🇴 NO | 2585 |
| 16 | 🇨🇭 CH | 2432 |
| 17 | 🇲🇾 MY | 2068 |
| 18 | 🇹🇷 TR | 1714 |
| 19 | 🇿🇦 ZA | 1683 |
| 20 | 🇳🇿 NZ | 1590 |
| 21 | 🇹🇭 TH | 1572 |
| 22 | 🇵🇱 PL | 1521 |
| 23 | 🇰🇷 KR | 1484 |
| 24 | 🇵🇭 PH | 1413 |
| 25 | 🇬🇹 GT | 1409 |
| 26 | 🇲🇦 MA | 1068 |
| 27 | 🇲🇴 MO | 1037 |
| 28 | 🇳🇱 NL | 935 |
| 29 | 🇲🇪 ME | 930 |
| 30 | 🇭🇷 HR | 842 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2030 |
| 2 | Denver International Airport |  | US | 1579 |
| 3 | Tokyo International Airport |  | JP | 1492 |
| 4 | Indira Gandhi International Airport |  | IN | 1330 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1241 |
| 6 | Harry Reid International Airport |  | US | 1203 |
| 7 | Frankfurt am Main International Airport |  | DE | 1141 |
| 8 | Guaymaral Airport |  | CO | 1133 |
| 9 | Zurich Airport |  | CH | 1086 |
| 10 | La Aurora Airport |  | GT | 1077 |
| 11 | Macau International Airport |  | MO | 1037 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1023 |
| 13 | El Dorado International Airport |  | CO | 1021 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 936 |
| 15 | Chicago O'Hare International Airport |  | US | 893 |
| 16 | Madrid Barajas International Airport |  | ES | 836 |
| 17 | Kuala Lumpur International Airport |  | MY | 816 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 789 |
| 19 | Salt Lake City International Airport |  | US | 787 |
| 20 | Capua Airport |  | IT | 776 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 744 |
| 22 | Malpensa International Airport |  | IT | 740 |
| 23 | Bengaluru International Airport |  | IN | 734 |
| 24 | Charles de Gaulle International Airport |  | FR | 727 |
| 25 | Charlotte/Douglas International Airport |  | US | 713 |
| 26 | Congonhas Airport |  | BR | 709 |
| 27 | Daniel K Inouye International Airport |  | US | 673 |
| 28 | Tenerife Norte Airport |  | ES | 664 |
| 29 | Ninoy Aquino International Airport |  | PH | 647 |
| 30 | Barcelona International Airport |  | ES | 627 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 625 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 610 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 599 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 594 |
| 35 | Vitoria/Foronda Airport |  | ES | 583 |
| 36 | Don Mueang International Airport |  | TH | 576 |
| 37 | Amsterdam Airport Schiphol |  | NL | 575 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 567 |
| 39 | Calgary International Airport |  | CA | 555 |
| 40 | O. R. Tambo International Airport |  | ZA | 533 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 465 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 345 | 21m | 244 km | 1,452.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 249 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 239 | 14m | 114 km | 468.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 238 | 1h 26m | 910 km | 3,734.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 234 | 28m | 304 km | 1,226.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 213 | 1h 10m | 770 km | 2,829.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 201 | 19m | 165 km | 571.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 138 | 27m | 215 km | 511.1 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 134 | 14m | 154 km | 355.0 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 120 | 1h 1m | 695 km | 1,438.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 120 | 18m | 144 km | 298.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 115 | 1h 40m | 1,156 km | 2,294.2 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 113 | 1h 42m | 1,423 km | 2,773.2 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 112 | 1h 18m | 961 km | 1,856.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL2187 | United Airlines | Bob Hope Airport (KBUR) | Denver International Airport (KDEN) | 2026-05-23 22:00 UTC | 2026-05-23 23:48 UTC | 1h 47m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-05-23 23:01 UTC | 2026-05-23 23:48 UTC | 46m |
| CXK328 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-05-23 23:10 UTC | 2026-05-23 23:46 UTC | 36m |
| N117BF |  | St George Regional Airport (KSGU) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-05-23 21:04 UTC | 2026-05-23 23:34 UTC | 2h 30m |
| N879HZ |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-05-23 22:52 UTC | 2026-05-23 23:33 UTC | 41m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-05-23 23:03 UTC | 2026-05-23 23:21 UTC | 17m |
| N966TS |  | TA11 (TA11) | TA11 (TA11) | 2026-05-23 22:37 UTC | 2026-05-23 23:19 UTC | 41m |
| N1178R |  | Petersburg James A Johnson Airport (PAPG) | Kake Airport (PAFE) | 2026-05-23 23:03 UTC | 2026-05-23 23:16 UTC | 13m |
| CORVT92 | COR | Palm Springs International Airport (KPSP) | Flying B Ranch Airstrip (35TX) | 2026-05-23 21:15 UTC | 2026-05-23 23:16 UTC | 2h 0m |
|  |  | Camembe Airport (FNCB) | Soyo Airport (FNSO) | 2026-05-23 22:33 UTC | 2026-05-23 23:06 UTC | 33m |
| N7873N |  | City Of Colorado Springs Municipal Airport (KCOS) | Southeast Colorado Regional Airport (KLAA) | 2026-05-23 21:58 UTC | 2026-05-23 23:06 UTC | 1h 7m |
| ASA7004 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Prince Rupert Airport (CYPR) | 2026-05-23 21:43 UTC | 2026-05-23 23:04 UTC | 1h 20m |
| TKR132 | TKR | Roswell Air Center Airport (KROW) | NM44 (NM44) | 2026-05-23 22:55 UTC | 2026-05-23 23:03 UTC | 8m |
| TKR914 | TKR | Mc Clellan Airfield (KMCC) | Mc Clellan Airfield (KMCC) | 2026-05-23 22:12 UTC | 2026-05-23 23:03 UTC | 51m |
| VIV7016 | VIV | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 2026-05-23 22:01 UTC | 2026-05-23 23:01 UTC | 1h 0m |
| ANA393 | All Nippon Airways | Tokyo International Airport (RJTT) | Yamagata Airport (RJSC) | 2026-05-23 22:29 UTC | 2026-05-23 22:57 UTC | 27m |
| AAL2929 | American Airlines | Phoenix Sky Harbor International Airport (KPHX) | Julian Hinds Pump Plant Airstrip (73CL) | 2026-05-23 22:25 UTC | 2026-05-23 22:55 UTC | 29m |
| ANA381 | All Nippon Airways | Tokyo International Airport (RJTT) | Tottori Airport (RJOR) | 2026-05-23 22:04 UTC | 2026-05-23 22:54 UTC | 50m |
| N405MK |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-05-23 22:38 UTC | 2026-05-23 22:54 UTC | 15m |
| CXK1084 | CXK | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-05-23 21:49 UTC | 2026-05-23 22:53 UTC | 1h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
