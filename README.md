# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_20:31:18_UTC-green)

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

**Latest saved flight:** 2026-08-18 20:31:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 20:31:18 UTC

- **213,404** saved flights
- **67,518** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **213,404** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,566,051.0 tonnes** estimated CO2 emissions
- **148,756,581 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8470 |
| 2 | SkyWest Airlines | 7656 |
| 3 | EJA | 4159 |
| 4 | IndiGo | 3643 |
| 5 | American Airlines | 3566 |
| 6 | Southwest Airlines | 3408 |
| 7 | Delta Air Lines | 2751 |
| 8 | ENY | 2649 |
| 9 | LATAM Airlines | 2009 |
| 10 | AZU | 1947 |
| 11 | Lufthansa | 1784 |
| 12 | Vueling | 1782 |
| 13 | WIF | 1712 |
| 14 | LXJ | 1683 |
| 15 | easyJet | 1480 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1391 |
| 18 | United Airlines | 1352 |
| 19 | QLK | 1320 |
| 20 | EJU | 1314 |
| 21 | Alaska Airlines | 1307 |
| 22 | All Nippon Airways | 1287 |
| 23 | VIV | 1176 |
| 24 | GLO | 1157 |
| 25 | PGT | 1154 |
| 26 | Air France | 1153 |
| 27 | WMT | 1101 |
| 28 | JetBlue | 1087 |
| 29 | AEE | 1079 |
| 30 | Wizz Air | 1068 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 180393 |
| 2 | 🇪🇸 ES | 13658 |
| 3 | 🇧🇷 BR | 12267 |
| 4 | 🇦🇺 AU | 11966 |
| 5 | 🇨🇦 CA | 11776 |
| 6 | 🇮🇳 IN | 11356 |
| 7 | 🇮🇹 IT | 11249 |
| 8 | 🇩🇪 DE | 10536 |
| 9 | 🇬🇧 GB | 9955 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8661 |
| 12 | 🇫🇷 FR | 8477 |
| 13 | 🇬🇷 GR | 6256 |
| 14 | 🇹🇷 TR | 6123 |
| 15 | 🇲🇽 MX | 5980 |
| 16 | 🇨🇭 CH | 5654 |
| 17 | 🇳🇴 NO | 5310 |
| 18 | 🇲🇾 MY | 3676 |
| 19 | 🇿🇦 ZA | 3606 |
| 20 | 🇵🇱 PL | 3521 |
| 21 | 🇹🇭 TH | 3450 |
| 22 | 🇳🇿 NZ | 2947 |
| 23 | 🇵🇭 PH | 2829 |
| 24 | 🇬🇹 GT | 2724 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2325 |
| 27 | 🇲🇦 MA | 2151 |
| 28 | 🇳🇱 NL | 1902 |
| 29 | 🇲🇪 ME | 1846 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4490 |
| 2 | Denver International Airport |  | US | 3487 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2592 |
| 5 | Guaymaral Airport |  | CO | 2557 |
| 6 | Harry Reid International Airport |  | US | 2384 |
| 7 | Zurich Airport |  | CH | 2223 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2200 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2199 |
| 10 | La Aurora Airport |  | GT | 2071 |
| 11 | El Dorado International Airport |  | CO | 1972 |
| 12 | Chicago O'Hare International Airport |  | US | 1972 |
| 13 | Salt Lake City International Airport |  | US | 1889 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1885 |
| 15 | Congonhas Airport |  | BR | 1786 |
| 16 | Frankfurt am Main International Airport |  | DE | 1739 |
| 17 | Madrid Barajas International Airport |  | ES | 1667 |
| 18 | Capua Airport |  | IT | 1615 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1611 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1602 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1561 |
| 22 | Macau International Airport |  | MO | 1554 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1490 |
| 24 | Malpensa International Airport |  | IT | 1487 |
| 25 | Charles de Gaulle International Airport |  | FR | 1471 |
| 26 | Charlotte/Douglas International Airport |  | US | 1438 |
| 27 | Kuala Lumpur International Airport |  | MY | 1357 |
| 28 | Ninoy Aquino International Airport |  | PH | 1341 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1314 |
| 30 | Bengaluru International Airport |  | IN | 1304 |
| 31 | Barcelona International Airport |  | ES | 1294 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1283 |
| 33 | Seattle-Tacoma International Airport |  | US | 1264 |
| 34 | Viracopos International Airport |  | BR | 1245 |
| 35 | Calgary International Airport |  | CA | 1205 |
| 36 | Oslo Gardermoen Airport |  | NO | 1182 |
| 37 | Vitoria/Foronda Airport |  | ES | 1176 |
| 38 | Reno/Tahoe International Airport |  | US | 1159 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1151 |
| 40 | Don Mueang International Airport |  | TH | 1138 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1046 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 759 | 21m | 244 km | 3,195.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 481 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 453 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 353 | 27m | 275 km | 1,672.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 314 | 1h 49m | 1,423 km | 7,706.1 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 312 | 44m | 241 km | 1,296.0 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 281 | 21m | 250 km | 1,213.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 265 | 19m | 99 km | 453.9 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 264 | 1h 38m | 1,156 km | 5,266.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 261 | 27m | 215 km | 966.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 252 | 1h 14m | 961 km | 4,177.0 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 251 | 19m | 165 km | 714.0 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 250 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 244 | 31m | 369 km | 1,553.1 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 240 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 229 | 1h 49m | 1,304 km | 5,151.9 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N41369 |  | Van Nuys Airport (KVNY) | San Bernardino International Airport (KSBD) | 2026-08-18 19:44 UTC | 2026-08-18 20:31 UTC | 46m |
| N130MT |  | Springfield Robertson County Airport (KM91) | Foreman Field (9TN4) | 2026-08-18 20:03 UTC | 2026-08-18 20:30 UTC | 27m |
| N4846G |  | Fort Meade Executive Airport (KFME) | Fort Meade Executive Airport (KFME) | 2026-08-18 19:35 UTC | 2026-08-18 20:28 UTC | 53m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-18 20:02 UTC | 2026-08-18 20:28 UTC | 26m |
| N6492H |  | Merrill Field (PAMR) | Beluga Airport (PABG) | 2026-08-18 19:55 UTC | 2026-08-18 20:25 UTC | 30m |
| GFY1124 | GFY | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-08-18 19:34 UTC | 2026-08-18 20:24 UTC | 49m |
| RMRNR53 | RMR | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-18 20:07 UTC | 2026-08-18 20:23 UTC | 16m |
| AAL2359 | American Airlines | Denver International Airport (KDEN) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-18 18:51 UTC | 2026-08-18 20:20 UTC | 1h 29m |
| 6407R |  | Yates Airport (IL29) | 89LL (89LL) | 2026-08-18 19:43 UTC | 2026-08-18 20:17 UTC | 33m |
| N5331F |  | Somerset Airport (KSMQ) | Somerset Airport (KSMQ) | 2026-08-18 19:51 UTC | 2026-08-18 20:15 UTC | 24m |
| CFR93 | CFR | Mc Clellan Airfield (KMCC) | Mc Clellan Airfield (KMCC) | 2026-08-18 20:00 UTC | 2026-08-18 20:14 UTC | 14m |
| LOST96 | LOS | Los Alamitos Army Air Field (KSLI) | Holiday Ranch Airport (27CA) | 2026-08-18 19:22 UTC | 2026-08-18 20:11 UTC | 48m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-18 19:59 UTC | 2026-08-18 20:10 UTC | 10m |
| N23SY |  | King's Airport (9OR4) | 33CA (33CA) | 2026-08-18 17:38 UTC | 2026-08-18 20:09 UTC | 2h 31m |
| N4279S |  | Kenosha Regional Airport (KENW) | Kenosha Regional Airport (KENW) | 2026-08-18 20:09 UTC | 2026-08-18 20:09 UTC | 0m |
| N62494 |  | Kinzua Airport (OR89) | Shaniko Cattle Airport (OG54) | 2026-08-18 19:39 UTC | 2026-08-18 20:08 UTC | 29m |
| MNL45 | MNL | Truckee-Tahoe Airport (KTRK) | Nervino Airport (KO02) | 2026-08-18 19:15 UTC | 2026-08-18 20:06 UTC | 50m |
| ETD3JC | Etihad Airways | Kuala Lumpur International Airport (WMKK) | OM11 (OM11) | 2026-08-18 14:10 UTC | 2026-08-18 20:04 UTC | 5h 53m |
| N9758H |  | Solberg/Hunterdon Airport (KN51) | Lancaster Airport (KLNS) | 2026-08-18 19:14 UTC | 2026-08-18 20:02 UTC | 48m |
| N711HA |  | Scottsdale Airport (KSDL) | Cascade Airport (KU70) | 2026-08-18 18:22 UTC | 2026-08-18 19:59 UTC | 1h 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
