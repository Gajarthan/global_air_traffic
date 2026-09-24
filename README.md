# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_23:05:40_UTC-green)

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

**Latest saved flight:** 2026-09-24 23:05:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-24 23:05:40 UTC

- **268,775** saved flights
- **78,876** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **268,775** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,260,917.9 tonnes** estimated CO2 emissions
- **189,038,716 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10592 |
| 2 | SkyWest Airlines | 9355 |
| 3 | EJA | 5249 |
| 4 | IndiGo | 4499 |
| 5 | American Airlines | 4181 |
| 6 | Southwest Airlines | 3950 |
| 7 | Delta Air Lines | 3345 |
| 8 | ENY | 3159 |
| 9 | LATAM Airlines | 2593 |
| 10 | AZU | 2518 |
| 11 | Vueling | 2243 |
| 12 | WIF | 2186 |
| 13 | LXJ | 2116 |
| 14 | Lufthansa | 2045 |
| 15 | easyJet | 1804 |
| 16 | Swiss International | 1761 |
| 17 | QLK | 1734 |
| 18 | EJU | 1687 |
| 19 | AXM | 1673 |
| 20 | United Airlines | 1647 |
| 21 | Alaska Airlines | 1587 |
| 22 | All Nippon Airways | 1546 |
| 23 | PGT | 1511 |
| 24 | WMT | 1502 |
| 25 | GLO | 1497 |
| 26 | Air France | 1477 |
| 27 | VIV | 1466 |
| 28 | Wizz Air | 1458 |
| 29 | CXK | 1316 |
| 30 | AEE | 1292 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 223740 |
| 2 | 🇪🇸 ES | 16848 |
| 3 | 🇧🇷 BR | 15715 |
| 4 | 🇦🇺 AU | 15461 |
| 5 | 🇨🇦 CA | 14999 |
| 6 | 🇮🇹 IT | 14557 |
| 7 | 🇮🇳 IN | 14230 |
| 8 | 🇩🇪 DE | 12901 |
| 9 | 🇬🇧 GB | 12443 |
| 10 | 🇨🇴 CO | 12299 |
| 11 | 🇫🇷 FR | 10691 |
| 12 | 🇯🇵 JP | 10332 |
| 13 | 🇹🇷 TR | 8136 |
| 14 | 🇬🇷 GR | 7769 |
| 15 | 🇲🇽 MX | 7409 |
| 16 | 🇨🇭 CH | 7144 |
| 17 | 🇳🇴 NO | 6651 |
| 18 | 🇹🇭 TH | 4805 |
| 19 | 🇲🇾 MY | 4518 |
| 20 | 🇿🇦 ZA | 4490 |
| 21 | 🇵🇱 PL | 4402 |
| 22 | 🇳🇿 NZ | 3757 |
| 23 | 🇵🇭 PH | 3558 |
| 24 | 🇬🇹 GT | 3403 |
| 25 | 🇭🇷 HR | 3060 |
| 26 | 🇰🇷 KR | 3041 |
| 27 | 🇲🇦 MA | 2681 |
| 28 | 🇲🇪 ME | 2517 |
| 29 | 🇳🇱 NL | 2405 |
| 30 | 🇮🇩 ID | 2239 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5478 |
| 2 | Denver International Airport |  | US | 4370 |
| 3 | Indira Gandhi International Airport |  | IN | 3219 |
| 4 | Tokyo International Airport |  | JP | 3091 |
| 5 | El Dorado International Airport |  | CO | 2909 |
| 6 | Harry Reid International Airport |  | US | 2880 |
| 7 | Guaymaral Airport |  | CO | 2810 |
| 8 | Zurich Airport |  | CH | 2784 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2703 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2590 |
| 11 | La Aurora Airport |  | GT | 2586 |
| 12 | Salt Lake City International Airport |  | US | 2367 |
| 13 | Chicago O'Hare International Airport |  | US | 2300 |
| 14 | Congonhas Airport |  | BR | 2288 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2198 |
| 16 | Capua Airport |  | IT | 2093 |
| 17 | Madrid Barajas International Airport |  | ES | 2069 |
| 18 | Frankfurt am Main International Airport |  | DE | 2038 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2035 |
| 20 | Malpensa International Airport |  | IT | 1926 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1918 |
| 22 | Charles de Gaulle International Airport |  | FR | 1908 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1883 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1879 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1818 |
| 26 | Macau International Airport |  | MO | 1786 |
| 27 | Ninoy Aquino International Airport |  | PH | 1746 |
| 28 | Charlotte/Douglas International Airport |  | US | 1679 |
| 29 | Barcelona International Airport |  | ES | 1672 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1663 |
| 31 | Viracopos International Airport |  | BR | 1625 |
| 32 | Kuala Lumpur International Airport |  | MY | 1617 |
| 33 | Seattle-Tacoma International Airport |  | US | 1575 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1572 |
| 35 | Calgary International Airport |  | CA | 1532 |
| 36 | Don Mueang International Airport |  | TH | 1522 |
| 37 | Bengaluru International Airport |  | IN | 1514 |
| 38 | Oslo Gardermoen Airport |  | NO | 1509 |
| 39 | Vancouver International Airport |  | CA | 1506 |
| 40 | Antalya International Airport |  | TR | 1431 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1121 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1008 | 21m | 244 km | 4,244.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 741 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 676 | 1h 6m | 770 km | 8,980.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 669 | 24m | 225 km | 2,595.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 598 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 442 | 44m | 555 km | 4,232.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 431 | 27m | 275 km | 2,042.3 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 425 | 1h 50m | 1,423 km | 10,430.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 410 | 44m | 241 km | 1,703.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 384 | 24m | 218 km | 1,446.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 364 | 21m | 250 km | 1,572.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 360 | 23m | 55 km | 342.2 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 342 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 339 | 1h 6m | 706 km | 4,127.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 338 | 19m | 99 km | 579.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 335 | 26m | 215 km | 1,240.7 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 313 | 19m | 144 km | 778.6 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 293 | 42m | 535 km | 2,706.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 287 | 18m | 14 km | 71.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 284 | 28m | 152 km | 742.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QTR8434 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-09-24 15:47 UTC | 2026-09-24 23:05 UTC | 7h 18m |
| CFXEP | CFX | Montréal (Mirabel) Airport (CYMX) | Montréal (Mirabel) Airport (CYMX) | 2026-09-24 21:53 UTC | 2026-09-24 23:03 UTC | 1h 9m |
| N38EE |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-09-24 19:07 UTC | 2026-09-24 23:02 UTC | 3h 54m |
| PRE315 | PRE | Columbus Municipal Airport (KOLU) | Rocky Mountain Metro Airport (KBJC) | 2026-09-24 21:13 UTC | 2026-09-24 23:01 UTC | 1h 47m |
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-09-24 11:36 UTC | 2026-09-24 22:54 UTC | 11h 17m |
| CGNNP | CGN | Colonial Airport (NY24) | Colonial Airport (NY24) | 2026-09-24 22:41 UTC | 2026-09-24 22:49 UTC | 8m |
| N880AF |  | Addison Airport (KADS) | Majors Airport (KGVT) | 2026-09-24 21:31 UTC | 2026-09-24 22:47 UTC | 1h 16m |
| N522JW |  | NK89 (NK89) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-09-24 22:10 UTC | 2026-09-24 22:44 UTC | 34m |
| DAL2799 | Delta Air Lines | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-09-24 21:16 UTC | 2026-09-24 22:44 UTC | 1h 28m |
| EJA819 | EJA | Teterboro Airport (KTEB) | Boire Field (KASH) | 2026-09-24 22:02 UTC | 2026-09-24 22:43 UTC | 41m |
| N9957M |  | Homer Airport (PAHO) | Seldovia Airport (PASO) | 2026-09-24 22:28 UTC | 2026-09-24 22:42 UTC | 13m |
| ICL851 | ICL | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-09-24 13:43 UTC | 2026-09-24 22:42 UTC | 8h 58m |
| GPD433 | GPD | Philadelphia International Airport (KPHL) | 8NK3 (8NK3) | 2026-09-24 21:44 UTC | 2026-09-24 22:41 UTC | 57m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Zhuhai Airport (ZGSD) | 2026-09-24 11:33 UTC | 2026-09-24 22:39 UTC | 11h 5m |
| EJA547 | EJA | Pocono Mountains Regional Airport (KMPO) | Lehigh Valley International Airport (KABE) | 2026-09-24 22:20 UTC | 2026-09-24 22:39 UTC | 18m |
| N110CT |  | Capital City Airport (KCXY) | Capital City Airport (KCXY) | 2026-09-24 22:37 UTC | 2026-09-24 22:38 UTC | 0m |
| BRG595 | BRG | Red Dog Airport (PADG) | Selawik Airport (PASK) | 2026-09-24 21:52 UTC | 2026-09-24 22:38 UTC | 46m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-09-24 12:05 UTC | 2026-09-24 22:37 UTC | 10h 32m |
| N277GT |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-09-24 21:54 UTC | 2026-09-24 22:37 UTC | 42m |
| NYV | NYV | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-09-24 22:13 UTC | 2026-09-24 22:35 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
