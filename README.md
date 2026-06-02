# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_01:38:02_UTC-green)

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

**Latest saved flight:** 2026-06-02 01:38:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-02 01:38:02 UTC

- **100,698** saved flights
- **35,740** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **100,698** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,232,944.5 tonnes** estimated CO2 emissions
- **71,475,043 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4158 |
| 2 | SkyWest Airlines | 3790 |
| 3 | IndiGo | 2027 |
| 4 | EJA | 1922 |
| 5 | American Airlines | 1631 |
| 6 | Southwest Airlines | 1529 |
| 7 | ENY | 1257 |
| 8 | Delta Air Lines | 1186 |
| 9 | Lufthansa | 1176 |
| 10 | Vueling | 941 |
| 11 | LATAM Airlines | 897 |
| 12 | WIF | 879 |
| 13 | AXM | 867 |
| 14 | AZU | 811 |
| 15 | LXJ | 761 |
| 16 | Swiss International | 732 |
| 17 | All Nippon Airways | 716 |
| 18 | Alaska Airlines | 704 |
| 19 | QLK | 677 |
| 20 | easyJet | 655 |
| 21 | EJU | 633 |
| 22 | Cathay Pacific | 605 |
| 23 | AEE | 588 |
| 24 | Air France | 581 |
| 25 | VIV | 581 |
| 26 | United Airlines | 565 |
| 27 | CXK | 542 |
| 28 | MXY | 539 |
| 29 | Japan Airlines | 508 |
| 30 | AXB | 498 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 84444 |
| 2 | 🇪🇸 ES | 6966 |
| 3 | 🇮🇳 IN | 6403 |
| 4 | 🇦🇺 AU | 6099 |
| 5 | 🇧🇷 BR | 5506 |
| 6 | 🇩🇪 DE | 5445 |
| 7 | 🇮🇹 IT | 5363 |
| 8 | 🇨🇦 CA | 5198 |
| 9 | 🇯🇵 JP | 4675 |
| 10 | 🇬🇧 GB | 4279 |
| 11 | 🇫🇷 FR | 4018 |
| 12 | 🇨🇴 CO | 3495 |
| 13 | 🇲🇽 MX | 3048 |
| 14 | 🇬🇷 GR | 2870 |
| 15 | 🇳🇴 NO | 2786 |
| 16 | 🇨🇭 CH | 2597 |
| 17 | 🇲🇾 MY | 2204 |
| 18 | 🇹🇷 TR | 1910 |
| 19 | 🇿🇦 ZA | 1753 |
| 20 | 🇳🇿 NZ | 1691 |
| 21 | 🇹🇭 TH | 1674 |
| 22 | 🇰🇷 KR | 1634 |
| 23 | 🇵🇱 PL | 1618 |
| 24 | 🇬🇹 GT | 1491 |
| 25 | 🇵🇭 PH | 1469 |
| 26 | 🇲🇦 MA | 1129 |
| 27 | 🇲🇴 MO | 1066 |
| 28 | 🇳🇱 NL | 1003 |
| 29 | 🇲🇪 ME | 960 |
| 30 | 🇭🇷 HR | 889 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2199 |
| 2 | Denver International Airport |  | US | 1731 |
| 3 | Tokyo International Airport |  | JP | 1552 |
| 4 | Indira Gandhi International Airport |  | IN | 1392 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1294 |
| 6 | Harry Reid International Airport |  | US | 1288 |
| 7 | Guaymaral Airport |  | CO | 1262 |
| 8 | Frankfurt am Main International Airport |  | DE | 1180 |
| 9 | Zurich Airport |  | CH | 1151 |
| 10 | La Aurora Airport |  | GT | 1146 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1092 |
| 12 | El Dorado International Airport |  | CO | 1074 |
| 13 | Macau International Airport |  | MO | 1066 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1022 |
| 15 | Chicago O'Hare International Airport |  | US | 1012 |
| 16 | Madrid Barajas International Airport |  | ES | 876 |
| 17 | Kuala Lumpur International Airport |  | MY | 872 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 867 |
| 19 | Salt Lake City International Airport |  | US | 854 |
| 20 | Capua Airport |  | IT | 832 |
| 21 | Charlotte/Douglas International Airport |  | US | 784 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 783 |
| 23 | Charles de Gaulle International Airport |  | FR | 772 |
| 24 | Malpensa International Airport |  | IT | 767 |
| 25 | Bengaluru International Airport |  | IN | 767 |
| 26 | Congonhas Airport |  | BR | 766 |
| 27 | Daniel K Inouye International Airport |  | US | 696 |
| 28 | Tenerife Norte Airport |  | ES | 693 |
| 29 | Ninoy Aquino International Airport |  | PH | 671 |
| 30 | Barcelona International Airport |  | ES | 666 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 658 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 656 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 643 |
| 34 | Amsterdam Airport Schiphol |  | NL | 619 |
| 35 | Don Mueang International Airport |  | TH | 613 |
| 36 | Vitoria/Foronda Airport |  | ES | 611 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 590 |
| 39 | Seattle-Tacoma International Airport |  | US | 580 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 573 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 520 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 366 | 21m | 244 km | 1,541.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 269 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 265 | 24m | 225 km | 1,028.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 247 | 1h 26m | 910 km | 3,876.0 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 243 | 28m | 304 km | 1,273.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 231 | 1h 10m | 770 km | 3,068.7 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 211 | 19m | 165 km | 600.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 197 | 26m | 275 km | 933.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 157 | 20m | 99 km | 268.9 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 149 | 27m | 215 km | 551.8 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 146 | 22m | 55 km | 138.8 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 141 | 31m | 369 km | 897.5 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 132 | 13m | - | - |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 130 | 20m | 147 km | 329.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 130 | 18m | 144 km | 323.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 127 | 1h 39m | 1,156 km | 2,533.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 126 | 1h 1m | 695 km | 1,510.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RPA4644 | Republic Airways | Laguardia Airport (KLGA) | AR84 (AR84) | 2026-06-01 22:58 UTC | 2026-06-02 01:38 UTC | 2h 39m |
| SVY314 | SVY | Don Mueang International Airport (VTBD) | Watthana Nakhon Airport (VTBW) | 2026-06-02 00:31 UTC | 2026-06-02 01:31 UTC | 1h 0m |
| XLV | XLV | Collinsville Airport (YCSV) | Lakeside Airpark (YLAK) | 2026-06-01 22:01 UTC | 2026-06-02 01:30 UTC | 3h 29m |
| N43FA |  | Lakeland Linder International Airport (KLAL) | Lakeland Linder International Airport (KLAL) | 2026-06-02 01:23 UTC | 2026-06-02 01:27 UTC | 3m |
| N950TT |  | Lanai Airport (PHNY) | Kawaihapai Airfield (PHDH) | 2026-06-02 01:10 UTC | 2026-06-02 01:24 UTC | 13m |
| YNG | YNG | Watts Bridge Airport (YWSG) | Sunshine Coast Airport (YBMC) | 2026-06-02 01:00 UTC | 2026-06-02 01:18 UTC | 17m |
| C2703 |  | Mc Clellan Airfield (KMCC) | Hayfork Airport (KF62) | 2026-06-02 00:20 UTC | 2026-06-02 01:15 UTC | 55m |
| FGD563 | FGD | Green Lake Airport (CBG2) | Quesnel Airport (CYQZ) | 2026-06-02 00:44 UTC | 2026-06-02 01:15 UTC | 31m |
| N303HB |  | Newton-City-County Airport (KEWK) | Newton-City-County Airport (KEWK) | 2026-06-02 00:09 UTC | 2026-06-02 01:13 UTC | 1h 3m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-06-02 00:55 UTC | 2026-06-02 01:12 UTC | 17m |
| N320KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-02 00:10 UTC | 2026-06-02 01:08 UTC | 57m |
| N713PM |  | Birdwin Airport (7LA1) | St Tammany Regional Airport (KL31) | 2026-06-02 00:23 UTC | 2026-06-02 01:05 UTC | 42m |
| LBQ792 | LBQ | Reading Regional/Carl A Spaatz Field (KRDG) | PN21 (PN21) | 2026-06-02 00:33 UTC | 2026-06-02 01:03 UTC | 30m |
| N885RS |  | Stellar Airpark (KP19) | Cottonwood Airport (KP52) | 2026-06-02 00:41 UTC | 2026-06-02 01:02 UTC | 20m |
| N38RA |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-06-02 00:36 UTC | 2026-06-02 01:01 UTC | 24m |
| E3D |  | Perth Jandakot Airport (YPJT) | Garden Island (Military) Airport (YGAD) | 2026-06-02 00:47 UTC | 2026-06-02 01:00 UTC | 13m |
| FYC | FYC | Lakeside Airpark (YLAK) | Lakeside Airpark (YLAK) | 2026-06-02 00:29 UTC | 2026-06-02 00:59 UTC | 29m |
| SWA440 | Southwest Airlines | San Diego International Airport (KSAN) | Oakland San Francisco Bay Airport (KOAK) | 2026-06-01 23:56 UTC | 2026-06-02 00:58 UTC | 1h 1m |
| JJA104 | JJA | Gwangju Airport (RKJJ) | Gimpo International Airport (RKSS) | 2026-06-02 00:24 UTC | 2026-06-02 00:54 UTC | 30m |
| RAIDR29 | RAI | Miramar Mcas (Joe Foss Field) Airport (KNKX) | Emory Ranch Airport (0CA6) | 2026-06-02 00:32 UTC | 2026-06-02 00:54 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
