# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_23:25:26_UTC-green)

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

**Latest saved flight:** 2026-08-20 23:25:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 23:25:26 UTC

- **220,745** saved flights
- **69,259** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **220,745** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,657,098.6 tonnes** estimated CO2 emissions
- **154,034,704 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8844 |
| 2 | SkyWest Airlines | 7880 |
| 3 | EJA | 4285 |
| 4 | IndiGo | 3733 |
| 5 | American Airlines | 3662 |
| 6 | Southwest Airlines | 3487 |
| 7 | Delta Air Lines | 2845 |
| 8 | ENY | 2724 |
| 9 | LATAM Airlines | 2102 |
| 10 | AZU | 2028 |
| 11 | Vueling | 1858 |
| 12 | Lufthansa | 1830 |
| 13 | WIF | 1763 |
| 14 | LXJ | 1744 |
| 15 | easyJet | 1530 |
| 16 | Swiss International | 1466 |
| 17 | AXM | 1445 |
| 18 | United Airlines | 1390 |
| 19 | QLK | 1376 |
| 20 | EJU | 1374 |
| 21 | Alaska Airlines | 1345 |
| 22 | All Nippon Airways | 1319 |
| 23 | GLO | 1208 |
| 24 | VIV | 1205 |
| 25 | Air France | 1196 |
| 26 | PGT | 1196 |
| 27 | WMT | 1163 |
| 28 | Wizz Air | 1124 |
| 29 | JetBlue | 1118 |
| 30 | AEE | 1104 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 185899 |
| 2 | 🇪🇸 ES | 14138 |
| 3 | 🇧🇷 BR | 12774 |
| 4 | 🇦🇺 AU | 12443 |
| 5 | 🇨🇦 CA | 12190 |
| 6 | 🇮🇹 IT | 11741 |
| 7 | 🇮🇳 IN | 11639 |
| 8 | 🇩🇪 DE | 10893 |
| 9 | 🇬🇧 GB | 10365 |
| 10 | 🇨🇴 CO | 9074 |
| 11 | 🇯🇵 JP | 8965 |
| 12 | 🇫🇷 FR | 8783 |
| 13 | 🇬🇷 GR | 6436 |
| 14 | 🇹🇷 TR | 6351 |
| 15 | 🇲🇽 MX | 6142 |
| 16 | 🇨🇭 CH | 5829 |
| 17 | 🇳🇴 NO | 5481 |
| 18 | 🇲🇾 MY | 3820 |
| 19 | 🇿🇦 ZA | 3763 |
| 20 | 🇵🇱 PL | 3661 |
| 21 | 🇹🇭 TH | 3655 |
| 22 | 🇳🇿 NZ | 3043 |
| 23 | 🇵🇭 PH | 2965 |
| 24 | 🇬🇹 GT | 2789 |
| 25 | 🇰🇷 KR | 2638 |
| 26 | 🇭🇷 HR | 2447 |
| 27 | 🇲🇦 MA | 2219 |
| 28 | 🇳🇱 NL | 1962 |
| 29 | 🇲🇪 ME | 1950 |
| 30 | 🇮🇩 ID | 1866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4640 |
| 2 | Denver International Airport |  | US | 3611 |
| 3 | Tokyo International Airport |  | JP | 2690 |
| 4 | Indira Gandhi International Airport |  | IN | 2669 |
| 5 | Guaymaral Airport |  | CO | 2604 |
| 6 | Harry Reid International Airport |  | US | 2434 |
| 7 | Zurich Airport |  | CH | 2288 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2271 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2240 |
| 10 | La Aurora Airport |  | GT | 2125 |
| 11 | El Dorado International Airport |  | CO | 2066 |
| 12 | Chicago O'Hare International Airport |  | US | 2024 |
| 13 | Salt Lake City International Airport |  | US | 1943 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1908 |
| 15 | Congonhas Airport |  | BR | 1869 |
| 16 | Frankfurt am Main International Airport |  | DE | 1797 |
| 17 | Madrid Barajas International Airport |  | ES | 1731 |
| 18 | Capua Airport |  | IT | 1685 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1659 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1628 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1583 |
| 23 | Malpensa International Airport |  | IT | 1548 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1542 |
| 25 | Charles de Gaulle International Airport |  | FR | 1518 |
| 26 | Charlotte/Douglas International Airport |  | US | 1470 |
| 27 | Ninoy Aquino International Airport |  | PH | 1410 |
| 28 | Kuala Lumpur International Airport |  | MY | 1403 |
| 29 | Barcelona International Airport |  | ES | 1354 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1341 |
| 31 | Bengaluru International Airport |  | IN | 1325 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1312 |
| 33 | Seattle-Tacoma International Airport |  | US | 1306 |
| 34 | Viracopos International Airport |  | BR | 1296 |
| 35 | Calgary International Airport |  | CA | 1250 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1235 |
| 37 | Vitoria/Foronda Airport |  | ES | 1225 |
| 38 | Oslo Gardermoen Airport |  | NO | 1224 |
| 39 | Don Mueang International Airport |  | TH | 1202 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1186 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1063 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 792 | 21m | 244 km | 3,334.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 544 | 1h 7m | 770 km | 7,226.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 522 | 24m | 225 km | 2,025.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 499 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 499 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 371 | 27m | 275 km | 1,758.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 325 | 1h 50m | 1,423 km | 7,976.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 324 | 44m | 241 km | 1,345.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 275 | 1h 38m | 1,156 km | 5,486.1 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 274 | 24m | 218 km | 1,032.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 251 | 44m | 555 km | 2,403.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 250 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 239 | 1h 49m | 1,304 km | 5,376.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3223U |  | Southwest Washington Regional Airport (KKLS) | Michair Airport (WT44) | 2026-08-20 23:00 UTC | 2026-08-20 23:25 UTC | 25m |
| N725LU |  | Lynchburg Regional/Preston Glenn Field (KLYH) | Skovhus Airport (VA24) | 2026-08-20 22:34 UTC | 2026-08-20 23:24 UTC | 50m |
| N442HB |  | Springdale Municipal Airport (KASG) | Huntsville Municipal Airport (KH34) | 2026-08-20 23:08 UTC | 2026-08-20 23:23 UTC | 14m |
| N683WA |  | Delano Municipal Airport (KDLO) | Santa Monica Municipal Airport (KSMO) | 2026-08-20 22:52 UTC | 2026-08-20 23:22 UTC | 29m |
| N68750 |  | Poplar Grove Airport (KC77) | Southern Wisconsin Regional Airport (KJVL) | 2026-08-20 22:46 UTC | 2026-08-20 23:19 UTC | 32m |
| ARCAS17 | ARC | Kickapoo Downtown Airport (KCWC) | 54TS (54TS) | 2026-08-20 22:51 UTC | 2026-08-20 23:05 UTC | 14m |
| N7652F |  | Harry Clever Field (KPHD) | Gnadenhutten Airport (3OH8) | 2026-08-20 22:32 UTC | 2026-08-20 23:00 UTC | 27m |
| N5952J |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-08-20 22:29 UTC | 2026-08-20 22:58 UTC | 29m |
| N2056E |  | Merritt Island Airport (KCOI) | Merritt Island Airport (KCOI) | 2026-08-20 22:33 UTC | 2026-08-20 22:58 UTC | 24m |
| MTU35 | MTU | Rachel's Landing Airport (8TN6) | The Aviation Valley Airport (6TN4) | 2026-08-20 22:06 UTC | 2026-08-20 22:50 UTC | 44m |
| TKR168 | TKR | Fairbanks International Airport (PAFA) | Fairbanks International Airport (PAFA) | 2026-08-20 21:35 UTC | 2026-08-20 22:47 UTC | 1h 12m |
| XE1182 |  | Harry Reid International Airport (KLAS) | Santa Monica Municipal Airport (KSMO) | 2026-08-20 21:17 UTC | 2026-08-20 22:47 UTC | 1h 30m |
| EDGE91 | EDG | 4XA5 (4XA5) | Ksa Orchards Airport (OK11) | 2026-08-20 21:51 UTC | 2026-08-20 22:45 UTC | 53m |
| PDT5968 | PDT | Charlotte/Douglas International Airport (KCLT) | Faber Airport (VA96) | 2026-08-20 22:13 UTC | 2026-08-20 22:44 UTC | 30m |
| N465PA |  | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | Kelso Valley Airport (CN37) | 2026-08-20 22:20 UTC | 2026-08-20 22:44 UTC | 24m |
| RAIDR02 | RAI | Miramar Mcas (Joe Foss Field) Airport (KNKX) | Skyotee Ranch Airport (CL74) | 2026-08-20 18:51 UTC | 2026-08-20 22:43 UTC | 3h 51m |
| YGF | YGF | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-08-20 22:00 UTC | 2026-08-20 22:42 UTC | 41m |
| ZJU | ZJU | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-08-20 22:22 UTC | 2026-08-20 22:42 UTC | 19m |
| N851DB |  | Lovell Field (KCHA) | Clarke County Airport (K23M) | 2026-08-20 21:53 UTC | 2026-08-20 22:41 UTC | 48m |
| LR453 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-08-20 22:08 UTC | 2026-08-20 22:39 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
