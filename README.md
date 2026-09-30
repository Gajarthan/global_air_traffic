# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_13:31:12_UTC-green)

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

**Latest saved flight:** 2026-09-30 13:31:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-30 13:31:12 UTC

- **272,989** saved flights
- **79,728** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **272,989** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,306,333.4 tonnes** estimated CO2 emissions
- **191,671,499 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10730 |
| 2 | SkyWest Airlines | 9505 |
| 3 | EJA | 5341 |
| 4 | IndiGo | 4560 |
| 5 | American Airlines | 4234 |
| 6 | Southwest Airlines | 4014 |
| 7 | Delta Air Lines | 3391 |
| 8 | ENY | 3201 |
| 9 | LATAM Airlines | 2637 |
| 10 | AZU | 2565 |
| 11 | Vueling | 2269 |
| 12 | WIF | 2222 |
| 13 | LXJ | 2148 |
| 14 | Lufthansa | 2064 |
| 15 | easyJet | 1820 |
| 16 | Swiss International | 1786 |
| 17 | QLK | 1760 |
| 18 | EJU | 1704 |
| 19 | AXM | 1681 |
| 20 | United Airlines | 1668 |
| 21 | Alaska Airlines | 1610 |
| 22 | All Nippon Airways | 1563 |
| 23 | PGT | 1539 |
| 24 | GLO | 1523 |
| 25 | WMT | 1520 |
| 26 | Air France | 1501 |
| 27 | VIV | 1494 |
| 28 | Wizz Air | 1481 |
| 29 | CXK | 1349 |
| 30 | AEE | 1305 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 227492 |
| 2 | 🇪🇸 ES | 17075 |
| 3 | 🇧🇷 BR | 16024 |
| 4 | 🇦🇺 AU | 15762 |
| 5 | 🇨🇦 CA | 15209 |
| 6 | 🇮🇹 IT | 14739 |
| 7 | 🇮🇳 IN | 14427 |
| 8 | 🇩🇪 DE | 13093 |
| 9 | 🇨🇴 CO | 12609 |
| 10 | 🇬🇧 GB | 12592 |
| 11 | 🇫🇷 FR | 10832 |
| 12 | 🇯🇵 JP | 10436 |
| 13 | 🇹🇷 TR | 8265 |
| 14 | 🇬🇷 GR | 7862 |
| 15 | 🇲🇽 MX | 7540 |
| 16 | 🇨🇭 CH | 7253 |
| 17 | 🇳🇴 NO | 6740 |
| 18 | 🇹🇭 TH | 4891 |
| 19 | 🇲🇾 MY | 4554 |
| 20 | 🇿🇦 ZA | 4551 |
| 21 | 🇵🇱 PL | 4467 |
| 22 | 🇳🇿 NZ | 3854 |
| 23 | 🇵🇭 PH | 3604 |
| 24 | 🇬🇹 GT | 3430 |
| 25 | 🇭🇷 HR | 3106 |
| 26 | 🇰🇷 KR | 3076 |
| 27 | 🇲🇦 MA | 2703 |
| 28 | 🇲🇪 ME | 2564 |
| 29 | 🇳🇱 NL | 2446 |
| 30 | 🇮🇩 ID | 2268 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5555 |
| 2 | Denver International Airport |  | US | 4451 |
| 3 | Indira Gandhi International Airport |  | IN | 3259 |
| 4 | Tokyo International Airport |  | JP | 3127 |
| 5 | El Dorado International Airport |  | CO | 2999 |
| 6 | Harry Reid International Airport |  | US | 2934 |
| 7 | Guaymaral Airport |  | CO | 2838 |
| 8 | Zurich Airport |  | CH | 2832 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2735 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2618 |
| 11 | La Aurora Airport |  | GT | 2607 |
| 12 | Salt Lake City International Airport |  | US | 2420 |
| 13 | Congonhas Airport |  | BR | 2330 |
| 14 | Chicago O'Hare International Airport |  | US | 2318 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2233 |
| 16 | Capua Airport |  | IT | 2113 |
| 17 | Madrid Barajas International Airport |  | ES | 2102 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2071 |
| 19 | Frankfurt am Main International Airport |  | DE | 2060 |
| 20 | Malpensa International Airport |  | IT | 1938 |
| 21 | Charles de Gaulle International Airport |  | FR | 1937 |
| 22 | Enrique Olaya Herrera Airport |  | CO | 1936 |
| 23 | Hartsfield/Jackson Atlanta International Airport |  | US | 1936 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1916 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1830 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1771 |
| 28 | Charlotte/Douglas International Airport |  | US | 1708 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1699 |
| 30 | Barcelona International Airport |  | ES | 1689 |
| 31 | Viracopos International Airport |  | BR | 1640 |
| 32 | Kuala Lumpur International Airport |  | MY | 1631 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1601 |
| 34 | Seattle-Tacoma International Airport |  | US | 1599 |
| 35 | Calgary International Airport |  | CA | 1549 |
| 36 | Don Mueang International Airport |  | TH | 1545 |
| 37 | Bengaluru International Airport |  | IN | 1531 |
| 38 | Oslo Gardermoen Airport |  | NO | 1528 |
| 39 | Vancouver International Airport |  | CA | 1525 |
| 40 | Reno/Tahoe International Airport |  | US | 1465 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1129 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1026 | 21m | 244 km | 4,320.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 759 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 689 | 1h 6m | 770 km | 9,152.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 684 | 24m | 225 km | 2,653.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 603 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 457 | 44m | 555 km | 4,376.0 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 439 | 27m | 275 km | 2,080.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 431 | 1h 50m | 1,423 km | 10,577.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 418 | 44m | 241 km | 1,736.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 391 | 24m | 218 km | 1,473.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 381 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 367 | 23m | 55 km | 348.8 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 350 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 347 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 339 | 26m | 215 km | 1,255.5 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 318 | 19m | 144 km | 791.0 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 309 | 1h 14m | 961 km | 5,121.8 t |
| 24 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 307 | 18m | 14 km | 76.8 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 302 | 42m | 535 km | 2,789.2 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 295 | 1h 50m | 1,304 km | 6,636.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 271 | 44m | 431 km | 2,016.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N522FL |  | Cape May County Airport (KWWD) | South Jersey Regional Airport (KVAY) | 2026-09-30 12:43 UTC | 2026-09-30 13:31 UTC | 48m |
| N9151L |  | Union County Airport (KMRT) | Bellefontaine Regional Airport (KEDJ) | 2026-09-30 13:04 UTC | 2026-09-30 13:25 UTC | 20m |
| N653HB |  | Mcknight Airport (5OI8) | Knox County Airport (K4I3) | 2026-09-30 12:42 UTC | 2026-09-30 13:24 UTC | 42m |
| AIB84IL | AIB | Toulouse-Blagnac Airport (LFBO) | Toulouse-Blagnac Airport (LFBO) | 2026-09-30 12:50 UTC | 2026-09-30 13:15 UTC | 25m |
| ABY685 | ABY | Eleftherios Venizelos International Airport (LGAV) | Queen Alia International Airport (OJAI) | 2026-09-30 11:48 UTC | 2026-09-30 13:11 UTC | 1h 23m |
| N619PF |  | Chorman Airport (KD74) | Whalen Field (25MD) | 2026-09-30 12:20 UTC | 2026-09-30 13:09 UTC | 49m |
| N831AF |  | Addison Airport (KADS) | Gainesville Municipal Airport (KGLE) | 2026-09-30 12:34 UTC | 2026-09-30 13:09 UTC | 34m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-09-30 12:49 UTC | 2026-09-30 13:08 UTC | 18m |
| GAF390 | GAF | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-09-30 12:42 UTC | 2026-09-30 13:08 UTC | 25m |
| ELY396 | ELY | Madrid Barajas International Airport (LEMD) | Queen Alia International Airport (OJAI) | 2026-09-30 09:17 UTC | 2026-09-30 13:07 UTC | 3h 50m |
| R51264 |  | Dothan Regional Airport (KDHN) | Dothan Regional Airport (KDHN) | 2026-09-30 12:33 UTC | 2026-09-30 13:07 UTC | 34m |
| N1954T |  | Savannah/Hilton Head International Airport (KSAV) | Ridgeland-Claude Dean Airport (K3J1) | 2026-09-30 12:36 UTC | 2026-09-30 13:00 UTC | 24m |
| N249K |  | Prescott Regional/Ernest A Love Field (KPRC) | Robin Airport (59AZ) | 2026-09-30 12:56 UTC | 2026-09-30 12:59 UTC | 3m |
| FHVYC | FHV | Valenciennes-Denain Airport (LFAV) | Lyon-Bron Airport (LFLY) | 2026-09-30 12:02 UTC | 2026-09-30 12:58 UTC | 55m |
| RJA860 | Royal Jordanian | Amman-Marka International Airport (OJAM) | Queen Alia International Airport (OJAI) | 2026-09-30 12:46 UTC | 2026-09-30 12:57 UTC | 11m |
| ROKT11 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bird Nest Airport (4MS5) | 2026-09-30 12:38 UTC | 2026-09-30 12:56 UTC | 17m |
| WIF850 | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-09-30 12:43 UTC | 2026-09-30 12:56 UTC | 12m |
| SYS47 | SYS | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-09-30 08:23 UTC | 2026-09-30 12:52 UTC | 4h 28m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Melanes Airport (BIMN) | 2026-09-30 12:30 UTC | 2026-09-30 12:52 UTC | 21m |
| NQB | NQB | Halls Creek Airport (YHLC) | Halls Creek Airport (YHLC) | 2026-09-30 12:19 UTC | 2026-09-30 12:51 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
