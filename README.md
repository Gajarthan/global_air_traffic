# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_17:02:35_UTC-green)

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

**Latest saved flight:** 2026-08-19 17:02:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 17:02:35 UTC

- **216,445** saved flights
- **68,347** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **216,445** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,603,926.0 tonnes** estimated CO2 emissions
- **150,952,231 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8656 |
| 2 | SkyWest Airlines | 7725 |
| 3 | EJA | 4199 |
| 4 | IndiGo | 3686 |
| 5 | American Airlines | 3606 |
| 6 | Southwest Airlines | 3440 |
| 7 | Delta Air Lines | 2796 |
| 8 | ENY | 2670 |
| 9 | LATAM Airlines | 2048 |
| 10 | AZU | 1975 |
| 11 | Vueling | 1820 |
| 12 | Lufthansa | 1811 |
| 13 | WIF | 1732 |
| 14 | LXJ | 1702 |
| 15 | easyJet | 1502 |
| 16 | Swiss International | 1446 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1367 |
| 19 | EJU | 1350 |
| 20 | QLK | 1346 |
| 21 | Alaska Airlines | 1324 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1185 |
| 24 | PGT | 1175 |
| 25 | Air France | 1174 |
| 26 | GLO | 1174 |
| 27 | WMT | 1132 |
| 28 | JetBlue | 1102 |
| 29 | Wizz Air | 1100 |
| 30 | AEE | 1088 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 182317 |
| 2 | 🇪🇸 ES | 13895 |
| 3 | 🇧🇷 BR | 12455 |
| 4 | 🇦🇺 AU | 12169 |
| 5 | 🇨🇦 CA | 11910 |
| 6 | 🇮🇹 IT | 11481 |
| 7 | 🇮🇳 IN | 11480 |
| 8 | 🇩🇪 DE | 10737 |
| 9 | 🇬🇧 GB | 10167 |
| 10 | 🇯🇵 JP | 8870 |
| 11 | 🇨🇴 CO | 8848 |
| 12 | 🇫🇷 FR | 8647 |
| 13 | 🇬🇷 GR | 6333 |
| 14 | 🇹🇷 TR | 6221 |
| 15 | 🇲🇽 MX | 6045 |
| 16 | 🇨🇭 CH | 5760 |
| 17 | 🇳🇴 NO | 5386 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3681 |
| 20 | 🇵🇱 PL | 3583 |
| 21 | 🇹🇭 TH | 3539 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2898 |
| 24 | 🇬🇹 GT | 2749 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2372 |
| 27 | 🇲🇦 MA | 2179 |
| 28 | 🇳🇱 NL | 1935 |
| 29 | 🇲🇪 ME | 1886 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4537 |
| 2 | Denver International Airport |  | US | 3520 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2623 |
| 5 | Guaymaral Airport |  | CO | 2582 |
| 6 | Harry Reid International Airport |  | US | 2403 |
| 7 | Zurich Airport |  | CH | 2253 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2219 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2210 |
| 10 | La Aurora Airport |  | GT | 2090 |
| 11 | El Dorado International Airport |  | CO | 2019 |
| 12 | Chicago O'Hare International Airport |  | US | 1986 |
| 13 | Salt Lake City International Airport |  | US | 1903 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1891 |
| 15 | Congonhas Airport |  | BR | 1817 |
| 16 | Frankfurt am Main International Airport |  | DE | 1772 |
| 17 | Madrid Barajas International Airport |  | ES | 1696 |
| 18 | Capua Airport |  | IT | 1647 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1631 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1611 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1589 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Malpensa International Airport |  | IT | 1520 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 25 | Charles de Gaulle International Airport |  | FR | 1488 |
| 26 | Charlotte/Douglas International Airport |  | US | 1452 |
| 27 | Kuala Lumpur International Airport |  | MY | 1378 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1328 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1321 |
| 31 | Bengaluru International Airport |  | IN | 1315 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1290 |
| 33 | Seattle-Tacoma International Airport |  | US | 1282 |
| 34 | Viracopos International Airport |  | BR | 1261 |
| 35 | Calgary International Airport |  | CA | 1218 |
| 36 | Oslo Gardermoen Airport |  | NO | 1199 |
| 37 | Vitoria/Foronda Airport |  | ES | 1197 |
| 38 | Amsterdam Airport Schiphol |  | NL | 1171 |
| 39 | Enrique Olaya Herrera Airport |  | CO | 1170 |
| 40 | Don Mueang International Airport |  | TH | 1167 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1056 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 771 | 21m | 244 km | 3,246.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 487 | 13m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 471 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 361 | 27m | 275 km | 1,710.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 317 | 1h 49m | 1,423 km | 7,779.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 315 | 44m | 241 km | 1,308.4 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 271 | 19m | 99 km | 464.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 266 | 27m | 215 km | 985.2 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 256 | 1h 14m | 961 km | 4,243.3 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 255 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 253 | 31m | 369 km | 1,610.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 232 | 1h 49m | 1,304 km | 5,219.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FGURG | FGU | Voeltendorf Airport (LOAD) | Voeltendorf Airport (LOAD) | 2026-08-19 16:36 UTC | 2026-08-19 17:02 UTC | 26m |
| N504DD |  | 24WN (24WN) | Kirkpatrick Airport (8IL2) | 2026-08-19 16:35 UTC | 2026-08-19 16:59 UTC | 24m |
| N292SP |  | Ocean County Airport (KMJX) | Monmouth Executive Airport (KBLM) | 2026-08-19 16:37 UTC | 2026-08-19 16:53 UTC | 15m |
| N7874N |  | City Of Colorado Springs Municipal Airport (KCOS) | Limon Municipal Airport (KLIC) | 2026-08-19 15:58 UTC | 2026-08-19 16:46 UTC | 48m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-19 14:48 UTC | 2026-08-19 16:46 UTC | 1h 58m |
| N38316 |  | Tweed/New Haven Airport (KHVN) | Meriden Markham Municipal Airport (KMMK) | 2026-08-19 16:21 UTC | 2026-08-19 16:45 UTC | 24m |
| TCF653 | TCF | Duda Airstrip (FA69) | Palm Beach County Park Airport (KLNA) | 2026-08-19 16:17 UTC | 2026-08-19 16:44 UTC | 27m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-19 16:28 UTC | 2026-08-19 16:44 UTC | 16m |
| LOST56 | LOS | Los Alamitos Army Air Field (KSLI) | Meadows Field (KBFL) | 2026-08-19 16:07 UTC | 2026-08-19 16:41 UTC | 33m |
| WIZZO4 | WIZ | T-Ranch Airport (XS86) | T-Ranch Airport (XS86) | 2026-08-19 16:39 UTC | 2026-08-19 16:41 UTC | 1m |
| BRW149 | BRW | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-08-19 16:30 UTC | 2026-08-19 16:40 UTC | 10m |
| N123SL |  | St Simons Island Airport (KSSI) | Willow Bend Airport (2WV5) | 2026-08-19 14:59 UTC | 2026-08-19 16:36 UTC | 1h 36m |
| N208W |  | Merrill Field (PAMR) | Beluga Airport (PABG) | 2026-08-19 16:15 UTC | 2026-08-19 16:35 UTC | 20m |
| HGB8236 | HGB | Palau International Airport (PTRO) | Chek Lap Kok International Airport (VHHH) | 2026-08-19 13:07 UTC | 2026-08-19 16:32 UTC | 3h 24m |
| N157U |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-08-19 15:52 UTC | 2026-08-19 16:31 UTC | 39m |
| N995MK |  | Carson City Airport (KCXP) | Silver Springs Airport (KSPZ) | 2026-08-19 16:20 UTC | 2026-08-19 16:31 UTC | 10m |
| N761BB |  | Rocky Mountain Metro Airport (KBJC) | Laramie Regional Airport (KLAR) | 2026-08-19 15:48 UTC | 2026-08-19 16:30 UTC | 41m |
| GCKFG | GCK | London Biggin Hill Airport (EGKB) | London Biggin Hill Airport (EGKB) | 2026-08-19 16:23 UTC | 2026-08-19 16:30 UTC | 6m |
| N312GA |  | Spirit Of St Louis Airport (KSUS) | 07TN (07TN) | 2026-08-19 15:04 UTC | 2026-08-19 16:29 UTC | 1h 24m |
| CNS55 | CNS | Westchester County Airport (KHPN) | Lincoln Airport (KLNK) | 2026-08-19 13:06 UTC | 2026-08-19 16:29 UTC | 3h 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
