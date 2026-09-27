# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_00:15:39_UTC-green)

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

**Latest saved flight:** 2026-09-27 00:15:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-27 00:15:39 UTC

- **270,603** saved flights
- **79,269** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **270,603** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,282,191.4 tonnes** estimated CO2 emissions
- **190,271,966 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10646 |
| 2 | SkyWest Airlines | 9426 |
| 3 | EJA | 5286 |
| 4 | IndiGo | 4525 |
| 5 | American Airlines | 4207 |
| 6 | Southwest Airlines | 3985 |
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
| 17 | QLK | 1739 |
| 18 | EJU | 1695 |
| 19 | AXM | 1674 |
| 20 | United Airlines | 1655 |
| 21 | Alaska Airlines | 1599 |
| 22 | All Nippon Airways | 1556 |
| 23 | PGT | 1524 |
| 24 | WMT | 1513 |
| 25 | GLO | 1508 |
| 26 | Air France | 1485 |
| 27 | VIV | 1478 |
| 28 | Wizz Air | 1470 |
| 29 | CXK | 1330 |
| 30 | AEE | 1296 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 225477 |
| 2 | 🇪🇸 ES | 16944 |
| 3 | 🇧🇷 BR | 15822 |
| 4 | 🇦🇺 AU | 15539 |
| 5 | 🇨🇦 CA | 15089 |
| 6 | 🇮🇹 IT | 14631 |
| 7 | 🇮🇳 IN | 14323 |
| 8 | 🇩🇪 DE | 12985 |
| 9 | 🇬🇧 GB | 12516 |
| 10 | 🇨🇴 CO | 12429 |
| 11 | 🇫🇷 FR | 10744 |
| 12 | 🇯🇵 JP | 10378 |
| 13 | 🇹🇷 TR | 8188 |
| 14 | 🇬🇷 GR | 7806 |
| 15 | 🇲🇽 MX | 7472 |
| 16 | 🇨🇭 CH | 7192 |
| 17 | 🇳🇴 NO | 6682 |
| 18 | 🇹🇭 TH | 4831 |
| 19 | 🇲🇾 MY | 4532 |
| 20 | 🇿🇦 ZA | 4516 |
| 21 | 🇵🇱 PL | 4429 |
| 22 | 🇳🇿 NZ | 3791 |
| 23 | 🇵🇭 PH | 3584 |
| 24 | 🇬🇹 GT | 3422 |
| 25 | 🇭🇷 HR | 3086 |
| 26 | 🇰🇷 KR | 3057 |
| 27 | 🇲🇦 MA | 2686 |
| 28 | 🇲🇪 ME | 2537 |
| 29 | 🇳🇱 NL | 2418 |
| 30 | 🇮🇩 ID | 2251 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5512 |
| 2 | Denver International Airport |  | US | 4410 |
| 3 | Indira Gandhi International Airport |  | IN | 3238 |
| 4 | Tokyo International Airport |  | JP | 3108 |
| 5 | El Dorado International Airport |  | CO | 2947 |
| 6 | Harry Reid International Airport |  | US | 2901 |
| 7 | Guaymaral Airport |  | CO | 2821 |
| 8 | Zurich Airport |  | CH | 2805 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2718 |
| 10 | La Aurora Airport |  | GT | 2601 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2599 |
| 12 | Salt Lake City International Airport |  | US | 2392 |
| 13 | Chicago O'Hare International Airport |  | US | 2309 |
| 14 | Congonhas Airport |  | BR | 2307 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2214 |
| 16 | Capua Airport |  | IT | 2094 |
| 17 | Madrid Barajas International Airport |  | ES | 2085 |
| 18 | Frankfurt am Main International Airport |  | DE | 2048 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2044 |
| 20 | Malpensa International Airport |  | IT | 1931 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1925 |
| 22 | Charles de Gaulle International Airport |  | FR | 1919 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1904 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1891 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1824 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1759 |
| 28 | Charlotte/Douglas International Airport |  | US | 1696 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1683 |
| 30 | Barcelona International Airport |  | ES | 1681 |
| 31 | Viracopos International Airport |  | BR | 1631 |
| 32 | Kuala Lumpur International Airport |  | MY | 1624 |
| 33 | Seattle-Tacoma International Airport |  | US | 1586 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1585 |
| 35 | Calgary International Airport |  | CA | 1541 |
| 36 | Don Mueang International Airport |  | TH | 1528 |
| 37 | Bengaluru International Airport |  | IN | 1523 |
| 38 | Oslo Gardermoen Airport |  | NO | 1515 |
| 39 | Vancouver International Airport |  | CA | 1514 |
| 40 | Antalya International Airport |  | TR | 1446 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1123 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1015 | 21m | 244 km | 4,273.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 749 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 682 | 1h 6m | 770 km | 9,059.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 677 | 24m | 225 km | 2,626.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 446 | 44m | 555 km | 4,270.7 t |
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
| WUJ | WUJ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-09-26 23:58 UTC | 2026-09-27 00:15 UTC | 16m |
| NDU646 | NDU | Mesa Gateway Airport (KIWA) | Casa Grande Municipal Airport (KCGZ) | 2026-09-26 23:45 UTC | 2026-09-27 00:06 UTC | 21m |
| SWR76P | Swiss International | Zurich Airport (LSZH) | Queen Alia International Airport (OJAI) | 2026-09-26 21:01 UTC | 2026-09-27 00:06 UTC | 3h 5m |
| XSR926 | XSR | Mc Ghee Tyson Airport (KTYS) | Austin-Bergstrom International Airport (KAUS) | 2026-09-26 21:44 UTC | 2026-09-27 00:00 UTC | 2h 15m |
| ZKIDU | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-09-26 23:46 UTC | 2026-09-26 23:59 UTC | 12m |
| CHZ700 | CHZ | Liege Airport (EBLG) | Queen Alia International Airport (OJAI) | 2026-09-26 20:18 UTC | 2026-09-26 23:55 UTC | 3h 37m |
| N4958A |  | Santa Monica Municipal Airport (KSMO) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-26 22:49 UTC | 2026-09-26 23:54 UTC | 1h 4m |
| N821TN |  | Kansas City Downtown/Wheeler Field (KMKC) | Jesse Viertel Memorial Airport (KVER) | 2026-09-26 23:34 UTC | 2026-09-26 23:51 UTC | 17m |
| OAI | OAI | Barwon Heads Airport (YBRS) | Barwon Heads Airport (YBRS) | 2026-09-26 23:23 UTC | 2026-09-26 23:45 UTC | 21m |
| PFT420 | PFT | San Luis Obispo County Regional Airport (KSBP) | Van Nuys Airport (KVNY) | 2026-09-26 23:11 UTC | 2026-09-26 23:43 UTC | 32m |
| N409MR |  | Flagstaff Pulliam Airport (KFLG) | Henderson Executive Airport (KHND) | 2026-09-26 22:57 UTC | 2026-09-26 23:35 UTC | 38m |
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-09-26 21:39 UTC | 2026-09-26 23:33 UTC | 1h 53m |
| CGSSC | CGS | Nanaimo Airport (CYCD) | Vancouver International Airport (CYVR) | 2026-09-26 23:14 UTC | 2026-09-26 23:30 UTC | 15m |
| ENY4113 | ENY | Dallas-Fort Worth International Airport (KDFW) | Herington Regional Airport (KHRU) | 2026-09-26 22:36 UTC | 2026-09-26 23:30 UTC | 54m |
| AM295 |  | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-09-26 22:42 UTC | 2026-09-26 23:28 UTC | 46m |
| VOZ816 | Virgin Australia | Sydney Kingsford Smith International Airport (YSSY) | Melbourne International Airport (YMML) | 2026-09-26 22:13 UTC | 2026-09-26 23:28 UTC | 1h 15m |
| N399LG |  | Lux Field (25CD) | Lux Field (25CD) | 2026-09-26 23:27 UTC | 2026-09-26 23:27 UTC | 0m |
| JNX3 | JNX | Yav'Pe Ma'Ta Airport (16AZ) | Yav'Pe Ma'Ta Airport (16AZ) | 2026-09-26 23:17 UTC | 2026-09-26 23:25 UTC | 8m |
| N983RA |  | Marana Regional Airport (KAVQ) | Marana Regional Airport (KAVQ) | 2026-09-26 23:20 UTC | 2026-09-26 23:24 UTC | 4m |
| NSZ4402 | NSZ | Larnaca International Airport (LCLK) | Stockholm-Arlanda Airport (ESSA) | 2026-09-26 19:20 UTC | 2026-09-26 23:24 UTC | 4h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
