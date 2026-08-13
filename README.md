# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_03:40:25_UTC-green)

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

**Latest saved flight:** 2026-08-13 03:40:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 03:40:25 UTC

- **191,344** saved flights
- **60,367** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **191,344** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,289,334.9 tonnes** estimated CO2 emissions
- **132,715,066 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7581 |
| 2 | SkyWest Airlines | 6935 |
| 3 | EJA | 3785 |
| 4 | IndiGo | 3316 |
| 5 | Southwest Airlines | 2992 |
| 6 | American Airlines | 2972 |
| 7 | ENY | 2375 |
| 8 | Delta Air Lines | 2253 |
| 9 | LATAM Airlines | 1796 |
| 10 | AZU | 1729 |
| 11 | Lufthansa | 1661 |
| 12 | Vueling | 1584 |
| 13 | WIF | 1584 |
| 14 | LXJ | 1505 |
| 15 | easyJet | 1317 |
| 16 | Swiss International | 1300 |
| 17 | AXM | 1255 |
| 18 | EJU | 1179 |
| 19 | QLK | 1176 |
| 20 | All Nippon Airways | 1157 |
| 21 | Alaska Airlines | 1140 |
| 22 | VIV | 1056 |
| 23 | GLO | 1033 |
| 24 | Air France | 995 |
| 25 | PGT | 989 |
| 26 | CXK | 983 |
| 27 | United Airlines | 977 |
| 28 | AEE | 975 |
| 29 | WMT | 949 |
| 30 | Cathay Pacific | 947 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 163307 |
| 2 | 🇪🇸 ES | 12303 |
| 3 | 🇧🇷 BR | 11012 |
| 4 | 🇦🇺 AU | 10716 |
| 5 | 🇨🇦 CA | 10505 |
| 6 | 🇮🇳 IN | 10380 |
| 7 | 🇮🇹 IT | 9920 |
| 8 | 🇩🇪 DE | 9445 |
| 9 | 🇬🇧 GB | 8897 |
| 10 | 🇯🇵 JP | 7801 |
| 11 | 🇫🇷 FR | 7634 |
| 12 | 🇨🇴 CO | 7385 |
| 13 | 🇬🇷 GR | 5580 |
| 14 | 🇲🇽 MX | 5422 |
| 15 | 🇨🇭 CH | 5109 |
| 16 | 🇹🇷 TR | 5104 |
| 17 | 🇳🇴 NO | 4915 |
| 18 | 🇲🇾 MY | 3283 |
| 19 | 🇿🇦 ZA | 3214 |
| 20 | 🇵🇱 PL | 3158 |
| 21 | 🇹🇭 TH | 2944 |
| 22 | 🇳🇿 NZ | 2696 |
| 23 | 🇵🇭 PH | 2520 |
| 24 | 🇬🇹 GT | 2422 |
| 25 | 🇰🇷 KR | 2337 |
| 26 | 🇭🇷 HR | 1964 |
| 27 | 🇲🇦 MA | 1936 |
| 28 | 🇳🇱 NL | 1705 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇮🇩 ID | 1532 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3982 |
| 2 | Denver International Airport |  | US | 3141 |
| 3 | Tokyo International Airport |  | JP | 2404 |
| 4 | Guaymaral Airport |  | CO | 2365 |
| 5 | Indira Gandhi International Airport |  | IN | 2338 |
| 6 | Harry Reid International Airport |  | US | 2228 |
| 7 | Zurich Airport |  | CH | 2024 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2018 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1982 |
| 10 | La Aurora Airport |  | GT | 1861 |
| 11 | El Dorado International Airport |  | CO | 1733 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1731 |
| 13 | Salt Lake City International Airport |  | US | 1708 |
| 14 | Chicago O'Hare International Airport |  | US | 1680 |
| 15 | Frankfurt am Main International Airport |  | DE | 1627 |
| 16 | Congonhas Airport |  | BR | 1602 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1506 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1481 |
| 20 | Capua Airport |  | IT | 1481 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1415 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1375 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1334 |
| 24 | Malpensa International Airport |  | IT | 1319 |
| 25 | Charles de Gaulle International Airport |  | FR | 1306 |
| 26 | Charlotte/Douglas International Airport |  | US | 1277 |
| 27 | Kuala Lumpur International Airport |  | MY | 1228 |
| 28 | Bengaluru International Airport |  | IN | 1226 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1196 |
| 30 | Ninoy Aquino International Airport |  | PH | 1191 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1176 |
| 32 | Barcelona International Airport |  | ES | 1139 |
| 33 | Viracopos International Airport |  | BR | 1112 |
| 34 | Seattle-Tacoma International Airport |  | US | 1103 |
| 35 | Reno/Tahoe International Airport |  | US | 1097 |
| 36 | Calgary International Airport |  | CA | 1097 |
| 37 | Daniel K Inouye International Airport |  | US | 1074 |
| 38 | Oslo Gardermoen Airport |  | NO | 1069 |
| 39 | Tenerife Norte Airport |  | ES | 1047 |
| 40 | Vitoria/Foronda Airport |  | ES | 1035 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 976 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 702 | 21m | 244 km | 2,955.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 463 | 1h 7m | 770 km | 6,150.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 445 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 443 | 24m | 225 km | 1,718.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 321 | 27m | 275 km | 1,521.1 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 306 | 8m | - | - |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 284 | 44m | 241 km | 1,179.7 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 274 | 1h 49m | 1,423 km | 6,724.4 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 256 | 20m | 250 km | 1,105.8 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 239 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 238 | 27m | 215 km | 881.5 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 234 | 12m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 233 | 1h 15m | 961 km | 3,862.1 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 233 | 19m | 99 km | 399.1 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 228 | 24m | 218 km | 859.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JPT01 | JPT | Halim Perdanakusuma International Airport (WIHH) | Pondok Cabe Air Base (WIHP) | 2026-08-13 03:24 UTC | 2026-08-13 03:40 UTC | 15m |
| GRZLY67 | GRZ | Travis Afb Airport (KSUU) | Travis Afb Airport (KSUU) | 2026-08-13 02:14 UTC | 2026-08-13 03:22 UTC | 1h 7m |
| VPCAK | VPC | Seletar Airport (WSSL) | Senai International Airport (WMKJ) | 2026-08-13 03:09 UTC | 2026-08-13 03:20 UTC | 11m |
| ZKIWG | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-08-13 03:02 UTC | 2026-08-13 03:17 UTC | 15m |
| NMA301 | NMA | Malpensa International Airport (LIMC) | HE12 (HE12) | 2026-08-13 00:02 UTC | 2026-08-13 03:15 UTC | 3h 13m |
| N447JW |  | King Salmon Airport (PAKN) | Plains Airport (KS34) | 2026-08-13 00:06 UTC | 2026-08-13 03:12 UTC | 3h 6m |
| A7GQD |  | Doha International Airport (OTBD) | Al Khawr Airport (OTBK) | 2026-08-13 02:00 UTC | 2026-08-13 03:11 UTC | 1h 10m |
| SRR6118 | SRR | Cologne Bonn Airport (EDDK) | Munich International Airport (EDDM) | 2026-08-13 02:15 UTC | 2026-08-13 03:05 UTC | 49m |
| AAL1357 | American Airlines | Miami International Airport (KMIA) | John F Kennedy International Airport (KJFK) | 2026-08-13 00:31 UTC | 2026-08-13 03:02 UTC | 2h 30m |
| JBU894 | JetBlue | Luis Munoz Marin International Airport (TJSJ) | Newark Liberty International Airport (KEWR) | 2026-08-12 21:19 UTC | 2026-08-13 03:01 UTC | 5h 41m |
| N158J |  | Nantucket Memorial Airport (KACK) | Duflo Airport (NY10) | 2026-08-13 01:30 UTC | 2026-08-13 03:01 UTC | 1h 31m |
| QLK4D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Tamworth Airport (YSTW) | 2026-08-13 02:24 UTC | 2026-08-13 03:01 UTC | 37m |
| DAL691 | Delta Air Lines | San Francisco International Airport (KSFO) | John F Kennedy International Airport (KJFK) | 2026-08-12 21:57 UTC | 2026-08-13 03:00 UTC | 5h 2m |
| LICHEN9 | LIC | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-13 01:24 UTC | 2026-08-13 02:58 UTC | 1h 34m |
| EFC56E | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-13 02:45 UTC | 2026-08-13 02:55 UTC | 10m |
| XUM2593 | XUM | Gimpo International Airport (RKSS) | Sacheon Air Base (RKPS) | 2026-08-13 02:05 UTC | 2026-08-13 02:55 UTC | 49m |
| WIS500 | WIS | Wittman Regional Airport (KOSH) | Eugene F Kranz Toledo Express Airport (KTOL) | 2026-08-13 01:35 UTC | 2026-08-13 02:54 UTC | 1h 18m |
| RXA6174 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-13 02:28 UTC | 2026-08-13 02:54 UTC | 25m |
| WEN3404 | WEN | Edmonton International Airport (CYEG) | Moose Jaw Municipal Airport (CJS4) | 2026-08-13 01:40 UTC | 2026-08-13 02:54 UTC | 1h 13m |
| SCU39 | SCU | Cherokee Ranch Airport (OK25) | Haskell Airport (K2K9) | 2026-08-13 02:50 UTC | 2026-08-13 02:53 UTC | 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
