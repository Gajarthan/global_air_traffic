# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_09:57:52_UTC-green)

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

**Latest saved flight:** 2026-08-15 09:57:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 09:57:52 UTC

- **198,071** saved flights
- **62,002** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **198,071** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,365,818.6 tonnes** estimated CO2 emissions
- **137,148,903 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7867 |
| 2 | SkyWest Airlines | 7115 |
| 3 | EJA | 3897 |
| 4 | IndiGo | 3422 |
| 5 | Southwest Airlines | 3070 |
| 6 | American Airlines | 3054 |
| 7 | ENY | 2445 |
| 8 | Delta Air Lines | 2345 |
| 9 | LATAM Airlines | 1857 |
| 10 | AZU | 1791 |
| 11 | Lufthansa | 1699 |
| 12 | Vueling | 1660 |
| 13 | WIF | 1630 |
| 14 | LXJ | 1571 |
| 15 | easyJet | 1360 |
| 16 | Swiss International | 1337 |
| 17 | AXM | 1302 |
| 18 | EJU | 1228 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1204 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1093 |
| 23 | GLO | 1070 |
| 24 | PGT | 1041 |
| 25 | Air France | 1040 |
| 26 | AEE | 1020 |
| 27 | United Airlines | 1009 |
| 28 | CXK | 1005 |
| 29 | WMT | 995 |
| 30 | Wizz Air | 980 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 168181 |
| 2 | 🇪🇸 ES | 12783 |
| 3 | 🇧🇷 BR | 11383 |
| 4 | 🇦🇺 AU | 11143 |
| 5 | 🇨🇦 CA | 10843 |
| 6 | 🇮🇳 IN | 10692 |
| 7 | 🇮🇹 IT | 10343 |
| 8 | 🇩🇪 DE | 9818 |
| 9 | 🇬🇧 GB | 9275 |
| 10 | 🇯🇵 JP | 8116 |
| 11 | 🇫🇷 FR | 7882 |
| 12 | 🇨🇴 CO | 7806 |
| 13 | 🇬🇷 GR | 5833 |
| 14 | 🇲🇽 MX | 5605 |
| 15 | 🇹🇷 TR | 5431 |
| 16 | 🇨🇭 CH | 5353 |
| 17 | 🇳🇴 NO | 5052 |
| 18 | 🇲🇾 MY | 3401 |
| 19 | 🇿🇦 ZA | 3340 |
| 20 | 🇵🇱 PL | 3273 |
| 21 | 🇹🇭 TH | 3103 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2633 |
| 24 | 🇬🇹 GT | 2530 |
| 25 | 🇰🇷 KR | 2408 |
| 26 | 🇭🇷 HR | 2084 |
| 27 | 🇲🇦 MA | 2000 |
| 28 | 🇳🇱 NL | 1777 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1625 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4117 |
| 2 | Denver International Airport |  | US | 3220 |
| 3 | Tokyo International Airport |  | JP | 2484 |
| 4 | Guaymaral Airport |  | CO | 2443 |
| 5 | Indira Gandhi International Airport |  | IN | 2420 |
| 6 | Harry Reid International Airport |  | US | 2269 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2095 |
| 8 | Zurich Airport |  | CH | 2092 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2049 |
| 10 | La Aurora Airport |  | GT | 1938 |
| 11 | El Dorado International Airport |  | CO | 1816 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1764 |
| 13 | Salt Lake City International Airport |  | US | 1760 |
| 14 | Chicago O'Hare International Airport |  | US | 1737 |
| 15 | Frankfurt am Main International Airport |  | DE | 1669 |
| 16 | Congonhas Airport |  | BR | 1666 |
| 17 | Madrid Barajas International Airport |  | ES | 1557 |
| 18 | Macau International Airport |  | MO | 1533 |
| 19 | Capua Airport |  | IT | 1514 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1509 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1458 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1424 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1381 |
| 24 | Malpensa International Airport |  | IT | 1379 |
| 25 | Charles de Gaulle International Airport |  | FR | 1356 |
| 26 | Charlotte/Douglas International Airport |  | US | 1308 |
| 27 | Kuala Lumpur International Airport |  | MY | 1268 |
| 28 | Bengaluru International Airport |  | IN | 1252 |
| 29 | Ninoy Aquino International Airport |  | PH | 1245 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1236 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1212 |
| 32 | Barcelona International Airport |  | ES | 1191 |
| 33 | Viracopos International Airport |  | BR | 1151 |
| 34 | Seattle-Tacoma International Airport |  | US | 1140 |
| 35 | Calgary International Airport |  | CA | 1127 |
| 36 | Reno/Tahoe International Airport |  | US | 1116 |
| 37 | Oslo Gardermoen Airport |  | NO | 1116 |
| 38 | Daniel K Inouye International Airport |  | US | 1102 |
| 39 | Vitoria/Foronda Airport |  | ES | 1089 |
| 40 | Tenerife Norte Airport |  | ES | 1081 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1006 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 484 | 1h 7m | 770 km | 6,429.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 462 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 354 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 338 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 332 | 27m | 275 km | 1,573.2 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 306 | 1h 7m | 706 km | 3,725.6 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 298 | 44m | 241 km | 1,237.8 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 287 | 1h 49m | 1,423 km | 7,043.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 282 | 22m | 55 km | 268.0 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 246 | 24m | 218 km | 926.8 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 245 | 26m | 215 km | 907.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 242 | 19m | 99 km | 414.5 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 241 | 1h 15m | 961 km | 3,994.7 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 235 | 1h 38m | 1,156 km | 4,688.2 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 232 | 19m | 144 km | 577.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 215 | 28m | 152 km | 561.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 214 | 1h 3m | 695 km | 2,565.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JST419 | JST | Gold Coast Airport (YBCG) | Sydney Kingsford Smith International Airport (YSSY) | 2026-08-15 08:52 UTC | 2026-08-15 09:57 UTC | 1h 5m |
| HB2511 |  | Samedan Airport (LSZS) | Samedan Airport (LSZS) | 2026-08-15 09:25 UTC | 2026-08-15 09:49 UTC | 23m |
| OYPTR | OYP | AEro Airport (EKAE) | AEro Airport (EKAE) | 2026-08-15 09:34 UTC | 2026-08-15 09:48 UTC | 13m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-15 09:35 UTC | 2026-08-15 09:47 UTC | 11m |
| SUBTQ | SUB | October Airport (HEOC) | October Airport (HEOC) | 2026-08-15 08:57 UTC | 2026-08-15 09:44 UTC | 46m |
| VIP41 | VIP | Warsaw Chopin Airport (EPWA) | EPBB (EPBB) | 2026-08-15 09:10 UTC | 2026-08-15 09:32 UTC | 22m |
| DEGGO | DEG | Zweibrucken Airport (EDRZ) | Zweibrucken Airport (EDRZ) | 2026-08-15 09:10 UTC | 2026-08-15 09:26 UTC | 15m |
| OAL4MS | OAL | Eleftherios Venizelos International Airport (LGAV) | Milos Airport (LGML) | 2026-08-15 09:09 UTC | 2026-08-15 09:25 UTC | 16m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Melanes Airport (BIMN) | 2026-08-15 08:58 UTC | 2026-08-15 09:24 UTC | 25m |
| HBKNL | HBK | Locarno Airport (LSZL) | Aosta Airport (LIMW) | 2026-08-15 07:58 UTC | 2026-08-15 09:23 UTC | 1h 25m |
| N850BL |  | Jersey Airport (EGJJ) | RNAS Lee-On-Solent (EGHF) | 2026-08-15 08:51 UTC | 2026-08-15 09:23 UTC | 31m |
| FHVPC | FHV | Vannes-Meucon Airport (LFRV) | Vannes-Meucon Airport (LFRV) | 2026-08-15 09:06 UTC | 2026-08-15 09:22 UTC | 16m |
| CSH9161 | CSH | Tianjin Binhai International Airport (ZBTJ) | Wenzhou Yongqiang Airport (ZSWZ) | 2026-08-15 00:17 UTC | 2026-08-15 09:18 UTC | 9h 1m |
| EJU95FD | EJU | Alicante International Airport (LEAL) | Annemasse Airport (LFLI) | 2026-08-15 07:41 UTC | 2026-08-15 09:16 UTC | 1h 34m |
| BEL3DQ | Brussels Airlines | Brussels Airport (EBBR) | Frankfurt am Main International Airport (EDDF) | 2026-08-15 08:40 UTC | 2026-08-15 09:13 UTC | 33m |
| WIF36E | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-15 08:36 UTC | 2026-08-15 09:11 UTC | 35m |
| N883PG |  | Ninoy Aquino International Airport (RPLL) | Lingayen Airport (RPUG) | 2026-08-15 08:48 UTC | 2026-08-15 09:11 UTC | 23m |
| RJA128 | Royal Jordanian | Frankfurt am Main International Airport (EDDF) | Queen Alia International Airport (OJAI) | 2026-08-15 05:46 UTC | 2026-08-15 09:10 UTC | 3h 24m |
| VOE84KY | VOE | Menorca Airport (LEMH) | Bilbao Airport (LEBB) | 2026-08-15 08:03 UTC | 2026-08-15 09:09 UTC | 1h 5m |
| GOMST | GOM | Redhill Aerodrome (EGKR) | RNAS Lee-On-Solent (EGHF) | 2026-08-15 08:32 UTC | 2026-08-15 09:07 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
