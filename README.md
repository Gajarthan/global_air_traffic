# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_07:48:24_UTC-green)

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

**Latest saved flight:** 2026-08-12 07:48:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 07:48:24 UTC

- **188,822** saved flights
- **59,743** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **188,822** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,262,807.3 tonnes** estimated CO2 emissions
- **131,177,235 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7488 |
| 2 | SkyWest Airlines | 6863 |
| 3 | EJA | 3722 |
| 4 | IndiGo | 3285 |
| 5 | Southwest Airlines | 2956 |
| 6 | American Airlines | 2934 |
| 7 | ENY | 2344 |
| 8 | Delta Air Lines | 2220 |
| 9 | LATAM Airlines | 1762 |
| 10 | AZU | 1699 |
| 11 | Lufthansa | 1650 |
| 12 | Vueling | 1567 |
| 13 | WIF | 1563 |
| 14 | LXJ | 1478 |
| 15 | easyJet | 1298 |
| 16 | Swiss International | 1283 |
| 17 | AXM | 1249 |
| 18 | QLK | 1167 |
| 19 | EJU | 1165 |
| 20 | All Nippon Airways | 1151 |
| 21 | Alaska Airlines | 1131 |
| 22 | VIV | 1045 |
| 23 | GLO | 1017 |
| 24 | Air France | 978 |
| 25 | PGT | 973 |
| 26 | United Airlines | 970 |
| 27 | AEE | 969 |
| 28 | CXK | 966 |
| 29 | Cathay Pacific | 947 |
| 30 | Wizz Air | 936 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 161149 |
| 2 | 🇪🇸 ES | 12152 |
| 3 | 🇧🇷 BR | 10835 |
| 4 | 🇦🇺 AU | 10614 |
| 5 | 🇨🇦 CA | 10338 |
| 6 | 🇮🇳 IN | 10294 |
| 7 | 🇮🇹 IT | 9776 |
| 8 | 🇩🇪 DE | 9318 |
| 9 | 🇬🇧 GB | 8762 |
| 10 | 🇯🇵 JP | 7723 |
| 11 | 🇫🇷 FR | 7537 |
| 12 | 🇨🇴 CO | 7178 |
| 13 | 🇬🇷 GR | 5525 |
| 14 | 🇲🇽 MX | 5383 |
| 15 | 🇨🇭 CH | 5040 |
| 16 | 🇹🇷 TR | 5000 |
| 17 | 🇳🇴 NO | 4847 |
| 18 | 🇲🇾 MY | 3269 |
| 19 | 🇿🇦 ZA | 3160 |
| 20 | 🇵🇱 PL | 3126 |
| 21 | 🇹🇭 TH | 2919 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2498 |
| 24 | 🇬🇹 GT | 2399 |
| 25 | 🇰🇷 KR | 2329 |
| 26 | 🇲🇦 MA | 1916 |
| 27 | 🇭🇷 HR | 1912 |
| 28 | 🇲🇪 ME | 1685 |
| 29 | 🇳🇱 NL | 1683 |
| 30 | 🇲🇴 MO | 1525 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3924 |
| 2 | Denver International Airport |  | US | 3115 |
| 3 | Tokyo International Airport |  | JP | 2387 |
| 4 | Indira Gandhi International Airport |  | IN | 2320 |
| 5 | Guaymaral Airport |  | CO | 2312 |
| 6 | Harry Reid International Airport |  | US | 2210 |
| 7 | Zurich Airport |  | CH | 2002 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2001 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1956 |
| 10 | La Aurora Airport |  | GT | 1843 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1714 |
| 12 | El Dorado International Airport |  | CO | 1698 |
| 13 | Salt Lake City International Airport |  | US | 1680 |
| 14 | Chicago O'Hare International Airport |  | US | 1661 |
| 15 | Frankfurt am Main International Airport |  | DE | 1619 |
| 16 | Congonhas Airport |  | BR | 1575 |
| 17 | Macau International Airport |  | MO | 1525 |
| 18 | Madrid Barajas International Airport |  | ES | 1487 |
| 19 | Capua Airport |  | IT | 1471 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1465 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1398 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1350 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1321 |
| 24 | Malpensa International Airport |  | IT | 1302 |
| 25 | Charles de Gaulle International Airport |  | FR | 1285 |
| 26 | Charlotte/Douglas International Airport |  | US | 1264 |
| 27 | Kuala Lumpur International Airport |  | MY | 1223 |
| 28 | Bengaluru International Airport |  | IN | 1213 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1184 |
| 30 | Ninoy Aquino International Airport |  | PH | 1180 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1161 |
| 32 | Barcelona International Airport |  | ES | 1130 |
| 33 | Reno/Tahoe International Airport |  | US | 1094 |
| 34 | Viracopos International Airport |  | BR | 1091 |
| 35 | Seattle-Tacoma International Airport |  | US | 1089 |
| 36 | Calgary International Airport |  | CA | 1077 |
| 37 | Daniel K Inouye International Airport |  | US | 1064 |
| 38 | Oslo Gardermoen Airport |  | NO | 1053 |
| 39 | Tenerife Norte Airport |  | ES | 1035 |
| 40 | Vitoria/Foronda Airport |  | ES | 1021 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 953 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 692 | 21m | 244 km | 2,913.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 458 | 1h 7m | 770 km | 6,084.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 440 | 24m | 225 km | 1,707.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 439 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 331 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 317 | 27m | 275 km | 1,502.1 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 306 | 14m | 114 km | 600.2 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 284 | 8m | - | - |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 282 | 44m | 241 km | 1,171.4 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 271 | 22m | 55 km | 257.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 270 | 1h 49m | 1,423 km | 6,626.2 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 236 | 27m | 215 km | 874.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 235 | 13m | - | - |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 232 | 12m | - | - |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 230 | 1h 15m | 961 km | 3,812.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 225 | 1h 38m | 1,156 km | 4,488.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 224 | 19m | 144 km | 557.2 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 222 | 24m | 218 km | 836.4 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 206 | 1h 48m | 1,304 km | 4,634.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-12 07:35 UTC | 2026-08-12 07:48 UTC | 13m |
| EYY | EYY | Dunmore Manila Airport (YDNR) | Tamworth Airport (YSTW) | 2026-08-12 07:32 UTC | 2026-08-12 07:43 UTC | 11m |
| SEJYV | SEJ | Muenster Aero Airport (LSPU) | Aosta Airport (LIMW) | 2026-08-12 07:17 UTC | 2026-08-12 07:38 UTC | 20m |
| SKY019 | SKY | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-12 06:22 UTC | 2026-08-12 07:32 UTC | 1h 10m |
| ANA1278 | All Nippon Airways | New Chitose Airport (RJCC) | Ashiya Airport (RJFA) | 2026-08-12 05:43 UTC | 2026-08-12 07:32 UTC | 1h 49m |
| HBZVS | HBZ | Courchevel Airport (LFLJ) | Megeve Airport (LFHM) | 2026-08-12 05:56 UTC | 2026-08-12 07:24 UTC | 1h 27m |
| N155QS |  | Ellison Onizuka Kona International At Keahole Airport (PHKO) | San Francisco International Airport (KSFO) | 2026-08-12 02:54 UTC | 2026-08-12 07:21 UTC | 4h 27m |
| MAC351D | MAC | Ifrane Airport (GMFI) | Toulouse-Blagnac Airport (LFBO) | 2026-08-12 05:39 UTC | 2026-08-12 07:15 UTC | 1h 35m |
| 8AX |  | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-08-12 07:02 UTC | 2026-08-12 07:13 UTC | 10m |
| WIF3BR | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-12 06:42 UTC | 2026-08-12 07:09 UTC | 27m |
| INR50310 | INR | Reus Air Base (LERS) | Castellon-Costa Azahar Airport (LEDS) | 2026-08-12 06:44 UTC | 2026-08-12 07:04 UTC | 20m |
| KLM1827 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Stuttgart Airport (EDDS) | 2026-08-12 06:14 UTC | 2026-08-12 07:04 UTC | 50m |
| SEJYV | SEJ | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-08-12 05:19 UTC | 2026-08-12 06:58 UTC | 1h 38m |
| ANE30KP | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-08-12 06:21 UTC | 2026-08-12 06:57 UTC | 36m |
| DLH3PK | Lufthansa | Munich International Airport (EDDM) | Wismar Airport (EDCW) | 2026-08-12 05:54 UTC | 2026-08-12 06:57 UTC | 1h 2m |
| RYR3688 | Ryanair | Brussels South Charleroi Airport (EBCI) | Napoli / Capodichino International Airport (LIRN) | 2026-08-12 05:14 UTC | 2026-08-12 06:53 UTC | 1h 39m |
| RXA6832 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Mudgee Airport (YMDG) | 2026-08-12 06:22 UTC | 2026-08-12 06:52 UTC | 30m |
| PIZ35 | PIZ | Brussels Airport (EBBR) | Samedan Airport (LSZS) | 2026-08-12 05:31 UTC | 2026-08-12 06:50 UTC | 1h 18m |
| DKAGB | DKA | Juist Airport (EDWJ) | Juist Airport (EDWJ) | 2026-08-12 06:24 UTC | 2026-08-12 06:50 UTC | 25m |
| N51885 |  | Camino Airstrip (CL29) | 1CA4 (1CA4) | 2026-08-12 05:12 UTC | 2026-08-12 06:49 UTC | 1h 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
