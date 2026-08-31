# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_14:02:12_UTC-green)

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

**Latest saved flight:** 2026-08-31 14:02:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-31 14:02:12 UTC

- **242,822** saved flights
- **73,629** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **242,822** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,922,193.9 tonnes** estimated CO2 emissions
- **169,402,544 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9757 |
| 2 | SkyWest Airlines | 8507 |
| 3 | EJA | 4698 |
| 4 | IndiGo | 4082 |
| 5 | American Airlines | 3909 |
| 6 | Southwest Airlines | 3646 |
| 7 | Delta Air Lines | 3098 |
| 8 | ENY | 2925 |
| 9 | LATAM Airlines | 2327 |
| 10 | AZU | 2256 |
| 11 | Vueling | 2082 |
| 12 | Lufthansa | 1951 |
| 13 | WIF | 1928 |
| 14 | LXJ | 1880 |
| 15 | easyJet | 1693 |
| 16 | Swiss International | 1638 |
| 17 | AXM | 1602 |
| 18 | EJU | 1560 |
| 19 | QLK | 1550 |
| 20 | United Airlines | 1525 |
| 21 | Alaska Airlines | 1451 |
| 22 | All Nippon Airways | 1434 |
| 23 | WMT | 1367 |
| 24 | GLO | 1355 |
| 25 | PGT | 1330 |
| 26 | VIV | 1330 |
| 27 | Air France | 1326 |
| 28 | Wizz Air | 1317 |
| 29 | AEE | 1201 |
| 30 | JetBlue | 1200 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 201125 |
| 2 | 🇪🇸 ES | 15615 |
| 3 | 🇧🇷 BR | 14150 |
| 4 | 🇦🇺 AU | 13785 |
| 5 | 🇨🇦 CA | 13501 |
| 6 | 🇮🇹 IT | 13307 |
| 7 | 🇮🇳 IN | 12710 |
| 8 | 🇩🇪 DE | 11986 |
| 9 | 🇬🇧 GB | 11470 |
| 10 | 🇨🇴 CO | 10483 |
| 11 | 🇫🇷 FR | 9799 |
| 12 | 🇯🇵 JP | 9717 |
| 13 | 🇹🇷 TR | 7215 |
| 14 | 🇬🇷 GR | 7166 |
| 15 | 🇲🇽 MX | 6694 |
| 16 | 🇨🇭 CH | 6538 |
| 17 | 🇳🇴 NO | 6007 |
| 18 | 🇹🇭 TH | 4397 |
| 19 | 🇲🇾 MY | 4297 |
| 20 | 🇿🇦 ZA | 4233 |
| 21 | 🇵🇱 PL | 4086 |
| 22 | 🇳🇿 NZ | 3340 |
| 23 | 🇵🇭 PH | 3326 |
| 24 | 🇬🇹 GT | 3059 |
| 25 | 🇰🇷 KR | 2860 |
| 26 | 🇭🇷 HR | 2802 |
| 27 | 🇲🇦 MA | 2460 |
| 28 | 🇲🇪 ME | 2269 |
| 29 | 🇳🇱 NL | 2196 |
| 30 | 🇮🇩 ID | 2118 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5012 |
| 2 | Denver International Airport |  | US | 3910 |
| 3 | Indira Gandhi International Airport |  | IN | 2960 |
| 4 | Tokyo International Airport |  | JP | 2892 |
| 5 | Guaymaral Airport |  | CO | 2705 |
| 6 | Harry Reid International Airport |  | US | 2578 |
| 7 | Zurich Airport |  | CH | 2551 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2480 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2426 |
| 10 | El Dorado International Airport |  | CO | 2378 |
| 11 | La Aurora Airport |  | GT | 2328 |
| 12 | Chicago O'Hare International Airport |  | US | 2149 |
| 13 | Salt Lake City International Airport |  | US | 2143 |
| 14 | Congonhas Airport |  | BR | 2070 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2010 |
| 16 | Frankfurt am Main International Airport |  | DE | 1920 |
| 17 | Capua Airport |  | IT | 1912 |
| 18 | Madrid Barajas International Airport |  | ES | 1907 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1821 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1786 |
| 21 | Malpensa International Airport |  | IT | 1736 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1717 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1703 |
| 24 | Charles de Gaulle International Airport |  | FR | 1701 |
| 25 | Macau International Airport |  | MO | 1618 |
| 26 | Ninoy Aquino International Airport |  | PH | 1617 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1554 |
| 28 | Charlotte/Douglas International Airport |  | US | 1551 |
| 29 | Kuala Lumpur International Airport |  | MY | 1549 |
| 30 | Barcelona International Airport |  | ES | 1544 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1468 |
| 32 | Viracopos International Airport |  | BR | 1444 |
| 33 | Seattle-Tacoma International Airport |  | US | 1422 |
| 34 | Don Mueang International Airport |  | TH | 1416 |
| 35 | Bengaluru International Airport |  | IN | 1410 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1408 |
| 37 | Calgary International Airport |  | CA | 1393 |
| 38 | Oslo Gardermoen Airport |  | NO | 1366 |
| 39 | Vancouver International Airport |  | CA | 1346 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1325 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1096 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 895 | 21m | 244 km | 3,768.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 627 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 617 | 24m | 225 km | 2,393.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 614 | 1h 6m | 770 km | 8,156.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 548 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 399 | 27m | 275 km | 1,890.7 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 382 | 1h 50m | 1,423 km | 9,374.9 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 371 | 44m | 555 km | 3,552.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 354 | 44m | 241 km | 1,470.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 347 | 21m | 250 km | 1,498.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 334 | 24m | 218 km | 1,258.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 322 | 1h 40m | 1,156 km | 6,423.8 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 302 | 19m | 99 km | 517.3 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 296 | 26m | 215 km | 1,096.3 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 286 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 281 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 279 | 1h 14m | 961 km | 4,624.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 274 | 19m | 144 km | 681.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 265 | 15m | 154 km | 702.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 261 | 1h 50m | 1,304 km | 5,871.8 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N261PJ |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-31 13:28 UTC | 2026-08-31 14:02 UTC | 33m |
| N470AK |  | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-08-31 13:20 UTC | 2026-08-31 14:00 UTC | 40m |
| JANET88 | JAN | NV11 (NV11) | Harry Reid International Airport (KLAS) | 2026-08-31 13:13 UTC | 2026-08-31 14:00 UTC | 47m |
| N748RE |  | Waukegan Ntl Airport (KUGN) | Rhinelander/Oneida County Airport (KRHI) | 2026-08-31 12:58 UTC | 2026-08-31 13:59 UTC | 1h 1m |
| HBZYQ | HBZ | Bad Ragaz Airport (LSZE) | Bad Ragaz Airport (LSZE) | 2026-08-31 13:25 UTC | 2026-08-31 13:59 UTC | 33m |
| ECA4MR | ECA | London Biggin Hill Airport (EGKB) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-31 12:05 UTC | 2026-08-31 13:58 UTC | 1h 53m |
| N356BG |  | Wood County Regional Airport (K1G0) | Wood County Regional Airport (K1G0) | 2026-08-31 12:26 UTC | 2026-08-31 13:58 UTC | 1h 31m |
| RYR20KX | Ryanair | Palma De Mallorca Airport (LEPA) | Bristol International Airport (EGGD) | 2026-08-31 11:20 UTC | 2026-08-31 13:58 UTC | 2h 37m |
| EJU53EH | EJU | Toulouse-Blagnac Airport (LFBO) | Paris-Orly Airport (LFPO) | 2026-08-31 12:10 UTC | 2026-08-31 13:56 UTC | 1h 46m |
| LXJ581 | LXJ | Chicago Midway International Airport (KMDW) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-31 12:06 UTC | 2026-08-31 13:56 UTC | 1h 50m |
| AUA11Q | Austrian Airlines | Vienna International Airport (LOWW) | Graz Airport (LOWG) | 2026-08-31 13:04 UTC | 2026-08-31 13:56 UTC | 52m |
| FFL1728 | FFL | 4AL2 (4AL2) | Clark Field (LA15) | 2026-08-31 12:54 UTC | 2026-08-31 13:56 UTC | 1h 1m |
| CTM1481 | CTM | Castres-Mazamet Airport (LFCK) | Toulouse-Francazal (BA 101) Air Base (LFBF) | 2026-08-31 13:10 UTC | 2026-08-31 13:56 UTC | 45m |
| N962AU |  | Auburn University Regional Airport (KAUO) | Sommerset Strip (AL89) | 2026-08-31 12:12 UTC | 2026-08-31 13:55 UTC | 1h 43m |
| SEH415 | SEH | Tripolis Airport (LGTP) | Eleftherios Venizelos International Airport (LGAV) | 2026-08-31 13:42 UTC | 2026-08-31 13:54 UTC | 12m |
| WZZ5DH | Wizz Air | Sofia Airport (LBSF) | Vodochody Airport (LKVO) | 2026-08-31 11:33 UTC | 2026-08-31 13:54 UTC | 2h 20m |
| HBKGO | HBK | Bern Belp Airport (LSZB) | Bern Belp Airport (LSZB) | 2026-08-31 12:40 UTC | 2026-08-31 13:54 UTC | 1h 14m |
| RYR2BH | Ryanair | Madrid Barajas International Airport (LEMD) | Manchester Airport (EGCC) | 2026-08-31 11:06 UTC | 2026-08-31 13:54 UTC | 2h 48m |
| EJU36YR | EJU | Palma De Mallorca Airport (LEPA) | Dittingen Airport (LSPD) | 2026-08-31 11:50 UTC | 2026-08-31 13:52 UTC | 2h 2m |
| JZA7953 | JZA | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Billy Bishop Toronto City Airport (CYTZ) | 2026-08-31 11:32 UTC | 2026-08-31 13:52 UTC | 2h 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
