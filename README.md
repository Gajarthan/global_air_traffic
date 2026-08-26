# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_12:59:29_UTC-green)

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

**Latest saved flight:** 2026-08-26 12:59:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 12:59:29 UTC

- **238,458** saved flights
- **72,593** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **238,458** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,874,040.5 tonnes** estimated CO2 emissions
- **166,611,041 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9580 |
| 2 | SkyWest Airlines | 8391 |
| 3 | EJA | 4617 |
| 4 | IndiGo | 4021 |
| 5 | American Airlines | 3855 |
| 6 | Southwest Airlines | 3614 |
| 7 | Delta Air Lines | 3036 |
| 8 | ENY | 2881 |
| 9 | LATAM Airlines | 2289 |
| 10 | AZU | 2219 |
| 11 | Vueling | 2055 |
| 12 | Lufthansa | 1933 |
| 13 | WIF | 1893 |
| 14 | LXJ | 1852 |
| 15 | easyJet | 1665 |
| 16 | Swiss International | 1606 |
| 17 | AXM | 1591 |
| 18 | EJU | 1531 |
| 19 | QLK | 1527 |
| 20 | United Airlines | 1505 |
| 21 | Alaska Airlines | 1430 |
| 22 | All Nippon Airways | 1422 |
| 23 | WMT | 1337 |
| 24 | GLO | 1331 |
| 25 | VIV | 1312 |
| 26 | PGT | 1303 |
| 27 | Air France | 1301 |
| 28 | Wizz Air | 1278 |
| 29 | AEE | 1183 |
| 30 | JetBlue | 1181 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 197520 |
| 2 | 🇪🇸 ES | 15346 |
| 3 | 🇧🇷 BR | 13907 |
| 4 | 🇦🇺 AU | 13569 |
| 5 | 🇨🇦 CA | 13181 |
| 6 | 🇮🇹 IT | 13042 |
| 7 | 🇮🇳 IN | 12534 |
| 8 | 🇩🇪 DE | 11791 |
| 9 | 🇬🇧 GB | 11265 |
| 10 | 🇨🇴 CO | 10142 |
| 11 | 🇯🇵 JP | 9652 |
| 12 | 🇫🇷 FR | 9608 |
| 13 | 🇹🇷 TR | 7089 |
| 14 | 🇬🇷 GR | 7031 |
| 15 | 🇲🇽 MX | 6603 |
| 16 | 🇨🇭 CH | 6400 |
| 17 | 🇳🇴 NO | 5906 |
| 18 | 🇹🇭 TH | 4322 |
| 19 | 🇲🇾 MY | 4263 |
| 20 | 🇿🇦 ZA | 4189 |
| 21 | 🇵🇱 PL | 3972 |
| 22 | 🇳🇿 NZ | 3291 |
| 23 | 🇵🇭 PH | 3289 |
| 24 | 🇬🇹 GT | 2980 |
| 25 | 🇰🇷 KR | 2842 |
| 26 | 🇭🇷 HR | 2760 |
| 27 | 🇲🇦 MA | 2409 |
| 28 | 🇲🇪 ME | 2226 |
| 29 | 🇳🇱 NL | 2159 |
| 30 | 🇮🇩 ID | 2099 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4936 |
| 2 | Denver International Airport |  | US | 3851 |
| 3 | Indira Gandhi International Airport |  | IN | 2916 |
| 4 | Tokyo International Airport |  | JP | 2873 |
| 5 | Guaymaral Airport |  | CO | 2691 |
| 6 | Harry Reid International Airport |  | US | 2540 |
| 7 | Zurich Airport |  | CH | 2503 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2437 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2384 |
| 10 | El Dorado International Airport |  | CO | 2284 |
| 11 | La Aurora Airport |  | GT | 2271 |
| 12 | Chicago O'Hare International Airport |  | US | 2132 |
| 13 | Salt Lake City International Airport |  | US | 2095 |
| 14 | Congonhas Airport |  | BR | 2028 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1987 |
| 16 | Frankfurt am Main International Airport |  | DE | 1895 |
| 17 | Capua Airport |  | IT | 1876 |
| 18 | Madrid Barajas International Airport |  | ES | 1873 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1796 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1755 |
| 21 | Malpensa International Airport |  | IT | 1712 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1683 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1680 |
| 24 | Charles de Gaulle International Airport |  | FR | 1665 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1594 |
| 27 | Kuala Lumpur International Airport |  | MY | 1540 |
| 28 | Charlotte/Douglas International Airport |  | US | 1529 |
| 29 | Barcelona International Airport |  | ES | 1520 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1494 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1442 |
| 32 | Viracopos International Airport |  | BR | 1421 |
| 33 | Don Mueang International Airport |  | TH | 1398 |
| 34 | Bengaluru International Airport |  | IN | 1396 |
| 35 | Seattle-Tacoma International Airport |  | US | 1392 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1390 |
| 37 | Calgary International Airport |  | CA | 1367 |
| 38 | Oslo Gardermoen Airport |  | NO | 1342 |
| 39 | O. R. Tambo International Airport |  | ZA | 1305 |
| 40 | Vancouver International Airport |  | CA | 1303 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1090 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 877 | 21m | 244 km | 3,692.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 609 | 24m | 225 km | 2,362.6 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 607 | 1h 6m | 770 km | 8,063.5 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 604 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 533 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 394 | 27m | 275 km | 1,867.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 372 | 1h 50m | 1,423 km | 9,129.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 364 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 360 | 44m | 555 km | 3,447.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 345 | 44m | 241 km | 1,433.1 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 340 | 21m | 250 km | 1,468.6 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 323 | 24m | 218 km | 1,216.9 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 318 | 22m | 55 km | 302.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 317 | 1h 40m | 1,156 km | 6,324.0 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 296 | 19m | 99 km | 507.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 292 | 27m | 215 km | 1,081.4 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 277 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 270 | 19m | 144 km | 671.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 255 | 1h 50m | 1,304 km | 5,736.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 247 | 28m | 152 km | 645.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CAL187 | CAL | Gimhae International Airport (RKPK) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-26 11:12 UTC | 2026-08-26 12:59 UTC | 1h 47m |
| N390SF |  | 0OK0 (0OK0) | Chickasha Municipal Airport (KCHK) | 2026-08-26 12:29 UTC | 2026-08-26 12:47 UTC | 17m |
| N400DG |  | Colonel James Jabara Airport (KAAO) | Miller Airport (MO99) | 2026-08-26 12:09 UTC | 2026-08-26 12:44 UTC | 35m |
| LBQ651 | LBQ | New Century Aircenter Airport (KIXD) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-26 10:47 UTC | 2026-08-26 12:39 UTC | 1h 52m |
| N5343F |  | Easton/Newnam Field (KESN) | Ocean City Municipal Airport (KOXB) | 2026-08-26 12:03 UTC | 2026-08-26 12:38 UTC | 35m |
| TGGOR | TGG | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-26 12:24 UTC | 2026-08-26 12:38 UTC | 13m |
| CPA957 | Cathay Pacific | Guangzhou Baiyun International Airport (ZGGG) | Zhuhai Airport (ZGSD) | 2026-08-26 12:24 UTC | 2026-08-26 12:37 UTC | 12m |
| N610EB |  | Hopewell Airpark (90NY) | Hopewell Airpark (90NY) | 2026-08-26 12:32 UTC | 2026-08-26 12:36 UTC | 3m |
| N351SD |  | Mayer Airport (IN72) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-08-26 11:20 UTC | 2026-08-26 12:35 UTC | 1h 15m |
| N152DM |  | K55J (K55J) | K55J (K55J) | 2026-08-26 12:28 UTC | 2026-08-26 12:34 UTC | 6m |
| N54151 |  | Robertson Field (K4B8) | Robertson Field (K4B8) | 2026-08-26 12:27 UTC | 2026-08-26 12:34 UTC | 7m |
| CXK404 | CXK | Ogden-Hinckley Airport (KOGD) | Ogden-Hinckley Airport (KOGD) | 2026-08-26 12:29 UTC | 2026-08-26 12:33 UTC | 4m |
| N476TS |  | Mcgraw's Backyard Airport (5TN4) | Gatlinburg-Pigeon Forge Airport (KGKT) | 2026-08-26 12:16 UTC | 2026-08-26 12:31 UTC | 15m |
| N733LN |  | Fort Lauderdale Executive Airport (KFXE) | Duda Airstrip (FA69) | 2026-08-26 11:48 UTC | 2026-08-26 12:31 UTC | 42m |
| EWG9 | EWG | Dresden Airport (EDDC) | Dresden Airport (EDDC) | 2026-08-26 10:59 UTC | 2026-08-26 12:29 UTC | 1h 30m |
| HK4749 |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-26 12:16 UTC | 2026-08-26 12:27 UTC | 10m |
| N585M |  | Chippewa Valley Regional Airport (KEAU) | Des Moines International Airport (KDSM) | 2026-08-26 11:49 UTC | 2026-08-26 12:24 UTC | 34m |
| FNG8 | FNG | Kardla Airport (EEKA) | Kymi Airport (EFKY) | 2026-08-26 11:21 UTC | 2026-08-26 12:19 UTC | 58m |
| N546B |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-08-26 11:49 UTC | 2026-08-26 12:18 UTC | 29m |
| N323DB |  | 0MU8 (0MU8) | Sunburst Ranch Airport (MU48) | 2026-08-26 11:46 UTC | 2026-08-26 12:13 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
