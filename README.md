# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_07:37:00_UTC-green)

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

**Latest saved flight:** 2026-08-21 07:37:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 07:37:00 UTC

- **221,432** saved flights
- **69,380** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **221,432** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,665,036.4 tonnes** estimated CO2 emissions
- **154,494,863 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8865 |
| 2 | SkyWest Airlines | 7891 |
| 3 | EJA | 4289 |
| 4 | IndiGo | 3751 |
| 5 | American Airlines | 3670 |
| 6 | Southwest Airlines | 3491 |
| 7 | Delta Air Lines | 2851 |
| 8 | ENY | 2724 |
| 9 | LATAM Airlines | 2103 |
| 10 | AZU | 2032 |
| 11 | Vueling | 1861 |
| 12 | Lufthansa | 1831 |
| 13 | WIF | 1769 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1530 |
| 16 | Swiss International | 1471 |
| 17 | AXM | 1460 |
| 18 | QLK | 1399 |
| 19 | United Airlines | 1390 |
| 20 | EJU | 1379 |
| 21 | Alaska Airlines | 1351 |
| 22 | All Nippon Airways | 1327 |
| 23 | GLO | 1211 |
| 24 | PGT | 1207 |
| 25 | VIV | 1206 |
| 26 | Air France | 1197 |
| 27 | WMT | 1170 |
| 28 | Wizz Air | 1128 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1107 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186287 |
| 2 | 🇪🇸 ES | 14170 |
| 3 | 🇧🇷 BR | 12790 |
| 4 | 🇦🇺 AU | 12610 |
| 5 | 🇨🇦 CA | 12245 |
| 6 | 🇮🇹 IT | 11761 |
| 7 | 🇮🇳 IN | 11691 |
| 8 | 🇩🇪 DE | 10915 |
| 9 | 🇬🇧 GB | 10368 |
| 10 | 🇨🇴 CO | 9102 |
| 11 | 🇯🇵 JP | 9007 |
| 12 | 🇫🇷 FR | 8796 |
| 13 | 🇬🇷 GR | 6456 |
| 14 | 🇹🇷 TR | 6380 |
| 15 | 🇲🇽 MX | 6157 |
| 16 | 🇨🇭 CH | 5838 |
| 17 | 🇳🇴 NO | 5493 |
| 18 | 🇲🇾 MY | 3864 |
| 19 | 🇿🇦 ZA | 3777 |
| 20 | 🇹🇭 TH | 3712 |
| 21 | 🇵🇱 PL | 3669 |
| 22 | 🇳🇿 NZ | 3088 |
| 23 | 🇵🇭 PH | 3005 |
| 24 | 🇬🇹 GT | 2793 |
| 25 | 🇰🇷 KR | 2643 |
| 26 | 🇭🇷 HR | 2451 |
| 27 | 🇲🇦 MA | 2221 |
| 28 | 🇳🇱 NL | 1964 |
| 29 | 🇲🇪 ME | 1956 |
| 30 | 🇮🇩 ID | 1890 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4649 |
| 2 | Denver International Airport |  | US | 3615 |
| 3 | Tokyo International Airport |  | JP | 2704 |
| 4 | Indira Gandhi International Airport |  | IN | 2687 |
| 5 | Guaymaral Airport |  | CO | 2606 |
| 6 | Harry Reid International Airport |  | US | 2443 |
| 7 | Zurich Airport |  | CH | 2292 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2276 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2246 |
| 10 | La Aurora Airport |  | GT | 2128 |
| 11 | El Dorado International Airport |  | CO | 2073 |
| 12 | Chicago O'Hare International Airport |  | US | 2024 |
| 13 | Salt Lake City International Airport |  | US | 1948 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1909 |
| 15 | Congonhas Airport |  | BR | 1869 |
| 16 | Frankfurt am Main International Airport |  | DE | 1798 |
| 17 | Madrid Barajas International Airport |  | ES | 1732 |
| 18 | Capua Airport |  | IT | 1688 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1661 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1630 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1586 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1568 |
| 24 | Malpensa International Airport |  | IT | 1551 |
| 25 | Charles de Gaulle International Airport |  | FR | 1521 |
| 26 | Charlotte/Douglas International Airport |  | US | 1471 |
| 27 | Ninoy Aquino International Airport |  | PH | 1431 |
| 28 | Kuala Lumpur International Airport |  | MY | 1414 |
| 29 | Barcelona International Airport |  | ES | 1358 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1346 |
| 31 | Bengaluru International Airport |  | IN | 1327 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1315 |
| 33 | Seattle-Tacoma International Airport |  | US | 1313 |
| 34 | Viracopos International Airport |  | BR | 1299 |
| 35 | Calgary International Airport |  | CA | 1256 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1235 |
| 37 | Oslo Gardermoen Airport |  | NO | 1227 |
| 38 | Vitoria/Foronda Airport |  | ES | 1227 |
| 39 | Don Mueang International Airport |  | TH | 1221 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1188 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1064 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 798 | 21m | 244 km | 3,360.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 550 | 1h 7m | 770 km | 7,306.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 537 | 24m | 225 km | 2,083.3 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 499 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 499 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 372 | 27m | 275 km | 1,762.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 351 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 328 | 1h 50m | 1,423 km | 8,049.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 324 | 44m | 241 km | 1,345.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 277 | 1h 38m | 1,156 km | 5,526.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 276 | 24m | 218 km | 1,039.8 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 273 | 19m | 99 km | 467.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 262 | 44m | 555 km | 2,508.8 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 239 | 1h 49m | 1,304 km | 5,376.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FJJJY | FJJ | Saint-Nazaire-Montoir Airport (LFRZ) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-08-21 07:14 UTC | 2026-08-21 07:37 UTC | 22m |
| STW001 | STW | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-08-21 04:42 UTC | 2026-08-21 07:15 UTC | 2h 32m |
| N359DG |  | Los Angeles International Airport (KLAX) | Madera Municipal Airport (KMAE) | 2026-08-21 06:24 UTC | 2026-08-21 07:10 UTC | 46m |
| QLK575D | QLK | Adelaide International Airport (YPAD) | Whyalla Airport (YWHA) | 2026-08-21 06:37 UTC | 2026-08-21 07:10 UTC | 33m |
| AIQ510 | AIQ | Don Mueang International Airport (VTBD) | Senai International Airport (WMKJ) | 2026-08-21 05:12 UTC | 2026-08-21 07:08 UTC | 1h 55m |
| WIF4X | WIF | Oslo Gardermoen Airport (ENGM) | Gol Airport (ENKL) | 2026-08-21 06:33 UTC | 2026-08-21 07:08 UTC | 34m |
| RYR2ZL | Ryanair | Alicante International Airport (LEAL) | Belfast International Airport (EGAA) | 2026-08-21 04:23 UTC | 2026-08-21 07:05 UTC | 2h 41m |
| MRL11 | MRL | San Javier Airport (LELC) | Alhama De Murcia Airport (LELH) | 2026-08-21 06:49 UTC | 2026-08-21 07:04 UTC | 15m |
| IGO7HC | IndiGo | Bengaluru International Airport (VOBL) | VO80 (VO80) | 2026-08-21 05:49 UTC | 2026-08-21 07:04 UTC | 1h 15m |
| UPS18 | UPS | Cologne Bonn Airport (EDDK) | Zhuhai Airport (ZGSD) | 2026-08-20 20:45 UTC | 2026-08-21 07:03 UTC | 10h 18m |
| ELW104 | ELW | Nairobi Wilson Airport (HKNW) | Narok Airport (HKNO) | 2026-08-21 06:34 UTC | 2026-08-21 06:59 UTC | 24m |
| QLK11D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-21 06:38 UTC | 2026-08-21 06:59 UTC | 20m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-21 06:00 UTC | 2026-08-21 06:56 UTC | 55m |
| RYR5436 | Ryanair | Sevilla Airport (LEZL) | Luxembourg-Findel International Airport (ELLX) | 2026-08-21 04:45 UTC | 2026-08-21 06:54 UTC | 2h 9m |
| RYR41YE | Ryanair | Vienna International Airport (LOWW) | Palma De Mallorca Airport (LEPA) | 2026-08-21 04:40 UTC | 2026-08-21 06:49 UTC | 2h 8m |
| GAP2037 | GAP | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-08-21 06:25 UTC | 2026-08-21 06:48 UTC | 22m |
| QLK1580 | QLK | Sydney Kingsford Smith International Airport (YSSY) | Sunshine Coast Airport (YBMC) | 2026-08-21 05:28 UTC | 2026-08-21 06:46 UTC | 1h 18m |
| N911MN |  | Joe Foss Field (KFSD) | Platte Municipal Airport (K1D3) | 2026-08-21 06:20 UTC | 2026-08-21 06:45 UTC | 25m |
| KEM831 | KEM | Cape Town International Airport (FACT) | Vereeniging Airport (FAVV) | 2026-08-21 05:08 UTC | 2026-08-21 06:44 UTC | 1h 36m |
| WMT5QD | WMT | Henri Coanda International Airport (LROP) | Bilbao Airport (LEBB) | 2026-08-21 03:27 UTC | 2026-08-21 06:43 UTC | 3h 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
