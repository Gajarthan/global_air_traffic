# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--27_16:14:04_UTC-green)

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

**Latest saved flight:** 2026-08-27 16:14:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-27 16:14:04 UTC

- **239,969** saved flights
- **72,909** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **239,969** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,889,923.0 tonnes** estimated CO2 emissions
- **167,531,766 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9635 |
| 2 | SkyWest Airlines | 8419 |
| 3 | EJA | 4647 |
| 4 | IndiGo | 4044 |
| 5 | American Airlines | 3874 |
| 6 | Southwest Airlines | 3617 |
| 7 | Delta Air Lines | 3055 |
| 8 | ENY | 2900 |
| 9 | LATAM Airlines | 2300 |
| 10 | AZU | 2234 |
| 11 | Vueling | 2063 |
| 12 | Lufthansa | 1936 |
| 13 | WIF | 1903 |
| 14 | LXJ | 1862 |
| 15 | easyJet | 1669 |
| 16 | Swiss International | 1612 |
| 17 | AXM | 1592 |
| 18 | EJU | 1537 |
| 19 | QLK | 1530 |
| 20 | United Airlines | 1512 |
| 21 | Alaska Airlines | 1434 |
| 22 | All Nippon Airways | 1423 |
| 23 | WMT | 1352 |
| 24 | GLO | 1338 |
| 25 | VIV | 1317 |
| 26 | Air France | 1312 |
| 27 | PGT | 1305 |
| 28 | Wizz Air | 1284 |
| 29 | JetBlue | 1190 |
| 30 | AEE | 1189 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 198871 |
| 2 | 🇪🇸 ES | 15437 |
| 3 | 🇧🇷 BR | 13996 |
| 4 | 🇦🇺 AU | 13619 |
| 5 | 🇨🇦 CA | 13342 |
| 6 | 🇮🇹 IT | 13135 |
| 7 | 🇮🇳 IN | 12598 |
| 8 | 🇩🇪 DE | 11852 |
| 9 | 🇬🇧 GB | 11324 |
| 10 | 🇨🇴 CO | 10280 |
| 11 | 🇫🇷 FR | 9659 |
| 12 | 🇯🇵 JP | 9657 |
| 13 | 🇹🇷 TR | 7117 |
| 14 | 🇬🇷 GR | 7069 |
| 15 | 🇲🇽 MX | 6636 |
| 16 | 🇨🇭 CH | 6429 |
| 17 | 🇳🇴 NO | 5932 |
| 18 | 🇹🇭 TH | 4347 |
| 19 | 🇲🇾 MY | 4266 |
| 20 | 🇿🇦 ZA | 4207 |
| 21 | 🇵🇱 PL | 4000 |
| 22 | 🇵🇭 PH | 3295 |
| 23 | 🇳🇿 NZ | 3295 |
| 24 | 🇬🇹 GT | 3014 |
| 25 | 🇰🇷 KR | 2843 |
| 26 | 🇭🇷 HR | 2772 |
| 27 | 🇲🇦 MA | 2428 |
| 28 | 🇲🇪 ME | 2246 |
| 29 | 🇳🇱 NL | 2173 |
| 30 | 🇮🇩 ID | 2103 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4959 |
| 2 | Denver International Airport |  | US | 3868 |
| 3 | Indira Gandhi International Airport |  | IN | 2932 |
| 4 | Tokyo International Airport |  | JP | 2874 |
| 5 | Guaymaral Airport |  | CO | 2694 |
| 6 | Harry Reid International Airport |  | US | 2549 |
| 7 | Zurich Airport |  | CH | 2512 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2459 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2396 |
| 10 | El Dorado International Airport |  | CO | 2319 |
| 11 | La Aurora Airport |  | GT | 2300 |
| 12 | Chicago O'Hare International Airport |  | US | 2142 |
| 13 | Salt Lake City International Airport |  | US | 2110 |
| 14 | Congonhas Airport |  | BR | 2043 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1996 |
| 16 | Frankfurt am Main International Airport |  | DE | 1900 |
| 17 | Capua Airport |  | IT | 1895 |
| 18 | Madrid Barajas International Airport |  | ES | 1890 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1807 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1766 |
| 21 | Malpensa International Airport |  | IT | 1721 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1693 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1683 |
| 24 | Charles de Gaulle International Airport |  | FR | 1678 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1599 |
| 27 | Kuala Lumpur International Airport |  | MY | 1542 |
| 28 | Charlotte/Douglas International Airport |  | US | 1537 |
| 29 | Enrique Olaya Herrera Airport |  | CO | 1526 |
| 30 | Barcelona International Airport |  | ES | 1526 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1452 |
| 32 | Viracopos International Airport |  | BR | 1431 |
| 33 | Don Mueang International Airport |  | TH | 1403 |
| 34 | Bengaluru International Airport |  | IN | 1402 |
| 35 | Seattle-Tacoma International Airport |  | US | 1396 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1394 |
| 37 | Calgary International Airport |  | CA | 1380 |
| 38 | Oslo Gardermoen Airport |  | NO | 1346 |
| 39 | Vancouver International Airport |  | CA | 1318 |
| 40 | O. R. Tambo International Airport |  | ZA | 1312 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1091 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 883 | 21m | 244 km | 3,718.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 618 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 609 | 24m | 225 km | 2,362.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 608 | 1h 6m | 770 km | 8,076.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 543 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 397 | 27m | 275 km | 1,881.2 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 377 | 1h 50m | 1,423 km | 9,252.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 365 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 363 | 44m | 555 km | 3,475.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 348 | 44m | 241 km | 1,445.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 326 | 24m | 218 km | 1,228.2 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 319 | 1h 40m | 1,156 km | 6,363.9 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 298 | 19m | 99 km | 510.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 293 | 27m | 215 km | 1,085.1 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 277 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 271 | 19m | 144 km | 674.1 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 257 | 1h 50m | 1,304 km | 5,781.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N781FA |  | WEON (WEON) | Woodbridge Field (34AR) | 2026-08-27 15:10 UTC | 2026-08-27 16:14 UTC | 1h 3m |
| AFR13VK | Air France | Charles de Gaulle International Airport (LFPG) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-27 14:26 UTC | 2026-08-27 16:02 UTC | 1h 36m |
| CBJ622 | CBJ | Lisbon Portela Airport (LPPT) | Ukhta Airport (UUYH) | 2026-08-27 10:52 UTC | 2026-08-27 16:01 UTC | 5h 9m |
| N40GD |  | Essen Mulheim Airport (EDLE) | Straubing Airport (EDMS) | 2026-08-27 14:23 UTC | 2026-08-27 16:01 UTC | 1h 37m |
| N940LH |  | Dallas Executive Airport (KRBD) | Dallas Executive Airport (KRBD) | 2026-08-27 15:03 UTC | 2026-08-27 16:01 UTC | 58m |
| N9895Q |  | Harford County Airport (K0W3) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-27 15:21 UTC | 2026-08-27 16:01 UTC | 39m |
| BOE369 | BOE | Boeing Field/King County International Airport (KBFI) | Warden Airport (K2S4) | 2026-08-27 15:36 UTC | 2026-08-27 15:58 UTC | 22m |
| N330FZ |  | Asheville Regional Airport (KAVL) | Fox Haven Plantation Airport (58NC) | 2026-08-27 15:38 UTC | 2026-08-27 15:58 UTC | 20m |
| N120JW |  | Jacksonville International Airport (KJAX) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-27 14:20 UTC | 2026-08-27 15:46 UTC | 1h 26m |
| N80HB |  | Arnold Palmer Regional Airport (KLBE) | Capital City Airport (KCXY) | 2026-08-27 15:18 UTC | 2026-08-27 15:44 UTC | 25m |
| CXK505 | CXK | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-27 15:31 UTC | 2026-08-27 15:44 UTC | 13m |
| N415R |  | Lovell Field (KCHA) | Cleveland Regional Jetport Airport (KRZR) | 2026-08-27 15:29 UTC | 2026-08-27 15:43 UTC | 13m |
| N560HS |  | Pilots Ridge Airport (03NC) | Wilmington International Airport (KILM) | 2026-08-27 15:38 UTC | 2026-08-27 15:42 UTC | 4m |
| CFMHJ | CFM | Kelowna Airport (CYLW) | Vancouver International Airport (CYVR) | 2026-08-27 14:47 UTC | 2026-08-27 15:41 UTC | 54m |
| N579ME |  | 0PN2 (0PN2) | Allegheny County Airport (KAGC) | 2026-08-27 15:20 UTC | 2026-08-27 15:41 UTC | 20m |
| N605CA |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-08-27 15:28 UTC | 2026-08-27 15:40 UTC | 11m |
| CGWRS | CGW | Edmonton International Airport (CYEG) | Wainwright Airport (CYWV) | 2026-08-27 15:08 UTC | 2026-08-27 15:39 UTC | 31m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-27 15:25 UTC | 2026-08-27 15:38 UTC | 12m |
| WIF8JT | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-27 15:14 UTC | 2026-08-27 15:38 UTC | 23m |
| N80866 |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-08-27 15:07 UTC | 2026-08-27 15:38 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
