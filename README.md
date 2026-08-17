# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_17:38:53_UTC-green)

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

**Latest saved flight:** 2026-08-17 17:38:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 17:38:53 UTC

- **209,320** saved flights
- **66,691** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **209,320** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,517,232.5 tonnes** estimated CO2 emissions
- **145,926,522 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8290 |
| 2 | SkyWest Airlines | 7510 |
| 3 | EJA | 4070 |
| 4 | IndiGo | 3575 |
| 5 | American Airlines | 3497 |
| 6 | Southwest Airlines | 3367 |
| 7 | Delta Air Lines | 2706 |
| 8 | ENY | 2607 |
| 9 | LATAM Airlines | 1974 |
| 10 | AZU | 1892 |
| 11 | Lufthansa | 1766 |
| 12 | Vueling | 1742 |
| 13 | WIF | 1686 |
| 14 | LXJ | 1651 |
| 15 | easyJet | 1451 |
| 16 | Swiss International | 1399 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1323 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1288 |
| 21 | EJU | 1279 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1149 |
| 24 | GLO | 1131 |
| 25 | Air France | 1130 |
| 26 | PGT | 1121 |
| 27 | JetBlue | 1070 |
| 28 | AEE | 1067 |
| 29 | WMT | 1059 |
| 30 | Wizz Air | 1037 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 177315 |
| 2 | 🇪🇸 ES | 13401 |
| 3 | 🇧🇷 BR | 12005 |
| 4 | 🇦🇺 AU | 11751 |
| 5 | 🇨🇦 CA | 11543 |
| 6 | 🇮🇳 IN | 11153 |
| 7 | 🇮🇹 IT | 10948 |
| 8 | 🇩🇪 DE | 10352 |
| 9 | 🇬🇧 GB | 9779 |
| 10 | 🇯🇵 JP | 8645 |
| 11 | 🇨🇴 CO | 8338 |
| 12 | 🇫🇷 FR | 8323 |
| 13 | 🇬🇷 GR | 6162 |
| 14 | 🇹🇷 TR | 5957 |
| 15 | 🇲🇽 MX | 5874 |
| 16 | 🇨🇭 CH | 5574 |
| 17 | 🇳🇴 NO | 5227 |
| 18 | 🇲🇾 MY | 3594 |
| 19 | 🇿🇦 ZA | 3516 |
| 20 | 🇵🇱 PL | 3460 |
| 21 | 🇹🇭 TH | 3353 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2776 |
| 24 | 🇬🇹 GT | 2690 |
| 25 | 🇰🇷 KR | 2545 |
| 26 | 🇭🇷 HR | 2251 |
| 27 | 🇲🇦 MA | 2114 |
| 28 | 🇳🇱 NL | 1870 |
| 29 | 🇲🇪 ME | 1778 |
| 30 | 🇮🇩 ID | 1725 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4393 |
| 2 | Denver International Airport |  | US | 3409 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2538 |
| 5 | Guaymaral Airport |  | CO | 2513 |
| 6 | Harry Reid International Airport |  | US | 2354 |
| 7 | Zurich Airport |  | CH | 2185 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2178 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2167 |
| 10 | La Aurora Airport |  | GT | 2045 |
| 11 | Chicago O'Hare International Airport |  | US | 1938 |
| 12 | El Dorado International Airport |  | CO | 1909 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1862 |
| 14 | Salt Lake City International Airport |  | US | 1849 |
| 15 | Congonhas Airport |  | BR | 1745 |
| 16 | Frankfurt am Main International Airport |  | DE | 1721 |
| 17 | Madrid Barajas International Airport |  | ES | 1640 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1591 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1586 |
| 20 | Capua Airport |  | IT | 1578 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1527 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1469 |
| 24 | Malpensa International Airport |  | IT | 1450 |
| 25 | Charles de Gaulle International Airport |  | FR | 1440 |
| 26 | Charlotte/Douglas International Airport |  | US | 1419 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1315 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1293 |
| 30 | Bengaluru International Airport |  | IN | 1289 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1267 |
| 32 | Barcelona International Airport |  | ES | 1254 |
| 33 | Seattle-Tacoma International Airport |  | US | 1242 |
| 34 | Viracopos International Airport |  | BR | 1213 |
| 35 | Calgary International Airport |  | CA | 1179 |
| 36 | Oslo Gardermoen Airport |  | NO | 1159 |
| 37 | Vitoria/Foronda Airport |  | ES | 1154 |
| 38 | Reno/Tahoe International Airport |  | US | 1145 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1131 |
| 40 | Don Mueang International Airport |  | TH | 1113 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1032 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 475 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 413 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 350 | 27m | 275 km | 1,658.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 346 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 307 | 1h 49m | 1,423 km | 7,534.3 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 306 | 44m | 241 km | 1,271.1 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 289 | 22m | 55 km | 274.7 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 257 | 27m | 215 km | 951.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 249 | 1h 37m | 1,156 km | 4,967.5 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 246 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 240 | 19m | 144 km | 597.0 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 239 | 31m | 369 km | 1,521.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 229 | 28m | 152 km | 598.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 224 | 1h 49m | 1,304 km | 5,039.4 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N61WA |  | Alpine County Airport (KM45) | Lake Tahoe Airport (KTVL) | 2026-08-17 16:27 UTC | 2026-08-17 17:38 UTC | 1h 11m |
| N358BG |  | Wood County Regional Airport (K1G0) | Wood County Regional Airport (K1G0) | 2026-08-17 16:16 UTC | 2026-08-17 17:37 UTC | 1h 20m |
| ARRIS36 | ARR | Boron Airstrip (57CL) | Boron Airstrip (57CL) | 2026-08-17 17:24 UTC | 2026-08-17 17:36 UTC | 12m |
| SHED42 | SHE | TA29 (TA29) | Canyon Ranch Airport (TE37) | 2026-08-17 17:21 UTC | 2026-08-17 17:35 UTC | 13m |
| N6409D |  | Montgomery-Gibbs Executive Airport (KMYF) | John Wayne/Orange County Airport (KSNA) | 2026-08-17 16:50 UTC | 2026-08-17 17:35 UTC | 44m |
| N734M |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-08-17 17:22 UTC | 2026-08-17 17:34 UTC | 12m |
| N1833L |  | Peters Airport (4NJ8) | Sky Manor Airport (KN40) | 2026-08-17 17:14 UTC | 2026-08-17 17:28 UTC | 14m |
| CO35 |  | Leme Airport (SDLL) | Pirassununga Airport (SDPY) | 2026-08-17 17:08 UTC | 2026-08-17 17:27 UTC | 18m |
| N721JD |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-08-17 16:51 UTC | 2026-08-17 17:26 UTC | 34m |
| CXK1077 | CXK | Ogden-Hinckley Airport (KOGD) | Provo Municipal Airport (KPVU) | 2026-08-17 16:52 UTC | 2026-08-17 17:25 UTC | 33m |
| N79KJ |  | Citabriair Airport (UT43) | NV54 (NV54) | 2026-08-17 16:20 UTC | 2026-08-17 17:24 UTC | 1h 4m |
| N3096T |  | Yuba County Airport (KMYV) | Lake Tahoe Airport (KTVL) | 2026-08-17 16:53 UTC | 2026-08-17 17:22 UTC | 28m |
| CXK475 | CXK | Santa Barbara Municipal Airport (KSBA) | Riverside Airport (KRAL) | 2026-08-17 16:07 UTC | 2026-08-17 17:20 UTC | 1h 13m |
| FIN519 | Finnair | Helsinki Vantaa Airport (EFHK) | Ranua Airport (EFRU) | 2026-08-17 15:59 UTC | 2026-08-17 17:18 UTC | 1h 18m |
| ARRIS36 | ARR | Edwards Af Aux North Base Airport (K9L2) | Boron Airstrip (57CL) | 2026-08-17 16:37 UTC | 2026-08-17 17:13 UTC | 36m |
| N245FR |  | 95CA (95CA) | 95CA (95CA) | 2026-08-17 16:38 UTC | 2026-08-17 17:12 UTC | 34m |
| LS19 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-17 15:53 UTC | 2026-08-17 17:10 UTC | 1h 16m |
| N6279V |  | 5VA9 (5VA9) | 5VA9 (5VA9) | 2026-08-17 15:46 UTC | 2026-08-17 17:10 UTC | 1h 23m |
| EJA494 | EJA | Telluride Regional Airport (KTEX) | Durango-La Plata County Airport (KDRO) | 2026-08-17 16:54 UTC | 2026-08-17 17:08 UTC | 14m |
| N104PF |  | Lewis University Airport (KLOT) | Vogen Airport (IS41) | 2026-08-17 16:44 UTC | 2026-08-17 17:08 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
