# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_18:33:39_UTC-green)

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

**Latest saved flight:** 2026-08-29 18:33:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-29 18:33:39 UTC

- **241,139** saved flights
- **73,186** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **241,139** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,902,699.6 tonnes** estimated CO2 emissions
- **168,272,442 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9679 |
| 2 | SkyWest Airlines | 8451 |
| 3 | EJA | 4665 |
| 4 | IndiGo | 4068 |
| 5 | American Airlines | 3883 |
| 6 | Southwest Airlines | 3630 |
| 7 | Delta Air Lines | 3071 |
| 8 | ENY | 2907 |
| 9 | LATAM Airlines | 2314 |
| 10 | AZU | 2242 |
| 11 | Vueling | 2070 |
| 12 | Lufthansa | 1941 |
| 13 | WIF | 1909 |
| 14 | LXJ | 1869 |
| 15 | easyJet | 1682 |
| 16 | Swiss International | 1627 |
| 17 | AXM | 1597 |
| 18 | EJU | 1545 |
| 19 | QLK | 1538 |
| 20 | United Airlines | 1513 |
| 21 | Alaska Airlines | 1441 |
| 22 | All Nippon Airways | 1429 |
| 23 | WMT | 1357 |
| 24 | GLO | 1345 |
| 25 | VIV | 1322 |
| 26 | Air France | 1320 |
| 27 | PGT | 1316 |
| 28 | Wizz Air | 1299 |
| 29 | AEE | 1193 |
| 30 | JetBlue | 1191 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 199776 |
| 2 | 🇪🇸 ES | 15508 |
| 3 | 🇧🇷 BR | 14061 |
| 4 | 🇦🇺 AU | 13676 |
| 5 | 🇨🇦 CA | 13409 |
| 6 | 🇮🇹 IT | 13195 |
| 7 | 🇮🇳 IN | 12661 |
| 8 | 🇩🇪 DE | 11910 |
| 9 | 🇬🇧 GB | 11397 |
| 10 | 🇨🇴 CO | 10358 |
| 11 | 🇫🇷 FR | 9727 |
| 12 | 🇯🇵 JP | 9686 |
| 13 | 🇹🇷 TR | 7155 |
| 14 | 🇬🇷 GR | 7104 |
| 15 | 🇲🇽 MX | 6659 |
| 16 | 🇨🇭 CH | 6470 |
| 17 | 🇳🇴 NO | 5950 |
| 18 | 🇹🇭 TH | 4380 |
| 19 | 🇲🇾 MY | 4278 |
| 20 | 🇿🇦 ZA | 4217 |
| 21 | 🇵🇱 PL | 4043 |
| 22 | 🇳🇿 NZ | 3310 |
| 23 | 🇵🇭 PH | 3309 |
| 24 | 🇬🇹 GT | 3031 |
| 25 | 🇰🇷 KR | 2849 |
| 26 | 🇭🇷 HR | 2786 |
| 27 | 🇲🇦 MA | 2437 |
| 28 | 🇲🇪 ME | 2254 |
| 29 | 🇳🇱 NL | 2187 |
| 30 | 🇮🇩 ID | 2112 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4974 |
| 2 | Denver International Airport |  | US | 3885 |
| 3 | Indira Gandhi International Airport |  | IN | 2947 |
| 4 | Tokyo International Airport |  | JP | 2883 |
| 5 | Guaymaral Airport |  | CO | 2696 |
| 6 | Harry Reid International Airport |  | US | 2561 |
| 7 | Zurich Airport |  | CH | 2529 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2466 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2403 |
| 10 | El Dorado International Airport |  | CO | 2343 |
| 11 | La Aurora Airport |  | GT | 2311 |
| 12 | Chicago O'Hare International Airport |  | US | 2146 |
| 13 | Salt Lake City International Airport |  | US | 2121 |
| 14 | Congonhas Airport |  | BR | 2054 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1999 |
| 16 | Frankfurt am Main International Airport |  | DE | 1909 |
| 17 | Capua Airport |  | IT | 1902 |
| 18 | Madrid Barajas International Airport |  | ES | 1898 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1813 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1773 |
| 21 | Malpensa International Airport |  | IT | 1726 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1697 |
| 23 | Charles de Gaulle International Airport |  | FR | 1690 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1689 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1607 |
| 27 | Kuala Lumpur International Airport |  | MY | 1545 |
| 28 | Charlotte/Douglas International Airport |  | US | 1544 |
| 29 | Enrique Olaya Herrera Airport |  | CO | 1536 |
| 30 | Barcelona International Airport |  | ES | 1536 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1456 |
| 32 | Viracopos International Airport |  | BR | 1434 |
| 33 | Don Mueang International Airport |  | TH | 1410 |
| 34 | Bengaluru International Airport |  | IN | 1407 |
| 35 | Seattle-Tacoma International Airport |  | US | 1405 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1402 |
| 37 | Calgary International Airport |  | CA | 1383 |
| 38 | Oslo Gardermoen Airport |  | NO | 1354 |
| 39 | Vancouver International Airport |  | CA | 1327 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1319 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1092 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 888 | 21m | 244 km | 3,739.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 621 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 612 | 24m | 225 km | 2,374.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 610 | 1h 6m | 770 km | 8,103.4 t |
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
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 279 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 279 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 275 | 1h 14m | 961 km | 4,558.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 271 | 19m | 144 km | 674.1 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 258 | 1h 50m | 1,304 km | 5,804.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N828AK |  | Kissimmee Gateway Airport (KISM) | Kissimmee Gateway Airport (KISM) | 2026-08-29 17:34 UTC | 2026-08-29 18:33 UTC | 59m |
| BRW2 | BRW | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-08-29 17:59 UTC | 2026-08-29 18:30 UTC | 30m |
| N83FE |  | Humphreys County Airport (K0M5) | Humphreys County Airport (K0M5) | 2026-08-29 18:11 UTC | 2026-08-29 18:27 UTC | 15m |
| SWR849W | Swiss International | Dusseldorf International Airport (EDDL) | Zurich Airport (LSZH) | 2026-08-29 17:35 UTC | 2026-08-29 18:24 UTC | 48m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-08-29 18:01 UTC | 2026-08-29 18:21 UTC | 20m |
| N3040F |  | Greeneville Municipal Airport (KGCY) | Greeneville Municipal Airport (KGCY) | 2026-08-29 18:10 UTC | 2026-08-29 18:21 UTC | 10m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-08-29 17:41 UTC | 2026-08-29 18:18 UTC | 37m |
| N9563A |  | Greenwood Lake Airport (K4N1) | Greenwood Lake Airport (K4N1) | 2026-08-29 17:57 UTC | 2026-08-29 18:13 UTC | 15m |
| FDX6229 | FDX | Ted Stevens Anchorage International Airport (PANC) | Guangzhou Baiyun International Airport (ZGGG) | 2026-08-29 07:31 UTC | 2026-08-29 18:08 UTC | 10h 36m |
| N315SM |  | Centennial Airport (KAPA) | Limon Municipal Airport (KLIC) | 2026-08-29 17:26 UTC | 2026-08-29 18:06 UTC | 39m |
| BF708 |  | Thunder Bay Airport (CYQT) | Atikokan Municipal Airport (CYIB) | 2026-08-29 17:36 UTC | 2026-08-29 18:04 UTC | 28m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-29 16:17 UTC | 2026-08-29 18:02 UTC | 1h 45m |
| RJA102 | Royal Jordanian | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Amman-Marka International Airport (OJAM) | 2026-08-29 15:18 UTC | 2026-08-29 18:02 UTC | 2h 44m |
| N38549 |  | Laconia Municipal Airport (KLCI) | Lebanon Municipal Airport (KLEB) | 2026-08-29 17:35 UTC | 2026-08-29 18:01 UTC | 25m |
| N182KQ |  | Stuart Island Airpark (7WA5) | Nanaimo Airport (CYCD) | 2026-08-29 17:44 UTC | 2026-08-29 18:00 UTC | 16m |
| A6FNG |  | Fujairah International Airport (OMFJ) | Ras Al Khaimah International Airport (OMRK) | 2026-08-29 17:38 UTC | 2026-08-29 18:00 UTC | 21m |
| N745B |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-08-29 17:42 UTC | 2026-08-29 17:57 UTC | 14m |
| RJA118 | Royal Jordanian | Charles de Gaulle International Airport (LFPG) | Amman-Marka International Airport (OJAM) | 2026-08-29 14:11 UTC | 2026-08-29 17:57 UTC | 3h 46m |
| N4841Y |  | Kelly Air Park (CO15) | Kelly Air Park (CO15) | 2026-08-29 17:49 UTC | 2026-08-29 17:55 UTC | 6m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-29 17:38 UTC | 2026-08-29 17:54 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
