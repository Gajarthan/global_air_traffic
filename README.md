# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_23:40:51_UTC-green)

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

**Latest saved flight:** 2026-08-31 23:40:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-31 23:40:51 UTC

- **243,155** saved flights
- **73,696** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **243,155** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,927,539.9 tonnes** estimated CO2 emissions
- **169,712,457 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9765 |
| 2 | SkyWest Airlines | 8526 |
| 3 | EJA | 4703 |
| 4 | IndiGo | 4084 |
| 5 | American Airlines | 3915 |
| 6 | Southwest Airlines | 3656 |
| 7 | Delta Air Lines | 3101 |
| 8 | ENY | 2931 |
| 9 | LATAM Airlines | 2333 |
| 10 | AZU | 2263 |
| 11 | Vueling | 2083 |
| 12 | Lufthansa | 1951 |
| 13 | WIF | 1930 |
| 14 | LXJ | 1883 |
| 15 | easyJet | 1696 |
| 16 | Swiss International | 1638 |
| 17 | AXM | 1602 |
| 18 | EJU | 1561 |
| 19 | QLK | 1550 |
| 20 | United Airlines | 1531 |
| 21 | Alaska Airlines | 1453 |
| 22 | All Nippon Airways | 1434 |
| 23 | WMT | 1369 |
| 24 | GLO | 1360 |
| 25 | VIV | 1331 |
| 26 | PGT | 1330 |
| 27 | Air France | 1326 |
| 28 | Wizz Air | 1317 |
| 29 | JetBlue | 1204 |
| 30 | AEE | 1201 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 201508 |
| 2 | 🇪🇸 ES | 15623 |
| 3 | 🇧🇷 BR | 14185 |
| 4 | 🇦🇺 AU | 13799 |
| 5 | 🇨🇦 CA | 13530 |
| 6 | 🇮🇹 IT | 13317 |
| 7 | 🇮🇳 IN | 12715 |
| 8 | 🇩🇪 DE | 11994 |
| 9 | 🇬🇧 GB | 11483 |
| 10 | 🇨🇴 CO | 10502 |
| 11 | 🇫🇷 FR | 9801 |
| 12 | 🇯🇵 JP | 9719 |
| 13 | 🇹🇷 TR | 7230 |
| 14 | 🇬🇷 GR | 7169 |
| 15 | 🇲🇽 MX | 6707 |
| 16 | 🇨🇭 CH | 6542 |
| 17 | 🇳🇴 NO | 6010 |
| 18 | 🇹🇭 TH | 4397 |
| 19 | 🇲🇾 MY | 4297 |
| 20 | 🇿🇦 ZA | 4233 |
| 21 | 🇵🇱 PL | 4089 |
| 22 | 🇳🇿 NZ | 3342 |
| 23 | 🇵🇭 PH | 3326 |
| 24 | 🇬🇹 GT | 3060 |
| 25 | 🇰🇷 KR | 2860 |
| 26 | 🇭🇷 HR | 2805 |
| 27 | 🇲🇦 MA | 2462 |
| 28 | 🇲🇪 ME | 2270 |
| 29 | 🇳🇱 NL | 2199 |
| 30 | 🇮🇩 ID | 2118 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5019 |
| 2 | Denver International Airport |  | US | 3917 |
| 3 | Indira Gandhi International Airport |  | IN | 2962 |
| 4 | Tokyo International Airport |  | JP | 2893 |
| 5 | Guaymaral Airport |  | CO | 2707 |
| 6 | Harry Reid International Airport |  | US | 2587 |
| 7 | Zurich Airport |  | CH | 2553 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2484 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2426 |
| 10 | El Dorado International Airport |  | CO | 2384 |
| 11 | La Aurora Airport |  | GT | 2329 |
| 12 | Salt Lake City International Airport |  | US | 2151 |
| 13 | Chicago O'Hare International Airport |  | US | 2151 |
| 14 | Congonhas Airport |  | BR | 2076 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2016 |
| 16 | Frankfurt am Main International Airport |  | DE | 1921 |
| 17 | Capua Airport |  | IT | 1914 |
| 18 | Madrid Barajas International Airport |  | ES | 1909 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1826 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1790 |
| 21 | Malpensa International Airport |  | IT | 1736 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1720 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1703 |
| 24 | Charles de Gaulle International Airport |  | FR | 1702 |
| 25 | Macau International Airport |  | MO | 1619 |
| 26 | Ninoy Aquino International Airport |  | PH | 1617 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1558 |
| 28 | Charlotte/Douglas International Airport |  | US | 1555 |
| 29 | Kuala Lumpur International Airport |  | MY | 1549 |
| 30 | Barcelona International Airport |  | ES | 1544 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1470 |
| 32 | Viracopos International Airport |  | BR | 1445 |
| 33 | Seattle-Tacoma International Airport |  | US | 1424 |
| 34 | Don Mueang International Airport |  | TH | 1416 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1410 |
| 36 | Bengaluru International Airport |  | IN | 1410 |
| 37 | Calgary International Airport |  | CA | 1396 |
| 38 | Oslo Gardermoen Airport |  | NO | 1366 |
| 39 | Vancouver International Airport |  | CA | 1352 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1328 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1097 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 896 | 21m | 244 km | 3,772.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 628 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 617 | 24m | 225 km | 2,393.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 614 | 1h 6m | 770 km | 8,156.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 548 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 400 | 27m | 275 km | 1,895.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 382 | 1h 50m | 1,423 km | 9,374.9 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 371 | 44m | 555 km | 3,552.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 354 | 44m | 241 km | 1,470.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 347 | 21m | 250 km | 1,498.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 334 | 24m | 218 km | 1,258.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 323 | 1h 39m | 1,156 km | 6,443.7 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 322 | 22m | 55 km | 306.1 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 302 | 19m | 99 km | 517.3 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 296 | 26m | 215 km | 1,096.3 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 286 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 282 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 279 | 1h 14m | 961 km | 4,624.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 275 | 19m | 144 km | 684.0 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 265 | 15m | 154 km | 702.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 262 | 1h 50m | 1,304 km | 5,894.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N89KA |  | Seattle Paine Field International Airport (KPAE) | Renton Municipal Airport (KRNT) | 2026-08-31 23:05 UTC | 2026-08-31 23:40 UTC | 35m |
| UAL509 | United Airlines | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Newark Liberty International Airport (KEWR) | 2026-08-31 14:10 UTC | 2026-08-31 23:37 UTC | 9h 27m |
| N5779T |  | Stoney's Airport (OI32) | 2OI8 (2OI8) | 2026-08-31 22:46 UTC | 2026-08-31 23:36 UTC | 49m |
| SCU58 | SCU | William R Pogue Municipal Airport (KOWP) | Tulsa International Airport (KTUL) | 2026-08-31 23:15 UTC | 2026-08-31 23:35 UTC | 20m |
| N175DD |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-08-31 21:30 UTC | 2026-08-31 23:30 UTC | 1h 59m |
| N244MM |  | Aire Parque Airport (42MO) | Aire Parque Airport (42MO) | 2026-08-31 21:50 UTC | 2026-08-31 23:27 UTC | 1h 36m |
| N916RR |  | Santa Barbara Municipal Airport (KSBA) | Riverside Airport (KRAL) | 2026-08-31 22:13 UTC | 2026-08-31 23:26 UTC | 1h 13m |
| FOW | FOW | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-08-31 23:01 UTC | 2026-08-31 23:25 UTC | 24m |
| N79331 |  | Granbury Regional Airport (KGDJ) | Granbury Regional Airport (KGDJ) | 2026-08-31 23:14 UTC | 2026-08-31 23:20 UTC | 6m |
| ABY081 | ABY | Sharjah International Airport (OMSJ) | Sirri Island Airport (OIBS) | 2026-08-31 22:58 UTC | 2026-08-31 23:13 UTC | 15m |
| RGY710 | RGY | Los Angeles International Airport (KLAX) | Bermuda Dunes Airport (KUDD) | 2026-08-31 22:51 UTC | 2026-08-31 23:11 UTC | 20m |
| SRG199 | SRG | Cumbernauld Airport (EGPG) | Glasgow International Airport (EGPF) | 2026-08-31 22:53 UTC | 2026-08-31 23:09 UTC | 16m |
| AER930 | AER | King Salmon Airport (PAKN) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-31 21:57 UTC | 2026-08-31 23:05 UTC | 1h 7m |
| N538M |  | Mbs International Airport (KMBS) | Green Bay/Austin Straubel International Airport (KGRB) | 2026-08-31 22:27 UTC | 2026-08-31 23:02 UTC | 34m |
| JRE739 | JRE | Addison Airport (KADS) | Sharp Field (90LA) | 2026-08-31 22:26 UTC | 2026-08-31 23:00 UTC | 34m |
| CGPCL | CGP | Vancouver International Airport (CYVR) | Princeton Airport (CYDC) | 2026-08-31 22:25 UTC | 2026-08-31 22:56 UTC | 30m |
| SLH817 | SLH | Grand Forks International Airport (KGFK) | Loup City Municipal Airport (K0F4) | 2026-08-31 21:43 UTC | 2026-08-31 22:53 UTC | 1h 10m |
| SH471 |  | Adelaide International Airport (YPAD) | Tenneco Station Four Airport (YTNN) | 2026-08-31 21:53 UTC | 2026-08-31 22:50 UTC | 56m |
| WJA121 | WJA | Calgary International Airport (CYYC) | Vancouver International Airport (CYVR) | 2026-08-31 21:41 UTC | 2026-08-31 22:48 UTC | 1h 6m |
| THY6345 | Turkish Airlines | Istanbul Airport (LTFM) | Zhuhai Airport (ZGSD) | 2026-08-31 09:29 UTC | 2026-08-31 22:47 UTC | 13h 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
