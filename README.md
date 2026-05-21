# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_19:02:37_UTC-green)

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

**Latest saved flight:** 2026-05-21 19:02:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-21 19:02:37 UTC

- **90,509** saved flights
- **32,216** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **90,509** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,117,678.5 tonnes** estimated CO2 emissions
- **64,792,954 km** total distance flown
- **869 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3873 |
| 2 | SkyWest Airlines | 3347 |
| 3 | IndiGo | 1899 |
| 4 | EJA | 1712 |
| 5 | American Airlines | 1376 |
| 6 | Southwest Airlines | 1309 |
| 7 | Lufthansa | 1119 |
| 8 | ENY | 1115 |
| 9 | Delta Air Lines | 992 |
| 10 | Vueling | 863 |
| 11 | LATAM Airlines | 815 |
| 12 | AXM | 800 |
| 13 | WIF | 794 |
| 14 | AZU | 718 |
| 15 | Swiss International | 688 |
| 16 | All Nippon Airways | 679 |
| 17 | LXJ | 678 |
| 18 | Alaska Airlines | 641 |
| 19 | QLK | 639 |
| 20 | easyJet | 592 |
| 21 | EJU | 582 |
| 22 | Cathay Pacific | 579 |
| 23 | AEE | 556 |
| 24 | VIV | 536 |
| 25 | Air France | 532 |
| 26 | Japan Airlines | 482 |
| 27 | CXK | 477 |
| 28 | MXY | 465 |
| 29 | AXB | 462 |
| 30 | AIQ | 438 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 74547 |
| 2 | 🇪🇸 ES | 6420 |
| 3 | 🇮🇳 IN | 5973 |
| 4 | 🇦🇺 AU | 5618 |
| 5 | 🇩🇪 DE | 4997 |
| 6 | 🇮🇹 IT | 4979 |
| 7 | 🇧🇷 BR | 4962 |
| 8 | 🇨🇦 CA | 4539 |
| 9 | 🇯🇵 JP | 4400 |
| 10 | 🇬🇧 GB | 3871 |
| 11 | 🇫🇷 FR | 3637 |
| 12 | 🇨🇴 CO | 3117 |
| 13 | 🇲🇽 MX | 2792 |
| 14 | 🇬🇷 GR | 2607 |
| 15 | 🇳🇴 NO | 2534 |
| 16 | 🇨🇭 CH | 2380 |
| 17 | 🇲🇾 MY | 2011 |
| 18 | 🇹🇷 TR | 1653 |
| 19 | 🇿🇦 ZA | 1647 |
| 20 | 🇳🇿 NZ | 1555 |
| 21 | 🇹🇭 TH | 1538 |
| 22 | 🇵🇱 PL | 1489 |
| 23 | 🇰🇷 KR | 1417 |
| 24 | 🇵🇭 PH | 1387 |
| 25 | 🇬🇹 GT | 1351 |
| 26 | 🇲🇦 MA | 1047 |
| 27 | 🇲🇴 MO | 1035 |
| 28 | 🇳🇱 NL | 919 |
| 29 | 🇲🇪 ME | 919 |
| 30 | 🇭🇷 HR | 821 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1976 |
| 2 | Denver International Airport |  | US | 1516 |
| 3 | Tokyo International Airport |  | JP | 1468 |
| 4 | Indira Gandhi International Airport |  | IN | 1296 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1225 |
| 6 | Harry Reid International Airport |  | US | 1158 |
| 7 | Frankfurt am Main International Airport |  | DE | 1128 |
| 8 | Guaymaral Airport |  | CO | 1075 |
| 9 | Zurich Airport |  | CH | 1071 |
| 10 | Macau International Airport |  | MO | 1035 |
| 11 | La Aurora Airport |  | GT | 1031 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 995 |
| 13 | El Dorado International Airport |  | CO | 985 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 917 |
| 15 | Chicago O'Hare International Airport |  | US | 872 |
| 16 | Madrid Barajas International Airport |  | ES | 821 |
| 17 | Kuala Lumpur International Airport |  | MY | 796 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 773 |
| 19 | Capua Airport |  | IT | 761 |
| 20 | Salt Lake City International Airport |  | US | 760 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 733 |
| 22 | Malpensa International Airport |  | IT | 730 |
| 23 | Bengaluru International Airport |  | IN | 717 |
| 24 | Charles de Gaulle International Airport |  | FR | 709 |
| 25 | Charlotte/Douglas International Airport |  | US | 696 |
| 26 | Congonhas Airport |  | BR | 693 |
| 27 | Daniel K Inouye International Airport |  | US | 661 |
| 28 | Tenerife Norte Airport |  | ES | 660 |
| 29 | Ninoy Aquino International Airport |  | PH | 637 |
| 30 | Barcelona International Airport |  | ES | 611 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 600 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 597 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 593 |
| 34 | Vitoria/Foronda Airport |  | ES | 574 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 571 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 37 | Don Mueang International Airport |  | TH | 565 |
| 38 | Amsterdam Airport Schiphol |  | NL | 564 |
| 39 | Calgary International Airport |  | CA | 537 |
| 40 | O. R. Tambo International Airport |  | ZA | 521 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 440 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 336 | 21m | 244 km | 1,414.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 249 | 24m | 225 km | 966.0 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 236 | 14m | 114 km | 462.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 234 | 9m | - | - |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 232 | 1h 26m | 910 km | 3,640.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 231 | 28m | 304 km | 1,211.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 208 | 1h 10m | 770 km | 2,763.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 196 | 19m | 165 km | 557.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 188 | 26m | 275 km | 890.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 138 | 31m | 369 km | 878.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 135 | 27m | 215 km | 500.0 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 135 | 22m | 55 km | 128.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 129 | 14m | 154 km | 341.8 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 117 | 18m | 144 km | 291.0 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 116 | 13m | - | - |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 111 | 1h 40m | 1,156 km | 2,214.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N23HS |  | John Wayne/Orange County Airport (KSNA) | Corona Municipal Airport (KAJO) | 2026-05-21 17:38 UTC | 2026-05-21 19:02 UTC | 1h 24m |
| PGT39EA | PGT | Trabzon International Airport (LTCG) | Sabiha Gokcen International Airport (LTFJ) | 2026-05-21 17:51 UTC | 2026-05-21 18:59 UTC | 1h 8m |
| N555BG |  | Grand Junction Regional Airport (KGJT) | Telluride Regional Airport (KTEX) | 2026-05-21 18:39 UTC | 2026-05-21 18:59 UTC | 20m |
| N8158N |  | K4A7 (K4A7) | K4A7 (K4A7) | 2026-05-21 18:43 UTC | 2026-05-21 18:58 UTC | 15m |
| N801FL |  | Baldwin Airport (WI14) | Baldwin Airport (WI14) | 2026-05-21 18:42 UTC | 2026-05-21 18:53 UTC | 11m |
| N821SR |  | Double Eagle Ii Airport (KAEG) | Las Arenas Earth And Sky Observatory Airport (2CO2) | 2026-05-21 17:38 UTC | 2026-05-21 18:49 UTC | 1h 11m |
| N9055F |  | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-05-21 18:00 UTC | 2026-05-21 18:47 UTC | 47m |
| N11QX |  | Kawaihapai Airfield (PHDH) | Daniel K Inouye International Airport (PHNL) | 2026-05-21 18:21 UTC | 2026-05-21 18:45 UTC | 24m |
| CGKIX | CGK | Winnipeg James Armstrong Richardson International Airport (CYWG) | Winnipeg James Armstrong Richardson International Airport (CYWG) | 2026-05-21 18:28 UTC | 2026-05-21 18:45 UTC | 16m |
| OEGTX | OEG | Braunschweig Wolfsburg Airport (EDVE) | Salzburg Airport (LOWS) | 2026-05-21 17:56 UTC | 2026-05-21 18:44 UTC | 47m |
| EXP800 | EXP | Ketchikan International Airport (PAKT) | Sitka Rocky Gutierrez Airport (PASI) | 2026-05-21 17:51 UTC | 2026-05-21 18:41 UTC | 49m |
| N62SH |  | Phoenix Deer Valley Airport (KDVT) | Cottonwood Airport (KP52) | 2026-05-21 18:25 UTC | 2026-05-21 18:41 UTC | 15m |
| N776GX |  | Bend Municipal Airport (KBDN) | Dry Creek Airpark (OG21) | 2026-05-21 18:31 UTC | 2026-05-21 18:38 UTC | 6m |
| CGHAP | CGH | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-05-21 18:21 UTC | 2026-05-21 18:37 UTC | 16m |
| EJA632 | EJA | Oakland San Francisco Bay Airport (KOAK) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-21 18:36 UTC | 2026-05-21 18:36 UTC | 0m |
| MNL14 | MNL | NV13 (NV13) | Moffett Federal Airfield (KNUQ) | 2026-05-21 17:59 UTC | 2026-05-21 18:36 UTC | 37m |
| N9957M |  | Homer Airport (PAHO) | Longmere Lake Air Strip (AK07) | 2026-05-21 18:21 UTC | 2026-05-21 18:36 UTC | 14m |
| N418TJ |  | Aurora Municipal Airport (KARR) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-21 18:27 UTC | 2026-05-21 18:35 UTC | 8m |
| N51CU |  | MS18 (MS18) | Smith County Airport (MS39) | 2026-05-21 18:02 UTC | 2026-05-21 18:35 UTC | 32m |
| N594AF |  | New Castle Airport (KILG) | L.F. Wade International International Airport (TXKF) | 2026-05-21 16:40 UTC | 2026-05-21 18:34 UTC | 1h 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
