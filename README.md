# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_11:17:36_UTC-green)

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

**Latest saved flight:** 2026-08-26 11:17:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 11:17:36 UTC

- **238,201** saved flights
- **72,530** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **238,201** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,870,768.4 tonnes** estimated CO2 emissions
- **166,421,354 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9554 |
| 2 | SkyWest Airlines | 8391 |
| 3 | EJA | 4617 |
| 4 | IndiGo | 4016 |
| 5 | American Airlines | 3855 |
| 6 | Southwest Airlines | 3613 |
| 7 | Delta Air Lines | 3034 |
| 8 | ENY | 2881 |
| 9 | LATAM Airlines | 2285 |
| 10 | AZU | 2217 |
| 11 | Vueling | 2044 |
| 12 | Lufthansa | 1928 |
| 13 | WIF | 1891 |
| 14 | LXJ | 1852 |
| 15 | easyJet | 1661 |
| 16 | Swiss International | 1604 |
| 17 | AXM | 1590 |
| 18 | EJU | 1528 |
| 19 | QLK | 1527 |
| 20 | United Airlines | 1505 |
| 21 | Alaska Airlines | 1430 |
| 22 | All Nippon Airways | 1420 |
| 23 | WMT | 1333 |
| 24 | GLO | 1330 |
| 25 | VIV | 1312 |
| 26 | PGT | 1299 |
| 27 | Air France | 1298 |
| 28 | Wizz Air | 1274 |
| 29 | AEE | 1182 |
| 30 | JetBlue | 1180 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 197454 |
| 2 | 🇪🇸 ES | 15311 |
| 3 | 🇧🇷 BR | 13893 |
| 4 | 🇦🇺 AU | 13565 |
| 5 | 🇨🇦 CA | 13181 |
| 6 | 🇮🇹 IT | 13016 |
| 7 | 🇮🇳 IN | 12520 |
| 8 | 🇩🇪 DE | 11760 |
| 9 | 🇬🇧 GB | 11247 |
| 10 | 🇨🇴 CO | 10127 |
| 11 | 🇯🇵 JP | 9646 |
| 12 | 🇫🇷 FR | 9575 |
| 13 | 🇹🇷 TR | 7079 |
| 14 | 🇬🇷 GR | 7019 |
| 15 | 🇲🇽 MX | 6603 |
| 16 | 🇨🇭 CH | 6382 |
| 17 | 🇳🇴 NO | 5895 |
| 18 | 🇹🇭 TH | 4308 |
| 19 | 🇲🇾 MY | 4259 |
| 20 | 🇿🇦 ZA | 4177 |
| 21 | 🇵🇱 PL | 3958 |
| 22 | 🇳🇿 NZ | 3291 |
| 23 | 🇵🇭 PH | 3289 |
| 24 | 🇬🇹 GT | 2978 |
| 25 | 🇰🇷 KR | 2831 |
| 26 | 🇭🇷 HR | 2751 |
| 27 | 🇲🇦 MA | 2405 |
| 28 | 🇲🇪 ME | 2221 |
| 29 | 🇳🇱 NL | 2147 |
| 30 | 🇮🇩 ID | 2098 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4936 |
| 2 | Denver International Airport |  | US | 3851 |
| 3 | Indira Gandhi International Airport |  | IN | 2913 |
| 4 | Tokyo International Airport |  | JP | 2872 |
| 5 | Guaymaral Airport |  | CO | 2689 |
| 6 | Harry Reid International Airport |  | US | 2538 |
| 7 | Zurich Airport |  | CH | 2501 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2436 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2381 |
| 10 | El Dorado International Airport |  | CO | 2279 |
| 11 | La Aurora Airport |  | GT | 2269 |
| 12 | Chicago O'Hare International Airport |  | US | 2131 |
| 13 | Salt Lake City International Airport |  | US | 2095 |
| 14 | Congonhas Airport |  | BR | 2026 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1987 |
| 16 | Frankfurt am Main International Airport |  | DE | 1888 |
| 17 | Capua Airport |  | IT | 1875 |
| 18 | Madrid Barajas International Airport |  | ES | 1871 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1794 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1752 |
| 21 | Malpensa International Airport |  | IT | 1710 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1683 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1680 |
| 24 | Charles de Gaulle International Airport |  | FR | 1661 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1594 |
| 27 | Kuala Lumpur International Airport |  | MY | 1540 |
| 28 | Charlotte/Douglas International Airport |  | US | 1529 |
| 29 | Barcelona International Airport |  | ES | 1512 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1492 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1442 |
| 32 | Viracopos International Airport |  | BR | 1419 |
| 33 | Bengaluru International Airport |  | IN | 1394 |
| 34 | Don Mueang International Airport |  | TH | 1392 |
| 35 | Seattle-Tacoma International Airport |  | US | 1392 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1390 |
| 37 | Calgary International Airport |  | CA | 1367 |
| 38 | Oslo Gardermoen Airport |  | NO | 1338 |
| 39 | Vancouver International Airport |  | CA | 1303 |
| 40 | O. R. Tambo International Airport |  | ZA | 1299 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1089 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 876 | 21m | 244 km | 3,688.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 609 | 24m | 225 km | 2,362.6 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 606 | 1h 6m | 770 km | 8,050.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 604 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 532 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 393 | 27m | 275 km | 1,862.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 371 | 1h 50m | 1,423 km | 9,104.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 364 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 357 | 44m | 555 km | 3,418.4 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 344 | 44m | 241 km | 1,428.9 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 338 | 21m | 250 km | 1,460.0 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 321 | 24m | 218 km | 1,209.3 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 318 | 22m | 55 km | 302.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 317 | 1h 40m | 1,156 km | 6,324.0 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 296 | 19m | 99 km | 507.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 292 | 27m | 215 km | 1,081.4 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 277 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 269 | 19m | 144 km | 669.1 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 255 | 1h 50m | 1,304 km | 5,736.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 247 | 28m | 152 km | 645.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N280FG |  | Trenton Mercer Airport (KTTN) | Northeast Philadelphia Airport (KPNE) | 2026-08-26 10:37 UTC | 2026-08-26 11:17 UTC | 39m |
| PLF110 | PLF | Václav Havel Airport (LKPR) | Vilnius International Airport (EYVI) | 2026-08-26 09:51 UTC | 2026-08-26 11:14 UTC | 1h 23m |
| JAL3338 | Japan Airlines | Amakusa Airport (RJDA) | Tsushima Airport (RJDT) | 2026-08-26 10:30 UTC | 2026-08-26 11:12 UTC | 41m |
| CHH718 | CHH | Charles de Gaulle International Airport (LFPG) | Luoding Sulong Airport. (ZGLD) | 2026-08-25 10:34 UTC | 2026-08-26 11:12 UTC | 24h 37m |
| TMN1 | TMN | Auckland International Airport (NZAA) | Sydney Kingsford Smith International Airport (YSSY) | 2026-08-26 08:11 UTC | 2026-08-26 11:07 UTC | 2h 56m |
| HBLVC | HBL | Memmingen Allgau Airport (EDJA) | Friedrichshafen Airport (EDNY) | 2026-08-26 10:37 UTC | 2026-08-26 11:06 UTC | 29m |
| ANA267 | All Nippon Airways | Tokyo International Airport (RJTT) | Ozuki Airport (RJOZ) | 2026-08-26 09:46 UTC | 2026-08-26 11:02 UTC | 1h 15m |
| BB52 |  | Karup Airport (EKKA) | Karup Airport (EKKA) | 2026-08-26 09:54 UTC | 2026-08-26 10:55 UTC | 1h 0m |
| UFX61 | UFX | Blackpool International Airport (EGNH) | RAF Woodvale (EGOW) | 2026-08-26 10:39 UTC | 2026-08-26 10:50 UTC | 11m |
| OKC942 | OKC | Wiley Post Airport (KPWA) | Stevens Field (KPSO) | 2026-08-26 09:38 UTC | 2026-08-26 10:50 UTC | 1h 11m |
| UAE67V | Emirates | Dubai International Airport (OMDB) | Vienna International Airport (LOWW) | 2026-08-26 05:35 UTC | 2026-08-26 10:46 UTC | 5h 10m |
| EWG9 | EWG | Dresden Airport (EDDC) | Dresden Airport (EDDC) | 2026-08-26 10:04 UTC | 2026-08-26 10:45 UTC | 41m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-08-25 20:23 UTC | 2026-08-26 10:45 UTC | 14h 21m |
| SPTIR | SPT | Babice Airport (EPBC) | Babice Airport (EPBC) | 2026-08-26 09:00 UTC | 2026-08-26 10:45 UTC | 1h 44m |
| N2893E |  | Reno/Tahoe International Airport (KRNO) | Fallon Municipal Airport (KFLX) | 2026-08-26 09:51 UTC | 2026-08-26 10:44 UTC | 53m |
| RYR32FV | Ryanair | Sevilla Airport (LEZL) | Turweston Airport (EGBT) | 2026-08-26 08:36 UTC | 2026-08-26 10:44 UTC | 2h 8m |
| QAF5 | QAF | Lyon Saint-Exupery Airport (LFLL) | Lyon Saint-Exupery Airport (LFLL) | 2026-08-26 10:30 UTC | 2026-08-26 10:41 UTC | 11m |
| BPO603 | BPO | Uelzen Airport (EDVU) | Uelzen Airport (EDVU) | 2026-08-26 10:34 UTC | 2026-08-26 10:38 UTC | 4m |
| N253EA |  | AZ00 (AZ00) | Glendale Regional Airport (KGEU) | 2026-08-26 09:15 UTC | 2026-08-26 10:37 UTC | 1h 22m |
| RYR3RK | Ryanair | Berlin Brandenburg Airport (EDDB) | Manchester Airport (EGCC) | 2026-08-26 08:52 UTC | 2026-08-26 10:35 UTC | 1h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
