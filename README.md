# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_15:06:18_UTC-green)

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

**Latest saved flight:** 2026-09-27 15:06:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-27 15:06:18 UTC

- **270,939** saved flights
- **79,330** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **270,939** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,285,751.2 tonnes** estimated CO2 emissions
- **190,478,330 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10663 |
| 2 | SkyWest Airlines | 9428 |
| 3 | EJA | 5289 |
| 4 | IndiGo | 4537 |
| 5 | American Airlines | 4209 |
| 6 | Southwest Airlines | 3988 |
| 7 | Delta Air Lines | 3365 |
| 8 | ENY | 3181 |
| 9 | LATAM Airlines | 2605 |
| 10 | AZU | 2541 |
| 11 | Vueling | 2253 |
| 12 | WIF | 2203 |
| 13 | LXJ | 2129 |
| 14 | Lufthansa | 2057 |
| 15 | easyJet | 1813 |
| 16 | Swiss International | 1775 |
| 17 | QLK | 1743 |
| 18 | EJU | 1696 |
| 19 | AXM | 1677 |
| 20 | United Airlines | 1657 |
| 21 | Alaska Airlines | 1599 |
| 22 | All Nippon Airways | 1557 |
| 23 | PGT | 1528 |
| 24 | WMT | 1515 |
| 25 | GLO | 1510 |
| 26 | Air France | 1491 |
| 27 | VIV | 1478 |
| 28 | Wizz Air | 1472 |
| 29 | CXK | 1332 |
| 30 | AEE | 1298 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 225638 |
| 2 | 🇪🇸 ES | 16966 |
| 3 | 🇧🇷 BR | 15848 |
| 4 | 🇦🇺 AU | 15565 |
| 5 | 🇨🇦 CA | 15098 |
| 6 | 🇮🇹 IT | 14650 |
| 7 | 🇮🇳 IN | 14355 |
| 8 | 🇩🇪 DE | 13005 |
| 9 | 🇬🇧 GB | 12535 |
| 10 | 🇨🇴 CO | 12445 |
| 11 | 🇫🇷 FR | 10770 |
| 12 | 🇯🇵 JP | 10401 |
| 13 | 🇹🇷 TR | 8204 |
| 14 | 🇬🇷 GR | 7815 |
| 15 | 🇲🇽 MX | 7475 |
| 16 | 🇨🇭 CH | 7207 |
| 17 | 🇳🇴 NO | 6693 |
| 18 | 🇹🇭 TH | 4847 |
| 19 | 🇲🇾 MY | 4539 |
| 20 | 🇿🇦 ZA | 4522 |
| 21 | 🇵🇱 PL | 4452 |
| 22 | 🇳🇿 NZ | 3800 |
| 23 | 🇵🇭 PH | 3587 |
| 24 | 🇬🇹 GT | 3422 |
| 25 | 🇭🇷 HR | 3091 |
| 26 | 🇰🇷 KR | 3060 |
| 27 | 🇲🇦 MA | 2687 |
| 28 | 🇲🇪 ME | 2544 |
| 29 | 🇳🇱 NL | 2437 |
| 30 | 🇮🇩 ID | 2258 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5512 |
| 2 | Denver International Airport |  | US | 4411 |
| 3 | Indira Gandhi International Airport |  | IN | 3242 |
| 4 | Tokyo International Airport |  | JP | 3113 |
| 5 | El Dorado International Airport |  | CO | 2954 |
| 6 | Harry Reid International Airport |  | US | 2903 |
| 7 | Guaymaral Airport |  | CO | 2821 |
| 8 | Zurich Airport |  | CH | 2809 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2718 |
| 10 | La Aurora Airport |  | GT | 2601 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2601 |
| 12 | Salt Lake City International Airport |  | US | 2392 |
| 13 | Chicago O'Hare International Airport |  | US | 2310 |
| 14 | Congonhas Airport |  | BR | 2309 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2215 |
| 16 | Capua Airport |  | IT | 2094 |
| 17 | Madrid Barajas International Airport |  | ES | 2087 |
| 18 | Frankfurt am Main International Airport |  | DE | 2051 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2047 |
| 20 | Malpensa International Airport |  | IT | 1931 |
| 21 | Charles de Gaulle International Airport |  | FR | 1926 |
| 22 | Hartsfield/Jackson Atlanta International Airport |  | US | 1925 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1906 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1895 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1825 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1761 |
| 28 | Charlotte/Douglas International Airport |  | US | 1696 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1684 |
| 30 | Barcelona International Airport |  | ES | 1683 |
| 31 | Viracopos International Airport |  | BR | 1631 |
| 32 | Kuala Lumpur International Airport |  | MY | 1627 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1587 |
| 34 | Seattle-Tacoma International Airport |  | US | 1587 |
| 35 | Calgary International Airport |  | CA | 1541 |
| 36 | Don Mueang International Airport |  | TH | 1533 |
| 37 | Bengaluru International Airport |  | IN | 1527 |
| 38 | Oslo Gardermoen Airport |  | NO | 1519 |
| 39 | Vancouver International Airport |  | CA | 1514 |
| 40 | Reno/Tahoe International Airport |  | US | 1446 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1123 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1016 | 21m | 244 km | 4,278.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 750 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 683 | 1h 6m | 770 km | 9,073.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 678 | 24m | 225 km | 2,630.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 451 | 44m | 555 km | 4,318.5 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 436 | 27m | 275 km | 2,066.0 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 427 | 1h 50m | 1,423 km | 10,479.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 414 | 44m | 241 km | 1,719.7 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 387 | 24m | 218 km | 1,458.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 378 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 366 | 21m | 250 km | 1,580.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 364 | 23m | 55 km | 346.0 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 346 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 315 | 19m | 144 km | 783.5 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 306 | 1h 14m | 961 km | 5,072.1 t |
| 24 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 300 | 42m | 535 km | 2,770.7 t |
| 25 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 26 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 297 | 18m | 14 km | 74.3 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 291 | 1h 50m | 1,304 km | 6,546.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4321J |  | Newnan Coweta County Airport (KCCO) | Lagrange/Callaway Airport (KLGC) | 2026-09-27 14:30 UTC | 2026-09-27 15:06 UTC | 35m |
| SPMOC | SPM | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-09-27 14:10 UTC | 2026-09-27 15:05 UTC | 55m |
| CFEGU | CFE | CPL6 (CPL6) | Stony Plain (Lichtner Farms) Airport (CSP3) | 2026-09-27 14:47 UTC | 2026-09-27 15:01 UTC | 14m |
| N733NB |  | Majors Airport (KGVT) | Majors Airport (KGVT) | 2026-09-27 14:41 UTC | 2026-09-27 15:00 UTC | 19m |
| N8305B |  | Wright Army Air Field (Fort Stewart)/Midcoast Regional Airport (KLHW) | 9GA2 (9GA2) | 2026-09-27 14:50 UTC | 2026-09-27 15:00 UTC | 10m |
| N87KH |  | Penn Yan/Yates County Airport (KPEO) | Chautauqua County/Dunkirk Airport (KDKK) | 2026-09-27 14:29 UTC | 2026-09-27 14:58 UTC | 29m |
| DHAFZ | DHA | Muhlhausen Airport (EDEQ) | Nuremberg Airport (EDDN) | 2026-09-27 13:44 UTC | 2026-09-27 14:56 UTC | 1h 11m |
| VJT850 | VJT | Nice-Cote d'Azur Airport (LFMN) | London Biggin Hill Airport (EGKB) | 2026-09-27 13:26 UTC | 2026-09-27 14:56 UTC | 1h 29m |
| SVA555 | Saudia | Dubai International Airport (OMDB) | Buhasa Airport (OMAB) | 2026-09-27 14:27 UTC | 2026-09-27 14:53 UTC | 26m |
| N181PG |  | Piedmont Triad International Airport (KGSO) | Lewis Airstrip (7NC7) | 2026-09-27 14:41 UTC | 2026-09-27 14:51 UTC | 9m |
| DFOXI | DFO | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-09-27 14:30 UTC | 2026-09-27 14:45 UTC | 15m |
| N224BW |  | Shelby County Airport (KEET) | Lazy Eight Airpark Llc Airport (AL17) | 2026-09-27 14:41 UTC | 2026-09-27 14:44 UTC | 3m |
| N2078G |  | Double Eagle Ii Airport (KAEG) | Los Alamos Airport (KLAM) | 2026-09-27 14:10 UTC | 2026-09-27 14:38 UTC | 28m |
| N7269T |  | Albuquerque International Sunport Airport (KABQ) | Grants-Milan Municipal Airport (KGNT) | 2026-09-27 13:57 UTC | 2026-09-27 14:38 UTC | 40m |
| N928NG |  | Iowa City Municipal Airport (KIOW) | Spearman Field (4MS4) | 2026-09-27 12:43 UTC | 2026-09-27 14:37 UTC | 1h 53m |
| PPFRG | PPF | Brigadeiro Eduardo Gomes Airport (SWIW) | Cachoeira Rica Airport (SSYO) | 2026-09-27 14:14 UTC | 2026-09-27 14:35 UTC | 21m |
| LNX06AR | LNX | Hawarden Airport (EGNR) | Farnborough Airport (EGLF) | 2026-09-27 13:56 UTC | 2026-09-27 14:35 UTC | 38m |
| XBPBH | XBP | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-09-27 14:12 UTC | 2026-09-27 14:34 UTC | 22m |
| CES202 | China Eastern | London Gatwick Airport (EGKK) | Ukhta Airport (UUYH) | 2026-09-27 10:54 UTC | 2026-09-27 14:32 UTC | 3h 37m |
| N717LK |  | Centennial Airport (KAPA) | Cheyenne Regional/Jerry Olson Field (KCYS) | 2026-09-27 13:53 UTC | 2026-09-27 14:31 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
