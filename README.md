# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_04:38:06_UTC-green)

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

**Latest saved flight:** 2026-08-25 04:38:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 04:38:06 UTC

- **234,146** saved flights
- **71,828** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **234,146** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,820,419.6 tonnes** estimated CO2 emissions
- **163,502,587 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9382 |
| 2 | SkyWest Airlines | 8297 |
| 3 | EJA | 4553 |
| 4 | IndiGo | 3950 |
| 5 | American Airlines | 3815 |
| 6 | Southwest Airlines | 3598 |
| 7 | Delta Air Lines | 2991 |
| 8 | ENY | 2854 |
| 9 | LATAM Airlines | 2251 |
| 10 | AZU | 2183 |
| 11 | Vueling | 1998 |
| 12 | Lufthansa | 1901 |
| 13 | WIF | 1856 |
| 14 | LXJ | 1844 |
| 15 | easyJet | 1632 |
| 16 | Swiss International | 1565 |
| 17 | AXM | 1559 |
| 18 | EJU | 1495 |
| 19 | QLK | 1490 |
| 20 | United Airlines | 1484 |
| 21 | Alaska Airlines | 1414 |
| 22 | All Nippon Airways | 1395 |
| 23 | GLO | 1306 |
| 24 | WMT | 1297 |
| 25 | VIV | 1292 |
| 26 | PGT | 1275 |
| 27 | Air France | 1268 |
| 28 | Wizz Air | 1234 |
| 29 | AEE | 1162 |
| 30 | JetBlue | 1162 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195061 |
| 2 | 🇪🇸 ES | 15006 |
| 3 | 🇧🇷 BR | 13681 |
| 4 | 🇦🇺 AU | 13252 |
| 5 | 🇨🇦 CA | 12971 |
| 6 | 🇮🇹 IT | 12705 |
| 7 | 🇮🇳 IN | 12306 |
| 8 | 🇩🇪 DE | 11513 |
| 9 | 🇬🇧 GB | 11013 |
| 10 | 🇨🇴 CO | 9849 |
| 11 | 🇯🇵 JP | 9492 |
| 12 | 🇫🇷 FR | 9347 |
| 13 | 🇹🇷 TR | 6931 |
| 14 | 🇬🇷 GR | 6873 |
| 15 | 🇲🇽 MX | 6522 |
| 16 | 🇨🇭 CH | 6225 |
| 17 | 🇳🇴 NO | 5770 |
| 18 | 🇲🇾 MY | 4168 |
| 19 | 🇹🇭 TH | 4134 |
| 20 | 🇿🇦 ZA | 4071 |
| 21 | 🇵🇱 PL | 3894 |
| 22 | 🇳🇿 NZ | 3237 |
| 23 | 🇵🇭 PH | 3206 |
| 24 | 🇬🇹 GT | 2933 |
| 25 | 🇰🇷 KR | 2737 |
| 26 | 🇭🇷 HR | 2686 |
| 27 | 🇲🇦 MA | 2372 |
| 28 | 🇲🇪 ME | 2155 |
| 29 | 🇳🇱 NL | 2092 |
| 30 | 🇮🇩 ID | 2030 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4873 |
| 2 | Denver International Airport |  | US | 3798 |
| 3 | Indira Gandhi International Airport |  | IN | 2850 |
| 4 | Tokyo International Airport |  | JP | 2826 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2516 |
| 7 | Zurich Airport |  | CH | 2442 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2396 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2343 |
| 10 | La Aurora Airport |  | GT | 2235 |
| 11 | El Dorado International Airport |  | CO | 2195 |
| 12 | Chicago O'Hare International Airport |  | US | 2117 |
| 13 | Salt Lake City International Airport |  | US | 2068 |
| 14 | Congonhas Airport |  | BR | 1997 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1971 |
| 16 | Frankfurt am Main International Airport |  | DE | 1863 |
| 17 | Capua Airport |  | IT | 1840 |
| 18 | Madrid Barajas International Airport |  | ES | 1835 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1763 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1732 |
| 21 | Malpensa International Airport |  | IT | 1674 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1664 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1646 |
| 24 | Charles de Gaulle International Airport |  | FR | 1623 |
| 25 | Macau International Airport |  | MO | 1606 |
| 26 | Ninoy Aquino International Airport |  | PH | 1547 |
| 27 | Charlotte/Douglas International Airport |  | US | 1515 |
| 28 | Kuala Lumpur International Airport |  | MY | 1508 |
| 29 | Barcelona International Airport |  | ES | 1475 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1443 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1419 |
| 32 | Viracopos International Airport |  | BR | 1396 |
| 33 | Seattle-Tacoma International Airport |  | US | 1378 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1377 |
| 35 | Bengaluru International Airport |  | IN | 1375 |
| 36 | Don Mueang International Airport |  | TH | 1345 |
| 37 | Calgary International Airport |  | CA | 1344 |
| 38 | Oslo Gardermoen Airport |  | NO | 1307 |
| 39 | Vancouver International Airport |  | CA | 1281 |
| 40 | Vitoria/Foronda Airport |  | ES | 1267 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 859 | 21m | 244 km | 3,617.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 588 | 1h 6m | 770 km | 7,811.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 587 | 24m | 225 km | 2,277.3 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 584 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 523 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 385 | 27m | 275 km | 1,824.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 361 | 1h 50m | 1,423 km | 8,859.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 360 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 339 | 44m | 241 km | 1,408.1 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 329 | 44m | 555 km | 3,150.3 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 310 | 24m | 218 km | 1,167.9 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 307 | 1h 40m | 1,156 km | 6,124.5 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 290 | 19m | 99 km | 496.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 285 | 27m | 215 km | 1,055.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 271 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 266 | 19m | 144 km | 661.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 254 | 15m | 154 km | 673.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 251 | 1h 50m | 1,304 km | 5,646.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RNA254 | RNA | Hamad International Airport (OTHH) | Tribhuvan International Airport (VNKT) | 2026-08-25 00:29 UTC | 2026-08-25 04:38 UTC | 4h 8m |
| A7GAC |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-08-25 03:48 UTC | 2026-08-25 04:32 UTC | 44m |
| OXF5048 | OXF | Falcon Field (KFFZ) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-25 02:53 UTC | 2026-08-25 04:06 UTC | 1h 12m |
| A7GQB |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-08-25 02:11 UTC | 2026-08-25 04:01 UTC | 1h 50m |
| ANA8441 | All Nippon Airways | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-25 01:07 UTC | 2026-08-25 04:00 UTC | 2h 53m |
| SWI | SWI | Melbourne Essendon Airport (YMEN) | Manangatang Airport (YMAG) | 2026-08-25 03:21 UTC | 2026-08-25 03:58 UTC | 37m |
| STALK51 | STA | Albuquerque International Sunport Airport (KABQ) | Los Alamos Airport (KLAM) | 2026-08-25 03:07 UTC | 2026-08-25 03:55 UTC | 47m |
| CWA922 | CWA | Calgary International Airport (CYYC) | Foremost Airport (CFD4) | 2026-08-25 03:22 UTC | 2026-08-25 03:52 UTC | 29m |
| OC95 |  | Fukuoka Airport (RJFF) | Kamigoto Airport (RJDK) | 2026-08-25 03:25 UTC | 2026-08-25 03:51 UTC | 26m |
| XSN90 | XSN | Napa County Airport (KAPC) | Palo Alto Airport (KPAO) | 2026-08-25 03:33 UTC | 2026-08-25 03:49 UTC | 16m |
| STT5024 | STT | Daniel K Inouye International Airport (PHNL) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-08-25 03:00 UTC | 2026-08-25 03:47 UTC | 46m |
| N717PA |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-08-25 03:21 UTC | 2026-08-25 03:46 UTC | 25m |
| ZKTTL | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-08-25 03:34 UTC | 2026-08-25 03:46 UTC | 12m |
| ARE4026 | ARE | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 2026-08-25 03:24 UTC | 2026-08-25 03:43 UTC | 19m |
| N486LP |  | AZ00 (AZ00) | Glendale Regional Airport (KGEU) | 2026-08-25 02:26 UTC | 2026-08-25 03:40 UTC | 1h 14m |
| SWT1810 | SWT | Cologne Bonn Airport (EDDK) | Vitoria/Foronda Airport (LEVT) | 2026-08-25 01:57 UTC | 2026-08-25 03:40 UTC | 1h 42m |
| LAO442 | LAO | Suvarnabhumi Airport (VTBS) | Xieng Khouang Airport (VLXK) | 2026-08-25 02:49 UTC | 2026-08-25 03:37 UTC | 48m |
| QXE2292 | QXE | Seattle-Tacoma International Airport (KSEA) | Carson Field (MT53) | 2026-08-25 02:49 UTC | 2026-08-25 03:36 UTC | 46m |
| LTA660 | LTA | Scholes International At Galveston Airport (KGLS) | Eagle Air Park (2TE0) | 2026-08-25 03:10 UTC | 2026-08-25 03:35 UTC | 24m |
| VOI3316 | VOI | General Abelardo L. Rodriguez International Airport (MMTJ) | General Jose Maria Yanez International Airport (MMGM) | 2026-08-25 02:25 UTC | 2026-08-25 03:28 UTC | 1h 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
