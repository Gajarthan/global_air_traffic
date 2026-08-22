# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_12:45:38_UTC-green)

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

**Latest saved flight:** 2026-08-22 12:45:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 12:45:38 UTC

- **225,420** saved flights
- **70,156** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **225,420** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,717,060.5 tonnes** estimated CO2 emissions
- **157,510,754 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9042 |
| 2 | SkyWest Airlines | 7997 |
| 3 | EJA | 4353 |
| 4 | IndiGo | 3813 |
| 5 | American Airlines | 3705 |
| 6 | Southwest Airlines | 3524 |
| 7 | Delta Air Lines | 2879 |
| 8 | ENY | 2759 |
| 9 | LATAM Airlines | 2146 |
| 10 | AZU | 2077 |
| 11 | Vueling | 1906 |
| 12 | Lufthansa | 1852 |
| 13 | WIF | 1792 |
| 14 | LXJ | 1778 |
| 15 | easyJet | 1563 |
| 16 | Swiss International | 1502 |
| 17 | AXM | 1492 |
| 18 | QLK | 1421 |
| 19 | EJU | 1419 |
| 20 | United Airlines | 1417 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1356 |
| 23 | GLO | 1245 |
| 24 | PGT | 1242 |
| 25 | VIV | 1232 |
| 26 | Air France | 1225 |
| 27 | WMT | 1209 |
| 28 | Wizz Air | 1167 |
| 29 | JetBlue | 1129 |
| 30 | AEE | 1123 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188767 |
| 2 | 🇪🇸 ES | 14451 |
| 3 | 🇧🇷 BR | 13077 |
| 4 | 🇦🇺 AU | 12776 |
| 5 | 🇨🇦 CA | 12480 |
| 6 | 🇮🇹 IT | 12073 |
| 7 | 🇮🇳 IN | 11894 |
| 8 | 🇩🇪 DE | 11109 |
| 9 | 🇬🇧 GB | 10594 |
| 10 | 🇨🇴 CO | 9263 |
| 11 | 🇯🇵 JP | 9188 |
| 12 | 🇫🇷 FR | 9006 |
| 13 | 🇹🇷 TR | 6604 |
| 14 | 🇬🇷 GR | 6585 |
| 15 | 🇲🇽 MX | 6260 |
| 16 | 🇨🇭 CH | 5956 |
| 17 | 🇳🇴 NO | 5580 |
| 18 | 🇲🇾 MY | 3975 |
| 19 | 🇿🇦 ZA | 3907 |
| 20 | 🇹🇭 TH | 3878 |
| 21 | 🇵🇱 PL | 3742 |
| 22 | 🇳🇿 NZ | 3138 |
| 23 | 🇵🇭 PH | 3077 |
| 24 | 🇬🇹 GT | 2850 |
| 25 | 🇰🇷 KR | 2676 |
| 26 | 🇭🇷 HR | 2537 |
| 27 | 🇲🇦 MA | 2264 |
| 28 | 🇲🇪 ME | 2021 |
| 29 | 🇳🇱 NL | 2012 |
| 30 | 🇮🇩 ID | 1945 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4706 |
| 2 | Denver International Airport |  | US | 3670 |
| 3 | Tokyo International Airport |  | JP | 2746 |
| 4 | Indira Gandhi International Airport |  | IN | 2739 |
| 5 | Guaymaral Airport |  | CO | 2632 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2342 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2278 |
| 10 | La Aurora Airport |  | GT | 2172 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1979 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 15 | Congonhas Airport |  | BR | 1913 |
| 16 | Frankfurt am Main International Airport |  | DE | 1817 |
| 17 | Madrid Barajas International Airport |  | ES | 1760 |
| 18 | Capua Airport |  | IT | 1736 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1678 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1669 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1634 |
| 22 | Macau International Airport |  | MO | 1594 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1589 |
| 24 | Malpensa International Airport |  | IT | 1587 |
| 25 | Charles de Gaulle International Airport |  | FR | 1560 |
| 26 | Charlotte/Douglas International Airport |  | US | 1483 |
| 27 | Ninoy Aquino International Airport |  | PH | 1471 |
| 28 | Kuala Lumpur International Airport |  | MY | 1445 |
| 29 | Barcelona International Airport |  | ES | 1397 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1369 |
| 31 | Bengaluru International Airport |  | IN | 1342 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1334 |
| 33 | Seattle-Tacoma International Airport |  | US | 1329 |
| 34 | Viracopos International Airport |  | BR | 1326 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1305 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1272 |
| 38 | Oslo Gardermoen Airport |  | NO | 1257 |
| 39 | Vitoria/Foronda Airport |  | ES | 1242 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1220 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1073 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 815 | 21m | 244 km | 3,431.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 562 | 1h 6m | 770 km | 7,465.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 528 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 510 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 355 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 339 | 1h 50m | 1,423 km | 8,319.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 328 | 44m | 241 km | 1,362.4 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 301 | 21m | 250 km | 1,300.1 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 291 | 44m | 555 km | 2,786.5 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 287 | 1h 38m | 1,156 km | 5,725.5 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 283 | 24m | 218 km | 1,066.2 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 280 | 19m | 99 km | 479.6 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 264 | 1h 14m | 961 km | 4,375.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 257 | 19m | 144 km | 639.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-22 12:34 UTC | 2026-08-22 12:45 UTC | 11m |
| N906CH |  | Sugar Land Regional Airport (KSGR) | William P Hobby Airport (KHOU) | 2026-08-22 11:52 UTC | 2026-08-22 12:32 UTC | 40m |
| TOG561 | TOG | Redding Regional Airport (KRDD) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-22 11:39 UTC | 2026-08-22 12:19 UTC | 39m |
| N81NG |  | Cavern City Air Trml Airport (KCNM) | Casas Adobes Airpark (NM69) | 2026-08-22 11:29 UTC | 2026-08-22 12:17 UTC | 47m |
| HBZZO | HBZ | Sion Airport (LSGS) | Sion Airport (LSGS) | 2026-08-22 12:09 UTC | 2026-08-22 12:14 UTC | 4m |
| HBZWD | HBZ | Bern Belp Airport (LSZB) | Raron Airport (LSTA) | 2026-08-22 11:46 UTC | 2026-08-22 12:11 UTC | 25m |
| HK5019G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-22 11:46 UTC | 2026-08-22 12:01 UTC | 15m |
| NIA9001 | NIA | Cairo International Airport (HECA) | HE38 (HE38) | 2026-08-22 11:43 UTC | 2026-08-22 11:57 UTC | 14m |
| N937LR |  | Van Strien Airport (26MI) | 5MI3 (5MI3) | 2026-08-22 11:52 UTC | 2026-08-22 11:56 UTC | 3m |
| N35TJ |  | Youngstown Elser Metro Airport (K4G4) | Harry Clever Field (KPHD) | 2026-08-22 11:29 UTC | 2026-08-22 11:56 UTC | 27m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-08-22 11:48 UTC | 2026-08-22 11:52 UTC | 3m |
| KFS198 | KFS | Tweed/New Haven Airport (KHVN) | Tweed/New Haven Airport (KHVN) | 2026-08-22 11:35 UTC | 2026-08-22 11:49 UTC | 13m |
| AWA477 | AWA | VGZR (VGZR) | VGBG (VGBG) | 2026-08-22 11:15 UTC | 2026-08-22 11:45 UTC | 30m |
| IGO542M | IndiGo | Juhu Aerodrome (VAJJ) | Coimbatore International Airport (VOCB) | 2026-08-22 10:27 UTC | 2026-08-22 11:44 UTC | 1h 17m |
| GTI8782 | GTI | Ted Stevens Anchorage International Airport (PANC) | Miami International Airport (KMIA) | 2026-08-22 04:50 UTC | 2026-08-22 11:43 UTC | 6h 53m |
| AZU4158 | AZU | Viracopos International Airport (SBKP) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-08-22 10:53 UTC | 2026-08-22 11:43 UTC | 50m |
| RYR36RD | Ryanair | Barcelona International Airport (LEBL) | Gdańsk Lech Wałęsa Airport (EPGD) | 2026-08-22 09:13 UTC | 2026-08-22 11:40 UTC | 2h 26m |
| EWG1VH | EWG | Hamburg Airport (EDDH) | Salzburg Airport (LOWS) | 2026-08-22 10:39 UTC | 2026-08-22 11:39 UTC | 1h 0m |
| AWA449 | AWA | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-08-22 11:00 UTC | 2026-08-22 11:39 UTC | 39m |
| SWR217M | Swiss International | Geneva Cointrin International Airport (LSGG) | Santorini Airport (LGSR) | 2026-08-22 09:15 UTC | 2026-08-22 11:38 UTC | 2h 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
