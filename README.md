# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_17:14:11_UTC-green)

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

**Latest saved flight:** 2026-09-02 17:14:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-02 17:14:11 UTC

- **244,918** saved flights
- **74,064** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **244,918** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,950,887.0 tonnes** estimated CO2 emissions
- **171,065,911 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9830 |
| 2 | SkyWest Airlines | 8572 |
| 3 | EJA | 4723 |
| 4 | IndiGo | 4104 |
| 5 | American Airlines | 3937 |
| 6 | Southwest Airlines | 3668 |
| 7 | Delta Air Lines | 3113 |
| 8 | ENY | 2940 |
| 9 | LATAM Airlines | 2352 |
| 10 | AZU | 2274 |
| 11 | Vueling | 2099 |
| 12 | Lufthansa | 1962 |
| 13 | WIF | 1959 |
| 14 | LXJ | 1890 |
| 15 | easyJet | 1703 |
| 16 | Swiss International | 1653 |
| 17 | AXM | 1613 |
| 18 | EJU | 1578 |
| 19 | QLK | 1566 |
| 20 | United Airlines | 1540 |
| 21 | Alaska Airlines | 1462 |
| 22 | All Nippon Airways | 1443 |
| 23 | WMT | 1382 |
| 24 | GLO | 1368 |
| 25 | Air France | 1342 |
| 26 | PGT | 1342 |
| 27 | VIV | 1338 |
| 28 | Wizz Air | 1328 |
| 29 | AEE | 1208 |
| 30 | JetBlue | 1207 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 202825 |
| 2 | 🇪🇸 ES | 15736 |
| 3 | 🇧🇷 BR | 14271 |
| 4 | 🇦🇺 AU | 13915 |
| 5 | 🇨🇦 CA | 13624 |
| 6 | 🇮🇹 IT | 13438 |
| 7 | 🇮🇳 IN | 12794 |
| 8 | 🇩🇪 DE | 12095 |
| 9 | 🇬🇧 GB | 11555 |
| 10 | 🇨🇴 CO | 10622 |
| 11 | 🇫🇷 FR | 9895 |
| 12 | 🇯🇵 JP | 9751 |
| 13 | 🇹🇷 TR | 7285 |
| 14 | 🇬🇷 GR | 7228 |
| 15 | 🇲🇽 MX | 6745 |
| 16 | 🇨🇭 CH | 6587 |
| 17 | 🇳🇴 NO | 6080 |
| 18 | 🇹🇭 TH | 4429 |
| 19 | 🇲🇾 MY | 4324 |
| 20 | 🇿🇦 ZA | 4259 |
| 21 | 🇵🇱 PL | 4113 |
| 22 | 🇳🇿 NZ | 3360 |
| 23 | 🇵🇭 PH | 3352 |
| 24 | 🇬🇹 GT | 3073 |
| 25 | 🇰🇷 KR | 2870 |
| 26 | 🇭🇷 HR | 2821 |
| 27 | 🇲🇦 MA | 2475 |
| 28 | 🇲🇪 ME | 2291 |
| 29 | 🇳🇱 NL | 2217 |
| 30 | 🇮🇩 ID | 2137 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5048 |
| 2 | Denver International Airport |  | US | 3941 |
| 3 | Indira Gandhi International Airport |  | IN | 2984 |
| 4 | Tokyo International Airport |  | JP | 2906 |
| 5 | Guaymaral Airport |  | CO | 2717 |
| 6 | Harry Reid International Airport |  | US | 2605 |
| 7 | Zurich Airport |  | CH | 2574 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2492 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2439 |
| 10 | El Dorado International Airport |  | CO | 2418 |
| 11 | La Aurora Airport |  | GT | 2338 |
| 12 | Salt Lake City International Airport |  | US | 2167 |
| 13 | Chicago O'Hare International Airport |  | US | 2162 |
| 14 | Congonhas Airport |  | BR | 2091 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2024 |
| 16 | Frankfurt am Main International Airport |  | DE | 1932 |
| 17 | Capua Airport |  | IT | 1928 |
| 18 | Madrid Barajas International Airport |  | ES | 1923 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1842 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1800 |
| 21 | Malpensa International Airport |  | IT | 1753 |
| 22 | Charles de Gaulle International Airport |  | FR | 1726 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 1722 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1714 |
| 25 | Ninoy Aquino International Airport |  | PH | 1632 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1579 |
| 28 | Charlotte/Douglas International Airport |  | US | 1561 |
| 29 | Kuala Lumpur International Airport |  | MY | 1558 |
| 30 | Barcelona International Airport |  | ES | 1552 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1480 |
| 32 | Viracopos International Airport |  | BR | 1453 |
| 33 | Seattle-Tacoma International Airport |  | US | 1433 |
| 34 | Don Mueang International Airport |  | TH | 1424 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1418 |
| 36 | Bengaluru International Airport |  | IN | 1416 |
| 37 | Calgary International Airport |  | CA | 1409 |
| 38 | Oslo Gardermoen Airport |  | NO | 1382 |
| 39 | Vancouver International Airport |  | CA | 1364 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1339 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 905 | 21m | 244 km | 3,810.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 636 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 623 | 24m | 225 km | 2,416.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 615 | 1h 6m | 770 km | 8,169.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 550 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 403 | 27m | 275 km | 1,909.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 387 | 1h 50m | 1,423 km | 9,497.6 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 376 | 44m | 555 km | 3,600.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 361 | 44m | 241 km | 1,499.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 348 | 21m | 250 km | 1,503.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 336 | 24m | 218 km | 1,265.8 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 327 | 1h 39m | 1,156 km | 6,523.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 325 | 22m | 55 km | 308.9 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 303 | 19m | 99 km | 519.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 300 | 27m | 215 km | 1,111.1 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 289 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 284 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 282 | 1h 14m | 961 km | 4,674.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 278 | 19m | 144 km | 691.5 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 262 | 1h 50m | 1,304 km | 5,894.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 252 | 28m | 152 km | 658.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N929E |  | Okc Will Rogers International Airport (KOKC) | KF29 (KF29) | 2026-09-02 16:13 UTC | 2026-09-02 17:14 UTC | 1h 0m |
| N4881E |  | Downtown Airport (K3DW) | Downtown Airport (K3DW) | 2026-09-02 16:56 UTC | 2026-09-02 17:13 UTC | 16m |
| N272SP |  | Centennial Airport (KAPA) | Circle 8 Ranch Airport (CO42) | 2026-09-02 16:30 UTC | 2026-09-02 17:12 UTC | 42m |
| RVP316 | RVP | Ponte de Sôr Airport (LPSO) | Viseu Airport (LPVZ) | 2026-09-02 15:55 UTC | 2026-09-02 17:10 UTC | 1h 15m |
| SMGLR31 | SMG | Pardubice Airport (LKPD) | Pardubice Airport (LKPD) | 2026-09-02 16:57 UTC | 2026-09-02 17:09 UTC | 11m |
| N999VP |  | Vogen Airport (IS41) | IS95 (IS95) | 2026-09-02 16:46 UTC | 2026-09-02 17:08 UTC | 22m |
| TUI7KT | TUI | Dusseldorf International Airport (EDDL) | Diagoras Airport (LGRP) | 2026-09-02 12:49 UTC | 2026-09-02 17:06 UTC | 4h 17m |
| TIGER66 | TIG | Dunbar Ranch Airport (0XS8) | Dunbar Ranch Airport (0XS8) | 2026-09-02 16:48 UTC | 2026-09-02 17:02 UTC | 14m |
| N358EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-09-02 16:09 UTC | 2026-09-02 17:02 UTC | 52m |
| N697AZ |  | Encarnacion Airport (SGEN) | Encarnacion Airport (SGEN) | 2026-09-02 16:42 UTC | 2026-09-02 17:01 UTC | 19m |
| NIT244 | NIT | Heart Of Georgia Regional Airport (KEZM) | W H 'Bud' Barron Airport (KDBN) | 2026-09-02 16:21 UTC | 2026-09-02 16:59 UTC | 38m |
| CAP4186 | CAP | Smyrna Airport (KMQY) | KM33 (KM33) | 2026-09-02 15:54 UTC | 2026-09-02 16:55 UTC | 1h 0m |
| N862NC |  | Curtis L Brown Jr Field (KEYF) | Moore County Airport (KSOP) | 2026-09-02 16:32 UTC | 2026-09-02 16:54 UTC | 21m |
| N781FA |  | Mc Crory/Morton Airport (2AR4) | WEON (WEON) | 2026-09-02 16:26 UTC | 2026-09-02 16:53 UTC | 27m |
| CXK284 | CXK | Rocky Mountain Metro Airport (KBJC) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-09-02 14:54 UTC | 2026-09-02 16:53 UTC | 1h 59m |
| N880 |  | Whiteman Airport (KWHP) | Camarillo Airport (KCMA) | 2026-09-02 16:28 UTC | 2026-09-02 16:51 UTC | 22m |
| N49EM |  | Fond Du Lac County Airport (KFLD) | Green Bay/Austin Straubel International Airport (KGRB) | 2026-09-02 16:32 UTC | 2026-09-02 16:51 UTC | 18m |
| CGVTS | CGV | Abbotsford Airport (CYXX) | Chilliwack Airport (CYCW) | 2026-09-02 16:34 UTC | 2026-09-02 16:49 UTC | 15m |
| N7259F |  | Hartford-Brainard Airport (KHFD) | Windham Airport (KIJD) | 2026-09-02 16:25 UTC | 2026-09-02 16:49 UTC | 23m |
| N543PD |  | Hayward Executive Airport (KHWD) | Triple R Ranch Airport (6CA1) | 2026-09-02 16:02 UTC | 2026-09-02 16:46 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
