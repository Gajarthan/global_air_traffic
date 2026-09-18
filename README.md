# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_20:10:55_UTC-green)

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

**Latest saved flight:** 2026-09-18 20:10:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-18 20:10:55 UTC

- **262,750** saved flights
- **77,705** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **262,750** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,182,908.8 tonnes** estimated CO2 emissions
- **184,516,452 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10400 |
| 2 | SkyWest Airlines | 9144 |
| 3 | EJA | 5091 |
| 4 | IndiGo | 4415 |
| 5 | American Airlines | 4122 |
| 6 | Southwest Airlines | 3858 |
| 7 | Delta Air Lines | 3281 |
| 8 | ENY | 3100 |
| 9 | LATAM Airlines | 2528 |
| 10 | AZU | 2468 |
| 11 | Vueling | 2210 |
| 12 | WIF | 2125 |
| 13 | LXJ | 2060 |
| 14 | Lufthansa | 2030 |
| 15 | easyJet | 1777 |
| 16 | Swiss International | 1736 |
| 17 | QLK | 1698 |
| 18 | EJU | 1656 |
| 19 | AXM | 1655 |
| 20 | United Airlines | 1610 |
| 21 | Alaska Airlines | 1557 |
| 22 | All Nippon Airways | 1518 |
| 23 | WMT | 1479 |
| 24 | PGT | 1475 |
| 25 | GLO | 1466 |
| 26 | Air France | 1441 |
| 27 | VIV | 1434 |
| 28 | Wizz Air | 1428 |
| 29 | TKR | 1275 |
| 30 | CXK | 1273 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 218288 |
| 2 | 🇪🇸 ES | 16580 |
| 3 | 🇧🇷 BR | 15369 |
| 4 | 🇦🇺 AU | 15074 |
| 5 | 🇨🇦 CA | 14623 |
| 6 | 🇮🇹 IT | 14281 |
| 7 | 🇮🇳 IN | 13946 |
| 8 | 🇩🇪 DE | 12706 |
| 9 | 🇬🇧 GB | 12210 |
| 10 | 🇨🇴 CO | 11882 |
| 11 | 🇫🇷 FR | 10511 |
| 12 | 🇯🇵 JP | 10179 |
| 13 | 🇹🇷 TR | 7954 |
| 14 | 🇬🇷 GR | 7628 |
| 15 | 🇲🇽 MX | 7223 |
| 16 | 🇨🇭 CH | 7016 |
| 17 | 🇳🇴 NO | 6500 |
| 18 | 🇹🇭 TH | 4707 |
| 19 | 🇲🇾 MY | 4463 |
| 20 | 🇿🇦 ZA | 4432 |
| 21 | 🇵🇱 PL | 4333 |
| 22 | 🇳🇿 NZ | 3639 |
| 23 | 🇵🇭 PH | 3499 |
| 24 | 🇬🇹 GT | 3350 |
| 25 | 🇭🇷 HR | 3000 |
| 26 | 🇰🇷 KR | 2987 |
| 27 | 🇲🇦 MA | 2627 |
| 28 | 🇲🇪 ME | 2466 |
| 29 | 🇳🇱 NL | 2347 |
| 30 | 🇮🇩 ID | 2213 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5374 |
| 2 | Denver International Airport |  | US | 4250 |
| 3 | Indira Gandhi International Airport |  | IN | 3157 |
| 4 | Tokyo International Airport |  | JP | 3038 |
| 5 | Harry Reid International Airport |  | US | 2795 |
| 6 | Guaymaral Airport |  | CO | 2779 |
| 7 | El Dorado International Airport |  | CO | 2776 |
| 8 | Zurich Airport |  | CH | 2738 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2643 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2547 |
| 11 | La Aurora Airport |  | GT | 2546 |
| 12 | Salt Lake City International Airport |  | US | 2321 |
| 13 | Chicago O'Hare International Airport |  | US | 2263 |
| 14 | Congonhas Airport |  | BR | 2243 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2148 |
| 16 | Capua Airport |  | IT | 2052 |
| 17 | Madrid Barajas International Airport |  | ES | 2033 |
| 18 | Frankfurt am Main International Airport |  | DE | 2004 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1979 |
| 20 | Malpensa International Airport |  | IT | 1889 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1883 |
| 22 | Charles de Gaulle International Airport |  | FR | 1859 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1850 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1814 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1797 |
| 26 | Macau International Airport |  | MO | 1743 |
| 27 | Ninoy Aquino International Airport |  | PH | 1716 |
| 28 | Barcelona International Airport |  | ES | 1640 |
| 29 | Charlotte/Douglas International Airport |  | US | 1637 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1614 |
| 31 | Kuala Lumpur International Airport |  | MY | 1601 |
| 32 | Viracopos International Airport |  | BR | 1594 |
| 33 | Seattle-Tacoma International Airport |  | US | 1541 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1529 |
| 35 | Don Mueang International Airport |  | TH | 1498 |
| 36 | Calgary International Airport |  | CA | 1498 |
| 37 | Bengaluru International Airport |  | IN | 1492 |
| 38 | Oslo Gardermoen Airport |  | NO | 1481 |
| 39 | Vancouver International Airport |  | CA | 1470 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1406 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1112 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 980 | 21m | 244 km | 4,126.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 718 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 659 | 1h 6m | 770 km | 8,754.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 655 | 24m | 225 km | 2,541.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 590 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 426 | 44m | 555 km | 4,079.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 424 | 27m | 275 km | 2,009.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 415 | 1h 50m | 1,423 km | 10,184.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 401 | 44m | 241 km | 1,665.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 371 | 24m | 218 km | 1,397.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 360 | 21m | 250 km | 1,555.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 330 | 1h 6m | 706 km | 4,017.8 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 328 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 326 | 26m | 215 km | 1,207.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 326 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 306 | 19m | 144 km | 761.2 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 284 | 1h 50m | 1,304 km | 6,389.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 280 | 42m | 535 km | 2,586.0 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 280 | 28m | 152 km | 731.7 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N570FG |  | Trenton Mercer Airport (KTTN) | Chester County G O Carlson Airport (KMQS) | 2026-09-18 19:06 UTC | 2026-09-18 20:10 UTC | 1h 4m |
| N701NW |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-09-18 18:53 UTC | 2026-09-18 20:09 UTC | 1h 16m |
| N616BP |  | Rowland Dusters Airport (75XS) | Laredo International Airport (KLRD) | 2026-09-18 19:14 UTC | 2026-09-18 20:02 UTC | 47m |
| TWY281 | TWY | Camarillo Airport (KCMA) | Moffett Federal Airfield (KNUQ) | 2026-09-18 19:13 UTC | 2026-09-18 20:01 UTC | 48m |
| SCU1 | SCU | 2OL2 (2OL2) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-09-18 19:44 UTC | 2026-09-18 20:00 UTC | 15m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-09-18 08:47 UTC | 2026-09-18 19:58 UTC | 11h 11m |
| SCU18 | SCU | Tulsa Riverside Airport (KRVS) | Tulsa Riverside Airport (KRVS) | 2026-09-18 19:29 UTC | 2026-09-18 19:58 UTC | 29m |
| VIR358 | Virgin Atlantic | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-18 11:43 UTC | 2026-09-18 19:55 UTC | 8h 12m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-09-18 19:21 UTC | 2026-09-18 19:52 UTC | 30m |
| N622TP |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-09-18 19:27 UTC | 2026-09-18 19:51 UTC | 24m |
| CCDBA | CCD | Municipal de Vitacura Airport (SCLC) | Eulogio Sanchez Airport (SCTB) | 2026-09-18 19:38 UTC | 2026-09-18 19:47 UTC | 8m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-09-18 19:25 UTC | 2026-09-18 19:46 UTC | 21m |
| N514RB |  | Holk Field At Foley Municipal Airport (K5R4) | Oreck Airport (MS88) | 2026-09-18 18:49 UTC | 2026-09-18 19:46 UTC | 56m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-09-18 19:07 UTC | 2026-09-18 19:45 UTC | 38m |
| N353BG |  | Wood County Regional Airport (K1G0) | Wood County Regional Airport (K1G0) | 2026-09-18 18:51 UTC | 2026-09-18 19:44 UTC | 52m |
| N13CV |  | Northern Colorado Regional Airport (KFNL) | Granby-Grand County Airport (KGNB) | 2026-09-18 18:26 UTC | 2026-09-18 19:44 UTC | 1h 17m |
| N484BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-09-18 18:30 UTC | 2026-09-18 19:43 UTC | 1h 13m |
| AAL3103 | American Airlines | Fort Lauderdale/Hollywood International Airport (KFLL) | Charlotte/Douglas International Airport (KCLT) | 2026-09-18 18:07 UTC | 2026-09-18 19:43 UTC | 1h 35m |
| CFKLQ | CFK | Lourdes-De-Joliette Airport (CSE3) | Montréal (Mirabel) Airport (CYMX) | 2026-09-18 19:09 UTC | 2026-09-18 19:39 UTC | 30m |
| JSX9001 | JSX | John Wayne/Orange County Airport (KSNA) | Floyd Ranch Airport (TA56) | 2026-09-18 17:42 UTC | 2026-09-18 19:25 UTC | 1h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
