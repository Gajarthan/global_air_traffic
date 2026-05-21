# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_08:08:35_UTC-green)

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

**Latest saved flight:** 2026-05-21 08:08:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-21 08:08:35 UTC

- **89,782** saved flights
- **31,990** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **89,782** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,110,486.9 tonnes** estimated CO2 emissions
- **64,376,054 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3848 |
| 2 | SkyWest Airlines | 3333 |
| 3 | IndiGo | 1892 |
| 4 | EJA | 1696 |
| 5 | American Airlines | 1369 |
| 6 | Southwest Airlines | 1300 |
| 7 | Lufthansa | 1116 |
| 8 | ENY | 1106 |
| 9 | Delta Air Lines | 987 |
| 10 | Vueling | 855 |
| 11 | LATAM Airlines | 807 |
| 12 | AXM | 798 |
| 13 | WIF | 778 |
| 14 | AZU | 713 |
| 15 | Swiss International | 688 |
| 16 | All Nippon Airways | 675 |
| 17 | LXJ | 668 |
| 18 | Alaska Airlines | 639 |
| 19 | QLK | 639 |
| 20 | easyJet | 590 |
| 21 | Cathay Pacific | 579 |
| 22 | EJU | 579 |
| 23 | AEE | 552 |
| 24 | VIV | 535 |
| 25 | Air France | 524 |
| 26 | Japan Airlines | 482 |
| 27 | CXK | 470 |
| 28 | AXB | 461 |
| 29 | MXY | 457 |
| 30 | AIQ | 435 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 73900 |
| 2 | 🇪🇸 ES | 6363 |
| 3 | 🇮🇳 IN | 5940 |
| 4 | 🇦🇺 AU | 5608 |
| 5 | 🇩🇪 DE | 4963 |
| 6 | 🇮🇹 IT | 4962 |
| 7 | 🇧🇷 BR | 4920 |
| 8 | 🇨🇦 CA | 4496 |
| 9 | 🇯🇵 JP | 4384 |
| 10 | 🇬🇧 GB | 3829 |
| 11 | 🇫🇷 FR | 3599 |
| 12 | 🇨🇴 CO | 3079 |
| 13 | 🇲🇽 MX | 2778 |
| 14 | 🇬🇷 GR | 2587 |
| 15 | 🇳🇴 NO | 2492 |
| 16 | 🇨🇭 CH | 2359 |
| 17 | 🇲🇾 MY | 2007 |
| 18 | 🇿🇦 ZA | 1643 |
| 19 | 🇹🇷 TR | 1629 |
| 20 | 🇳🇿 NZ | 1554 |
| 21 | 🇹🇭 TH | 1529 |
| 22 | 🇵🇱 PL | 1482 |
| 23 | 🇰🇷 KR | 1409 |
| 24 | 🇵🇭 PH | 1385 |
| 25 | 🇬🇹 GT | 1339 |
| 26 | 🇲🇴 MO | 1035 |
| 27 | 🇲🇦 MA | 1033 |
| 28 | 🇲🇪 ME | 917 |
| 29 | 🇳🇱 NL | 910 |
| 30 | 🇭🇷 HR | 810 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1964 |
| 2 | Denver International Airport |  | US | 1507 |
| 3 | Tokyo International Airport |  | JP | 1462 |
| 4 | Indira Gandhi International Airport |  | IN | 1286 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1218 |
| 6 | Harry Reid International Airport |  | US | 1149 |
| 7 | Frankfurt am Main International Airport |  | DE | 1126 |
| 8 | Zurich Airport |  | CH | 1066 |
| 9 | Guaymaral Airport |  | CO | 1049 |
| 10 | Macau International Airport |  | MO | 1035 |
| 11 | La Aurora Airport |  | GT | 1019 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 992 |
| 13 | El Dorado International Airport |  | CO | 980 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 913 |
| 15 | Chicago O'Hare International Airport |  | US | 868 |
| 16 | Madrid Barajas International Airport |  | ES | 817 |
| 17 | Kuala Lumpur International Airport |  | MY | 794 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 770 |
| 19 | Capua Airport |  | IT | 761 |
| 20 | Salt Lake City International Airport |  | US | 756 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 731 |
| 22 | Malpensa International Airport |  | IT | 727 |
| 23 | Bengaluru International Airport |  | IN | 715 |
| 24 | Charles de Gaulle International Airport |  | FR | 699 |
| 25 | Congonhas Airport |  | BR | 690 |
| 26 | Charlotte/Douglas International Airport |  | US | 689 |
| 27 | Daniel K Inouye International Airport |  | US | 658 |
| 28 | Tenerife Norte Airport |  | ES | 654 |
| 29 | Ninoy Aquino International Airport |  | PH | 636 |
| 30 | Barcelona International Airport |  | ES | 603 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 600 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 589 |
| 34 | Vitoria/Foronda Airport |  | ES | 570 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 567 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 37 | Amsterdam Airport Schiphol |  | NL | 560 |
| 38 | Don Mueang International Airport |  | TH | 559 |
| 39 | Calgary International Airport |  | CA | 533 |
| 40 | O. R. Tambo International Airport |  | ZA | 519 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 429 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 334 | 21m | 244 km | 1,406.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 249 | 24m | 225 km | 966.0 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 235 | 14m | 114 km | 460.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 232 | 1h 26m | 910 km | 3,640.6 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 231 | 28m | 304 km | 1,211.0 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 229 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 207 | 1h 10m | 770 km | 2,749.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 196 | 19m | 165 km | 557.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 186 | 26m | 275 km | 881.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 137 | 31m | 369 km | 872.0 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 132 | 22m | 55 km | 125.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 131 | 27m | 215 km | 485.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 129 | 14m | 154 km | 341.8 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 116 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 116 | 18m | 144 km | 288.5 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 109 | 1h 18m | 961 km | 1,806.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 109 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 108 | 1h 40m | 1,156 km | 2,154.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBZWD | HBZ | Saanen Airport (LSGK) | Sion Airport (LSGS) | 2026-05-21 07:22 UTC | 2026-05-21 08:08 UTC | 46m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-05-21 07:54 UTC | 2026-05-21 08:07 UTC | 12m |
| CFH3 | CFH | YRBN (YRBN) | Sydney Bankstown Airport (YSBK) | 2026-05-21 07:40 UTC | 2026-05-21 08:05 UTC | 25m |
| HBZJB | HBZ | Schanis Airport (LSZX) | Speck-Fehraltorf Airport (LSZK) | 2026-05-21 07:48 UTC | 2026-05-21 07:59 UTC | 10m |
| SRB502 | SRB | Batajnica Air Base (LYBT) | LYLE (LYLE) | 2026-05-21 07:23 UTC | 2026-05-21 07:57 UTC | 33m |
| N254EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-05-21 04:58 UTC | 2026-05-21 07:54 UTC | 2h 55m |
| SHA944 | SHA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-05-21 07:53 UTC | 2026-05-21 07:53 UTC | 0m |
| 5YPCS |  | Nairobi Wilson Airport (HKNW) | Nairobi Wilson Airport (HKNW) | 2026-05-21 07:44 UTC | 2026-05-21 07:48 UTC | 3m |
| ZSMSF | ZSM | Lanseria Airport (FALA) | Dwaalboom Airport (FADB) | 2026-05-21 07:08 UTC | 2026-05-21 07:32 UTC | 24m |
| M28A |  | Mengen-Hohentengen Airport (EDTM) | Mengen-Hohentengen Airport (EDTM) | 2026-05-21 07:13 UTC | 2026-05-21 07:30 UTC | 17m |
| GAP2680 | GAP | Godofredo P. Ramos Airport (RPVE) | San Jose Airport (RPUH) | 2026-05-21 07:16 UTC | 2026-05-21 07:28 UTC | 12m |
| AIQ3203 | AIQ | Don Mueang International Airport (VTBD) | VLXL (VLXL) | 2026-05-21 06:36 UTC | 2026-05-21 07:27 UTC | 50m |
| AUR202 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-05-21 07:07 UTC | 2026-05-21 07:21 UTC | 13m |
| HIM775 | HIM | Ramechhap Airport (VNRC) | Ramechhap Airport (VNRC) | 2026-05-21 07:17 UTC | 2026-05-21 07:18 UTC | 0m |
| GRZLY67 | GRZ | Travis Afb Airport (KSUU) | Travis Afb Airport (KSUU) | 2026-05-21 07:00 UTC | 2026-05-21 07:16 UTC | 15m |
| ANE30KP | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-05-21 06:35 UTC | 2026-05-21 07:12 UTC | 37m |
| VSB92 | VSB | Barrow Walney Island Airport (EGNL) | Bristol International Airport (EGGD) | 2026-05-21 06:34 UTC | 2026-05-21 07:11 UTC | 37m |
| ANE82BX | ANE | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 2026-05-21 06:41 UTC | 2026-05-21 07:09 UTC | 27m |
| ABL8819 | ABL | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-05-21 06:41 UTC | 2026-05-21 07:09 UTC | 27m |
| AXM6037 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-05-21 06:48 UTC | 2026-05-21 07:07 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
