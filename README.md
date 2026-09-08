# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_18:22:25_UTC-green)

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

**Latest saved flight:** 2026-09-08 18:22:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-08 18:22:25 UTC

- **251,778** saved flights
- **75,477** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **251,778** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,031,785.3 tonnes** estimated CO2 emissions
- **175,755,670 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10068 |
| 2 | SkyWest Airlines | 8793 |
| 3 | EJA | 4868 |
| 4 | IndiGo | 4218 |
| 5 | American Airlines | 4020 |
| 6 | Southwest Airlines | 3728 |
| 7 | Delta Air Lines | 3184 |
| 8 | ENY | 3006 |
| 9 | LATAM Airlines | 2423 |
| 10 | AZU | 2337 |
| 11 | Vueling | 2144 |
| 12 | WIF | 2018 |
| 13 | Lufthansa | 1991 |
| 14 | LXJ | 1965 |
| 15 | easyJet | 1730 |
| 16 | Swiss International | 1693 |
| 17 | AXM | 1629 |
| 18 | QLK | 1619 |
| 19 | EJU | 1615 |
| 20 | United Airlines | 1571 |
| 21 | Alaska Airlines | 1502 |
| 22 | All Nippon Airways | 1474 |
| 23 | WMT | 1429 |
| 24 | GLO | 1397 |
| 25 | PGT | 1382 |
| 26 | VIV | 1379 |
| 27 | Air France | 1376 |
| 28 | Wizz Air | 1373 |
| 29 | JetBlue | 1233 |
| 30 | AEE | 1231 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 208849 |
| 2 | 🇪🇸 ES | 16082 |
| 3 | 🇧🇷 BR | 14672 |
| 4 | 🇦🇺 AU | 14315 |
| 5 | 🇨🇦 CA | 13969 |
| 6 | 🇮🇹 IT | 13780 |
| 7 | 🇮🇳 IN | 13177 |
| 8 | 🇩🇪 DE | 12362 |
| 9 | 🇬🇧 GB | 11795 |
| 10 | 🇨🇴 CO | 11096 |
| 11 | 🇫🇷 FR | 10134 |
| 12 | 🇯🇵 JP | 9906 |
| 13 | 🇹🇷 TR | 7534 |
| 14 | 🇬🇷 GR | 7391 |
| 15 | 🇲🇽 MX | 6948 |
| 16 | 🇨🇭 CH | 6795 |
| 17 | 🇳🇴 NO | 6237 |
| 18 | 🇹🇭 TH | 4537 |
| 19 | 🇲🇾 MY | 4379 |
| 20 | 🇿🇦 ZA | 4321 |
| 21 | 🇵🇱 PL | 4198 |
| 22 | 🇳🇿 NZ | 3432 |
| 23 | 🇵🇭 PH | 3412 |
| 24 | 🇬🇹 GT | 3140 |
| 25 | 🇰🇷 KR | 2908 |
| 26 | 🇭🇷 HR | 2895 |
| 27 | 🇲🇦 MA | 2545 |
| 28 | 🇲🇪 ME | 2370 |
| 29 | 🇳🇱 NL | 2270 |
| 30 | 🇮🇩 ID | 2153 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5196 |
| 2 | Denver International Airport |  | US | 4074 |
| 3 | Indira Gandhi International Airport |  | IN | 3061 |
| 4 | Tokyo International Airport |  | JP | 2955 |
| 5 | Guaymaral Airport |  | CO | 2743 |
| 6 | Harry Reid International Airport |  | US | 2674 |
| 7 | Zurich Airport |  | CH | 2638 |
| 8 | El Dorado International Airport |  | CO | 2557 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2552 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2487 |
| 11 | La Aurora Airport |  | GT | 2395 |
| 12 | Salt Lake City International Airport |  | US | 2226 |
| 13 | Chicago O'Hare International Airport |  | US | 2194 |
| 14 | Congonhas Airport |  | BR | 2152 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2071 |
| 16 | Capua Airport |  | IT | 1986 |
| 17 | Madrid Barajas International Airport |  | ES | 1979 |
| 18 | Frankfurt am Main International Airport |  | DE | 1960 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1885 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1831 |
| 21 | Malpensa International Airport |  | IT | 1810 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1768 |
| 23 | Charles de Gaulle International Airport |  | FR | 1767 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1752 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1671 |
| 26 | Ninoy Aquino International Airport |  | PH | 1666 |
| 27 | Macau International Airport |  | MO | 1652 |
| 28 | Barcelona International Airport |  | ES | 1589 |
| 29 | Charlotte/Douglas International Airport |  | US | 1588 |
| 30 | Kuala Lumpur International Airport |  | MY | 1577 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1545 |
| 32 | Viracopos International Airport |  | BR | 1501 |
| 33 | Seattle-Tacoma International Airport |  | US | 1484 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1461 |
| 35 | Don Mueang International Airport |  | TH | 1453 |
| 36 | Calgary International Airport |  | CA | 1447 |
| 37 | Bengaluru International Airport |  | IN | 1438 |
| 38 | Oslo Gardermoen Airport |  | NO | 1419 |
| 39 | Vancouver International Airport |  | CA | 1406 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1362 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 935 | 21m | 244 km | 3,937.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 669 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 635 | 24m | 225 km | 2,463.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 632 | 1h 6m | 770 km | 8,395.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 565 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 414 | 27m | 275 km | 1,961.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 402 | 1h 50m | 1,423 km | 9,865.7 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 396 | 44m | 555 km | 3,791.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 375 | 44m | 241 km | 1,557.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 353 | 21m | 250 km | 1,524.7 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 350 | 24m | 218 km | 1,318.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 336 | 23m | 55 km | 319.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 311 | 26m | 215 km | 1,151.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 294 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 272 | 1h 50m | 1,304 km | 6,119.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 261 | 41m | 535 km | 2,410.5 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N40993 |  | General Dick Stout Field (K1L8) | Colorado City Municipal Airport (KAZC) | 2026-09-08 17:46 UTC | 2026-09-08 18:22 UTC | 36m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-09-08 16:00 UTC | 2026-09-08 18:21 UTC | 2h 21m |
| N650GP |  | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-09-08 18:05 UTC | 2026-09-08 18:18 UTC | 12m |
| N945RF |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-09-08 17:17 UTC | 2026-09-08 18:17 UTC | 59m |
| N4427R |  | Charles M Schulz/Sonoma County Airport (KSTS) | Charles M Schulz/Sonoma County Airport (KSTS) | 2026-09-08 18:02 UTC | 2026-09-08 18:16 UTC | 14m |
| EIX35M | EIX | London Biggin Hill Airport (EGKB) | Gloucestershire Airport (EGBJ) | 2026-09-08 17:43 UTC | 2026-09-08 18:14 UTC | 31m |
| CXK596 | CXK | Stinson Municipal Airport (KSSF) | Gillespie County Airport (KT82) | 2026-09-08 17:35 UTC | 2026-09-08 18:13 UTC | 37m |
| SWA1584 | Southwest Airlines | Fort Lauderdale/Hollywood International Airport (KFLL) | Powhatan Airport (VA57) | 2026-09-08 16:01 UTC | 2026-09-08 18:11 UTC | 2h 9m |
| N8843X |  | Silver Springs Airport (KSPZ) | Silver Springs Airport (KSPZ) | 2026-09-08 17:45 UTC | 2026-09-08 18:07 UTC | 21m |
| VAR969 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-09-08 16:32 UTC | 2026-09-08 18:06 UTC | 1h 34m |
| MSR754 | EgyptAir | Madrid Barajas International Airport (LEMD) | HE42 (HE42) | 2026-09-08 14:13 UTC | 2026-09-08 18:04 UTC | 3h 51m |
| R08848 |  | Gray Army Air Field (Joint Base Lewis-Mcchord) Airport (KGRF) | KZ10 (KZ10) | 2026-09-08 17:59 UTC | 2026-09-08 18:04 UTC | 4m |
| AER101 | AER | PAFV (PAFV) | Fairbanks International Airport (PAFA) | 2026-09-08 17:41 UTC | 2026-09-08 18:02 UTC | 21m |
| ES805 |  | Ranchaero Airport (CL56) | Mc Clellan Airfield (KMCC) | 2026-09-08 17:12 UTC | 2026-09-08 18:02 UTC | 50m |
| N222DQ |  | Reno/Tahoe International Airport (KRNO) | Yerington Municipal Airport (KO43) | 2026-09-08 17:42 UTC | 2026-09-08 18:01 UTC | 19m |
| CO77 |  | Pirassununga Airport (SDPY) | Campo Fontenelle Airport (SBYS) | 2026-09-08 17:54 UTC | 2026-09-08 18:00 UTC | 6m |
| N464FA |  | Allentown Queen City Municipal Airport (KXLL) | Capital City Airport (KCXY) | 2026-09-08 17:18 UTC | 2026-09-08 18:00 UTC | 42m |
| N708LA |  | Northeast Philadelphia Airport (KPNE) | Lancaster Airport (KLNS) | 2026-09-08 17:15 UTC | 2026-09-08 18:00 UTC | 44m |
| CHX77 | CHX | Langenlonsheim Airport (EDEL) | Wiesbaden Army Airfield (ETOU) | 2026-09-08 17:51 UTC | 2026-09-08 17:58 UTC | 7m |
| N105UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-09-08 16:54 UTC | 2026-09-08 17:57 UTC | 1h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
