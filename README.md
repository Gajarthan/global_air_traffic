# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_20:59:53_UTC-green)

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

**Latest saved flight:** 2026-08-24 20:59:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 20:59:53 UTC

- **233,398** saved flights
- **71,682** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **233,398** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,813,142.5 tonnes** estimated CO2 emissions
- **163,080,724 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9376 |
| 2 | SkyWest Airlines | 8262 |
| 3 | EJA | 4536 |
| 4 | IndiGo | 3943 |
| 5 | American Airlines | 3809 |
| 6 | Southwest Airlines | 3590 |
| 7 | Delta Air Lines | 2982 |
| 8 | ENY | 2841 |
| 9 | LATAM Airlines | 2243 |
| 10 | AZU | 2175 |
| 11 | Vueling | 1994 |
| 12 | Lufthansa | 1901 |
| 13 | WIF | 1856 |
| 14 | LXJ | 1839 |
| 15 | easyJet | 1631 |
| 16 | Swiss International | 1564 |
| 17 | AXM | 1551 |
| 18 | EJU | 1494 |
| 19 | United Airlines | 1480 |
| 20 | QLK | 1474 |
| 21 | Alaska Airlines | 1403 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1299 |
| 24 | WMT | 1297 |
| 25 | VIV | 1283 |
| 26 | PGT | 1274 |
| 27 | Air France | 1268 |
| 28 | Wizz Air | 1233 |
| 29 | JetBlue | 1161 |
| 30 | AEE | 1160 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 194363 |
| 2 | 🇪🇸 ES | 14990 |
| 3 | 🇧🇷 BR | 13636 |
| 4 | 🇦🇺 AU | 13166 |
| 5 | 🇨🇦 CA | 12879 |
| 6 | 🇮🇹 IT | 12697 |
| 7 | 🇮🇳 IN | 12281 |
| 8 | 🇩🇪 DE | 11505 |
| 9 | 🇬🇧 GB | 11007 |
| 10 | 🇨🇴 CO | 9781 |
| 11 | 🇯🇵 JP | 9448 |
| 12 | 🇫🇷 FR | 9339 |
| 13 | 🇹🇷 TR | 6916 |
| 14 | 🇬🇷 GR | 6866 |
| 15 | 🇲🇽 MX | 6479 |
| 16 | 🇨🇭 CH | 6223 |
| 17 | 🇳🇴 NO | 5769 |
| 18 | 🇲🇾 MY | 4144 |
| 19 | 🇹🇭 TH | 4108 |
| 20 | 🇿🇦 ZA | 4071 |
| 21 | 🇵🇱 PL | 3888 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3186 |
| 24 | 🇬🇹 GT | 2928 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2686 |
| 27 | 🇲🇦 MA | 2370 |
| 28 | 🇲🇪 ME | 2154 |
| 29 | 🇳🇱 NL | 2092 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4855 |
| 2 | Denver International Airport |  | US | 3786 |
| 3 | Indira Gandhi International Airport |  | IN | 2844 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2676 |
| 6 | Harry Reid International Airport |  | US | 2505 |
| 7 | Zurich Airport |  | CH | 2440 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2389 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2341 |
| 10 | La Aurora Airport |  | GT | 2231 |
| 11 | El Dorado International Airport |  | CO | 2177 |
| 12 | Chicago O'Hare International Airport |  | US | 2111 |
| 13 | Salt Lake City International Airport |  | US | 2058 |
| 14 | Congonhas Airport |  | BR | 1990 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1967 |
| 16 | Frankfurt am Main International Airport |  | DE | 1863 |
| 17 | Capua Airport |  | IT | 1840 |
| 18 | Madrid Barajas International Airport |  | ES | 1835 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1753 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1728 |
| 21 | Malpensa International Airport |  | IT | 1673 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1662 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1621 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1535 |
| 27 | Charlotte/Douglas International Airport |  | US | 1513 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1472 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1434 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1410 |
| 32 | Viracopos International Airport |  | BR | 1390 |
| 33 | Bengaluru International Airport |  | IN | 1372 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1370 |
| 35 | Seattle-Tacoma International Airport |  | US | 1368 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1329 |
| 38 | Oslo Gardermoen Airport |  | NO | 1307 |
| 39 | Vancouver International Airport |  | CA | 1266 |
| 40 | O. R. Tambo International Airport |  | ZA | 1265 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 851 | 21m | 244 km | 3,583.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 582 | 8m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
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
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 271 | 1h 14m | 961 km | 4,492.0 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 271 | 13m | - | - |
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
| N4438U |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-08-24 20:09 UTC | 2026-08-24 20:59 UTC | 50m |
| N19GR |  | Orlando Sanford International Airport (KSFB) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-24 18:45 UTC | 2026-08-24 20:44 UTC | 1h 59m |
| N616ML |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-08-24 20:17 UTC | 2026-08-24 20:41 UTC | 23m |
| OST4 | OST | Stillwater Regional Airport (KSWO) | Stillwater Regional Airport (KSWO) | 2026-08-24 20:00 UTC | 2026-08-24 20:39 UTC | 39m |
| CGIJP | CGI | Vancouver International Airport (CYVR) | Moose Jaw Municipal Airport (CJS4) | 2026-08-24 18:50 UTC | 2026-08-24 20:38 UTC | 1h 48m |
| CGJEI | CGJ | Piedmont Triad International Airport (KGSO) | Laurence G Hanscom Field (KBED) | 2026-08-24 19:07 UTC | 2026-08-24 20:29 UTC | 1h 21m |
| FHY753 | FHY | Antalya International Airport (LTAI) | Baneasa International Airport (LRBS) | 2026-08-24 18:56 UTC | 2026-08-24 20:28 UTC | 1h 31m |
| VAR513 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-24 18:42 UTC | 2026-08-24 20:27 UTC | 1h 45m |
| N916GW |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-24 19:51 UTC | 2026-08-24 20:27 UTC | 36m |
| N93154 |  | Butler County Regional/Hogan Field (KHAO) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-24 20:12 UTC | 2026-08-24 20:27 UTC | 14m |
| TKR106 | TKR | K43U (K43U) | UT99 (UT99) | 2026-08-24 20:18 UTC | 2026-08-24 20:25 UTC | 7m |
| BPX265 | BPX | 4SC4 (4SC4) | Pickens County Airport (KLQK) | 2026-08-24 20:07 UTC | 2026-08-24 20:23 UTC | 16m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-24 20:10 UTC | 2026-08-24 20:22 UTC | 12m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-24 20:09 UTC | 2026-08-24 20:21 UTC | 11m |
| N64KA |  | Lake Tahoe Airport (KTVL) | Tracy Municipal Airport (KTCY) | 2026-08-24 19:47 UTC | 2026-08-24 20:19 UTC | 32m |
| HK5340 |  | El Dorado International Airport (SKBO) | Urrao Airport (SKUR) | 2026-08-24 19:46 UTC | 2026-08-24 20:19 UTC | 33m |
| N993SD |  | March Arb Airport (KRIV) | Hemet-Ryan Airport (KHMT) | 2026-08-24 19:40 UTC | 2026-08-24 20:19 UTC | 39m |
| N233S |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-08-24 18:48 UTC | 2026-08-24 20:19 UTC | 1h 30m |
| N862TC |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-08-24 20:01 UTC | 2026-08-24 20:18 UTC | 17m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-24 20:06 UTC | 2026-08-24 20:16 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
