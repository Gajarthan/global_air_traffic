# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_17:29:27_UTC-green)

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

**Latest saved flight:** 2026-08-24 17:29:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 17:29:27 UTC

- **232,666** saved flights
- **71,522** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **232,666** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,803,910.6 tonnes** estimated CO2 emissions
- **162,545,544 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9339 |
| 2 | SkyWest Airlines | 8228 |
| 3 | EJA | 4502 |
| 4 | IndiGo | 3938 |
| 5 | American Airlines | 3793 |
| 6 | Southwest Airlines | 3580 |
| 7 | Delta Air Lines | 2970 |
| 8 | ENY | 2830 |
| 9 | LATAM Airlines | 2238 |
| 10 | AZU | 2163 |
| 11 | Vueling | 1989 |
| 12 | Lufthansa | 1898 |
| 13 | WIF | 1850 |
| 14 | LXJ | 1831 |
| 15 | easyJet | 1630 |
| 16 | Swiss International | 1559 |
| 17 | AXM | 1551 |
| 18 | EJU | 1489 |
| 19 | United Airlines | 1476 |
| 20 | QLK | 1474 |
| 21 | Alaska Airlines | 1397 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1296 |
| 24 | WMT | 1292 |
| 25 | VIV | 1276 |
| 26 | PGT | 1270 |
| 27 | Air France | 1266 |
| 28 | Wizz Air | 1229 |
| 29 | AEE | 1159 |
| 30 | JetBlue | 1156 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 193657 |
| 2 | 🇪🇸 ES | 14938 |
| 3 | 🇧🇷 BR | 13588 |
| 4 | 🇦🇺 AU | 13162 |
| 5 | 🇨🇦 CA | 12800 |
| 6 | 🇮🇹 IT | 12662 |
| 7 | 🇮🇳 IN | 12273 |
| 8 | 🇩🇪 DE | 11470 |
| 9 | 🇬🇧 GB | 10976 |
| 10 | 🇨🇴 CO | 9710 |
| 11 | 🇯🇵 JP | 9448 |
| 12 | 🇫🇷 FR | 9320 |
| 13 | 🇹🇷 TR | 6884 |
| 14 | 🇬🇷 GR | 6851 |
| 15 | 🇲🇽 MX | 6458 |
| 16 | 🇨🇭 CH | 6208 |
| 17 | 🇳🇴 NO | 5759 |
| 18 | 🇲🇾 MY | 4143 |
| 19 | 🇹🇭 TH | 4108 |
| 20 | 🇿🇦 ZA | 4069 |
| 21 | 🇵🇱 PL | 3877 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3184 |
| 24 | 🇬🇹 GT | 2922 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2679 |
| 27 | 🇲🇦 MA | 2363 |
| 28 | 🇲🇪 ME | 2146 |
| 29 | 🇳🇱 NL | 2085 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4835 |
| 2 | Denver International Airport |  | US | 3775 |
| 3 | Indira Gandhi International Airport |  | IN | 2839 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2669 |
| 6 | Harry Reid International Airport |  | US | 2498 |
| 7 | Zurich Airport |  | CH | 2430 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2375 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2339 |
| 10 | La Aurora Airport |  | GT | 2225 |
| 11 | El Dorado International Airport |  | CO | 2163 |
| 12 | Chicago O'Hare International Airport |  | US | 2100 |
| 13 | Salt Lake City International Airport |  | US | 2045 |
| 14 | Congonhas Airport |  | BR | 1982 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1962 |
| 16 | Frankfurt am Main International Airport |  | DE | 1858 |
| 17 | Capua Airport |  | IT | 1830 |
| 18 | Madrid Barajas International Airport |  | ES | 1828 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1751 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1724 |
| 21 | Malpensa International Airport |  | IT | 1669 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1662 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1619 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1533 |
| 27 | Charlotte/Douglas International Airport |  | US | 1509 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1470 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1415 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1405 |
| 32 | Viracopos International Airport |  | BR | 1384 |
| 33 | Bengaluru International Airport |  | IN | 1372 |
| 34 | Seattle-Tacoma International Airport |  | US | 1364 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1363 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1318 |
| 38 | Oslo Gardermoen Airport |  | NO | 1305 |
| 39 | O. R. Tambo International Airport |  | ZA | 1264 |
| 40 | Vitoria/Foronda Airport |  | ES | 1260 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1083 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 847 | 21m | 244 km | 3,566.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 574 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 520 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 384 | 27m | 275 km | 1,819.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 359 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 359 | 1h 50m | 1,423 km | 8,810.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 338 | 44m | 241 km | 1,404.0 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 308 | 24m | 218 km | 1,160.4 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 304 | 1h 38m | 1,156 km | 6,064.7 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 289 | 19m | 99 km | 495.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 285 | 27m | 215 km | 1,055.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 269 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 265 | 19m | 144 km | 659.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 251 | 15m | 154 km | 665.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 248 | 1h 50m | 1,304 km | 5,579.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GRIM61 | GRI | Four Square Ranch Airport (3TA0) | Four Square Ranch Airport (3TA0) | 2026-08-24 17:12 UTC | 2026-08-24 17:29 UTC | 16m |
| GRIM62 | GRI | Pilots Landing Airport (81TE) | TA29 (TA29) | 2026-08-24 17:09 UTC | 2026-08-24 17:29 UTC | 19m |
| OKAUI73 | OKA | Kazimierz Biskup Airport (EPKB) | Kazimierz Biskup Airport (EPKB) | 2026-08-24 17:09 UTC | 2026-08-24 17:23 UTC | 14m |
| DESERT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-24 17:09 UTC | 2026-08-24 17:23 UTC | 14m |
| N581TG |  | Jacksonville Executive At Craig Airport (KCRG) | Jacksonville Executive At Craig Airport (KCRG) | 2026-08-24 16:27 UTC | 2026-08-24 17:15 UTC | 48m |
| SJN7 | SJN | 1WA9 (1WA9) | Orcas Island Airport (KORS) | 2026-08-24 16:55 UTC | 2026-08-24 17:15 UTC | 20m |
| N2459W |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-24 16:06 UTC | 2026-08-24 17:15 UTC | 1h 9m |
| N680BF |  | Vero Beach Regional Airport (KVRB) | Northeast Philadelphia Airport (KPNE) | 2026-08-24 15:15 UTC | 2026-08-24 17:14 UTC | 1h 59m |
| CGLII | CGL | Tofield Airport (CEV7) | Tofield Airport (CEV7) | 2026-08-24 17:09 UTC | 2026-08-24 17:10 UTC | 1m |
| LOST77 | LOS | Los Alamitos Army Air Field (KSLI) | Apple Valley Airport (KAPV) | 2026-08-24 16:42 UTC | 2026-08-24 17:09 UTC | 27m |
| N911RR |  | Miami Homestead General Aviation Airport (KX51) | Miami Executive Airport (KTMB) | 2026-08-24 16:55 UTC | 2026-08-24 17:09 UTC | 13m |
| N65DJ |  | Linden Airport (KLDJ) | Newark Liberty International Airport (KEWR) | 2026-08-24 13:45 UTC | 2026-08-24 17:06 UTC | 3h 20m |
| FFAB123 | FFA | Mayport Ns (Adm David L Mcdonald Field) Airport (KNRB) | Whitehouse Nolf Airport (KNEN) | 2026-08-24 16:39 UTC | 2026-08-24 17:02 UTC | 23m |
| N527JG |  | Greenville Spartanburg International Airport (KGSP) | Toronto Pearson International Airport (CYYZ) | 2026-08-24 15:26 UTC | 2026-08-24 17:02 UTC | 1h 35m |
| N65JA |  | Aurora Municipal Airport (KARR) | Walnut Creek Airport (49IL) | 2026-08-24 16:32 UTC | 2026-08-24 17:01 UTC | 28m |
| N127XY |  | Skypark Airport (KBTF) | Preston Airport (KU10) | 2026-08-24 15:54 UTC | 2026-08-24 16:59 UTC | 1h 5m |
| N107MY |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-08-24 16:05 UTC | 2026-08-24 16:58 UTC | 52m |
| DRAG971 | DRA | Martinique Aime Cesaire International Airport (TFFF) | Martinique Aime Cesaire International Airport (TFFF) | 2026-08-24 16:56 UTC | 2026-08-24 16:57 UTC | 0m |
| N98EG |  | Linden Airport (KLDJ) | Newark Liberty International Airport (KEWR) | 2026-08-24 13:45 UTC | 2026-08-24 16:56 UTC | 3h 11m |
| MANLY51 | MAN | Enix Airport (OK51) | Sopwith Ldg Airport (OK56) | 2026-08-24 16:43 UTC | 2026-08-24 16:54 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
