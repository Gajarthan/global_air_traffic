# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_00:30:08_UTC-green)

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

**Latest saved flight:** 2026-08-12 00:30:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 00:30:08 UTC

- **188,444** saved flights
- **59,666** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **188,444** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,259,176.7 tonnes** estimated CO2 emissions
- **130,966,763 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7479 |
| 2 | SkyWest Airlines | 6862 |
| 3 | EJA | 3722 |
| 4 | IndiGo | 3277 |
| 5 | Southwest Airlines | 2954 |
| 6 | American Airlines | 2934 |
| 7 | ENY | 2344 |
| 8 | Delta Air Lines | 2217 |
| 9 | LATAM Airlines | 1762 |
| 10 | AZU | 1698 |
| 11 | Lufthansa | 1647 |
| 12 | Vueling | 1564 |
| 13 | WIF | 1556 |
| 14 | LXJ | 1477 |
| 15 | easyJet | 1297 |
| 16 | Swiss International | 1283 |
| 17 | AXM | 1247 |
| 18 | EJU | 1163 |
| 19 | QLK | 1158 |
| 20 | All Nippon Airways | 1145 |
| 21 | Alaska Airlines | 1127 |
| 22 | VIV | 1044 |
| 23 | GLO | 1017 |
| 24 | Air France | 978 |
| 25 | AEE | 969 |
| 26 | PGT | 967 |
| 27 | United Airlines | 967 |
| 28 | CXK | 965 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 935 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 160950 |
| 2 | 🇪🇸 ES | 12134 |
| 3 | 🇧🇷 BR | 10833 |
| 4 | 🇦🇺 AU | 10512 |
| 5 | 🇨🇦 CA | 10324 |
| 6 | 🇮🇳 IN | 10266 |
| 7 | 🇮🇹 IT | 9761 |
| 8 | 🇩🇪 DE | 9300 |
| 9 | 🇬🇧 GB | 8758 |
| 10 | 🇯🇵 JP | 7663 |
| 11 | 🇫🇷 FR | 7528 |
| 12 | 🇨🇴 CO | 7174 |
| 13 | 🇬🇷 GR | 5520 |
| 14 | 🇲🇽 MX | 5376 |
| 15 | 🇨🇭 CH | 5034 |
| 16 | 🇹🇷 TR | 4983 |
| 17 | 🇳🇴 NO | 4833 |
| 18 | 🇲🇾 MY | 3263 |
| 19 | 🇿🇦 ZA | 3156 |
| 20 | 🇵🇱 PL | 3120 |
| 21 | 🇹🇭 TH | 2896 |
| 22 | 🇳🇿 NZ | 2678 |
| 23 | 🇵🇭 PH | 2487 |
| 24 | 🇬🇹 GT | 2399 |
| 25 | 🇰🇷 KR | 2318 |
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
| 3 | Tokyo International Airport |  | JP | 2370 |
| 4 | Guaymaral Airport |  | CO | 2312 |
| 5 | Indira Gandhi International Airport |  | IN | 2311 |
| 6 | Harry Reid International Airport |  | US | 2208 |
| 7 | Zurich Airport |  | CH | 2001 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2000 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1954 |
| 10 | La Aurora Airport |  | GT | 1843 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1713 |
| 12 | El Dorado International Airport |  | CO | 1698 |
| 13 | Salt Lake City International Airport |  | US | 1680 |
| 14 | Chicago O'Hare International Airport |  | US | 1660 |
| 15 | Frankfurt am Main International Airport |  | DE | 1617 |
| 16 | Congonhas Airport |  | BR | 1575 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1485 |
| 19 | Capua Airport |  | IT | 1470 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1464 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1397 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1350 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1311 |
| 24 | Malpensa International Airport |  | IT | 1299 |
| 25 | Charles de Gaulle International Airport |  | FR | 1285 |
| 26 | Charlotte/Douglas International Airport |  | US | 1264 |
| 27 | Kuala Lumpur International Airport |  | MY | 1221 |
| 28 | Bengaluru International Airport |  | IN | 1210 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1183 |
| 30 | Ninoy Aquino International Airport |  | PH | 1174 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1161 |
| 32 | Barcelona International Airport |  | ES | 1128 |
| 33 | Reno/Tahoe International Airport |  | US | 1092 |
| 34 | Viracopos International Airport |  | BR | 1090 |
| 35 | Seattle-Tacoma International Airport |  | US | 1087 |
| 36 | Calgary International Airport |  | CA | 1073 |
| 37 | Daniel K Inouye International Airport |  | US | 1061 |
| 38 | Oslo Gardermoen Airport |  | NO | 1051 |
| 39 | Tenerife Norte Airport |  | ES | 1035 |
| 40 | Vitoria/Foronda Airport |  | ES | 1019 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 953 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 689 | 21m | 244 km | 2,901.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 454 | 1h 7m | 770 km | 6,031.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 439 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 438 | 24m | 225 km | 1,699.2 t |
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
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 232 | 50m | 556 km | 2,223.9 t |
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
| N9297U |  | Harvey's Acres Airport (OR28) | Portland-Hillsboro Airport (KHIO) | 2026-08-11 23:36 UTC | 2026-08-12 00:30 UTC | 53m |
| AIRCAM | AIR | Castle Mountain Airstrip (48AK) | Warren "Bud" Woods Palmer Municipal Airport (PAAQ) | 2026-08-11 23:51 UTC | 2026-08-12 00:26 UTC | 34m |
| TKR103 | TKR | Hill Afb Airport (KHIF) | Trinity Center Airport (KO86) | 2026-08-11 22:50 UTC | 2026-08-12 00:14 UTC | 1h 24m |
| ROT101C | ROT | Henri Coanda International Airport (LROP) | HE42 (HE42) | 2026-08-11 22:12 UTC | 2026-08-12 00:13 UTC | 2h 0m |
| TKR186 | TKR | Chamberlain Airport (OR60) | Christensen Field (8WA6) | 2026-08-11 23:51 UTC | 2026-08-12 00:10 UTC | 18m |
| UAL135 | United Airlines | Zurich Airport (LSZH) | Newark Liberty International Airport (KEWR) | 2026-08-11 15:49 UTC | 2026-08-12 00:10 UTC | 8h 20m |
| QXE2191 | QXE | Seattle-Tacoma International Airport (KSEA) | Truth Or Consequences Municipal Airport (KTCS) | 2026-08-11 21:27 UTC | 2026-08-12 00:09 UTC | 2h 42m |
| N205DY |  | Perryman Airport (7CL9) | Perryman Airport (7CL9) | 2026-08-11 23:41 UTC | 2026-08-11 23:59 UTC | 18m |
| MAFFS4 | MAF | Mc Clellan Airfield (KMCC) | Truckee-Tahoe Airport (KTRK) | 2026-08-11 23:38 UTC | 2026-08-11 23:58 UTC | 19m |
| MAFFS6 | MAF | Mc Clellan Airfield (KMCC) | NV17 (NV17) | 2026-08-11 23:31 UTC | 2026-08-11 23:57 UTC | 26m |
| N884GT |  | American Falconry Airport (45WY) | Casper/Natrona County International Airport (KCPR) | 2026-08-11 23:49 UTC | 2026-08-11 23:57 UTC | 7m |
| N711R |  | Scottsdale Airport (KSDL) | Easterwood Field (KCLL) | 2026-08-11 21:50 UTC | 2026-08-11 23:54 UTC | 2h 4m |
| N628TS |  | Austin-Bergstrom International Airport (KAUS) | NV13 (NV13) | 2026-08-11 21:15 UTC | 2026-08-11 23:52 UTC | 2h 36m |
| N21RF |  | Prattville/Grouby Field (K1A9) | MU78 (MU78) | 2026-08-11 22:14 UTC | 2026-08-11 23:51 UTC | 1h 36m |
| SIS927 | SIS | CA40 (CA40) | San Carlos Airport (KSQL) | 2026-08-11 23:04 UTC | 2026-08-11 23:49 UTC | 44m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-11 23:47 UTC | 2026-08-11 23:48 UTC | 1m |
| N8024Q |  | Ocean City Municipal Airport (KOXB) | Ocean City Municipal Airport (KOXB) | 2026-08-11 23:41 UTC | 2026-08-11 23:48 UTC | 6m |
| DLH584 | Lufthansa | Almaza Air Force Base (HEAZ) | Cairo International Airport (HECA) | 2026-08-11 23:42 UTC | 2026-08-11 23:43 UTC | 0m |
| N442WT |  | K7K8 (K7K8) | Wadena Municipal Airport (KADC) | 2026-08-11 23:08 UTC | 2026-08-11 23:42 UTC | 33m |
| APG211 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-08-11 23:18 UTC | 2026-08-11 23:41 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
