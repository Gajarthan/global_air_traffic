# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_20:47:48_UTC-green)

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

**Latest saved flight:** 2026-08-22 20:47:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 20:47:48 UTC

- **226,937** saved flights
- **70,441** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **226,937** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,735,600.2 tonnes** estimated CO2 emissions
- **158,585,521 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9110 |
| 2 | SkyWest Airlines | 8068 |
| 3 | EJA | 4381 |
| 4 | IndiGo | 3829 |
| 5 | American Airlines | 3726 |
| 6 | Southwest Airlines | 3539 |
| 7 | Delta Air Lines | 2909 |
| 8 | ENY | 2779 |
| 9 | LATAM Airlines | 2170 |
| 10 | AZU | 2103 |
| 11 | Vueling | 1925 |
| 12 | Lufthansa | 1860 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1577 |
| 16 | Swiss International | 1514 |
| 17 | AXM | 1493 |
| 18 | United Airlines | 1436 |
| 19 | EJU | 1433 |
| 20 | QLK | 1421 |
| 21 | Alaska Airlines | 1374 |
| 22 | All Nippon Airways | 1356 |
| 23 | GLO | 1263 |
| 24 | PGT | 1247 |
| 25 | VIV | 1244 |
| 26 | Air France | 1235 |
| 27 | WMT | 1229 |
| 28 | Wizz Air | 1178 |
| 29 | JetBlue | 1136 |
| 30 | AEE | 1130 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190033 |
| 2 | 🇪🇸 ES | 14558 |
| 3 | 🇧🇷 BR | 13244 |
| 4 | 🇦🇺 AU | 12780 |
| 5 | 🇨🇦 CA | 12548 |
| 6 | 🇮🇹 IT | 12198 |
| 7 | 🇮🇳 IN | 11933 |
| 8 | 🇩🇪 DE | 11172 |
| 9 | 🇬🇧 GB | 10679 |
| 10 | 🇨🇴 CO | 9349 |
| 11 | 🇯🇵 JP | 9194 |
| 12 | 🇫🇷 FR | 9091 |
| 13 | 🇹🇷 TR | 6659 |
| 14 | 🇬🇷 GR | 6642 |
| 15 | 🇲🇽 MX | 6319 |
| 16 | 🇨🇭 CH | 5994 |
| 17 | 🇳🇴 NO | 5598 |
| 18 | 🇲🇾 MY | 3981 |
| 19 | 🇿🇦 ZA | 3923 |
| 20 | 🇹🇭 TH | 3889 |
| 21 | 🇵🇱 PL | 3772 |
| 22 | 🇳🇿 NZ | 3140 |
| 23 | 🇵🇭 PH | 3087 |
| 24 | 🇬🇹 GT | 2871 |
| 25 | 🇰🇷 KR | 2676 |
| 26 | 🇭🇷 HR | 2567 |
| 27 | 🇲🇦 MA | 2292 |
| 28 | 🇲🇪 ME | 2047 |
| 29 | 🇳🇱 NL | 2026 |
| 30 | 🇮🇩 ID | 1952 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4744 |
| 2 | Denver International Airport |  | US | 3704 |
| 3 | Indira Gandhi International Airport |  | IN | 2751 |
| 4 | Tokyo International Airport |  | JP | 2748 |
| 5 | Guaymaral Airport |  | CO | 2643 |
| 6 | Harry Reid International Airport |  | US | 2470 |
| 7 | Zurich Airport |  | CH | 2360 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2323 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2292 |
| 10 | La Aurora Airport |  | GT | 2187 |
| 11 | El Dorado International Airport |  | CO | 2081 |
| 12 | Chicago O'Hare International Airport |  | US | 2065 |
| 13 | Salt Lake City International Airport |  | US | 1998 |
| 14 | Congonhas Airport |  | BR | 1936 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1934 |
| 16 | Frankfurt am Main International Airport |  | DE | 1823 |
| 17 | Madrid Barajas International Airport |  | ES | 1770 |
| 18 | Capua Airport |  | IT | 1761 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1694 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1691 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1641 |
| 22 | Malpensa International Airport |  | IT | 1611 |
| 23 | Macau International Airport |  | MO | 1594 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1589 |
| 25 | Charles de Gaulle International Airport |  | FR | 1572 |
| 26 | Charlotte/Douglas International Airport |  | US | 1489 |
| 27 | Ninoy Aquino International Airport |  | PH | 1476 |
| 28 | Kuala Lumpur International Airport |  | MY | 1446 |
| 29 | Barcelona International Airport |  | ES | 1413 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1380 |
| 31 | Bengaluru International Airport |  | IN | 1345 |
| 32 | Viracopos International Airport |  | BR | 1344 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1341 |
| 34 | Enrique Olaya Herrera Airport |  | CO | 1339 |
| 35 | Seattle-Tacoma International Airport |  | US | 1334 |
| 36 | Calgary International Airport |  | CA | 1285 |
| 37 | Don Mueang International Airport |  | TH | 1276 |
| 38 | Oslo Gardermoen Airport |  | NO | 1263 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1227 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 821 | 21m | 244 km | 3,457.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 563 | 1h 6m | 770 km | 7,479.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 543 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 513 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 343 | 1h 50m | 1,423 km | 8,417.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 306 | 21m | 250 km | 1,321.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 293 | 44m | 555 km | 2,805.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 290 | 1h 38m | 1,156 km | 5,785.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 288 | 24m | 218 km | 1,085.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 266 | 1h 14m | 961 km | 4,409.1 t |
| 22 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 260 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 259 | 19m | 144 km | 644.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N919CM |  | Godfrey Airport (SN91) | Cessna Acft Field (KCEA) | 2026-08-22 20:27 UTC | 2026-08-22 20:47 UTC | 20m |
| N718DD |  | William P Hobby Airport (KHOU) | Austin Executive Airport (KEDC) | 2026-08-22 20:19 UTC | 2026-08-22 20:46 UTC | 27m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-22 20:28 UTC | 2026-08-22 20:46 UTC | 18m |
| N5852K |  | Albuquerque International Sunport Airport (KABQ) | G Bar F Ranch Airport (NM84) | 2026-08-22 19:55 UTC | 2026-08-22 20:41 UTC | 46m |
| ERU855 | ERU | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-08-22 20:27 UTC | 2026-08-22 20:38 UTC | 10m |
| N346CP |  | Mc Clellan-Palomar Airport (KCRQ) | Mc Clellan-Palomar Airport (KCRQ) | 2026-08-22 20:02 UTC | 2026-08-22 20:36 UTC | 34m |
| TRP7 | TRP | 5MD8 (5MD8) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-08-22 20:24 UTC | 2026-08-22 20:35 UTC | 11m |
| N314EV |  | Minden-Tahoe Airport (KMEV) | Desert Creek Airport (NV97) | 2026-08-22 19:05 UTC | 2026-08-22 20:33 UTC | 1h 27m |
| N70275 |  | San Bernardino International Airport (KSBD) | Hemet-Ryan Airport (KHMT) | 2026-08-22 20:09 UTC | 2026-08-22 20:31 UTC | 22m |
| TKR186 | TKR | Ephrata Municipal Airport (KEPH) | Ephrata Municipal Airport (KEPH) | 2026-08-22 20:24 UTC | 2026-08-22 20:25 UTC | 1m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-22 20:03 UTC | 2026-08-22 20:22 UTC | 18m |
| N901ST |  | Gittleson Farms Airport (15IL) | Staton Airport (4LL1) | 2026-08-22 20:08 UTC | 2026-08-22 20:20 UTC | 12m |
|  |  | 59WA (59WA) | Ochoa Field (6WA4) | 2026-08-22 19:47 UTC | 2026-08-22 20:17 UTC | 30m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-22 19:58 UTC | 2026-08-22 20:16 UTC | 18m |
| N945RF |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-22 19:56 UTC | 2026-08-22 20:15 UTC | 19m |
| N2699L |  | Caddo Mills Municipal Airport (K7F3) | 9XS7 (9XS7) | 2026-08-22 19:48 UTC | 2026-08-22 20:14 UTC | 25m |
| CFR72 | CFR | San Bernardino International Airport (KSBD) | San Bernardino International Airport (KSBD) | 2026-08-22 20:00 UTC | 2026-08-22 20:13 UTC | 13m |
| RAIDR08 | RAI | Chiriaco Summit Airport (KL77) | 1CA4 (1CA4) | 2026-08-22 17:57 UTC | 2026-08-22 20:06 UTC | 2h 8m |
| RYR45KP | Ryanair | London Gatwick Airport (EGKK) | Dublin Airport (EIDW) | 2026-08-22 19:16 UTC | 2026-08-22 20:06 UTC | 49m |
| N122ME |  | Auburn Municipal Airport (KAUN) | Lake Tahoe Airport (KTVL) | 2026-08-22 19:41 UTC | 2026-08-22 20:05 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
