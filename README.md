# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_19:47:47_UTC-green)

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

**Latest saved flight:** 2026-09-01 19:47:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-01 19:47:47 UTC

- **244,012** saved flights
- **73,890** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **244,012** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,939,184.2 tonnes** estimated CO2 emissions
- **170,387,490 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9798 |
| 2 | SkyWest Airlines | 8551 |
| 3 | EJA | 4714 |
| 4 | IndiGo | 4095 |
| 5 | American Airlines | 3926 |
| 6 | Southwest Airlines | 3660 |
| 7 | Delta Air Lines | 3108 |
| 8 | ENY | 2934 |
| 9 | LATAM Airlines | 2340 |
| 10 | AZU | 2267 |
| 11 | Vueling | 2092 |
| 12 | Lufthansa | 1956 |
| 13 | WIF | 1945 |
| 14 | LXJ | 1884 |
| 15 | easyJet | 1698 |
| 16 | Swiss International | 1646 |
| 17 | AXM | 1609 |
| 18 | EJU | 1570 |
| 19 | QLK | 1556 |
| 20 | United Airlines | 1537 |
| 21 | Alaska Airlines | 1456 |
| 22 | All Nippon Airways | 1438 |
| 23 | WMT | 1371 |
| 24 | GLO | 1365 |
| 25 | VIV | 1335 |
| 26 | Air France | 1333 |
| 27 | PGT | 1333 |
| 28 | Wizz Air | 1326 |
| 29 | AEE | 1207 |
| 30 | JetBlue | 1204 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 202141 |
| 2 | 🇪🇸 ES | 15685 |
| 3 | 🇧🇷 BR | 14223 |
| 4 | 🇦🇺 AU | 13832 |
| 5 | 🇨🇦 CA | 13575 |
| 6 | 🇮🇹 IT | 13373 |
| 7 | 🇮🇳 IN | 12757 |
| 8 | 🇩🇪 DE | 12037 |
| 9 | 🇬🇧 GB | 11524 |
| 10 | 🇨🇴 CO | 10551 |
| 11 | 🇫🇷 FR | 9850 |
| 12 | 🇯🇵 JP | 9735 |
| 13 | 🇹🇷 TR | 7260 |
| 14 | 🇬🇷 GR | 7208 |
| 15 | 🇲🇽 MX | 6724 |
| 16 | 🇨🇭 CH | 6565 |
| 17 | 🇳🇴 NO | 6049 |
| 18 | 🇹🇭 TH | 4409 |
| 19 | 🇲🇾 MY | 4317 |
| 20 | 🇿🇦 ZA | 4247 |
| 21 | 🇵🇱 PL | 4104 |
| 22 | 🇳🇿 NZ | 3347 |
| 23 | 🇵🇭 PH | 3340 |
| 24 | 🇬🇹 GT | 3068 |
| 25 | 🇰🇷 KR | 2866 |
| 26 | 🇭🇷 HR | 2813 |
| 27 | 🇲🇦 MA | 2468 |
| 28 | 🇲🇪 ME | 2282 |
| 29 | 🇳🇱 NL | 2211 |
| 30 | 🇮🇩 ID | 2126 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5031 |
| 2 | Denver International Airport |  | US | 3928 |
| 3 | Indira Gandhi International Airport |  | IN | 2974 |
| 4 | Tokyo International Airport |  | JP | 2900 |
| 5 | Guaymaral Airport |  | CO | 2710 |
| 6 | Harry Reid International Airport |  | US | 2596 |
| 7 | Zurich Airport |  | CH | 2565 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2489 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2435 |
| 10 | El Dorado International Airport |  | CO | 2398 |
| 11 | La Aurora Airport |  | GT | 2333 |
| 12 | Salt Lake City International Airport |  | US | 2161 |
| 13 | Chicago O'Hare International Airport |  | US | 2157 |
| 14 | Congonhas Airport |  | BR | 2084 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2022 |
| 16 | Frankfurt am Main International Airport |  | DE | 1927 |
| 17 | Capua Airport |  | IT | 1922 |
| 18 | Madrid Barajas International Airport |  | ES | 1920 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1832 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1796 |
| 21 | Malpensa International Airport |  | IT | 1746 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1720 |
| 23 | Charles de Gaulle International Airport |  | FR | 1715 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1708 |
| 25 | Ninoy Aquino International Airport |  | PH | 1625 |
| 26 | Macau International Airport |  | MO | 1624 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1566 |
| 28 | Charlotte/Douglas International Airport |  | US | 1557 |
| 29 | Kuala Lumpur International Airport |  | MY | 1555 |
| 30 | Barcelona International Airport |  | ES | 1547 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1476 |
| 32 | Viracopos International Airport |  | BR | 1448 |
| 33 | Seattle-Tacoma International Airport |  | US | 1428 |
| 34 | Don Mueang International Airport |  | TH | 1420 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1414 |
| 36 | Bengaluru International Airport |  | IN | 1412 |
| 37 | Calgary International Airport |  | CA | 1402 |
| 38 | Oslo Gardermoen Airport |  | NO | 1377 |
| 39 | Vancouver International Airport |  | CA | 1357 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1336 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1098 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 900 | 21m | 244 km | 3,789.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 631 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 621 | 24m | 225 km | 2,409.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 615 | 1h 6m | 770 km | 8,169.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 548 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 403 | 27m | 275 km | 1,909.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 385 | 1h 50m | 1,423 km | 9,448.5 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 373 | 44m | 555 km | 3,571.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 360 | 44m | 241 km | 1,495.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 347 | 21m | 250 km | 1,498.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 335 | 24m | 218 km | 1,262.1 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 326 | 1h 39m | 1,156 km | 6,503.6 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 324 | 22m | 55 km | 308.0 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 303 | 19m | 99 km | 519.0 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 297 | 26m | 215 km | 1,100.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 288 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 283 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 280 | 1h 14m | 961 km | 4,641.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 276 | 19m | 144 km | 686.5 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 262 | 1h 50m | 1,304 km | 5,894.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N88HX |  | Rancho San Simeon Airport (66CA) | Rancho San Simeon Airport (66CA) | 2026-09-01 19:13 UTC | 2026-09-01 19:47 UTC | 34m |
| RSQ118 | RSQ | Belmullet Aerodrome (EIBT) | Ireland West Knock Airport (EIKN) | 2026-09-01 19:33 UTC | 2026-09-01 19:47 UTC | 14m |
| N216CH |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-09-01 19:27 UTC | 2026-09-01 19:45 UTC | 18m |
| N777ZA |  | Essex County Airport (KCDW) | Somerset Airport (KSMQ) | 2026-09-01 19:32 UTC | 2026-09-01 19:43 UTC | 10m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-09-01 19:04 UTC | 2026-09-01 19:41 UTC | 36m |
| CGQPB | CGQ | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-09-01 19:19 UTC | 2026-09-01 19:40 UTC | 20m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-09-01 08:40 UTC | 2026-09-01 19:39 UTC | 10h 58m |
| N2441D |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-09-01 18:46 UTC | 2026-09-01 19:33 UTC | 46m |
| N7KP |  | Stiletto Airpark (XS79) | John B Connally Ranch Airport (8TA0) | 2026-09-01 19:19 UTC | 2026-09-01 19:29 UTC | 10m |
| SRD375 | SRD | RNAS Lee-On-Solent (EGHF) | Isle of Wight / Sandown Airport (EGHN) | 2026-09-01 19:07 UTC | 2026-09-01 19:29 UTC | 22m |
| CONGO64 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-09-01 19:03 UTC | 2026-09-01 19:25 UTC | 21m |
| GHA22 | GHA | Rocky Mountain Metro Airport (KBJC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-09-01 17:21 UTC | 2026-09-01 19:23 UTC | 2h 2m |
| N8573X |  | Lorain County Regional Airport (KLPR) | 70OH (70OH) | 2026-09-01 19:03 UTC | 2026-09-01 19:23 UTC | 20m |
| N26BQ |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-09-01 18:43 UTC | 2026-09-01 19:21 UTC | 38m |
| AWH91A | AWH | Hannover Airport (EDDV) | Kiel-Holtenau Airport (EDHK) | 2026-09-01 18:41 UTC | 2026-09-01 19:18 UTC | 36m |
| LYM3912 | LYM | Chicago O'Hare International Airport (KORD) | Manitowish Waters Airport (KD25) | 2026-09-01 18:27 UTC | 2026-09-01 19:14 UTC | 47m |
| EJA616 | EJA | Mc Ghee Tyson Airport (KTYS) | Monmouth Executive Airport (KBLM) | 2026-09-01 17:38 UTC | 2026-09-01 19:13 UTC | 1h 34m |
| RNGR822 | RNG | Waldron Field Nolf Airport (KNWL) | Mustang Beach Airport (KRAS) | 2026-09-01 18:32 UTC | 2026-09-01 19:12 UTC | 40m |
| N17VA |  | Bob Hope Airport (KBUR) | Sweetwater (Usmc) Airport (NV72) | 2026-09-01 17:56 UTC | 2026-09-01 19:12 UTC | 1h 16m |
| SRG199 | SRG | Glasgow International Airport (EGPF) | Glasgow International Airport (EGPF) | 2026-09-01 19:05 UTC | 2026-09-01 19:12 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
