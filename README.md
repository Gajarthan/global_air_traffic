# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_11:13:13_UTC-green)

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

**Latest saved flight:** 2026-09-20 11:13:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-20 11:13:13 UTC

- **264,303** saved flights
- **78,002** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **264,303** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,203,897.6 tonnes** estimated CO2 emissions
- **185,733,197 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10460 |
| 2 | SkyWest Airlines | 9187 |
| 3 | EJA | 5136 |
| 4 | IndiGo | 4446 |
| 5 | American Airlines | 4133 |
| 6 | Southwest Airlines | 3887 |
| 7 | Delta Air Lines | 3290 |
| 8 | ENY | 3114 |
| 9 | LATAM Airlines | 2551 |
| 10 | AZU | 2486 |
| 11 | Vueling | 2218 |
| 12 | WIF | 2131 |
| 13 | LXJ | 2070 |
| 14 | Lufthansa | 2034 |
| 15 | easyJet | 1783 |
| 16 | Swiss International | 1743 |
| 17 | QLK | 1708 |
| 18 | EJU | 1666 |
| 19 | AXM | 1662 |
| 20 | United Airlines | 1621 |
| 21 | Alaska Airlines | 1567 |
| 22 | All Nippon Airways | 1525 |
| 23 | PGT | 1486 |
| 24 | WMT | 1485 |
| 25 | GLO | 1471 |
| 26 | Air France | 1447 |
| 27 | VIV | 1444 |
| 28 | Wizz Air | 1434 |
| 29 | CXK | 1279 |
| 30 | TKR | 1275 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 219549 |
| 2 | 🇪🇸 ES | 16644 |
| 3 | 🇧🇷 BR | 15470 |
| 4 | 🇦🇺 AU | 15145 |
| 5 | 🇨🇦 CA | 14712 |
| 6 | 🇮🇹 IT | 14378 |
| 7 | 🇮🇳 IN | 14059 |
| 8 | 🇩🇪 DE | 12760 |
| 9 | 🇬🇧 GB | 12266 |
| 10 | 🇨🇴 CO | 11995 |
| 11 | 🇫🇷 FR | 10559 |
| 12 | 🇯🇵 JP | 10226 |
| 13 | 🇹🇷 TR | 8008 |
| 14 | 🇬🇷 GR | 7665 |
| 15 | 🇲🇽 MX | 7270 |
| 16 | 🇨🇭 CH | 7055 |
| 17 | 🇳🇴 NO | 6524 |
| 18 | 🇹🇭 TH | 4738 |
| 19 | 🇲🇾 MY | 4480 |
| 20 | 🇿🇦 ZA | 4446 |
| 21 | 🇵🇱 PL | 4356 |
| 22 | 🇳🇿 NZ | 3678 |
| 23 | 🇵🇭 PH | 3521 |
| 24 | 🇬🇹 GT | 3366 |
| 25 | 🇭🇷 HR | 3015 |
| 26 | 🇰🇷 KR | 2999 |
| 27 | 🇲🇦 MA | 2648 |
| 28 | 🇲🇪 ME | 2478 |
| 29 | 🇳🇱 NL | 2370 |
| 30 | 🇮🇩 ID | 2220 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5399 |
| 2 | Denver International Airport |  | US | 4275 |
| 3 | Indira Gandhi International Airport |  | IN | 3181 |
| 4 | Tokyo International Airport |  | JP | 3055 |
| 5 | Harry Reid International Airport |  | US | 2812 |
| 6 | El Dorado International Airport |  | CO | 2811 |
| 7 | Guaymaral Airport |  | CO | 2785 |
| 8 | Zurich Airport |  | CH | 2748 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2654 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2558 |
| 11 | La Aurora Airport |  | GT | 2557 |
| 12 | Salt Lake City International Airport |  | US | 2330 |
| 13 | Chicago O'Hare International Airport |  | US | 2270 |
| 14 | Congonhas Airport |  | BR | 2255 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2158 |
| 16 | Capua Airport |  | IT | 2067 |
| 17 | Madrid Barajas International Airport |  | ES | 2041 |
| 18 | Frankfurt am Main International Airport |  | DE | 2016 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1996 |
| 20 | Malpensa International Airport |  | IT | 1905 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1891 |
| 22 | Charles de Gaulle International Airport |  | FR | 1868 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1862 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1836 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1804 |
| 26 | Macau International Airport |  | MO | 1760 |
| 27 | Ninoy Aquino International Airport |  | PH | 1729 |
| 28 | Barcelona International Airport |  | ES | 1650 |
| 29 | Charlotte/Douglas International Airport |  | US | 1647 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1625 |
| 31 | Kuala Lumpur International Airport |  | MY | 1606 |
| 32 | Viracopos International Airport |  | BR | 1603 |
| 33 | Seattle-Tacoma International Airport |  | US | 1552 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1541 |
| 35 | Calgary International Airport |  | CA | 1507 |
| 36 | Don Mueang International Airport |  | TH | 1503 |
| 37 | Bengaluru International Airport |  | IN | 1501 |
| 38 | Oslo Gardermoen Airport |  | NO | 1486 |
| 39 | Vancouver International Airport |  | CA | 1479 |
| 40 | Antalya International Airport |  | TR | 1417 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1113 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 989 | 21m | 244 km | 4,164.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 725 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 665 | 1h 6m | 770 km | 8,834.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 659 | 24m | 225 km | 2,556.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 591 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 430 | 44m | 555 km | 4,117.5 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 420 | 1h 50m | 1,423 km | 10,307.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 402 | 44m | 241 km | 1,669.8 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 379 | 24m | 218 km | 1,427.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 338 | 12m | - | - |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 333 | 19m | 99 km | 570.4 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 327 | 26m | 215 km | 1,211.1 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 326 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 286 | 1h 50m | 1,304 km | 6,434.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 285 | 42m | 535 km | 2,632.2 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 282 | 28m | 152 km | 737.0 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 266 | 18m | 14 km | 66.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HB1982 |  | Buttwil Airport (LSZU) | Buttwil Airport (LSZU) | 2026-09-20 10:29 UTC | 2026-09-20 11:13 UTC | 43m |
| GXMGO | GXM | RAF Rufforth (EG64) | RAF Dishforth (EGXD) | 2026-09-20 10:26 UTC | 2026-09-20 11:11 UTC | 44m |
| YRTWI | YRT | LRPV (LRPV) | LRPV (LRPV) | 2026-09-20 10:31 UTC | 2026-09-20 11:11 UTC | 39m |
| VOZ978 | Virgin Australia | Brisbane International Airport (YBBN) | Sydney Kingsford Smith International Airport (YSSY) | 2026-09-20 09:41 UTC | 2026-09-20 11:08 UTC | 1h 27m |
| WIF8HK | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-09-20 10:46 UTC | 2026-09-20 11:03 UTC | 17m |
| FJJJY | FJJ | Saint-Nazaire-Montoir Airport (LFRZ) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-09-20 10:27 UTC | 2026-09-20 10:58 UTC | 31m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Zhuhai Airport (ZGSD) | 2026-09-19 23:49 UTC | 2026-09-20 10:52 UTC | 11h 3m |
| LOT3517 | LOT Polish Airlines | Gdańsk Lech Wałęsa Airport (EPGD) | Katowice International Airport (EPKT) | 2026-09-20 09:48 UTC | 2026-09-20 10:51 UTC | 1h 3m |
| QTR8040 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-09-20 03:22 UTC | 2026-09-20 10:47 UTC | 7h 24m |
| SBI6409 | SBI | Achinsk Airport (UNKS) | Savvatiya Air Base (ULKS) | 2026-09-20 03:28 UTC | 2026-09-20 10:45 UTC | 7h 17m |
| VLG4WW | Vueling | Barcelona International Airport (LEBL) | Mollis Airport (LSZM) | 2026-09-20 09:22 UTC | 2026-09-20 10:44 UTC | 1h 22m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-09-20 10:12 UTC | 2026-09-20 10:43 UTC | 30m |
| N767BS |  | Reading Regional/Carl A Spaatz Field (KRDG) | Lehigh Valley International Airport (KABE) | 2026-09-20 10:29 UTC | 2026-09-20 10:41 UTC | 11m |
| DLH7LL | Lufthansa | Munich International Airport (EDDM) | Munster Osnabruck Airport (EDDG) | 2026-09-20 09:48 UTC | 2026-09-20 10:40 UTC | 52m |
| RYR65SB | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Trapani / Birgi Airport (LICT) | 2026-09-20 09:30 UTC | 2026-09-20 10:39 UTC | 1h 8m |
| OMM654 | OMM | LZRY (LZRY) | LZRY (LZRY) | 2026-09-20 09:30 UTC | 2026-09-20 10:34 UTC | 1h 4m |
| BNO93J | BNO | Bergen Airport Flesland (ENBR) | Trondheim Airport Vaernes (ENVA) | 2026-09-20 09:50 UTC | 2026-09-20 10:31 UTC | 41m |
| OEFDV | OEF | Klatovy Airport (LKKT) | Ceske Budejovice Airport (LKCS) | 2026-09-20 10:06 UTC | 2026-09-20 10:28 UTC | 21m |
| BHA709 | BHA | Tribhuvan International Airport (VNKT) | Thamkharka Airport (VNTH) | 2026-09-20 10:00 UTC | 2026-09-20 10:28 UTC | 27m |
| SWR431M | Swiss International | Geneva Cointrin International Airport (LSGG) | Palma De Mallorca Airport (LEPA) | 2026-09-20 09:16 UTC | 2026-09-20 10:27 UTC | 1h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
