# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_12:53:40_UTC-green)

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

**Latest saved flight:** 2026-08-19 12:53:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 12:53:40 UTC

- **215,372** saved flights
- **67,980** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **215,372** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,591,892.5 tonnes** estimated CO2 emissions
- **150,254,637 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8594 |
| 2 | SkyWest Airlines | 7696 |
| 3 | EJA | 4184 |
| 4 | IndiGo | 3680 |
| 5 | American Airlines | 3584 |
| 6 | Southwest Airlines | 3430 |
| 7 | Delta Air Lines | 2768 |
| 8 | ENY | 2660 |
| 9 | LATAM Airlines | 2033 |
| 10 | AZU | 1966 |
| 11 | Vueling | 1813 |
| 12 | Lufthansa | 1804 |
| 13 | WIF | 1725 |
| 14 | LXJ | 1695 |
| 15 | easyJet | 1495 |
| 16 | Swiss International | 1435 |
| 17 | AXM | 1416 |
| 18 | United Airlines | 1362 |
| 19 | QLK | 1346 |
| 20 | EJU | 1336 |
| 21 | Alaska Airlines | 1324 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1183 |
| 24 | PGT | 1170 |
| 25 | Air France | 1164 |
| 26 | GLO | 1164 |
| 27 | WMT | 1120 |
| 28 | JetBlue | 1092 |
| 29 | Wizz Air | 1090 |
| 30 | AEE | 1083 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181502 |
| 2 | 🇪🇸 ES | 13804 |
| 3 | 🇧🇷 BR | 12374 |
| 4 | 🇦🇺 AU | 12161 |
| 5 | 🇨🇦 CA | 11863 |
| 6 | 🇮🇳 IN | 11460 |
| 7 | 🇮🇹 IT | 11397 |
| 8 | 🇩🇪 DE | 10678 |
| 9 | 🇬🇧 GB | 10077 |
| 10 | 🇯🇵 JP | 8868 |
| 11 | 🇨🇴 CO | 8765 |
| 12 | 🇫🇷 FR | 8589 |
| 13 | 🇬🇷 GR | 6315 |
| 14 | 🇹🇷 TR | 6187 |
| 15 | 🇲🇽 MX | 6023 |
| 16 | 🇨🇭 CH | 5720 |
| 17 | 🇳🇴 NO | 5352 |
| 18 | 🇲🇾 MY | 3741 |
| 19 | 🇿🇦 ZA | 3654 |
| 20 | 🇵🇱 PL | 3551 |
| 21 | 🇹🇭 TH | 3519 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2894 |
| 24 | 🇬🇹 GT | 2732 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2357 |
| 27 | 🇲🇦 MA | 2167 |
| 28 | 🇳🇱 NL | 1920 |
| 29 | 🇲🇪 ME | 1872 |
| 30 | 🇮🇩 ID | 1813 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4516 |
| 2 | Denver International Airport |  | US | 3508 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2618 |
| 5 | Guaymaral Airport |  | CO | 2561 |
| 6 | Harry Reid International Airport |  | US | 2398 |
| 7 | Zurich Airport |  | CH | 2238 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2212 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2207 |
| 10 | La Aurora Airport |  | GT | 2077 |
| 11 | El Dorado International Airport |  | CO | 2005 |
| 12 | Chicago O'Hare International Airport |  | US | 1979 |
| 13 | Salt Lake City International Airport |  | US | 1900 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1889 |
| 15 | Congonhas Airport |  | BR | 1802 |
| 16 | Frankfurt am Main International Airport |  | DE | 1764 |
| 17 | Madrid Barajas International Airport |  | ES | 1681 |
| 18 | Capua Airport |  | IT | 1637 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1617 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1605 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1577 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 24 | Malpensa International Airport |  | IT | 1509 |
| 25 | Charles de Gaulle International Airport |  | FR | 1481 |
| 26 | Charlotte/Douglas International Airport |  | US | 1448 |
| 27 | Kuala Lumpur International Airport |  | MY | 1377 |
| 28 | Ninoy Aquino International Airport |  | PH | 1374 |
| 29 | Barcelona International Airport |  | ES | 1320 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1319 |
| 31 | Bengaluru International Airport |  | IN | 1313 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1288 |
| 33 | Seattle-Tacoma International Airport |  | US | 1281 |
| 34 | Viracopos International Airport |  | BR | 1257 |
| 35 | Calgary International Airport |  | CA | 1217 |
| 36 | Oslo Gardermoen Airport |  | NO | 1196 |
| 37 | Vitoria/Foronda Airport |  | ES | 1191 |
| 38 | Reno/Tahoe International Airport |  | US | 1164 |
| 39 | Don Mueang International Airport |  | TH | 1163 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1163 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1047 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 769 | 21m | 244 km | 3,238.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 483 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 460 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 358 | 27m | 275 km | 1,696.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 316 | 1h 49m | 1,423 km | 7,755.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 315 | 44m | 241 km | 1,308.4 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 282 | 21m | 250 km | 1,218.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 268 | 1h 38m | 1,156 km | 5,346.5 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 267 | 19m | 99 km | 457.4 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 263 | 27m | 215 km | 974.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 254 | 1h 14m | 961 km | 4,210.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 254 | 13m | - | - |
| 23 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 252 | 31m | 369 km | 1,604.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 246 | 19m | 144 km | 611.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 231 | 44m | 555 km | 2,211.9 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 231 | 1h 49m | 1,304 km | 5,196.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N138BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-08-19 12:23 UTC | 2026-08-19 12:53 UTC | 30m |
| LZB977 | LZB | Sofia Airport (LBSF) | Gorna Oryahovitsa Airport (LBGO) | 2026-08-19 12:12 UTC | 2026-08-19 12:51 UTC | 39m |
| EJU52UH | EJU | Francisco de Sá Carneiro Airport (LPPR) | Dittingen Airport (LSPD) | 2026-08-19 10:26 UTC | 2026-08-19 12:51 UTC | 2h 25m |
| N44AE |  | Fort Worth Meacham International Airport (KFTW) | Fort Worth Meacham International Airport (KFTW) | 2026-08-19 12:14 UTC | 2026-08-19 12:49 UTC | 34m |
| EOK305 | EOK | Kansai International Airport (RJBB) | Yecheon Airport (RKTY) | 2026-08-19 11:47 UTC | 2026-08-19 12:48 UTC | 1h 1m |
| N9371Y |  | Walnut Ridge Regional Airport (KARG) | Jonesboro Municipal Airport (KJBR) | 2026-08-19 11:58 UTC | 2026-08-19 12:46 UTC | 47m |
| N1723A |  | Cobb County International/Mccollum Field (KRYY) | Cartersville Airport (KVPC) | 2026-08-19 11:56 UTC | 2026-08-19 12:46 UTC | 49m |
| IFJ39D | IFJ | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-08-19 12:28 UTC | 2026-08-19 12:45 UTC | 16m |
| N926JA |  | Republic Airport (KFRG) | Republic Airport (KFRG) | 2026-08-19 11:10 UTC | 2026-08-19 12:41 UTC | 1h 31m |
| N99347 |  | Pensacola International Airport (KPNS) | Mc Kinnon Airpark (48FL) | 2026-08-19 12:13 UTC | 2026-08-19 12:41 UTC | 28m |
| N15760 |  | Chester Airport (KSNC) | Chester Airport (KSNC) | 2026-08-19 12:22 UTC | 2026-08-19 12:41 UTC | 19m |
| N441VP |  | Northwest Arkansas Ntl Airport (KXNA) | Belleview Landing Airport (45OK) | 2026-08-19 12:08 UTC | 2026-08-19 12:40 UTC | 32m |
| PGT1917 | PGT | Ercan International Airport (LCEN) | Zafer Airport (LTBZ) | 2026-08-19 11:55 UTC | 2026-08-19 12:39 UTC | 44m |
| PGT49W | PGT | Gaziemir Airport (LTBK) | Zafer Airport (LTBZ) | 2026-08-19 12:14 UTC | 2026-08-19 12:37 UTC | 23m |
| RYR21WJ | Ryanair | Dublin Airport (EIDW) | Manchester Airport (EGCC) | 2026-08-19 11:32 UTC | 2026-08-19 12:36 UTC | 1h 4m |
| AFR85ZQ | Air France | Bergen Airport Flesland (ENBR) | Charles de Gaulle International Airport (LFPG) | 2026-08-19 10:35 UTC | 2026-08-19 12:35 UTC | 1h 59m |
| N12JK |  | Lovell Field (KCHA) | Lovell Field (KCHA) | 2026-08-19 12:18 UTC | 2026-08-19 12:31 UTC | 13m |
| N584SF |  | Denton Enterprise Airport (KDTO) | Gainesville Municipal Airport (KGLE) | 2026-08-19 11:32 UTC | 2026-08-19 12:29 UTC | 56m |
| N300PL |  | Anoka County/Blaine (Janes Field) Airport (KANE) | Cox-Coyour Memorial Field (59MN) | 2026-08-19 11:33 UTC | 2026-08-19 12:27 UTC | 54m |
| WMT524 | WMT | Cluj-Napoca International Airport (LRCL) | Cardak Airport (LTAY) | 2026-08-19 11:10 UTC | 2026-08-19 12:27 UTC | 1h 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
