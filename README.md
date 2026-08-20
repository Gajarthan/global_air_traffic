# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_05:50:31_UTC-green)

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

**Latest saved flight:** 2026-08-20 05:50:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 05:50:31 UTC

- **218,295** saved flights
- **68,721** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **218,295** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,626,964.4 tonnes** estimated CO2 emissions
- **152,287,793 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8727 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4247 |
| 4 | IndiGo | 3701 |
| 5 | American Airlines | 3636 |
| 6 | Southwest Airlines | 3470 |
| 7 | Delta Air Lines | 2822 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2069 |
| 10 | AZU | 2002 |
| 11 | Vueling | 1827 |
| 12 | Lufthansa | 1813 |
| 13 | WIF | 1739 |
| 14 | LXJ | 1728 |
| 15 | easyJet | 1511 |
| 16 | Swiss International | 1449 |
| 17 | AXM | 1426 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1366 |
| 20 | EJU | 1355 |
| 21 | Alaska Airlines | 1338 |
| 22 | All Nippon Airways | 1314 |
| 23 | VIV | 1195 |
| 24 | GLO | 1187 |
| 25 | PGT | 1181 |
| 26 | Air France | 1178 |
| 27 | WMT | 1145 |
| 28 | JetBlue | 1112 |
| 29 | Wizz Air | 1106 |
| 30 | AEE | 1093 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184148 |
| 2 | 🇪🇸 ES | 13946 |
| 3 | 🇧🇷 BR | 12597 |
| 4 | 🇦🇺 AU | 12334 |
| 5 | 🇨🇦 CA | 12057 |
| 6 | 🇮🇹 IT | 11580 |
| 7 | 🇮🇳 IN | 11525 |
| 8 | 🇩🇪 DE | 10772 |
| 9 | 🇬🇧 GB | 10217 |
| 10 | 🇨🇴 CO | 8979 |
| 11 | 🇯🇵 JP | 8916 |
| 12 | 🇫🇷 FR | 8668 |
| 13 | 🇬🇷 GR | 6361 |
| 14 | 🇹🇷 TR | 6276 |
| 15 | 🇲🇽 MX | 6094 |
| 16 | 🇨🇭 CH | 5774 |
| 17 | 🇳🇴 NO | 5408 |
| 18 | 🇲🇾 MY | 3769 |
| 19 | 🇿🇦 ZA | 3691 |
| 20 | 🇵🇱 PL | 3600 |
| 21 | 🇹🇭 TH | 3575 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2927 |
| 24 | 🇬🇹 GT | 2767 |
| 25 | 🇰🇷 KR | 2622 |
| 26 | 🇭🇷 HR | 2392 |
| 27 | 🇲🇦 MA | 2189 |
| 28 | 🇳🇱 NL | 1940 |
| 29 | 🇲🇪 ME | 1910 |
| 30 | 🇮🇩 ID | 1839 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4591 |
| 2 | Denver International Airport |  | US | 3576 |
| 3 | Tokyo International Airport |  | JP | 2678 |
| 4 | Indira Gandhi International Airport |  | IN | 2643 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2416 |
| 7 | Zurich Airport |  | CH | 2259 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2245 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2217 |
| 10 | La Aurora Airport |  | GT | 2106 |
| 11 | El Dorado International Airport |  | CO | 2053 |
| 12 | Chicago O'Hare International Airport |  | US | 2007 |
| 13 | Salt Lake City International Airport |  | US | 1931 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1840 |
| 16 | Frankfurt am Main International Airport |  | DE | 1779 |
| 17 | Madrid Barajas International Airport |  | ES | 1704 |
| 18 | Capua Airport |  | IT | 1658 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1616 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1604 |
| 22 | Macau International Airport |  | MO | 1566 |
| 23 | Malpensa International Airport |  | IT | 1537 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1533 |
| 25 | Charles de Gaulle International Airport |  | FR | 1494 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1390 |
| 28 | Kuala Lumpur International Airport |  | MY | 1387 |
| 29 | Barcelona International Airport |  | ES | 1333 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1331 |
| 31 | Bengaluru International Airport |  | IN | 1316 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1278 |
| 35 | Calgary International Airport |  | CA | 1234 |
| 36 | Oslo Gardermoen Airport |  | NO | 1206 |
| 37 | Vitoria/Foronda Airport |  | ES | 1205 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1201 |
| 39 | Don Mueang International Airport |  | TH | 1180 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1173 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 784 | 21m | 244 km | 3,301.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 539 | 1h 7m | 770 km | 7,160.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 514 | 24m | 225 km | 1,994.1 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 493 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 485 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 364 | 27m | 275 km | 1,724.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 321 | 1h 50m | 1,423 km | 7,877.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 316 | 44m | 241 km | 1,312.6 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 311 | 1h 7m | 706 km | 3,786.4 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 272 | 1h 38m | 1,156 km | 5,426.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 268 | 24m | 218 km | 1,009.7 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 267 | 27m | 215 km | 988.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 259 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 258 | 31m | 369 km | 1,642.2 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 27 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 238 | 44m | 555 km | 2,279.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 236 | 1h 49m | 1,304 km | 5,309.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N548SF |  | KU77 (KU77) | Wendover Airport (KENV) | 2026-08-20 04:30 UTC | 2026-08-20 05:50 UTC | 1h 20m |
| YOA | YOA | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-20 05:16 UTC | 2026-08-20 05:50 UTC | 33m |
| RSCU515 | RSC | Alert Bay Airport (CYAL) | Vancouver International Airport (CYVR) | 2026-08-20 04:52 UTC | 2026-08-20 05:46 UTC | 53m |
| LBQ790 | LBQ | Worcester Regional Airport (KORH) | Teterboro Airport (KTEB) | 2026-08-20 05:04 UTC | 2026-08-20 05:41 UTC | 37m |
| SXAEO | SXA | Amigdhaleon Airport (LGKM) | Kastoria National Airport (LGKA) | 2026-08-20 04:24 UTC | 2026-08-20 05:40 UTC | 1h 15m |
| N81NG |  | Cavern City Air Trml Airport (KCNM) | Grant County Airport (KSVC) | 2026-08-20 04:49 UTC | 2026-08-20 05:36 UTC | 46m |
| WGTL17 | WGT | Newcastle Airport (YWLM) | Maryborough Airport (YMYB) | 2026-08-20 04:29 UTC | 2026-08-20 05:35 UTC | 1h 5m |
| RGY937 | RGY | Portland-Hillsboro Airport (KHIO) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-20 04:02 UTC | 2026-08-20 05:31 UTC | 1h 29m |
| RYR5914 | Ryanair | Malpensa International Airport (LIMC) | Capua Airport (LIAU) | 2026-08-20 04:36 UTC | 2026-08-20 05:31 UTC | 55m |
| JJP215 | JJP | Narita International Airport (RJAA) | Tokushima Airport (RJOS) | 2026-08-20 04:39 UTC | 2026-08-20 05:29 UTC | 50m |
| AMF | AMF | Perth Jandakot Airport (YPJT) | Morawa Airport (YMRW) | 2026-08-20 04:40 UTC | 2026-08-20 05:27 UTC | 47m |
| FIN7WB | Finnair | Helsinki Vantaa Airport (EFHK) | Gothenburg-Landvetter Airport (ESGG) | 2026-08-20 04:18 UTC | 2026-08-20 05:26 UTC | 1h 7m |
| RYR95YC | Ryanair | Memmingen Allgau Airport (EDJA) | Capua Airport (LIAU) | 2026-08-20 04:20 UTC | 2026-08-20 05:25 UTC | 1h 4m |
| SXS8SR | SXS | Antalya International Airport (LTAI) | Václav Havel Airport (LKPR) | 2026-08-20 02:31 UTC | 2026-08-20 05:25 UTC | 2h 54m |
| SAS39K | Scandinavian Airlines | Haugesund Airport (ENHD) | Oslo Gardermoen Airport (ENGM) | 2026-08-20 04:43 UTC | 2026-08-20 05:21 UTC | 38m |
| RYR7KN | Ryanair | Gdańsk Lech Wałęsa Airport (EPGD) | Livno Brda Bosni Airport (LQLV) | 2026-08-20 03:48 UTC | 2026-08-20 05:21 UTC | 1h 33m |
| N13377 |  | Sacramento Executive Airport (KSAC) | Nut Tree Airport (KVCB) | 2026-08-20 05:00 UTC | 2026-08-20 05:19 UTC | 18m |
| RYR3TJ | Ryanair | Lamezia Terme Airport (LICA) | Malpensa International Airport (LIMC) | 2026-08-20 03:52 UTC | 2026-08-20 05:17 UTC | 1h 24m |
| EWG6YE | EWG | Cologne Bonn Airport (EDDK) | Visoko Sport Airfield (LQVI) | 2026-08-20 03:52 UTC | 2026-08-20 05:15 UTC | 1h 23m |
| RYR221H | Ryanair | Copernicus Wrocław Airport (EPWR) | Mostar International Airport (LQMO) | 2026-08-20 04:01 UTC | 2026-08-20 05:14 UTC | 1h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
