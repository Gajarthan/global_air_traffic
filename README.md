# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_16:49:43_UTC-green)

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

**Latest saved flight:** 2026-09-17 16:49:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-17 16:49:43 UTC

- **261,338** saved flights
- **77,404** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **261,338** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,164,872.5 tonnes** estimated CO2 emissions
- **183,470,872 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10351 |
| 2 | SkyWest Airlines | 9100 |
| 3 | EJA | 5063 |
| 4 | IndiGo | 4385 |
| 5 | American Airlines | 4104 |
| 6 | Southwest Airlines | 3839 |
| 7 | Delta Air Lines | 3264 |
| 8 | ENY | 3089 |
| 9 | LATAM Airlines | 2520 |
| 10 | AZU | 2452 |
| 11 | Vueling | 2202 |
| 12 | WIF | 2106 |
| 13 | LXJ | 2042 |
| 14 | Lufthansa | 2028 |
| 15 | easyJet | 1770 |
| 16 | Swiss International | 1734 |
| 17 | QLK | 1688 |
| 18 | AXM | 1651 |
| 19 | EJU | 1648 |
| 20 | United Airlines | 1605 |
| 21 | Alaska Airlines | 1550 |
| 22 | All Nippon Airways | 1515 |
| 23 | WMT | 1474 |
| 24 | PGT | 1458 |
| 25 | GLO | 1457 |
| 26 | Air France | 1435 |
| 27 | VIV | 1430 |
| 28 | Wizz Air | 1418 |
| 29 | TKR | 1274 |
| 30 | AEE | 1264 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 217015 |
| 2 | 🇪🇸 ES | 16521 |
| 3 | 🇧🇷 BR | 15293 |
| 4 | 🇦🇺 AU | 14968 |
| 5 | 🇨🇦 CA | 14558 |
| 6 | 🇮🇹 IT | 14228 |
| 7 | 🇮🇳 IN | 13830 |
| 8 | 🇩🇪 DE | 12663 |
| 9 | 🇬🇧 GB | 12150 |
| 10 | 🇨🇴 CO | 11772 |
| 11 | 🇫🇷 FR | 10465 |
| 12 | 🇯🇵 JP | 10153 |
| 13 | 🇹🇷 TR | 7893 |
| 14 | 🇬🇷 GR | 7586 |
| 15 | 🇲🇽 MX | 7195 |
| 16 | 🇨🇭 CH | 6997 |
| 17 | 🇳🇴 NO | 6451 |
| 18 | 🇹🇭 TH | 4684 |
| 19 | 🇲🇾 MY | 4450 |
| 20 | 🇿🇦 ZA | 4420 |
| 21 | 🇵🇱 PL | 4317 |
| 22 | 🇳🇿 NZ | 3621 |
| 23 | 🇵🇭 PH | 3494 |
| 24 | 🇬🇹 GT | 3331 |
| 25 | 🇭🇷 HR | 2988 |
| 26 | 🇰🇷 KR | 2980 |
| 27 | 🇲🇦 MA | 2616 |
| 28 | 🇲🇪 ME | 2461 |
| 29 | 🇳🇱 NL | 2334 |
| 30 | 🇮🇩 ID | 2208 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5354 |
| 2 | Denver International Airport |  | US | 4223 |
| 3 | Indira Gandhi International Airport |  | IN | 3145 |
| 4 | Tokyo International Airport |  | JP | 3030 |
| 5 | Guaymaral Airport |  | CO | 2777 |
| 6 | Harry Reid International Airport |  | US | 2775 |
| 7 | El Dorado International Airport |  | CO | 2747 |
| 8 | Zurich Airport |  | CH | 2730 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2630 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2537 |
| 11 | La Aurora Airport |  | GT | 2528 |
| 12 | Salt Lake City International Airport |  | US | 2306 |
| 13 | Chicago O'Hare International Airport |  | US | 2260 |
| 14 | Congonhas Airport |  | BR | 2232 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2132 |
| 16 | Capua Airport |  | IT | 2041 |
| 17 | Madrid Barajas International Airport |  | ES | 2024 |
| 18 | Frankfurt am Main International Airport |  | DE | 1998 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1970 |
| 20 | Malpensa International Airport |  | IT | 1883 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1876 |
| 22 | Charles de Gaulle International Airport |  | FR | 1848 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1843 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1795 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1788 |
| 26 | Macau International Airport |  | MO | 1733 |
| 27 | Ninoy Aquino International Airport |  | PH | 1714 |
| 28 | Barcelona International Airport |  | ES | 1631 |
| 29 | Charlotte/Douglas International Airport |  | US | 1628 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1607 |
| 31 | Kuala Lumpur International Airport |  | MY | 1597 |
| 32 | Viracopos International Airport |  | BR | 1584 |
| 33 | Seattle-Tacoma International Airport |  | US | 1530 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1522 |
| 35 | Don Mueang International Airport |  | TH | 1495 |
| 36 | Calgary International Airport |  | CA | 1492 |
| 37 | Bengaluru International Airport |  | IN | 1484 |
| 38 | Oslo Gardermoen Airport |  | NO | 1469 |
| 39 | Vancouver International Airport |  | CA | 1465 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1401 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1112 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 975 | 21m | 244 km | 4,105.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 708 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 656 | 1h 6m | 770 km | 8,714.5 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 653 | 24m | 225 km | 2,533.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 585 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 424 | 27m | 275 km | 2,009.2 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 423 | 44m | 555 km | 4,050.4 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 398 | 44m | 241 km | 1,653.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 368 | 24m | 218 km | 1,386.4 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 359 | 21m | 250 km | 1,550.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 329 | 1h 6m | 706 km | 4,005.6 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 327 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 323 | 26m | 215 km | 1,196.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 320 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 302 | 1h 14m | 961 km | 5,005.8 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 301 | 19m | 144 km | 748.7 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 282 | 1h 50m | 1,304 km | 6,344.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 278 | 42m | 535 km | 2,567.5 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 278 | 28m | 152 km | 726.5 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N733NV |  | Pearson Field (KVUO) | Pearson Field (KVUO) | 2026-09-17 16:36 UTC | 2026-09-17 16:49 UTC | 13m |
| AIC4JC | Air India | Dabolim Airport (VOGO) | Pune Airport (VAPO) | 2026-09-17 16:02 UTC | 2026-09-17 16:42 UTC | 40m |
| N628SR |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-09-17 16:06 UTC | 2026-09-17 16:42 UTC | 36m |
| SNAKE1 | SNA | 4XA5 (4XA5) | Jones Farm Field (OK12) | 2026-09-17 16:17 UTC | 2026-09-17 16:41 UTC | 23m |
| N216RF |  | Spirit Of St Louis Airport (KSUS) | Buffalo Municipal Airport (KH17) | 2026-09-17 15:18 UTC | 2026-09-17 16:40 UTC | 1h 21m |
| N738BG |  | Burlington/Alamance Regional Airport (KBUY) | Burlington/Alamance Regional Airport (KBUY) | 2026-09-17 15:51 UTC | 2026-09-17 16:39 UTC | 47m |
| ATG9720 | ATG | Ben Gurion International Airport (LLBG) | Macau International Airport (VMMC) | 2026-09-17 06:31 UTC | 2026-09-17 16:37 UTC | 10h 5m |
| FXC22 | FXC | Bridgeport/Sikorsky Airport (KBDR) | Laguardia Airport (KLGA) | 2026-09-17 16:16 UTC | 2026-09-17 16:37 UTC | 21m |
| N977DT |  | Midland International Air And Space Port Airport (KMAF) | 81NM (81NM) | 2026-09-17 16:05 UTC | 2026-09-17 16:35 UTC | 30m |
| N174EM |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-09-17 15:39 UTC | 2026-09-17 16:31 UTC | 51m |
| N462CB |  | Hollywood Burbank Airport (KBUR) | Beryl Junction Airport (UT82) | 2026-09-17 15:40 UTC | 2026-09-17 16:27 UTC | 47m |
| EPI619 | EPI | North Texas Regional/Perrin Field (KGYI) | TX68 (TX68) | 2026-09-17 15:51 UTC | 2026-09-17 16:24 UTC | 32m |
| N342T |  | K00V (K00V) | Limon Municipal Airport (KLIC) | 2026-09-17 15:46 UTC | 2026-09-17 16:23 UTC | 37m |
| SAZ53 | SAZ | Ostersund Airport (ESNZ) | Raron Airport (LSTA) | 2026-09-17 13:40 UTC | 2026-09-17 16:23 UTC | 2h 43m |
| N498SB |  | Cameron Ranch Airport (TE97) | Navajo Lake Airport (K1V0) | 2026-09-17 14:57 UTC | 2026-09-17 16:22 UTC | 1h 25m |
| NIKE46 | NIK | Mesa Verde Ranch Strip (7NM1) | Ohkay Owingeh Airport (KE14) | 2026-09-17 15:36 UTC | 2026-09-17 16:22 UTC | 46m |
| EJA635 | EJA | Sacramento Executive Airport (KSAC) | 51CO (51CO) | 2026-09-17 14:55 UTC | 2026-09-17 16:22 UTC | 1h 27m |
| MAS194 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Pune Airport (VAPO) | 2026-09-17 11:58 UTC | 2026-09-17 16:21 UTC | 4h 22m |
| N7857G |  | 2 X 4 Ranch Airport (NM47) | 2 X 4 Ranch Airport (NM47) | 2026-09-17 16:18 UTC | 2026-09-17 16:21 UTC | 3m |
| N350TF |  | Riverside Airport (KRAL) | Flagstaff Pulliam Airport (KFLG) | 2026-09-17 14:22 UTC | 2026-09-17 16:19 UTC | 1h 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
