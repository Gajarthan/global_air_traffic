# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_17:22:21_UTC-green)

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

**Latest saved flight:** 2026-08-23 17:22:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 17:22:21 UTC

- **229,309** saved flights
- **70,868** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **229,309** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,765,114.5 tonnes** estimated CO2 emissions
- **160,296,491 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9211 |
| 2 | SkyWest Airlines | 8129 |
| 3 | EJA | 4419 |
| 4 | IndiGo | 3879 |
| 5 | American Airlines | 3749 |
| 6 | Southwest Airlines | 3551 |
| 7 | Delta Air Lines | 2933 |
| 8 | ENY | 2796 |
| 9 | LATAM Airlines | 2202 |
| 10 | AZU | 2127 |
| 11 | Vueling | 1947 |
| 12 | Lufthansa | 1873 |
| 13 | WIF | 1808 |
| 14 | LXJ | 1796 |
| 15 | easyJet | 1600 |
| 16 | Swiss International | 1531 |
| 17 | AXM | 1520 |
| 18 | EJU | 1461 |
| 19 | United Airlines | 1450 |
| 20 | QLK | 1448 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1274 |
| 24 | VIV | 1257 |
| 25 | PGT | 1254 |
| 26 | WMT | 1254 |
| 27 | Air France | 1251 |
| 28 | Wizz Air | 1202 |
| 29 | JetBlue | 1144 |
| 30 | AEE | 1142 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 191301 |
| 2 | 🇪🇸 ES | 14728 |
| 3 | 🇧🇷 BR | 13388 |
| 4 | 🇦🇺 AU | 12963 |
| 5 | 🇨🇦 CA | 12644 |
| 6 | 🇮🇹 IT | 12416 |
| 7 | 🇮🇳 IN | 12094 |
| 8 | 🇩🇪 DE | 11302 |
| 9 | 🇬🇧 GB | 10799 |
| 10 | 🇨🇴 CO | 9460 |
| 11 | 🇯🇵 JP | 9314 |
| 12 | 🇫🇷 FR | 9193 |
| 13 | 🇹🇷 TR | 6761 |
| 14 | 🇬🇷 GR | 6741 |
| 15 | 🇲🇽 MX | 6375 |
| 16 | 🇨🇭 CH | 6096 |
| 17 | 🇳🇴 NO | 5642 |
| 18 | 🇲🇾 MY | 4062 |
| 19 | 🇿🇦 ZA | 4001 |
| 20 | 🇹🇭 TH | 3997 |
| 21 | 🇵🇱 PL | 3821 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3144 |
| 24 | 🇬🇹 GT | 2884 |
| 25 | 🇰🇷 KR | 2705 |
| 26 | 🇭🇷 HR | 2623 |
| 27 | 🇲🇦 MA | 2325 |
| 28 | 🇲🇪 ME | 2095 |
| 29 | 🇳🇱 NL | 2056 |
| 30 | 🇮🇩 ID | 1978 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4788 |
| 2 | Denver International Airport |  | US | 3728 |
| 3 | Indira Gandhi International Airport |  | IN | 2795 |
| 4 | Tokyo International Airport |  | JP | 2781 |
| 5 | Guaymaral Airport |  | CO | 2652 |
| 6 | Harry Reid International Airport |  | US | 2478 |
| 7 | Zurich Airport |  | CH | 2389 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2344 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2312 |
| 10 | La Aurora Airport |  | GT | 2197 |
| 11 | El Dorado International Airport |  | CO | 2100 |
| 12 | Chicago O'Hare International Airport |  | US | 2073 |
| 13 | Salt Lake City International Airport |  | US | 2014 |
| 14 | Congonhas Airport |  | BR | 1954 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1941 |
| 16 | Frankfurt am Main International Airport |  | DE | 1840 |
| 17 | Madrid Barajas International Airport |  | ES | 1799 |
| 18 | Capua Airport |  | IT | 1795 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1716 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1705 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1651 |
| 22 | Malpensa International Airport |  | IT | 1640 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Macau International Airport |  | MO | 1596 |
| 25 | Charles de Gaulle International Airport |  | FR | 1594 |
| 26 | Ninoy Aquino International Airport |  | PH | 1509 |
| 27 | Charlotte/Douglas International Airport |  | US | 1498 |
| 28 | Kuala Lumpur International Airport |  | MY | 1471 |
| 29 | Barcelona International Airport |  | ES | 1437 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1389 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1367 |
| 32 | Viracopos International Airport |  | BR | 1361 |
| 33 | Bengaluru International Airport |  | IN | 1358 |
| 34 | Seattle-Tacoma International Airport |  | US | 1350 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1346 |
| 36 | Don Mueang International Airport |  | TH | 1307 |
| 37 | Calgary International Airport |  | CA | 1300 |
| 38 | Oslo Gardermoen Airport |  | NO | 1276 |
| 39 | Vitoria/Foronda Airport |  | ES | 1250 |
| 40 | O. R. Tambo International Airport |  | ZA | 1244 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 834 | 21m | 244 km | 3,511.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 575 | 1h 6m | 770 km | 7,638.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 554 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 515 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 380 | 27m | 275 km | 1,800.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 351 | 1h 50m | 1,423 km | 8,614.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 332 | 44m | 241 km | 1,379.1 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 320 | 21m | 250 km | 1,382.2 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 310 | 44m | 555 km | 2,968.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 306 | 22m | 55 km | 290.8 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 297 | 24m | 218 km | 1,118.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 295 | 1h 38m | 1,156 km | 5,885.1 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 280 | 27m | 215 km | 1,037.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 269 | 1h 14m | 961 km | 4,458.8 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 261 | 19m | 144 km | 649.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 240 | 28m | 152 km | 627.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MVK79 | MVK | Mankato Regional Airport (KMKT) | Mankato Regional Airport (KMKT) | 2026-08-23 16:57 UTC | 2026-08-23 17:22 UTC | 24m |
| OKAUR21 | OKA | LKSP (LKSP) | LKSP (LKSP) | 2026-08-23 16:37 UTC | 2026-08-23 17:12 UTC | 34m |
| EXS91JH | EXS | London Luton Airport (EGGW) | Kastoria National Airport (LGKA) | 2026-08-23 14:36 UTC | 2026-08-23 17:09 UTC | 2h 32m |
| N5470K |  | Orlando Apopka Airport (KX04) | FL47 (FL47) | 2026-08-23 16:25 UTC | 2026-08-23 17:09 UTC | 43m |
| N1976F |  | Princeton Airport (K39N) | Sky Manor Airport (KN40) | 2026-08-23 16:21 UTC | 2026-08-23 17:06 UTC | 45m |
| N84BL |  | Newark Liberty International Airport (KEWR) | John F Kennedy International Airport (KJFK) | 2026-08-23 16:48 UTC | 2026-08-23 17:03 UTC | 15m |
| IBRPP | IBR | Comiso Airport Vincenzo Magliocco (LICB) | Comiso Airport Vincenzo Magliocco (LICB) | 2026-08-23 17:01 UTC | 2026-08-23 17:02 UTC | 1m |
| THY3120 | Turkish Airlines | Cardak Airport (LTAY) | Białystok-Krywlany Airport (EPBK) | 2026-08-23 14:36 UTC | 2026-08-23 17:02 UTC | 2h 25m |
| N405VJ |  | Miami-Opa Locka Executive Airport (KOPF) | 20NC (20NC) | 2026-08-23 15:27 UTC | 2026-08-23 17:01 UTC | 1h 34m |
| N5280F |  | William P Hobby Airport (KHOU) | George Bush Intcntl/Houston Airport (KIAH) | 2026-08-23 16:52 UTC | 2026-08-23 16:58 UTC | 5m |
| N223RC |  | Norfolk International Airport (KORF) | Robert F Swinnie Airport (KPHH) | 2026-08-23 15:54 UTC | 2026-08-23 16:56 UTC | 1h 2m |
| RGA07 | RGA | Bad Ragaz Airport (LSZE) | Sitterdorf Airport (LSZV) | 2026-08-23 16:46 UTC | 2026-08-23 16:55 UTC | 8m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-23 15:43 UTC | 2026-08-23 16:54 UTC | 1h 11m |
| N5852K |  | Albuquerque International Sunport Airport (KABQ) | G Bar F Ranch Airport (NM84) | 2026-08-23 15:37 UTC | 2026-08-23 16:50 UTC | 1h 13m |
| TGJFC | TGJ | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-23 16:30 UTC | 2026-08-23 16:50 UTC | 20m |
| N29EF |  | Monmouth Executive Airport (KBLM) | Monmouth Executive Airport (KBLM) | 2026-08-23 15:59 UTC | 2026-08-23 16:48 UTC | 48m |
| CGJKI | CGJ | Saint John Airport (CYSJ) | Bangor International Airport (KBGR) | 2026-08-23 16:16 UTC | 2026-08-23 16:46 UTC | 29m |
| N750DX |  | Addison Airport (KADS) | CD99 (CD99) | 2026-08-23 15:13 UTC | 2026-08-23 16:46 UTC | 1h 33m |
| N692CK |  | Muskegon County Airport (KMKG) | Muskegon County Airport (KMKG) | 2026-08-23 16:34 UTC | 2026-08-23 16:45 UTC | 11m |
| CRV1 | CRV | Deauville-Saint-Gatien Airport (LFRG) | Cork Airport (EICK) | 2026-08-23 15:36 UTC | 2026-08-23 16:45 UTC | 1h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
