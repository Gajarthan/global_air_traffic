# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_15:47:19_UTC-green)

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

**Latest saved flight:** 2026-09-05 15:47:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-05 15:47:19 UTC

- **248,400** saved flights
- **74,795** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **248,400** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,988,674.9 tonnes** estimated CO2 emissions
- **173,256,517 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9948 |
| 2 | SkyWest Airlines | 8674 |
| 3 | EJA | 4792 |
| 4 | IndiGo | 4151 |
| 5 | American Airlines | 3977 |
| 6 | Southwest Airlines | 3695 |
| 7 | Delta Air Lines | 3154 |
| 8 | ENY | 2970 |
| 9 | LATAM Airlines | 2399 |
| 10 | AZU | 2314 |
| 11 | Vueling | 2121 |
| 12 | WIF | 1986 |
| 13 | Lufthansa | 1973 |
| 14 | LXJ | 1928 |
| 15 | easyJet | 1716 |
| 16 | Swiss International | 1666 |
| 17 | AXM | 1627 |
| 18 | EJU | 1599 |
| 19 | QLK | 1591 |
| 20 | United Airlines | 1559 |
| 21 | Alaska Airlines | 1482 |
| 22 | All Nippon Airways | 1455 |
| 23 | WMT | 1404 |
| 24 | GLO | 1386 |
| 25 | VIV | 1365 |
| 26 | PGT | 1361 |
| 27 | Air France | 1357 |
| 28 | Wizz Air | 1341 |
| 29 | JetBlue | 1222 |
| 30 | AEE | 1220 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 206009 |
| 2 | 🇪🇸 ES | 15906 |
| 3 | 🇧🇷 BR | 14531 |
| 4 | 🇦🇺 AU | 14105 |
| 5 | 🇨🇦 CA | 13798 |
| 6 | 🇮🇹 IT | 13609 |
| 7 | 🇮🇳 IN | 12946 |
| 8 | 🇩🇪 DE | 12209 |
| 9 | 🇬🇧 GB | 11669 |
| 10 | 🇨🇴 CO | 10850 |
| 11 | 🇫🇷 FR | 10007 |
| 12 | 🇯🇵 JP | 9815 |
| 13 | 🇹🇷 TR | 7399 |
| 14 | 🇬🇷 GR | 7317 |
| 15 | 🇲🇽 MX | 6872 |
| 16 | 🇨🇭 CH | 6697 |
| 17 | 🇳🇴 NO | 6155 |
| 18 | 🇹🇭 TH | 4491 |
| 19 | 🇲🇾 MY | 4362 |
| 20 | 🇿🇦 ZA | 4291 |
| 21 | 🇵🇱 PL | 4155 |
| 22 | 🇳🇿 NZ | 3397 |
| 23 | 🇵🇭 PH | 3383 |
| 24 | 🇬🇹 GT | 3102 |
| 25 | 🇰🇷 KR | 2886 |
| 26 | 🇭🇷 HR | 2855 |
| 27 | 🇲🇦 MA | 2512 |
| 28 | 🇲🇪 ME | 2323 |
| 29 | 🇳🇱 NL | 2237 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5114 |
| 2 | Denver International Airport |  | US | 4009 |
| 3 | Indira Gandhi International Airport |  | IN | 3025 |
| 4 | Tokyo International Airport |  | JP | 2928 |
| 5 | Guaymaral Airport |  | CO | 2724 |
| 6 | Harry Reid International Airport |  | US | 2650 |
| 7 | Zurich Airport |  | CH | 2598 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2524 |
| 9 | El Dorado International Airport |  | CO | 2490 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2470 |
| 11 | La Aurora Airport |  | GT | 2361 |
| 12 | Salt Lake City International Airport |  | US | 2202 |
| 13 | Chicago O'Hare International Airport |  | US | 2177 |
| 14 | Congonhas Airport |  | BR | 2137 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2045 |
| 16 | Capua Airport |  | IT | 1955 |
| 17 | Madrid Barajas International Airport |  | ES | 1949 |
| 18 | Frankfurt am Main International Airport |  | DE | 1944 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1868 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1814 |
| 21 | Malpensa International Airport |  | IT | 1787 |
| 22 | Charles de Gaulle International Airport |  | FR | 1744 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1742 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1728 |
| 25 | Ninoy Aquino International Airport |  | PH | 1647 |
| 26 | Macau International Airport |  | MO | 1638 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1629 |
| 28 | Charlotte/Douglas International Airport |  | US | 1574 |
| 29 | Barcelona International Airport |  | ES | 1573 |
| 30 | Kuala Lumpur International Airport |  | MY | 1570 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1525 |
| 32 | Viracopos International Airport |  | BR | 1483 |
| 33 | Seattle-Tacoma International Airport |  | US | 1462 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1446 |
| 35 | Don Mueang International Airport |  | TH | 1440 |
| 36 | Calgary International Airport |  | CA | 1430 |
| 37 | Bengaluru International Airport |  | IN | 1429 |
| 38 | Oslo Gardermoen Airport |  | NO | 1397 |
| 39 | Vancouver International Airport |  | CA | 1388 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1348 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 921 | 21m | 244 km | 3,878.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 655 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 629 | 24m | 225 km | 2,440.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 624 | 1h 6m | 770 km | 8,289.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 555 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 409 | 27m | 275 km | 1,938.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 397 | 1h 50m | 1,423 km | 9,743.0 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 387 | 44m | 555 km | 3,705.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 370 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 368 | 44m | 241 km | 1,528.6 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 351 | 21m | 250 km | 1,516.1 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 348 | 24m | 218 km | 1,311.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 333 | 23m | 55 km | 316.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 295 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 287 | 1h 14m | 961 km | 4,757.2 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 287 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 284 | 19m | 144 km | 706.4 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 255 | 28m | 152 km | 666.4 t |
| 30 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 254 | 41m | 535 km | 2,345.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N695ND |  | Allentown Queen City Municipal Airport (KXLL) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-09-05 15:02 UTC | 2026-09-05 15:47 UTC | 45m |
| N1044A |  | Lewis Airport (FL78) | Plant City Airport (KPCM) | 2026-09-05 15:28 UTC | 2026-09-05 15:45 UTC | 17m |
| N169PS |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-09-05 15:24 UTC | 2026-09-05 15:44 UTC | 20m |
| CKS703 | CKS | Ben Gurion International Airport (LLBG) | Macau International Airport (VMMC) | 2026-09-05 06:44 UTC | 2026-09-05 15:39 UTC | 8h 54m |
| N71560 |  | Abilene Municipal Airport (KK78) | Abilene Municipal Airport (KK78) | 2026-09-05 15:17 UTC | 2026-09-05 15:31 UTC | 13m |
| N739GY |  | Sacramento Executive Airport (KSAC) | Sacramento Executive Airport (KSAC) | 2026-09-05 15:16 UTC | 2026-09-05 15:30 UTC | 13m |
| N4014Z |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-05 15:10 UTC | 2026-09-05 15:29 UTC | 19m |
| N125PM |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-09-05 14:28 UTC | 2026-09-05 15:27 UTC | 58m |
| N8533X |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-09-05 14:59 UTC | 2026-09-05 15:24 UTC | 25m |
| N263DC |  | Ranchaero Airport (CL56) | Lincoln Regional/Karl Harder Field (KLHM) | 2026-09-05 14:42 UTC | 2026-09-05 15:23 UTC | 41m |
| N915NX |  | Santa Ynez/Kunkle Field (KIZA) | Truckee-Tahoe Airport (KTRK) | 2026-09-05 14:15 UTC | 2026-09-05 15:18 UTC | 1h 2m |
| N3040F |  | Hensley Airpark (04TN) | Greeneville Municipal Airport (KGCY) | 2026-09-05 15:05 UTC | 2026-09-05 15:16 UTC | 11m |
| N777RV |  | St George Regional Airport (KSGU) | Flagstaff Pulliam Airport (KFLG) | 2026-09-05 14:13 UTC | 2026-09-05 15:16 UTC | 1h 3m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-09-05 15:01 UTC | 2026-09-05 15:13 UTC | 12m |
| N1979B |  | Floydada Municipal Airport (K41F) | Whitfield Airport (6TX4) | 2026-09-05 15:01 UTC | 2026-09-05 15:12 UTC | 10m |
| RPB7449 | RPB | Jose Leonardo Chirinos Airport (SVCR) | Jose Maria Cordova International Airport (SKRG) | 2026-09-05 14:06 UTC | 2026-09-05 15:11 UTC | 1h 5m |
| GKAMY | GKA | Glasgow Prestwick Airport (EGPK) | Glasgow Prestwick Airport (EGPK) | 2026-09-05 15:04 UTC | 2026-09-05 15:11 UTC | 7m |
| EAI71G | EAI | Newquay Cornwall Airport (EGHQ) | Dublin Airport (EIDW) | 2026-09-05 14:11 UTC | 2026-09-05 15:09 UTC | 58m |
| CKS221 | CKS | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-09-05 04:41 UTC | 2026-09-05 15:08 UTC | 10h 27m |
| N80896 |  | Denton Enterprise Airport (KDTO) | Jim Sears Airport (3TA7) | 2026-09-05 14:44 UTC | 2026-09-05 15:08 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
