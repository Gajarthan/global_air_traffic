# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_15:31:36_UTC-green)

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

**Latest saved flight:** 2026-08-19 15:31:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 15:31:36 UTC

- **216,105** saved flights
- **68,277** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **216,105** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,600,357.0 tonnes** estimated CO2 emissions
- **150,745,331 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8641 |
| 2 | SkyWest Airlines | 7711 |
| 3 | EJA | 4191 |
| 4 | IndiGo | 3684 |
| 5 | American Airlines | 3597 |
| 6 | Southwest Airlines | 3435 |
| 7 | Delta Air Lines | 2791 |
| 8 | ENY | 2665 |
| 9 | LATAM Airlines | 2045 |
| 10 | AZU | 1973 |
| 11 | Vueling | 1818 |
| 12 | Lufthansa | 1809 |
| 13 | WIF | 1728 |
| 14 | LXJ | 1699 |
| 15 | easyJet | 1501 |
| 16 | Swiss International | 1441 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1367 |
| 19 | EJU | 1347 |
| 20 | QLK | 1346 |
| 21 | Alaska Airlines | 1324 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1185 |
| 24 | PGT | 1173 |
| 25 | Air France | 1172 |
| 26 | GLO | 1169 |
| 27 | WMT | 1128 |
| 28 | JetBlue | 1101 |
| 29 | Wizz Air | 1099 |
| 30 | AEE | 1086 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181998 |
| 2 | 🇪🇸 ES | 13880 |
| 3 | 🇧🇷 BR | 12432 |
| 4 | 🇦🇺 AU | 12163 |
| 5 | 🇨🇦 CA | 11893 |
| 6 | 🇮🇳 IN | 11473 |
| 7 | 🇮🇹 IT | 11455 |
| 8 | 🇩🇪 DE | 10726 |
| 9 | 🇬🇧 GB | 10144 |
| 10 | 🇯🇵 JP | 8869 |
| 11 | 🇨🇴 CO | 8821 |
| 12 | 🇫🇷 FR | 8639 |
| 13 | 🇬🇷 GR | 6330 |
| 14 | 🇹🇷 TR | 6209 |
| 15 | 🇲🇽 MX | 6035 |
| 16 | 🇨🇭 CH | 5748 |
| 17 | 🇳🇴 NO | 5371 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3673 |
| 20 | 🇵🇱 PL | 3575 |
| 21 | 🇹🇭 TH | 3537 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2898 |
| 24 | 🇬🇹 GT | 2745 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2366 |
| 27 | 🇲🇦 MA | 2176 |
| 28 | 🇳🇱 NL | 1932 |
| 29 | 🇲🇪 ME | 1880 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4526 |
| 2 | Denver International Airport |  | US | 3511 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2620 |
| 5 | Guaymaral Airport |  | CO | 2579 |
| 6 | Harry Reid International Airport |  | US | 2402 |
| 7 | Zurich Airport |  | CH | 2247 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2215 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2208 |
| 10 | La Aurora Airport |  | GT | 2086 |
| 11 | El Dorado International Airport |  | CO | 2014 |
| 12 | Chicago O'Hare International Airport |  | US | 1985 |
| 13 | Salt Lake City International Airport |  | US | 1902 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1889 |
| 15 | Congonhas Airport |  | BR | 1811 |
| 16 | Frankfurt am Main International Airport |  | DE | 1768 |
| 17 | Madrid Barajas International Airport |  | ES | 1691 |
| 18 | Capua Airport |  | IT | 1644 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1627 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1610 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1587 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 24 | Malpensa International Airport |  | IT | 1515 |
| 25 | Charles de Gaulle International Airport |  | FR | 1486 |
| 26 | Charlotte/Douglas International Airport |  | US | 1449 |
| 27 | Kuala Lumpur International Airport |  | MY | 1378 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1326 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1320 |
| 31 | Bengaluru International Airport |  | IN | 1315 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1290 |
| 33 | Seattle-Tacoma International Airport |  | US | 1281 |
| 34 | Viracopos International Airport |  | BR | 1260 |
| 35 | Calgary International Airport |  | CA | 1217 |
| 36 | Oslo Gardermoen Airport |  | NO | 1197 |
| 37 | Vitoria/Foronda Airport |  | ES | 1193 |
| 38 | Amsterdam Airport Schiphol |  | NL | 1168 |
| 39 | Don Mueang International Airport |  | TH | 1167 |
| 40 | Reno/Tahoe International Airport |  | US | 1164 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1055 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 770 | 21m | 244 km | 3,242.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 485 | 13m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 466 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 359 | 27m | 275 km | 1,701.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 316 | 1h 49m | 1,423 km | 7,755.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 315 | 44m | 241 km | 1,308.4 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 284 | 21m | 250 km | 1,226.7 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 271 | 19m | 99 km | 464.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 264 | 27m | 215 km | 977.7 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 255 | 1h 14m | 961 km | 4,226.8 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 254 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 253 | 31m | 369 km | 1,610.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 246 | 19m | 144 km | 611.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 232 | 1h 49m | 1,304 km | 5,219.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N777ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-19 15:08 UTC | 2026-08-19 15:31 UTC | 23m |
| N464TA |  | Laurence G Hanscom Field (KBED) | Lebanon Municipal Airport (KLEB) | 2026-08-19 14:35 UTC | 2026-08-19 15:28 UTC | 53m |
| N16YF |  | Dothan Regional Airport (KDHN) | Auburn University Regional Airport (KAUO) | 2026-08-19 15:12 UTC | 2026-08-19 15:27 UTC | 14m |
| N24613 |  | Belle Glade State Municipal Airport (KX10) | Pompano Beach Airpark (KPMP) | 2026-08-19 14:58 UTC | 2026-08-19 15:25 UTC | 26m |
| VAR517 | VAR | Phoenix Goodyear Airport (KGYR) | Lake Havasu City Airport (KHII) | 2026-08-19 14:08 UTC | 2026-08-19 15:22 UTC | 1h 14m |
| DOC42 | DOC | Trondheim Airport Vaernes (ENVA) | Trondheim Airport Vaernes (ENVA) | 2026-08-19 15:03 UTC | 2026-08-19 15:19 UTC | 15m |
| EWG12L | EWG | Dusseldorf International Airport (EDDL) | Son Bonet Airport (LESB) | 2026-08-19 13:15 UTC | 2026-08-19 15:17 UTC | 2h 2m |
| N2116J |  | Gnoss Field (KDVO) | Buchanan Field (KCCR) | 2026-08-19 14:55 UTC | 2026-08-19 15:17 UTC | 22m |
| IHACF | IHA | LIVD (LIVD) | Zell Am See Airport (LOWZ) | 2026-08-19 14:57 UTC | 2026-08-19 15:17 UTC | 20m |
| N2119E |  | Brookhaven Airport (KHWV) | Brookhaven Airport (KHWV) | 2026-08-19 14:30 UTC | 2026-08-19 15:15 UTC | 44m |
| N60HF |  | Coulter Field (KCFD) | Easterwood Field (KCLL) | 2026-08-19 14:30 UTC | 2026-08-19 15:15 UTC | 44m |
| GOLEM21 | GOL | Cottonwood Airport (OK66) | Lariat Ranch Airport (OK42) | 2026-08-19 14:59 UTC | 2026-08-19 15:14 UTC | 14m |
| FHIAM | FHI | Montauban Airport (LFDB) | Montauban Airport (LFDB) | 2026-08-19 14:46 UTC | 2026-08-19 15:12 UTC | 26m |
| N813CG |  | Naples Municipal Airport (KAPF) | Immokalee Regional Airport (KIMM) | 2026-08-19 14:13 UTC | 2026-08-19 15:12 UTC | 58m |
| N9993E |  | Pratermill Flight Park Airport (GA72) | Flying G Ranch Airport (86GA) | 2026-08-19 14:59 UTC | 2026-08-19 15:11 UTC | 11m |
| WLDLD27 | WLD | Centennial Airport (KAPA) | Lake County Airport (KLXV) | 2026-08-19 14:09 UTC | 2026-08-19 15:11 UTC | 1h 1m |
| CAL109 | CAL | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-19 12:00 UTC | 2026-08-19 15:08 UTC | 3h 8m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-08-19 14:24 UTC | 2026-08-19 15:08 UTC | 44m |
| N539SH |  | Gold King Creek Airport (PAAN) | Healy River Airport (PAHV) | 2026-08-19 15:04 UTC | 2026-08-19 15:07 UTC | 3m |
| AAL2906 | American Airlines | General Edward Lawrence Logan International Airport (KBOS) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-19 11:38 UTC | 2026-08-19 15:07 UTC | 3h 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
