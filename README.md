# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_08:40:42_UTC-green)

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

**Latest saved flight:** 2026-08-26 08:40:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 08:40:42 UTC

- **237,819** saved flights
- **72,429** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **237,819** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,864,686.5 tonnes** estimated CO2 emissions
- **166,068,785 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9526 |
| 2 | SkyWest Airlines | 8391 |
| 3 | EJA | 4617 |
| 4 | IndiGo | 4008 |
| 5 | American Airlines | 3855 |
| 6 | Southwest Airlines | 3613 |
| 7 | Delta Air Lines | 3034 |
| 8 | ENY | 2881 |
| 9 | LATAM Airlines | 2283 |
| 10 | AZU | 2216 |
| 11 | Vueling | 2038 |
| 12 | Lufthansa | 1924 |
| 13 | WIF | 1887 |
| 14 | LXJ | 1852 |
| 15 | easyJet | 1657 |
| 16 | Swiss International | 1594 |
| 17 | AXM | 1589 |
| 18 | EJU | 1526 |
| 19 | QLK | 1525 |
| 20 | United Airlines | 1505 |
| 21 | Alaska Airlines | 1430 |
| 22 | All Nippon Airways | 1417 |
| 23 | GLO | 1329 |
| 24 | WMT | 1329 |
| 25 | VIV | 1312 |
| 26 | PGT | 1297 |
| 27 | Air France | 1287 |
| 28 | Wizz Air | 1269 |
| 29 | JetBlue | 1180 |
| 30 | AEE | 1179 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 197427 |
| 2 | 🇪🇸 ES | 15255 |
| 3 | 🇧🇷 BR | 13885 |
| 4 | 🇦🇺 AU | 13544 |
| 5 | 🇨🇦 CA | 13177 |
| 6 | 🇮🇹 IT | 12977 |
| 7 | 🇮🇳 IN | 12494 |
| 8 | 🇩🇪 DE | 11702 |
| 9 | 🇬🇧 GB | 11191 |
| 10 | 🇨🇴 CO | 10125 |
| 11 | 🇯🇵 JP | 9626 |
| 12 | 🇫🇷 FR | 9524 |
| 13 | 🇹🇷 TR | 7058 |
| 14 | 🇬🇷 GR | 7007 |
| 15 | 🇲🇽 MX | 6603 |
| 16 | 🇨🇭 CH | 6345 |
| 17 | 🇳🇴 NO | 5874 |
| 18 | 🇹🇭 TH | 4279 |
| 19 | 🇲🇾 MY | 4257 |
| 20 | 🇿🇦 ZA | 4159 |
| 21 | 🇵🇱 PL | 3948 |
| 22 | 🇳🇿 NZ | 3290 |
| 23 | 🇵🇭 PH | 3285 |
| 24 | 🇬🇹 GT | 2978 |
| 25 | 🇰🇷 KR | 2813 |
| 26 | 🇭🇷 HR | 2743 |
| 27 | 🇲🇦 MA | 2399 |
| 28 | 🇲🇪 ME | 2212 |
| 29 | 🇳🇱 NL | 2132 |
| 30 | 🇮🇩 ID | 2084 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4936 |
| 2 | Denver International Airport |  | US | 3851 |
| 3 | Indira Gandhi International Airport |  | IN | 2905 |
| 4 | Tokyo International Airport |  | JP | 2866 |
| 5 | Guaymaral Airport |  | CO | 2689 |
| 6 | Harry Reid International Airport |  | US | 2538 |
| 7 | Zurich Airport |  | CH | 2488 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2436 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2378 |
| 10 | El Dorado International Airport |  | CO | 2278 |
| 11 | La Aurora Airport |  | GT | 2269 |
| 12 | Chicago O'Hare International Airport |  | US | 2131 |
| 13 | Salt Lake City International Airport |  | US | 2095 |
| 14 | Congonhas Airport |  | BR | 2024 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1987 |
| 16 | Frankfurt am Main International Airport |  | DE | 1883 |
| 17 | Capua Airport |  | IT | 1873 |
| 18 | Madrid Barajas International Airport |  | ES | 1866 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1794 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1752 |
| 21 | Malpensa International Airport |  | IT | 1708 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1683 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1677 |
| 24 | Charles de Gaulle International Airport |  | FR | 1649 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1591 |
| 27 | Kuala Lumpur International Airport |  | MY | 1539 |
| 28 | Charlotte/Douglas International Airport |  | US | 1529 |
| 29 | Barcelona International Airport |  | ES | 1506 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1492 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1442 |
| 32 | Viracopos International Airport |  | BR | 1418 |
| 33 | Seattle-Tacoma International Airport |  | US | 1392 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1390 |
| 35 | Bengaluru International Airport |  | IN | 1390 |
| 36 | Don Mueang International Airport |  | TH | 1384 |
| 37 | Calgary International Airport |  | CA | 1367 |
| 38 | Oslo Gardermoen Airport |  | NO | 1330 |
| 39 | Vancouver International Airport |  | CA | 1303 |
| 40 | O. R. Tambo International Airport |  | ZA | 1293 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1089 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 876 | 21m | 244 km | 3,688.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 609 | 24m | 225 km | 2,362.6 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 605 | 1h 6m | 770 km | 8,037.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 604 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 532 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 393 | 27m | 275 km | 1,862.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 370 | 1h 50m | 1,423 km | 9,080.4 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 364 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 354 | 44m | 555 km | 3,389.7 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 344 | 44m | 241 km | 1,428.9 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 337 | 21m | 250 km | 1,455.6 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 321 | 24m | 218 km | 1,209.3 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 320 | 1h 7m | 706 km | 3,896.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 318 | 22m | 55 km | 302.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 316 | 1h 40m | 1,156 km | 6,304.1 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 296 | 19m | 99 km | 507.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 291 | 27m | 215 km | 1,077.7 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 276 | 13m | - | - |
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
| MILAN77 | MIL | Nimes-Arles-Camargue Airport (LFTW) | Marseille Provence Airport (LFML) | 2026-08-26 08:06 UTC | 2026-08-26 08:40 UTC | 34m |
| N133DB |  | Grand Junction Regional Airport (KGJT) | Westwater Airport (UT42) | 2026-08-26 07:45 UTC | 2026-08-26 08:24 UTC | 38m |
| CTM034 | CTM | Villacoublay-Velizy (BA 107) Air Base (LFPV) | Clermont-Ferrand Auvergne Airport (LFLC) | 2026-08-26 07:01 UTC | 2026-08-26 08:14 UTC | 1h 12m |
| RYR3YD | Ryanair | Newcastle Airport (EGNT) | Dublin Airport (EIDW) | 2026-08-26 07:21 UTC | 2026-08-26 08:11 UTC | 50m |
| DLH9MT | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-08-26 07:34 UTC | 2026-08-26 08:06 UTC | 31m |
| HKS79 | HKS | Humberside Airport (EGNJ) | Norwich International Airport (EGSH) | 2026-08-26 07:09 UTC | 2026-08-26 08:02 UTC | 53m |
| R20576 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-26 05:41 UTC | 2026-08-26 07:58 UTC | 2h 16m |
| QTR83B | Qatar Airways | Jomo Kenyatta International Airport (HKJK) | Hamad International Airport (OTHH) | 2026-08-25 22:43 UTC | 2026-08-26 07:54 UTC | 9h 10m |
| SWR138 | Swiss International | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-08-25 20:49 UTC | 2026-08-26 07:51 UTC | 11h 2m |
| BPO807 | BPO | Neumunster Airport (EDHN) | Nordholz Airport (ETMN) | 2026-08-26 07:30 UTC | 2026-08-26 07:51 UTC | 21m |
| SAS62Y | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Gallivare Airport (ESNG) | 2026-08-26 06:36 UTC | 2026-08-26 07:49 UTC | 1h 12m |
| NOZ44A | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-08-26 07:10 UTC | 2026-08-26 07:48 UTC | 37m |
| EIN151 | Aer Lingus | London Heathrow Airport (EGLL) | Dublin Airport (EIDW) | 2026-08-26 06:51 UTC | 2026-08-26 07:47 UTC | 55m |
|  |  | Chennai International Airport (VOMM) | Zhuhai Airport (ZGSD) | 2026-08-26 03:03 UTC | 2026-08-26 07:46 UTC | 4h 43m |
| DAL176 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | Dublin Airport (EIDW) | 2026-08-26 00:35 UTC | 2026-08-26 07:44 UTC | 7h 9m |
| WMT6PG | WMT | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Cairo West Airport (HECW) | 2026-08-26 04:42 UTC | 2026-08-26 07:41 UTC | 2h 58m |
| AEE4SR | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-26 07:19 UTC | 2026-08-26 07:41 UTC | 21m |
| LION54 | LIO | St. Johann In Tirol Airport (LOIJ) | Innsbruck Airport (LOWI) | 2026-08-26 07:11 UTC | 2026-08-26 07:38 UTC | 27m |
| WMT5604 | WMT | Memmingen Allgau Airport (EDJA) | Sibiu International Airport (LRSB) | 2026-08-26 06:21 UTC | 2026-08-26 07:37 UTC | 1h 16m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Brunei International Airport (WBSB) | 2026-08-26 07:20 UTC | 2026-08-26 07:37 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
