# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_09:18:36_UTC-green)

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

**Latest saved flight:** 2026-08-16 09:18:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 09:18:36 UTC

- **204,035** saved flights
- **65,302** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **204,035** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,452,058.5 tonnes** estimated CO2 emissions
- **142,148,318 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8024 |
| 2 | SkyWest Airlines | 7351 |
| 3 | EJA | 3956 |
| 4 | IndiGo | 3483 |
| 5 | American Airlines | 3400 |
| 6 | Southwest Airlines | 3304 |
| 7 | Delta Air Lines | 2611 |
| 8 | ENY | 2548 |
| 9 | LATAM Airlines | 1907 |
| 10 | AZU | 1837 |
| 11 | Lufthansa | 1738 |
| 12 | Vueling | 1688 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1606 |
| 15 | easyJet | 1404 |
| 16 | Swiss International | 1357 |
| 17 | AXM | 1328 |
| 18 | United Airlines | 1292 |
| 19 | Alaska Airlines | 1275 |
| 20 | QLK | 1259 |
| 21 | EJU | 1248 |
| 22 | All Nippon Airways | 1242 |
| 23 | VIV | 1119 |
| 24 | GLO | 1094 |
| 25 | Air France | 1085 |
| 26 | PGT | 1083 |
| 27 | JetBlue | 1051 |
| 28 | AEE | 1041 |
| 29 | WMT | 1015 |
| 30 | CXK | 1011 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 173786 |
| 2 | 🇪🇸 ES | 13029 |
| 3 | 🇧🇷 BR | 11646 |
| 4 | 🇦🇺 AU | 11470 |
| 5 | 🇨🇦 CA | 11281 |
| 6 | 🇮🇳 IN | 10876 |
| 7 | 🇮🇹 IT | 10571 |
| 8 | 🇩🇪 DE | 10087 |
| 9 | 🇬🇧 GB | 9483 |
| 10 | 🇯🇵 JP | 8401 |
| 11 | 🇫🇷 FR | 8070 |
| 12 | 🇨🇴 CO | 8046 |
| 13 | 🇬🇷 GR | 5995 |
| 14 | 🇲🇽 MX | 5741 |
| 15 | 🇹🇷 TR | 5708 |
| 16 | 🇨🇭 CH | 5454 |
| 17 | 🇳🇴 NO | 5080 |
| 18 | 🇲🇾 MY | 3491 |
| 19 | 🇿🇦 ZA | 3392 |
| 20 | 🇵🇱 PL | 3343 |
| 21 | 🇹🇭 TH | 3211 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2712 |
| 24 | 🇬🇹 GT | 2556 |
| 25 | 🇰🇷 KR | 2491 |
| 26 | 🇭🇷 HR | 2155 |
| 27 | 🇲🇦 MA | 2045 |
| 28 | 🇳🇱 NL | 1811 |
| 29 | 🇲🇪 ME | 1698 |
| 30 | 🇮🇩 ID | 1670 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4287 |
| 2 | Denver International Airport |  | US | 3339 |
| 3 | Tokyo International Airport |  | JP | 2537 |
| 4 | Guaymaral Airport |  | CO | 2476 |
| 5 | Indira Gandhi International Airport |  | IN | 2469 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2133 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2118 |
| 9 | Zurich Airport |  | CH | 2117 |
| 10 | La Aurora Airport |  | GT | 1958 |
| 11 | Chicago O'Hare International Airport |  | US | 1903 |
| 12 | El Dorado International Airport |  | CO | 1861 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1827 |
| 14 | Salt Lake City International Airport |  | US | 1808 |
| 15 | Congonhas Airport |  | BR | 1694 |
| 16 | Frankfurt am Main International Airport |  | DE | 1693 |
| 17 | Madrid Barajas International Airport |  | ES | 1593 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1564 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1555 |
| 20 | Capua Airport |  | IT | 1546 |
| 21 | Macau International Airport |  | MO | 1541 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1471 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1435 |
| 24 | Malpensa International Airport |  | IT | 1402 |
| 25 | Charles de Gaulle International Airport |  | FR | 1392 |
| 26 | Charlotte/Douglas International Airport |  | US | 1391 |
| 27 | Kuala Lumpur International Airport |  | MY | 1295 |
| 28 | Ninoy Aquino International Airport |  | PH | 1284 |
| 29 | Bengaluru International Airport |  | IN | 1267 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1257 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1232 |
| 32 | Barcelona International Airport |  | ES | 1219 |
| 33 | Seattle-Tacoma International Airport |  | US | 1212 |
| 34 | Viracopos International Airport |  | BR | 1177 |
| 35 | Calgary International Airport |  | CA | 1157 |
| 36 | Reno/Tahoe International Airport |  | US | 1133 |
| 37 | Oslo Gardermoen Airport |  | NO | 1122 |
| 38 | Vitoria/Foronda Airport |  | ES | 1121 |
| 39 | Daniel K Inouye International Airport |  | US | 1103 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1098 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 496 | 1h 7m | 770 km | 6,589.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 477 | 24m | 225 km | 1,850.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 341 | 27m | 275 km | 1,615.9 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 294 | 1h 49m | 1,423 km | 7,215.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 263 | 21m | 250 km | 1,136.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 253 | 24m | 218 km | 953.2 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 245 | 19m | 99 km | 419.7 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 239 | 1h 37m | 1,156 km | 4,768.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 234 | 19m | 144 km | 582.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 230 | 31m | 369 km | 1,464.0 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 220 | 1h 49m | 1,304 km | 4,949.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OHFMZ | OHF | Lahti Vesivehmaa Airport (EFLA) | Lahti Vesivehmaa Airport (EFLA) | 2026-08-16 08:51 UTC | 2026-08-16 09:18 UTC | 27m |
| FFT4392 | FFT | Phoenix Sky Harbor International Airport (KPHX) | NM21 (NM21) | 2026-08-16 08:22 UTC | 2026-08-16 09:09 UTC | 47m |
| TVF29EN | TVF | Houari Boumediene Airport (DAAG) | Paris-Orly Airport (LFPO) | 2026-08-16 07:11 UTC | 2026-08-16 09:04 UTC | 1h 52m |
| DESAD | DES | Essen Mulheim Airport (EDLE) | Essen Mulheim Airport (EDLE) | 2026-08-16 08:29 UTC | 2026-08-16 08:46 UTC | 16m |
| S5DYG |  | Lesce Bled Glider Airport (LJBL) | Lesce Bled Glider Airport (LJBL) | 2026-08-16 08:18 UTC | 2026-08-16 08:39 UTC | 21m |
| AAR8735 | AAR | Gimpo International Airport (RKSS) | Yeosu Airport (RKJY) | 2026-08-16 08:07 UTC | 2026-08-16 08:38 UTC | 31m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-16 07:39 UTC | 2026-08-16 08:32 UTC | 52m |
| RXA2131 | RXA | Perth International Airport (YPPH) | Frankland Airport (YFRK) | 2026-08-16 07:47 UTC | 2026-08-16 08:30 UTC | 43m |
| RGA08 | RGA | Ambri Airport (LSPM) | Lodrino Air Base (LSML) | 2026-08-16 07:59 UTC | 2026-08-16 08:28 UTC | 28m |
| DKEGL | DKE | Kempten-Durach Airport (EDMK) | Hoefen Airport (LOIR) | 2026-08-16 07:45 UTC | 2026-08-16 08:26 UTC | 41m |
| AXM6082 | AXM | Senai International Airport (WMKJ) | Jendarata Airport (WMAJ) | 2026-08-16 07:48 UTC | 2026-08-16 08:25 UTC | 37m |
| ANA297 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-08-16 07:43 UTC | 2026-08-16 08:25 UTC | 41m |
| OKHEZ | OKH | Sumperk Airport (LKSU) | Sumperk Airport (LKSU) | 2026-08-16 08:03 UTC | 2026-08-16 08:22 UTC | 19m |
| 5YZBS |  | Nairobi Wilson Airport (HKNW) | Naivasha Airport (HKNV) | 2026-08-16 08:10 UTC | 2026-08-16 08:21 UTC | 11m |
| ITY1617 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Gioia Del Colle Airport (LIBV) | 2026-08-16 07:46 UTC | 2026-08-16 08:19 UTC | 32m |
| HERC32 | HER | Amman-Marka International Airport (OJAM) | Arad Airport (LL1B) | 2026-08-16 07:43 UTC | 2026-08-16 08:16 UTC | 33m |
| LLR516 | LLR | Cochin International Airport (VOCI) | Coimbatore Air Force Station (VOSX) | 2026-08-16 07:41 UTC | 2026-08-16 08:15 UTC | 33m |
| SEH1SM | SEH | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-08-16 07:43 UTC | 2026-08-16 08:13 UTC | 30m |
| HFA602 | HFA | Yotvata Airfield (LLYT) | Haifa International Airport (LLHA) | 2026-08-16 07:18 UTC | 2026-08-16 08:10 UTC | 51m |
| ANA697 | All Nippon Airways | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-08-16 07:11 UTC | 2026-08-16 08:09 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
