# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_08:52:14_UTC-green)

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

**Latest saved flight:** 2026-08-23 08:52:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 08:52:14 UTC

- **227,944** saved flights
- **70,615** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **227,944** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,748,350.0 tonnes** estimated CO2 emissions
- **159,324,640 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9145 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4393 |
| 4 | IndiGo | 3856 |
| 5 | American Airlines | 3740 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2919 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2184 |
| 10 | AZU | 2112 |
| 11 | Vueling | 1933 |
| 12 | Lufthansa | 1863 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1583 |
| 16 | Swiss International | 1519 |
| 17 | AXM | 1512 |
| 18 | QLK | 1446 |
| 19 | United Airlines | 1444 |
| 20 | EJU | 1441 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1367 |
| 23 | GLO | 1264 |
| 24 | VIV | 1253 |
| 25 | PGT | 1251 |
| 26 | Air France | 1235 |
| 27 | WMT | 1235 |
| 28 | Wizz Air | 1181 |
| 29 | JetBlue | 1142 |
| 30 | AEE | 1135 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190643 |
| 2 | 🇪🇸 ES | 14610 |
| 3 | 🇧🇷 BR | 13293 |
| 4 | 🇦🇺 AU | 12937 |
| 5 | 🇨🇦 CA | 12616 |
| 6 | 🇮🇹 IT | 12258 |
| 7 | 🇮🇳 IN | 12014 |
| 8 | 🇩🇪 DE | 11209 |
| 9 | 🇬🇧 GB | 10699 |
| 10 | 🇨🇴 CO | 9384 |
| 11 | 🇯🇵 JP | 9276 |
| 12 | 🇫🇷 FR | 9108 |
| 13 | 🇹🇷 TR | 6695 |
| 14 | 🇬🇷 GR | 6681 |
| 15 | 🇲🇽 MX | 6358 |
| 16 | 🇨🇭 CH | 6013 |
| 17 | 🇳🇴 NO | 5601 |
| 18 | 🇲🇾 MY | 4033 |
| 19 | 🇹🇭 TH | 3944 |
| 20 | 🇿🇦 ZA | 3939 |
| 21 | 🇵🇱 PL | 3787 |
| 22 | 🇳🇿 NZ | 3167 |
| 23 | 🇵🇭 PH | 3123 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2699 |
| 26 | 🇭🇷 HR | 2586 |
| 27 | 🇲🇦 MA | 2298 |
| 28 | 🇲🇪 ME | 2060 |
| 29 | 🇳🇱 NL | 2032 |
| 30 | 🇮🇩 ID | 1970 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3714 |
| 3 | Indira Gandhi International Airport |  | IN | 2774 |
| 4 | Tokyo International Airport |  | JP | 2772 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2473 |
| 7 | Zurich Airport |  | CH | 2369 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2332 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2300 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2084 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2009 |
| 14 | Congonhas Airport |  | BR | 1939 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1938 |
| 16 | Frankfurt am Main International Airport |  | DE | 1827 |
| 17 | Madrid Barajas International Airport |  | ES | 1778 |
| 18 | Capua Airport |  | IT | 1771 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1703 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1698 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1648 |
| 22 | Malpensa International Airport |  | IT | 1622 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1608 |
| 24 | Macau International Airport |  | MO | 1594 |
| 25 | Charles de Gaulle International Airport |  | FR | 1573 |
| 26 | Ninoy Aquino International Airport |  | PH | 1496 |
| 27 | Charlotte/Douglas International Airport |  | US | 1492 |
| 28 | Kuala Lumpur International Airport |  | MY | 1462 |
| 29 | Barcelona International Airport |  | ES | 1419 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1384 |
| 31 | Bengaluru International Airport |  | IN | 1351 |
| 32 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 33 | Viracopos International Airport |  | BR | 1348 |
| 34 | Seattle-Tacoma International Airport |  | US | 1347 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Calgary International Airport |  | CA | 1299 |
| 37 | Don Mueang International Airport |  | TH | 1293 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1231 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 832 | 21m | 244 km | 3,503.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 572 | 1h 6m | 770 km | 7,598.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 566 | 24m | 225 km | 2,195.8 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 346 | 1h 50m | 1,423 km | 8,491.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 314 | 1h 7m | 706 km | 3,823.0 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 310 | 21m | 250 km | 1,339.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 15 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 301 | 44m | 555 km | 2,882.2 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 292 | 1h 38m | 1,156 km | 5,825.3 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 290 | 24m | 218 km | 1,092.5 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 259 | 19m | 144 km | 644.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 239 | 15m | 154 km | 633.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FPTUN | FPT | Ambri Airport (LSPM) | Ambri Airport (LSPM) | 2026-08-23 08:32 UTC | 2026-08-23 08:52 UTC | 20m |
| HBKPJ | HBK | Mollis Airport (LSZM) | Donaueschingen-Villingen Airport (EDTD) | 2026-08-23 07:44 UTC | 2026-08-23 08:39 UTC | 55m |
| CHX80 | CHX | Weiden in der Oberpfalz Airport (EDQW) | Weiden in der Oberpfalz Airport (EDQW) | 2026-08-23 08:35 UTC | 2026-08-23 08:38 UTC | 2m |
| ZSOHK | ZSO | Grand Central Airport (FAGC) | Morningside Farm Airport (FAMS) | 2026-08-23 07:24 UTC | 2026-08-23 08:31 UTC | 1h 6m |
| LOT6669 | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Palermo / Punta Raisi Airport (LICJ) | 2026-08-23 06:11 UTC | 2026-08-23 08:26 UTC | 2h 15m |
| RXA6178 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-23 07:57 UTC | 2026-08-23 08:21 UTC | 23m |
| N857GA |  | Ted Stevens Anchorage International Airport (PANC) | Tianjin Binhai International Airport (ZBTJ) | 2026-08-22 23:06 UTC | 2026-08-23 08:20 UTC | 9h 14m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-23 08:09 UTC | 2026-08-23 08:19 UTC | 10m |
| SKY765 | SKY | Matsumoto Airport (RJAF) | Chitose Air Base (RJCJ) | 2026-08-23 06:53 UTC | 2026-08-23 08:19 UTC | 1h 25m |
| SFJ83 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-08-23 06:59 UTC | 2026-08-23 08:02 UTC | 1h 3m |
| MMA361 | MMA | Don Mueang International Airport (VTBD) | Anisakan Airport (VYAS) | 2026-08-23 06:52 UTC | 2026-08-23 08:00 UTC | 1h 8m |
| BNI47 | BNI | Łódź Władysław Reymont Airport (EPLL) | Łódź Władysław Reymont Airport (EPLL) | 2026-08-23 07:25 UTC | 2026-08-23 08:00 UTC | 34m |
| AEE4SR | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-23 07:36 UTC | 2026-08-23 07:59 UTC | 22m |
| 8AX |  | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-08-23 07:44 UTC | 2026-08-23 07:58 UTC | 14m |
| WMT9984 | WMT | Budapest Ferenc Liszt International Airport (LHBP) | Malpensa International Airport (LIMC) | 2026-08-23 06:25 UTC | 2026-08-23 07:56 UTC | 1h 31m |
| AEZ836S | AEZ | Linate Airport (LIML) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-23 07:08 UTC | 2026-08-23 07:55 UTC | 46m |
| EWG7DM | EWG | Dusseldorf International Airport (EDDL) | Kasteli Airport (LGTL) | 2026-08-23 05:14 UTC | 2026-08-23 07:52 UTC | 2h 37m |
| AEE306 | AEE | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-08-23 07:25 UTC | 2026-08-23 07:50 UTC | 25m |
| FDA357 | FDA | Nagoya Airport (RJNA) | Yamagata Airport (RJSC) | 2026-08-23 07:05 UTC | 2026-08-23 07:49 UTC | 43m |
| LNK661V | LNK | Cape Town International Airport (FACT) | Ermelo Airport (FAEO) | 2026-08-23 06:09 UTC | 2026-08-23 07:47 UTC | 1h 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
