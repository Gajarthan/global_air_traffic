# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_22:14:49_UTC-green)

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

**Latest saved flight:** 2026-09-30 22:14:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-30 22:14:49 UTC

- **273,392** saved flights
- **79,833** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **273,392** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,310,691.7 tonnes** estimated CO2 emissions
- **191,924,155 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10743 |
| 2 | SkyWest Airlines | 9516 |
| 3 | EJA | 5355 |
| 4 | IndiGo | 4562 |
| 5 | American Airlines | 4238 |
| 6 | Southwest Airlines | 4025 |
| 7 | Delta Air Lines | 3394 |
| 8 | ENY | 3205 |
| 9 | LATAM Airlines | 2641 |
| 10 | AZU | 2570 |
| 11 | Vueling | 2270 |
| 12 | WIF | 2224 |
| 13 | LXJ | 2154 |
| 14 | Lufthansa | 2065 |
| 15 | easyJet | 1822 |
| 16 | Swiss International | 1788 |
| 17 | QLK | 1762 |
| 18 | EJU | 1706 |
| 19 | AXM | 1681 |
| 20 | United Airlines | 1670 |
| 21 | Alaska Airlines | 1613 |
| 22 | All Nippon Airways | 1563 |
| 23 | PGT | 1540 |
| 24 | WMT | 1526 |
| 25 | GLO | 1525 |
| 26 | Air France | 1504 |
| 27 | VIV | 1497 |
| 28 | Wizz Air | 1482 |
| 29 | CXK | 1351 |
| 30 | AEE | 1306 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 227956 |
| 2 | 🇪🇸 ES | 17095 |
| 3 | 🇧🇷 BR | 16048 |
| 4 | 🇦🇺 AU | 15768 |
| 5 | 🇨🇦 CA | 15237 |
| 6 | 🇮🇹 IT | 14759 |
| 7 | 🇮🇳 IN | 14434 |
| 8 | 🇩🇪 DE | 13106 |
| 9 | 🇨🇴 CO | 12645 |
| 10 | 🇬🇧 GB | 12608 |
| 11 | 🇫🇷 FR | 10841 |
| 12 | 🇯🇵 JP | 10437 |
| 13 | 🇹🇷 TR | 8272 |
| 14 | 🇬🇷 GR | 7868 |
| 15 | 🇲🇽 MX | 7549 |
| 16 | 🇨🇭 CH | 7255 |
| 17 | 🇳🇴 NO | 6746 |
| 18 | 🇹🇭 TH | 4891 |
| 19 | 🇲🇾 MY | 4554 |
| 20 | 🇿🇦 ZA | 4551 |
| 21 | 🇵🇱 PL | 4469 |
| 22 | 🇳🇿 NZ | 3860 |
| 23 | 🇵🇭 PH | 3606 |
| 24 | 🇬🇹 GT | 3430 |
| 25 | 🇭🇷 HR | 3111 |
| 26 | 🇰🇷 KR | 3076 |
| 27 | 🇲🇦 MA | 2704 |
| 28 | 🇲🇪 ME | 2568 |
| 29 | 🇳🇱 NL | 2447 |
| 30 | 🇮🇩 ID | 2268 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5559 |
| 2 | Denver International Airport |  | US | 4456 |
| 3 | Indira Gandhi International Airport |  | IN | 3263 |
| 4 | Tokyo International Airport |  | JP | 3127 |
| 5 | El Dorado International Airport |  | CO | 3005 |
| 6 | Harry Reid International Airport |  | US | 2940 |
| 7 | Guaymaral Airport |  | CO | 2841 |
| 8 | Zurich Airport |  | CH | 2834 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2736 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2620 |
| 11 | La Aurora Airport |  | GT | 2607 |
| 12 | Salt Lake City International Airport |  | US | 2421 |
| 13 | Congonhas Airport |  | BR | 2335 |
| 14 | Chicago O'Hare International Airport |  | US | 2320 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2239 |
| 16 | Capua Airport |  | IT | 2116 |
| 17 | Madrid Barajas International Airport |  | ES | 2104 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2073 |
| 19 | Frankfurt am Main International Airport |  | DE | 2062 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1945 |
| 21 | Malpensa International Airport |  | IT | 1943 |
| 22 | Hartsfield/Jackson Atlanta International Airport |  | US | 1942 |
| 23 | Charles de Gaulle International Airport |  | FR | 1940 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1917 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1830 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1772 |
| 28 | Charlotte/Douglas International Airport |  | US | 1710 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1699 |
| 30 | Barcelona International Airport |  | ES | 1690 |
| 31 | Viracopos International Airport |  | BR | 1642 |
| 32 | Kuala Lumpur International Airport |  | MY | 1631 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1603 |
| 34 | Seattle-Tacoma International Airport |  | US | 1602 |
| 35 | Calgary International Airport |  | CA | 1551 |
| 36 | Don Mueang International Airport |  | TH | 1545 |
| 37 | Vancouver International Airport |  | CA | 1531 |
| 38 | Bengaluru International Airport |  | IN | 1531 |
| 39 | Oslo Gardermoen Airport |  | NO | 1530 |
| 40 | Reno/Tahoe International Airport |  | US | 1475 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1130 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1029 | 21m | 244 km | 4,332.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 762 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 689 | 1h 6m | 770 km | 9,152.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 685 | 24m | 225 km | 2,657.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 603 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 457 | 44m | 555 km | 4,376.0 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 439 | 27m | 275 km | 2,080.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 433 | 1h 50m | 1,423 km | 10,626.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 418 | 44m | 241 km | 1,736.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 391 | 24m | 218 km | 1,473.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 381 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 368 | 23m | 55 km | 349.8 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 350 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 347 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 339 | 26m | 215 km | 1,255.5 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 318 | 19m | 144 km | 791.0 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 310 | 1h 14m | 961 km | 5,138.4 t |
| 24 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 308 | 18m | 14 km | 77.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 302 | 42m | 535 km | 2,789.2 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 295 | 1h 50m | 1,304 km | 6,636.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 271 | 44m | 431 km | 2,016.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N835Z |  | John Wayne/Orange County Airport (KSNA) | Gillespie Field (KSEE) | 2026-09-30 21:41 UTC | 2026-09-30 22:14 UTC | 32m |
| N529HC |  | C A M P Airport (8NE9) | Lincoln Airport (KLNK) | 2026-09-30 21:42 UTC | 2026-09-30 22:13 UTC | 31m |
| N166WC |  | Vancouver International Airport (CYVR) | Boeing Field/King County International Airport (KBFI) | 2026-09-30 21:40 UTC | 2026-09-30 22:10 UTC | 30m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-09-30 11:14 UTC | 2026-09-30 22:03 UTC | 10h 49m |
| N175LF |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-09-30 21:46 UTC | 2026-09-30 22:03 UTC | 16m |
| BOE792 | BOE | Seattle Paine Field International Airport (KPAE) | Basin City Airfield (97WA) | 2026-09-30 20:31 UTC | 2026-09-30 21:59 UTC | 1h 28m |
| N707H |  | Merrill Field (PAMR) | Kenai Municipal Airport (PAEN) | 2026-09-30 21:25 UTC | 2026-09-30 21:59 UTC | 33m |
| SPSTR9 | SPS | Long Beach (Daugherty Field) Airport (KLGB) | Hemet-Ryan Airport (KHMT) | 2026-09-30 21:17 UTC | 2026-09-30 21:58 UTC | 41m |
| HEX30 | HEX | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-30 19:58 UTC | 2026-09-30 21:55 UTC | 1h 56m |
| N235CD |  | Iberlin Strip (WY23) | Iberlin Strip (WY23) | 2026-09-30 21:33 UTC | 2026-09-30 21:54 UTC | 20m |
| CHX76 | CHX | Diepholz Airport (ETND) | Bremen Airport (EDDW) | 2026-09-30 21:31 UTC | 2026-09-30 21:47 UTC | 15m |
| MVK90 | MVK | Mankato Regional Airport (KMKT) | Mankato Regional Airport (KMKT) | 2026-09-30 21:20 UTC | 2026-09-30 21:46 UTC | 25m |
| N600HD |  | Philadelphia International Airport (KPHL) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-09-30 20:46 UTC | 2026-09-30 21:44 UTC | 58m |
| N257FA |  | Lehigh Valley International Airport (KABE) | Harrisburg International Airport (KMDT) | 2026-09-30 20:53 UTC | 2026-09-30 21:43 UTC | 49m |
| N132TS |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-09-30 21:21 UTC | 2026-09-30 21:41 UTC | 19m |
| MVK69 | MVK | Mankato Regional Airport (KMKT) | Mankato Regional Airport (KMKT) | 2026-09-30 21:41 UTC | 2026-09-30 21:41 UTC | 0m |
| EJA312 | EJA | Shreveport Regional Airport (KSHV) | Craig Field (KSEM) | 2026-09-30 20:46 UTC | 2026-09-30 21:41 UTC | 54m |
| N765AT |  | Van Nuys Airport (KVNY) | Reno/Tahoe International Airport (KRNO) | 2026-09-30 20:51 UTC | 2026-09-30 21:40 UTC | 48m |
| DEVIL43 | DEV | 2TX3 (2TX3) | Dunbar Ranch Airport (0XS8) | 2026-09-30 21:12 UTC | 2026-09-30 21:40 UTC | 27m |
| N168DC |  | Perry-Houston County Airport (KPXE) | Perry-Houston County Airport (KPXE) | 2026-09-30 21:25 UTC | 2026-09-30 21:39 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
