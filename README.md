# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_17:39:06_UTC-green)

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

**Latest saved flight:** 2026-07-27 17:39:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-27 17:39:06 UTC

- **154,972** saved flights
- **51,603** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **154,972** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,857,042.0 tonnes** estimated CO2 emissions
- **107,654,609 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6234 |
| 2 | SkyWest Airlines | 5674 |
| 3 | EJA | 3067 |
| 4 | IndiGo | 2753 |
| 5 | American Airlines | 2470 |
| 6 | Southwest Airlines | 2436 |
| 7 | ENY | 1936 |
| 8 | Delta Air Lines | 1843 |
| 9 | Lufthansa | 1498 |
| 10 | LATAM Airlines | 1440 |
| 11 | AZU | 1349 |
| 12 | WIF | 1305 |
| 13 | Vueling | 1294 |
| 14 | LXJ | 1193 |
| 15 | AXM | 1098 |
| 16 | Swiss International | 1081 |
| 17 | easyJet | 1007 |
| 18 | Alaska Airlines | 971 |
| 19 | All Nippon Airways | 966 |
| 20 | QLK | 965 |
| 21 | EJU | 948 |
| 22 | VIV | 853 |
| 23 | United Airlines | 832 |
| 24 | CXK | 823 |
| 25 | AEE | 811 |
| 26 | JetBlue | 810 |
| 27 | MXY | 810 |
| 28 | GLO | 807 |
| 29 | Air France | 806 |
| 30 | Cathay Pacific | 793 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 133799 |
| 2 | 🇪🇸 ES | 9983 |
| 3 | 🇧🇷 BR | 8814 |
| 4 | 🇦🇺 AU | 8770 |
| 5 | 🇮🇳 IN | 8649 |
| 6 | 🇨🇦 CA | 8332 |
| 7 | 🇮🇹 IT | 7986 |
| 8 | 🇩🇪 DE | 7883 |
| 9 | 🇬🇧 GB | 7105 |
| 10 | 🇯🇵 JP | 6369 |
| 11 | 🇫🇷 FR | 6134 |
| 12 | 🇨🇴 CO | 5348 |
| 13 | 🇲🇽 MX | 4453 |
| 14 | 🇬🇷 GR | 4402 |
| 15 | 🇳🇴 NO | 4090 |
| 16 | 🇨🇭 CH | 4053 |
| 17 | 🇹🇷 TR | 3689 |
| 18 | 🇲🇾 MY | 2863 |
| 19 | 🇵🇱 PL | 2643 |
| 20 | 🇿🇦 ZA | 2507 |
| 21 | 🇳🇿 NZ | 2312 |
| 22 | 🇹🇭 TH | 2233 |
| 23 | 🇰🇷 KR | 2087 |
| 24 | 🇵🇭 PH | 2039 |
| 25 | 🇬🇹 GT | 2006 |
| 26 | 🇲🇦 MA | 1581 |
| 27 | 🇲🇪 ME | 1504 |
| 28 | 🇭🇷 HR | 1428 |
| 29 | 🇳🇱 NL | 1419 |
| 30 | 🇲🇴 MO | 1266 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3182 |
| 2 | Denver International Airport |  | US | 2599 |
| 3 | Tokyo International Airport |  | JP | 2017 |
| 4 | Guaymaral Airport |  | CO | 1946 |
| 5 | Indira Gandhi International Airport |  | IN | 1916 |
| 6 | Harry Reid International Airport |  | US | 1905 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1722 |
| 8 | Zurich Airport |  | CH | 1678 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1621 |
| 10 | La Aurora Airport |  | GT | 1555 |
| 11 | Frankfurt am Main International Airport |  | DE | 1446 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1442 |
| 13 | Chicago O'Hare International Airport |  | US | 1420 |
| 14 | Salt Lake City International Airport |  | US | 1398 |
| 15 | El Dorado International Airport |  | CO | 1396 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1315 |
| 17 | Macau International Airport |  | MO | 1266 |
| 18 | Congonhas Airport |  | BR | 1256 |
| 19 | Madrid Barajas International Airport |  | ES | 1231 |
| 20 | Capua Airport |  | IT | 1218 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1190 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1119 |
| 23 | Charlotte/Douglas International Airport |  | US | 1104 |
| 24 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1101 |
| 25 | Kuala Lumpur International Airport |  | MY | 1097 |
| 26 | Charles de Gaulle International Airport |  | FR | 1062 |
| 27 | Bengaluru International Airport |  | IN | 1033 |
| 28 | Malpensa International Airport |  | IT | 1007 |
| 29 | Ninoy Aquino International Airport |  | PH | 955 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 939 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 935 |
| 32 | Barcelona International Airport |  | ES | 921 |
| 33 | Daniel K Inouye International Airport |  | US | 919 |
| 34 | Seattle-Tacoma International Airport |  | US | 902 |
| 35 | Tenerife Norte Airport |  | ES | 889 |
| 36 | Calgary International Airport |  | CA | 887 |
| 37 | Scottsdale Airport |  | US | 878 |
| 38 | Viracopos International Airport |  | BR | 876 |
| 39 | Amsterdam Airport Schiphol |  | NL | 858 |
| 40 | Oslo Gardermoen Airport |  | NO | 848 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 818 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 558 | 21m | 244 km | 2,349.6 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 374 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 371 | 24m | 225 km | 1,439.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 358 | 1h 9m | 770 km | 4,755.8 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 286 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 230 | 22m | 55 km | 218.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 212 | 44m | 241 km | 880.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 204 | 26m | 215 km | 755.5 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 198 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 195 | 20m | 250 km | 842.3 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 187 | 27m | 152 km | 488.7 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 182 | 1h 15m | 961 km | 3,016.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 182 | 18m | 144 km | 452.7 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 180 | 31m | 369 km | 1,145.7 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 180 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 174 | 50m | 556 km | 1,667.9 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 172 | 1h 1m | 695 km | 2,061.8 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N745AK |  | Cape May County Airport (KWWD) | Millville Municipal Airport (KMIV) | 2026-07-27 16:56 UTC | 2026-07-27 17:39 UTC | 42m |
| HK5297G |  | El Eden Airport (SKAR) | Santa Ana Airport (SKGO) | 2026-07-27 17:04 UTC | 2026-07-27 17:38 UTC | 33m |
| FIRE5 | FIR | Van Nuys Airport (KVNY) | Santa Monica Municipal Airport (KSMO) | 2026-07-27 16:40 UTC | 2026-07-27 17:38 UTC | 57m |
| N7209F |  | New Garden Airport (KN57) | New Garden Airport (KN57) | 2026-07-27 17:16 UTC | 2026-07-27 17:38 UTC | 21m |
| N8019V |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-07-27 17:07 UTC | 2026-07-27 17:37 UTC | 29m |
| N862TC |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-07-27 16:23 UTC | 2026-07-27 17:31 UTC | 1h 7m |
| FTO382 | FTO | Essex County Airport (KCDW) | Laguardia Airport (KLGA) | 2026-07-27 17:19 UTC | 2026-07-27 17:29 UTC | 10m |
| BRG621 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-07-27 16:45 UTC | 2026-07-27 17:29 UTC | 44m |
| C2302 |  | Vinalhaven Airport (ME55) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-27 16:30 UTC | 2026-07-27 17:27 UTC | 57m |
| N232LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Bob Hope Airport (KBUR) | 2026-07-27 15:37 UTC | 2026-07-27 17:24 UTC | 1h 46m |
| N222HN |  | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-07-27 17:17 UTC | 2026-07-27 17:21 UTC | 4m |
| N119UV |  | Provo Municipal Airport (KPVU) | KU77 (KU77) | 2026-07-27 17:03 UTC | 2026-07-27 17:20 UTC | 16m |
| N5918T |  | Auburn Municipal Airport (KAUN) | Chico Regional Airport (KCIC) | 2026-07-27 16:26 UTC | 2026-07-27 17:19 UTC | 53m |
| BYF4 | BYF | San Carlos Airport (KSQL) | Livermore Municipal Airport (KLVK) | 2026-07-27 17:00 UTC | 2026-07-27 17:18 UTC | 17m |
| TRP6 | TRP | Kent Fort Manor Airport (7MD8) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-07-27 17:08 UTC | 2026-07-27 17:18 UTC | 10m |
| N172YY |  | CA40 (CA40) | Meadows Field (KBFL) | 2026-07-27 16:38 UTC | 2026-07-27 17:17 UTC | 39m |
| N53371 |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-07-27 16:46 UTC | 2026-07-27 17:17 UTC | 30m |
| T7ARES |  | Girona Airport (LEGE) | Nice-Cote d'Azur Airport (LFMN) | 2026-07-27 16:24 UTC | 2026-07-27 17:15 UTC | 51m |
| N81FF |  | Naples Municipal Airport (KAPF) | Marco Island Executive Airport (KMKY) | 2026-07-27 16:46 UTC | 2026-07-27 17:12 UTC | 26m |
| N779US |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-07-27 16:57 UTC | 2026-07-27 17:10 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
