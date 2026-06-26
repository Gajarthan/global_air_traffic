# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_01:07:07_UTC-green)

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

**Latest saved flight:** 2026-06-26 01:07:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-26 01:07:07 UTC

- **120,602** saved flights
- **41,458** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **120,602** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,457,934.3 tonnes** estimated CO2 emissions
- **84,517,928 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4942 |
| 2 | SkyWest Airlines | 4464 |
| 3 | EJA | 2335 |
| 4 | IndiGo | 2309 |
| 5 | American Airlines | 1872 |
| 6 | Southwest Airlines | 1799 |
| 7 | ENY | 1506 |
| 8 | Delta Air Lines | 1426 |
| 9 | Lufthansa | 1318 |
| 10 | Vueling | 1082 |
| 11 | LATAM Airlines | 1071 |
| 12 | WIF | 1067 |
| 13 | AZU | 1005 |
| 14 | AXM | 980 |
| 15 | LXJ | 918 |
| 16 | Swiss International | 843 |
| 17 | All Nippon Airways | 822 |
| 18 | Alaska Airlines | 795 |
| 19 | easyJet | 776 |
| 20 | QLK | 772 |
| 21 | EJU | 754 |
| 22 | Cathay Pacific | 676 |
| 23 | AEE | 670 |
| 24 | VIV | 660 |
| 25 | Air France | 659 |
| 26 | United Airlines | 659 |
| 27 | CXK | 645 |
| 28 | MXY | 634 |
| 29 | JetBlue | 602 |
| 30 | AXB | 598 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 102386 |
| 2 | 🇪🇸 ES | 8170 |
| 3 | 🇮🇳 IN | 7259 |
| 4 | 🇦🇺 AU | 7094 |
| 5 | 🇧🇷 BR | 6638 |
| 6 | 🇩🇪 DE | 6430 |
| 7 | 🇮🇹 IT | 6409 |
| 8 | 🇨🇦 CA | 6342 |
| 9 | 🇯🇵 JP | 5367 |
| 10 | 🇬🇧 GB | 5294 |
| 11 | 🇫🇷 FR | 4786 |
| 12 | 🇨🇴 CO | 4018 |
| 13 | 🇲🇽 MX | 3517 |
| 14 | 🇬🇷 GR | 3440 |
| 15 | 🇳🇴 NO | 3312 |
| 16 | 🇨🇭 CH | 3087 |
| 17 | 🇲🇾 MY | 2543 |
| 18 | 🇹🇷 TR | 2477 |
| 19 | 🇿🇦 ZA | 2021 |
| 20 | 🇵🇱 PL | 1980 |
| 21 | 🇳🇿 NZ | 1960 |
| 22 | 🇹🇭 TH | 1916 |
| 23 | 🇰🇷 KR | 1904 |
| 24 | 🇵🇭 PH | 1729 |
| 25 | 🇬🇹 GT | 1680 |
| 26 | 🇲🇦 MA | 1300 |
| 27 | 🇲🇪 ME | 1200 |
| 28 | 🇲🇴 MO | 1174 |
| 29 | 🇳🇱 NL | 1150 |
| 30 | 🇭🇷 HR | 1040 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2536 |
| 2 | Denver International Airport |  | US | 2032 |
| 3 | Tokyo International Airport |  | JP | 1778 |
| 4 | Indira Gandhi International Airport |  | IN | 1597 |
| 5 | Guaymaral Airport |  | CO | 1508 |
| 6 | Harry Reid International Airport |  | US | 1504 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1460 |
| 8 | Zurich Airport |  | CH | 1339 |
| 9 | La Aurora Airport |  | GT | 1297 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1282 |
| 11 | Frankfurt am Main International Airport |  | DE | 1273 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1193 |
| 13 | Chicago O'Hare International Airport |  | US | 1175 |
| 14 | Macau International Airport |  | MO | 1174 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1047 |
| 17 | Capua Airport |  | IT | 1035 |
| 18 | Madrid Barajas International Airport |  | ES | 1011 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1003 |
| 20 | Kuala Lumpur International Airport |  | MY | 984 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 940 |
| 22 | Congonhas Airport |  | BR | 929 |
| 23 | Charlotte/Douglas International Airport |  | US | 912 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 896 |
| 25 | Charles de Gaulle International Airport |  | FR | 883 |
| 26 | Bengaluru International Airport |  | IN | 874 |
| 27 | Malpensa International Airport |  | IT | 840 |
| 28 | Ninoy Aquino International Airport |  | PH | 801 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 787 |
| 30 | Daniel K Inouye International Airport |  | US | 776 |
| 31 | Tenerife Norte Airport |  | ES | 762 |
| 32 | Barcelona International Airport |  | ES | 761 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 741 |
| 34 | Calgary International Airport |  | CA | 705 |
| 35 | Vitoria/Foronda Airport |  | ES | 703 |
| 36 | Amsterdam Airport Schiphol |  | NL | 696 |
| 37 | Don Mueang International Airport |  | TH | 694 |
| 38 | Seattle-Tacoma International Airport |  | US | 694 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 691 |
| 40 | Scottsdale Airport |  | US | 686 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 628 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 437 | 21m | 244 km | 1,840.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 317 | 24m | 225 km | 1,229.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 308 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 291 | 1h 10m | 770 km | 3,865.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 291 | 1h 25m | 910 km | 4,566.5 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 237 | 26m | 275 km | 1,123.0 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 223 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 174 | 27m | 215 km | 644.4 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 173 | 20m | 99 km | 296.3 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 165 | 44m | 241 km | 685.4 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 161 | 27m | 152 km | 420.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 156 | 31m | 369 km | 993.0 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 154 | 44m | 452 km | 1,200.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 150 | 1h 44m | 1,423 km | 3,681.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 150 | 18m | 144 km | 373.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 141 | 1h 38m | 1,156 km | 2,812.9 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 136 | 1h 17m | 961 km | 2,254.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| G26332 |  | KEDG (KEDG) | KEDG (KEDG) | 2026-06-26 00:41 UTC | 2026-06-26 01:07 UTC | 25m |
| N6744W |  | Rocky Mountain Metro Airport (KBJC) | CO86 (CO86) | 2026-06-26 00:40 UTC | 2026-06-26 01:00 UTC | 19m |
| N636KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-26 00:19 UTC | 2026-06-26 00:59 UTC | 39m |
| STGRY43 | STG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Laredo International Airport (KLRD) | 2026-06-25 23:45 UTC | 2026-06-26 00:57 UTC | 1h 12m |
| EJA921 | EJA | Los Angeles International Airport (KLAX) | Oakland San Francisco Bay Airport (KOAK) | 2026-06-25 23:59 UTC | 2026-06-26 00:53 UTC | 54m |
| FTC55 | FTC | Larnaca International Airport (LCLK) | Diagoras Airport (LGRP) | 2026-06-26 00:01 UTC | 2026-06-26 00:52 UTC | 50m |
| N628SR |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-06-26 00:12 UTC | 2026-06-26 00:47 UTC | 35m |
| N100BW |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-25 23:42 UTC | 2026-06-26 00:44 UTC | 1h 2m |
| N64087 |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-06-25 23:26 UTC | 2026-06-26 00:44 UTC | 1h 17m |
| N68080 |  | King Salmon Airport (PAKN) | Tibbetts Airport (4AK9) | 2026-06-26 00:19 UTC | 2026-06-26 00:42 UTC | 23m |
| N293DC |  | Nevada County Airport (KGOO) | Sierraville Dearwater Airport (KO79) | 2026-06-26 00:08 UTC | 2026-06-26 00:42 UTC | 33m |
| N307SW |  | Gillespie Field (KSEE) | Emory Ranch Airport (0CA6) | 2026-06-26 00:15 UTC | 2026-06-26 00:42 UTC | 26m |
| N862YB |  | Los Alamos Airport (KLAM) | NM74 (NM74) | 2026-06-26 00:04 UTC | 2026-06-26 00:42 UTC | 37m |
| N959BH |  | Ralph Wien Memorial Airport (PAOT) | Ralph Wien Memorial Airport (PAOT) | 2026-06-25 23:07 UTC | 2026-06-26 00:40 UTC | 1h 32m |
| N2259X |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-06-25 23:40 UTC | 2026-06-26 00:39 UTC | 58m |
| N345DG |  | West Houston Airport (KIWS) | Howard County Airport (KM77) | 2026-06-25 23:30 UTC | 2026-06-26 00:38 UTC | 1h 8m |
| AMF1901 | AMF | Inyokern Airport (KIYK) | Mojave Air & Space Port/Rutan Field (KMHV) | 2026-06-26 00:23 UTC | 2026-06-26 00:35 UTC | 12m |
| N48FA |  | Knoxville Downtown Island Airport (KDKX) | Mc Ghee Tyson Airport (KTYS) | 2026-06-26 00:00 UTC | 2026-06-26 00:35 UTC | 35m |
| AAL1322 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Denver International Airport (KDEN) | 2026-06-25 22:35 UTC | 2026-06-26 00:33 UTC | 1h 57m |
| SKW6513 | SkyWest Airlines | Los Angeles International Airport (KLAX) | Ohkay Owingeh Airport (KE14) | 2026-06-25 22:57 UTC | 2026-06-26 00:33 UTC | 1h 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
