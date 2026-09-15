# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_05:36:19_UTC-green)

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

**Latest saved flight:** 2026-09-15 05:36:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-15 05:36:19 UTC

- **258,974** saved flights
- **76,928** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **258,974** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,136,552.6 tonnes** estimated CO2 emissions
- **181,829,134 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10265 |
| 2 | SkyWest Airlines | 9030 |
| 3 | EJA | 5024 |
| 4 | IndiGo | 4343 |
| 5 | American Airlines | 4088 |
| 6 | Southwest Airlines | 3810 |
| 7 | Delta Air Lines | 3237 |
| 8 | ENY | 3070 |
| 9 | LATAM Airlines | 2489 |
| 10 | AZU | 2428 |
| 11 | Vueling | 2189 |
| 12 | WIF | 2077 |
| 13 | LXJ | 2024 |
| 14 | Lufthansa | 2018 |
| 15 | easyJet | 1763 |
| 16 | Swiss International | 1727 |
| 17 | QLK | 1673 |
| 18 | AXM | 1647 |
| 19 | EJU | 1641 |
| 20 | United Airlines | 1598 |
| 21 | Alaska Airlines | 1538 |
| 22 | All Nippon Airways | 1502 |
| 23 | WMT | 1463 |
| 24 | GLO | 1443 |
| 25 | PGT | 1442 |
| 26 | VIV | 1419 |
| 27 | Air France | 1415 |
| 28 | Wizz Air | 1409 |
| 29 | AEE | 1252 |
| 30 | TKR | 1252 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 215035 |
| 2 | 🇪🇸 ES | 16404 |
| 3 | 🇧🇷 BR | 15132 |
| 4 | 🇦🇺 AU | 14790 |
| 5 | 🇨🇦 CA | 14410 |
| 6 | 🇮🇹 IT | 14099 |
| 7 | 🇮🇳 IN | 13668 |
| 8 | 🇩🇪 DE | 12587 |
| 9 | 🇬🇧 GB | 12059 |
| 10 | 🇨🇴 CO | 11639 |
| 11 | 🇫🇷 FR | 10396 |
| 12 | 🇯🇵 JP | 10080 |
| 13 | 🇹🇷 TR | 7812 |
| 14 | 🇬🇷 GR | 7539 |
| 15 | 🇲🇽 MX | 7142 |
| 16 | 🇨🇭 CH | 6941 |
| 17 | 🇳🇴 NO | 6390 |
| 18 | 🇹🇭 TH | 4651 |
| 19 | 🇲🇾 MY | 4433 |
| 20 | 🇿🇦 ZA | 4392 |
| 21 | 🇵🇱 PL | 4285 |
| 22 | 🇳🇿 NZ | 3588 |
| 23 | 🇵🇭 PH | 3478 |
| 24 | 🇬🇹 GT | 3270 |
| 25 | 🇭🇷 HR | 2967 |
| 26 | 🇰🇷 KR | 2959 |
| 27 | 🇲🇦 MA | 2597 |
| 28 | 🇲🇪 ME | 2437 |
| 29 | 🇳🇱 NL | 2324 |
| 30 | 🇮🇩 ID | 2198 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5311 |
| 2 | Denver International Airport |  | US | 4189 |
| 3 | Indira Gandhi International Airport |  | IN | 3128 |
| 4 | Tokyo International Airport |  | JP | 3008 |
| 5 | Guaymaral Airport |  | CO | 2767 |
| 6 | Harry Reid International Airport |  | US | 2752 |
| 7 | Zurich Airport |  | CH | 2713 |
| 8 | El Dorado International Airport |  | CO | 2712 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2609 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2526 |
| 11 | La Aurora Airport |  | GT | 2484 |
| 12 | Salt Lake City International Airport |  | US | 2287 |
| 13 | Chicago O'Hare International Airport |  | US | 2250 |
| 14 | Congonhas Airport |  | BR | 2215 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2118 |
| 16 | Capua Airport |  | IT | 2025 |
| 17 | Madrid Barajas International Airport |  | ES | 2013 |
| 18 | Frankfurt am Main International Airport |  | DE | 1992 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1947 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1867 |
| 21 | Malpensa International Airport |  | IT | 1862 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1826 |
| 23 | Charles de Gaulle International Airport |  | FR | 1823 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1788 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1760 |
| 26 | Macau International Airport |  | MO | 1716 |
| 27 | Ninoy Aquino International Airport |  | PH | 1705 |
| 28 | Barcelona International Airport |  | ES | 1623 |
| 29 | Charlotte/Douglas International Airport |  | US | 1621 |
| 30 | Kuala Lumpur International Airport |  | MY | 1595 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1591 |
| 32 | Viracopos International Airport |  | BR | 1563 |
| 33 | Seattle-Tacoma International Airport |  | US | 1520 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1509 |
| 35 | Don Mueang International Airport |  | TH | 1487 |
| 36 | Calgary International Airport |  | CA | 1482 |
| 37 | Bengaluru International Airport |  | IN | 1470 |
| 38 | Oslo Gardermoen Airport |  | NO | 1458 |
| 39 | Vancouver International Airport |  | CA | 1452 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1393 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 966 | 21m | 244 km | 4,067.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 698 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 648 | 1h 6m | 770 km | 8,608.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 647 | 24m | 225 km | 2,510.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 578 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 419 | 27m | 275 km | 1,985.5 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 419 | 44m | 555 km | 4,012.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 392 | 44m | 241 km | 1,628.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 364 | 24m | 218 km | 1,371.3 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 356 | 21m | 250 km | 1,537.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 346 | 23m | 55 km | 328.9 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 326 | 1h 6m | 706 km | 3,969.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 322 | 19m | 99 km | 551.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 321 | 26m | 215 km | 1,188.8 t |
| 19 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 316 | 12m | - | - |
| 20 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 311 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 298 | 1h 14m | 961 km | 4,939.5 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 279 | 1h 50m | 1,304 km | 6,276.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 274 | 42m | 535 km | 2,530.6 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NWC9151 | NWC | Sheremetyevo International Airport (UUEE) | Ukhta Airport (UUYH) | 2026-09-15 03:55 UTC | 2026-09-15 05:36 UTC | 1h 41m |
| UAL946 | United Airlines | Washington Dulles International Airport (KIAD) | Amsterdam Airport Schiphol (EHAM) | 2026-09-14 22:45 UTC | 2026-09-15 05:35 UTC | 6h 49m |
| NIU | NIU | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-09-15 05:21 UTC | 2026-09-15 05:34 UTC | 13m |
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-09-14 18:01 UTC | 2026-09-15 05:32 UTC | 11h 30m |
| RYR85ZR | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | EPZB (EPZB) | 2026-09-15 04:07 UTC | 2026-09-15 05:24 UTC | 1h 16m |
| ZKIDU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-09-15 05:16 UTC | 2026-09-15 05:20 UTC | 4m |
| A6SSM |  | Fujairah International Airport (OMFJ) | Fujairah International Airport (OMFJ) | 2026-09-15 04:49 UTC | 2026-09-15 05:15 UTC | 26m |
| AIC4XV | Air India | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 2026-09-15 03:59 UTC | 2026-09-15 05:08 UTC | 1h 9m |
| YTW | YTW | Watts Bridge Airport (YWSG) | Sunshine Coast Airport (YBMC) | 2026-09-15 04:30 UTC | 2026-09-15 05:04 UTC | 34m |
| VTVSV | VTV | Cochin International Airport (VOCI) | Pune Airport (VAPO) | 2026-09-15 03:28 UTC | 2026-09-15 05:00 UTC | 1h 31m |
| A06 |  | Doha International Airport (OTBD) | Doha International Airport (OTBD) | 2026-09-15 04:52 UTC | 2026-09-15 04:56 UTC | 3m |
| IGO627 | IndiGo | Trivandrum International Airport (VOTV) | Pune Airport (VAPO) | 2026-09-15 03:19 UTC | 2026-09-15 04:55 UTC | 1h 35m |
| N713TS |  | William P Hobby Airport (KHOU) | Austin-Bergstrom International Airport (KAUS) | 2026-09-15 04:20 UTC | 2026-09-15 04:52 UTC | 32m |
| N910NM |  | Kansas City Downtown/Wheeler Field (KMKC) | Clinton Regional Airport (KGLY) | 2026-09-15 04:38 UTC | 2026-09-15 04:50 UTC | 12m |
| FFT3283 | FFT | Dallas-Fort Worth International Airport (KDFW) | Harry Reid International Airport (KLAS) | 2026-09-15 02:17 UTC | 2026-09-15 04:49 UTC | 2h 32m |
| BAW199 | British Airways | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-14 20:39 UTC | 2026-09-15 04:49 UTC | 8h 9m |
| RYR11EX | Ryanair | Eleftherios Venizelos International Airport (LGAV) | Kalymnos Airport (LGKY) | 2026-09-15 04:26 UTC | 2026-09-15 04:46 UTC | 20m |
| AAL1238 | American Airlines | Newark Liberty International Airport (KEWR) | Harry Reid International Airport (KLAS) | 2026-09-14 23:45 UTC | 2026-09-15 04:45 UTC | 5h 0m |
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-09-14 14:15 UTC | 2026-09-15 04:42 UTC | 14h 26m |
| ANZ852M | ANZ | Christchurch International Airport (NZCH) | Molesworth Airport (NZML) | 2026-09-15 04:16 UTC | 2026-09-15 04:40 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
