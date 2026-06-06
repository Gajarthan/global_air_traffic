# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_03:56:24_UTC-green)

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

**Latest saved flight:** 2026-06-06 03:56:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-06 03:56:24 UTC

- **103,403** saved flights
- **36,569** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **103,403** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,262,786.2 tonnes** estimated CO2 emissions
- **73,204,999 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4238 |
| 2 | SkyWest Airlines | 3898 |
| 3 | IndiGo | 2061 |
| 4 | EJA | 1983 |
| 5 | American Airlines | 1672 |
| 6 | Southwest Airlines | 1566 |
| 7 | ENY | 1289 |
| 8 | Delta Air Lines | 1226 |
| 9 | Lufthansa | 1191 |
| 10 | Vueling | 952 |
| 11 | LATAM Airlines | 916 |
| 12 | WIF | 907 |
| 13 | AXM | 891 |
| 14 | AZU | 830 |
| 15 | LXJ | 782 |
| 16 | Swiss International | 744 |
| 17 | All Nippon Airways | 728 |
| 18 | Alaska Airlines | 722 |
| 19 | QLK | 696 |
| 20 | easyJet | 669 |
| 21 | EJU | 645 |
| 22 | Cathay Pacific | 618 |
| 23 | AEE | 600 |
| 24 | VIV | 594 |
| 25 | Air France | 590 |
| 26 | United Airlines | 574 |
| 27 | MXY | 560 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 514 |
| 30 | AXB | 507 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 87144 |
| 2 | 🇪🇸 ES | 7089 |
| 3 | 🇮🇳 IN | 6512 |
| 4 | 🇦🇺 AU | 6295 |
| 5 | 🇧🇷 BR | 5650 |
| 6 | 🇩🇪 DE | 5541 |
| 7 | 🇮🇹 IT | 5471 |
| 8 | 🇨🇦 CA | 5385 |
| 9 | 🇯🇵 JP | 4766 |
| 10 | 🇬🇧 GB | 4350 |
| 11 | 🇫🇷 FR | 4090 |
| 12 | 🇨🇴 CO | 3553 |
| 13 | 🇲🇽 MX | 3110 |
| 14 | 🇬🇷 GR | 2935 |
| 15 | 🇳🇴 NO | 2874 |
| 16 | 🇨🇭 CH | 2639 |
| 17 | 🇲🇾 MY | 2271 |
| 18 | 🇹🇷 TR | 1954 |
| 19 | 🇿🇦 ZA | 1790 |
| 20 | 🇳🇿 NZ | 1741 |
| 21 | 🇹🇭 TH | 1702 |
| 22 | 🇰🇷 KR | 1697 |
| 23 | 🇵🇱 PL | 1649 |
| 24 | 🇵🇭 PH | 1522 |
| 25 | 🇬🇹 GT | 1509 |
| 26 | 🇲🇦 MA | 1138 |
| 27 | 🇲🇴 MO | 1083 |
| 28 | 🇳🇱 NL | 1017 |
| 29 | 🇲🇪 ME | 970 |
| 30 | 🇭🇷 HR | 903 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2253 |
| 2 | Denver International Airport |  | US | 1776 |
| 3 | Tokyo International Airport |  | JP | 1582 |
| 4 | Indira Gandhi International Airport |  | IN | 1412 |
| 5 | Harry Reid International Airport |  | US | 1331 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1316 |
| 7 | Guaymaral Airport |  | CO | 1287 |
| 8 | Frankfurt am Main International Airport |  | DE | 1191 |
| 9 | Zurich Airport |  | CH | 1173 |
| 10 | La Aurora Airport |  | GT | 1162 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1120 |
| 12 | El Dorado International Airport |  | CO | 1088 |
| 13 | Macau International Airport |  | MO | 1083 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1050 |
| 15 | Chicago O'Hare International Airport |  | US | 1037 |
| 16 | Madrid Barajas International Airport |  | ES | 899 |
| 17 | Kuala Lumpur International Airport |  | MY | 893 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 888 |
| 19 | Salt Lake City International Airport |  | US | 878 |
| 20 | Capua Airport |  | IT | 856 |
| 21 | Charlotte/Douglas International Airport |  | US | 806 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 803 |
| 23 | Charles de Gaulle International Airport |  | FR | 785 |
| 24 | Congonhas Airport |  | BR | 785 |
| 25 | Bengaluru International Airport |  | IN | 781 |
| 26 | Malpensa International Airport |  | IT | 776 |
| 27 | Daniel K Inouye International Airport |  | US | 711 |
| 28 | Tenerife Norte Airport |  | ES | 703 |
| 29 | Ninoy Aquino International Airport |  | PH | 694 |
| 30 | Barcelona International Airport |  | ES | 678 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 672 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 668 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 662 |
| 34 | Amsterdam Airport Schiphol |  | NL | 629 |
| 35 | Don Mueang International Airport |  | TH | 624 |
| 36 | Vitoria/Foronda Airport |  | ES | 621 |
| 37 | Calgary International Airport |  | CA | 616 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 600 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 590 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 531 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 379 | 21m | 244 km | 1,595.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 274 | 24m | 225 km | 1,063.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 273 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 258 | 14m | 114 km | 506.0 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 252 | 28m | 304 km | 1,321.1 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 252 | 1h 26m | 910 km | 3,954.5 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 237 | 1h 10m | 770 km | 3,148.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 134 | 18m | 144 km | 333.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 132 | 20m | 147 km | 334.0 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 52m | 1,304 km | 2,677.2 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |
| 30 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 118 | 44m | 241 km | 490.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VAR517 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-06-06 03:35 UTC | 2026-06-06 03:56 UTC | 20m |
| N168NW |  | Bordeaux-Merignac (BA 106) Airport (LFBD) | Macau International Airport (VMMC) | 2026-06-05 16:38 UTC | 2026-06-06 03:47 UTC | 11h 8m |
| LNI | LNI | Jurien Bay Airport (YJNB) | Jurien Bay Airport (YJNB) | 2026-06-06 03:33 UTC | 2026-06-06 03:45 UTC | 11m |
| AM221 |  | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-06-06 03:17 UTC | 2026-06-06 03:40 UTC | 23m |
| HKC9492 | HKC | Istanbul Airport (LTFM) | Macau International Airport (VMMC) | 2026-06-05 15:22 UTC | 2026-06-06 03:38 UTC | 12h 15m |
| N727KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-06 03:10 UTC | 2026-06-06 03:37 UTC | 26m |
| CKS9706 | CKS | Ramstein Air Base (ETAR) | Macau International Airport (VMMC) | 2026-06-05 16:15 UTC | 2026-06-06 03:36 UTC | 11h 20m |
| LSI155 | LSI | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-06-05 16:34 UTC | 2026-06-06 03:31 UTC | 10h 56m |
| N929KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-06 02:58 UTC | 2026-06-06 03:29 UTC | 30m |
| N393EA |  | K00V (K00V) | Mann Ranch Airport (95CO) | 2026-06-06 02:43 UTC | 2026-06-06 03:29 UTC | 45m |
| HIGH68 | HIG | Antelope Airpark (93CO) | Fremont County Airport (K1V6) | 2026-06-06 02:43 UTC | 2026-06-06 03:27 UTC | 43m |
| N119SP |  | St Paul Downtown Holman Field (KSTP) | Crystal Airport (KMIC) | 2026-06-06 02:08 UTC | 2026-06-06 03:27 UTC | 1h 18m |
| SKW5697 | SkyWest Airlines | Denver International Airport (KDEN) | Lake County Airport (KLXV) | 2026-06-06 03:02 UTC | 2026-06-06 03:26 UTC | 23m |
| N907KW |  | Healy River Airport (PAHV) | Mc Kinley Country Airport (81AK) | 2026-06-06 02:30 UTC | 2026-06-06 03:20 UTC | 49m |
| QLK1504 | QLK | Cape Barren Island Airport (YCBN) | Sydney Kingsford Smith International Airport (YSSY) | 2026-06-06 02:11 UTC | 2026-06-06 03:16 UTC | 1h 5m |
| IGO7573 | IndiGo | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-06-06 02:39 UTC | 2026-06-06 03:16 UTC | 36m |
| AXM6320 | AXM | Kuala Lumpur International Airport (WMKK) | Penang International Airport (WMKP) | 2026-06-06 02:47 UTC | 2026-06-06 03:15 UTC | 28m |
| CEB897 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-06-06 02:38 UTC | 2026-06-06 03:05 UTC | 26m |
| UAL904 | United Airlines | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-06-06 00:35 UTC | 2026-06-06 03:04 UTC | 2h 29m |
| DOC15 | DOC | Trondheim Airport Vaernes (ENVA) | Trondheim Airport Vaernes (ENVA) | 2026-06-06 03:00 UTC | 2026-06-06 03:04 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
