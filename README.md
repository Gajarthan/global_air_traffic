# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_00:26:00_UTC-green)

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

**Latest saved flight:** 2026-08-09 00:26:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 00:26:00 UTC

- **180,033** saved flights
- **57,694** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **180,033** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,163,988.7 tonnes** estimated CO2 emissions
- **125,448,622 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7126 |
| 2 | SkyWest Airlines | 6581 |
| 3 | EJA | 3552 |
| 4 | IndiGo | 3146 |
| 5 | Southwest Airlines | 2839 |
| 6 | American Airlines | 2814 |
| 7 | ENY | 2249 |
| 8 | Delta Air Lines | 2141 |
| 9 | LATAM Airlines | 1679 |
| 10 | AZU | 1613 |
| 11 | Lufthansa | 1600 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1487 |
| 14 | LXJ | 1406 |
| 15 | easyJet | 1229 |
| 16 | Swiss International | 1225 |
| 17 | AXM | 1211 |
| 18 | EJU | 1095 |
| 19 | QLK | 1095 |
| 20 | Alaska Airlines | 1092 |
| 21 | All Nippon Airways | 1090 |
| 22 | VIV | 995 |
| 23 | GLO | 964 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 946 |
| 26 | AEE | 936 |
| 27 | United Airlines | 929 |
| 28 | Air France | 924 |
| 29 | MXY | 904 |
| 30 | PGT | 896 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154540 |
| 2 | 🇪🇸 ES | 11553 |
| 3 | 🇧🇷 BR | 10342 |
| 4 | 🇦🇺 AU | 10093 |
| 5 | 🇮🇳 IN | 9863 |
| 6 | 🇨🇦 CA | 9836 |
| 7 | 🇮🇹 IT | 9285 |
| 8 | 🇩🇪 DE | 8896 |
| 9 | 🇬🇧 GB | 8307 |
| 10 | 🇯🇵 JP | 7241 |
| 11 | 🇫🇷 FR | 7153 |
| 12 | 🇨🇴 CO | 6701 |
| 13 | 🇬🇷 GR | 5243 |
| 14 | 🇲🇽 MX | 5158 |
| 15 | 🇨🇭 CH | 4789 |
| 16 | 🇳🇴 NO | 4646 |
| 17 | 🇹🇷 TR | 4584 |
| 18 | 🇲🇾 MY | 3160 |
| 19 | 🇵🇱 PL | 2999 |
| 20 | 🇿🇦 ZA | 2922 |
| 21 | 🇹🇭 TH | 2719 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2370 |
| 24 | 🇬🇹 GT | 2294 |
| 25 | 🇰🇷 KR | 2247 |
| 26 | 🇲🇦 MA | 1816 |
| 27 | 🇭🇷 HR | 1793 |
| 28 | 🇲🇪 ME | 1635 |
| 29 | 🇳🇱 NL | 1616 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3731 |
| 2 | Denver International Airport |  | US | 2987 |
| 3 | Tokyo International Airport |  | JP | 2249 |
| 4 | Guaymaral Airport |  | CO | 2222 |
| 5 | Indira Gandhi International Airport |  | IN | 2197 |
| 6 | Harry Reid International Airport |  | US | 2123 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1934 |
| 8 | Zurich Airport |  | CH | 1909 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1762 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1647 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | Salt Lake City International Airport |  | US | 1614 |
| 14 | El Dorado International Airport |  | CO | 1611 |
| 15 | Frankfurt am Main International Airport |  | DE | 1564 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1500 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1434 |
| 19 | Madrid Barajas International Airport |  | ES | 1409 |
| 20 | Capua Airport |  | IT | 1401 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1349 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1283 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1253 |
| 24 | Malpensa International Airport |  | IT | 1240 |
| 25 | Charlotte/Douglas International Airport |  | US | 1224 |
| 26 | Charles de Gaulle International Airport |  | FR | 1216 |
| 27 | Kuala Lumpur International Airport |  | MY | 1191 |
| 28 | Bengaluru International Airport |  | IN | 1175 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1121 |
| 30 | Ninoy Aquino International Airport |  | PH | 1115 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1108 |
| 32 | Barcelona International Airport |  | ES | 1072 |
| 33 | Seattle-Tacoma International Airport |  | US | 1040 |
| 34 | Viracopos International Airport |  | BR | 1036 |
| 35 | Daniel K Inouye International Airport |  | US | 1033 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1028 |
| 38 | Oslo Gardermoen Airport |  | NO | 998 |
| 39 | Tenerife Norte Airport |  | ES | 983 |
| 40 | Amsterdam Airport Schiphol |  | NL | 973 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 663 | 21m | 244 km | 2,791.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 422 | 24m | 225 km | 1,637.2 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 421 | 1h 8m | 770 km | 5,592.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 301 | 27m | 275 km | 1,426.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 252 | 1h 48m | 1,423 km | 6,184.5 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 241 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 218 | 1h 15m | 961 km | 3,613.5 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 217 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 215 | 19m | 144 km | 534.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 211 | 1h 38m | 1,156 km | 4,209.4 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 207 | 31m | 369 km | 1,317.6 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 205 | 24m | 218 km | 772.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N278SP |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-08-08 23:26 UTC | 2026-08-09 00:26 UTC | 59m |
| MSR802 | EgyptAir | Charles de Gaulle International Airport (LFPG) | HE42 (HE42) | 2026-08-08 20:28 UTC | 2026-08-09 00:12 UTC | 3h 43m |
| TKR103 | TKR | Hill Afb Airport (KHIF) | Morgan County Airport (K42U) | 2026-08-09 00:07 UTC | 2026-08-09 00:11 UTC | 4m |
| N17PJ |  | Raleigh-Durham International Airport (KRDU) | Capital City Airport (KCXY) | 2026-08-08 23:07 UTC | 2026-08-09 00:03 UTC | 55m |
| MSR910 | EgyptAir | HE13 (HE13) | Sirri Island Airport (OIBS) | 2026-08-08 21:24 UTC | 2026-08-09 00:01 UTC | 2h 37m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-08 23:43 UTC | 2026-08-08 23:58 UTC | 14m |
| 051465 |  | Scott Valley Airport (KA30) | Redding Regional Airport (KRDD) | 2026-08-08 23:46 UTC | 2026-08-08 23:57 UTC | 11m |
| CUL550 | CUL | Independence Airport (K2O7) | Mammoth Yosemite Airport (KMMH) | 2026-08-08 23:24 UTC | 2026-08-08 23:50 UTC | 26m |
| QLK20D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Woodville Airport (YWVL) | 2026-08-08 23:07 UTC | 2026-08-08 23:50 UTC | 42m |
| N5283K |  | Astoria Regional Airport (KAST) | Newport Municipal Airport (KONP) | 2026-08-08 22:51 UTC | 2026-08-08 23:47 UTC | 56m |
| N408CA |  | Ramona Airport (KRNM) | Gillespie Field (KSEE) | 2026-08-08 23:25 UTC | 2026-08-08 23:43 UTC | 18m |
| TKK62 | TKK | Bob Hope Airport (KBUR) | SN28 (SN28) | 2026-08-08 21:01 UTC | 2026-08-08 23:43 UTC | 2h 41m |
| EJA481 | EJA | San Diego International Airport (KSAN) | Rocky Mountain Metro Airport (KBJC) | 2026-08-08 21:40 UTC | 2026-08-08 23:42 UTC | 2h 1m |
| FAG706 | FAG | La Aurora Airport (MGGT) | Santa Cruz del Quiche Airport (MGQC) | 2026-08-08 23:29 UTC | 2026-08-08 23:41 UTC | 12m |
| APG211 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-08-08 23:13 UTC | 2026-08-08 23:40 UTC | 27m |
| CTF684 | CTF | Centennial Airport (KAPA) | Scottsdale Airport (KSDL) | 2026-08-08 22:19 UTC | 2026-08-08 23:39 UTC | 1h 19m |
| SCU40 | SCU | 2OL2 (2OL2) | 2OL2 (2OL2) | 2026-08-08 23:38 UTC | 2026-08-08 23:39 UTC | 0m |
| N703LB |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-08-08 23:19 UTC | 2026-08-08 23:36 UTC | 17m |
| ANA1891 | All Nippon Airways | Tokyo International Airport (RJTT) | Kozushima Airport (RJAZ) | 2026-08-08 23:13 UTC | 2026-08-08 23:36 UTC | 22m |
| ZFN | ZFN | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-08-08 23:02 UTC | 2026-08-08 23:35 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
