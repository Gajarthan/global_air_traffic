# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--12_04:39:02_UTC-green)

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

**Latest saved flight:** 2026-09-12 04:39:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-12 04:39:02 UTC

- **255,750** saved flights
- **76,306** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **255,750** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,088,476.8 tonnes** estimated CO2 emissions
- **179,042,132 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10182 |
| 2 | SkyWest Airlines | 8919 |
| 3 | EJA | 4941 |
| 4 | IndiGo | 4275 |
| 5 | American Airlines | 4054 |
| 6 | Southwest Airlines | 3768 |
| 7 | Delta Air Lines | 3203 |
| 8 | ENY | 3039 |
| 9 | LATAM Airlines | 2464 |
| 10 | AZU | 2382 |
| 11 | Vueling | 2164 |
| 12 | WIF | 2053 |
| 13 | Lufthansa | 2001 |
| 14 | LXJ | 1996 |
| 15 | easyJet | 1740 |
| 16 | Swiss International | 1711 |
| 17 | QLK | 1653 |
| 18 | AXM | 1640 |
| 19 | EJU | 1629 |
| 20 | United Airlines | 1586 |
| 21 | Alaska Airlines | 1520 |
| 22 | All Nippon Airways | 1492 |
| 23 | WMT | 1444 |
| 24 | GLO | 1426 |
| 25 | PGT | 1410 |
| 26 | VIV | 1402 |
| 27 | Air France | 1395 |
| 28 | Wizz Air | 1389 |
| 29 | TKR | 1247 |
| 30 | JetBlue | 1243 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 212429 |
| 2 | 🇪🇸 ES | 16254 |
| 3 | 🇧🇷 BR | 14933 |
| 4 | 🇦🇺 AU | 14603 |
| 5 | 🇨🇦 CA | 14249 |
| 6 | 🇮🇹 IT | 13965 |
| 7 | 🇮🇳 IN | 13400 |
| 8 | 🇩🇪 DE | 12473 |
| 9 | 🇬🇧 GB | 11931 |
| 10 | 🇨🇴 CO | 11387 |
| 11 | 🇫🇷 FR | 10262 |
| 12 | 🇯🇵 JP | 10000 |
| 13 | 🇹🇷 TR | 7661 |
| 14 | 🇬🇷 GR | 7458 |
| 15 | 🇲🇽 MX | 7063 |
| 16 | 🇨🇭 CH | 6854 |
| 17 | 🇳🇴 NO | 6339 |
| 18 | 🇹🇭 TH | 4596 |
| 19 | 🇲🇾 MY | 4410 |
| 20 | 🇿🇦 ZA | 4354 |
| 21 | 🇵🇱 PL | 4236 |
| 22 | 🇳🇿 NZ | 3537 |
| 23 | 🇵🇭 PH | 3444 |
| 24 | 🇬🇹 GT | 3209 |
| 25 | 🇰🇷 KR | 2933 |
| 26 | 🇭🇷 HR | 2925 |
| 27 | 🇲🇦 MA | 2576 |
| 28 | 🇲🇪 ME | 2401 |
| 29 | 🇳🇱 NL | 2301 |
| 30 | 🇮🇩 ID | 2176 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5246 |
| 2 | Denver International Airport |  | US | 4135 |
| 3 | Indira Gandhi International Airport |  | IN | 3088 |
| 4 | Tokyo International Airport |  | JP | 2986 |
| 5 | Guaymaral Airport |  | CO | 2759 |
| 6 | Harry Reid International Airport |  | US | 2710 |
| 7 | Zurich Airport |  | CH | 2675 |
| 8 | El Dorado International Airport |  | CO | 2633 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2580 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2502 |
| 11 | La Aurora Airport |  | GT | 2443 |
| 12 | Salt Lake City International Airport |  | US | 2256 |
| 13 | Chicago O'Hare International Airport |  | US | 2227 |
| 14 | Congonhas Airport |  | BR | 2193 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2092 |
| 16 | Capua Airport |  | IT | 2013 |
| 17 | Madrid Barajas International Airport |  | ES | 1995 |
| 18 | Frankfurt am Main International Airport |  | DE | 1976 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1919 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1850 |
| 21 | Malpensa International Airport |  | IT | 1838 |
| 22 | Charles de Gaulle International Airport |  | FR | 1799 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1798 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1777 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1722 |
| 26 | Macau International Airport |  | MO | 1697 |
| 27 | Ninoy Aquino International Airport |  | PH | 1684 |
| 28 | Barcelona International Airport |  | ES | 1606 |
| 29 | Charlotte/Douglas International Airport |  | US | 1602 |
| 30 | Kuala Lumpur International Airport |  | MY | 1588 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1571 |
| 32 | Viracopos International Airport |  | BR | 1528 |
| 33 | Seattle-Tacoma International Airport |  | US | 1501 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1488 |
| 35 | Don Mueang International Airport |  | TH | 1472 |
| 36 | Calgary International Airport |  | CA | 1470 |
| 37 | Bengaluru International Airport |  | IN | 1452 |
| 38 | Oslo Gardermoen Airport |  | NO | 1445 |
| 39 | Vancouver International Airport |  | CA | 1436 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1381 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 952 | 21m | 244 km | 4,008.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 684 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 641 | 1h 6m | 770 km | 8,515.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 639 | 24m | 225 km | 2,479.0 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 573 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 416 | 27m | 275 km | 1,971.2 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 410 | 44m | 555 km | 3,925.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 406 | 1h 50m | 1,423 km | 9,963.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 386 | 44m | 241 km | 1,603.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 356 | 24m | 218 km | 1,341.2 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 342 | 23m | 55 km | 325.1 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 316 | 26m | 215 km | 1,170.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 313 | 19m | 99 km | 536.1 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 309 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 303 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 294 | 1h 14m | 961 km | 4,873.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 293 | 19m | 144 km | 728.8 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 267 | 41m | 535 km | 2,465.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 265 | 28m | 152 km | 692.5 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ETH3728 | Ethiopian Airlines | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-09-11 17:55 UTC | 2026-09-12 04:39 UTC | 10h 43m |
| TVR4719 | TVR | Ben Gurion International Airport (LLBG) | Macau International Airport (VMMC) | 2026-09-11 18:20 UTC | 2026-09-12 04:33 UTC | 10h 12m |
| AZG628 | AZG | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-09-11 17:42 UTC | 2026-09-12 04:29 UTC | 10h 47m |
|  |  | Okadama Airport (RJCO) | Okadama Airport (RJCO) | 2026-09-12 03:33 UTC | 2026-09-12 04:24 UTC | 51m |
| N803CP |  | Martin State Airport (KMTN) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-09-12 03:03 UTC | 2026-09-12 04:22 UTC | 1h 19m |
| N107UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-09-12 03:08 UTC | 2026-09-12 04:21 UTC | 1h 13m |
| N81NG |  | Cavern City Air Trml Airport (KCNM) | Grant County Airport (KSVC) | 2026-09-12 03:30 UTC | 2026-09-12 04:19 UTC | 49m |
| N113UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-09-12 03:10 UTC | 2026-09-12 04:18 UTC | 1h 8m |
| 8SC |  | Aldinga Airport (YADG) | Aldinga Airport (YADG) | 2026-09-12 03:54 UTC | 2026-09-12 04:16 UTC | 22m |
| N727HG |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | San Bernardino International Airport (KSBD) | 2026-09-12 03:38 UTC | 2026-09-12 04:09 UTC | 30m |
| LPE2080 | LPE | Malin Airport (SOML) | Paramonga Airport (SPPG) | 2026-09-12 03:44 UTC | 2026-09-12 04:08 UTC | 24m |
| N911TG |  | Brooksville-Tampa Bay Regional Airport (KBKV) | Peter O Knight Airport (KTPF) | 2026-09-12 03:46 UTC | 2026-09-12 04:07 UTC | 21m |
| VAR657 | VAR | Phoenix Goodyear Airport (KGYR) | Chiriaco Summit Airport (KL77) | 2026-09-12 02:51 UTC | 2026-09-12 04:07 UTC | 1h 15m |
| IGO604H | IndiGo | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 2026-09-12 03:00 UTC | 2026-09-12 04:07 UTC | 1h 6m |
| BBC584 | BBC | VGZR (VGZR) | Naypyidaw Airport (VYEL) | 2026-09-12 02:57 UTC | 2026-09-12 04:05 UTC | 1h 7m |
| VIR354 | Virgin Atlantic | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-11 19:26 UTC | 2026-09-12 04:04 UTC | 8h 37m |
| N814SS |  | Beluga Airport (PABG) | Trading Bay Production Airport (5AK0) | 2026-09-12 03:45 UTC | 2026-09-12 03:59 UTC | 14m |
| N738WE |  | Jones Field (KF00) | Jones Field (KF00) | 2026-09-12 03:57 UTC | 2026-09-12 03:57 UTC | 0m |
| IGO36F | IndiGo | Amsterdam Airport Schiphol (EHAM) | Pune Airport (VAPO) | 2026-09-11 19:01 UTC | 2026-09-12 03:57 UTC | 8h 55m |
| ANA1087 | All Nippon Airways | Tokyo International Airport (RJTT) | Oki Airport (RJNO) | 2026-09-12 03:04 UTC | 2026-09-12 03:54 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
