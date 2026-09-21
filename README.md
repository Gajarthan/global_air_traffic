# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_10:41:25_UTC-green)

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

**Latest saved flight:** 2026-09-21 10:41:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-21 10:41:25 UTC

- **265,375** saved flights
- **78,198** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **265,375** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,217,102.2 tonnes** estimated CO2 emissions
- **186,498,676 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10503 |
| 2 | SkyWest Airlines | 9229 |
| 3 | EJA | 5156 |
| 4 | IndiGo | 4462 |
| 5 | American Airlines | 4144 |
| 6 | Southwest Airlines | 3907 |
| 7 | Delta Air Lines | 3303 |
| 8 | ENY | 3125 |
| 9 | LATAM Airlines | 2557 |
| 10 | AZU | 2498 |
| 11 | Vueling | 2228 |
| 12 | WIF | 2146 |
| 13 | LXJ | 2082 |
| 14 | Lufthansa | 2038 |
| 15 | easyJet | 1786 |
| 16 | Swiss International | 1751 |
| 17 | QLK | 1716 |
| 18 | EJU | 1677 |
| 19 | AXM | 1664 |
| 20 | United Airlines | 1626 |
| 21 | Alaska Airlines | 1571 |
| 22 | All Nippon Airways | 1530 |
| 23 | WMT | 1492 |
| 24 | PGT | 1491 |
| 25 | GLO | 1478 |
| 26 | Air France | 1455 |
| 27 | VIV | 1450 |
| 28 | Wizz Air | 1443 |
| 29 | CXK | 1284 |
| 30 | AEE | 1283 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 220502 |
| 2 | 🇪🇸 ES | 16693 |
| 3 | 🇧🇷 BR | 15528 |
| 4 | 🇦🇺 AU | 15208 |
| 5 | 🇨🇦 CA | 14766 |
| 6 | 🇮🇹 IT | 14456 |
| 7 | 🇮🇳 IN | 14103 |
| 8 | 🇩🇪 DE | 12795 |
| 9 | 🇬🇧 GB | 12311 |
| 10 | 🇨🇴 CO | 12066 |
| 11 | 🇫🇷 FR | 10597 |
| 12 | 🇯🇵 JP | 10244 |
| 13 | 🇹🇷 TR | 8035 |
| 14 | 🇬🇷 GR | 7687 |
| 15 | 🇲🇽 MX | 7301 |
| 16 | 🇨🇭 CH | 7080 |
| 17 | 🇳🇴 NO | 6557 |
| 18 | 🇹🇭 TH | 4765 |
| 19 | 🇲🇾 MY | 4487 |
| 20 | 🇿🇦 ZA | 4458 |
| 21 | 🇵🇱 PL | 4365 |
| 22 | 🇳🇿 NZ | 3689 |
| 23 | 🇵🇭 PH | 3529 |
| 24 | 🇬🇹 GT | 3377 |
| 25 | 🇭🇷 HR | 3027 |
| 26 | 🇰🇷 KR | 3008 |
| 27 | 🇲🇦 MA | 2653 |
| 28 | 🇲🇪 ME | 2487 |
| 29 | 🇳🇱 NL | 2379 |
| 30 | 🇮🇩 ID | 2222 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5411 |
| 2 | Denver International Airport |  | US | 4297 |
| 3 | Indira Gandhi International Airport |  | IN | 3191 |
| 4 | Tokyo International Airport |  | JP | 3062 |
| 5 | El Dorado International Airport |  | CO | 2832 |
| 6 | Harry Reid International Airport |  | US | 2832 |
| 7 | Guaymaral Airport |  | CO | 2788 |
| 8 | Zurich Airport |  | CH | 2760 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2661 |
| 10 | La Aurora Airport |  | GT | 2565 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2563 |
| 12 | Salt Lake City International Airport |  | US | 2346 |
| 13 | Chicago O'Hare International Airport |  | US | 2278 |
| 14 | Congonhas Airport |  | BR | 2262 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2172 |
| 16 | Capua Airport |  | IT | 2080 |
| 17 | Madrid Barajas International Airport |  | ES | 2047 |
| 18 | Frankfurt am Main International Airport |  | DE | 2022 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2004 |
| 20 | Malpensa International Airport |  | IT | 1918 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1897 |
| 22 | Charles de Gaulle International Airport |  | FR | 1879 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1869 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1850 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1807 |
| 26 | Macau International Airport |  | MO | 1767 |
| 27 | Ninoy Aquino International Airport |  | PH | 1733 |
| 28 | Barcelona International Airport |  | ES | 1657 |
| 29 | Charlotte/Douglas International Airport |  | US | 1656 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1636 |
| 31 | Viracopos International Airport |  | BR | 1610 |
| 32 | Kuala Lumpur International Airport |  | MY | 1609 |
| 33 | Seattle-Tacoma International Airport |  | US | 1558 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1548 |
| 35 | Calgary International Airport |  | CA | 1515 |
| 36 | Don Mueang International Airport |  | TH | 1513 |
| 37 | Bengaluru International Airport |  | IN | 1501 |
| 38 | Oslo Gardermoen Airport |  | NO | 1493 |
| 39 | Vancouver International Airport |  | CA | 1484 |
| 40 | Antalya International Airport |  | TR | 1422 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1114 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 992 | 21m | 244 km | 4,177.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 730 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 667 | 1h 6m | 770 km | 8,860.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 661 | 24m | 225 km | 2,564.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 592 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 438 | 44m | 555 km | 4,194.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 420 | 1h 50m | 1,423 km | 10,307.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 404 | 44m | 241 km | 1,678.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 380 | 24m | 218 km | 1,431.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 339 | 12m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 335 | 1h 6m | 706 km | 4,078.6 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 331 | 13m | - | - |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 329 | 26m | 215 km | 1,218.5 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 309 | 19m | 144 km | 768.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 288 | 1h 50m | 1,304 km | 6,479.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 287 | 42m | 535 km | 2,650.6 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 272 | 18m | 14 km | 68.0 t |
| 29 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SYS300 | SYS | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-09-21 09:11 UTC | 2026-09-21 10:41 UTC | 1h 30m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-09-21 09:43 UTC | 2026-09-21 10:35 UTC | 51m |
| UAE9836 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-09-21 03:20 UTC | 2026-09-21 10:31 UTC | 7h 11m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-09-20 19:21 UTC | 2026-09-21 10:23 UTC | 15h 1m |
| N492LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-09-21 07:55 UTC | 2026-09-21 10:15 UTC | 2h 19m |
| HNL24B | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-09-21 09:46 UTC | 2026-09-21 10:13 UTC | 26m |
| NVD8524 | NVD | Antalya International Airport (LTAI) | Vilnius International Airport (EYVI) | 2026-09-21 07:09 UTC | 2026-09-21 10:11 UTC | 3h 1m |
| UBA582 | UBA | Monywar Airport (VYMY) | Phonngbyin Airport (VYPB) | 2026-09-21 09:37 UTC | 2026-09-21 10:07 UTC | 29m |
| 8QMAH |  | Dharavandhoo Airport (VRMD) | Dharavandhoo Airport (VRMD) | 2026-09-21 10:03 UTC | 2026-09-21 10:07 UTC | 4m |
| IFJ42B | IFJ | Viseu Airport (LPVZ) | Braga Municipal Aerodrome (LPBR) | 2026-09-21 09:22 UTC | 2026-09-21 10:03 UTC | 40m |
| FWWHY | FWW | Aix-en-Provence (BA 114) Airport (LFMA) | Aix-en-Provence (BA 114) Airport (LFMA) | 2026-09-21 09:57 UTC | 2026-09-21 10:00 UTC | 3m |
| AFR11ZB | Air France | Charles de Gaulle International Airport (LFPG) | Stockholm-Arlanda Airport (ESSA) | 2026-09-21 07:32 UTC | 2026-09-21 09:58 UTC | 2h 25m |
| BAW385 | British Airways | Melsbroek Air Base (EBMB) | London Heathrow Airport (EGLL) | 2026-09-21 09:12 UTC | 2026-09-21 09:56 UTC | 43m |
| AFR32GL | Air France | Charles de Gaulle International Airport (LFPG) | Budapest Ferenc Liszt International Airport (LHBP) | 2026-09-21 08:09 UTC | 2026-09-21 09:50 UTC | 1h 40m |
| BHA707 | BHA | Tribhuvan International Airport (VNKT) | Rajbiraj Airport (VNRB) | 2026-09-21 09:20 UTC | 2026-09-21 09:49 UTC | 28m |
| QLK1581 | QLK | Sunshine Coast Airport (YBMC) | Sydney Kingsford Smith International Airport (YSSY) | 2026-09-21 08:12 UTC | 2026-09-21 09:49 UTC | 1h 36m |
| RSC88AZ | RSC | Tenerife Norte Airport (GCXO) | La Gomera Airport (GCGM) | 2026-09-21 09:36 UTC | 2026-09-21 09:48 UTC | 12m |
| IGO1631 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Naypyidaw Airport (VYEL) | 2026-09-21 08:50 UTC | 2026-09-21 09:46 UTC | 56m |
| SWR97Q | Swiss International | Bologna / Borgo Panigale Airport (LIPE) | Zurich Airport (LSZH) | 2026-09-21 08:48 UTC | 2026-09-21 09:44 UTC | 55m |
| CWA921 | CWA | Edmonton International Airport (CYEG) | St. Paul Airport (CEW3) | 2026-09-21 09:19 UTC | 2026-09-21 09:44 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
