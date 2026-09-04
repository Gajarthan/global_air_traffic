# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_21:28:03_UTC-green)

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

**Latest saved flight:** 2026-09-04 21:28:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-04 21:28:03 UTC

- **247,642** saved flights
- **74,656** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **247,642** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,978,405.4 tonnes** estimated CO2 emissions
- **172,661,181 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9929 |
| 2 | SkyWest Airlines | 8653 |
| 3 | EJA | 4783 |
| 4 | IndiGo | 4134 |
| 5 | American Airlines | 3973 |
| 6 | Southwest Airlines | 3689 |
| 7 | Delta Air Lines | 3142 |
| 8 | ENY | 2962 |
| 9 | LATAM Airlines | 2390 |
| 10 | AZU | 2304 |
| 11 | Vueling | 2117 |
| 12 | WIF | 1983 |
| 13 | Lufthansa | 1970 |
| 14 | LXJ | 1924 |
| 15 | easyJet | 1713 |
| 16 | Swiss International | 1662 |
| 17 | AXM | 1619 |
| 18 | EJU | 1591 |
| 19 | QLK | 1588 |
| 20 | United Airlines | 1554 |
| 21 | Alaska Airlines | 1478 |
| 22 | All Nippon Airways | 1452 |
| 23 | WMT | 1398 |
| 24 | GLO | 1381 |
| 25 | VIV | 1360 |
| 26 | PGT | 1355 |
| 27 | Air France | 1352 |
| 28 | Wizz Air | 1337 |
| 29 | JetBlue | 1221 |
| 30 | AEE | 1218 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 205425 |
| 2 | 🇪🇸 ES | 15868 |
| 3 | 🇧🇷 BR | 14480 |
| 4 | 🇦🇺 AU | 14071 |
| 5 | 🇨🇦 CA | 13768 |
| 6 | 🇮🇹 IT | 13563 |
| 7 | 🇮🇳 IN | 12897 |
| 8 | 🇩🇪 DE | 12178 |
| 9 | 🇬🇧 GB | 11638 |
| 10 | 🇨🇴 CO | 10801 |
| 11 | 🇫🇷 FR | 9977 |
| 12 | 🇯🇵 JP | 9788 |
| 13 | 🇹🇷 TR | 7367 |
| 14 | 🇬🇷 GR | 7285 |
| 15 | 🇲🇽 MX | 6845 |
| 16 | 🇨🇭 CH | 6671 |
| 17 | 🇳🇴 NO | 6147 |
| 18 | 🇹🇭 TH | 4462 |
| 19 | 🇲🇾 MY | 4345 |
| 20 | 🇿🇦 ZA | 4281 |
| 21 | 🇵🇱 PL | 4145 |
| 22 | 🇳🇿 NZ | 3380 |
| 23 | 🇵🇭 PH | 3372 |
| 24 | 🇬🇹 GT | 3096 |
| 25 | 🇰🇷 KR | 2884 |
| 26 | 🇭🇷 HR | 2844 |
| 27 | 🇲🇦 MA | 2505 |
| 28 | 🇲🇪 ME | 2313 |
| 29 | 🇳🇱 NL | 2233 |
| 30 | 🇮🇩 ID | 2145 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5098 |
| 2 | Denver International Airport |  | US | 4002 |
| 3 | Indira Gandhi International Airport |  | IN | 3015 |
| 4 | Tokyo International Airport |  | JP | 2920 |
| 5 | Guaymaral Airport |  | CO | 2723 |
| 6 | Harry Reid International Airport |  | US | 2641 |
| 7 | Zurich Airport |  | CH | 2592 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2517 |
| 9 | El Dorado International Airport |  | CO | 2472 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2459 |
| 11 | La Aurora Airport |  | GT | 2356 |
| 12 | Salt Lake City International Airport |  | US | 2194 |
| 13 | Chicago O'Hare International Airport |  | US | 2173 |
| 14 | Congonhas Airport |  | BR | 2126 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2041 |
| 16 | Capua Airport |  | IT | 1948 |
| 17 | Madrid Barajas International Airport |  | ES | 1944 |
| 18 | Frankfurt am Main International Airport |  | DE | 1941 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1861 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1810 |
| 21 | Malpensa International Airport |  | IT | 1777 |
| 22 | Charles de Gaulle International Airport |  | FR | 1738 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1736 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1727 |
| 25 | Ninoy Aquino International Airport |  | PH | 1641 |
| 26 | Macau International Airport |  | MO | 1633 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1625 |
| 28 | Charlotte/Douglas International Airport |  | US | 1573 |
| 29 | Barcelona International Airport |  | ES | 1567 |
| 30 | Kuala Lumpur International Airport |  | MY | 1565 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1514 |
| 32 | Viracopos International Airport |  | BR | 1476 |
| 33 | Seattle-Tacoma International Airport |  | US | 1456 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1442 |
| 35 | Don Mueang International Airport |  | TH | 1434 |
| 36 | Calgary International Airport |  | CA | 1426 |
| 37 | Bengaluru International Airport |  | IN | 1426 |
| 38 | Oslo Gardermoen Airport |  | NO | 1395 |
| 39 | Vancouver International Airport |  | CA | 1383 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1345 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 919 | 21m | 244 km | 3,869.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 653 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 628 | 24m | 225 km | 2,436.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 620 | 1h 6m | 770 km | 8,236.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 554 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 408 | 27m | 275 km | 1,933.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 394 | 1h 50m | 1,423 km | 9,669.4 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 382 | 44m | 555 km | 3,657.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 368 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 367 | 44m | 241 km | 1,524.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 346 | 24m | 218 km | 1,303.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 333 | 23m | 55 km | 316.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 292 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 286 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 285 | 1h 14m | 961 km | 4,724.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 283 | 19m | 144 km | 703.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 269 | 1h 50m | 1,304 km | 6,051.8 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 255 | 28m | 152 km | 666.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N33RK |  | Peter O Knight Airport (KTPF) | Orlando Executive Airport (KORL) | 2026-09-04 20:56 UTC | 2026-09-04 21:28 UTC | 31m |
| CAL007 | CAL | Los Angeles International Airport (KLAX) | Taiwan Taoyuan International Airport (RCTP) | 2026-09-04 08:22 UTC | 2026-09-04 21:21 UTC | 12h 59m |
| N429RL |  | Ayers Field (8XS2) | Quetzalcoatl International Airport (MMNL) | 2026-09-04 21:00 UTC | 2026-09-04 21:21 UTC | 21m |
| N13658 |  | Lake Elmo Airport (K21D) | Lake Elmo Airport (K21D) | 2026-09-04 20:28 UTC | 2026-09-04 21:19 UTC | 51m |
| N991TH |  | Columbia Metro Airport (KCAE) | SC60 (SC60) | 2026-09-04 20:59 UTC | 2026-09-04 21:11 UTC | 12m |
| N738KA |  | Savannah/Hilton Head International Airport (KSAV) | Hilton Head Airport (KHXD) | 2026-09-04 20:57 UTC | 2026-09-04 21:08 UTC | 10m |
| N835ZT |  | Indianapolis Executive Airport (KTYQ) | Cherry Capital Airport (KTVC) | 2026-09-04 20:22 UTC | 2026-09-04 21:07 UTC | 45m |
| CXK179 | CXK | Wayne Executive Jetport Airport (KGWW) | Wayne Executive Jetport Airport (KGWW) | 2026-09-04 20:49 UTC | 2026-09-04 21:07 UTC | 17m |
| N1882S |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-09-04 20:29 UTC | 2026-09-04 21:06 UTC | 36m |
| N22GS |  | Fort Worth Meacham International Airport (KFTW) | Arledge Field (KF56) | 2026-09-04 20:35 UTC | 2026-09-04 21:03 UTC | 27m |
| N94SF |  | Tyler Pounds Regional Airport (KTYR) | Austin-Bergstrom International Airport (KAUS) | 2026-09-04 20:28 UTC | 2026-09-04 21:02 UTC | 34m |
| N473HB |  | Mahlon Sweet Field (KEUG) | Chamberlain Airport (OR60) | 2026-09-04 20:40 UTC | 2026-09-04 21:02 UTC | 21m |
| CAP5034 | CAP | Merrill Field (PAMR) | Ted Stevens Anchorage International Airport (PANC) | 2026-09-04 20:41 UTC | 2026-09-04 20:58 UTC | 17m |
| N125PM |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-09-04 20:01 UTC | 2026-09-04 20:57 UTC | 56m |
| N366EA |  | Glendale Regional Airport (KGEU) | Bagdad Airport (KE51) | 2026-09-04 19:52 UTC | 2026-09-04 20:57 UTC | 1h 4m |
| N227TW |  | French Valley Airport (KF70) | Hemet-Ryan Airport (KHMT) | 2026-09-04 20:24 UTC | 2026-09-04 20:56 UTC | 31m |
| PAWS31 | PAW | Enix Airport (OK51) | Herington Regional Airport (KHRU) | 2026-09-04 20:14 UTC | 2026-09-04 20:49 UTC | 34m |
| WMU63 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | Battle Creek Executive At Kellogg Field (KBTL) | 2026-09-04 19:43 UTC | 2026-09-04 20:48 UTC | 1h 5m |
| N620AS |  | Henderson Executive Airport (KHND) | 1TX7 (1TX7) | 2026-09-04 18:32 UTC | 2026-09-04 20:46 UTC | 2h 13m |
| N412MH |  | Portland International Airport (KPDX) | Cascade Airport (KU70) | 2026-09-04 19:55 UTC | 2026-09-04 20:43 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
