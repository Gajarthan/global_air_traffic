# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_09:46:21_UTC-green)

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

**Latest saved flight:** 2026-08-23 09:46:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 09:46:21 UTC

- **228,052** saved flights
- **70,630** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **228,052** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,749,900.6 tonnes** estimated CO2 emissions
- **159,414,530 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9152 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4393 |
| 4 | IndiGo | 3858 |
| 5 | American Airlines | 3740 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2919 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2184 |
| 10 | AZU | 2112 |
| 11 | Vueling | 1935 |
| 12 | Lufthansa | 1865 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1587 |
| 16 | Swiss International | 1519 |
| 17 | AXM | 1514 |
| 18 | QLK | 1447 |
| 19 | United Airlines | 1444 |
| 20 | EJU | 1442 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1369 |
| 23 | GLO | 1264 |
| 24 | VIV | 1253 |
| 25 | PGT | 1251 |
| 26 | WMT | 1239 |
| 27 | Air France | 1237 |
| 28 | Wizz Air | 1182 |
| 29 | JetBlue | 1142 |
| 30 | AEE | 1137 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190647 |
| 2 | 🇪🇸 ES | 14621 |
| 3 | 🇧🇷 BR | 13293 |
| 4 | 🇦🇺 AU | 12943 |
| 5 | 🇨🇦 CA | 12618 |
| 6 | 🇮🇹 IT | 12276 |
| 7 | 🇮🇳 IN | 12023 |
| 8 | 🇩🇪 DE | 11215 |
| 9 | 🇬🇧 GB | 10710 |
| 10 | 🇨🇴 CO | 9384 |
| 11 | 🇯🇵 JP | 9290 |
| 12 | 🇫🇷 FR | 9115 |
| 13 | 🇹🇷 TR | 6698 |
| 14 | 🇬🇷 GR | 6694 |
| 15 | 🇲🇽 MX | 6358 |
| 16 | 🇨🇭 CH | 6023 |
| 17 | 🇳🇴 NO | 5602 |
| 18 | 🇲🇾 MY | 4039 |
| 19 | 🇹🇭 TH | 3952 |
| 20 | 🇿🇦 ZA | 3951 |
| 21 | 🇵🇱 PL | 3788 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3131 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2703 |
| 26 | 🇭🇷 HR | 2589 |
| 27 | 🇲🇦 MA | 2302 |
| 28 | 🇲🇪 ME | 2065 |
| 29 | 🇳🇱 NL | 2034 |
| 30 | 🇮🇩 ID | 1970 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3714 |
| 3 | Indira Gandhi International Airport |  | IN | 2778 |
| 4 | Tokyo International Airport |  | JP | 2774 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2473 |
| 7 | Zurich Airport |  | CH | 2369 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2332 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2302 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2084 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2009 |
| 14 | Congonhas Airport |  | BR | 1939 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1938 |
| 16 | Frankfurt am Main International Airport |  | DE | 1829 |
| 17 | Madrid Barajas International Airport |  | ES | 1778 |
| 18 | Capua Airport |  | IT | 1771 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1703 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1698 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1648 |
| 22 | Malpensa International Airport |  | IT | 1624 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1610 |
| 24 | Macau International Airport |  | MO | 1594 |
| 25 | Charles de Gaulle International Airport |  | FR | 1575 |
| 26 | Ninoy Aquino International Airport |  | PH | 1500 |
| 27 | Charlotte/Douglas International Airport |  | US | 1492 |
| 28 | Kuala Lumpur International Airport |  | MY | 1464 |
| 29 | Barcelona International Airport |  | ES | 1423 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1384 |
| 31 | Bengaluru International Airport |  | IN | 1352 |
| 32 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 33 | Viracopos International Airport |  | BR | 1348 |
| 34 | Seattle-Tacoma International Airport |  | US | 1347 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Calgary International Airport |  | CA | 1299 |
| 37 | Don Mueang International Airport |  | TH | 1295 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1231 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 832 | 21m | 244 km | 3,503.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 572 | 1h 6m | 770 km | 7,598.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 347 | 1h 50m | 1,423 km | 8,515.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 314 | 1h 7m | 706 km | 3,823.0 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 312 | 21m | 250 km | 1,347.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 15 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 302 | 44m | 555 km | 2,891.8 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 293 | 1h 38m | 1,156 km | 5,845.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 291 | 24m | 218 km | 1,096.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 260 | 19m | 144 km | 646.7 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 240 | 15m | 154 km | 635.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UPS64 | UPS | Incheon International Airport (RKSI) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-23 07:45 UTC | 2026-08-23 09:46 UTC | 2h 1m |
| RGA17 | RGA | Reichenbach Air Base (LSGR) | Muenster Aero Airport (LSPU) | 2026-08-23 09:29 UTC | 2026-08-23 09:44 UTC | 14m |
| AEE4579 | AEE | Kuopio Airport (EFKU) | Barysiai Airport (EYSB) | 2026-08-23 08:26 UTC | 2026-08-23 09:26 UTC | 1h 0m |
| ZKICU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-08-23 09:10 UTC | 2026-08-23 09:21 UTC | 10m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-08-23 08:54 UTC | 2026-08-23 09:19 UTC | 25m |
| OAL094A | OAL | Diagoras Airport (LGRP) | Kos Airport (LGKO) | 2026-08-23 08:58 UTC | 2026-08-23 09:14 UTC | 15m |
| RYR93HA | Ryanair | Barcelona International Airport (LEBL) | Bergamo / Orio Al Serio Airport (LIME) | 2026-08-23 07:56 UTC | 2026-08-23 09:09 UTC | 1h 12m |
| HBYJF | HBY | Langenthal Airport (LSPL) | Ambri Airport (LSPM) | 2026-08-23 08:22 UTC | 2026-08-23 09:07 UTC | 45m |
| BEL7NL | Brussels Airlines | Geneva Cointrin International Airport (LSGG) | Brussels Airport (EBBR) | 2026-08-23 07:16 UTC | 2026-08-23 09:06 UTC | 1h 50m |
| VOE1ZP | VOE | Alicante International Airport (LEAL) | La Morgal Airport (LEMR) | 2026-08-23 07:52 UTC | 2026-08-23 08:58 UTC | 1h 6m |
| BAW88LP | British Airways | London Heathrow Airport (EGLL) | Hannover Airport (EDDV) | 2026-08-23 07:50 UTC | 2026-08-23 08:57 UTC | 1h 7m |
| FHCJQ | FHC | Biarritz-Anglet-Bayonne Airport (LFBZ) | Itxassou Airport (LFIX) | 2026-08-23 08:48 UTC | 2026-08-23 08:53 UTC | 4m |
| NJE348N | NJE | George Best Belfast City Airport (EGAC) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-23 07:15 UTC | 2026-08-23 08:53 UTC | 1h 38m |
| FPTUN | FPT | Ambri Airport (LSPM) | Ambri Airport (LSPM) | 2026-08-23 08:32 UTC | 2026-08-23 08:52 UTC | 20m |
| JAL2825 | Japan Airlines | Okadama Airport (RJCO) | Odate Noshiro Airport (RJSR) | 2026-08-23 08:05 UTC | 2026-08-23 08:51 UTC | 46m |
| RYR866B | Ryanair | Eindhoven Airport (EHEH) | Bergamo / Orio Al Serio Airport (LIME) | 2026-08-23 07:45 UTC | 2026-08-23 08:49 UTC | 1h 3m |
| WMT1097 | WMT | Ciampino Airport (LIRA) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-23 08:23 UTC | 2026-08-23 08:49 UTC | 25m |
| VLG2RE | Vueling | Palma De Mallorca Airport (LEPA) | Bilbao Airport (LEBB) | 2026-08-23 07:51 UTC | 2026-08-23 08:46 UTC | 55m |
| CWA921 | CWA | Edmonton International Airport (CYEG) | Mayerthorpe Airport (CEV5) | 2026-08-23 08:28 UTC | 2026-08-23 08:45 UTC | 17m |
| JAL2009 | Japan Airlines | Osaka International Airport (RJOO) | Chitose Air Base (RJCJ) | 2026-08-23 07:09 UTC | 2026-08-23 08:45 UTC | 1h 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
