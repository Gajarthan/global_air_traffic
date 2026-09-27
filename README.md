# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_05:12:18_UTC-green)

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

**Latest saved flight:** 2026-09-27 05:12:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-27 05:12:18 UTC

- **270,661** saved flights
- **79,281** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **270,661** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,282,817.8 tonnes** estimated CO2 emissions
- **190,308,277 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10646 |
| 2 | SkyWest Airlines | 9426 |
| 3 | EJA | 5286 |
| 4 | IndiGo | 4530 |
| 5 | American Airlines | 4208 |
| 6 | Southwest Airlines | 3986 |
| 7 | Delta Air Lines | 3364 |
| 8 | ENY | 3181 |
| 9 | LATAM Airlines | 2603 |
| 10 | AZU | 2537 |
| 11 | Vueling | 2253 |
| 12 | WIF | 2198 |
| 13 | LXJ | 2128 |
| 14 | Lufthansa | 2053 |
| 15 | easyJet | 1813 |
| 16 | Swiss International | 1773 |
| 17 | QLK | 1741 |
| 18 | EJU | 1695 |
| 19 | AXM | 1675 |
| 20 | United Airlines | 1656 |
| 21 | Alaska Airlines | 1599 |
| 22 | All Nippon Airways | 1557 |
| 23 | PGT | 1527 |
| 24 | WMT | 1513 |
| 25 | GLO | 1508 |
| 26 | Air France | 1485 |
| 27 | VIV | 1478 |
| 28 | Wizz Air | 1470 |
| 29 | CXK | 1330 |
| 30 | AEE | 1297 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 225503 |
| 2 | 🇪🇸 ES | 16944 |
| 3 | 🇧🇷 BR | 15822 |
| 4 | 🇦🇺 AU | 15554 |
| 5 | 🇨🇦 CA | 15090 |
| 6 | 🇮🇹 IT | 14632 |
| 7 | 🇮🇳 IN | 14336 |
| 8 | 🇩🇪 DE | 12986 |
| 9 | 🇬🇧 GB | 12516 |
| 10 | 🇨🇴 CO | 12429 |
| 11 | 🇫🇷 FR | 10745 |
| 12 | 🇯🇵 JP | 10388 |
| 13 | 🇹🇷 TR | 8192 |
| 14 | 🇬🇷 GR | 7809 |
| 15 | 🇲🇽 MX | 7473 |
| 16 | 🇨🇭 CH | 7194 |
| 17 | 🇳🇴 NO | 6682 |
| 18 | 🇹🇭 TH | 4837 |
| 19 | 🇲🇾 MY | 4534 |
| 20 | 🇿🇦 ZA | 4516 |
| 21 | 🇵🇱 PL | 4430 |
| 22 | 🇳🇿 NZ | 3800 |
| 23 | 🇵🇭 PH | 3584 |
| 24 | 🇬🇹 GT | 3422 |
| 25 | 🇭🇷 HR | 3087 |
| 26 | 🇰🇷 KR | 3058 |
| 27 | 🇲🇦 MA | 2686 |
| 28 | 🇲🇪 ME | 2537 |
| 29 | 🇳🇱 NL | 2418 |
| 30 | 🇮🇩 ID | 2254 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5512 |
| 2 | Denver International Airport |  | US | 4411 |
| 3 | Indira Gandhi International Airport |  | IN | 3241 |
| 4 | Tokyo International Airport |  | JP | 3110 |
| 5 | El Dorado International Airport |  | CO | 2947 |
| 6 | Harry Reid International Airport |  | US | 2901 |
| 7 | Guaymaral Airport |  | CO | 2821 |
| 8 | Zurich Airport |  | CH | 2805 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2718 |
| 10 | La Aurora Airport |  | GT | 2601 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2600 |
| 12 | Salt Lake City International Airport |  | US | 2392 |
| 13 | Chicago O'Hare International Airport |  | US | 2310 |
| 14 | Congonhas Airport |  | BR | 2307 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2215 |
| 16 | Capua Airport |  | IT | 2094 |
| 17 | Madrid Barajas International Airport |  | ES | 2085 |
| 18 | Frankfurt am Main International Airport |  | DE | 2049 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2044 |
| 20 | Malpensa International Airport |  | IT | 1931 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1925 |
| 22 | Charles de Gaulle International Airport |  | FR | 1919 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1904 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1894 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1824 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1759 |
| 28 | Charlotte/Douglas International Airport |  | US | 1696 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1684 |
| 30 | Barcelona International Airport |  | ES | 1681 |
| 31 | Viracopos International Airport |  | BR | 1631 |
| 32 | Kuala Lumpur International Airport |  | MY | 1625 |
| 33 | Seattle-Tacoma International Airport |  | US | 1586 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1585 |
| 35 | Calgary International Airport |  | CA | 1541 |
| 36 | Don Mueang International Airport |  | TH | 1531 |
| 37 | Bengaluru International Airport |  | IN | 1524 |
| 38 | Oslo Gardermoen Airport |  | NO | 1515 |
| 39 | Vancouver International Airport |  | CA | 1514 |
| 40 | Antalya International Airport |  | TR | 1446 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1123 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1016 | 21m | 244 km | 4,278.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 749 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 683 | 1h 6m | 770 km | 9,073.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 677 | 24m | 225 km | 2,626.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 449 | 44m | 555 km | 4,299.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 435 | 27m | 275 km | 2,061.3 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 427 | 1h 50m | 1,423 km | 10,479.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 412 | 44m | 241 km | 1,711.4 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 387 | 24m | 218 km | 1,458.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 378 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 366 | 21m | 250 km | 1,580.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 364 | 23m | 55 km | 346.0 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 345 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 341 | 1h 6m | 706 km | 4,151.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 314 | 19m | 144 km | 781.1 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 306 | 1h 14m | 961 km | 5,072.1 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 298 | 42m | 535 km | 2,752.2 t |
| 26 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 295 | 18m | 14 km | 73.8 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 291 | 1h 50m | 1,304 km | 6,546.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N409AE |  | Brandon Airdrome Airport (28KY) | Hopkinsville-Christian County Airport (KHVC) | 2026-09-27 04:47 UTC | 2026-09-27 05:12 UTC | 25m |
| UAL1564 | United Airlines | Chicago O'Hare International Airport (KORD) | San Diego International Airport (KSAN) | 2026-09-27 01:29 UTC | 2026-09-27 05:12 UTC | 3h 42m |
| IGO573E | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Dehradun Airport (VIDN) | 2026-09-27 03:23 UTC | 2026-09-27 05:03 UTC | 1h 40m |
| LBQ968 | LBQ | Washington Manassas/Harry P Davis Field (KHEF) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-09-27 04:21 UTC | 2026-09-27 05:03 UTC | 41m |
| BLVD | BLV | Shek Kong Air Base (VHSK) | Shek Kong Air Base (VHSK) | 2026-09-27 04:52 UTC | 2026-09-27 05:03 UTC | 11m |
| OAI | OAI | Barwon Heads Airport (YBRS) | Barwon Heads Airport (YBRS) | 2026-09-27 03:57 UTC | 2026-09-27 04:49 UTC | 51m |
| AAL9735 | American Airlines | Eugene F Kranz Toledo Express Airport (KTOL) | Tampa International Airport (KTPA) | 2026-09-27 02:40 UTC | 2026-09-27 04:40 UTC | 1h 59m |
| QLK203D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-09-27 03:34 UTC | 2026-09-27 04:38 UTC | 1h 4m |
| A7GQD |  | Doha International Airport (OTBD) | Al Khawr Airport (OTBK) | 2026-09-27 04:15 UTC | 2026-09-27 04:37 UTC | 22m |
| OCN910 | OCN | Frankfurt am Main International Airport (EDDF) | Otocac Airport (LDRO) | 2026-09-27 03:36 UTC | 2026-09-27 04:35 UTC | 58m |
| VOE3NF | VOE | Firenze / Peretola Airport (LIRQ) | Corte Airport (LFKT) | 2026-09-27 04:01 UTC | 2026-09-27 04:30 UTC | 28m |
| N748RM |  | Stillwater Regional Airport (KSWO) | Dallas Love Field (KDAL) | 2026-09-27 03:43 UTC | 2026-09-27 04:23 UTC | 39m |
| VLW | VLW | Sydney Bankstown Airport (YSBK) | Orange Airport (YORG) | 2026-09-27 03:46 UTC | 2026-09-27 04:21 UTC | 35m |
| AEE6054 | AEE | Eleftherios Venizelos International Airport (LGAV) | Kalamata Airport (LGKL) | 2026-09-27 03:58 UTC | 2026-09-27 04:20 UTC | 22m |
| JST293 | JST | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 2026-09-27 03:02 UTC | 2026-09-27 04:15 UTC | 1h 13m |
| N51C |  | Drake Field (KFYV) | Bill And Hillary Clinton Ntl/Adams Field (KLIT) | 2026-09-27 03:44 UTC | 2026-09-27 04:12 UTC | 27m |
| ANZ886L | ANZ | Wellington International Airport (NZWN) | Napier Airport (NZNR) | 2026-09-27 03:00 UTC | 2026-09-27 04:10 UTC | 1h 9m |
| AXM6126 | AXM | Kuala Lumpur International Airport (WMKK) | Sitiawan Airport (WMBA) | 2026-09-27 03:52 UTC | 2026-09-27 04:07 UTC | 15m |
| AAY4932 | AAY | Redding Regional Airport (KRDD) | Gienger/Box Bar Ranch Airport (1NA5) | 2026-09-27 01:53 UTC | 2026-09-27 04:05 UTC | 2h 12m |
| PGT2940 | PGT | Sabiha Gokcen International Airport (LTFJ) | Balikesir Korfez Airport (LTFD) | 2026-09-27 03:40 UTC | 2026-09-27 04:05 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
