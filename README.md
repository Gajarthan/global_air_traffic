# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_13:51:51_UTC-green)

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

**Latest saved flight:** 2026-08-20 13:51:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 13:51:51 UTC

- **219,257** saved flights
- **68,891** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **219,257** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,640,243.5 tonnes** estimated CO2 emissions
- **153,057,596 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8795 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4247 |
| 4 | IndiGo | 3724 |
| 5 | American Airlines | 3639 |
| 6 | Southwest Airlines | 3470 |
| 7 | Delta Air Lines | 2824 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2078 |
| 10 | AZU | 2010 |
| 11 | Vueling | 1845 |
| 12 | Lufthansa | 1821 |
| 13 | WIF | 1753 |
| 14 | LXJ | 1729 |
| 15 | easyJet | 1521 |
| 16 | Swiss International | 1458 |
| 17 | AXM | 1443 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1375 |
| 20 | EJU | 1368 |
| 21 | Alaska Airlines | 1339 |
| 22 | All Nippon Airways | 1319 |
| 23 | VIV | 1197 |
| 24 | GLO | 1191 |
| 25 | Air France | 1190 |
| 26 | PGT | 1188 |
| 27 | WMT | 1152 |
| 28 | Wizz Air | 1120 |
| 29 | JetBlue | 1113 |
| 30 | AEE | 1099 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184349 |
| 2 | 🇪🇸 ES | 14059 |
| 3 | 🇧🇷 BR | 12650 |
| 4 | 🇦🇺 AU | 12416 |
| 5 | 🇨🇦 CA | 12082 |
| 6 | 🇮🇹 IT | 11684 |
| 7 | 🇮🇳 IN | 11612 |
| 8 | 🇩🇪 DE | 10838 |
| 9 | 🇬🇧 GB | 10302 |
| 10 | 🇨🇴 CO | 8996 |
| 11 | 🇯🇵 JP | 8959 |
| 12 | 🇫🇷 FR | 8742 |
| 13 | 🇬🇷 GR | 6396 |
| 14 | 🇹🇷 TR | 6313 |
| 15 | 🇲🇽 MX | 6097 |
| 16 | 🇨🇭 CH | 5807 |
| 17 | 🇳🇴 NO | 5445 |
| 18 | 🇲🇾 MY | 3817 |
| 19 | 🇿🇦 ZA | 3743 |
| 20 | 🇹🇭 TH | 3645 |
| 21 | 🇵🇱 PL | 3639 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2957 |
| 24 | 🇬🇹 GT | 2771 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2422 |
| 27 | 🇲🇦 MA | 2209 |
| 28 | 🇳🇱 NL | 1950 |
| 29 | 🇲🇪 ME | 1937 |
| 30 | 🇮🇩 ID | 1866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3579 |
| 3 | Tokyo International Airport |  | JP | 2689 |
| 4 | Indira Gandhi International Airport |  | IN | 2661 |
| 5 | Guaymaral Airport |  | CO | 2596 |
| 6 | Harry Reid International Airport |  | US | 2420 |
| 7 | Zurich Airport |  | CH | 2275 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2246 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2228 |
| 10 | La Aurora Airport |  | GT | 2109 |
| 11 | El Dorado International Airport |  | CO | 2058 |
| 12 | Chicago O'Hare International Airport |  | US | 2008 |
| 13 | Salt Lake City International Airport |  | US | 1931 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1849 |
| 16 | Frankfurt am Main International Airport |  | DE | 1786 |
| 17 | Madrid Barajas International Airport |  | ES | 1721 |
| 18 | Capua Airport |  | IT | 1672 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1620 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1610 |
| 22 | Macau International Airport |  | MO | 1574 |
| 23 | Malpensa International Airport |  | IT | 1546 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1542 |
| 25 | Charles de Gaulle International Airport |  | FR | 1510 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1406 |
| 28 | Kuala Lumpur International Airport |  | MY | 1402 |
| 29 | Barcelona International Airport |  | ES | 1347 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1332 |
| 31 | Bengaluru International Airport |  | IN | 1322 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1284 |
| 35 | Calgary International Airport |  | CA | 1236 |
| 36 | Vitoria/Foronda Airport |  | ES | 1216 |
| 37 | Oslo Gardermoen Airport |  | NO | 1214 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1205 |
| 39 | Don Mueang International Airport |  | TH | 1201 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1178 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 786 | 21m | 244 km | 3,309.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 543 | 1h 7m | 770 km | 7,213.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 494 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 486 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 367 | 27m | 275 km | 1,739.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 323 | 1h 50m | 1,423 km | 7,926.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 321 | 44m | 241 km | 1,333.4 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 289 | 21m | 250 km | 1,248.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 273 | 1h 38m | 1,156 km | 5,446.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 271 | 24m | 218 km | 1,021.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 270 | 27m | 215 km | 1,000.0 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 260 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 250 | 44m | 555 km | 2,393.9 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 250 | 19m | 144 km | 621.9 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N901BS |  | P K Airpark (K5W4) | P K Airpark (K5W4) | 2026-08-20 13:14 UTC | 2026-08-20 13:51 UTC | 37m |
| N448T |  | WEON (WEON) | Jonesboro Municipal Airport (KJBR) | 2026-08-20 13:35 UTC | 2026-08-20 13:47 UTC | 11m |
| CXK111 | CXK | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-08-20 12:50 UTC | 2026-08-20 13:47 UTC | 56m |
| SYS57 | SYS | RAF Shawbury (EGOS) | DCAE Cosford Airport (EGWC) | 2026-08-20 12:59 UTC | 2026-08-20 13:46 UTC | 47m |
| IBS1698 | IBS | Ibiza Airport (LEIB) | Madrid Barajas International Airport (LEMD) | 2026-08-20 12:32 UTC | 2026-08-20 13:44 UTC | 1h 11m |
| DREAD81 | DRE | Collier Airpark (2AL1) | Collier Airpark (2AL1) | 2026-08-20 13:17 UTC | 2026-08-20 13:42 UTC | 25m |
| N408RR |  | Hampton Roads Executive Airport (KPVG) | Newport News/Williamsburg International Airport (KPHF) | 2026-08-20 13:13 UTC | 2026-08-20 13:40 UTC | 26m |
| TRP2 | TRP | Sandy Point Airport (62MD) | Joint Base Andrews Airport (KADW) | 2026-08-20 13:25 UTC | 2026-08-20 13:38 UTC | 13m |
| N737TY |  | Mckinney Ntl Airport (KTKI) | Commerce Municipal Airport (K2F7) | 2026-08-20 13:10 UTC | 2026-08-20 13:36 UTC | 25m |
| CXK363 | CXK | Raleigh-Durham International Airport (KRDU) | Raleigh Regional At Person County Airport (KTDF) | 2026-08-20 12:46 UTC | 2026-08-20 13:34 UTC | 48m |
| N2575U |  | Mid-Carolina Regional Airport (KRUQ) | Mid-Carolina Regional Airport (KRUQ) | 2026-08-20 12:33 UTC | 2026-08-20 13:33 UTC | 1h 0m |
| N56BH |  | Albert Lea Municipal Airport (KAEL) | Albert Lea Municipal Airport (KAEL) | 2026-08-20 12:58 UTC | 2026-08-20 13:28 UTC | 30m |
| QTR816 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-08-20 05:59 UTC | 2026-08-20 13:27 UTC | 7h 27m |
|  |  | Linz Airport (LOWL) | Linz Airport (LOWL) | 2026-08-20 13:23 UTC | 2026-08-20 13:23 UTC | 0m |
| CONGO64 | CON | City Of Colorado Springs Municipal Airport (KCOS) | Usaf Academy Davis Airfield (KAFF) | 2026-08-20 13:10 UTC | 2026-08-20 13:23 UTC | 12m |
| N50011 |  | Denton Enterprise Airport (KDTO) | Bass Aero Airport (OK17) | 2026-08-20 12:46 UTC | 2026-08-20 13:20 UTC | 34m |
| SCU27 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-08-20 13:01 UTC | 2026-08-20 13:20 UTC | 19m |
| N572JA |  | Aurora Municipal Airport (KARR) | 95LL (95LL) | 2026-08-20 12:27 UTC | 2026-08-20 13:19 UTC | 51m |
| DREAD81 | DRE | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Collier Airpark (2AL1) | 2026-08-20 12:45 UTC | 2026-08-20 13:17 UTC | 32m |
| TUTOR046 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-20 12:52 UTC | 2026-08-20 13:16 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
