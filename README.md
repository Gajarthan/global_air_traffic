# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_19:04:18_UTC-green)

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

**Latest saved flight:** 2026-08-19 19:04:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 19:04:18 UTC

- **216,892** saved flights
- **68,446** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **216,892** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,609,376.9 tonnes** estimated CO2 emissions
- **151,268,228 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8676 |
| 2 | SkyWest Airlines | 7743 |
| 3 | EJA | 4217 |
| 4 | IndiGo | 3691 |
| 5 | American Airlines | 3613 |
| 6 | Southwest Airlines | 3447 |
| 7 | Delta Air Lines | 2802 |
| 8 | ENY | 2678 |
| 9 | LATAM Airlines | 2053 |
| 10 | AZU | 1986 |
| 11 | Vueling | 1822 |
| 12 | Lufthansa | 1812 |
| 13 | WIF | 1734 |
| 14 | LXJ | 1707 |
| 15 | easyJet | 1506 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1369 |
| 19 | EJU | 1352 |
| 20 | QLK | 1346 |
| 21 | Alaska Airlines | 1327 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1190 |
| 24 | GLO | 1180 |
| 25 | Air France | 1177 |
| 26 | PGT | 1177 |
| 27 | WMT | 1136 |
| 28 | JetBlue | 1105 |
| 29 | Wizz Air | 1103 |
| 30 | AEE | 1088 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 182786 |
| 2 | 🇪🇸 ES | 13918 |
| 3 | 🇧🇷 BR | 12507 |
| 4 | 🇦🇺 AU | 12169 |
| 5 | 🇨🇦 CA | 11936 |
| 6 | 🇮🇹 IT | 11516 |
| 7 | 🇮🇳 IN | 11491 |
| 8 | 🇩🇪 DE | 10750 |
| 9 | 🇬🇧 GB | 10190 |
| 10 | 🇨🇴 CO | 8883 |
| 11 | 🇯🇵 JP | 8870 |
| 12 | 🇫🇷 FR | 8655 |
| 13 | 🇬🇷 GR | 6341 |
| 14 | 🇹🇷 TR | 6239 |
| 15 | 🇲🇽 MX | 6056 |
| 16 | 🇨🇭 CH | 5766 |
| 17 | 🇳🇴 NO | 5394 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3683 |
| 20 | 🇵🇱 PL | 3584 |
| 21 | 🇹🇭 TH | 3539 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2898 |
| 24 | 🇬🇹 GT | 2751 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2377 |
| 27 | 🇲🇦 MA | 2184 |
| 28 | 🇳🇱 NL | 1940 |
| 29 | 🇲🇪 ME | 1892 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4551 |
| 2 | Denver International Airport |  | US | 3528 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2627 |
| 5 | Guaymaral Airport |  | CO | 2588 |
| 6 | Harry Reid International Airport |  | US | 2406 |
| 7 | Zurich Airport |  | CH | 2257 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2227 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2210 |
| 10 | La Aurora Airport |  | GT | 2092 |
| 11 | El Dorado International Airport |  | CO | 2025 |
| 12 | Chicago O'Hare International Airport |  | US | 1992 |
| 13 | Salt Lake City International Airport |  | US | 1911 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1893 |
| 15 | Congonhas Airport |  | BR | 1827 |
| 16 | Frankfurt am Main International Airport |  | DE | 1774 |
| 17 | Madrid Barajas International Airport |  | ES | 1699 |
| 18 | Capua Airport |  | IT | 1651 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1635 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1611 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1593 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Malpensa International Airport |  | IT | 1524 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 25 | Charles de Gaulle International Airport |  | FR | 1491 |
| 26 | Charlotte/Douglas International Airport |  | US | 1457 |
| 27 | Kuala Lumpur International Airport |  | MY | 1378 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1329 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1325 |
| 31 | Bengaluru International Airport |  | IN | 1315 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1293 |
| 33 | Seattle-Tacoma International Airport |  | US | 1283 |
| 34 | Viracopos International Airport |  | BR | 1268 |
| 35 | Calgary International Airport |  | CA | 1220 |
| 36 | Oslo Gardermoen Airport |  | NO | 1202 |
| 37 | Vitoria/Foronda Airport |  | ES | 1202 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1182 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1173 |
| 40 | Don Mueang International Airport |  | TH | 1167 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1059 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 773 | 21m | 244 km | 3,254.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 488 | 13m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 476 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 362 | 27m | 275 km | 1,715.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 318 | 1h 49m | 1,423 km | 7,804.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 316 | 44m | 241 km | 1,312.6 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 293 | 22m | 55 km | 278.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 271 | 19m | 99 km | 464.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 266 | 27m | 215 km | 985.2 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 256 | 1h 14m | 961 km | 4,243.3 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 256 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 253 | 31m | 369 km | 1,610.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 233 | 1h 49m | 1,304 km | 5,241.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N738AZ |  | Riverside Airport (KRAL) | Hemet-Ryan Airport (KHMT) | 2026-08-19 18:44 UTC | 2026-08-19 19:04 UTC | 19m |
| N798BP |  | Sky River Ranch Airport (WA78) | Sky River Ranch Airport (WA78) | 2026-08-19 18:07 UTC | 2026-08-19 19:02 UTC | 55m |
| N41TE |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-08-19 18:25 UTC | 2026-08-19 18:56 UTC | 31m |
| FXC66 | FXC | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-08-19 18:05 UTC | 2026-08-19 18:55 UTC | 49m |
| TXH5749 | TXH | Montréal (Mirabel) Airport (CYMX) | Montréal (Mirabel) Airport (CYMX) | 2026-08-19 18:34 UTC | 2026-08-19 18:52 UTC | 18m |
| N248SF |  | Dupage Airport (KDPA) | Jack W Watson Airport (0IL9) | 2026-08-19 18:32 UTC | 2026-08-19 18:52 UTC | 19m |
| LS16 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-19 17:31 UTC | 2026-08-19 18:51 UTC | 1h 20m |
| N1833L |  | Somerset Airport (KSMQ) | Sky Manor Airport (KN40) | 2026-08-19 18:25 UTC | 2026-08-19 18:51 UTC | 26m |
| N46826 |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-08-19 18:34 UTC | 2026-08-19 18:50 UTC | 15m |
| N733AM |  | Whiteman Airport (KWHP) | Camarillo Airport (KCMA) | 2026-08-19 18:19 UTC | 2026-08-19 18:50 UTC | 30m |
| ASI717 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-08-19 18:34 UTC | 2026-08-19 18:50 UTC | 15m |
| CXK419 | CXK | Harrisburg International Airport (KMDT) | Lancaster Airport (KLNS) | 2026-08-19 18:23 UTC | 2026-08-19 18:48 UTC | 25m |
| SPECK21 | SPE | Enid Woodring Regional Airport (KWDG) | Ramey 1 Airport (0OK8) | 2026-08-19 18:32 UTC | 2026-08-19 18:47 UTC | 15m |
| N216BG |  | Birmingham-Shuttlesworth International Airport (KBHM) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-19 18:16 UTC | 2026-08-19 18:47 UTC | 30m |
| N595GL |  | Livingston County/Spencer J Hardy Airport (KOZW) | Owosso Community Airport (KRNP) | 2026-08-19 18:31 UTC | 2026-08-19 18:43 UTC | 12m |
| N7157G |  | Olive Branch/Taylor Field (KOLV) | Jeter Field (4MS3) | 2026-08-19 18:21 UTC | 2026-08-19 18:42 UTC | 21m |
| N313NR |  | Concord Municipal Airport (KCON) | Concord Municipal Airport (KCON) | 2026-08-19 18:26 UTC | 2026-08-19 18:41 UTC | 15m |
| N739HP |  | Ellison Onizuka Kona International At Keahole Airport (PHKO) | Lanai Airport (PHNY) | 2026-08-19 17:40 UTC | 2026-08-19 18:39 UTC | 58m |
| N498MB |  | Mason City Municipal Airport (KMCW) | Mason City Municipal Airport (KMCW) | 2026-08-19 18:25 UTC | 2026-08-19 18:39 UTC | 13m |
| N944VB |  | Hampton Roads Executive Airport (KPVG) | Hampton Roads Executive Airport (KPVG) | 2026-08-19 18:11 UTC | 2026-08-19 18:38 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
