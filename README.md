# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_16:03:17_UTC-green)

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

**Latest saved flight:** 2026-05-17 16:03:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-17 16:03:17 UTC

- **86,237** saved flights
- **30,905** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **86,237** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,066,574.9 tonnes** estimated CO2 emissions
- **61,830,426 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3690 |
| 2 | SkyWest Airlines | 3182 |
| 3 | IndiGo | 1863 |
| 4 | EJA | 1619 |
| 5 | American Airlines | 1322 |
| 6 | Southwest Airlines | 1249 |
| 7 | Lufthansa | 1092 |
| 8 | ENY | 1066 |
| 9 | Delta Air Lines | 941 |
| 10 | Vueling | 818 |
| 11 | AXM | 782 |
| 12 | LATAM Airlines | 780 |
| 13 | WIF | 737 |
| 14 | AZU | 674 |
| 15 | Swiss International | 671 |
| 16 | All Nippon Airways | 666 |
| 17 | LXJ | 631 |
| 18 | QLK | 625 |
| 19 | Alaska Airlines | 611 |
| 20 | easyJet | 570 |
| 21 | EJU | 553 |
| 22 | Cathay Pacific | 549 |
| 23 | AEE | 541 |
| 24 | VIV | 515 |
| 25 | Air France | 508 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 457 |
| 28 | AXB | 453 |
| 29 | MXY | 429 |
| 30 | AIQ | 426 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 70482 |
| 2 | 🇪🇸 ES | 6115 |
| 3 | 🇮🇳 IN | 5819 |
| 4 | 🇦🇺 AU | 5477 |
| 5 | 🇩🇪 DE | 4811 |
| 6 | 🇮🇹 IT | 4766 |
| 7 | 🇧🇷 BR | 4729 |
| 8 | 🇯🇵 JP | 4320 |
| 9 | 🇨🇦 CA | 4270 |
| 10 | 🇬🇧 GB | 3688 |
| 11 | 🇫🇷 FR | 3452 |
| 12 | 🇨🇴 CO | 2904 |
| 13 | 🇲🇽 MX | 2649 |
| 14 | 🇬🇷 GR | 2513 |
| 15 | 🇳🇴 NO | 2384 |
| 16 | 🇨🇭 CH | 2298 |
| 17 | 🇲🇾 MY | 1964 |
| 18 | 🇿🇦 ZA | 1617 |
| 19 | 🇹🇷 TR | 1558 |
| 20 | 🇳🇿 NZ | 1505 |
| 21 | 🇹🇭 TH | 1502 |
| 22 | 🇵🇱 PL | 1435 |
| 23 | 🇵🇭 PH | 1352 |
| 24 | 🇰🇷 KR | 1352 |
| 25 | 🇬🇹 GT | 1293 |
| 26 | 🇲🇴 MO | 1007 |
| 27 | 🇲🇦 MA | 1004 |
| 28 | 🇲🇪 ME | 900 |
| 29 | 🇳🇱 NL | 882 |
| 30 | 🇭🇷 HR | 774 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1879 |
| 2 | Denver International Airport |  | US | 1447 |
| 3 | Tokyo International Airport |  | JP | 1443 |
| 4 | Indira Gandhi International Airport |  | IN | 1247 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1200 |
| 6 | Frankfurt am Main International Airport |  | DE | 1104 |
| 7 | Harry Reid International Airport |  | US | 1091 |
| 8 | Zurich Airport |  | CH | 1029 |
| 9 | Macau International Airport |  | MO | 1007 |
| 10 | Guaymaral Airport |  | CO | 985 |
| 11 | La Aurora Airport |  | GT | 982 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 953 |
| 13 | El Dorado International Airport |  | CO | 931 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 866 |
| 15 | Chicago O'Hare International Airport |  | US | 829 |
| 16 | Madrid Barajas International Airport |  | ES | 788 |
| 17 | Kuala Lumpur International Airport |  | MY | 780 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 742 |
| 19 | Capua Airport |  | IT | 717 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 715 |
| 21 | Salt Lake City International Airport |  | US | 714 |
| 22 | Malpensa International Airport |  | IT | 712 |
| 23 | Bengaluru International Airport |  | IN | 706 |
| 24 | Charles de Gaulle International Airport |  | FR | 675 |
| 25 | Charlotte/Douglas International Airport |  | US | 667 |
| 26 | Congonhas Airport |  | BR | 662 |
| 27 | Tenerife Norte Airport |  | ES | 635 |
| 28 | Daniel K Inouye International Airport |  | US | 631 |
| 29 | Ninoy Aquino International Airport |  | PH | 619 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 583 |
| 32 | Barcelona International Airport |  | ES | 577 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 575 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 556 |
| 35 | Vitoria/Foronda Airport |  | ES | 549 |
| 36 | Don Mueang International Airport |  | TH | 544 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 542 |
| 38 | Amsterdam Airport Schiphol |  | NL | 538 |
| 39 | O. R. Tambo International Airport |  | ZA | 510 |
| 40 | Calgary International Airport |  | CA | 503 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 407 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 320 | 21m | 244 km | 1,347.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 230 | 1h 26m | 910 km | 3,609.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 221 | 14m | 114 km | 433.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 219 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 200 | 1h 10m | 770 km | 2,656.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 193 | 19m | 165 km | 549.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 182 | 26m | 275 km | 862.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 135 | 31m | 369 km | 859.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 130 | 27m | 152 km | 339.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 126 | 20m | 147 km | 318.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 124 | 14m | 154 km | 328.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 123 | 23m | 55 km | 116.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 110 | 1h 42m | 1,423 km | 2,699.6 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 109 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 109 | 18m | 144 km | 271.1 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 52m | 1,304 km | 2,339.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5QD |  | 0PA0 (0PA0) | 0PA0 (0PA0) | 2026-05-17 16:00 UTC | 2026-05-17 16:03 UTC | 2m |
| CSH870 | CSH | Budapest Ferenc Liszt International Airport (LHBP) | Yeltsovka Airport (UNNE) | 2026-05-17 10:37 UTC | 2026-05-17 16:02 UTC | 5h 25m |
| N2872Q |  | K2A5 (K2A5) | K5W8 (K5W8) | 2026-05-17 15:17 UTC | 2026-05-17 16:01 UTC | 43m |
| N985AW |  | Crystal Springs Ranch Airport (UT54) | Logan-Cache Airport (KLGU) | 2026-05-17 14:55 UTC | 2026-05-17 15:57 UTC | 1h 2m |
| N333HN |  | Barcelona International Airport (LEBL) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-17 15:01 UTC | 2026-05-17 15:51 UTC | 50m |
| N204EH |  | Zephyrhills Municipal Airport (KZPH) | Zephyrhills Municipal Airport (KZPH) | 2026-05-17 15:34 UTC | 2026-05-17 15:51 UTC | 16m |
| G08759 |  | Frederick Douglass/Greater Rochester International Airport (KROC) | 68NY (68NY) | 2026-05-17 15:39 UTC | 2026-05-17 15:51 UTC | 11m |
| N106PA |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-05-17 15:31 UTC | 2026-05-17 15:51 UTC | 19m |
| N818MT |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-05-17 15:21 UTC | 2026-05-17 15:49 UTC | 27m |
| N79013 |  | Trenton-Robbinsville Airport (KN87) | Millville Municipal Airport (KMIV) | 2026-05-17 15:12 UTC | 2026-05-17 15:47 UTC | 34m |
| N660JW |  | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-05-17 15:26 UTC | 2026-05-17 15:43 UTC | 17m |
| N713EE |  | Pickens County Airport (KJZP) | Pickens County Airport (KJZP) | 2026-05-17 15:24 UTC | 2026-05-17 15:42 UTC | 18m |
| ASR252 | ASR | Pecs-Pogany Airport (LHPP) | Otocac Airport (LDRO) | 2026-05-17 10:10 UTC | 2026-05-17 15:42 UTC | 5h 31m |
| DLH6YM | Lufthansa | Frankfurt am Main International Airport (EDDF) | Herzogenaurach Airport (EDQH) | 2026-05-17 15:14 UTC | 2026-05-17 15:41 UTC | 26m |
| N110EX |  | Destin Executive Airport (KDTS) | Jonesboro Municipal Airport (KJBR) | 2026-05-17 14:37 UTC | 2026-05-17 15:40 UTC | 1h 2m |
| EJU13NF | EJU | Grazzanise Airport (LIRM) | Sallanches Airport (LFHZ) | 2026-05-17 14:10 UTC | 2026-05-17 15:39 UTC | 1h 28m |
| EJU96HC | EJU | Venezia / Tessera -  Marco Polo Airport (LIPZ) | La Tour Du Pin Airport (LFKP) | 2026-05-17 14:23 UTC | 2026-05-17 15:39 UTC | 1h 15m |
| N500RW |  | Reggio Calabria Airport (LICR) | LIVV (LIVV) | 2026-05-17 13:08 UTC | 2026-05-17 15:39 UTC | 2h 30m |
| AFR98ZF | Air France | Charles de Gaulle International Airport (LFPG) | Torino / Caselle International Airport (LIMF) | 2026-05-17 14:30 UTC | 2026-05-17 15:39 UTC | 1h 8m |
| PTN97X | PTN | Vienna International Airport (LOWW) | Ecuvillens Airport (LSGE) | 2026-05-17 14:13 UTC | 2026-05-17 15:39 UTC | 1h 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
