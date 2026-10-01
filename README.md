# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_14:31:38_UTC-green)

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

**Latest saved flight:** 2026-10-01 14:31:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-01 14:31:38 UTC

- **273,749** saved flights
- **79,889** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **273,749** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,313,704.7 tonnes** estimated CO2 emissions
- **192,098,825 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10754 |
| 2 | SkyWest Airlines | 9521 |
| 3 | EJA | 5359 |
| 4 | IndiGo | 4567 |
| 5 | American Airlines | 4238 |
| 6 | Southwest Airlines | 4025 |
| 7 | Delta Air Lines | 3397 |
| 8 | ENY | 3206 |
| 9 | LATAM Airlines | 2648 |
| 10 | AZU | 2575 |
| 11 | Vueling | 2275 |
| 12 | WIF | 2228 |
| 13 | LXJ | 2158 |
| 14 | Lufthansa | 2066 |
| 15 | easyJet | 1822 |
| 16 | Swiss International | 1792 |
| 17 | QLK | 1772 |
| 18 | EJU | 1707 |
| 19 | AXM | 1683 |
| 20 | United Airlines | 1671 |
| 21 | Alaska Airlines | 1614 |
| 22 | All Nippon Airways | 1565 |
| 23 | PGT | 1541 |
| 24 | GLO | 1528 |
| 25 | WMT | 1527 |
| 26 | Air France | 1504 |
| 27 | VIV | 1501 |
| 28 | Wizz Air | 1484 |
| 29 | CXK | 1353 |
| 30 | AEE | 1307 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 228205 |
| 2 | 🇪🇸 ES | 17128 |
| 3 | 🇧🇷 BR | 16078 |
| 4 | 🇦🇺 AU | 15819 |
| 5 | 🇨🇦 CA | 15258 |
| 6 | 🇮🇹 IT | 14775 |
| 7 | 🇮🇳 IN | 14454 |
| 8 | 🇩🇪 DE | 13123 |
| 9 | 🇨🇴 CO | 12665 |
| 10 | 🇬🇧 GB | 12618 |
| 11 | 🇫🇷 FR | 10848 |
| 12 | 🇯🇵 JP | 10454 |
| 13 | 🇹🇷 TR | 8283 |
| 14 | 🇬🇷 GR | 7876 |
| 15 | 🇲🇽 MX | 7565 |
| 16 | 🇨🇭 CH | 7265 |
| 17 | 🇳🇴 NO | 6757 |
| 18 | 🇹🇭 TH | 4900 |
| 19 | 🇲🇾 MY | 4559 |
| 20 | 🇿🇦 ZA | 4553 |
| 21 | 🇵🇱 PL | 4473 |
| 22 | 🇳🇿 NZ | 3869 |
| 23 | 🇵🇭 PH | 3612 |
| 24 | 🇬🇹 GT | 3434 |
| 25 | 🇭🇷 HR | 3117 |
| 26 | 🇰🇷 KR | 3084 |
| 27 | 🇲🇦 MA | 2705 |
| 28 | 🇲🇪 ME | 2571 |
| 29 | 🇳🇱 NL | 2452 |
| 30 | 🇮🇩 ID | 2268 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5560 |
| 2 | Denver International Airport |  | US | 4460 |
| 3 | Indira Gandhi International Airport |  | IN | 3269 |
| 4 | Tokyo International Airport |  | JP | 3134 |
| 5 | El Dorado International Airport |  | CO | 3012 |
| 6 | Harry Reid International Airport |  | US | 2946 |
| 7 | Guaymaral Airport |  | CO | 2841 |
| 8 | Zurich Airport |  | CH | 2840 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2739 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2622 |
| 11 | La Aurora Airport |  | GT | 2610 |
| 12 | Salt Lake City International Airport |  | US | 2423 |
| 13 | Congonhas Airport |  | BR | 2339 |
| 14 | Chicago O'Hare International Airport |  | US | 2320 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2241 |
| 16 | Capua Airport |  | IT | 2120 |
| 17 | Madrid Barajas International Airport |  | ES | 2107 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2080 |
| 19 | Frankfurt am Main International Airport |  | DE | 2063 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1948 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1943 |
| 22 | Malpensa International Airport |  | IT | 1943 |
| 23 | Charles de Gaulle International Airport |  | FR | 1940 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1928 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1830 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1775 |
| 28 | Charlotte/Douglas International Airport |  | US | 1711 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1699 |
| 30 | Barcelona International Airport |  | ES | 1691 |
| 31 | Viracopos International Airport |  | BR | 1642 |
| 32 | Kuala Lumpur International Airport |  | MY | 1632 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1608 |
| 34 | Seattle-Tacoma International Airport |  | US | 1602 |
| 35 | Calgary International Airport |  | CA | 1556 |
| 36 | Don Mueang International Airport |  | TH | 1547 |
| 37 | Bengaluru International Airport |  | IN | 1533 |
| 38 | Oslo Gardermoen Airport |  | NO | 1532 |
| 39 | Vancouver International Airport |  | CA | 1531 |
| 40 | Reno/Tahoe International Airport |  | US | 1477 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1130 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1030 | 21m | 244 km | 4,337.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 763 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 693 | 1h 6m | 770 km | 9,206.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 686 | 24m | 225 km | 2,661.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 604 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 458 | 44m | 555 km | 4,385.6 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 440 | 27m | 275 km | 2,085.0 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 433 | 1h 50m | 1,423 km | 10,626.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 419 | 44m | 241 km | 1,740.4 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 392 | 24m | 218 km | 1,476.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 371 | 23m | 55 km | 352.6 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 351 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 347 | 12m | - | - |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 18 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 342 | 19m | 99 km | 585.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 318 | 19m | 144 km | 791.0 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 313 | 18m | 14 km | 78.3 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 311 | 1h 14m | 961 km | 5,155.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 303 | 42m | 535 km | 2,798.4 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 295 | 1h 50m | 1,304 km | 6,636.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 271 | 44m | 431 km | 2,016.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N265FA |  | Wings Field (KLOM) | Lancaster Airport (KLNS) | 2026-10-01 13:59 UTC | 2026-10-01 14:31 UTC | 32m |
| N18NR |  | Meadows Field (KBFL) | Santa Monica Municipal Airport (KSMO) | 2026-10-01 13:43 UTC | 2026-10-01 14:25 UTC | 42m |
| SYERTN1 | SYE | RAF Syerston (EGXY) | RAF Syerston (EGXY) | 2026-10-01 12:38 UTC | 2026-10-01 14:25 UTC | 1h 46m |
| ERU98 | ERU | Big Springs Ranch Airport (AZ27) | Pilots Rest Airport (AZ57) | 2026-10-01 14:13 UTC | 2026-10-01 14:24 UTC | 10m |
| N916GW |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-10-01 13:59 UTC | 2026-10-01 14:23 UTC | 23m |
| SCA40 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-10-01 14:09 UTC | 2026-10-01 14:22 UTC | 13m |
| CXK436 | CXK | Concord-Padgett Regional Airport (KJQF) | Wilkes County Airport (KUKF) | 2026-10-01 13:37 UTC | 2026-10-01 14:22 UTC | 44m |
| STAB11 | STA | 75OK (75OK) | Kegelman Af Aux Field (KCKA) | 2026-10-01 13:59 UTC | 2026-10-01 14:20 UTC | 20m |
| OKRAV | OKR | Brno-Turany Airport (LKTB) | Brno-Turany Airport (LKTB) | 2026-10-01 13:14 UTC | 2026-10-01 14:20 UTC | 1h 5m |
| BEJ27G | BEJ | La Roche-sur-Yon Airport (LFRI) | Lyon-Bron Airport (LFLY) | 2026-10-01 13:34 UTC | 2026-10-01 14:18 UTC | 43m |
| N831MT |  | Boise Air Trml/Gowen Field (KBOI) | Mineta San Jose International Airport (KSJC) | 2026-10-01 12:56 UTC | 2026-10-01 14:17 UTC | 1h 21m |
| SPOT91 | SPO | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-10-01 13:44 UTC | 2026-10-01 14:14 UTC | 30m |
| N113UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-10-01 13:54 UTC | 2026-10-01 14:13 UTC | 18m |
| VEGA21 | VEG | Flysooner Field (OK50) | Ramey 1 Airport (0OK8) | 2026-10-01 13:47 UTC | 2026-10-01 14:10 UTC | 23m |
| ASI423 | ASI | Phoenix Deer Valley Airport (KDVT) | Wickenburg Municipal Airport (KE25) | 2026-10-01 13:34 UTC | 2026-10-01 14:08 UTC | 33m |
| EPI252 | EPI | Tucson International Airport (KTUS) | Tucson International Airport (KTUS) | 2026-10-01 13:44 UTC | 2026-10-01 14:07 UTC | 22m |
| N333CT |  | St George Regional Airport (KSGU) | UT80 (UT80) | 2026-10-01 13:38 UTC | 2026-10-01 14:03 UTC | 24m |
| TAUNT11 | TAU | Flysooner Field (OK50) | Enix Airport (OK51) | 2026-10-01 13:51 UTC | 2026-10-01 14:02 UTC | 11m |
| CGRHD | CGR | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-10-01 13:40 UTC | 2026-10-01 14:02 UTC | 22m |
| BLZR263 | BLZ | Kingsville Nas Airport (KNQI) | El Coyote Ranch Airport (2TA8) | 2026-10-01 13:21 UTC | 2026-10-01 13:58 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
