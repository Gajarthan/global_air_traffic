# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_01:03:01_UTC-green)

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

**Latest saved flight:** 2026-08-30 01:03:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-30 01:03:01 UTC

- **241,495** saved flights
- **73,269** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **241,495** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,906,906.6 tonnes** estimated CO2 emissions
- **168,516,325 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9685 |
| 2 | SkyWest Airlines | 8478 |
| 3 | EJA | 4672 |
| 4 | IndiGo | 4069 |
| 5 | American Airlines | 3891 |
| 6 | Southwest Airlines | 3633 |
| 7 | Delta Air Lines | 3080 |
| 8 | ENY | 2915 |
| 9 | LATAM Airlines | 2315 |
| 10 | AZU | 2243 |
| 11 | Vueling | 2072 |
| 12 | Lufthansa | 1941 |
| 13 | WIF | 1909 |
| 14 | LXJ | 1870 |
| 15 | easyJet | 1685 |
| 16 | Swiss International | 1627 |
| 17 | AXM | 1598 |
| 18 | EJU | 1547 |
| 19 | QLK | 1540 |
| 20 | United Airlines | 1517 |
| 21 | Alaska Airlines | 1443 |
| 22 | All Nippon Airways | 1429 |
| 23 | WMT | 1358 |
| 24 | GLO | 1347 |
| 25 | VIV | 1323 |
| 26 | Air France | 1320 |
| 27 | PGT | 1320 |
| 28 | Wizz Air | 1302 |
| 29 | JetBlue | 1197 |
| 30 | AEE | 1194 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 200201 |
| 2 | 🇪🇸 ES | 15517 |
| 3 | 🇧🇷 BR | 14071 |
| 4 | 🇦🇺 AU | 13684 |
| 5 | 🇨🇦 CA | 13442 |
| 6 | 🇮🇹 IT | 13203 |
| 7 | 🇮🇳 IN | 12665 |
| 8 | 🇩🇪 DE | 11912 |
| 9 | 🇬🇧 GB | 11402 |
| 10 | 🇨🇴 CO | 10395 |
| 11 | 🇫🇷 FR | 9731 |
| 12 | 🇯🇵 JP | 9688 |
| 13 | 🇹🇷 TR | 7167 |
| 14 | 🇬🇷 GR | 7111 |
| 15 | 🇲🇽 MX | 6669 |
| 16 | 🇨🇭 CH | 6471 |
| 17 | 🇳🇴 NO | 5950 |
| 18 | 🇹🇭 TH | 4380 |
| 19 | 🇲🇾 MY | 4280 |
| 20 | 🇿🇦 ZA | 4217 |
| 21 | 🇵🇱 PL | 4048 |
| 22 | 🇳🇿 NZ | 3324 |
| 23 | 🇵🇭 PH | 3315 |
| 24 | 🇬🇹 GT | 3031 |
| 25 | 🇰🇷 KR | 2849 |
| 26 | 🇭🇷 HR | 2788 |
| 27 | 🇲🇦 MA | 2439 |
| 28 | 🇲🇪 ME | 2255 |
| 29 | 🇳🇱 NL | 2187 |
| 30 | 🇮🇩 ID | 2115 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4990 |
| 2 | Denver International Airport |  | US | 3898 |
| 3 | Indira Gandhi International Airport |  | IN | 2948 |
| 4 | Tokyo International Airport |  | JP | 2884 |
| 5 | Guaymaral Airport |  | CO | 2701 |
| 6 | Harry Reid International Airport |  | US | 2568 |
| 7 | Zurich Airport |  | CH | 2530 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2471 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2405 |
| 10 | El Dorado International Airport |  | CO | 2355 |
| 11 | La Aurora Airport |  | GT | 2311 |
| 12 | Chicago O'Hare International Airport |  | US | 2148 |
| 13 | Salt Lake City International Airport |  | US | 2130 |
| 14 | Congonhas Airport |  | BR | 2056 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2000 |
| 16 | Frankfurt am Main International Airport |  | DE | 1910 |
| 17 | Capua Airport |  | IT | 1903 |
| 18 | Madrid Barajas International Airport |  | ES | 1900 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1814 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1777 |
| 21 | Malpensa International Airport |  | IT | 1729 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1703 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1690 |
| 24 | Charles de Gaulle International Airport |  | FR | 1690 |
| 25 | Macau International Airport |  | MO | 1615 |
| 26 | Ninoy Aquino International Airport |  | PH | 1610 |
| 27 | Charlotte/Douglas International Airport |  | US | 1547 |
| 28 | Kuala Lumpur International Airport |  | MY | 1546 |
| 29 | Enrique Olaya Herrera Airport |  | CO | 1538 |
| 30 | Barcelona International Airport |  | ES | 1538 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1458 |
| 32 | Viracopos International Airport |  | BR | 1435 |
| 33 | Don Mueang International Airport |  | TH | 1410 |
| 34 | Seattle-Tacoma International Airport |  | US | 1410 |
| 35 | Bengaluru International Airport |  | IN | 1407 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1404 |
| 37 | Calgary International Airport |  | CA | 1387 |
| 38 | Oslo Gardermoen Airport |  | NO | 1354 |
| 39 | Vancouver International Airport |  | CA | 1337 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1319 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1094 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 889 | 21m | 244 km | 3,743.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 621 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 614 | 24m | 225 km | 2,382.0 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 611 | 1h 6m | 770 km | 8,116.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 546 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 398 | 27m | 275 km | 1,886.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 380 | 1h 50m | 1,423 km | 9,325.8 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 367 | 44m | 555 km | 3,514.2 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 366 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 350 | 44m | 241 km | 1,453.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 328 | 24m | 218 km | 1,235.7 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 321 | 1h 40m | 1,156 km | 6,403.8 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 299 | 19m | 99 km | 512.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 294 | 26m | 215 km | 1,088.9 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 284 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 279 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 275 | 1h 14m | 961 km | 4,558.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 272 | 19m | 144 km | 676.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 264 | 15m | 154 km | 699.5 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 259 | 1h 50m | 1,304 km | 5,826.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ALFT5 | ALF | Bellingham International Airport (KBLI) | Boeing Field/King County International Airport (KBFI) | 2026-08-30 00:25 UTC | 2026-08-30 01:03 UTC | 37m |
| N776LF |  | Portland International Airport (KPDX) | Pilot Butte Airport (8OR5) | 2026-08-30 00:07 UTC | 2026-08-30 00:54 UTC | 47m |
| CGKGP | CGK | Nanaimo Airport (CYCD) | Vancouver International Airport (CYVR) | 2026-08-30 00:32 UTC | 2026-08-30 00:48 UTC | 16m |
| N96LA |  | Centennial Airport (KAPA) | Santa Fe Regional Airport (KSAF) | 2026-08-30 00:08 UTC | 2026-08-30 00:44 UTC | 35m |
| N437FA |  | Palo Alto Airport (KPAO) | Livermore Municipal Airport (KLVK) | 2026-08-30 00:12 UTC | 2026-08-30 00:43 UTC | 31m |
| N565TA |  | Talkeetna Village Strip (AK44) | Mc Kinley Country Airport (81AK) | 2026-08-29 23:42 UTC | 2026-08-30 00:39 UTC | 57m |
| LYM5411 | LYM | Dallas-Fort Worth International Airport (KDFW) | Locker Brothers Airport (1TE0) | 2026-08-29 23:54 UTC | 2026-08-30 00:39 UTC | 44m |
| N35121 |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-08-29 23:33 UTC | 2026-08-30 00:38 UTC | 1h 4m |
| JBU2459 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | Philadelphia International Airport (KPHL) | 2026-08-29 23:28 UTC | 2026-08-30 00:27 UTC | 58m |
| QLK1253 | QLK | Brisbane International Airport (YBBN) | Melbourne International Airport (YMML) | 2026-08-29 22:20 UTC | 2026-08-30 00:20 UTC | 1h 59m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-30 00:11 UTC | 2026-08-30 00:19 UTC | 7m |
| N411WA |  | Ted Stevens Anchorage International Airport (PANC) | Edward G Pitka Sr Airport (PAGA) | 2026-08-29 23:08 UTC | 2026-08-30 00:18 UTC | 1h 10m |
| N95897 |  | Ed Carlson Memorial Field/South Lewis County Airport (KTDO) | Renton Municipal Airport (KRNT) | 2026-08-29 23:39 UTC | 2026-08-30 00:15 UTC | 35m |
| LEAD79 | LEA | Denton Enterprise Airport (KDTO) | 85OL (85OL) | 2026-08-29 22:36 UTC | 2026-08-30 00:15 UTC | 1h 38m |
| FFT1816 | FFT | Denver International Airport (KDEN) | Austin-Bergstrom International Airport (KAUS) | 2026-08-29 22:33 UTC | 2026-08-30 00:14 UTC | 1h 40m |
| SCU23 | SCU | Haskell Airport (K2K9) | Haskell Airport (K2K9) | 2026-08-30 00:01 UTC | 2026-08-30 00:13 UTC | 12m |
| JAP7042 | JAP | Vicco Airport (SPVI) | Jorge Chavez International Airport (SPJC) | 2026-08-29 23:57 UTC | 2026-08-30 00:13 UTC | 15m |
| DAL362 | Delta Air Lines | Faith Municipal Airport (KD07) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-08-29 23:19 UTC | 2026-08-30 00:12 UTC | 53m |
| DAL417 | Delta Air Lines | Salt Lake City International Airport (KSLC) | Heiner Airport (WY60) | 2026-08-29 23:50 UTC | 2026-08-30 00:11 UTC | 20m |
| ANZ617 | ANZ | Auckland International Airport (NZAA) | Glenorchy Airport (NZGY) | 2026-08-29 22:39 UTC | 2026-08-30 00:10 UTC | 1h 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
