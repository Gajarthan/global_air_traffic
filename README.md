# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_18:50:51_UTC-green)

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

**Latest saved flight:** 2026-09-15 18:50:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-15 18:50:51 UTC

- **259,483** saved flights
- **77,031** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **259,483** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,142,126.0 tonnes** estimated CO2 emissions
- **182,152,230 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10281 |
| 2 | SkyWest Airlines | 9043 |
| 3 | EJA | 5032 |
| 4 | IndiGo | 4353 |
| 5 | American Airlines | 4090 |
| 6 | Southwest Airlines | 3816 |
| 7 | Delta Air Lines | 3240 |
| 8 | ENY | 3073 |
| 9 | LATAM Airlines | 2497 |
| 10 | AZU | 2435 |
| 11 | Vueling | 2193 |
| 12 | WIF | 2086 |
| 13 | LXJ | 2030 |
| 14 | Lufthansa | 2022 |
| 15 | easyJet | 1766 |
| 16 | Swiss International | 1731 |
| 17 | QLK | 1675 |
| 18 | AXM | 1649 |
| 19 | EJU | 1643 |
| 20 | United Airlines | 1598 |
| 21 | Alaska Airlines | 1539 |
| 22 | All Nippon Airways | 1503 |
| 23 | WMT | 1464 |
| 24 | PGT | 1445 |
| 25 | GLO | 1444 |
| 26 | VIV | 1423 |
| 27 | Air France | 1419 |
| 28 | Wizz Air | 1413 |
| 29 | AEE | 1254 |
| 30 | TKR | 1253 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 215425 |
| 2 | 🇪🇸 ES | 16435 |
| 3 | 🇧🇷 BR | 15166 |
| 4 | 🇦🇺 AU | 14800 |
| 5 | 🇨🇦 CA | 14443 |
| 6 | 🇮🇹 IT | 14125 |
| 7 | 🇮🇳 IN | 13707 |
| 8 | 🇩🇪 DE | 12605 |
| 9 | 🇬🇧 GB | 12083 |
| 10 | 🇨🇴 CO | 11665 |
| 11 | 🇫🇷 FR | 10414 |
| 12 | 🇯🇵 JP | 10093 |
| 13 | 🇹🇷 TR | 7835 |
| 14 | 🇬🇷 GR | 7547 |
| 15 | 🇲🇽 MX | 7158 |
| 16 | 🇨🇭 CH | 6969 |
| 17 | 🇳🇴 NO | 6410 |
| 18 | 🇹🇭 TH | 4662 |
| 19 | 🇲🇾 MY | 4437 |
| 20 | 🇿🇦 ZA | 4398 |
| 21 | 🇵🇱 PL | 4288 |
| 22 | 🇳🇿 NZ | 3590 |
| 23 | 🇵🇭 PH | 3479 |
| 24 | 🇬🇹 GT | 3301 |
| 25 | 🇭🇷 HR | 2970 |
| 26 | 🇰🇷 KR | 2961 |
| 27 | 🇲🇦 MA | 2601 |
| 28 | 🇲🇪 ME | 2444 |
| 29 | 🇳🇱 NL | 2328 |
| 30 | 🇮🇩 ID | 2198 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5317 |
| 2 | Denver International Airport |  | US | 4198 |
| 3 | Indira Gandhi International Airport |  | IN | 3132 |
| 4 | Tokyo International Airport |  | JP | 3010 |
| 5 | Guaymaral Airport |  | CO | 2767 |
| 6 | Harry Reid International Airport |  | US | 2754 |
| 7 | El Dorado International Airport |  | CO | 2720 |
| 8 | Zurich Airport |  | CH | 2720 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2611 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2528 |
| 11 | La Aurora Airport |  | GT | 2506 |
| 12 | Salt Lake City International Airport |  | US | 2289 |
| 13 | Chicago O'Hare International Airport |  | US | 2251 |
| 14 | Congonhas Airport |  | BR | 2218 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2121 |
| 16 | Capua Airport |  | IT | 2028 |
| 17 | Madrid Barajas International Airport |  | ES | 2016 |
| 18 | Frankfurt am Main International Airport |  | DE | 1994 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1951 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1869 |
| 21 | Malpensa International Airport |  | IT | 1865 |
| 22 | Charles de Gaulle International Airport |  | FR | 1829 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1826 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1789 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1764 |
| 26 | Macau International Airport |  | MO | 1719 |
| 27 | Ninoy Aquino International Airport |  | PH | 1706 |
| 28 | Barcelona International Airport |  | ES | 1625 |
| 29 | Charlotte/Douglas International Airport |  | US | 1622 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1596 |
| 31 | Kuala Lumpur International Airport |  | MY | 1595 |
| 32 | Viracopos International Airport |  | BR | 1569 |
| 33 | Seattle-Tacoma International Airport |  | US | 1521 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1512 |
| 35 | Don Mueang International Airport |  | TH | 1489 |
| 36 | Calgary International Airport |  | CA | 1484 |
| 37 | Bengaluru International Airport |  | IN | 1473 |
| 38 | Oslo Gardermoen Airport |  | NO | 1461 |
| 39 | Vancouver International Airport |  | CA | 1453 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1396 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 967 | 21m | 244 km | 4,071.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 700 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 649 | 1h 6m | 770 km | 8,621.5 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 647 | 24m | 225 km | 2,510.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 582 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 420 | 44m | 555 km | 4,021.7 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 419 | 27m | 275 km | 1,985.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 394 | 44m | 241 km | 1,636.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 365 | 24m | 218 km | 1,375.1 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 357 | 21m | 250 km | 1,542.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 348 | 23m | 55 km | 330.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 326 | 1h 6m | 706 km | 3,969.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 326 | 19m | 99 km | 558.4 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 321 | 26m | 215 km | 1,188.8 t |
| 19 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 316 | 12m | - | - |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 315 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 298 | 1h 14m | 961 km | 4,939.5 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 279 | 1h 50m | 1,304 km | 6,276.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 275 | 42m | 535 km | 2,539.8 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 273 | 28m | 152 km | 713.5 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CONGO63 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-09-15 18:25 UTC | 2026-09-15 18:50 UTC | 24m |
| N458MM |  | San Carlos Airport (KSQL) | Sacramento Mather Airport (KMHR) | 2026-09-15 18:01 UTC | 2026-09-15 18:43 UTC | 41m |
| N753BL |  | Santa Barbara Municipal Airport (KSBA) | Sacramento International Airport (KSMF) | 2026-09-15 17:23 UTC | 2026-09-15 18:43 UTC | 1h 19m |
| N6544 |  | Winter Haven Regional Airport (KGIF) | Orlampa Inc Airport (FA08) | 2026-09-15 18:20 UTC | 2026-09-15 18:42 UTC | 21m |
| MSR782 | EgyptAir | Manchester Airport (EGCC) | HE42 (HE42) | 2026-09-15 14:10 UTC | 2026-09-15 18:33 UTC | 4h 23m |
| N1602M |  | Harford County Airport (K0W3) | Carroll County Regional/Jack B Poage Field (KDMW) | 2026-09-15 17:47 UTC | 2026-09-15 18:33 UTC | 46m |
| 1820991 |  | Lakehurst Maxfield Field (KNEL) | Newark Liberty International Airport (KEWR) | 2026-09-15 17:59 UTC | 2026-09-15 18:33 UTC | 33m |
| RATLR02 | RAT | 2TX3 (2TX3) | Anacacho Ranch Airport (0XS7) | 2026-09-15 18:22 UTC | 2026-09-15 18:32 UTC | 10m |
| N156XL |  | Hollywood Burbank Airport (KBUR) | Aztec Municipal Airport (KN19) | 2026-09-15 17:10 UTC | 2026-09-15 18:28 UTC | 1h 18m |
| WIF6Y | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-09-15 18:15 UTC | 2026-09-15 18:27 UTC | 11m |
| N745BA |  | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-09-15 17:22 UTC | 2026-09-15 18:20 UTC | 58m |
| TGVAV | TGV | San Jose Airport (MGSJ) | La Aurora Airport (MGGT) | 2026-09-15 17:55 UTC | 2026-09-15 18:20 UTC | 24m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-09-15 17:41 UTC | 2026-09-15 18:20 UTC | 38m |
| TKR41 | TKR | TX11 (TX11) | TX11 (TX11) | 2026-09-15 17:43 UTC | 2026-09-15 18:20 UTC | 37m |
| 0 |  | XA65 (XA65) | Baylie Airport (66XS) | 2026-09-15 17:57 UTC | 2026-09-15 18:20 UTC | 22m |
| XBSKT | XBS | Hermanos Serdan International Airport (MMPB) | Tlaxcala Airport (MMTA) | 2026-09-15 18:09 UTC | 2026-09-15 18:19 UTC | 10m |
| N99JW |  | Corpus Christi International Airport (KCRP) | Sugar Land Regional Airport (KSGR) | 2026-09-15 17:42 UTC | 2026-09-15 18:19 UTC | 36m |
| VULCN91 | VUL | Flysooner Field (OK50) | Walker Family Farm Airport (OK14) | 2026-09-15 17:51 UTC | 2026-09-15 18:18 UTC | 27m |
| N734RE |  | Montgomery-Gibbs Executive Airport (KMYF) | Gillespie Field (KSEE) | 2026-09-15 17:45 UTC | 2026-09-15 18:18 UTC | 32m |
| DLH766 | Lufthansa | Munich International Airport (EDDM) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-15 10:54 UTC | 2026-09-15 18:15 UTC | 7h 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
