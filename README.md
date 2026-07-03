# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_01:07:22_UTC-green)

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

**Latest saved flight:** 2026-07-03 01:07:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-03 01:07:22 UTC

- **126,865** saved flights
- **43,305** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **126,865** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,530,241.8 tonnes** estimated CO2 emissions
- **88,709,669 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5137 |
| 2 | SkyWest Airlines | 4692 |
| 3 | EJA | 2499 |
| 4 | IndiGo | 2396 |
| 5 | American Airlines | 1950 |
| 6 | Southwest Airlines | 1904 |
| 7 | ENY | 1594 |
| 8 | Delta Air Lines | 1512 |
| 9 | Lufthansa | 1350 |
| 10 | LATAM Airlines | 1153 |
| 11 | Vueling | 1121 |
| 12 | WIF | 1115 |
| 13 | AZU | 1072 |
| 14 | AXM | 999 |
| 15 | LXJ | 990 |
| 16 | Swiss International | 879 |
| 17 | All Nippon Airways | 852 |
| 18 | Alaska Airlines | 824 |
| 19 | easyJet | 809 |
| 20 | QLK | 802 |
| 21 | EJU | 784 |
| 22 | Cathay Pacific | 705 |
| 23 | VIV | 697 |
| 24 | AEE | 695 |
| 25 | Air France | 692 |
| 26 | CXK | 681 |
| 27 | United Airlines | 674 |
| 28 | MXY | 660 |
| 29 | JetBlue | 652 |
| 30 | GLO | 639 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 108634 |
| 2 | 🇪🇸 ES | 8439 |
| 3 | 🇮🇳 IN | 7518 |
| 4 | 🇦🇺 AU | 7419 |
| 5 | 🇧🇷 BR | 7090 |
| 6 | 🇩🇪 DE | 6682 |
| 7 | 🇨🇦 CA | 6675 |
| 8 | 🇮🇹 IT | 6648 |
| 9 | 🇬🇧 GB | 5587 |
| 10 | 🇯🇵 JP | 5550 |
| 11 | 🇫🇷 FR | 5004 |
| 12 | 🇨🇴 CO | 4046 |
| 13 | 🇲🇽 MX | 3686 |
| 14 | 🇬🇷 GR | 3600 |
| 15 | 🇳🇴 NO | 3461 |
| 16 | 🇨🇭 CH | 3218 |
| 17 | 🇹🇷 TR | 2674 |
| 18 | 🇲🇾 MY | 2590 |
| 19 | 🇿🇦 ZA | 2089 |
| 20 | 🇵🇱 PL | 2071 |
| 21 | 🇳🇿 NZ | 2051 |
| 22 | 🇹🇭 TH | 1977 |
| 23 | 🇰🇷 KR | 1953 |
| 24 | 🇵🇭 PH | 1796 |
| 25 | 🇬🇹 GT | 1743 |
| 26 | 🇲🇦 MA | 1357 |
| 27 | 🇲🇪 ME | 1253 |
| 28 | 🇳🇱 NL | 1193 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇧🇸 BS | 1098 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2654 |
| 2 | Denver International Airport |  | US | 2141 |
| 3 | Tokyo International Airport |  | JP | 1830 |
| 4 | Indira Gandhi International Airport |  | IN | 1654 |
| 5 | Harry Reid International Airport |  | US | 1589 |
| 6 | Guaymaral Airport |  | CO | 1533 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1508 |
| 8 | Zurich Airport |  | CH | 1392 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1351 |
| 10 | La Aurora Airport |  | GT | 1347 |
| 11 | Frankfurt am Main International Airport |  | DE | 1304 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1244 |
| 13 | Chicago O'Hare International Airport |  | US | 1227 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1120 |
| 17 | Capua Airport |  | IT | 1067 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1052 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1045 |
| 20 | Madrid Barajas International Airport |  | ES | 1041 |
| 21 | Kuala Lumpur International Airport |  | MY | 1007 |
| 22 | Congonhas Airport |  | BR | 996 |
| 23 | Charlotte/Douglas International Airport |  | US | 952 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 934 |
| 25 | Charles de Gaulle International Airport |  | FR | 923 |
| 26 | Bengaluru International Airport |  | IN | 909 |
| 27 | Malpensa International Airport |  | IT | 868 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 848 |
| 29 | Ninoy Aquino International Airport |  | PH | 832 |
| 30 | Daniel K Inouye International Airport |  | US | 806 |
| 31 | Barcelona International Airport |  | ES | 790 |
| 32 | Tenerife Norte Airport |  | ES | 776 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 770 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 745 |
| 35 | Calgary International Airport |  | CA | 741 |
| 36 | Scottsdale Airport |  | US | 736 |
| 37 | Seattle-Tacoma International Airport |  | US | 734 |
| 38 | Vitoria/Foronda Airport |  | ES | 725 |
| 39 | Viracopos International Airport |  | BR | 723 |
| 40 | Amsterdam Airport Schiphol |  | NL | 720 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 639 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 461 | 21m | 244 km | 1,941.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 326 | 24m | 225 km | 1,264.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 318 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 306 | 1h 10m | 770 km | 4,065.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 243 | 26m | 275 km | 1,151.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 235 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 187 | 22m | 55 km | 177.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 175 | 44m | 241 km | 726.9 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 162 | 1h 45m | 1,423 km | 3,975.7 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 161 | 31m | 369 km | 1,024.8 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 153 | 20m | 250 km | 660.9 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 152 | 30m | 49 km | 128.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 148 | 1h 1m | 695 km | 1,774.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 147 | 1h 17m | 961 km | 2,436.6 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 140 | 54m | 136 km | 328.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5280F |  | William P Hobby Airport (KHOU) | 8TX7 (8TX7) | 2026-07-03 00:19 UTC | 2026-07-03 01:07 UTC | 48m |
| LXJ428 | LXJ | Moffett Federal Airfield (KNUQ) | Vancouver International Airport (CYVR) | 2026-07-02 22:59 UTC | 2026-07-03 00:56 UTC | 1h 57m |
| BRG644 | BRG | Buckland Airport (PABL) | Deering Airport (PADE) | 2026-07-03 00:39 UTC | 2026-07-03 00:53 UTC | 13m |
| CXK337 | CXK | Denton Enterprise Airport (KDTO) | 69XA (69XA) | 2026-07-02 23:38 UTC | 2026-07-03 00:47 UTC | 1h 9m |
| N628SR |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-07-03 00:07 UTC | 2026-07-03 00:43 UTC | 36m |
| N62112 |  | John C Tune Airport (KJWN) | John C Tune Airport (KJWN) | 2026-07-03 00:24 UTC | 2026-07-03 00:42 UTC | 17m |
| BRG605 | BRG | Ralph Wien Memorial Airport (PAOT) | Deering Airport (PADE) | 2026-07-03 00:14 UTC | 2026-07-03 00:42 UTC | 27m |
| SCA77 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-07-03 00:18 UTC | 2026-07-03 00:41 UTC | 23m |
| N510PR |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-02 23:51 UTC | 2026-07-03 00:41 UTC | 50m |
| N690SG |  | Blanding Municipal Airport (KBDG) | Blanding Municipal Airport (KBDG) | 2026-07-03 00:01 UTC | 2026-07-03 00:35 UTC | 33m |
| CPA694 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-07-02 20:04 UTC | 2026-07-03 00:35 UTC | 4h 31m |
| N5921C |  | Camarillo Airport (KCMA) | Lake Tahoe Airport (KTVL) | 2026-07-02 22:22 UTC | 2026-07-03 00:35 UTC | 2h 12m |
| N797GM |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-07-02 23:57 UTC | 2026-07-03 00:34 UTC | 37m |
| TVR4727 | TVR | Ras Tanura Airport (OERT) | Zhuhai Airport (ZGSD) | 2026-07-02 16:53 UTC | 2026-07-03 00:32 UTC | 7h 39m |
| N721SE |  | Salt Lake City International Airport (KSLC) | Burley Municipal Airport (KBYI) | 2026-07-03 00:03 UTC | 2026-07-03 00:32 UTC | 28m |
| FKH8021 | FKH | Chek Lap Kok International Airport (VHHH) | Zhuhai Airport (ZGSD) | 2026-07-01 11:11 UTC | 2026-07-03 00:28 UTC | 37h 17m |
| AM340 |  | Albury Airport (YMAY) | Shepparton Airport (YSHT) | 2026-07-02 23:54 UTC | 2026-07-03 00:23 UTC | 28m |
| N228SB |  | Denver International Airport (KDEN) | 25NE (25NE) | 2026-07-03 00:01 UTC | 2026-07-03 00:22 UTC | 20m |
| EQK | EQK | Adelaide Parafield Airport (YPPF) | Adelaide Parafield Airport (YPPF) | 2026-07-02 23:37 UTC | 2026-07-03 00:21 UTC | 43m |
| SKW6513 | SkyWest Airlines | Los Angeles International Airport (KLAX) | Los Alamos Airport (KLAM) | 2026-07-02 22:52 UTC | 2026-07-03 00:20 UTC | 1h 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
