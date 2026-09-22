# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_23:24:21_UTC-green)

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

**Latest saved flight:** 2026-09-22 23:24:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-22 23:24:21 UTC

- **266,796** saved flights
- **78,459** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **266,796** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,235,915.5 tonnes** estimated CO2 emissions
- **187,589,305 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10539 |
| 2 | SkyWest Airlines | 9286 |
| 3 | EJA | 5190 |
| 4 | IndiGo | 4474 |
| 5 | American Airlines | 4161 |
| 6 | Southwest Airlines | 3927 |
| 7 | Delta Air Lines | 3320 |
| 8 | ENY | 3139 |
| 9 | LATAM Airlines | 2575 |
| 10 | AZU | 2508 |
| 11 | Vueling | 2239 |
| 12 | WIF | 2161 |
| 13 | LXJ | 2095 |
| 14 | Lufthansa | 2039 |
| 15 | easyJet | 1792 |
| 16 | Swiss International | 1758 |
| 17 | QLK | 1722 |
| 18 | EJU | 1684 |
| 19 | AXM | 1667 |
| 20 | United Airlines | 1637 |
| 21 | Alaska Airlines | 1576 |
| 22 | All Nippon Airways | 1536 |
| 23 | PGT | 1504 |
| 24 | WMT | 1498 |
| 25 | GLO | 1491 |
| 26 | Air France | 1467 |
| 27 | VIV | 1460 |
| 28 | Wizz Air | 1450 |
| 29 | CXK | 1298 |
| 30 | AEE | 1285 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 221819 |
| 2 | 🇪🇸 ES | 16763 |
| 3 | 🇧🇷 BR | 15624 |
| 4 | 🇦🇺 AU | 15279 |
| 5 | 🇨🇦 CA | 14872 |
| 6 | 🇮🇹 IT | 14504 |
| 7 | 🇮🇳 IN | 14153 |
| 8 | 🇩🇪 DE | 12834 |
| 9 | 🇬🇧 GB | 12374 |
| 10 | 🇨🇴 CO | 12184 |
| 11 | 🇫🇷 FR | 10649 |
| 12 | 🇯🇵 JP | 10271 |
| 13 | 🇹🇷 TR | 8084 |
| 14 | 🇬🇷 GR | 7717 |
| 15 | 🇲🇽 MX | 7357 |
| 16 | 🇨🇭 CH | 7114 |
| 17 | 🇳🇴 NO | 6604 |
| 18 | 🇹🇭 TH | 4784 |
| 19 | 🇲🇾 MY | 4496 |
| 20 | 🇿🇦 ZA | 4470 |
| 21 | 🇵🇱 PL | 4382 |
| 22 | 🇳🇿 NZ | 3711 |
| 23 | 🇵🇭 PH | 3539 |
| 24 | 🇬🇹 GT | 3386 |
| 25 | 🇭🇷 HR | 3038 |
| 26 | 🇰🇷 KR | 3020 |
| 27 | 🇲🇦 MA | 2663 |
| 28 | 🇲🇪 ME | 2500 |
| 29 | 🇳🇱 NL | 2387 |
| 30 | 🇮🇩 ID | 2226 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5440 |
| 2 | Denver International Airport |  | US | 4334 |
| 3 | Indira Gandhi International Airport |  | IN | 3203 |
| 4 | Tokyo International Airport |  | JP | 3070 |
| 5 | El Dorado International Airport |  | CO | 2871 |
| 6 | Harry Reid International Airport |  | US | 2853 |
| 7 | Guaymaral Airport |  | CO | 2800 |
| 8 | Zurich Airport |  | CH | 2775 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2676 |
| 10 | La Aurora Airport |  | GT | 2572 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2568 |
| 12 | Salt Lake City International Airport |  | US | 2357 |
| 13 | Chicago O'Hare International Airport |  | US | 2293 |
| 14 | Congonhas Airport |  | BR | 2275 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2180 |
| 16 | Capua Airport |  | IT | 2084 |
| 17 | Madrid Barajas International Airport |  | ES | 2052 |
| 18 | Frankfurt am Main International Airport |  | DE | 2028 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2023 |
| 20 | Malpensa International Airport |  | IT | 1923 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1904 |
| 22 | Charles de Gaulle International Airport |  | FR | 1894 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1873 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1872 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1812 |
| 26 | Macau International Airport |  | MO | 1776 |
| 27 | Ninoy Aquino International Airport |  | PH | 1737 |
| 28 | Charlotte/Douglas International Airport |  | US | 1666 |
| 29 | Barcelona International Airport |  | ES | 1664 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1654 |
| 31 | Viracopos International Airport |  | BR | 1618 |
| 32 | Kuala Lumpur International Airport |  | MY | 1610 |
| 33 | Seattle-Tacoma International Airport |  | US | 1563 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1561 |
| 35 | Calgary International Airport |  | CA | 1525 |
| 36 | Don Mueang International Airport |  | TH | 1516 |
| 37 | Bengaluru International Airport |  | IN | 1507 |
| 38 | Oslo Gardermoen Airport |  | NO | 1502 |
| 39 | Vancouver International Airport |  | CA | 1496 |
| 40 | Antalya International Airport |  | TR | 1428 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1117 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 998 | 21m | 244 km | 4,202.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 740 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 669 | 1h 6m | 770 km | 8,887.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 663 | 24m | 225 km | 2,572.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 594 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 440 | 44m | 555 km | 4,213.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 424 | 1h 50m | 1,423 km | 10,405.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 406 | 44m | 241 km | 1,686.4 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 381 | 24m | 218 km | 1,435.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 362 | 21m | 250 km | 1,563.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 352 | 23m | 55 km | 334.6 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 340 | 12m | - | - |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 336 | 1h 6m | 706 km | 4,090.8 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 334 | 13m | - | - |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 331 | 26m | 215 km | 1,225.9 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 310 | 19m | 144 km | 771.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 290 | 42m | 535 km | 2,678.3 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 282 | 18m | 14 km | 70.5 t |
| 29 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ERU392 | ERU | Daytona Beach International Airport (KDAB) | Jacksonville Executive At Craig Airport (KCRG) | 2026-09-22 22:38 UTC | 2026-09-22 23:24 UTC | 46m |
| N727LT |  | KL38 (KL38) | Harry P Williams Memorial Airport (KPTN) | 2026-09-22 22:40 UTC | 2026-09-22 23:17 UTC | 37m |
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-09-22 11:46 UTC | 2026-09-22 23:10 UTC | 11h 24m |
| N44668 |  | Westfield-Barnes Regional Airport (KBAF) | Hadley Airport (03MA) | 2026-09-22 22:30 UTC | 2026-09-22 23:09 UTC | 38m |
| N100PC |  | Homer Airport (PAHO) | Seldovia Airport (PASO) | 2026-09-22 22:48 UTC | 2026-09-22 23:02 UTC | 14m |
| N459M |  | Edmonton International Airport (CYEG) | Calgary International Airport (CYYC) | 2026-09-22 22:23 UTC | 2026-09-22 22:56 UTC | 33m |
| SLG2 | SLG | Saskatoon John G. Diefenbaker International Airport (CYXE) | Leoville Airport (CJT9) | 2026-09-22 22:29 UTC | 2026-09-22 22:56 UTC | 26m |
| MS4 |  | Skylark Airport (CA89) | Skylark Airport (CA89) | 2026-09-22 21:48 UTC | 2026-09-22 22:52 UTC | 1h 3m |
| N208GE |  | Kodiak Airport (PADQ) | Fort Jensen Airport (AK60) | 2026-09-22 22:04 UTC | 2026-09-22 22:51 UTC | 47m |
| SRG199 | SRG | Islay Airport (EGPI) | Glasgow International Airport (EGPF) | 2026-09-22 22:20 UTC | 2026-09-22 22:49 UTC | 29m |
| CUL558 | CUL | 6CL4 (6CL4) | 6CL4 (6CL4) | 2026-09-22 22:07 UTC | 2026-09-22 22:44 UTC | 36m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-09-22 11:59 UTC | 2026-09-22 22:41 UTC | 10h 41m |
| WMU79 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | Battle Creek Executive At Kellogg Field (KBTL) | 2026-09-22 21:48 UTC | 2026-09-22 22:39 UTC | 51m |
| N441JC |  | Norfolk Regional/Karl Stefan Memorial Field (KOFK) | De Ford Airport (4II0) | 2026-09-22 21:00 UTC | 2026-09-22 22:36 UTC | 1h 36m |
| EJA750 | EJA | Dallas Love Field (KDAL) | Buffalo Municipal Airport (KH17) | 2026-09-22 21:48 UTC | 2026-09-22 22:36 UTC | 47m |
| N509FG |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-09-22 21:45 UTC | 2026-09-22 22:36 UTC | 50m |
| N26ND |  | Mesa Gateway Airport (KIWA) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-22 21:10 UTC | 2026-09-22 22:35 UTC | 1h 25m |
| N441WF |  | Centennial Airport (KAPA) | Leach Airport (K1V8) | 2026-09-22 22:03 UTC | 2026-09-22 22:35 UTC | 32m |
| UAE9860 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-09-22 15:31 UTC | 2026-09-22 22:35 UTC | 7h 4m |
| N614SF |  | 21GE (21GE) | Tupelo Regional Airport (KTUP) | 2026-09-22 21:29 UTC | 2026-09-22 22:34 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
