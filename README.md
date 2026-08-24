# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_20:27:12_UTC-green)

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

**Latest saved flight:** 2026-08-24 20:27:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 20:27:12 UTC

- **233,317** saved flights
- **71,669** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **233,317** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,812,033.1 tonnes** estimated CO2 emissions
- **163,016,412 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9373 |
| 2 | SkyWest Airlines | 8256 |
| 3 | EJA | 4536 |
| 4 | IndiGo | 3943 |
| 5 | American Airlines | 3808 |
| 6 | Southwest Airlines | 3590 |
| 7 | Delta Air Lines | 2981 |
| 8 | ENY | 2840 |
| 9 | LATAM Airlines | 2241 |
| 10 | AZU | 2173 |
| 11 | Vueling | 1993 |
| 12 | Lufthansa | 1901 |
| 13 | WIF | 1856 |
| 14 | LXJ | 1838 |
| 15 | easyJet | 1631 |
| 16 | Swiss International | 1564 |
| 17 | AXM | 1551 |
| 18 | EJU | 1494 |
| 19 | United Airlines | 1479 |
| 20 | QLK | 1474 |
| 21 | Alaska Airlines | 1401 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1299 |
| 24 | WMT | 1296 |
| 25 | VIV | 1283 |
| 26 | PGT | 1274 |
| 27 | Air France | 1267 |
| 28 | Wizz Air | 1233 |
| 29 | AEE | 1160 |
| 30 | JetBlue | 1160 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 194293 |
| 2 | 🇪🇸 ES | 14986 |
| 3 | 🇧🇷 BR | 13627 |
| 4 | 🇦🇺 AU | 13164 |
| 5 | 🇨🇦 CA | 12867 |
| 6 | 🇮🇹 IT | 12692 |
| 7 | 🇮🇳 IN | 12281 |
| 8 | 🇩🇪 DE | 11503 |
| 9 | 🇬🇧 GB | 11001 |
| 10 | 🇨🇴 CO | 9770 |
| 11 | 🇯🇵 JP | 9448 |
| 12 | 🇫🇷 FR | 9337 |
| 13 | 🇹🇷 TR | 6909 |
| 14 | 🇬🇷 GR | 6865 |
| 15 | 🇲🇽 MX | 6475 |
| 16 | 🇨🇭 CH | 6223 |
| 17 | 🇳🇴 NO | 5769 |
| 18 | 🇲🇾 MY | 4144 |
| 19 | 🇹🇭 TH | 4108 |
| 20 | 🇿🇦 ZA | 4071 |
| 21 | 🇵🇱 PL | 3887 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3185 |
| 24 | 🇬🇹 GT | 2928 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2686 |
| 27 | 🇲🇦 MA | 2369 |
| 28 | 🇲🇪 ME | 2152 |
| 29 | 🇳🇱 NL | 2092 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4854 |
| 2 | Denver International Airport |  | US | 3783 |
| 3 | Indira Gandhi International Airport |  | IN | 2844 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2674 |
| 6 | Harry Reid International Airport |  | US | 2505 |
| 7 | Zurich Airport |  | CH | 2440 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2387 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2341 |
| 10 | La Aurora Airport |  | GT | 2231 |
| 11 | El Dorado International Airport |  | CO | 2174 |
| 12 | Chicago O'Hare International Airport |  | US | 2110 |
| 13 | Salt Lake City International Airport |  | US | 2057 |
| 14 | Congonhas Airport |  | BR | 1988 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1967 |
| 16 | Frankfurt am Main International Airport |  | DE | 1863 |
| 17 | Capua Airport |  | IT | 1839 |
| 18 | Madrid Barajas International Airport |  | ES | 1835 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1753 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1727 |
| 21 | Malpensa International Airport |  | IT | 1673 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1662 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1620 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1534 |
| 27 | Charlotte/Douglas International Airport |  | US | 1512 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1472 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1431 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1409 |
| 32 | Viracopos International Airport |  | BR | 1389 |
| 33 | Bengaluru International Airport |  | IN | 1372 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1368 |
| 35 | Seattle-Tacoma International Airport |  | US | 1367 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1327 |
| 38 | Oslo Gardermoen Airport |  | NO | 1307 |
| 39 | O. R. Tambo International Airport |  | ZA | 1265 |
| 40 | Vancouver International Airport |  | CA | 1265 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 851 | 21m | 244 km | 3,583.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 581 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 522 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 385 | 27m | 275 km | 1,824.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 361 | 1h 50m | 1,423 km | 8,859.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 359 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 339 | 44m | 241 km | 1,408.1 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 309 | 24m | 218 km | 1,164.1 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 306 | 1h 38m | 1,156 km | 6,104.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 289 | 19m | 99 km | 495.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 285 | 27m | 215 km | 1,055.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 271 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 266 | 19m | 144 km | 661.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 251 | 15m | 154 km | 665.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 250 | 1h 50m | 1,304 km | 5,624.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N93154 |  | Butler County Regional/Hogan Field (KHAO) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-24 20:12 UTC | 2026-08-24 20:27 UTC | 14m |
| BPX265 | BPX | 4SC4 (4SC4) | Pickens County Airport (KLQK) | 2026-08-24 20:07 UTC | 2026-08-24 20:23 UTC | 16m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-24 20:10 UTC | 2026-08-24 20:22 UTC | 12m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-24 20:09 UTC | 2026-08-24 20:21 UTC | 11m |
| N64KA |  | Lake Tahoe Airport (KTVL) | Tracy Municipal Airport (KTCY) | 2026-08-24 19:47 UTC | 2026-08-24 20:19 UTC | 32m |
| N993SD |  | March Arb Airport (KRIV) | Hemet-Ryan Airport (KHMT) | 2026-08-24 19:40 UTC | 2026-08-24 20:19 UTC | 39m |
| N862TC |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-08-24 20:01 UTC | 2026-08-24 20:18 UTC | 17m |
| TGGBY | TGG | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-24 20:09 UTC | 2026-08-24 20:16 UTC | 7m |
| SCU58 | SCU | Double W Airport (3OK7) | Double W Airport (3OK7) | 2026-08-24 20:06 UTC | 2026-08-24 20:16 UTC | 10m |
| LFA318 | LFA | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-08-24 19:46 UTC | 2026-08-24 20:12 UTC | 25m |
| N601MB |  | Gooden Airpark (KRJD) | Gooden Airpark (KRJD) | 2026-08-24 19:20 UTC | 2026-08-24 20:11 UTC | 50m |
| N9304F |  | Harford County Airport (K0W3) | Harford County Airport (K0W3) | 2026-08-24 19:57 UTC | 2026-08-24 20:09 UTC | 11m |
| TKR15 | TKR | NV17 (NV17) | Desert Creek Airport (NV97) | 2026-08-24 19:53 UTC | 2026-08-24 20:06 UTC | 12m |
| KSF64 | KSF | Kent State University Airport (K1G3) | Kent State University Airport (K1G3) | 2026-08-24 19:49 UTC | 2026-08-24 20:06 UTC | 16m |
| LOST77 | LOS | Meadows Field (KBFL) | Santa Barbara Municipal Airport (KSBA) | 2026-08-24 19:34 UTC | 2026-08-24 20:05 UTC | 30m |
| N330XT |  | Caldwell Executive Airport (KEUL) | Sky Ranch South Airport (ID79) | 2026-08-24 19:55 UTC | 2026-08-24 20:03 UTC | 7m |
| SCU11 | SCU | Jirik Field (OL23) | Eagle Creek Airport (51OK) | 2026-08-24 19:42 UTC | 2026-08-24 20:02 UTC | 20m |
| EJA291 | EJA | Mc Clellan-Palomar Airport (KCRQ) | Lancaster Airport (KLNS) | 2026-08-24 15:47 UTC | 2026-08-24 20:01 UTC | 4h 14m |
|  |  | K8A0 (K8A0) | K8A0 (K8A0) | 2026-08-24 20:01 UTC | 2026-08-24 20:01 UTC | 0m |
| N560C |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-08-24 19:58 UTC | 2026-08-24 19:59 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
