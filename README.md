# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_02:55:09_UTC-green)

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

**Latest saved flight:** 2026-08-12 02:55:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 02:55:09 UTC

- **188,550** saved flights
- **59,696** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **188,550** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,260,067.7 tonnes** estimated CO2 emissions
- **131,018,420 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7479 |
| 2 | SkyWest Airlines | 6862 |
| 3 | EJA | 3722 |
| 4 | IndiGo | 3278 |
| 5 | Southwest Airlines | 2956 |
| 6 | American Airlines | 2934 |
| 7 | ENY | 2344 |
| 8 | Delta Air Lines | 2219 |
| 9 | LATAM Airlines | 1762 |
| 10 | AZU | 1698 |
| 11 | Lufthansa | 1647 |
| 12 | Vueling | 1564 |
| 13 | WIF | 1556 |
| 14 | LXJ | 1478 |
| 15 | easyJet | 1297 |
| 16 | Swiss International | 1283 |
| 17 | AXM | 1247 |
| 18 | EJU | 1163 |
| 19 | QLK | 1160 |
| 20 | All Nippon Airways | 1148 |
| 21 | Alaska Airlines | 1127 |
| 22 | VIV | 1044 |
| 23 | GLO | 1017 |
| 24 | Air France | 978 |
| 25 | AEE | 969 |
| 26 | PGT | 969 |
| 27 | United Airlines | 969 |
| 28 | CXK | 966 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 935 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 161058 |
| 2 | 🇪🇸 ES | 12134 |
| 3 | 🇧🇷 BR | 10833 |
| 4 | 🇦🇺 AU | 10536 |
| 5 | 🇨🇦 CA | 10335 |
| 6 | 🇮🇳 IN | 10269 |
| 7 | 🇮🇹 IT | 9761 |
| 8 | 🇩🇪 DE | 9300 |
| 9 | 🇬🇧 GB | 8759 |
| 10 | 🇯🇵 JP | 7681 |
| 11 | 🇫🇷 FR | 7528 |
| 12 | 🇨🇴 CO | 7176 |
| 13 | 🇬🇷 GR | 5520 |
| 14 | 🇲🇽 MX | 5378 |
| 15 | 🇨🇭 CH | 5034 |
| 16 | 🇹🇷 TR | 4985 |
| 17 | 🇳🇴 NO | 4833 |
| 18 | 🇲🇾 MY | 3264 |
| 19 | 🇿🇦 ZA | 3156 |
| 20 | 🇵🇱 PL | 3121 |
| 21 | 🇹🇭 TH | 2905 |
| 22 | 🇳🇿 NZ | 2678 |
| 23 | 🇵🇭 PH | 2492 |
| 24 | 🇬🇹 GT | 2399 |
| 25 | 🇰🇷 KR | 2320 |
| 26 | 🇲🇦 MA | 1915 |
| 27 | 🇭🇷 HR | 1910 |
| 28 | 🇲🇪 ME | 1685 |
| 29 | 🇳🇱 NL | 1677 |
| 30 | 🇲🇴 MO | 1523 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3924 |
| 2 | Denver International Airport |  | US | 3115 |
| 3 | Tokyo International Airport |  | JP | 2376 |
| 4 | Guaymaral Airport |  | CO | 2312 |
| 5 | Indira Gandhi International Airport |  | IN | 2312 |
| 6 | Harry Reid International Airport |  | US | 2210 |
| 7 | Zurich Airport |  | CH | 2001 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2000 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1955 |
| 10 | La Aurora Airport |  | GT | 1843 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1714 |
| 12 | El Dorado International Airport |  | CO | 1698 |
| 13 | Salt Lake City International Airport |  | US | 1680 |
| 14 | Chicago O'Hare International Airport |  | US | 1660 |
| 15 | Frankfurt am Main International Airport |  | DE | 1617 |
| 16 | Congonhas Airport |  | BR | 1575 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1485 |
| 19 | Capua Airport |  | IT | 1470 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1465 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1398 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1350 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1312 |
| 24 | Malpensa International Airport |  | IT | 1299 |
| 25 | Charles de Gaulle International Airport |  | FR | 1285 |
| 26 | Charlotte/Douglas International Airport |  | US | 1264 |
| 27 | Kuala Lumpur International Airport |  | MY | 1222 |
| 28 | Bengaluru International Airport |  | IN | 1210 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1183 |
| 30 | Ninoy Aquino International Airport |  | PH | 1177 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1161 |
| 32 | Barcelona International Airport |  | ES | 1128 |
| 33 | Reno/Tahoe International Airport |  | US | 1094 |
| 34 | Viracopos International Airport |  | BR | 1090 |
| 35 | Seattle-Tacoma International Airport |  | US | 1088 |
| 36 | Calgary International Airport |  | CA | 1077 |
| 37 | Daniel K Inouye International Airport |  | US | 1061 |
| 38 | Oslo Gardermoen Airport |  | NO | 1051 |
| 39 | Tenerife Norte Airport |  | ES | 1035 |
| 40 | Vitoria/Foronda Airport |  | ES | 1019 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 953 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 689 | 21m | 244 km | 2,901.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 455 | 1h 7m | 770 km | 6,044.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 439 | 24m | 225 km | 1,703.1 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 439 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 330 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 316 | 27m | 275 km | 1,497.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 306 | 14m | 114 km | 600.2 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 284 | 8m | - | - |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 282 | 44m | 241 km | 1,171.4 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 271 | 22m | 55 km | 257.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 268 | 1h 49m | 1,423 km | 6,577.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 235 | 27m | 215 km | 870.3 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 234 | 13m | - | - |
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
| VVHK002 | VVH | Mayport Ns (Adm David L Mcdonald Field) Airport (KNRB) | K55J (K55J) | 2026-08-12 02:17 UTC | 2026-08-12 02:55 UTC | 37m |
| HRCLS63 | HRC | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-08-12 02:20 UTC | 2026-08-12 02:55 UTC | 34m |
| YNW | YNW | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-08-12 02:14 UTC | 2026-08-12 02:53 UTC | 39m |
| SKY007 | SKY | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-12 01:34 UTC | 2026-08-12 02:47 UTC | 1h 13m |
| N539SH |  | Gold King Creek Airport (PAAN) | Healy River Airport (PAHV) | 2026-08-12 02:40 UTC | 2026-08-12 02:43 UTC | 3m |
| N684DT |  | Destin Executive Airport (KDTS) | Auburn University Regional Airport (KAUO) | 2026-08-12 02:12 UTC | 2026-08-12 02:43 UTC | 30m |
| N126AA |  | Brooksville-Tampa Bay Regional Airport (KBKV) | Sarasota/Bradenton International Airport (KSRQ) | 2026-08-12 01:55 UTC | 2026-08-12 02:43 UTC | 47m |
| ANA249 | All Nippon Airways | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-12 01:35 UTC | 2026-08-12 02:42 UTC | 1h 7m |
| JAL313 | Japan Airlines | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-12 01:30 UTC | 2026-08-12 02:38 UTC | 1h 8m |
| NCJ12 | NCJ | Cavern City Air Trml Airport (KCNM) | Country Haven Airport (MY94) | 2026-08-12 00:05 UTC | 2026-08-12 02:37 UTC | 2h 31m |
| SKY831 | SKY | Hyakuri Airport (RJAH) | Ashiya Airport (RJFA) | 2026-08-12 01:17 UTC | 2026-08-12 02:36 UTC | 1h 19m |
| TCF653 | TCF | Melbourne Orlando International Airport (KMLB) | Palm Beach County Park Airport (KLNA) | 2026-08-12 01:31 UTC | 2026-08-12 02:35 UTC | 1h 4m |
| N17SU |  | UT80 (UT80) | Grassy Meadows/Sky Ranch Landowners Assn Airport (UT47) | 2026-08-12 02:20 UTC | 2026-08-12 02:33 UTC | 13m |
| N325ND |  | Lincoln Airport (KLNK) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-11 23:52 UTC | 2026-08-12 02:33 UTC | 2h 40m |
| TKR103 | TKR | Redding Regional Airport (KRDD) | Lonnie Pool Field/Weaverville Airport (KO54) | 2026-08-12 02:17 UTC | 2026-08-12 02:26 UTC | 9m |
| SWX | SWX | Southport Airport (YSPT) | Southport Airport (YSPT) | 2026-08-12 02:22 UTC | 2026-08-12 02:25 UTC | 3m |
| TKR910 | TKR | Mc Clellan Airfield (KMCC) | Sierraville Dearwater Airport (KO79) | 2026-08-12 02:02 UTC | 2026-08-12 02:16 UTC | 14m |
| N3NJ |  | 8NJ0 (8NJ0) | NJ58 (NJ58) | 2026-08-12 02:08 UTC | 2026-08-12 02:14 UTC | 6m |
| NKD | NKD | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-08-12 01:59 UTC | 2026-08-12 02:11 UTC | 12m |
| S421 |  | Mcnary Field (KSLE) | KS48 (KS48) | 2026-08-12 01:50 UTC | 2026-08-12 02:11 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
