# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_19:53:50_UTC-green)

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

**Latest saved flight:** 2026-08-26 19:53:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 19:53:50 UTC

- **239,487** saved flights
- **72,802** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **239,487** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,884,508.4 tonnes** estimated CO2 emissions
- **167,217,878 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9621 |
| 2 | SkyWest Airlines | 8413 |
| 3 | EJA | 4634 |
| 4 | IndiGo | 4038 |
| 5 | American Airlines | 3871 |
| 6 | Southwest Airlines | 3616 |
| 7 | Delta Air Lines | 3046 |
| 8 | ENY | 2894 |
| 9 | LATAM Airlines | 2296 |
| 10 | AZU | 2228 |
| 11 | Vueling | 2061 |
| 12 | Lufthansa | 1935 |
| 13 | WIF | 1901 |
| 14 | LXJ | 1859 |
| 15 | easyJet | 1669 |
| 16 | Swiss International | 1611 |
| 17 | AXM | 1591 |
| 18 | EJU | 1536 |
| 19 | QLK | 1527 |
| 20 | United Airlines | 1511 |
| 21 | Alaska Airlines | 1432 |
| 22 | All Nippon Airways | 1422 |
| 23 | WMT | 1348 |
| 24 | GLO | 1336 |
| 25 | VIV | 1316 |
| 26 | Air France | 1310 |
| 27 | PGT | 1305 |
| 28 | Wizz Air | 1284 |
| 29 | AEE | 1188 |
| 30 | JetBlue | 1187 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 198406 |
| 2 | 🇪🇸 ES | 15409 |
| 3 | 🇧🇷 BR | 13968 |
| 4 | 🇦🇺 AU | 13575 |
| 5 | 🇨🇦 CA | 13296 |
| 6 | 🇮🇹 IT | 13107 |
| 7 | 🇮🇳 IN | 12576 |
| 8 | 🇩🇪 DE | 11834 |
| 9 | 🇬🇧 GB | 11316 |
| 10 | 🇨🇴 CO | 10237 |
| 11 | 🇯🇵 JP | 9652 |
| 12 | 🇫🇷 FR | 9651 |
| 13 | 🇹🇷 TR | 7115 |
| 14 | 🇬🇷 GR | 7061 |
| 15 | 🇲🇽 MX | 6623 |
| 16 | 🇨🇭 CH | 6426 |
| 17 | 🇳🇴 NO | 5925 |
| 18 | 🇹🇭 TH | 4338 |
| 19 | 🇲🇾 MY | 4264 |
| 20 | 🇿🇦 ZA | 4207 |
| 21 | 🇵🇱 PL | 3986 |
| 22 | 🇵🇭 PH | 3294 |
| 23 | 🇳🇿 NZ | 3291 |
| 24 | 🇬🇹 GT | 3002 |
| 25 | 🇰🇷 KR | 2842 |
| 26 | 🇭🇷 HR | 2771 |
| 27 | 🇲🇦 MA | 2425 |
| 28 | 🇲🇪 ME | 2244 |
| 29 | 🇳🇱 NL | 2171 |
| 30 | 🇮🇩 ID | 2103 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4949 |
| 2 | Denver International Airport |  | US | 3866 |
| 3 | Indira Gandhi International Airport |  | IN | 2926 |
| 4 | Tokyo International Airport |  | JP | 2873 |
| 5 | Guaymaral Airport |  | CO | 2692 |
| 6 | Harry Reid International Airport |  | US | 2546 |
| 7 | Zurich Airport |  | CH | 2509 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2452 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2393 |
| 10 | El Dorado International Airport |  | CO | 2308 |
| 11 | La Aurora Airport |  | GT | 2291 |
| 12 | Chicago O'Hare International Airport |  | US | 2141 |
| 13 | Salt Lake City International Airport |  | US | 2104 |
| 14 | Congonhas Airport |  | BR | 2038 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1994 |
| 16 | Frankfurt am Main International Airport |  | DE | 1898 |
| 17 | Capua Airport |  | IT | 1891 |
| 18 | Madrid Barajas International Airport |  | ES | 1880 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1804 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1761 |
| 21 | Malpensa International Airport |  | IT | 1718 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1688 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1680 |
| 24 | Charles de Gaulle International Airport |  | FR | 1675 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1598 |
| 27 | Kuala Lumpur International Airport |  | MY | 1541 |
| 28 | Charlotte/Douglas International Airport |  | US | 1536 |
| 29 | Barcelona International Airport |  | ES | 1525 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1516 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1447 |
| 32 | Viracopos International Airport |  | BR | 1427 |
| 33 | Don Mueang International Airport |  | TH | 1400 |
| 34 | Bengaluru International Airport |  | IN | 1399 |
| 35 | Seattle-Tacoma International Airport |  | US | 1394 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1392 |
| 37 | Calgary International Airport |  | CA | 1374 |
| 38 | Oslo Gardermoen Airport |  | NO | 1345 |
| 39 | Vancouver International Airport |  | CA | 1315 |
| 40 | O. R. Tambo International Airport |  | ZA | 1312 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1090 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 881 | 21m | 244 km | 3,709.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 613 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 609 | 24m | 225 km | 2,362.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 607 | 1h 6m | 770 km | 8,063.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 541 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 396 | 27m | 275 km | 1,876.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 375 | 1h 50m | 1,423 km | 9,203.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 365 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 361 | 44m | 555 km | 3,456.7 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 347 | 44m | 241 km | 1,441.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 326 | 24m | 218 km | 1,228.2 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 319 | 22m | 55 km | 303.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 318 | 1h 40m | 1,156 km | 6,344.0 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 297 | 19m | 99 km | 508.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 292 | 27m | 215 km | 1,081.4 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 277 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 271 | 19m | 144 km | 674.1 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 257 | 1h 50m | 1,304 km | 5,781.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EJU57VZ | EJU | Edinburgh Airport (EGPH) | Amsterdam Airport Schiphol (EHAM) | 2026-08-26 18:52 UTC | 2026-08-26 19:53 UTC | 1h 1m |
| CGZSN | CGZ | Dungannon (CDG3) | Dungannon (CDG3) | 2026-08-26 19:39 UTC | 2026-08-26 19:50 UTC | 10m |
| N79975 |  | Peters Airport (4NJ8) | Princeton Airport (K39N) | 2026-08-26 19:34 UTC | 2026-08-26 19:50 UTC | 15m |
| N15000 |  | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-08-26 19:24 UTC | 2026-08-26 19:46 UTC | 22m |
| LSXX | LSX | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-26 18:53 UTC | 2026-08-26 19:46 UTC | 53m |
| TRTUGA91 | TRT | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-26 19:30 UTC | 2026-08-26 19:45 UTC | 15m |
| N535KT |  | Talkeetna Village Strip (AK44) | Helio Airport (2AK7) | 2026-08-26 19:15 UTC | 2026-08-26 19:44 UTC | 29m |
| LW706 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-26 18:47 UTC | 2026-08-26 19:42 UTC | 55m |
| N636KT |  | Talkeetna Village Strip (AK44) | Helio Airport (2AK7) | 2026-08-26 19:10 UTC | 2026-08-26 19:42 UTC | 32m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-26 19:07 UTC | 2026-08-26 19:39 UTC | 32m |
| N57RD |  | Wings Field (KLOM) | Slack Airport (18PA) | 2026-08-26 19:22 UTC | 2026-08-26 19:39 UTC | 17m |
| STW011 | STW | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-08-26 16:33 UTC | 2026-08-26 19:38 UTC | 3h 5m |
| N360CH |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-26 19:33 UTC | 2026-08-26 19:38 UTC | 4m |
| BOX714 | BOX | Dubai International Airport (OMDB) | Zhuhai Airport (ZGSD) | 2026-08-26 12:49 UTC | 2026-08-26 19:34 UTC | 6h 44m |
| MAFFS2 | MAF | Boise Air Trml/Gowen Field (KBOI) | Skinner Ranch Airport (12OR) | 2026-08-26 19:16 UTC | 2026-08-26 19:31 UTC | 14m |
| XBPBH | XBP | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-08-26 18:59 UTC | 2026-08-26 19:28 UTC | 28m |
| N6094E |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-26 18:54 UTC | 2026-08-26 19:27 UTC | 33m |
| N3028E |  | Linden Airport (KLDJ) | Central Jersey Regional Airport (K47N) | 2026-08-26 18:37 UTC | 2026-08-26 19:25 UTC | 48m |
| N591SS |  | Reno/Tahoe International Airport (KRNO) | Carson City Airport (KCXP) | 2026-08-26 19:10 UTC | 2026-08-26 19:23 UTC | 12m |
| CGZSN | CGZ | London Airport (CYXU) | Dungannon (CDG3) | 2026-08-26 18:36 UTC | 2026-08-26 19:21 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
