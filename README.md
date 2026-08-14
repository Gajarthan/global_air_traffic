# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_02:31:49_UTC-green)

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

**Latest saved flight:** 2026-08-14 02:31:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 02:31:49 UTC

- **194,171** saved flights
- **61,095** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **194,171** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,320,461.4 tonnes** estimated CO2 emissions
- **134,519,498 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7710 |
| 2 | SkyWest Airlines | 7016 |
| 3 | EJA | 3833 |
| 4 | IndiGo | 3346 |
| 5 | Southwest Airlines | 3026 |
| 6 | American Airlines | 3014 |
| 7 | ENY | 2410 |
| 8 | Delta Air Lines | 2298 |
| 9 | LATAM Airlines | 1825 |
| 10 | AZU | 1752 |
| 11 | Lufthansa | 1673 |
| 12 | Vueling | 1614 |
| 13 | WIF | 1603 |
| 14 | LXJ | 1541 |
| 15 | easyJet | 1337 |
| 16 | Swiss International | 1315 |
| 17 | AXM | 1260 |
| 18 | EJU | 1193 |
| 19 | QLK | 1192 |
| 20 | All Nippon Airways | 1173 |
| 21 | Alaska Airlines | 1154 |
| 22 | VIV | 1069 |
| 23 | GLO | 1046 |
| 24 | Air France | 1011 |
| 25 | PGT | 1007 |
| 26 | AEE | 991 |
| 27 | United Airlines | 991 |
| 28 | CXK | 989 |
| 29 | WMT | 964 |
| 30 | Wizz Air | 962 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 165549 |
| 2 | 🇪🇸 ES | 12505 |
| 3 | 🇧🇷 BR | 11173 |
| 4 | 🇦🇺 AU | 10866 |
| 5 | 🇨🇦 CA | 10647 |
| 6 | 🇮🇳 IN | 10475 |
| 7 | 🇮🇹 IT | 10082 |
| 8 | 🇩🇪 DE | 9586 |
| 9 | 🇬🇧 GB | 9069 |
| 10 | 🇯🇵 JP | 7904 |
| 11 | 🇫🇷 FR | 7732 |
| 12 | 🇨🇴 CO | 7567 |
| 13 | 🇬🇷 GR | 5674 |
| 14 | 🇲🇽 MX | 5504 |
| 15 | 🇹🇷 TR | 5232 |
| 16 | 🇨🇭 CH | 5208 |
| 17 | 🇳🇴 NO | 4964 |
| 18 | 🇲🇾 MY | 3306 |
| 19 | 🇿🇦 ZA | 3264 |
| 20 | 🇵🇱 PL | 3190 |
| 21 | 🇹🇭 TH | 2994 |
| 22 | 🇳🇿 NZ | 2720 |
| 23 | 🇵🇭 PH | 2553 |
| 24 | 🇬🇹 GT | 2468 |
| 25 | 🇰🇷 KR | 2357 |
| 26 | 🇭🇷 HR | 2012 |
| 27 | 🇲🇦 MA | 1970 |
| 28 | 🇳🇱 NL | 1742 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1559 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4051 |
| 2 | Denver International Airport |  | US | 3183 |
| 3 | Tokyo International Airport |  | JP | 2429 |
| 4 | Guaymaral Airport |  | CO | 2412 |
| 5 | Indira Gandhi International Airport |  | IN | 2360 |
| 6 | Harry Reid International Airport |  | US | 2247 |
| 7 | Zurich Airport |  | CH | 2054 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2047 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2015 |
| 10 | La Aurora Airport |  | GT | 1898 |
| 11 | El Dorado International Airport |  | CO | 1773 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1746 |
| 13 | Salt Lake City International Airport |  | US | 1734 |
| 14 | Chicago O'Hare International Airport |  | US | 1702 |
| 15 | Frankfurt am Main International Airport |  | DE | 1639 |
| 16 | Congonhas Airport |  | BR | 1627 |
| 17 | Macau International Airport |  | MO | 1528 |
| 18 | Madrid Barajas International Airport |  | ES | 1527 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1493 |
| 20 | Capua Airport |  | IT | 1492 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1436 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1396 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1348 |
| 24 | Malpensa International Airport |  | IT | 1343 |
| 25 | Charles de Gaulle International Airport |  | FR | 1327 |
| 26 | Charlotte/Douglas International Airport |  | US | 1291 |
| 27 | Bengaluru International Airport |  | IN | 1236 |
| 28 | Kuala Lumpur International Airport |  | MY | 1233 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1214 |
| 30 | Ninoy Aquino International Airport |  | PH | 1209 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1191 |
| 32 | Barcelona International Airport |  | ES | 1160 |
| 33 | Viracopos International Airport |  | BR | 1128 |
| 34 | Seattle-Tacoma International Airport |  | US | 1119 |
| 35 | Calgary International Airport |  | CA | 1111 |
| 36 | Reno/Tahoe International Airport |  | US | 1103 |
| 37 | Oslo Gardermoen Airport |  | NO | 1088 |
| 38 | Daniel K Inouye International Airport |  | US | 1084 |
| 39 | Tenerife Norte Airport |  | ES | 1067 |
| 40 | Vitoria/Foronda Airport |  | ES | 1060 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 996 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 712 | 21m | 244 km | 2,998.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 470 | 1h 7m | 770 km | 6,243.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 455 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 446 | 24m | 225 km | 1,730.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 326 | 27m | 275 km | 1,544.8 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 321 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 289 | 44m | 241 km | 1,200.4 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 278 | 1h 49m | 1,423 km | 6,822.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 277 | 22m | 55 km | 263.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 259 | 20m | 250 km | 1,118.7 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 242 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 241 | 27m | 215 km | 892.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 238 | 24m | 218 km | 896.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 237 | 1h 15m | 961 km | 3,928.4 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 229 | 19m | 144 km | 569.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 228 | 1h 38m | 1,156 km | 4,548.5 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 221 | 31m | 369 km | 1,406.7 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 212 | 28m | 152 km | 554.0 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 211 | 1h 3m | 695 km | 2,529.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LBQ792 | LBQ | KNY2 (KNY2) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-14 02:13 UTC | 2026-08-14 02:31 UTC | 18m |
| N5PG |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-14 01:36 UTC | 2026-08-14 02:29 UTC | 52m |
|  |  | St Simons Island Airport (KSSI) | St Simons Island Airport (KSSI) | 2026-08-14 02:16 UTC | 2026-08-14 02:16 UTC | 0m |
| T77 |  | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-14 01:04 UTC | 2026-08-14 02:14 UTC | 1h 9m |
| MNN | MNN | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-14 01:58 UTC | 2026-08-14 02:10 UTC | 12m |
| N704MD |  | Juneau International Airport (PAJN) | Mule Creek Airport (CBS4) | 2026-08-14 01:40 UTC | 2026-08-14 02:05 UTC | 24m |
| N469FG |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-14 01:24 UTC | 2026-08-14 02:04 UTC | 39m |
| N8118U |  | Danbury Municipal Airport (KDXR) | Waterbury-Oxford Airport (KOXC) | 2026-08-14 01:28 UTC | 2026-08-14 02:04 UTC | 35m |
| N182KQ |  | Renton Municipal Airport (KRNT) | Boeing Field/King County International Airport (KBFI) | 2026-08-14 01:49 UTC | 2026-08-14 01:53 UTC | 4m |
| N363WD |  | 0TS1 (0TS1) | Denton Enterprise Airport (KDTO) | 2026-08-14 01:50 UTC | 2026-08-14 01:53 UTC | 3m |
| N954JH |  | Stormville Airport (KN69) | Hartford-Brainard Airport (KHFD) | 2026-08-14 01:21 UTC | 2026-08-14 01:53 UTC | 32m |
| N396JA |  | Beaver County Airport (KBVI) | Beaver County Airport (KBVI) | 2026-08-14 01:50 UTC | 2026-08-14 01:52 UTC | 2m |
| N552YM |  | Truckee-Tahoe Airport (KTRK) | Santa Barbara Municipal Airport (KSBA) | 2026-08-14 00:53 UTC | 2026-08-14 01:43 UTC | 50m |
| N642PF |  | Brandywine Regional Airport (KOQN) | Cape May County Airport (KWWD) | 2026-08-14 00:59 UTC | 2026-08-14 01:42 UTC | 43m |
| SWA2222 | Southwest Airlines | Harry Reid International Airport (KLAS) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-14 00:37 UTC | 2026-08-14 01:41 UTC | 1h 3m |
| MAFFS6 | MAF | Redding Regional Airport (KRDD) | Lonnie Pool Field/Weaverville Airport (KO54) | 2026-08-14 01:25 UTC | 2026-08-14 01:37 UTC | 12m |
| DAL1306 | Delta Air Lines | Chicago O'Hare International Airport (KORD) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-08-14 00:38 UTC | 2026-08-14 01:36 UTC | 58m |
| TKR103 | TKR | Redding Regional Airport (KRDD) | Lonnie Pool Field/Weaverville Airport (KO54) | 2026-08-14 01:27 UTC | 2026-08-14 01:34 UTC | 7m |
| N53371 |  | Palm Beach County Park Airport (KLNA) | Baggett Airport (FD57) | 2026-08-14 00:52 UTC | 2026-08-14 01:34 UTC | 42m |
| N398UA |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-08-14 00:52 UTC | 2026-08-14 01:33 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
