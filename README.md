# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_23:05:01_UTC-green)

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

**Latest saved flight:** 2026-06-02 23:05:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-02 23:05:01 UTC

- **101,266** saved flights
- **35,921** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **101,266** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,240,115.2 tonnes** estimated CO2 emissions
- **71,890,739 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4184 |
| 2 | SkyWest Airlines | 3807 |
| 3 | IndiGo | 2036 |
| 4 | EJA | 1931 |
| 5 | American Airlines | 1637 |
| 6 | Southwest Airlines | 1533 |
| 7 | ENY | 1259 |
| 8 | Delta Air Lines | 1190 |
| 9 | Lufthansa | 1184 |
| 10 | Vueling | 944 |
| 11 | LATAM Airlines | 900 |
| 12 | WIF | 888 |
| 13 | AXM | 871 |
| 14 | AZU | 818 |
| 15 | LXJ | 762 |
| 16 | Swiss International | 736 |
| 17 | All Nippon Airways | 717 |
| 18 | Alaska Airlines | 707 |
| 19 | QLK | 680 |
| 20 | easyJet | 658 |
| 21 | EJU | 636 |
| 22 | Cathay Pacific | 615 |
| 23 | AEE | 589 |
| 24 | Air France | 586 |
| 25 | VIV | 585 |
| 26 | United Airlines | 566 |
| 27 | CXK | 544 |
| 28 | MXY | 543 |
| 29 | Japan Airlines | 509 |
| 30 | AXB | 500 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 84955 |
| 2 | 🇪🇸 ES | 7004 |
| 3 | 🇮🇳 IN | 6440 |
| 4 | 🇦🇺 AU | 6121 |
| 5 | 🇧🇷 BR | 5537 |
| 6 | 🇩🇪 DE | 5472 |
| 7 | 🇮🇹 IT | 5396 |
| 8 | 🇨🇦 CA | 5248 |
| 9 | 🇯🇵 JP | 4687 |
| 10 | 🇬🇧 GB | 4301 |
| 11 | 🇫🇷 FR | 4038 |
| 12 | 🇨🇴 CO | 3503 |
| 13 | 🇲🇽 MX | 3063 |
| 14 | 🇬🇷 GR | 2881 |
| 15 | 🇳🇴 NO | 2813 |
| 16 | 🇨🇭 CH | 2605 |
| 17 | 🇲🇾 MY | 2219 |
| 18 | 🇹🇷 TR | 1919 |
| 19 | 🇿🇦 ZA | 1765 |
| 20 | 🇳🇿 NZ | 1703 |
| 21 | 🇹🇭 TH | 1679 |
| 22 | 🇰🇷 KR | 1641 |
| 23 | 🇵🇱 PL | 1625 |
| 24 | 🇬🇹 GT | 1499 |
| 25 | 🇵🇭 PH | 1477 |
| 26 | 🇲🇦 MA | 1132 |
| 27 | 🇲🇴 MO | 1074 |
| 28 | 🇳🇱 NL | 1008 |
| 29 | 🇲🇪 ME | 960 |
| 30 | 🇭🇷 HR | 892 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2204 |
| 2 | Denver International Airport |  | US | 1739 |
| 3 | Tokyo International Airport |  | JP | 1556 |
| 4 | Indira Gandhi International Airport |  | IN | 1402 |
| 5 | Harry Reid International Airport |  | US | 1297 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1296 |
| 7 | Guaymaral Airport |  | CO | 1265 |
| 8 | Frankfurt am Main International Airport |  | DE | 1184 |
| 9 | Zurich Airport |  | CH | 1156 |
| 10 | La Aurora Airport |  | GT | 1153 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1095 |
| 12 | El Dorado International Airport |  | CO | 1075 |
| 13 | Macau International Airport |  | MO | 1074 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1026 |
| 15 | Chicago O'Hare International Airport |  | US | 1013 |
| 16 | Madrid Barajas International Airport |  | ES | 881 |
| 17 | Kuala Lumpur International Airport |  | MY | 878 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 872 |
| 19 | Salt Lake City International Airport |  | US | 855 |
| 20 | Capua Airport |  | IT | 838 |
| 21 | Charlotte/Douglas International Airport |  | US | 787 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 785 |
| 23 | Charles de Gaulle International Airport |  | FR | 780 |
| 24 | Malpensa International Airport |  | IT | 770 |
| 25 | Bengaluru International Airport |  | IN | 769 |
| 26 | Congonhas Airport |  | BR | 769 |
| 27 | Daniel K Inouye International Airport |  | US | 698 |
| 28 | Tenerife Norte Airport |  | ES | 697 |
| 29 | Ninoy Aquino International Airport |  | PH | 675 |
| 30 | Barcelona International Airport |  | ES | 669 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 659 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 658 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 646 |
| 34 | Amsterdam Airport Schiphol |  | NL | 623 |
| 35 | Don Mueang International Airport |  | TH | 616 |
| 36 | Vitoria/Foronda Airport |  | ES | 614 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 596 |
| 39 | Seattle-Tacoma International Airport |  | US | 584 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 575 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 521 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 367 | 21m | 244 km | 1,545.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 271 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 265 | 24m | 225 km | 1,028.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 248 | 1h 26m | 910 km | 3,891.7 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 244 | 28m | 304 km | 1,279.1 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 233 | 1h 10m | 770 km | 3,095.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 211 | 19m | 165 km | 600.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 199 | 26m | 275 km | 943.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 158 | 20m | 99 km | 270.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 149 | 27m | 215 km | 551.8 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 148 | 22m | 55 km | 140.7 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 146 | 14m | 154 km | 386.8 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 142 | 31m | 369 km | 903.9 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 135 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 130 | 20m | 147 km | 329.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 130 | 18m | 144 km | 323.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 128 | 1h 39m | 1,156 km | 2,553.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N843TC |  | Bentonville Municipal/Louise M Thaden Field (KVBT) | Sahoma Lake Airport (03OK) | 2026-06-02 22:18 UTC | 2026-06-02 23:05 UTC | 46m |
| USC101 | USC | Charlotte/Douglas International Airport (KCLT) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-06-02 22:22 UTC | 2026-06-02 23:04 UTC | 42m |
| N993CB |  | Bodad Airport (CA11) | Redding Regional Airport (KRDD) | 2026-06-02 22:46 UTC | 2026-06-02 23:01 UTC | 14m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-06-02 11:57 UTC | 2026-06-02 22:59 UTC | 11h 1m |
| BOX728 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-06-02 07:14 UTC | 2026-06-02 22:55 UTC | 15h 40m |
| N6382D |  | Chino Airport (KCNO) | Meadows Field (KBFL) | 2026-06-02 21:31 UTC | 2026-06-02 22:54 UTC | 1h 22m |
| MWH46 | MWH | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-06-02 22:39 UTC | 2026-06-02 22:53 UTC | 14m |
| CFWAL | CFW | Thunder Bay Airport (CYQT) | Kenora Airport (CYQK) | 2026-06-02 19:53 UTC | 2026-06-02 22:51 UTC | 2h 58m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-06-02 22:24 UTC | 2026-06-02 22:50 UTC | 25m |
| N2899J |  | Ted Stevens Anchorage International Airport (PANC) | Nugget Bench Airport (33AK) | 2026-06-02 21:46 UTC | 2026-06-02 22:49 UTC | 1h 3m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-06-02 11:38 UTC | 2026-06-02 22:47 UTC | 11h 8m |
| N734LQ |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-06-02 21:53 UTC | 2026-06-02 22:46 UTC | 52m |
| N61NG |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-06-02 22:07 UTC | 2026-06-02 22:42 UTC | 34m |
| JOLLY21 | JOL | Eielson Afb Airport (PAEI) | Eielson Afb Airport (PAEI) | 2026-06-02 22:04 UTC | 2026-06-02 22:39 UTC | 35m |
| N205FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-06-02 21:52 UTC | 2026-06-02 22:39 UTC | 46m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-06-02 11:02 UTC | 2026-06-02 22:38 UTC | 11h 36m |
| N654T |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-06-02 21:28 UTC | 2026-06-02 22:35 UTC | 1h 7m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Macau International Airport (VMMC) | 2026-06-02 12:12 UTC | 2026-06-02 22:35 UTC | 10h 23m |
| CPA395 | Cathay Pacific | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-06-02 19:52 UTC | 2026-06-02 22:33 UTC | 2h 41m |
| N866SL |  | Zamperini Field (KTOA) | Whiteman Airport (KWHP) | 2026-06-02 21:42 UTC | 2026-06-02 22:32 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
