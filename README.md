# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_10:50:46_UTC-green)

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

**Latest saved flight:** 2026-08-26 10:50:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 10:50:46 UTC

- **238,136** saved flights
- **72,516** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **238,136** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,869,440.5 tonnes** estimated CO2 emissions
- **166,344,376 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9551 |
| 2 | SkyWest Airlines | 8391 |
| 3 | EJA | 4617 |
| 4 | IndiGo | 4014 |
| 5 | American Airlines | 3855 |
| 6 | Southwest Airlines | 3613 |
| 7 | Delta Air Lines | 3034 |
| 8 | ENY | 2881 |
| 9 | LATAM Airlines | 2284 |
| 10 | AZU | 2217 |
| 11 | Vueling | 2043 |
| 12 | Lufthansa | 1928 |
| 13 | WIF | 1891 |
| 14 | LXJ | 1852 |
| 15 | easyJet | 1661 |
| 16 | Swiss International | 1604 |
| 17 | AXM | 1589 |
| 18 | EJU | 1528 |
| 19 | QLK | 1527 |
| 20 | United Airlines | 1505 |
| 21 | Alaska Airlines | 1430 |
| 22 | All Nippon Airways | 1418 |
| 23 | WMT | 1332 |
| 24 | GLO | 1329 |
| 25 | VIV | 1312 |
| 26 | PGT | 1299 |
| 27 | Air France | 1297 |
| 28 | Wizz Air | 1272 |
| 29 | AEE | 1182 |
| 30 | JetBlue | 1180 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 197448 |
| 2 | 🇪🇸 ES | 15299 |
| 3 | 🇧🇷 BR | 13889 |
| 4 | 🇦🇺 AU | 13560 |
| 5 | 🇨🇦 CA | 13180 |
| 6 | 🇮🇹 IT | 13015 |
| 7 | 🇮🇳 IN | 12514 |
| 8 | 🇩🇪 DE | 11752 |
| 9 | 🇬🇧 GB | 11241 |
| 10 | 🇨🇴 CO | 10127 |
| 11 | 🇯🇵 JP | 9640 |
| 12 | 🇫🇷 FR | 9566 |
| 13 | 🇹🇷 TR | 7075 |
| 14 | 🇬🇷 GR | 7019 |
| 15 | 🇲🇽 MX | 6603 |
| 16 | 🇨🇭 CH | 6379 |
| 17 | 🇳🇴 NO | 5892 |
| 18 | 🇹🇭 TH | 4306 |
| 19 | 🇲🇾 MY | 4258 |
| 20 | 🇿🇦 ZA | 4173 |
| 21 | 🇵🇱 PL | 3956 |
| 22 | 🇳🇿 NZ | 3290 |
| 23 | 🇵🇭 PH | 3287 |
| 24 | 🇬🇹 GT | 2978 |
| 25 | 🇰🇷 KR | 2825 |
| 26 | 🇭🇷 HR | 2749 |
| 27 | 🇲🇦 MA | 2404 |
| 28 | 🇲🇪 ME | 2220 |
| 29 | 🇳🇱 NL | 2146 |
| 30 | 🇮🇩 ID | 2093 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4936 |
| 2 | Denver International Airport |  | US | 3851 |
| 3 | Indira Gandhi International Airport |  | IN | 2911 |
| 4 | Tokyo International Airport |  | JP | 2870 |
| 5 | Guaymaral Airport |  | CO | 2689 |
| 6 | Harry Reid International Airport |  | US | 2538 |
| 7 | Zurich Airport |  | CH | 2501 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2436 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2381 |
| 10 | El Dorado International Airport |  | CO | 2279 |
| 11 | La Aurora Airport |  | GT | 2269 |
| 12 | Chicago O'Hare International Airport |  | US | 2131 |
| 13 | Salt Lake City International Airport |  | US | 2095 |
| 14 | Congonhas Airport |  | BR | 2024 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1987 |
| 16 | Frankfurt am Main International Airport |  | DE | 1888 |
| 17 | Capua Airport |  | IT | 1875 |
| 18 | Madrid Barajas International Airport |  | ES | 1870 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1794 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1752 |
| 21 | Malpensa International Airport |  | IT | 1710 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1683 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1679 |
| 24 | Charles de Gaulle International Airport |  | FR | 1659 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1593 |
| 27 | Kuala Lumpur International Airport |  | MY | 1539 |
| 28 | Charlotte/Douglas International Airport |  | US | 1529 |
| 29 | Barcelona International Airport |  | ES | 1511 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1492 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1442 |
| 32 | Viracopos International Airport |  | BR | 1419 |
| 33 | Bengaluru International Airport |  | IN | 1393 |
| 34 | Don Mueang International Airport |  | TH | 1392 |
| 35 | Seattle-Tacoma International Airport |  | US | 1392 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1390 |
| 37 | Calgary International Airport |  | CA | 1367 |
| 38 | Oslo Gardermoen Airport |  | NO | 1337 |
| 39 | Vancouver International Airport |  | CA | 1303 |
| 40 | O. R. Tambo International Airport |  | ZA | 1297 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1089 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 876 | 21m | 244 km | 3,688.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 609 | 24m | 225 km | 2,362.6 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 606 | 1h 6m | 770 km | 8,050.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 604 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 532 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 393 | 27m | 275 km | 1,862.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 370 | 1h 50m | 1,423 km | 9,080.4 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 364 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 357 | 44m | 555 km | 3,418.4 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 344 | 44m | 241 km | 1,428.9 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 337 | 21m | 250 km | 1,455.6 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 321 | 24m | 218 km | 1,209.3 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 318 | 22m | 55 km | 302.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 317 | 1h 40m | 1,156 km | 6,324.0 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 296 | 19m | 99 km | 507.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 292 | 27m | 215 km | 1,081.4 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 277 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 269 | 19m | 144 km | 669.1 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 255 | 1h 50m | 1,304 km | 5,736.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 247 | 28m | 152 km | 645.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UFX61 | UFX | Blackpool International Airport (EGNH) | RAF Woodvale (EGOW) | 2026-08-26 10:39 UTC | 2026-08-26 10:50 UTC | 11m |
| EWG9 | EWG | Dresden Airport (EDDC) | Dresden Airport (EDDC) | 2026-08-26 10:04 UTC | 2026-08-26 10:45 UTC | 41m |
| SPTIR | SPT | Babice Airport (EPBC) | Babice Airport (EPBC) | 2026-08-26 09:00 UTC | 2026-08-26 10:45 UTC | 1h 44m |
| N253EA |  | AZ00 (AZ00) | Glendale Regional Airport (KGEU) | 2026-08-26 09:15 UTC | 2026-08-26 10:37 UTC | 1h 22m |
| LICHEN8 | LIC | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-26 07:41 UTC | 2026-08-26 10:33 UTC | 2h 52m |
| FDA207 | FDA | Matsumoto Airport (RJAF) | Ozuki Airport (RJOZ) | 2026-08-26 09:07 UTC | 2026-08-26 10:31 UTC | 1h 24m |
| LINCE01 | LIN | Torrejon Airport (LETO) | Vitoria/Foronda Airport (LEVT) | 2026-08-26 10:02 UTC | 2026-08-26 10:28 UTC | 25m |
| DEFFY | DEF | Baneasa International Airport (LRBS) | Baneasa International Airport (LRBS) | 2026-08-26 10:05 UTC | 2026-08-26 10:27 UTC | 21m |
| CRK641 | CRK | Fukuoka Airport (RJFF) | Zhuhai Airport (ZGSD) | 2026-08-26 07:40 UTC | 2026-08-26 10:26 UTC | 2h 46m |
| QLK1284 | QLK | Adelaide International Airport (YPAD) | Brisbane International Airport (YBBN) | 2026-08-26 08:20 UTC | 2026-08-26 10:24 UTC | 2h 3m |
| A7GAC |  | Al Khawr Airport (OTBK) | Das Island Airport (OMAS) | 2026-08-26 10:07 UTC | 2026-08-26 10:24 UTC | 16m |
| UFX61 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-26 09:50 UTC | 2026-08-26 10:22 UTC | 32m |
| ZSSUJ | ZSS | Wonderboom Airport (FAWB) | Wonderboom Airport (FAWB) | 2026-08-26 09:36 UTC | 2026-08-26 10:22 UTC | 46m |
| SWR896B | Swiss International | Munich International Airport (EDDM) | Zurich Airport (LSZH) | 2026-08-26 09:44 UTC | 2026-08-26 10:21 UTC | 37m |
| FHOKE | FHO | Lille/Marcq-en-Baroeul Airport (LFQO) | Lille/Marcq-en-Baroeul Airport (LFQO) | 2026-08-26 10:01 UTC | 2026-08-26 10:16 UTC | 14m |
| QAF5 | QAF | Lyon Saint-Exupery Airport (LFLL) | Lyon Saint-Exupery Airport (LFLL) | 2026-08-26 09:59 UTC | 2026-08-26 10:15 UTC | 15m |
| HKS51 | HKS | Humberside Airport (EGNJ) | EGYO (EGYO) | 2026-08-26 09:49 UTC | 2026-08-26 10:11 UTC | 22m |
| RGA08 | RGA | Luzern-Beromunster Airport (LSZO) | Kagiswil Airport (LSPG) | 2026-08-26 09:50 UTC | 2026-08-26 10:09 UTC | 19m |
| N7873N |  | City Of Colorado Springs Municipal Airport (KCOS) | Limon Municipal Airport (KLIC) | 2026-08-26 09:35 UTC | 2026-08-26 10:04 UTC | 29m |
| GLFIX | GLF | Sywell Aerodrome (EGBK) | Bedford Aerodrome (EGBF) | 2026-08-26 09:58 UTC | 2026-08-26 10:03 UTC | 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
