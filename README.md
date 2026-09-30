# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_06:55:15_UTC-green)

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

**Latest saved flight:** 2026-09-30 06:55:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-30 06:55:15 UTC

- **272,848** saved flights
- **79,717** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **272,848** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,304,864.8 tonnes** estimated CO2 emissions
- **191,586,366 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10725 |
| 2 | SkyWest Airlines | 9505 |
| 3 | EJA | 5340 |
| 4 | IndiGo | 4557 |
| 5 | American Airlines | 4234 |
| 6 | Southwest Airlines | 4014 |
| 7 | Delta Air Lines | 3391 |
| 8 | ENY | 3201 |
| 9 | LATAM Airlines | 2632 |
| 10 | AZU | 2562 |
| 11 | Vueling | 2269 |
| 12 | WIF | 2218 |
| 13 | LXJ | 2148 |
| 14 | Lufthansa | 2063 |
| 15 | easyJet | 1820 |
| 16 | Swiss International | 1784 |
| 17 | QLK | 1760 |
| 18 | EJU | 1702 |
| 19 | AXM | 1680 |
| 20 | United Airlines | 1668 |
| 21 | Alaska Airlines | 1610 |
| 22 | All Nippon Airways | 1563 |
| 23 | PGT | 1538 |
| 24 | GLO | 1522 |
| 25 | WMT | 1520 |
| 26 | Air France | 1499 |
| 27 | VIV | 1494 |
| 28 | Wizz Air | 1481 |
| 29 | CXK | 1348 |
| 30 | AEE | 1305 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 227438 |
| 2 | 🇪🇸 ES | 17068 |
| 3 | 🇧🇷 BR | 16001 |
| 4 | 🇦🇺 AU | 15757 |
| 5 | 🇨🇦 CA | 15207 |
| 6 | 🇮🇹 IT | 14731 |
| 7 | 🇮🇳 IN | 14420 |
| 8 | 🇩🇪 DE | 13075 |
| 9 | 🇨🇴 CO | 12589 |
| 10 | 🇬🇧 GB | 12585 |
| 11 | 🇫🇷 FR | 10825 |
| 12 | 🇯🇵 JP | 10436 |
| 13 | 🇹🇷 TR | 8261 |
| 14 | 🇬🇷 GR | 7859 |
| 15 | 🇲🇽 MX | 7540 |
| 16 | 🇨🇭 CH | 7245 |
| 17 | 🇳🇴 NO | 6730 |
| 18 | 🇹🇭 TH | 4884 |
| 19 | 🇲🇾 MY | 4552 |
| 20 | 🇿🇦 ZA | 4545 |
| 21 | 🇵🇱 PL | 4467 |
| 22 | 🇳🇿 NZ | 3854 |
| 23 | 🇵🇭 PH | 3604 |
| 24 | 🇬🇹 GT | 3428 |
| 25 | 🇭🇷 HR | 3104 |
| 26 | 🇰🇷 KR | 3076 |
| 27 | 🇲🇦 MA | 2701 |
| 28 | 🇲🇪 ME | 2558 |
| 29 | 🇳🇱 NL | 2446 |
| 30 | 🇮🇩 ID | 2268 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5555 |
| 2 | Denver International Airport |  | US | 4451 |
| 3 | Indira Gandhi International Airport |  | IN | 3258 |
| 4 | Tokyo International Airport |  | JP | 3127 |
| 5 | El Dorado International Airport |  | CO | 2994 |
| 6 | Harry Reid International Airport |  | US | 2934 |
| 7 | Guaymaral Airport |  | CO | 2833 |
| 8 | Zurich Airport |  | CH | 2829 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2735 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2616 |
| 11 | La Aurora Airport |  | GT | 2605 |
| 12 | Salt Lake City International Airport |  | US | 2420 |
| 13 | Congonhas Airport |  | BR | 2328 |
| 14 | Chicago O'Hare International Airport |  | US | 2317 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2233 |
| 16 | Capua Airport |  | IT | 2111 |
| 17 | Madrid Barajas International Airport |  | ES | 2100 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2067 |
| 19 | Frankfurt am Main International Airport |  | DE | 2060 |
| 20 | Malpensa International Airport |  | IT | 1938 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1936 |
| 22 | Charles de Gaulle International Airport |  | FR | 1935 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1933 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1916 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1830 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1771 |
| 28 | Charlotte/Douglas International Airport |  | US | 1707 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1699 |
| 30 | Barcelona International Airport |  | ES | 1689 |
| 31 | Viracopos International Airport |  | BR | 1640 |
| 32 | Kuala Lumpur International Airport |  | MY | 1630 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1601 |
| 34 | Seattle-Tacoma International Airport |  | US | 1599 |
| 35 | Calgary International Airport |  | CA | 1549 |
| 36 | Don Mueang International Airport |  | TH | 1543 |
| 37 | Bengaluru International Airport |  | IN | 1531 |
| 38 | Oslo Gardermoen Airport |  | NO | 1527 |
| 39 | Vancouver International Airport |  | CA | 1525 |
| 40 | Reno/Tahoe International Airport |  | US | 1465 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1127 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1025 | 21m | 244 km | 4,316.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 758 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 689 | 1h 6m | 770 km | 9,152.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 684 | 24m | 225 km | 2,653.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 456 | 44m | 555 km | 4,366.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 439 | 27m | 275 km | 2,080.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 431 | 1h 50m | 1,423 km | 10,577.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 418 | 44m | 241 km | 1,736.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 391 | 24m | 218 km | 1,473.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 380 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 369 | 21m | 250 km | 1,593.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 367 | 23m | 55 km | 348.8 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 349 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 347 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 338 | 26m | 215 km | 1,251.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 317 | 19m | 144 km | 788.5 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 309 | 1h 14m | 961 km | 5,121.8 t |
| 24 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 306 | 18m | 14 km | 76.5 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 302 | 42m | 535 km | 2,789.2 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 295 | 1h 50m | 1,304 km | 6,636.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 271 | 44m | 431 km | 2,016.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SPKOG | SPK | Babice Airport (EPBC) | Warsaw Modlin Airport (EPMO) | 2026-09-30 06:39 UTC | 2026-09-30 06:55 UTC | 15m |
| BBX55A | BBX | De Kooy Airport (EHKD) | Borkum Airport (EDWR) | 2026-09-30 06:07 UTC | 2026-09-30 06:50 UTC | 43m |
| FGIBV | FGI | Ghisonaccia Alzitone Airport (LFKG) | Ghisonaccia Alzitone Airport (LFKG) | 2026-09-30 05:34 UTC | 2026-09-30 06:39 UTC | 1h 5m |
| CHX100 | CHX | Berlin-Tegel International Airport (EDDT) | Berlin-Tegel International Airport (EDDT) | 2026-09-30 06:32 UTC | 2026-09-30 06:35 UTC | 3m |
| HSOWA1 | HSO | Emden Airport (EDWE) | Borkum Airport (EDWR) | 2026-09-30 06:09 UTC | 2026-09-30 06:33 UTC | 24m |
| FD231 |  | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-09-30 05:57 UTC | 2026-09-30 06:19 UTC | 22m |
| WIF5DB | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-09-30 05:48 UTC | 2026-09-30 06:11 UTC | 23m |
| IGO58DA | IndiGo | Indira Gandhi International Airport (VIDP) | VIBN (VIBN) | 2026-09-30 05:13 UTC | 2026-09-30 06:05 UTC | 51m |
| GAP2037 | GAP | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-09-30 05:38 UTC | 2026-09-30 06:03 UTC | 24m |
| ZSLBD | ZSL | O. R. Tambo International Airport (FAOR) | Thabazimbi Airport (FATI) | 2026-09-30 05:22 UTC | 2026-09-30 06:03 UTC | 41m |
| QLK42D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Fairview Airport (YFVW) | 2026-09-30 05:29 UTC | 2026-09-30 06:00 UTC | 31m |
| N648BH |  | Kenosha Regional Airport (KENW) | General Mitchell International Airport (KMKE) | 2026-09-30 05:45 UTC | 2026-09-30 06:00 UTC | 14m |
| MTNG402 | MTN | Kamphaeng Saen Airport (VTBK) | Prachuap Airport (VTBP) | 2026-09-30 05:27 UTC | 2026-09-30 06:00 UTC | 32m |
| QAV30E | QAV | Larnaca International Airport (LCLK) | Ohrid St. Paul the Apostle Airport (LWOH) | 2026-09-30 04:07 UTC | 2026-09-30 05:59 UTC | 1h 51m |
| ASA1122 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-09-30 05:36 UTC | 2026-09-30 05:57 UTC | 20m |
| RYR7GH | Ryanair | John Paul II International Airport Kraków-Balice Airport (EPKK) | EPKI (EPKI) | 2026-09-30 05:31 UTC | 2026-09-30 05:56 UTC | 24m |
| RYR9858 | Ryanair | Malpensa International Airport (LIMC) | Dolna Banya Airport (LBDB) | 2026-09-30 04:15 UTC | 2026-09-30 05:56 UTC | 1h 40m |
| CGWRS | CGW | Edmonton International Airport (CYEG) | St. Paul Airport (CEW3) | 2026-09-30 05:32 UTC | 2026-09-30 05:55 UTC | 23m |
| RYR5MM | Ryanair | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Chania International Airport (LGSA) | 2026-09-30 04:19 UTC | 2026-09-30 05:55 UTC | 1h 35m |
| AM341 |  | Melbourne Essendon Airport (YMEN) | Lake Leagur Airport (YLLR) | 2026-09-30 05:18 UTC | 2026-09-30 05:55 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
