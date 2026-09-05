# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_12:48:19_UTC-green)

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

**Latest saved flight:** 2026-09-05 12:48:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-05 12:48:19 UTC

- **248,212** saved flights
- **74,758** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **248,212** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,986,490.5 tonnes** estimated CO2 emissions
- **173,129,887 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9944 |
| 2 | SkyWest Airlines | 8670 |
| 3 | EJA | 4792 |
| 4 | IndiGo | 4147 |
| 5 | American Airlines | 3976 |
| 6 | Southwest Airlines | 3694 |
| 7 | Delta Air Lines | 3152 |
| 8 | ENY | 2966 |
| 9 | LATAM Airlines | 2395 |
| 10 | AZU | 2313 |
| 11 | Vueling | 2120 |
| 12 | WIF | 1984 |
| 13 | Lufthansa | 1972 |
| 14 | LXJ | 1927 |
| 15 | easyJet | 1715 |
| 16 | Swiss International | 1663 |
| 17 | AXM | 1627 |
| 18 | EJU | 1594 |
| 19 | QLK | 1591 |
| 20 | United Airlines | 1559 |
| 21 | Alaska Airlines | 1482 |
| 22 | All Nippon Airways | 1455 |
| 23 | WMT | 1401 |
| 24 | GLO | 1382 |
| 25 | VIV | 1365 |
| 26 | PGT | 1359 |
| 27 | Air France | 1357 |
| 28 | Wizz Air | 1341 |
| 29 | JetBlue | 1222 |
| 30 | AEE | 1220 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 205862 |
| 2 | 🇪🇸 ES | 15890 |
| 3 | 🇧🇷 BR | 14514 |
| 4 | 🇦🇺 AU | 14103 |
| 5 | 🇨🇦 CA | 13792 |
| 6 | 🇮🇹 IT | 13596 |
| 7 | 🇮🇳 IN | 12938 |
| 8 | 🇩🇪 DE | 12197 |
| 9 | 🇬🇧 GB | 11661 |
| 10 | 🇨🇴 CO | 10835 |
| 11 | 🇫🇷 FR | 9994 |
| 12 | 🇯🇵 JP | 9814 |
| 13 | 🇹🇷 TR | 7395 |
| 14 | 🇬🇷 GR | 7307 |
| 15 | 🇲🇽 MX | 6866 |
| 16 | 🇨🇭 CH | 6690 |
| 17 | 🇳🇴 NO | 6151 |
| 18 | 🇹🇭 TH | 4489 |
| 19 | 🇲🇾 MY | 4362 |
| 20 | 🇿🇦 ZA | 4291 |
| 21 | 🇵🇱 PL | 4153 |
| 22 | 🇳🇿 NZ | 3397 |
| 23 | 🇵🇭 PH | 3379 |
| 24 | 🇬🇹 GT | 3100 |
| 25 | 🇰🇷 KR | 2886 |
| 26 | 🇭🇷 HR | 2854 |
| 27 | 🇲🇦 MA | 2509 |
| 28 | 🇲🇪 ME | 2317 |
| 29 | 🇳🇱 NL | 2236 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5108 |
| 2 | Denver International Airport |  | US | 4008 |
| 3 | Indira Gandhi International Airport |  | IN | 3024 |
| 4 | Tokyo International Airport |  | JP | 2928 |
| 5 | Guaymaral Airport |  | CO | 2724 |
| 6 | Harry Reid International Airport |  | US | 2649 |
| 7 | Zurich Airport |  | CH | 2595 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2523 |
| 9 | El Dorado International Airport |  | CO | 2484 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2468 |
| 11 | La Aurora Airport |  | GT | 2359 |
| 12 | Salt Lake City International Airport |  | US | 2199 |
| 13 | Chicago O'Hare International Airport |  | US | 2177 |
| 14 | Congonhas Airport |  | BR | 2132 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2045 |
| 16 | Capua Airport |  | IT | 1954 |
| 17 | Madrid Barajas International Airport |  | ES | 1947 |
| 18 | Frankfurt am Main International Airport |  | DE | 1943 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1864 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1812 |
| 21 | Malpensa International Airport |  | IT | 1784 |
| 22 | Charles de Gaulle International Airport |  | FR | 1744 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1742 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1728 |
| 25 | Ninoy Aquino International Airport |  | PH | 1645 |
| 26 | Macau International Airport |  | MO | 1637 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1627 |
| 28 | Charlotte/Douglas International Airport |  | US | 1573 |
| 29 | Barcelona International Airport |  | ES | 1570 |
| 30 | Kuala Lumpur International Airport |  | MY | 1570 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1521 |
| 32 | Viracopos International Airport |  | BR | 1483 |
| 33 | Seattle-Tacoma International Airport |  | US | 1462 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1446 |
| 35 | Don Mueang International Airport |  | TH | 1440 |
| 36 | Calgary International Airport |  | CA | 1430 |
| 37 | Bengaluru International Airport |  | IN | 1427 |
| 38 | Oslo Gardermoen Airport |  | NO | 1396 |
| 39 | Vancouver International Airport |  | CA | 1388 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1347 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 921 | 21m | 244 km | 3,878.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 654 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 629 | 24m | 225 km | 2,440.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 624 | 1h 6m | 770 km | 8,289.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 554 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 408 | 27m | 275 km | 1,933.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 397 | 1h 50m | 1,423 km | 9,743.0 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 387 | 44m | 555 km | 3,705.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 369 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 367 | 44m | 241 km | 1,524.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 351 | 21m | 250 km | 1,516.1 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 348 | 24m | 218 km | 1,311.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 333 | 23m | 55 km | 316.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 295 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 287 | 1h 14m | 961 km | 4,757.2 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 287 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 284 | 19m | 144 km | 706.4 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 255 | 28m | 152 km | 666.4 t |
| 30 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 254 | 41m | 535 km | 2,345.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FGRUB | FGR | Maubeuge-Elesmes Airport (LFQJ) | Maubeuge-Elesmes Airport (LFQJ) | 2026-09-05 12:07 UTC | 2026-09-05 12:48 UTC | 40m |
| N699SA |  | Leutkirch-Unterzeil Airport (EDNL) | Leutkirch-Unterzeil Airport (EDNL) | 2026-09-05 11:03 UTC | 2026-09-05 12:43 UTC | 1h 40m |
| SAS789 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Olbia / Costa Smeralda Airport (LIEO) | 2026-09-05 10:42 UTC | 2026-09-05 12:43 UTC | 2h 1m |
| SIO512 | SIO | Ancona / Falconara Airport (LIPY) | Olbia / Costa Smeralda Airport (LIEO) | 2026-09-05 12:09 UTC | 2026-09-05 12:42 UTC | 33m |
| CFG9KH | CFG | Munich International Airport (EDDM) | Palma De Mallorca Airport (LEPA) | 2026-09-05 11:04 UTC | 2026-09-05 12:39 UTC | 1h 35m |
| N145FH |  | Ormond Beach Municipal Airport (KOMN) | Orlando Executive Airport (KORL) | 2026-09-05 12:13 UTC | 2026-09-05 12:35 UTC | 21m |
| GAZRZ | GAZ | Truro Airport (EGHY) | Truro Airport (EGHY) | 2026-09-05 12:32 UTC | 2026-09-05 12:34 UTC | 2m |
| N1212U |  | Shady International Airport (FA49) | KX40 (KX40) | 2026-09-05 12:14 UTC | 2026-09-05 12:31 UTC | 16m |
| RJA302 | Royal Jordanian | Queen Alia International Airport (OJAI) | LLYO (LLYO) | 2026-09-05 11:46 UTC | 2026-09-05 12:16 UTC | 29m |
| SRG897 | SRG | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-09-05 12:04 UTC | 2026-09-05 12:15 UTC | 10m |
| NHL06 | NHL | Redhill Aerodrome (EGKR) | Redhill Aerodrome (EGKR) | 2026-09-05 11:40 UTC | 2026-09-05 12:14 UTC | 34m |
| GCLXB | GCL | RAF Church Fenton (EGXG) | EGNU (EGNU) | 2026-09-05 12:06 UTC | 2026-09-05 12:10 UTC | 4m |
| OKHEZ | OKH | Frydlant Airport (LKFR) | Frydlant Airport (LKFR) | 2026-09-05 11:54 UTC | 2026-09-05 12:10 UTC | 15m |
| N566RG |  | Bay Minette Municipal Airport (K1R8) | Bay Minette Municipal Airport (K1R8) | 2026-09-05 12:07 UTC | 2026-09-05 12:09 UTC | 2m |
| DFANO | DFA | Æra Airfield (ENAE) | Æra Airfield (ENAE) | 2026-09-05 11:56 UTC | 2026-09-05 12:09 UTC | 12m |
| PH1B1 |  | Buchel Airport (ETSB) | Twenthe Airport (EHTW) | 2026-09-05 10:40 UTC | 2026-09-05 12:07 UTC | 1h 26m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Zhuhai Airport (ZGSD) | 2026-09-04 21:26 UTC | 2026-09-05 12:04 UTC | 14h 37m |
| LBQ651 | LBQ | New Century Aircenter Airport (KIXD) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-09-05 09:59 UTC | 2026-09-05 12:02 UTC | 2h 2m |
| JJA1395 | JJA | Incheon International Airport (RKSI) | Kansai International Airport (RJBB) | 2026-09-05 10:34 UTC | 2026-09-05 11:52 UTC | 1h 17m |
| SEH6JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-09-05 11:19 UTC | 2026-09-05 11:46 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
