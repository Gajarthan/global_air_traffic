# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_15:18:45_UTC-green)

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

**Latest saved flight:** 2026-08-22 15:18:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 15:18:45 UTC

- **225,836** saved flights
- **70,236** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **225,836** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,721,228.1 tonnes** estimated CO2 emissions
- **157,752,352 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9067 |
| 2 | SkyWest Airlines | 7999 |
| 3 | EJA | 4356 |
| 4 | IndiGo | 3821 |
| 5 | American Airlines | 3707 |
| 6 | Southwest Airlines | 3525 |
| 7 | Delta Air Lines | 2881 |
| 8 | ENY | 2761 |
| 9 | LATAM Airlines | 2157 |
| 10 | AZU | 2089 |
| 11 | Vueling | 1911 |
| 12 | Lufthansa | 1854 |
| 13 | WIF | 1796 |
| 14 | LXJ | 1780 |
| 15 | easyJet | 1565 |
| 16 | Swiss International | 1506 |
| 17 | AXM | 1493 |
| 18 | QLK | 1421 |
| 19 | EJU | 1420 |
| 20 | United Airlines | 1419 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1356 |
| 23 | GLO | 1257 |
| 24 | PGT | 1243 |
| 25 | VIV | 1234 |
| 26 | Air France | 1230 |
| 27 | WMT | 1214 |
| 28 | Wizz Air | 1172 |
| 29 | JetBlue | 1129 |
| 30 | AEE | 1124 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188983 |
| 2 | 🇪🇸 ES | 14468 |
| 3 | 🇧🇷 BR | 13161 |
| 4 | 🇦🇺 AU | 12776 |
| 5 | 🇨🇦 CA | 12497 |
| 6 | 🇮🇹 IT | 12119 |
| 7 | 🇮🇳 IN | 11913 |
| 8 | 🇩🇪 DE | 11128 |
| 9 | 🇬🇧 GB | 10617 |
| 10 | 🇨🇴 CO | 9281 |
| 11 | 🇯🇵 JP | 9192 |
| 12 | 🇫🇷 FR | 9039 |
| 13 | 🇹🇷 TR | 6619 |
| 14 | 🇬🇷 GR | 6604 |
| 15 | 🇲🇽 MX | 6268 |
| 16 | 🇨🇭 CH | 5975 |
| 17 | 🇳🇴 NO | 5590 |
| 18 | 🇲🇾 MY | 3981 |
| 19 | 🇿🇦 ZA | 3911 |
| 20 | 🇹🇭 TH | 3889 |
| 21 | 🇵🇱 PL | 3755 |
| 22 | 🇳🇿 NZ | 3138 |
| 23 | 🇵🇭 PH | 3087 |
| 24 | 🇬🇹 GT | 2860 |
| 25 | 🇰🇷 KR | 2676 |
| 26 | 🇭🇷 HR | 2550 |
| 27 | 🇲🇦 MA | 2275 |
| 28 | 🇲🇪 ME | 2032 |
| 29 | 🇳🇱 NL | 2019 |
| 30 | 🇮🇩 ID | 1952 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4708 |
| 2 | Denver International Airport |  | US | 3671 |
| 3 | Tokyo International Airport |  | JP | 2748 |
| 4 | Indira Gandhi International Airport |  | IN | 2743 |
| 5 | Guaymaral Airport |  | CO | 2633 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2349 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2303 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2284 |
| 10 | La Aurora Airport |  | GT | 2179 |
| 11 | El Dorado International Airport |  | CO | 2081 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1979 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 15 | Congonhas Airport |  | BR | 1925 |
| 16 | Frankfurt am Main International Airport |  | DE | 1819 |
| 17 | Madrid Barajas International Airport |  | ES | 1762 |
| 18 | Capua Airport |  | IT | 1742 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1680 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1679 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1635 |
| 22 | Malpensa International Airport |  | IT | 1595 |
| 23 | Macau International Airport |  | MO | 1594 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1589 |
| 25 | Charles de Gaulle International Airport |  | FR | 1564 |
| 26 | Charlotte/Douglas International Airport |  | US | 1484 |
| 27 | Ninoy Aquino International Airport |  | PH | 1476 |
| 28 | Kuala Lumpur International Airport |  | MY | 1446 |
| 29 | Barcelona International Airport |  | ES | 1403 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1370 |
| 31 | Bengaluru International Airport |  | IN | 1344 |
| 32 | Viracopos International Airport |  | BR | 1336 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1334 |
| 34 | Seattle-Tacoma International Airport |  | US | 1329 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1311 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1276 |
| 38 | Oslo Gardermoen Airport |  | NO | 1259 |
| 39 | Vitoria/Foronda Airport |  | ES | 1242 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1222 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1073 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 816 | 21m | 244 km | 3,436.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 563 | 1h 6m | 770 km | 7,479.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 530 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 511 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 340 | 1h 50m | 1,423 km | 8,344.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 301 | 21m | 250 km | 1,300.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 300 | 22m | 55 km | 285.1 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 293 | 44m | 555 km | 2,805.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 289 | 1h 38m | 1,156 km | 5,765.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 284 | 24m | 218 km | 1,069.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 282 | 19m | 99 km | 483.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 265 | 1h 14m | 961 km | 4,392.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 258 | 19m | 144 km | 641.8 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK236 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-22 14:32 UTC | 2026-08-22 15:18 UTC | 46m |
| N227WW |  | Ashland County Airport (K3G4) | Ashland County Airport (K3G4) | 2026-08-22 14:57 UTC | 2026-08-22 15:12 UTC | 15m |
| N2729U |  | Hopewell Airpark (90NY) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-22 14:37 UTC | 2026-08-22 15:11 UTC | 33m |
| CKS221 | CKS | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-08-22 04:41 UTC | 2026-08-22 15:10 UTC | 10h 29m |
| SWR179E | Swiss International | Palma De Mallorca Airport (LEPA) | Zurich Airport (LSZH) | 2026-08-22 13:37 UTC | 2026-08-22 15:02 UTC | 1h 24m |
| OEKFC | OEK | Stadtlohn-Vreden Airport (EDLS) | Stadtlohn-Vreden Airport (EDLS) | 2026-08-22 14:36 UTC | 2026-08-22 15:01 UTC | 25m |
| N529AB |  | MN38 (MN38) | Aitkin Municipal/Steve Kurtz Field (KAIT) | 2026-08-22 13:31 UTC | 2026-08-22 15:00 UTC | 1h 29m |
| N221AX |  | Flagstaff Pulliam Airport (KFLG) | Scottsdale Airport (KSDL) | 2026-08-22 14:25 UTC | 2026-08-22 15:00 UTC | 34m |
| N8449E |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-22 14:16 UTC | 2026-08-22 14:59 UTC | 43m |
| ASP858 | ASP | Vancouver International Airport (CYVR) | Boeing Field/King County International Airport (KBFI) | 2026-08-22 14:17 UTC | 2026-08-22 14:57 UTC | 40m |
| N470RG |  | KU77 (KU77) | Provo Municipal Airport (KPVU) | 2026-08-22 14:31 UTC | 2026-08-22 14:57 UTC | 25m |
| AWH96C | AWH | Munster Osnabruck Airport (EDDG) | Hoefen Airport (LOIR) | 2026-08-22 14:02 UTC | 2026-08-22 14:53 UTC | 50m |
| ES807 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-08-22 14:46 UTC | 2026-08-22 14:52 UTC | 5m |
| N35683 |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-08-22 14:38 UTC | 2026-08-22 14:52 UTC | 13m |
| N525DW |  | Midland International Air And Space Port Airport (KMAF) | Creekside Airport (03XS) | 2026-08-22 14:37 UTC | 2026-08-22 14:51 UTC | 13m |
| N787WW |  | Allegheny County Airport (KAGC) | Rostraver Airport (KFWQ) | 2026-08-22 14:40 UTC | 2026-08-22 14:50 UTC | 10m |
| N734ES |  | Ramona Airport (KRNM) | Chino Airport (KCNO) | 2026-08-22 14:04 UTC | 2026-08-22 14:50 UTC | 46m |
| N444FE |  | Southern Fruit Groves Airport (FD24) | Brady Ranch Airport (80FD) | 2026-08-22 14:45 UTC | 2026-08-22 14:49 UTC | 4m |
| CXK1107 | CXK | Conroe/North Houston Regional Airport (KCXO) | Navasota Municipal Airport (K60R) | 2026-08-22 13:54 UTC | 2026-08-22 14:47 UTC | 52m |
| N4120R |  | 36AZ (36AZ) | Sarita Airport (37AZ) | 2026-08-22 12:44 UTC | 2026-08-22 14:46 UTC | 2h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
