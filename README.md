# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_07:21:14_UTC-green)

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

**Latest saved flight:** 2026-07-27 07:21:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-27 07:21:14 UTC

- **154,294** saved flights
- **51,427** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **154,294** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,849,725.1 tonnes** estimated CO2 emissions
- **107,230,442 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6210 |
| 2 | SkyWest Airlines | 5660 |
| 3 | EJA | 3055 |
| 4 | IndiGo | 2742 |
| 5 | American Airlines | 2468 |
| 6 | Southwest Airlines | 2428 |
| 7 | ENY | 1932 |
| 8 | Delta Air Lines | 1838 |
| 9 | Lufthansa | 1493 |
| 10 | LATAM Airlines | 1434 |
| 11 | AZU | 1341 |
| 12 | WIF | 1295 |
| 13 | Vueling | 1287 |
| 14 | LXJ | 1189 |
| 15 | AXM | 1096 |
| 16 | Swiss International | 1074 |
| 17 | easyJet | 1004 |
| 18 | Alaska Airlines | 970 |
| 19 | All Nippon Airways | 964 |
| 20 | QLK | 963 |
| 21 | EJU | 944 |
| 22 | VIV | 850 |
| 23 | United Airlines | 830 |
| 24 | CXK | 820 |
| 25 | MXY | 810 |
| 26 | AEE | 808 |
| 27 | JetBlue | 806 |
| 28 | GLO | 805 |
| 29 | Air France | 798 |
| 30 | Cathay Pacific | 789 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 133268 |
| 2 | 🇪🇸 ES | 9942 |
| 3 | 🇧🇷 BR | 8768 |
| 4 | 🇦🇺 AU | 8759 |
| 5 | 🇮🇳 IN | 8615 |
| 6 | 🇨🇦 CA | 8300 |
| 7 | 🇮🇹 IT | 7959 |
| 8 | 🇩🇪 DE | 7842 |
| 9 | 🇬🇧 GB | 7046 |
| 10 | 🇯🇵 JP | 6361 |
| 11 | 🇫🇷 FR | 6087 |
| 12 | 🇨🇴 CO | 5280 |
| 13 | 🇲🇽 MX | 4441 |
| 14 | 🇬🇷 GR | 4385 |
| 15 | 🇳🇴 NO | 4061 |
| 16 | 🇨🇭 CH | 4030 |
| 17 | 🇹🇷 TR | 3676 |
| 18 | 🇲🇾 MY | 2858 |
| 19 | 🇵🇱 PL | 2631 |
| 20 | 🇿🇦 ZA | 2487 |
| 21 | 🇳🇿 NZ | 2312 |
| 22 | 🇹🇭 TH | 2229 |
| 23 | 🇰🇷 KR | 2085 |
| 24 | 🇵🇭 PH | 2033 |
| 25 | 🇬🇹 GT | 1999 |
| 26 | 🇲🇦 MA | 1572 |
| 27 | 🇲🇪 ME | 1497 |
| 28 | 🇭🇷 HR | 1413 |
| 29 | 🇳🇱 NL | 1409 |
| 30 | 🇲🇴 MO | 1257 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3176 |
| 2 | Denver International Airport |  | US | 2594 |
| 3 | Tokyo International Airport |  | JP | 2016 |
| 4 | Guaymaral Airport |  | CO | 1928 |
| 5 | Indira Gandhi International Airport |  | IN | 1911 |
| 6 | Harry Reid International Airport |  | US | 1898 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1718 |
| 8 | Zurich Airport |  | CH | 1670 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1616 |
| 10 | La Aurora Airport |  | GT | 1550 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1441 |
| 12 | Frankfurt am Main International Airport |  | DE | 1441 |
| 13 | Chicago O'Hare International Airport |  | US | 1418 |
| 14 | Salt Lake City International Airport |  | US | 1395 |
| 15 | El Dorado International Airport |  | CO | 1389 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1312 |
| 17 | Macau International Airport |  | MO | 1257 |
| 18 | Congonhas Airport |  | BR | 1250 |
| 19 | Madrid Barajas International Airport |  | ES | 1228 |
| 20 | Capua Airport |  | IT | 1216 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1189 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1118 |
| 23 | Charlotte/Douglas International Airport |  | US | 1103 |
| 24 | Kuala Lumpur International Airport |  | MY | 1096 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1093 |
| 26 | Charles de Gaulle International Airport |  | FR | 1053 |
| 27 | Bengaluru International Airport |  | IN | 1031 |
| 28 | Malpensa International Airport |  | IT | 1005 |
| 29 | Ninoy Aquino International Airport |  | PH | 952 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 935 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 930 |
| 32 | Barcelona International Airport |  | ES | 920 |
| 33 | Daniel K Inouye International Airport |  | US | 917 |
| 34 | Seattle-Tacoma International Airport |  | US | 900 |
| 35 | Tenerife Norte Airport |  | ES | 883 |
| 36 | Calgary International Airport |  | CA | 882 |
| 37 | Viracopos International Airport |  | BR | 874 |
| 38 | Scottsdale Airport |  | US | 873 |
| 39 | Amsterdam Airport Schiphol |  | NL | 850 |
| 40 | Oslo Gardermoen Airport |  | NO | 844 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 810 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 556 | 21m | 244 km | 2,341.2 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 373 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 371 | 24m | 225 km | 1,439.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 358 | 1h 9m | 770 km | 4,755.8 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 284 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 210 | 44m | 241 km | 872.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 203 | 26m | 215 km | 751.8 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 200 | 20m | 99 km | 342.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 198 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 187 | 27m | 152 km | 488.7 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 182 | 1h 15m | 961 km | 3,016.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 180 | 18m | 144 km | 447.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 180 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 179 | 31m | 369 km | 1,139.4 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 172 | 1h 1m | 695 km | 2,061.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 172 | 51m | 556 km | 1,648.8 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGO1153 | IndiGo | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-07-27 06:08 UTC | 2026-07-27 07:21 UTC | 1h 13m |
| AOJ75J | AOJ | Ostrava Leos Janacek Airport (LKMT) | Cewice Military Airport (EPCE) | 2026-07-27 06:25 UTC | 2026-07-27 07:10 UTC | 45m |
| CPA256 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-07-26 19:51 UTC | 2026-07-27 07:08 UTC | 11h 16m |
| CPA335 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Zhuhai Airport (ZGSD) | 2026-07-26 23:50 UTC | 2026-07-27 07:02 UTC | 7h 12m |
| MRL12 | MRL | San Javier Airport (LELC) | Alcantarilla Airport (LERI) | 2026-07-27 06:42 UTC | 2026-07-27 07:01 UTC | 18m |
| MRL11F | MRL | San Javier Airport (LELC) | Alcantarilla Airport (LERI) | 2026-07-27 06:41 UTC | 2026-07-27 06:59 UTC | 18m |
| WIF4X | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-07-27 06:14 UTC | 2026-07-27 06:50 UTC | 36m |
| FD614 |  | Perth Jandakot Airport (YPJT) | Kellerberrin Airport (YKEB) | 2026-07-27 06:22 UTC | 2026-07-27 06:50 UTC | 27m |
| CLX4327 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-07-26 19:59 UTC | 2026-07-27 06:44 UTC | 10h 45m |
| WIF3LP | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-07-27 05:56 UTC | 2026-07-27 06:44 UTC | 47m |
| N606TD |  | Addison Airport (KADS) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-27 03:56 UTC | 2026-07-27 06:43 UTC | 2h 46m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-07-27 05:51 UTC | 2026-07-27 06:43 UTC | 51m |
| NSZ4377 | NSZ | Stockholm-Arlanda Airport (ESSA) | Malpensa International Airport (LIMC) | 2026-07-27 04:19 UTC | 2026-07-27 06:41 UTC | 2h 22m |
| QLK42D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-07-27 06:12 UTC | 2026-07-27 06:40 UTC | 27m |
| WZZ93GB | Wizz Air | Stockholm Skavsta Airport (ESKN) | Khrabrovo Airport (UMKK) | 2026-07-27 05:55 UTC | 2026-07-27 06:39 UTC | 43m |
| MTR | MTR | Boonah Airport (YBOA) | Brisbane Archerfield Airport (YBAF) | 2026-07-27 06:13 UTC | 2026-07-27 06:39 UTC | 25m |
| IGO291 | IndiGo | Indira Gandhi International Airport (VIDP) | Lengpui Airport (VELP) | 2026-07-27 04:25 UTC | 2026-07-27 06:37 UTC | 2h 11m |
| RYR90RJ | Ryanair | Dublin Airport (EIDW) | Dublin Airport (EIDW) | 2026-07-27 06:23 UTC | 2026-07-27 06:37 UTC | 13m |
| DHTJE | DHT | St. Johann In Tirol Airport (LOIJ) | Weiden in der Oberpfalz Airport (EDQW) | 2026-07-27 05:35 UTC | 2026-07-27 06:36 UTC | 1h 0m |
| ANE29MQ | ANE | Madrid Barajas International Airport (LEMD) | Morante Airport (LETE) | 2026-07-27 05:50 UTC | 2026-07-27 06:32 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
