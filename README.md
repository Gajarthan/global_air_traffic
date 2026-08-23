# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_20:18:39_UTC-green)

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

**Latest saved flight:** 2026-08-23 20:18:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 20:18:39 UTC

- **230,011** saved flights
- **71,019** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **230,011** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,774,107.5 tonnes** estimated CO2 emissions
- **160,817,826 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9241 |
| 2 | SkyWest Airlines | 8162 |
| 3 | EJA | 4448 |
| 4 | IndiGo | 3881 |
| 5 | American Airlines | 3768 |
| 6 | Southwest Airlines | 3558 |
| 7 | Delta Air Lines | 2942 |
| 8 | ENY | 2805 |
| 9 | LATAM Airlines | 2210 |
| 10 | AZU | 2138 |
| 11 | Vueling | 1956 |
| 12 | Lufthansa | 1874 |
| 13 | LXJ | 1814 |
| 14 | WIF | 1812 |
| 15 | easyJet | 1606 |
| 16 | Swiss International | 1538 |
| 17 | AXM | 1520 |
| 18 | EJU | 1467 |
| 19 | United Airlines | 1459 |
| 20 | QLK | 1448 |
| 21 | Alaska Airlines | 1386 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1282 |
| 24 | VIV | 1263 |
| 25 | WMT | 1260 |
| 26 | PGT | 1257 |
| 27 | Air France | 1253 |
| 28 | Wizz Air | 1211 |
| 29 | AEE | 1147 |
| 30 | JetBlue | 1147 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 191986 |
| 2 | 🇪🇸 ES | 14771 |
| 3 | 🇧🇷 BR | 13452 |
| 4 | 🇦🇺 AU | 12964 |
| 5 | 🇨🇦 CA | 12695 |
| 6 | 🇮🇹 IT | 12459 |
| 7 | 🇮🇳 IN | 12099 |
| 8 | 🇩🇪 DE | 11325 |
| 9 | 🇬🇧 GB | 10830 |
| 10 | 🇨🇴 CO | 9515 |
| 11 | 🇯🇵 JP | 9314 |
| 12 | 🇫🇷 FR | 9215 |
| 13 | 🇹🇷 TR | 6786 |
| 14 | 🇬🇷 GR | 6767 |
| 15 | 🇲🇽 MX | 6400 |
| 16 | 🇨🇭 CH | 6115 |
| 17 | 🇳🇴 NO | 5655 |
| 18 | 🇲🇾 MY | 4063 |
| 19 | 🇿🇦 ZA | 4015 |
| 20 | 🇹🇭 TH | 3997 |
| 21 | 🇵🇱 PL | 3826 |
| 22 | 🇳🇿 NZ | 3171 |
| 23 | 🇵🇭 PH | 3144 |
| 24 | 🇬🇹 GT | 2892 |
| 25 | 🇰🇷 KR | 2706 |
| 26 | 🇭🇷 HR | 2634 |
| 27 | 🇲🇦 MA | 2334 |
| 28 | 🇲🇪 ME | 2106 |
| 29 | 🇳🇱 NL | 2059 |
| 30 | 🇮🇩 ID | 1978 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4803 |
| 2 | Denver International Airport |  | US | 3742 |
| 3 | Indira Gandhi International Airport |  | IN | 2799 |
| 4 | Tokyo International Airport |  | JP | 2781 |
| 5 | Guaymaral Airport |  | CO | 2653 |
| 6 | Harry Reid International Airport |  | US | 2484 |
| 7 | Zurich Airport |  | CH | 2402 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2352 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2318 |
| 10 | La Aurora Airport |  | GT | 2203 |
| 11 | El Dorado International Airport |  | CO | 2114 |
| 12 | Chicago O'Hare International Airport |  | US | 2084 |
| 13 | Salt Lake City International Airport |  | US | 2025 |
| 14 | Congonhas Airport |  | BR | 1963 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1947 |
| 16 | Frankfurt am Main International Airport |  | DE | 1842 |
| 17 | Madrid Barajas International Airport |  | ES | 1806 |
| 18 | Capua Airport |  | IT | 1806 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1723 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1710 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1653 |
| 22 | Malpensa International Airport |  | IT | 1643 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Charles de Gaulle International Airport |  | FR | 1598 |
| 25 | Macau International Airport |  | MO | 1597 |
| 26 | Ninoy Aquino International Airport |  | PH | 1509 |
| 27 | Charlotte/Douglas International Airport |  | US | 1503 |
| 28 | Kuala Lumpur International Airport |  | MY | 1472 |
| 29 | Barcelona International Airport |  | ES | 1440 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1397 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1378 |
| 32 | Viracopos International Airport |  | BR | 1368 |
| 33 | Bengaluru International Airport |  | IN | 1358 |
| 34 | Seattle-Tacoma International Airport |  | US | 1355 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1349 |
| 36 | Don Mueang International Airport |  | TH | 1307 |
| 37 | Calgary International Airport |  | CA | 1305 |
| 38 | Oslo Gardermoen Airport |  | NO | 1282 |
| 39 | Vitoria/Foronda Airport |  | ES | 1251 |
| 40 | O. R. Tambo International Airport |  | ZA | 1250 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 835 | 21m | 244 km | 3,516.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 575 | 1h 6m | 770 km | 7,638.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 559 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 515 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 380 | 27m | 275 km | 1,800.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 353 | 1h 50m | 1,423 km | 8,663.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 334 | 44m | 241 km | 1,387.4 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 325 | 21m | 250 km | 1,403.8 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 310 | 44m | 555 km | 2,968.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 306 | 22m | 55 km | 290.8 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 298 | 24m | 218 km | 1,122.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 296 | 1h 38m | 1,156 km | 5,905.1 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 280 | 27m | 215 km | 1,037.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 269 | 1h 14m | 961 km | 4,458.8 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 268 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 264 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 262 | 19m | 144 km | 651.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 242 | 28m | 152 km | 632.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N135CK |  | Cross Keys Airport (K17N) | Cross Keys Airport (K17N) | 2026-08-23 20:06 UTC | 2026-08-23 20:18 UTC | 12m |
| PSAAV | PSA | Nashville International Airport (KBNA) | Vancouver International Airport (CYVR) | 2026-08-23 15:55 UTC | 2026-08-23 20:16 UTC | 4h 20m |
| TRP7 | TRP | 5MD8 (5MD8) | Joint Base Andrews Airport (KADW) | 2026-08-23 20:04 UTC | 2026-08-23 20:16 UTC | 11m |
| N149TH |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-23 19:50 UTC | 2026-08-23 20:14 UTC | 23m |
| CXK569 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-08-23 19:04 UTC | 2026-08-23 20:11 UTC | 1h 7m |
| N46355 |  | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-08-23 19:48 UTC | 2026-08-23 20:06 UTC | 17m |
| VACA22 | VAC | San Antonio International Airport (KSAT) | Squirrel Creek Ranch Airport (4TE9) | 2026-08-23 19:32 UTC | 2026-08-23 20:04 UTC | 31m |
| N9421F |  | Pennridge Airport (KCKZ) | Pennridge Airport (KCKZ) | 2026-08-23 19:45 UTC | 2026-08-23 20:04 UTC | 19m |
| N469TS |  | Orange County Airport (KOMH) | Orange County Airport (KOMH) | 2026-08-23 19:43 UTC | 2026-08-23 20:02 UTC | 18m |
| N95420 |  | PA68 (PA68) | Lancaster Airport (KLNS) | 2026-08-23 19:13 UTC | 2026-08-23 20:00 UTC | 47m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-23 19:21 UTC | 2026-08-23 19:56 UTC | 35m |
| RAIDR08 | RAI | Yucca Valley Airport (KL22) | Citabriair Airport (UT43) | 2026-08-23 19:03 UTC | 2026-08-23 19:56 UTC | 52m |
| N54FA |  | Wings Field (KLOM) | Lancaster Airport (KLNS) | 2026-08-23 19:28 UTC | 2026-08-23 19:55 UTC | 27m |
| N750BB |  | Louis Armstrong New Orleans International Airport (KMSY) | Marksville Municipal Airport (KMKV) | 2026-08-23 19:24 UTC | 2026-08-23 19:55 UTC | 30m |
| N330XT |  | Caldwell Executive Airport (KEUL) | Sunrise Skypark Airport (ID40) | 2026-08-23 19:42 UTC | 2026-08-23 19:53 UTC | 11m |
| N20BQ |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-08-23 19:42 UTC | 2026-08-23 19:53 UTC | 11m |
| CGEFK | CGE | Edmonton / Villeneuve Airport (CZVL) | Edmonton / Villeneuve (Rose Field) (CRF3) | 2026-08-23 19:47 UTC | 2026-08-23 19:53 UTC | 5m |
| N780JH |  | Monett Regional Airport (KHFJ) | Logan-Cache Airport (KLGU) | 2026-08-23 17:32 UTC | 2026-08-23 19:50 UTC | 2h 18m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-23 19:27 UTC | 2026-08-23 19:49 UTC | 21m |
| EJA962 | EJA | Salt Lake City International Airport (KSLC) | San Francisco International Airport (KSFO) | 2026-08-23 18:03 UTC | 2026-08-23 19:49 UTC | 1h 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
