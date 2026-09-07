# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_22:44:28_UTC-green)

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

**Latest saved flight:** 2026-09-07 22:44:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-07 22:44:28 UTC

- **251,047** saved flights
- **75,338** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **251,047** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,022,560.4 tonnes** estimated CO2 emissions
- **175,220,890 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10049 |
| 2 | SkyWest Airlines | 8777 |
| 3 | EJA | 4854 |
| 4 | IndiGo | 4197 |
| 5 | American Airlines | 4017 |
| 6 | Southwest Airlines | 3721 |
| 7 | Delta Air Lines | 3180 |
| 8 | ENY | 3000 |
| 9 | LATAM Airlines | 2418 |
| 10 | AZU | 2333 |
| 11 | Vueling | 2142 |
| 12 | WIF | 2011 |
| 13 | Lufthansa | 1987 |
| 14 | LXJ | 1959 |
| 15 | easyJet | 1728 |
| 16 | Swiss International | 1686 |
| 17 | AXM | 1628 |
| 18 | EJU | 1613 |
| 19 | QLK | 1610 |
| 20 | United Airlines | 1570 |
| 21 | Alaska Airlines | 1500 |
| 22 | All Nippon Airways | 1469 |
| 23 | WMT | 1423 |
| 24 | GLO | 1394 |
| 25 | PGT | 1377 |
| 26 | VIV | 1373 |
| 27 | Wizz Air | 1366 |
| 28 | Air France | 1365 |
| 29 | AEE | 1230 |
| 30 | JetBlue | 1229 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 208308 |
| 2 | 🇪🇸 ES | 16053 |
| 3 | 🇧🇷 BR | 14635 |
| 4 | 🇦🇺 AU | 14244 |
| 5 | 🇨🇦 CA | 13933 |
| 6 | 🇮🇹 IT | 13753 |
| 7 | 🇮🇳 IN | 13101 |
| 8 | 🇩🇪 DE | 12329 |
| 9 | 🇬🇧 GB | 11769 |
| 10 | 🇨🇴 CO | 11053 |
| 11 | 🇫🇷 FR | 10105 |
| 12 | 🇯🇵 JP | 9878 |
| 13 | 🇹🇷 TR | 7502 |
| 14 | 🇬🇷 GR | 7377 |
| 15 | 🇲🇽 MX | 6929 |
| 16 | 🇨🇭 CH | 6764 |
| 17 | 🇳🇴 NO | 6218 |
| 18 | 🇹🇭 TH | 4512 |
| 19 | 🇲🇾 MY | 4371 |
| 20 | 🇿🇦 ZA | 4313 |
| 21 | 🇵🇱 PL | 4191 |
| 22 | 🇳🇿 NZ | 3423 |
| 23 | 🇵🇭 PH | 3408 |
| 24 | 🇬🇹 GT | 3135 |
| 25 | 🇰🇷 KR | 2902 |
| 26 | 🇭🇷 HR | 2885 |
| 27 | 🇲🇦 MA | 2537 |
| 28 | 🇲🇪 ME | 2362 |
| 29 | 🇳🇱 NL | 2267 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5188 |
| 2 | Denver International Airport |  | US | 4067 |
| 3 | Indira Gandhi International Airport |  | IN | 3053 |
| 4 | Tokyo International Airport |  | JP | 2949 |
| 5 | Guaymaral Airport |  | CO | 2739 |
| 6 | Harry Reid International Airport |  | US | 2671 |
| 7 | Zurich Airport |  | CH | 2628 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2550 |
| 9 | El Dorado International Airport |  | CO | 2548 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2483 |
| 11 | La Aurora Airport |  | GT | 2390 |
| 12 | Salt Lake City International Airport |  | US | 2219 |
| 13 | Chicago O'Hare International Airport |  | US | 2191 |
| 14 | Congonhas Airport |  | BR | 2148 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2068 |
| 16 | Capua Airport |  | IT | 1982 |
| 17 | Madrid Barajas International Airport |  | ES | 1976 |
| 18 | Frankfurt am Main International Airport |  | DE | 1957 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1882 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1828 |
| 21 | Malpensa International Airport |  | IT | 1804 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1759 |
| 23 | Charles de Gaulle International Airport |  | FR | 1757 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1748 |
| 25 | Ninoy Aquino International Airport |  | PH | 1663 |
| 26 | Enrique Olaya Herrera Airport |  | CO | 1659 |
| 27 | Macau International Airport |  | MO | 1651 |
| 28 | Barcelona International Airport |  | ES | 1587 |
| 29 | Charlotte/Douglas International Airport |  | US | 1586 |
| 30 | Kuala Lumpur International Airport |  | MY | 1574 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1537 |
| 32 | Viracopos International Airport |  | BR | 1500 |
| 33 | Seattle-Tacoma International Airport |  | US | 1484 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1459 |
| 35 | Don Mueang International Airport |  | TH | 1446 |
| 36 | Calgary International Airport |  | CA | 1444 |
| 37 | Bengaluru International Airport |  | IN | 1434 |
| 38 | Oslo Gardermoen Airport |  | NO | 1414 |
| 39 | Vancouver International Airport |  | CA | 1401 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1361 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 932 | 21m | 244 km | 3,924.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 665 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 635 | 24m | 225 km | 2,463.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 630 | 1h 6m | 770 km | 8,369.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 563 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 412 | 27m | 275 km | 1,952.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 400 | 1h 50m | 1,423 km | 9,816.6 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 391 | 44m | 555 km | 3,744.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 374 | 44m | 241 km | 1,553.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 352 | 21m | 250 km | 1,520.4 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 349 | 24m | 218 km | 1,314.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 335 | 23m | 55 km | 318.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 310 | 26m | 215 km | 1,148.1 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 291 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 271 | 1h 50m | 1,304 km | 6,096.8 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 257 | 41m | 535 km | 2,373.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6605P |  | Portland-Hillsboro Airport (KHIO) | Venell Airport (OR52) | 2026-09-07 21:55 UTC | 2026-09-07 22:44 UTC | 49m |
| IGO1402 | IndiGo | Abu Dhabi International Airport (OMAA) | Pune Airport (VAPO) | 2026-09-07 20:09 UTC | 2026-09-07 22:44 UTC | 2h 34m |
| ABY405 | ABY | Sharjah International Airport (OMSJ) | Pune Airport (VAPO) | 2026-09-07 20:04 UTC | 2026-09-07 22:41 UTC | 2h 36m |
| FTO382 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-09-07 22:06 UTC | 2026-09-07 22:37 UTC | 30m |
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-09-07 22:15 UTC | 2026-09-07 22:37 UTC | 22m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-09-07 12:08 UTC | 2026-09-07 22:34 UTC | 10h 26m |
| N81RV |  | Zamperini Field (KTOA) | Bob Maxwell Memorial Airfield (KOKB) | 2026-09-07 22:05 UTC | 2026-09-07 22:34 UTC | 28m |
| N47698 |  | Denali Airport (AK06) | Summit Airport (PAST) | 2026-09-07 22:14 UTC | 2026-09-07 22:31 UTC | 16m |
| XSN90 | XSN | Hermitage Airport (45CN) | San Carlos Airport (KSQL) | 2026-09-07 22:05 UTC | 2026-09-07 22:31 UTC | 25m |
| BCS694 | BCS | Bengaluru International Airport (VOBL) | Zhuhai Airport (ZGSD) | 2026-09-07 17:12 UTC | 2026-09-07 22:30 UTC | 5h 18m |
| N456LB |  | Martin State Airport (KMTN) | Easton/Newnam Field (KESN) | 2026-09-07 21:21 UTC | 2026-09-07 22:29 UTC | 1h 7m |
| FIRE5 | FIR | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-09-07 22:10 UTC | 2026-09-07 22:29 UTC | 19m |
| THY3122 | Turkish Airlines | Milas Bodrum International Airport (LTFE) | Smolensk North Airport (XUBS) | 2026-09-07 19:40 UTC | 2026-09-07 22:29 UTC | 2h 49m |
| N9150M |  | Brown Field Municipal Airport (KSDM) | Brown Field Municipal Airport (KSDM) | 2026-09-07 22:10 UTC | 2026-09-07 22:27 UTC | 17m |
| N41380 |  | Van Nuys Airport (KVNY) | Santa Barbara Municipal Airport (KSBA) | 2026-09-07 21:34 UTC | 2026-09-07 22:27 UTC | 52m |
| DCM3160 | DCM | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-09-07 22:26 UTC | 2026-09-07 22:26 UTC | 0m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-09-07 21:43 UTC | 2026-09-07 22:26 UTC | 43m |
| SIS49 | SIS | Mineta San Jose International Airport (KSJC) | Meadows Field (KBFL) | 2026-09-07 21:50 UTC | 2026-09-07 22:26 UTC | 35m |
| N2B |  | Bremerton Ntl Airport (KPWT) | 1WA9 (1WA9) | 2026-09-07 21:25 UTC | 2026-09-07 22:23 UTC | 57m |
| IGO018 | IndiGo | Istanbul Airport (LTFM) | Pune Airport (VAPO) | 2026-09-07 15:11 UTC | 2026-09-07 22:21 UTC | 7h 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
