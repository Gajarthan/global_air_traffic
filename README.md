# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_20:11:20_UTC-green)

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

**Latest saved flight:** 2026-05-29 20:11:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-29 20:11:20 UTC

- **96,997** saved flights
- **34,094** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **96,997** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,186,732.9 tonnes** estimated CO2 emissions
- **68,796,109 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4071 |
| 2 | SkyWest Airlines | 3606 |
| 3 | IndiGo | 1998 |
| 4 | EJA | 1835 |
| 5 | American Airlines | 1470 |
| 6 | Southwest Airlines | 1408 |
| 7 | ENY | 1192 |
| 8 | Lufthansa | 1156 |
| 9 | Delta Air Lines | 1061 |
| 10 | Vueling | 915 |
| 11 | LATAM Airlines | 865 |
| 12 | WIF | 864 |
| 13 | AXM | 854 |
| 14 | AZU | 785 |
| 15 | LXJ | 739 |
| 16 | Swiss International | 719 |
| 17 | All Nippon Airways | 709 |
| 18 | Alaska Airlines | 674 |
| 19 | QLK | 669 |
| 20 | easyJet | 635 |
| 21 | EJU | 614 |
| 22 | Cathay Pacific | 585 |
| 23 | AEE | 584 |
| 24 | VIV | 573 |
| 25 | Air France | 569 |
| 26 | CXK | 520 |
| 27 | MXY | 514 |
| 28 | Japan Airlines | 497 |
| 29 | AXB | 488 |
| 30 | AIQ | 465 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 80279 |
| 2 | 🇪🇸 ES | 6770 |
| 3 | 🇮🇳 IN | 6310 |
| 4 | 🇦🇺 AU | 5922 |
| 5 | 🇧🇷 BR | 5335 |
| 6 | 🇩🇪 DE | 5314 |
| 7 | 🇮🇹 IT | 5233 |
| 8 | 🇨🇦 CA | 4934 |
| 9 | 🇯🇵 JP | 4599 |
| 10 | 🇬🇧 GB | 4157 |
| 11 | 🇫🇷 FR | 3931 |
| 12 | 🇨🇴 CO | 3369 |
| 13 | 🇲🇽 MX | 2982 |
| 14 | 🇬🇷 GR | 2804 |
| 15 | 🇳🇴 NO | 2733 |
| 16 | 🇨🇭 CH | 2545 |
| 17 | 🇲🇾 MY | 2171 |
| 18 | 🇹🇷 TR | 1804 |
| 19 | 🇿🇦 ZA | 1731 |
| 20 | 🇳🇿 NZ | 1651 |
| 21 | 🇹🇭 TH | 1639 |
| 22 | 🇰🇷 KR | 1589 |
| 23 | 🇵🇱 PL | 1583 |
| 24 | 🇵🇭 PH | 1455 |
| 25 | 🇬🇹 GT | 1451 |
| 26 | 🇲🇦 MA | 1096 |
| 27 | 🇲🇴 MO | 1043 |
| 28 | 🇳🇱 NL | 973 |
| 29 | 🇲🇪 ME | 950 |
| 30 | 🇭🇷 HR | 879 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2100 |
| 2 | Denver International Airport |  | US | 1637 |
| 3 | Tokyo International Airport |  | JP | 1524 |
| 4 | Indira Gandhi International Airport |  | IN | 1367 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1283 |
| 6 | Harry Reid International Airport |  | US | 1244 |
| 7 | Guaymaral Airport |  | CO | 1198 |
| 8 | Frankfurt am Main International Airport |  | DE | 1167 |
| 9 | Zurich Airport |  | CH | 1132 |
| 10 | La Aurora Airport |  | GT | 1113 |
| 11 | El Dorado International Airport |  | CO | 1046 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1044 |
| 13 | Macau International Airport |  | MO | 1043 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 972 |
| 15 | Chicago O'Hare International Airport |  | US | 932 |
| 16 | Madrid Barajas International Airport |  | ES | 860 |
| 17 | Kuala Lumpur International Airport |  | MY | 858 |
| 18 | Salt Lake City International Airport |  | US | 817 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 812 |
| 20 | Capua Airport |  | IT | 801 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 769 |
| 22 | Malpensa International Airport |  | IT | 755 |
| 23 | Bengaluru International Airport |  | IN | 755 |
| 24 | Charles de Gaulle International Airport |  | FR | 752 |
| 25 | Congonhas Airport |  | BR | 740 |
| 26 | Charlotte/Douglas International Airport |  | US | 735 |
| 27 | Daniel K Inouye International Airport |  | US | 688 |
| 28 | Tenerife Norte Airport |  | ES | 682 |
| 29 | Ninoy Aquino International Airport |  | PH | 664 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 651 |
| 31 | Barcelona International Airport |  | ES | 646 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 624 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 618 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 35 | Don Mueang International Airport |  | TH | 600 |
| 36 | Amsterdam Airport Schiphol |  | NL | 600 |
| 37 | Vitoria/Foronda Airport |  | ES | 597 |
| 38 | Calgary International Airport |  | CA | 572 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 571 |
| 40 | O. R. Tambo International Airport |  | ZA | 551 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 494 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 358 | 21m | 244 km | 1,507.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 259 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 247 | 14m | 114 km | 484.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 243 | 1h 26m | 910 km | 3,813.2 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 242 | 28m | 304 km | 1,268.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 223 | 1h 10m | 770 km | 2,962.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 209 | 19m | 165 km | 594.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 193 | 26m | 275 km | 914.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 155 | 20m | 99 km | 265.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 146 | 27m | 215 km | 540.7 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 141 | 22m | 55 km | 134.0 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 140 | 27m | 152 km | 365.9 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 132 | 20m | 250 km | 570.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 129 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 126 | 18m | 144 km | 313.4 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 124 | 1h 1m | 695 km | 1,486.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 123 | 1h 39m | 1,156 km | 2,453.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 115 | 1h 18m | 961 km | 1,906.2 t |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 2121231 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-05-29 19:44 UTC | 2026-05-29 20:11 UTC | 26m |
| N536HC |  | Spirit Of St Louis Airport (KSUS) | Dubuque Regional Airport (KDBQ) | 2026-05-29 19:13 UTC | 2026-05-29 20:10 UTC | 57m |
| LSXX | LSX | Catalina Airport (KAVX) | Catalina Airport (KAVX) | 2026-05-29 19:58 UTC | 2026-05-29 20:10 UTC | 12m |
| TOGO05 | TOG | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-05-29 18:43 UTC | 2026-05-29 20:03 UTC | 1h 20m |
| AXEL10 | AXE | El Paso International Airport (KELP) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-05-29 18:22 UTC | 2026-05-29 20:03 UTC | 1h 41m |
| SFE1 | SFE | Cross Triangle Ranch Airport (2XS5) | Bud Dryden Airport (TX05) | 2026-05-29 19:36 UTC | 2026-05-29 20:02 UTC | 26m |
| VTM487 | VTM | Plan De Guadalupe International Airport (MMIO) | Monclova International Airport (MMMV) | 2026-05-29 19:40 UTC | 2026-05-29 20:02 UTC | 21m |
| N28PK |  | Dubuque Regional Airport (KDBQ) | Monticello Regional Airport (KMXO) | 2026-05-29 19:11 UTC | 2026-05-29 19:55 UTC | 43m |
| CXK1000 | CXK | Arlington Municipal Airport (KGKY) | Mid-Way Regional Airport (KJWY) | 2026-05-29 19:07 UTC | 2026-05-29 19:55 UTC | 48m |
| C2703 |  | Mc Clellan Airfield (KMCC) | Mc Clellan Airfield (KMCC) | 2026-05-29 19:34 UTC | 2026-05-29 19:54 UTC | 19m |
| N94MN |  | Paso Robles Municipal Airport (KPRB) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-05-29 19:20 UTC | 2026-05-29 19:53 UTC | 33m |
| N110UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-05-29 19:28 UTC | 2026-05-29 19:53 UTC | 24m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-05-29 08:49 UTC | 2026-05-29 19:50 UTC | 11h 1m |
| N1238N |  | 4PA0 (4PA0) | PS35 (PS35) | 2026-05-29 18:47 UTC | 2026-05-29 19:48 UTC | 1h 1m |
| N555WL |  | Oakland County International Airport (KPTK) | Grayling Army Air Field (KGOV) | 2026-05-29 19:22 UTC | 2026-05-29 19:48 UTC | 26m |
| N893AP |  | Waterbury-Oxford Airport (KOXC) | Laguardia Airport (KLGA) | 2026-05-29 19:17 UTC | 2026-05-29 19:48 UTC | 30m |
| CWA935 | CWA | Edmonton International Airport (CYEG) | Provost Airport (CEH6) | 2026-05-29 19:17 UTC | 2026-05-29 19:48 UTC | 30m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-05-29 19:29 UTC | 2026-05-29 19:47 UTC | 18m |
| N99DQ |  | Republic Airport (KFRG) | Laguardia Airport (KLGA) | 2026-05-29 19:30 UTC | 2026-05-29 19:45 UTC | 15m |
| EJA442 | EJA | Blue Grass Airport (KLEX) | Gainesville Regional Airport (KGNV) | 2026-05-29 18:25 UTC | 2026-05-29 19:45 UTC | 1h 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
