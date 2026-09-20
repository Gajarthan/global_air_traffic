# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_22:17:43_UTC-green)

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

**Latest saved flight:** 2026-09-20 22:17:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-20 22:17:43 UTC

- **265,037** saved flights
- **78,144** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **265,037** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,212,058.8 tonnes** estimated CO2 emissions
- **186,206,308 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10495 |
| 2 | SkyWest Airlines | 9214 |
| 3 | EJA | 5154 |
| 4 | IndiGo | 4449 |
| 5 | American Airlines | 4142 |
| 6 | Southwest Airlines | 3899 |
| 7 | Delta Air Lines | 3300 |
| 8 | ENY | 3121 |
| 9 | LATAM Airlines | 2556 |
| 10 | AZU | 2495 |
| 11 | Vueling | 2226 |
| 12 | WIF | 2142 |
| 13 | LXJ | 2081 |
| 14 | Lufthansa | 2037 |
| 15 | easyJet | 1785 |
| 16 | Swiss International | 1745 |
| 17 | QLK | 1709 |
| 18 | EJU | 1674 |
| 19 | AXM | 1662 |
| 20 | United Airlines | 1624 |
| 21 | Alaska Airlines | 1569 |
| 22 | All Nippon Airways | 1525 |
| 23 | WMT | 1489 |
| 24 | PGT | 1488 |
| 25 | GLO | 1478 |
| 26 | Air France | 1451 |
| 27 | VIV | 1446 |
| 28 | Wizz Air | 1440 |
| 29 | CXK | 1283 |
| 30 | AEE | 1282 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 220280 |
| 2 | 🇪🇸 ES | 16679 |
| 3 | 🇧🇷 BR | 15520 |
| 4 | 🇦🇺 AU | 15151 |
| 5 | 🇨🇦 CA | 14747 |
| 6 | 🇮🇹 IT | 14450 |
| 7 | 🇮🇳 IN | 14073 |
| 8 | 🇩🇪 DE | 12784 |
| 9 | 🇬🇧 GB | 12290 |
| 10 | 🇨🇴 CO | 12054 |
| 11 | 🇫🇷 FR | 10578 |
| 12 | 🇯🇵 JP | 10226 |
| 13 | 🇹🇷 TR | 8027 |
| 14 | 🇬🇷 GR | 7679 |
| 15 | 🇲🇽 MX | 7291 |
| 16 | 🇨🇭 CH | 7066 |
| 17 | 🇳🇴 NO | 6549 |
| 18 | 🇹🇭 TH | 4749 |
| 19 | 🇲🇾 MY | 4480 |
| 20 | 🇿🇦 ZA | 4452 |
| 21 | 🇵🇱 PL | 4363 |
| 22 | 🇳🇿 NZ | 3684 |
| 23 | 🇵🇭 PH | 3524 |
| 24 | 🇬🇹 GT | 3377 |
| 25 | 🇭🇷 HR | 3026 |
| 26 | 🇰🇷 KR | 2999 |
| 27 | 🇲🇦 MA | 2652 |
| 28 | 🇲🇪 ME | 2482 |
| 29 | 🇳🇱 NL | 2377 |
| 30 | 🇮🇩 ID | 2220 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5408 |
| 2 | Denver International Airport |  | US | 4290 |
| 3 | Indira Gandhi International Airport |  | IN | 3184 |
| 4 | Tokyo International Airport |  | JP | 3055 |
| 5 | Harry Reid International Airport |  | US | 2829 |
| 6 | El Dorado International Airport |  | CO | 2824 |
| 7 | Guaymaral Airport |  | CO | 2788 |
| 8 | Zurich Airport |  | CH | 2754 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2661 |
| 10 | La Aurora Airport |  | GT | 2565 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2563 |
| 12 | Salt Lake City International Airport |  | US | 2337 |
| 13 | Chicago O'Hare International Airport |  | US | 2275 |
| 14 | Congonhas Airport |  | BR | 2261 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2167 |
| 16 | Capua Airport |  | IT | 2078 |
| 17 | Madrid Barajas International Airport |  | ES | 2045 |
| 18 | Frankfurt am Main International Airport |  | DE | 2022 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2003 |
| 20 | Malpensa International Airport |  | IT | 1918 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1894 |
| 22 | Charles de Gaulle International Airport |  | FR | 1872 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1862 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1850 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1807 |
| 26 | Macau International Airport |  | MO | 1765 |
| 27 | Ninoy Aquino International Airport |  | PH | 1731 |
| 28 | Barcelona International Airport |  | ES | 1656 |
| 29 | Charlotte/Douglas International Airport |  | US | 1653 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1632 |
| 31 | Viracopos International Airport |  | BR | 1608 |
| 32 | Kuala Lumpur International Airport |  | MY | 1606 |
| 33 | Seattle-Tacoma International Airport |  | US | 1556 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1543 |
| 35 | Calgary International Airport |  | CA | 1512 |
| 36 | Don Mueang International Airport |  | TH | 1506 |
| 37 | Bengaluru International Airport |  | IN | 1501 |
| 38 | Oslo Gardermoen Airport |  | NO | 1492 |
| 39 | Vancouver International Airport |  | CA | 1483 |
| 40 | Antalya International Airport |  | TR | 1421 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1114 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 990 | 21m | 244 km | 4,168.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 730 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 665 | 1h 6m | 770 km | 8,834.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 659 | 24m | 225 km | 2,556.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 592 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 432 | 44m | 555 km | 4,136.6 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 420 | 1h 50m | 1,423 km | 10,307.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 404 | 44m | 241 km | 1,678.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 380 | 24m | 218 km | 1,431.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 338 | 12m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 18 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 329 | 26m | 215 km | 1,218.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 329 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 308 | 19m | 144 km | 766.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 287 | 1h 50m | 1,304 km | 6,456.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 286 | 42m | 535 km | 2,641.4 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 271 | 18m | 14 km | 67.8 t |
| 29 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N821TN |  | Kansas City Downtown/Wheeler Field (KMKC) | Jesse Viertel Memorial Airport (KVER) | 2026-09-20 22:01 UTC | 2026-09-20 22:17 UTC | 15m |
| N2818E |  | Davidson County Executive Airport (KEXX) | Quiet Acres Airport (NC31) | 2026-09-20 21:43 UTC | 2026-09-20 22:15 UTC | 31m |
| FNA77A | FNA | Kerlingafjoll Airport (BIKE) | Hvolsvollur Airport (BIHR) | 2026-09-20 21:53 UTC | 2026-09-20 22:11 UTC | 17m |
| CNK86 | CNK | Indianapolis International Airport (KIND) | Calgary International Airport (CYYC) | 2026-09-20 18:50 UTC | 2026-09-20 22:09 UTC | 3h 18m |
| EJA871 | EJA | TN62 (TN62) | Orlando Executive Airport (KORL) | 2026-09-20 20:53 UTC | 2026-09-20 22:08 UTC | 1h 14m |
| CPA953 | Cathay Pacific | Guangzhou Baiyun International Airport (ZGGG) | Macau International Airport (VMMC) | 2026-09-20 21:51 UTC | 2026-09-20 22:04 UTC | 12m |
| N441PN |  | Visalia Municipal Airport (KVIS) | NV13 (NV13) | 2026-09-20 21:21 UTC | 2026-09-20 22:01 UTC | 39m |
| JRE869 | JRE | Scottsdale Airport (KSDL) | Truckee-Tahoe Airport (KTRK) | 2026-09-20 20:33 UTC | 2026-09-20 22:00 UTC | 1h 27m |
| CPA395 | Cathay Pacific | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-09-20 19:24 UTC | 2026-09-20 21:59 UTC | 2h 35m |
| N227DH |  | Chapman Farms Airport (67CA) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-09-20 21:28 UTC | 2026-09-20 21:57 UTC | 29m |
|  |  | Seven Feathers Airport (10FD) | Seven Feathers Airport (10FD) | 2026-09-20 21:55 UTC | 2026-09-20 21:56 UTC | 0m |
| HCCRE | HCC | Nuevo Aeropuerto Internacional Mariscal Sucre (SEQM) | Nuevo Aeropuerto Internacional Mariscal Sucre (SEQM) | 2026-09-20 21:11 UTC | 2026-09-20 21:55 UTC | 43m |
| LBQ968 | LBQ | Reading Regional/Carl A Spaatz Field (KRDG) | Worcester Regional Airport (KORH) | 2026-09-20 20:57 UTC | 2026-09-20 21:55 UTC | 58m |
| XSN40 | XSN | Napa County Airport (KAPC) | Banning Municipal Airport (KBNG) | 2026-09-20 20:20 UTC | 2026-09-20 21:54 UTC | 1h 34m |
| N84VS |  | John C Tune Airport (KJWN) | Mason County Airport (KLDM) | 2026-09-20 20:32 UTC | 2026-09-20 21:53 UTC | 1h 21m |
| N40DA |  | San Martin Airport (KE16) | San Martin Airport (KE16) | 2026-09-20 21:12 UTC | 2026-09-20 21:53 UTC | 40m |
| N96GA |  | Harry Reid International Airport (KLAS) | Dry Pen Airport (16CO) | 2026-09-20 20:36 UTC | 2026-09-20 21:49 UTC | 1h 12m |
| ANZ266L | ANZ | Auckland International Airport (NZAA) | Kerikeri Airport (NZKK) | 2026-09-20 21:17 UTC | 2026-09-20 21:45 UTC | 27m |
| N957CR |  | Centennial Airport (KAPA) | K14F (K14F) | 2026-09-20 20:28 UTC | 2026-09-20 21:33 UTC | 1h 4m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-09-20 10:44 UTC | 2026-09-20 21:33 UTC | 10h 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
