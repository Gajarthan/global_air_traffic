# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_15:21:17_UTC-green)

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

**Latest saved flight:** 2026-05-17 15:21:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-17 15:21:17 UTC

- **86,066** saved flights
- **30,842** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **86,066** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,064,844.7 tonnes** estimated CO2 emissions
- **61,730,127 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3687 |
| 2 | SkyWest Airlines | 3173 |
| 3 | IndiGo | 1859 |
| 4 | EJA | 1615 |
| 5 | American Airlines | 1321 |
| 6 | Southwest Airlines | 1248 |
| 7 | Lufthansa | 1091 |
| 8 | ENY | 1063 |
| 9 | Delta Air Lines | 938 |
| 10 | Vueling | 816 |
| 11 | AXM | 782 |
| 12 | LATAM Airlines | 780 |
| 13 | WIF | 735 |
| 14 | AZU | 674 |
| 15 | All Nippon Airways | 666 |
| 16 | Swiss International | 666 |
| 17 | LXJ | 628 |
| 18 | QLK | 625 |
| 19 | Alaska Airlines | 611 |
| 20 | easyJet | 569 |
| 21 | Cathay Pacific | 549 |
| 22 | EJU | 548 |
| 23 | AEE | 540 |
| 24 | VIV | 515 |
| 25 | Air France | 506 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 454 |
| 28 | AXB | 453 |
| 29 | MXY | 429 |
| 30 | AIQ | 425 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 70340 |
| 2 | 🇪🇸 ES | 6094 |
| 3 | 🇮🇳 IN | 5812 |
| 4 | 🇦🇺 AU | 5475 |
| 5 | 🇩🇪 DE | 4804 |
| 6 | 🇮🇹 IT | 4748 |
| 7 | 🇧🇷 BR | 4729 |
| 8 | 🇯🇵 JP | 4320 |
| 9 | 🇨🇦 CA | 4264 |
| 10 | 🇬🇧 GB | 3683 |
| 11 | 🇫🇷 FR | 3438 |
| 12 | 🇨🇴 CO | 2896 |
| 13 | 🇲🇽 MX | 2646 |
| 14 | 🇬🇷 GR | 2500 |
| 15 | 🇳🇴 NO | 2380 |
| 16 | 🇨🇭 CH | 2285 |
| 17 | 🇲🇾 MY | 1964 |
| 18 | 🇿🇦 ZA | 1613 |
| 19 | 🇹🇷 TR | 1556 |
| 20 | 🇳🇿 NZ | 1505 |
| 21 | 🇹🇭 TH | 1501 |
| 22 | 🇵🇱 PL | 1432 |
| 23 | 🇵🇭 PH | 1352 |
| 24 | 🇰🇷 KR | 1352 |
| 25 | 🇬🇹 GT | 1290 |
| 26 | 🇲🇴 MO | 1007 |
| 27 | 🇲🇦 MA | 1003 |
| 28 | 🇲🇪 ME | 898 |
| 29 | 🇳🇱 NL | 879 |
| 30 | 🇭🇷 HR | 770 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1876 |
| 2 | Denver International Airport |  | US | 1443 |
| 3 | Tokyo International Airport |  | JP | 1443 |
| 4 | Indira Gandhi International Airport |  | IN | 1245 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1196 |
| 6 | Frankfurt am Main International Airport |  | DE | 1102 |
| 7 | Harry Reid International Airport |  | US | 1089 |
| 8 | Zurich Airport |  | CH | 1024 |
| 9 | Macau International Airport |  | MO | 1007 |
| 10 | Guaymaral Airport |  | CO | 984 |
| 11 | La Aurora Airport |  | GT | 979 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 947 |
| 13 | El Dorado International Airport |  | CO | 928 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 864 |
| 15 | Chicago O'Hare International Airport |  | US | 829 |
| 16 | Madrid Barajas International Airport |  | ES | 785 |
| 17 | Kuala Lumpur International Airport |  | MY | 780 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 740 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 715 |
| 20 | Salt Lake City International Airport |  | US | 713 |
| 21 | Malpensa International Airport |  | IT | 712 |
| 22 | Capua Airport |  | IT | 709 |
| 23 | Bengaluru International Airport |  | IN | 704 |
| 24 | Charles de Gaulle International Airport |  | FR | 672 |
| 25 | Charlotte/Douglas International Airport |  | US | 665 |
| 26 | Congonhas Airport |  | BR | 662 |
| 27 | Tenerife Norte Airport |  | ES | 632 |
| 28 | Daniel K Inouye International Airport |  | US | 630 |
| 29 | Ninoy Aquino International Airport |  | PH | 619 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 583 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 574 |
| 33 | Barcelona International Airport |  | ES | 574 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 555 |
| 35 | Vitoria/Foronda Airport |  | ES | 547 |
| 36 | Don Mueang International Airport |  | TH | 543 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 542 |
| 38 | Amsterdam Airport Schiphol |  | NL | 535 |
| 39 | O. R. Tambo International Airport |  | ZA | 508 |
| 40 | Calgary International Airport |  | CA | 502 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 407 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 319 | 21m | 244 km | 1,343.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 230 | 1h 26m | 910 km | 3,609.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 221 | 14m | 114 km | 433.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 219 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 200 | 1h 10m | 770 km | 2,656.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 193 | 19m | 165 km | 549.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 181 | 26m | 275 km | 857.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 135 | 31m | 369 km | 859.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 128 | 27m | 152 km | 334.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 125 | 20m | 147 km | 316.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 124 | 14m | 154 km | 328.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 122 | 23m | 55 km | 116.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 109 | 1h 43m | 1,423 km | 2,675.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 109 | 18m | 144 km | 271.1 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 107 | 12m | - | - |
| 29 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 52m | 1,304 km | 2,339.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N737LG |  | Ohio State University Airport (KOSU) | Delaware Municipal/Jim Moore Field (KDLZ) | 2026-05-17 14:55 UTC | 2026-05-17 15:21 UTC | 25m |
| N41533 |  | Bugs Airport (PA68) | Schuylkill County/Joe Zerbey Airport (KZER) | 2026-05-17 14:11 UTC | 2026-05-17 15:18 UTC | 1h 7m |
| N386RH |  | Norwood Memorial Airport (KOWD) | Norwood Memorial Airport (KOWD) | 2026-05-17 14:46 UTC | 2026-05-17 15:17 UTC | 31m |
| N80790 |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-17 14:31 UTC | 2026-05-17 15:15 UTC | 44m |
| N125PM |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-05-17 13:58 UTC | 2026-05-17 15:11 UTC | 1h 13m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-17 14:56 UTC | 2026-05-17 15:10 UTC | 14m |
| THY6256 | Turkish Airlines | Istanbul Airport (LTFM) | Macau International Airport (VMMC) | 2026-05-17 01:36 UTC | 2026-05-17 15:09 UTC | 13h 33m |
| AAL2867 | American Airlines | Salt Lake City International Airport (KSLC) | Dallas-Fort Worth International Airport (KDFW) | 2026-05-17 12:48 UTC | 2026-05-17 14:59 UTC | 2h 10m |
| VAR851 | VAR | Phoenix Goodyear Airport (KGYR) | Bishop Airfield (1AZ0) | 2026-05-17 14:43 UTC | 2026-05-17 14:57 UTC | 14m |
| PGT74AU | PGT | Dusseldorf International Airport (EDDL) | Sabiha Gokcen International Airport (LTFJ) | 2026-05-17 12:13 UTC | 2026-05-17 14:50 UTC | 2h 36m |
| N68334 |  | Ann Arbor Municipal Airport (KARB) | 46MI (46MI) | 2026-05-17 14:31 UTC | 2026-05-17 14:46 UTC | 14m |
| N113VG |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-05-17 13:52 UTC | 2026-05-17 14:45 UTC | 52m |
| N223AL |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-05-17 14:26 UTC | 2026-05-17 14:45 UTC | 18m |
| N475LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-05-17 13:47 UTC | 2026-05-17 14:44 UTC | 57m |
| N739WR |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-05-17 14:42 UTC | 2026-05-17 14:43 UTC | 0m |
| N9936W |  | Columbus Airport (KCSG) | Harris County Airport (KPIM) | 2026-05-17 14:19 UTC | 2026-05-17 14:42 UTC | 23m |
| CXK326 | CXK | Morristown Municipal Airport (KMMU) | Lancaster Airport (KLNS) | 2026-05-17 13:46 UTC | 2026-05-17 14:41 UTC | 54m |
| N55BF |  | KU77 (KU77) | KU77 (KU77) | 2026-05-17 14:12 UTC | 2026-05-17 14:36 UTC | 23m |
| N739WR |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-05-17 14:10 UTC | 2026-05-17 14:32 UTC | 22m |
| N7277F |  | Guaymaral Airport (SKGY) | Tunja Airport (SKTJ) | 2026-05-17 14:18 UTC | 2026-05-17 14:30 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
