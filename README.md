# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_09:30:54_UTC-green)

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

**Latest saved flight:** 2026-09-03 09:30:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-03 09:30:54 UTC

- **245,616** saved flights
- **74,190** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **245,616** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,957,574.2 tonnes** estimated CO2 emissions
- **171,453,575 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9852 |
| 2 | SkyWest Airlines | 8596 |
| 3 | EJA | 4736 |
| 4 | IndiGo | 4115 |
| 5 | American Airlines | 3942 |
| 6 | Southwest Airlines | 3678 |
| 7 | Delta Air Lines | 3122 |
| 8 | ENY | 2944 |
| 9 | LATAM Airlines | 2360 |
| 10 | AZU | 2281 |
| 11 | Vueling | 2103 |
| 12 | Lufthansa | 1967 |
| 13 | WIF | 1961 |
| 14 | LXJ | 1898 |
| 15 | easyJet | 1707 |
| 16 | Swiss International | 1655 |
| 17 | AXM | 1616 |
| 18 | EJU | 1581 |
| 19 | QLK | 1577 |
| 20 | United Airlines | 1546 |
| 21 | Alaska Airlines | 1468 |
| 22 | All Nippon Airways | 1448 |
| 23 | WMT | 1384 |
| 24 | GLO | 1370 |
| 25 | PGT | 1346 |
| 26 | VIV | 1346 |
| 27 | Air France | 1343 |
| 28 | Wizz Air | 1330 |
| 29 | JetBlue | 1212 |
| 30 | AEE | 1211 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 203480 |
| 2 | 🇪🇸 ES | 15767 |
| 3 | 🇧🇷 BR | 14312 |
| 4 | 🇦🇺 AU | 13986 |
| 5 | 🇨🇦 CA | 13671 |
| 6 | 🇮🇹 IT | 13458 |
| 7 | 🇮🇳 IN | 12830 |
| 8 | 🇩🇪 DE | 12114 |
| 9 | 🇬🇧 GB | 11580 |
| 10 | 🇨🇴 CO | 10657 |
| 11 | 🇫🇷 FR | 9912 |
| 12 | 🇯🇵 JP | 9773 |
| 13 | 🇹🇷 TR | 7300 |
| 14 | 🇬🇷 GR | 7246 |
| 15 | 🇲🇽 MX | 6775 |
| 16 | 🇨🇭 CH | 6607 |
| 17 | 🇳🇴 NO | 6089 |
| 18 | 🇹🇭 TH | 4440 |
| 19 | 🇲🇾 MY | 4329 |
| 20 | 🇿🇦 ZA | 4265 |
| 21 | 🇵🇱 PL | 4120 |
| 22 | 🇳🇿 NZ | 3369 |
| 23 | 🇵🇭 PH | 3361 |
| 24 | 🇬🇹 GT | 3075 |
| 25 | 🇰🇷 KR | 2878 |
| 26 | 🇭🇷 HR | 2827 |
| 27 | 🇲🇦 MA | 2480 |
| 28 | 🇲🇪 ME | 2298 |
| 29 | 🇳🇱 NL | 2226 |
| 30 | 🇮🇩 ID | 2140 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5057 |
| 2 | Denver International Airport |  | US | 3964 |
| 3 | Indira Gandhi International Airport |  | IN | 2994 |
| 4 | Tokyo International Airport |  | JP | 2914 |
| 5 | Guaymaral Airport |  | CO | 2718 |
| 6 | Harry Reid International Airport |  | US | 2614 |
| 7 | Zurich Airport |  | CH | 2579 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2496 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2448 |
| 10 | El Dorado International Airport |  | CO | 2428 |
| 11 | La Aurora Airport |  | GT | 2340 |
| 12 | Salt Lake City International Airport |  | US | 2178 |
| 13 | Chicago O'Hare International Airport |  | US | 2163 |
| 14 | Congonhas Airport |  | BR | 2100 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2028 |
| 16 | Frankfurt am Main International Airport |  | DE | 1936 |
| 17 | Capua Airport |  | IT | 1930 |
| 18 | Madrid Barajas International Airport |  | ES | 1928 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1844 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1804 |
| 21 | Malpensa International Airport |  | IT | 1759 |
| 22 | Charles de Gaulle International Airport |  | FR | 1728 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 1725 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1724 |
| 25 | Ninoy Aquino International Airport |  | PH | 1635 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1588 |
| 28 | Charlotte/Douglas International Airport |  | US | 1565 |
| 29 | Kuala Lumpur International Airport |  | MY | 1560 |
| 30 | Barcelona International Airport |  | ES | 1556 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1492 |
| 32 | Viracopos International Airport |  | BR | 1457 |
| 33 | Seattle-Tacoma International Airport |  | US | 1443 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1427 |
| 35 | Don Mueang International Airport |  | TH | 1427 |
| 36 | Bengaluru International Airport |  | IN | 1421 |
| 37 | Calgary International Airport |  | CA | 1415 |
| 38 | Oslo Gardermoen Airport |  | NO | 1384 |
| 39 | Vancouver International Airport |  | CA | 1369 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1342 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 909 | 21m | 244 km | 3,827.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 638 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 625 | 24m | 225 km | 2,424.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 618 | 1h 6m | 770 km | 8,209.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 551 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 405 | 27m | 275 km | 1,919.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 388 | 1h 50m | 1,423 km | 9,522.1 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 379 | 44m | 555 km | 3,629.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 361 | 44m | 241 km | 1,499.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 339 | 24m | 218 km | 1,277.1 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 329 | 1h 39m | 1,156 km | 6,563.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 328 | 22m | 55 km | 311.8 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 303 | 19m | 99 km | 519.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 300 | 27m | 215 km | 1,111.1 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 290 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 284 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 283 | 1h 14m | 961 km | 4,690.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 279 | 19m | 144 km | 694.0 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 265 | 1h 50m | 1,304 km | 5,961.8 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 252 | 28m | 152 km | 658.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FGYXV | FGY | Les Sables-d'Olonne Talmont Airport (LFOO) | Les Sables-d'Olonne Talmont Airport (LFOO) | 2026-09-03 09:11 UTC | 2026-09-03 09:30 UTC | 19m |
| HBZZZ | HBZ | Hausen am Albis Airport (LSZN) | Hausen am Albis Airport (LSZN) | 2026-09-03 09:13 UTC | 2026-09-03 09:29 UTC | 16m |
| UBG218 | UBG | VGZR (VGZR) | Naypyidaw Airport (VYEL) | 2026-09-03 04:21 UTC | 2026-09-03 09:19 UTC | 4h 57m |
| OAL4MS | OAL | Eleftherios Venizelos International Airport (LGAV) | Milos Airport (LGML) | 2026-09-03 08:59 UTC | 2026-09-03 09:17 UTC | 17m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-09-03 08:25 UTC | 2026-09-03 09:08 UTC | 42m |
| HBXTP | HBX | Wangen-Lachen Airport (LSPV) | Meiringen Airport (LSMM) | 2026-09-03 08:16 UTC | 2026-09-03 08:58 UTC | 42m |
| IGO1157 | IndiGo | Juhu Aerodrome (VAJJ) | Tribhuvan International Airport (VNKT) | 2026-09-03 06:28 UTC | 2026-09-03 08:48 UTC | 2h 19m |
| OKHTO | OKH | Straubing Airport (EDMS) | Straubing Airport (EDMS) | 2026-09-03 08:18 UTC | 2026-09-03 08:39 UTC | 21m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Melanes Airport (BIMN) | 2026-09-03 08:15 UTC | 2026-09-03 08:38 UTC | 22m |
| RSQ08 | RSQ | Zuienkerke Airport (EBZU) | Rotterdam Airport (EHRD) | 2026-09-03 08:14 UTC | 2026-09-03 08:37 UTC | 23m |
| EZY527C | easyJet | Newcastle Airport (EGNT) | Bristol International Airport (EGGD) | 2026-09-03 07:51 UTC | 2026-09-03 08:37 UTC | 45m |
| HNL24A | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-09-03 07:56 UTC | 2026-09-03 08:33 UTC | 36m |
| RYR7JA | Ryanair | Malaga Airport (LEMG) | Vienna International Airport (LOWW) | 2026-09-03 05:28 UTC | 2026-09-03 08:31 UTC | 3h 3m |
| NOZ30BF | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Kiruna Airport (ESNQ) | 2026-09-03 07:05 UTC | 2026-09-03 08:29 UTC | 1h 24m |
| RYR33RX | Ryanair | Dublin Airport (EIDW) | Decimomannu Airport (LIED) | 2026-09-03 06:07 UTC | 2026-09-03 08:29 UTC | 2h 21m |
| S5DYG |  | Lesce Bled Glider Airport (LJBL) | Lesce Bled Glider Airport (LJBL) | 2026-09-03 08:08 UTC | 2026-09-03 08:27 UTC | 19m |
| CONDR31 | CON | Getafe Air Base (LEGT) | Albacete-Los Llanos Airport (LEAB) | 2026-09-03 07:53 UTC | 2026-09-03 08:27 UTC | 33m |
| ECISV | ECI | Ampuriabrava Airport (LEAP) | Ampuriabrava Airport (LEAP) | 2026-09-03 08:13 UTC | 2026-09-03 08:26 UTC | 13m |
| BELIGOUY | Brussels Airlines | Caen-Carpiquet Airport (LFRK) | Caen-Carpiquet Airport (LFRK) | 2026-09-03 08:19 UTC | 2026-09-03 08:25 UTC | 5m |
| SAS71K | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Malpensa International Airport (LIMC) | 2026-09-03 06:40 UTC | 2026-09-03 08:25 UTC | 1h 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
