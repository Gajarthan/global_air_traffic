# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_11:13:48_UTC-green)

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

**Latest saved flight:** 2026-08-22 11:13:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 11:13:48 UTC

- **225,248** saved flights
- **70,128** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **225,248** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,714,183.4 tonnes** estimated CO2 emissions
- **157,343,962 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9035 |
| 2 | SkyWest Airlines | 7997 |
| 3 | EJA | 4353 |
| 4 | IndiGo | 3809 |
| 5 | American Airlines | 3705 |
| 6 | Southwest Airlines | 3524 |
| 7 | Delta Air Lines | 2879 |
| 8 | ENY | 2759 |
| 9 | LATAM Airlines | 2142 |
| 10 | AZU | 2074 |
| 11 | Vueling | 1902 |
| 12 | Lufthansa | 1851 |
| 13 | WIF | 1791 |
| 14 | LXJ | 1777 |
| 15 | easyJet | 1559 |
| 16 | Swiss International | 1500 |
| 17 | AXM | 1489 |
| 18 | QLK | 1421 |
| 19 | EJU | 1419 |
| 20 | United Airlines | 1417 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1355 |
| 23 | GLO | 1244 |
| 24 | PGT | 1239 |
| 25 | VIV | 1231 |
| 26 | Air France | 1225 |
| 27 | WMT | 1207 |
| 28 | Wizz Air | 1164 |
| 29 | JetBlue | 1129 |
| 30 | AEE | 1122 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188745 |
| 2 | 🇪🇸 ES | 14431 |
| 3 | 🇧🇷 BR | 13059 |
| 4 | 🇦🇺 AU | 12772 |
| 5 | 🇨🇦 CA | 12480 |
| 6 | 🇮🇹 IT | 12066 |
| 7 | 🇮🇳 IN | 11879 |
| 8 | 🇩🇪 DE | 11094 |
| 9 | 🇬🇧 GB | 10566 |
| 10 | 🇨🇴 CO | 9256 |
| 11 | 🇯🇵 JP | 9178 |
| 12 | 🇫🇷 FR | 8999 |
| 13 | 🇹🇷 TR | 6593 |
| 14 | 🇬🇷 GR | 6575 |
| 15 | 🇲🇽 MX | 6259 |
| 16 | 🇨🇭 CH | 5936 |
| 17 | 🇳🇴 NO | 5575 |
| 18 | 🇲🇾 MY | 3966 |
| 19 | 🇿🇦 ZA | 3897 |
| 20 | 🇹🇭 TH | 3862 |
| 21 | 🇵🇱 PL | 3734 |
| 22 | 🇳🇿 NZ | 3138 |
| 23 | 🇵🇭 PH | 3075 |
| 24 | 🇬🇹 GT | 2850 |
| 25 | 🇰🇷 KR | 2674 |
| 26 | 🇭🇷 HR | 2530 |
| 27 | 🇲🇦 MA | 2263 |
| 28 | 🇲🇪 ME | 2013 |
| 29 | 🇳🇱 NL | 2004 |
| 30 | 🇮🇩 ID | 1945 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4706 |
| 2 | Denver International Airport |  | US | 3670 |
| 3 | Tokyo International Airport |  | JP | 2742 |
| 4 | Indira Gandhi International Airport |  | IN | 2737 |
| 5 | Guaymaral Airport |  | CO | 2630 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2339 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2275 |
| 10 | La Aurora Airport |  | GT | 2172 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1979 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 15 | Congonhas Airport |  | BR | 1909 |
| 16 | Frankfurt am Main International Airport |  | DE | 1816 |
| 17 | Madrid Barajas International Airport |  | ES | 1760 |
| 18 | Capua Airport |  | IT | 1734 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1678 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1668 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1634 |
| 22 | Macau International Airport |  | MO | 1593 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1589 |
| 24 | Malpensa International Airport |  | IT | 1585 |
| 25 | Charles de Gaulle International Airport |  | FR | 1560 |
| 26 | Charlotte/Douglas International Airport |  | US | 1483 |
| 27 | Ninoy Aquino International Airport |  | PH | 1470 |
| 28 | Kuala Lumpur International Airport |  | MY | 1442 |
| 29 | Barcelona International Airport |  | ES | 1392 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1368 |
| 31 | Bengaluru International Airport |  | IN | 1342 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1333 |
| 33 | Seattle-Tacoma International Airport |  | US | 1329 |
| 34 | Viracopos International Airport |  | BR | 1323 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1303 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1268 |
| 38 | Oslo Gardermoen Airport |  | NO | 1255 |
| 39 | Vitoria/Foronda Airport |  | ES | 1242 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1217 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1072 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 815 | 21m | 244 km | 3,431.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 561 | 1h 7m | 770 km | 7,452.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 527 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 510 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 354 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 338 | 1h 50m | 1,423 km | 8,295.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 327 | 44m | 241 km | 1,358.3 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 301 | 21m | 250 km | 1,300.1 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 289 | 44m | 555 km | 2,767.3 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 286 | 1h 38m | 1,156 km | 5,705.6 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 283 | 24m | 218 km | 1,066.2 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 280 | 19m | 99 km | 479.6 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 264 | 1h 14m | 961 km | 4,375.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 257 | 19m | 144 km | 639.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4431R |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-22 11:03 UTC | 2026-08-22 11:13 UTC | 10m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-22 10:42 UTC | 2026-08-22 10:54 UTC | 11m |
| N961LA |  | Long Beach (Daugherty Field) Airport (KLGB) | San Gabriel Valley Airport (KEMT) | 2026-08-22 08:08 UTC | 2026-08-22 10:39 UTC | 2h 31m |
| IAM9001 | IAM | Ciampino Airport (LIRA) | Trento / Mattarello Airport (LIDT) | 2026-08-22 09:49 UTC | 2026-08-22 10:37 UTC | 48m |
| THY1EM | Turkish Airlines | Maritsa Airport (LGRD) | Pushkin Airport (ULLP) | 2026-08-22 04:59 UTC | 2026-08-22 10:35 UTC | 5h 35m |
| BNO42S | BNO | Harstad/Narvik Airport Evenes (ENEV) | Trondheim Airport Vaernes (ENVA) | 2026-08-22 09:25 UTC | 2026-08-22 10:22 UTC | 56m |
| RYR69CX | Ryanair | Vienna International Airport (LOWW) | Kalamata Airport (LGKL) | 2026-08-22 08:36 UTC | 2026-08-22 10:16 UTC | 1h 40m |
| RYR79DW | Ryanair | Dublin Airport (EIDW) | Vienna International Airport (LOWW) | 2026-08-22 07:55 UTC | 2026-08-22 10:13 UTC | 2h 17m |
| TKJ5NE | TKJ | Zafer Airport (LTBZ) | Antalya International Airport (LTAI) | 2026-08-22 09:29 UTC | 2026-08-22 10:12 UTC | 42m |
| EMD556 | EMD | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-08-22 09:58 UTC | 2026-08-22 10:11 UTC | 12m |
| PGT95CJ | PGT | Bydgoszcz-Biedaszkowo Airport (EPBD) | Antalya International Airport (LTAI) | 2026-08-22 07:07 UTC | 2026-08-22 10:08 UTC | 3h 1m |
| CTV764 | CTV | Soekarno-Hatta International Airport (WIII) | Achmad Yani Airport (WARS) | 2026-08-22 09:32 UTC | 2026-08-22 10:08 UTC | 35m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-22 09:35 UTC | 2026-08-22 10:04 UTC | 29m |
| RYR28SK | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Bari / Palese International Airport (LIBD) | 2026-08-22 09:16 UTC | 2026-08-22 10:04 UTC | 47m |
|  |  | Mendig Airport (ETHM) | Mendig Airport (ETHM) | 2026-08-22 10:00 UTC | 2026-08-22 10:00 UTC | 0m |
| EDW21W | EDW | Itxassou Airport (LFIX) | Zurich Airport (LSZH) | 2026-08-22 08:34 UTC | 2026-08-22 10:00 UTC | 1h 26m |
| HYS7621 | HYS | Henri Coanda International Airport (LROP) | Antalya International Airport (LTAI) | 2026-08-22 08:25 UTC | 2026-08-22 09:58 UTC | 1h 33m |
| TVJ306 | TVJ | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 2026-08-22 09:14 UTC | 2026-08-22 09:57 UTC | 43m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-22 09:33 UTC | 2026-08-22 09:57 UTC | 23m |
| WWF287 | WWF | Roberts Field/Redmond Municipal Airport (KRDM) | Josephine Ranch Airport (2ID3) | 2026-08-22 07:47 UTC | 2026-08-22 09:56 UTC | 2h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
