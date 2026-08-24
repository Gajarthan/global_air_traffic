# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_15:39:16_UTC-green)

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

**Latest saved flight:** 2026-08-24 15:39:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 15:39:16 UTC

- **232,248** saved flights
- **71,433** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **232,248** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,799,736.6 tonnes** estimated CO2 emissions
- **162,303,570 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9328 |
| 2 | SkyWest Airlines | 8210 |
| 3 | EJA | 4482 |
| 4 | IndiGo | 3936 |
| 5 | American Airlines | 3786 |
| 6 | Southwest Airlines | 3577 |
| 7 | Delta Air Lines | 2962 |
| 8 | ENY | 2823 |
| 9 | LATAM Airlines | 2236 |
| 10 | AZU | 2159 |
| 11 | Vueling | 1987 |
| 12 | Lufthansa | 1893 |
| 13 | WIF | 1843 |
| 14 | LXJ | 1825 |
| 15 | easyJet | 1627 |
| 16 | Swiss International | 1556 |
| 17 | AXM | 1551 |
| 18 | EJU | 1486 |
| 19 | United Airlines | 1475 |
| 20 | QLK | 1474 |
| 21 | Alaska Airlines | 1397 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1293 |
| 24 | WMT | 1287 |
| 25 | VIV | 1275 |
| 26 | PGT | 1268 |
| 27 | Air France | 1261 |
| 28 | Wizz Air | 1227 |
| 29 | AEE | 1157 |
| 30 | JetBlue | 1154 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 193228 |
| 2 | 🇪🇸 ES | 14920 |
| 3 | 🇧🇷 BR | 13570 |
| 4 | 🇦🇺 AU | 13162 |
| 5 | 🇨🇦 CA | 12776 |
| 6 | 🇮🇹 IT | 12641 |
| 7 | 🇮🇳 IN | 12260 |
| 8 | 🇩🇪 DE | 11455 |
| 9 | 🇬🇧 GB | 10964 |
| 10 | 🇨🇴 CO | 9666 |
| 11 | 🇯🇵 JP | 9448 |
| 12 | 🇫🇷 FR | 9300 |
| 13 | 🇹🇷 TR | 6864 |
| 14 | 🇬🇷 GR | 6839 |
| 15 | 🇲🇽 MX | 6447 |
| 16 | 🇨🇭 CH | 6200 |
| 17 | 🇳🇴 NO | 5741 |
| 18 | 🇲🇾 MY | 4143 |
| 19 | 🇹🇭 TH | 4108 |
| 20 | 🇿🇦 ZA | 4063 |
| 21 | 🇵🇱 PL | 3865 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3184 |
| 24 | 🇬🇹 GT | 2920 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2674 |
| 27 | 🇲🇦 MA | 2357 |
| 28 | 🇲🇪 ME | 2140 |
| 29 | 🇳🇱 NL | 2084 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4824 |
| 2 | Denver International Airport |  | US | 3764 |
| 3 | Indira Gandhi International Airport |  | IN | 2835 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2666 |
| 6 | Harry Reid International Airport |  | US | 2496 |
| 7 | Zurich Airport |  | CH | 2427 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2368 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2335 |
| 10 | La Aurora Airport |  | GT | 2224 |
| 11 | El Dorado International Airport |  | CO | 2154 |
| 12 | Chicago O'Hare International Airport |  | US | 2097 |
| 13 | Salt Lake City International Airport |  | US | 2042 |
| 14 | Congonhas Airport |  | BR | 1978 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1959 |
| 16 | Frankfurt am Main International Airport |  | DE | 1853 |
| 17 | Capua Airport |  | IT | 1826 |
| 18 | Madrid Barajas International Airport |  | ES | 1825 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1749 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1720 |
| 21 | Malpensa International Airport |  | IT | 1666 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1658 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1612 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1533 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1467 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1403 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1403 |
| 32 | Viracopos International Airport |  | BR | 1381 |
| 33 | Bengaluru International Airport |  | IN | 1372 |
| 34 | Seattle-Tacoma International Airport |  | US | 1364 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1361 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1317 |
| 38 | Oslo Gardermoen Airport |  | NO | 1302 |
| 39 | O. R. Tambo International Airport |  | ZA | 1262 |
| 40 | Vitoria/Foronda Airport |  | ES | 1259 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1082 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 846 | 21m | 244 km | 3,562.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 570 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 520 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 383 | 27m | 275 km | 1,814.9 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 359 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 359 | 1h 50m | 1,423 km | 8,810.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 338 | 44m | 241 km | 1,404.0 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 308 | 22m | 55 km | 292.7 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 307 | 24m | 218 km | 1,156.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 302 | 1h 38m | 1,156 km | 6,024.8 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 289 | 19m | 99 km | 495.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 283 | 27m | 215 km | 1,048.1 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 268 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 264 | 19m | 144 km | 656.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 251 | 15m | 154 km | 665.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 248 | 1h 50m | 1,304 km | 5,579.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N737GE |  | Warren County/John Lane Field (KI68) | Cincinnati/Northern Kentucky International Airport (KCVG) | 2026-08-24 13:52 UTC | 2026-08-24 15:39 UTC | 1h 46m |
| N2459Y |  | Rhode Island Tf Green International Airport (KPVD) | Westerly State Airport (KWST) | 2026-08-24 15:15 UTC | 2026-08-24 15:37 UTC | 22m |
| 6407R |  | 89LL (89LL) | Yates Airport (IL29) | 2026-08-24 14:39 UTC | 2026-08-24 15:37 UTC | 57m |
| N716AT |  | Ralph Wien Memorial Airport (PAOT) | Shungnak Airport (PAGH) | 2026-08-24 14:45 UTC | 2026-08-24 15:35 UTC | 49m |
| N21272 |  | Ryan Field (KRYN) | Ryan Field (KRYN) | 2026-08-24 14:54 UTC | 2026-08-24 15:34 UTC | 40m |
| N2231E |  | IA17 (IA17) | Iowa City Municipal Airport (KIOW) | 2026-08-24 14:51 UTC | 2026-08-24 15:33 UTC | 41m |
| N6988J |  | Brigham City Regional Airport (KBMC) | Preston Airport (KU10) | 2026-08-24 14:26 UTC | 2026-08-24 15:33 UTC | 1h 6m |
| N1952 |  | Capital City Airport (KCXY) | Lehigh Valley International Airport (KABE) | 2026-08-24 14:55 UTC | 2026-08-24 15:31 UTC | 36m |
| N702PC |  | KU77 (KU77) | Henderson Executive Airport (KHND) | 2026-08-24 14:12 UTC | 2026-08-24 15:31 UTC | 1h 19m |
| N1323X |  | Sky Manor Airport (KN40) | Sky Manor Airport (KN40) | 2026-08-24 15:28 UTC | 2026-08-24 15:28 UTC | 0m |
| N59FM |  | Tucson International Airport (KTUS) | Four Pillars Airport (AZ21) | 2026-08-24 14:51 UTC | 2026-08-24 15:28 UTC | 36m |
| BBG764 | BBG | Ben Gurion International Airport (LLBG) | Heraklion International Nikos Kazantzakis Airport (LGIR) | 2026-08-24 14:11 UTC | 2026-08-24 15:28 UTC | 1h 16m |
| AMMO91 | AMM | Sandy Creek Airport (73TX) | 6TA4 (6TA4) | 2026-08-24 15:02 UTC | 2026-08-24 15:22 UTC | 20m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-24 15:02 UTC | 2026-08-24 15:18 UTC | 16m |
| N7DG |  | Elizabeth City Cg Air Station/Regional Airport (KECG) | Pine Island Airport (7NC2) | 2026-08-24 15:01 UTC | 2026-08-24 15:14 UTC | 13m |
| N215LP |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-08-24 14:45 UTC | 2026-08-24 15:14 UTC | 29m |
| N221FL |  | Trenton Mercer Airport (KTTN) | Trenton-Robbinsville Airport (KN87) | 2026-08-24 14:37 UTC | 2026-08-24 15:13 UTC | 36m |
| DMKCV | DMK | Pirna-Pratzschwitz Airport (EDAR) | Pirna-Pratzschwitz Airport (EDAR) | 2026-08-24 14:57 UTC | 2026-08-24 15:12 UTC | 15m |
| N8410J |  | Lehigh Valley International Airport (KABE) | Lehigh Valley International Airport (KABE) | 2026-08-24 14:50 UTC | 2026-08-24 15:09 UTC | 19m |
| N4511E |  | Reno/Tahoe International Airport (KRNO) | NV44 (NV44) | 2026-08-24 14:25 UTC | 2026-08-24 15:09 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
