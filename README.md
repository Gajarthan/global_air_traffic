# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_16:48:18_UTC-green)

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

**Latest saved flight:** 2026-08-23 16:48:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 16:48:18 UTC

- **229,218** saved flights
- **70,841** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **229,218** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,764,037.0 tonnes** estimated CO2 emissions
- **160,234,030 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9206 |
| 2 | SkyWest Airlines | 8128 |
| 3 | EJA | 4413 |
| 4 | IndiGo | 3878 |
| 5 | American Airlines | 3748 |
| 6 | Southwest Airlines | 3551 |
| 7 | Delta Air Lines | 2933 |
| 8 | ENY | 2796 |
| 9 | LATAM Airlines | 2202 |
| 10 | AZU | 2127 |
| 11 | Vueling | 1947 |
| 12 | Lufthansa | 1873 |
| 13 | WIF | 1806 |
| 14 | LXJ | 1794 |
| 15 | easyJet | 1600 |
| 16 | Swiss International | 1531 |
| 17 | AXM | 1520 |
| 18 | EJU | 1459 |
| 19 | United Airlines | 1450 |
| 20 | QLK | 1448 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1274 |
| 24 | VIV | 1256 |
| 25 | PGT | 1253 |
| 26 | WMT | 1253 |
| 27 | Air France | 1249 |
| 28 | Wizz Air | 1201 |
| 29 | JetBlue | 1143 |
| 30 | AEE | 1142 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 191234 |
| 2 | 🇪🇸 ES | 14724 |
| 3 | 🇧🇷 BR | 13385 |
| 4 | 🇦🇺 AU | 12963 |
| 5 | 🇨🇦 CA | 12643 |
| 6 | 🇮🇹 IT | 12405 |
| 7 | 🇮🇳 IN | 12090 |
| 8 | 🇩🇪 DE | 11293 |
| 9 | 🇬🇧 GB | 10796 |
| 10 | 🇨🇴 CO | 9456 |
| 11 | 🇯🇵 JP | 9314 |
| 12 | 🇫🇷 FR | 9190 |
| 13 | 🇹🇷 TR | 6753 |
| 14 | 🇬🇷 GR | 6739 |
| 15 | 🇲🇽 MX | 6373 |
| 16 | 🇨🇭 CH | 6094 |
| 17 | 🇳🇴 NO | 5637 |
| 18 | 🇲🇾 MY | 4062 |
| 19 | 🇿🇦 ZA | 3999 |
| 20 | 🇹🇭 TH | 3997 |
| 21 | 🇵🇱 PL | 3817 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3144 |
| 24 | 🇬🇹 GT | 2880 |
| 25 | 🇰🇷 KR | 2705 |
| 26 | 🇭🇷 HR | 2621 |
| 27 | 🇲🇦 MA | 2325 |
| 28 | 🇲🇪 ME | 2093 |
| 29 | 🇳🇱 NL | 2054 |
| 30 | 🇮🇩 ID | 1978 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4785 |
| 2 | Denver International Airport |  | US | 3725 |
| 3 | Indira Gandhi International Airport |  | IN | 2795 |
| 4 | Tokyo International Airport |  | JP | 2781 |
| 5 | Guaymaral Airport |  | CO | 2652 |
| 6 | Harry Reid International Airport |  | US | 2477 |
| 7 | Zurich Airport |  | CH | 2389 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2344 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2312 |
| 10 | La Aurora Airport |  | GT | 2194 |
| 11 | El Dorado International Airport |  | CO | 2098 |
| 12 | Chicago O'Hare International Airport |  | US | 2073 |
| 13 | Salt Lake City International Airport |  | US | 2014 |
| 14 | Congonhas Airport |  | BR | 1954 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1941 |
| 16 | Frankfurt am Main International Airport |  | DE | 1837 |
| 17 | Madrid Barajas International Airport |  | ES | 1798 |
| 18 | Capua Airport |  | IT | 1791 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1716 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1705 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1650 |
| 22 | Malpensa International Airport |  | IT | 1640 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Macau International Airport |  | MO | 1596 |
| 25 | Charles de Gaulle International Airport |  | FR | 1592 |
| 26 | Ninoy Aquino International Airport |  | PH | 1509 |
| 27 | Charlotte/Douglas International Airport |  | US | 1497 |
| 28 | Kuala Lumpur International Airport |  | MY | 1471 |
| 29 | Barcelona International Airport |  | ES | 1437 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1388 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1367 |
| 32 | Viracopos International Airport |  | BR | 1361 |
| 33 | Bengaluru International Airport |  | IN | 1357 |
| 34 | Seattle-Tacoma International Airport |  | US | 1350 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Don Mueang International Airport |  | TH | 1307 |
| 37 | Calgary International Airport |  | CA | 1300 |
| 38 | Oslo Gardermoen Airport |  | NO | 1273 |
| 39 | Vitoria/Foronda Airport |  | ES | 1250 |
| 40 | O. R. Tambo International Airport |  | ZA | 1243 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 834 | 21m | 244 km | 3,511.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 575 | 1h 6m | 770 km | 7,638.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 554 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 380 | 27m | 275 km | 1,800.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 351 | 1h 50m | 1,423 km | 8,614.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 319 | 21m | 250 km | 1,377.9 t |
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
| N29EF |  | Monmouth Executive Airport (KBLM) | Monmouth Executive Airport (KBLM) | 2026-08-23 15:59 UTC | 2026-08-23 16:48 UTC | 48m |
| N692CK |  | Muskegon County Airport (KMKG) | Muskegon County Airport (KMKG) | 2026-08-23 16:34 UTC | 2026-08-23 16:45 UTC | 11m |
| N572JA |  | Aurora Municipal Airport (KARR) | 0IL8 (0IL8) | 2026-08-23 16:24 UTC | 2026-08-23 16:41 UTC | 16m |
| N721CT |  | Haskell Airport (K2K9) | Gregg Airport (7OK1) | 2026-08-23 16:23 UTC | 2026-08-23 16:41 UTC | 17m |
| SXS7WX | SXS | Mollis Airport (LSZM) | Kaklic Airport (LTFA) | 2026-08-23 14:23 UTC | 2026-08-23 16:39 UTC | 2h 15m |
| N70739 |  | Middleton Municipal/Morey Field (KC29) | Thiessen Field (34WI) | 2026-08-23 16:24 UTC | 2026-08-23 16:36 UTC | 12m |
| N35672 |  | Sweetbriar Airport (83OK) | Mount Vernon Municipal Airport (K2MO) | 2026-08-23 15:20 UTC | 2026-08-23 16:33 UTC | 1h 13m |
| N21754 |  | Orlando Apopka Airport (KX04) | Leesburg International Airport (KLEE) | 2026-08-23 15:42 UTC | 2026-08-23 16:31 UTC | 48m |
| GHEVR | GHE | Deanland Lewes Airport (EGKL) | Shoreham Airport (EGKA) | 2026-08-23 16:16 UTC | 2026-08-23 16:29 UTC | 12m |
| CXK180 | CXK | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-23 16:18 UTC | 2026-08-23 16:29 UTC | 10m |
| DETDP | DET | ETIN (ETIN) | Wurzburg-Schenkenturm Airport (EDFW) | 2026-08-23 16:16 UTC | 2026-08-23 16:28 UTC | 12m |
| N446RT |  | Dallas Executive Airport (KRBD) | Moonbow Field (25XS) | 2026-08-23 16:19 UTC | 2026-08-23 16:27 UTC | 7m |
| N734RE |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-08-23 15:41 UTC | 2026-08-23 16:26 UTC | 44m |
| N357LP |  | Witham Field (KSUA) | Mountain Empire Airport (KMKJ) | 2026-08-23 14:28 UTC | 2026-08-23 16:23 UTC | 1h 54m |
| SCU45 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-08-23 16:22 UTC | 2026-08-23 16:22 UTC | 0m |
| N499MD |  | Flying Cloud Airport (KFCM) | Glendale Regional Airport (KGEU) | 2026-08-23 13:15 UTC | 2026-08-23 16:21 UTC | 3h 6m |
| N3803S |  | Boise Air Trml/Gowen Field (KBOI) | Green Acres Airport (ID68) | 2026-08-23 15:40 UTC | 2026-08-23 16:20 UTC | 39m |
| N523WC |  | Griffin/Sloas Airport (80OH) | Dubuque Regional Airport (KDBQ) | 2026-08-23 15:05 UTC | 2026-08-23 16:19 UTC | 1h 14m |
| N3546T |  | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-08-23 15:42 UTC | 2026-08-23 16:18 UTC | 36m |
| TRF500 | TRF | Addison Airport (KADS) | 01TE (01TE) | 2026-08-23 15:59 UTC | 2026-08-23 16:15 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
