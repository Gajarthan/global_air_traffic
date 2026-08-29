# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_10:22:24_UTC-green)

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

**Latest saved flight:** 2026-08-29 10:22:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-29 10:22:24 UTC

- **240,707** saved flights
- **73,078** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **240,707** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,897,675.6 tonnes** estimated CO2 emissions
- **167,981,197 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9658 |
| 2 | SkyWest Airlines | 8444 |
| 3 | EJA | 4658 |
| 4 | IndiGo | 4064 |
| 5 | American Airlines | 3878 |
| 6 | Southwest Airlines | 3624 |
| 7 | Delta Air Lines | 3065 |
| 8 | ENY | 2903 |
| 9 | LATAM Airlines | 2310 |
| 10 | AZU | 2240 |
| 11 | Vueling | 2067 |
| 12 | Lufthansa | 1938 |
| 13 | WIF | 1908 |
| 14 | LXJ | 1869 |
| 15 | easyJet | 1677 |
| 16 | Swiss International | 1623 |
| 17 | AXM | 1597 |
| 18 | EJU | 1541 |
| 19 | QLK | 1538 |
| 20 | United Airlines | 1513 |
| 21 | Alaska Airlines | 1438 |
| 22 | All Nippon Airways | 1429 |
| 23 | WMT | 1354 |
| 24 | GLO | 1340 |
| 25 | VIV | 1321 |
| 26 | Air France | 1317 |
| 27 | PGT | 1315 |
| 28 | Wizz Air | 1295 |
| 29 | AEE | 1191 |
| 30 | JetBlue | 1190 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 199373 |
| 2 | 🇪🇸 ES | 15484 |
| 3 | 🇧🇷 BR | 14033 |
| 4 | 🇦🇺 AU | 13675 |
| 5 | 🇨🇦 CA | 13385 |
| 6 | 🇮🇹 IT | 13164 |
| 7 | 🇮🇳 IN | 12650 |
| 8 | 🇩🇪 DE | 11884 |
| 9 | 🇬🇧 GB | 11378 |
| 10 | 🇨🇴 CO | 10339 |
| 11 | 🇫🇷 FR | 9707 |
| 12 | 🇯🇵 JP | 9686 |
| 13 | 🇹🇷 TR | 7145 |
| 14 | 🇬🇷 GR | 7092 |
| 15 | 🇲🇽 MX | 6653 |
| 16 | 🇨🇭 CH | 6450 |
| 17 | 🇳🇴 NO | 5943 |
| 18 | 🇹🇭 TH | 4376 |
| 19 | 🇲🇾 MY | 4278 |
| 20 | 🇿🇦 ZA | 4215 |
| 21 | 🇵🇱 PL | 4033 |
| 22 | 🇳🇿 NZ | 3310 |
| 23 | 🇵🇭 PH | 3307 |
| 24 | 🇬🇹 GT | 3026 |
| 25 | 🇰🇷 KR | 2849 |
| 26 | 🇭🇷 HR | 2779 |
| 27 | 🇲🇦 MA | 2432 |
| 28 | 🇲🇪 ME | 2251 |
| 29 | 🇳🇱 NL | 2180 |
| 30 | 🇮🇩 ID | 2112 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4968 |
| 2 | Denver International Airport |  | US | 3882 |
| 3 | Indira Gandhi International Airport |  | IN | 2944 |
| 4 | Tokyo International Airport |  | JP | 2883 |
| 5 | Guaymaral Airport |  | CO | 2696 |
| 6 | Harry Reid International Airport |  | US | 2556 |
| 7 | Zurich Airport |  | CH | 2524 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2461 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2402 |
| 10 | El Dorado International Airport |  | CO | 2339 |
| 11 | La Aurora Airport |  | GT | 2306 |
| 12 | Chicago O'Hare International Airport |  | US | 2143 |
| 13 | Salt Lake City International Airport |  | US | 2121 |
| 14 | Congonhas Airport |  | BR | 2052 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1998 |
| 16 | Frankfurt am Main International Airport |  | DE | 1904 |
| 17 | Capua Airport |  | IT | 1898 |
| 18 | Madrid Barajas International Airport |  | ES | 1897 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1810 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1768 |
| 21 | Malpensa International Airport |  | IT | 1721 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1696 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1689 |
| 24 | Charles de Gaulle International Airport |  | FR | 1686 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1606 |
| 27 | Kuala Lumpur International Airport |  | MY | 1545 |
| 28 | Charlotte/Douglas International Airport |  | US | 1539 |
| 29 | Barcelona International Airport |  | ES | 1534 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1533 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1455 |
| 32 | Viracopos International Airport |  | BR | 1434 |
| 33 | Don Mueang International Airport |  | TH | 1410 |
| 34 | Bengaluru International Airport |  | IN | 1406 |
| 35 | Seattle-Tacoma International Airport |  | US | 1404 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1402 |
| 37 | Calgary International Airport |  | CA | 1381 |
| 38 | Oslo Gardermoen Airport |  | NO | 1350 |
| 39 | Vancouver International Airport |  | CA | 1324 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1316 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1092 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 886 | 21m | 244 km | 3,730.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 620 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 612 | 24m | 225 km | 2,374.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 610 | 1h 6m | 770 km | 8,103.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 544 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 398 | 27m | 275 km | 1,886.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 379 | 1h 50m | 1,423 km | 9,301.3 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 367 | 44m | 555 km | 3,514.2 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 365 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 349 | 44m | 241 km | 1,449.7 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 328 | 24m | 218 km | 1,235.7 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 320 | 1h 40m | 1,156 km | 6,383.9 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 299 | 19m | 99 km | 512.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 294 | 26m | 215 km | 1,088.9 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 279 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 279 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 274 | 1h 14m | 961 km | 4,541.7 t |
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
| SWR8KW | Swiss International | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Zurich Airport (LSZH) | 2026-08-29 09:20 UTC | 2026-08-29 10:22 UTC | 1h 1m |
| EIN151 | Aer Lingus | Belfast International Airport (EGAA) | Dublin Airport (EIDW) | 2026-08-29 09:57 UTC | 2026-08-29 10:22 UTC | 24m |
| ICC03 | ICC | Sabadell Airport (LELL) | Ste Leocadie Airport (LFYS) | 2026-08-29 07:28 UTC | 2026-08-29 10:15 UTC | 2h 47m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-08-28 22:35 UTC | 2026-08-29 10:03 UTC | 11h 27m |
| SWR431 | Swiss International | London Gatwick Airport (EGKK) | Zurich Airport (LSZH) | 2026-08-29 08:48 UTC | 2026-08-29 10:01 UTC | 1h 13m |
| RYR4588 | Ryanair | Katowice International Airport (EPKT) | Aarhus Airport (EKAH) | 2026-08-29 08:46 UTC | 2026-08-29 09:54 UTC | 1h 8m |
| EZY96BC | easyJet | Inverness Airport (EGPE) | London Luton Airport (EGGW) | 2026-08-29 08:48 UTC | 2026-08-29 09:54 UTC | 1h 5m |
| STW171 | STW | Cardak Airport (LTAY) | Smolensk North Airport (XUBS) | 2026-08-29 07:05 UTC | 2026-08-29 09:52 UTC | 2h 47m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-29 09:35 UTC | 2026-08-29 09:47 UTC | 12m |
| IGO273W | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Lengpui Airport (VELP) | 2026-08-29 09:01 UTC | 2026-08-29 09:47 UTC | 45m |
| SWR5KP | Swiss International | Barcelona International Airport (LEBL) | Zurich Airport (LSZH) | 2026-08-29 08:21 UTC | 2026-08-29 09:46 UTC | 1h 25m |
| EZY17NC | easyJet | Geneva Cointrin International Airport (LSGG) | Bristol International Airport (EGGD) | 2026-08-29 08:17 UTC | 2026-08-29 09:45 UTC | 1h 27m |
| EZY26ZK | easyJet | Belfast International Airport (EGAA) | Calaf-Sallavinera Airport (LECF) | 2026-08-29 07:33 UTC | 2026-08-29 09:44 UTC | 2h 10m |
| OKBIR | OKB | Ostrava Leos Janacek Airport (LKMT) | Prerov Air Base (LKPO) | 2026-08-29 08:41 UTC | 2026-08-29 09:43 UTC | 1h 1m |
| NYT876 | NYT | Manang Airport (VNMA) | Bharatpur Airport (VNBP) | 2026-08-29 09:26 UTC | 2026-08-29 09:38 UTC | 11m |
| LLR860 | LLR | Pilani New Airport (VI70) | Jaipur International Airport (VIJP) | 2026-08-29 09:02 UTC | 2026-08-29 09:36 UTC | 34m |
| RNA409 | RNA | Tribhuvan International Airport (VNKT) | Zhuhai Airport (ZGSD) | 2026-08-29 05:30 UTC | 2026-08-29 09:35 UTC | 4h 5m |
| IGO1155 | IndiGo | Indira Gandhi International Airport (VIDP) | Simara Airport (VNSI) | 2026-08-29 08:24 UTC | 2026-08-29 09:34 UTC | 1h 10m |
| IBE07VN | Iberia | Madrid Barajas International Airport (LEMD) | Vienna International Airport (LOWW) | 2026-08-29 06:59 UTC | 2026-08-29 09:33 UTC | 2h 34m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-29 09:10 UTC | 2026-08-29 09:33 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
