# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_20:29:11_UTC-green)

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

**Latest saved flight:** 2026-08-16 20:29:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 20:29:11 UTC

- **206,099** saved flights
- **65,733** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **206,099** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,478,063.5 tonnes** estimated CO2 emissions
- **143,655,856 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8134 |
| 2 | SkyWest Airlines | 7403 |
| 3 | EJA | 3998 |
| 4 | IndiGo | 3522 |
| 5 | American Airlines | 3433 |
| 6 | Southwest Airlines | 3318 |
| 7 | Delta Air Lines | 2649 |
| 8 | ENY | 2570 |
| 9 | LATAM Airlines | 1935 |
| 10 | AZU | 1866 |
| 11 | Lufthansa | 1749 |
| 12 | Vueling | 1708 |
| 13 | WIF | 1656 |
| 14 | LXJ | 1628 |
| 15 | easyJet | 1428 |
| 16 | Swiss International | 1374 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1301 |
| 19 | Alaska Airlines | 1278 |
| 20 | QLK | 1261 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1130 |
| 24 | GLO | 1110 |
| 25 | Air France | 1102 |
| 26 | PGT | 1100 |
| 27 | JetBlue | 1055 |
| 28 | AEE | 1052 |
| 29 | WMT | 1039 |
| 30 | CXK | 1015 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 175136 |
| 2 | 🇪🇸 ES | 13177 |
| 3 | 🇧🇷 BR | 11805 |
| 4 | 🇦🇺 AU | 11483 |
| 5 | 🇨🇦 CA | 11375 |
| 6 | 🇮🇳 IN | 10990 |
| 7 | 🇮🇹 IT | 10749 |
| 8 | 🇩🇪 DE | 10204 |
| 9 | 🇬🇧 GB | 9614 |
| 10 | 🇯🇵 JP | 8453 |
| 11 | 🇨🇴 CO | 8190 |
| 12 | 🇫🇷 FR | 8163 |
| 13 | 🇬🇷 GR | 6067 |
| 14 | 🇹🇷 TR | 5843 |
| 15 | 🇲🇽 MX | 5790 |
| 16 | 🇨🇭 CH | 5510 |
| 17 | 🇳🇴 NO | 5131 |
| 18 | 🇲🇾 MY | 3529 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3401 |
| 21 | 🇹🇭 TH | 3246 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2618 |
| 25 | 🇰🇷 KR | 2505 |
| 26 | 🇭🇷 HR | 2207 |
| 27 | 🇲🇦 MA | 2080 |
| 28 | 🇳🇱 NL | 1837 |
| 29 | 🇲🇪 ME | 1736 |
| 30 | 🇮🇩 ID | 1686 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4332 |
| 2 | Denver International Airport |  | US | 3366 |
| 3 | Tokyo International Airport |  | JP | 2550 |
| 4 | Indira Gandhi International Airport |  | IN | 2494 |
| 5 | Guaymaral Airport |  | CO | 2493 |
| 6 | Harry Reid International Airport |  | US | 2327 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2151 |
| 8 | Zurich Airport |  | CH | 2151 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2140 |
| 10 | La Aurora Airport |  | GT | 1997 |
| 11 | Chicago O'Hare International Airport |  | US | 1909 |
| 12 | El Dorado International Airport |  | CO | 1883 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1841 |
| 14 | Salt Lake City International Airport |  | US | 1825 |
| 15 | Congonhas Airport |  | BR | 1719 |
| 16 | Frankfurt am Main International Airport |  | DE | 1706 |
| 17 | Madrid Barajas International Airport |  | ES | 1617 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1573 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1568 |
| 20 | Capua Airport |  | IT | 1566 |
| 21 | Macau International Airport |  | MO | 1542 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1491 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1419 |
| 25 | Charles de Gaulle International Airport |  | FR | 1412 |
| 26 | Charlotte/Douglas International Airport |  | US | 1405 |
| 27 | Kuala Lumpur International Airport |  | MY | 1309 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Bengaluru International Airport |  | IN | 1276 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1271 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1242 |
| 32 | Barcelona International Airport |  | ES | 1227 |
| 33 | Seattle-Tacoma International Airport |  | US | 1221 |
| 34 | Viracopos International Airport |  | BR | 1195 |
| 35 | Calgary International Airport |  | CA | 1167 |
| 36 | Reno/Tahoe International Airport |  | US | 1139 |
| 37 | Oslo Gardermoen Airport |  | NO | 1138 |
| 38 | Vitoria/Foronda Airport |  | ES | 1136 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1106 |
| 40 | Tenerife Norte Airport |  | ES | 1104 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 469 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 398 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 297 | 1h 49m | 1,423 km | 7,288.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 257 | 24m | 218 km | 968.2 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 249 | 19m | 99 km | 426.5 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 247 | 1h 14m | 961 km | 4,094.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 244 | 1h 37m | 1,156 km | 4,867.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 237 | 19m | 144 km | 589.5 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 224 | 28m | 152 km | 585.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 222 | 1h 49m | 1,304 km | 4,994.4 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N878CC |  | Centennial Airport (KAPA) | Centennial Airport (KAPA) | 2026-08-16 19:55 UTC | 2026-08-16 20:29 UTC | 33m |
| ES801 |  | Castle Airport (KMER) | Sacramento Mather Airport (KMHR) | 2026-08-16 19:41 UTC | 2026-08-16 20:24 UTC | 42m |
| N616EM |  | Victoria Regional Airport (KVCT) | Addison Airport (KADS) | 2026-08-16 19:16 UTC | 2026-08-16 20:21 UTC | 1h 4m |
| N938AX |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-08-16 19:33 UTC | 2026-08-16 20:21 UTC | 47m |
| N874EB |  | Bend Municipal Airport (KBDN) | Josephine Ranch Airport (2ID3) | 2026-08-16 18:32 UTC | 2026-08-16 20:15 UTC | 1h 42m |
| N9758H |  | Tangier Island Airport (KTGI) | Central Jersey Regional Airport (K47N) | 2026-08-16 18:55 UTC | 2026-08-16 20:12 UTC | 1h 16m |
| N53540 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-16 19:37 UTC | 2026-08-16 20:07 UTC | 30m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-16 19:53 UTC | 2026-08-16 20:06 UTC | 12m |
| EJA871 | EJA | Oxnard Airport (KOXR) | Moffett Federal Airfield (KNUQ) | 2026-08-16 19:22 UTC | 2026-08-16 20:01 UTC | 39m |
| N579AM |  | Boeing Field/King County International Airport (KBFI) | Boeing Field/King County International Airport (KBFI) | 2026-08-16 19:57 UTC | 2026-08-16 20:01 UTC | 3m |
| N1243M |  | Gardner Municipal Airport (KGDM) | Gardner Municipal Airport (KGDM) | 2026-08-16 19:56 UTC | 2026-08-16 19:59 UTC | 2m |
| N636JC |  | Baton Rouge Metro, Ryan Field (KBTR) | False River Regional Airport (KHZR) | 2026-08-16 19:46 UTC | 2026-08-16 19:58 UTC | 11m |
| N71560 |  | Abilene Municipal Airport (KK78) | Abilene Municipal Airport (KK78) | 2026-08-16 19:45 UTC | 2026-08-16 19:57 UTC | 12m |
| TVF50LQ | TVF | Nice-Cote d'Azur Airport (LFMN) | Paris-Orly Airport (LFPO) | 2026-08-16 18:44 UTC | 2026-08-16 19:57 UTC | 1h 13m |
| HK4350 |  | Alfredo Vasquez Cobo International Airport (SKLT) | El Dorado International Airport (SKBO) | 2026-08-16 14:39 UTC | 2026-08-16 19:57 UTC | 5h 18m |
| N294NG |  | Oakland San Francisco Bay Airport (KOAK) | San Carlos Airport (KSQL) | 2026-08-16 15:24 UTC | 2026-08-16 19:57 UTC | 4h 33m |
| N876AD |  | Ohio State University Airport (KOSU) | Tweed/New Haven Airport (KHVN) | 2026-08-16 18:30 UTC | 2026-08-16 19:55 UTC | 1h 24m |
| ASI414 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-08-16 19:48 UTC | 2026-08-16 19:54 UTC | 5m |
| N560SM |  | Norman Y Mineta San Jose International Airport (KSJC) | Lake Tahoe Airport (KTVL) | 2026-08-16 19:27 UTC | 2026-08-16 19:53 UTC | 25m |
| N314LM |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-08-16 19:30 UTC | 2026-08-16 19:53 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
