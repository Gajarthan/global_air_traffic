# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_21:40:15_UTC-green)

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

**Latest saved flight:** 2026-08-22 21:40:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 21:40:15 UTC

- **227,074** saved flights
- **70,472** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **227,074** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,737,480.4 tonnes** estimated CO2 emissions
- **158,694,513 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9117 |
| 2 | SkyWest Airlines | 8080 |
| 3 | EJA | 4384 |
| 4 | IndiGo | 3829 |
| 5 | American Airlines | 3730 |
| 6 | Southwest Airlines | 3542 |
| 7 | Delta Air Lines | 2910 |
| 8 | ENY | 2782 |
| 9 | LATAM Airlines | 2173 |
| 10 | AZU | 2103 |
| 11 | Vueling | 1925 |
| 12 | Lufthansa | 1860 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1578 |
| 16 | Swiss International | 1514 |
| 17 | AXM | 1493 |
| 18 | United Airlines | 1437 |
| 19 | EJU | 1434 |
| 20 | QLK | 1421 |
| 21 | Alaska Airlines | 1377 |
| 22 | All Nippon Airways | 1356 |
| 23 | GLO | 1264 |
| 24 | PGT | 1247 |
| 25 | VIV | 1246 |
| 26 | Air France | 1235 |
| 27 | WMT | 1229 |
| 28 | Wizz Air | 1178 |
| 29 | JetBlue | 1136 |
| 30 | AEE | 1130 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190178 |
| 2 | 🇪🇸 ES | 14563 |
| 3 | 🇧🇷 BR | 13254 |
| 4 | 🇦🇺 AU | 12780 |
| 5 | 🇨🇦 CA | 12558 |
| 6 | 🇮🇹 IT | 12207 |
| 7 | 🇮🇳 IN | 11933 |
| 8 | 🇩🇪 DE | 11176 |
| 9 | 🇬🇧 GB | 10685 |
| 10 | 🇨🇴 CO | 9364 |
| 11 | 🇯🇵 JP | 9194 |
| 12 | 🇫🇷 FR | 9093 |
| 13 | 🇹🇷 TR | 6665 |
| 14 | 🇬🇷 GR | 6643 |
| 15 | 🇲🇽 MX | 6325 |
| 16 | 🇨🇭 CH | 5995 |
| 17 | 🇳🇴 NO | 5601 |
| 18 | 🇲🇾 MY | 3981 |
| 19 | 🇿🇦 ZA | 3923 |
| 20 | 🇹🇭 TH | 3889 |
| 21 | 🇵🇱 PL | 3774 |
| 22 | 🇳🇿 NZ | 3144 |
| 23 | 🇵🇭 PH | 3088 |
| 24 | 🇬🇹 GT | 2871 |
| 25 | 🇰🇷 KR | 2676 |
| 26 | 🇭🇷 HR | 2567 |
| 27 | 🇲🇦 MA | 2294 |
| 28 | 🇲🇪 ME | 2051 |
| 29 | 🇳🇱 NL | 2026 |
| 30 | 🇮🇩 ID | 1952 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4751 |
| 2 | Denver International Airport |  | US | 3708 |
| 3 | Indira Gandhi International Airport |  | IN | 2751 |
| 4 | Tokyo International Airport |  | JP | 2748 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2470 |
| 7 | Zurich Airport |  | CH | 2361 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2324 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2292 |
| 10 | La Aurora Airport |  | GT | 2187 |
| 11 | El Dorado International Airport |  | CO | 2081 |
| 12 | Chicago O'Hare International Airport |  | US | 2068 |
| 13 | Salt Lake City International Airport |  | US | 2000 |
| 14 | Congonhas Airport |  | BR | 1937 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1935 |
| 16 | Frankfurt am Main International Airport |  | DE | 1823 |
| 17 | Madrid Barajas International Airport |  | ES | 1771 |
| 18 | Capua Airport |  | IT | 1761 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1694 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1694 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1641 |
| 22 | Malpensa International Airport |  | IT | 1613 |
| 23 | Macau International Airport |  | MO | 1594 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1589 |
| 25 | Charles de Gaulle International Airport |  | FR | 1573 |
| 26 | Charlotte/Douglas International Airport |  | US | 1491 |
| 27 | Ninoy Aquino International Airport |  | PH | 1477 |
| 28 | Kuala Lumpur International Airport |  | MY | 1446 |
| 29 | Barcelona International Airport |  | ES | 1413 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1381 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1347 |
| 32 | Bengaluru International Airport |  | IN | 1345 |
| 33 | Viracopos International Airport |  | BR | 1344 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1342 |
| 35 | Seattle-Tacoma International Airport |  | US | 1337 |
| 36 | Calgary International Airport |  | CA | 1289 |
| 37 | Don Mueang International Airport |  | TH | 1276 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1227 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 822 | 21m | 244 km | 3,461.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 563 | 1h 6m | 770 km | 7,479.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 546 | 8m | - | - |
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
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 261 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 259 | 19m | 144 km | 644.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N485K |  | Marina Municipal Airport (KOAR) | Marina Municipal Airport (KOAR) | 2026-08-22 21:28 UTC | 2026-08-22 21:40 UTC | 11m |
| N4480T |  | 37II (37II) | Southwest Michigan Regional Airport (KBEH) | 2026-08-22 21:07 UTC | 2026-08-22 21:40 UTC | 32m |
| N5852K |  | G Bar F Ranch Airport (NM84) | G Bar F Ranch Airport (NM84) | 2026-08-22 20:59 UTC | 2026-08-22 21:38 UTC | 39m |
| LTG8506 | LTG | Miami International Airport (KMIA) | Brussels Airport (EBBR) | 2026-08-22 13:09 UTC | 2026-08-22 21:35 UTC | 8h 25m |
| MAO3 | MAO | Owatonna Degner Regional Airport (KOWA) | Mankato Regional Airport (KMKT) | 2026-08-22 21:13 UTC | 2026-08-22 21:31 UTC | 18m |
| UAL1306 | United Airlines | Wexford County Airport (KCAD) | 5NE5 (5NE5) | 2026-08-22 19:43 UTC | 2026-08-22 21:28 UTC | 1h 44m |
| ASI642 | ASI | Georgetown Executive Airport (KGTU) | Taylor Municipal Airport (KT74) | 2026-08-22 20:04 UTC | 2026-08-22 21:27 UTC | 1h 22m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-22 21:15 UTC | 2026-08-22 21:25 UTC | 10m |
| AMD1 | AMD | Christchurch International Airport (NZCH) | Christchurch International Airport (NZCH) | 2026-08-22 21:15 UTC | 2026-08-22 21:18 UTC | 3m |
| N3546T |  | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-08-22 19:13 UTC | 2026-08-22 21:16 UTC | 2h 2m |
| TKR15 | TKR | Truckee-Tahoe Airport (KTRK) | K4SD (K4SD) | 2026-08-22 20:38 UTC | 2026-08-22 21:13 UTC | 35m |
| FTO383 | FTO | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-08-22 20:34 UTC | 2026-08-22 21:12 UTC | 38m |
| TKR12 | TKR | K4SD (K4SD) | K4SD (K4SD) | 2026-08-22 20:48 UTC | 2026-08-22 21:12 UTC | 23m |
| TORTGA32 | TOR | San Clemente Island Nalf Airport (KNUC) | San Clemente Island Nalf Airport (KNUC) | 2026-08-22 21:02 UTC | 2026-08-22 21:08 UTC | 5m |
| VKG615 | VKG | Antalya International Airport (LTAI) | Cengiz Topel Airport (LTBQ) | 2026-08-22 20:32 UTC | 2026-08-22 21:07 UTC | 34m |
| N490NW |  | Daniel K Inouye International Airport (PHNL) | Kawaihapai Airfield (PHDH) | 2026-08-22 20:49 UTC | 2026-08-22 21:07 UTC | 18m |
| NOZ5KH | Norwegian Air | Belgrade Nikola Tesla Airport (LYBE) | Mirosławiec Military Air Base (EPMI) | 2026-08-22 19:53 UTC | 2026-08-22 21:06 UTC | 1h 13m |
| TKR181 | TKR | Roberts Field/Redmond Municipal Airport (KRDM) | Hoverhawk Ranch Airport (WN17) | 2026-08-22 20:28 UTC | 2026-08-22 21:02 UTC | 34m |
| N527DR |  | Mountain Valley Airport (KL94) | Porter Ranch Airport (68CN) | 2026-08-22 19:24 UTC | 2026-08-22 21:01 UTC | 1h 37m |
| N65DJ |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-22 18:59 UTC | 2026-08-22 21:01 UTC | 2h 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
