# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_16:20:11_UTC-green)

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

**Latest saved flight:** 2026-08-17 16:20:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 16:20:11 UTC

- **208,948** saved flights
- **66,568** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **208,948** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,512,989.0 tonnes** estimated CO2 emissions
- **145,680,524 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8275 |
| 2 | SkyWest Airlines | 7495 |
| 3 | EJA | 4061 |
| 4 | IndiGo | 3569 |
| 5 | American Airlines | 3489 |
| 6 | Southwest Airlines | 3364 |
| 7 | Delta Air Lines | 2697 |
| 8 | ENY | 2599 |
| 9 | LATAM Airlines | 1972 |
| 10 | AZU | 1890 |
| 11 | Lufthansa | 1764 |
| 12 | Vueling | 1738 |
| 13 | WIF | 1683 |
| 14 | LXJ | 1649 |
| 15 | easyJet | 1449 |
| 16 | Swiss International | 1396 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1320 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1279 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1147 |
| 24 | GLO | 1129 |
| 25 | Air France | 1124 |
| 26 | PGT | 1119 |
| 27 | JetBlue | 1067 |
| 28 | AEE | 1065 |
| 29 | WMT | 1056 |
| 30 | Wizz Air | 1036 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176983 |
| 2 | 🇪🇸 ES | 13379 |
| 3 | 🇧🇷 BR | 11982 |
| 4 | 🇦🇺 AU | 11747 |
| 5 | 🇨🇦 CA | 11516 |
| 6 | 🇮🇳 IN | 11140 |
| 7 | 🇮🇹 IT | 10926 |
| 8 | 🇩🇪 DE | 10334 |
| 9 | 🇬🇧 GB | 9763 |
| 10 | 🇯🇵 JP | 8645 |
| 11 | 🇨🇴 CO | 8309 |
| 12 | 🇫🇷 FR | 8300 |
| 13 | 🇬🇷 GR | 6153 |
| 14 | 🇹🇷 TR | 5946 |
| 15 | 🇲🇽 MX | 5858 |
| 16 | 🇨🇭 CH | 5567 |
| 17 | 🇳🇴 NO | 5215 |
| 18 | 🇲🇾 MY | 3594 |
| 19 | 🇿🇦 ZA | 3512 |
| 20 | 🇵🇱 PL | 3454 |
| 21 | 🇹🇭 TH | 3353 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2776 |
| 24 | 🇬🇹 GT | 2685 |
| 25 | 🇰🇷 KR | 2545 |
| 26 | 🇭🇷 HR | 2242 |
| 27 | 🇲🇦 MA | 2105 |
| 28 | 🇳🇱 NL | 1869 |
| 29 | 🇲🇪 ME | 1772 |
| 30 | 🇮🇩 ID | 1725 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4383 |
| 2 | Denver International Airport |  | US | 3405 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2534 |
| 5 | Guaymaral Airport |  | CO | 2509 |
| 6 | Harry Reid International Airport |  | US | 2352 |
| 7 | Zurich Airport |  | CH | 2180 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2174 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2165 |
| 10 | La Aurora Airport |  | GT | 2042 |
| 11 | Chicago O'Hare International Airport |  | US | 1936 |
| 12 | El Dorado International Airport |  | CO | 1904 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1862 |
| 14 | Salt Lake City International Airport |  | US | 1845 |
| 15 | Congonhas Airport |  | BR | 1743 |
| 16 | Frankfurt am Main International Airport |  | DE | 1718 |
| 17 | Madrid Barajas International Airport |  | ES | 1640 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1587 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1586 |
| 20 | Capua Airport |  | IT | 1576 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1523 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1468 |
| 24 | Malpensa International Airport |  | IT | 1448 |
| 25 | Charles de Gaulle International Airport |  | FR | 1434 |
| 26 | Charlotte/Douglas International Airport |  | US | 1417 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1315 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1288 |
| 30 | Bengaluru International Airport |  | IN | 1288 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1264 |
| 32 | Barcelona International Airport |  | ES | 1252 |
| 33 | Seattle-Tacoma International Airport |  | US | 1240 |
| 34 | Viracopos International Airport |  | BR | 1212 |
| 35 | Calgary International Airport |  | CA | 1179 |
| 36 | Oslo Gardermoen Airport |  | NO | 1157 |
| 37 | Vitoria/Foronda Airport |  | ES | 1150 |
| 38 | Reno/Tahoe International Airport |  | US | 1144 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1130 |
| 40 | Don Mueang International Airport |  | TH | 1113 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1031 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 475 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 408 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 350 | 27m | 275 km | 1,658.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 346 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 306 | 44m | 241 km | 1,271.1 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 305 | 1h 49m | 1,423 km | 7,485.2 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 288 | 22m | 55 km | 273.7 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 262 | 19m | 99 km | 448.8 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 256 | 27m | 215 km | 948.1 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 249 | 1h 37m | 1,156 km | 4,967.5 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 246 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 239 | 31m | 369 km | 1,521.3 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 239 | 19m | 144 km | 594.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 229 | 28m | 152 km | 598.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 224 | 1h 49m | 1,304 km | 5,039.4 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LIFELN3 | LIF | Cheyenne Regional/Jerry Olson Field (KCYS) | Buckley Space Force Base Airport (KBKF) | 2026-08-17 15:35 UTC | 2026-08-17 16:20 UTC | 44m |
| SCU39 | SCU | Neversweat Airport (1OK0) | Jones Memorial Airport (K3F7) | 2026-08-17 15:51 UTC | 2026-08-17 16:19 UTC | 28m |
| N555DP |  | Falcon Field (KFFZ) | Morris Ag Air Sw Airport (56CL) | 2026-08-17 14:44 UTC | 2026-08-17 16:18 UTC | 1h 33m |
| INOST | INO | Torino / Aeritalia Airport (LIMA) | LIVV (LIVV) | 2026-08-17 16:01 UTC | 2026-08-17 16:16 UTC | 14m |
| CODE21 | COD | 75OK (75OK) | Flying E Ranch Airport (OK16) | 2026-08-17 15:54 UTC | 2026-08-17 16:14 UTC | 20m |
| GTI8138 | GTI | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-08-17 11:41 UTC | 2026-08-17 16:12 UTC | 4h 30m |
| FDB71T | flydubai | Tbilisi International Airport (UGTB) | Dubai International Airport (OMDB) | 2026-08-17 12:36 UTC | 2026-08-17 16:10 UTC | 3h 33m |
| N12442 |  | Dupage Airport (KDPA) | Aero Lake Estates Airport (30IS) | 2026-08-17 15:49 UTC | 2026-08-17 16:10 UTC | 20m |
| EFC50I | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-17 15:32 UTC | 2026-08-17 16:10 UTC | 38m |
| AXEL10 | AXE | Me-Own Airport (1NM0) | 4Z Ranch Airport (30ID) | 2026-08-17 14:45 UTC | 2026-08-17 16:07 UTC | 1h 22m |
| N7073U |  | Bolingbrook's Clow International Airport (K1C5) | Bolingbrook's Clow International Airport (K1C5) | 2026-08-17 15:50 UTC | 2026-08-17 16:06 UTC | 16m |
| N5402E |  | Holk Field At Foley Municipal Airport (K5R4) | KNQB (KNQB) | 2026-08-17 15:35 UTC | 2026-08-17 16:06 UTC | 30m |
| N451DS |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-08-17 15:44 UTC | 2026-08-17 16:05 UTC | 20m |
| N65516 |  | Nashville International Airport (KBNA) | KM33 (KM33) | 2026-08-17 15:40 UTC | 2026-08-17 16:03 UTC | 23m |
| SHINR81 | SHI | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-08-17 15:36 UTC | 2026-08-17 16:03 UTC | 27m |
| AFR11QN | Air France | Charles de Gaulle International Airport (LFPG) | Decimomannu Airport (LIED) | 2026-08-17 14:32 UTC | 2026-08-17 16:01 UTC | 1h 28m |
| N6343D |  | Creve Coeur Airport (K1H0) | Creve Coeur Airport (K1H0) | 2026-08-17 15:26 UTC | 2026-08-17 15:59 UTC | 33m |
| TGJAC | TGJ | Rio Vista Ranch Airport (TS04) | Piedras Negras International Airport (MMPG) | 2026-08-17 15:40 UTC | 2026-08-17 15:57 UTC | 17m |
| HAWK275 | HAW | Kingsville Nas Airport (KNQI) | Triple B Ranch Airport (42XS) | 2026-08-17 15:36 UTC | 2026-08-17 15:57 UTC | 21m |
| N6392W |  | K7K8 (K7K8) | Harold Davidson Field (KVMR) | 2026-08-17 15:28 UTC | 2026-08-17 15:51 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
