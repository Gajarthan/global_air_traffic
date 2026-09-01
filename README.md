# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_08:24:11_UTC-green)

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

**Latest saved flight:** 2026-09-01 08:24:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-01 08:24:11 UTC

- **243,367** saved flights
- **73,733** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **243,367** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,931,433.4 tonnes** estimated CO2 emissions
- **169,938,166 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9774 |
| 2 | SkyWest Airlines | 8529 |
| 3 | EJA | 4703 |
| 4 | IndiGo | 4090 |
| 5 | American Airlines | 3918 |
| 6 | Southwest Airlines | 3656 |
| 7 | Delta Air Lines | 3102 |
| 8 | ENY | 2931 |
| 9 | LATAM Airlines | 2333 |
| 10 | AZU | 2263 |
| 11 | Vueling | 2085 |
| 12 | Lufthansa | 1954 |
| 13 | WIF | 1933 |
| 14 | LXJ | 1883 |
| 15 | easyJet | 1696 |
| 16 | Swiss International | 1641 |
| 17 | AXM | 1606 |
| 18 | EJU | 1565 |
| 19 | QLK | 1556 |
| 20 | United Airlines | 1531 |
| 21 | Alaska Airlines | 1455 |
| 22 | All Nippon Airways | 1438 |
| 23 | WMT | 1369 |
| 24 | GLO | 1361 |
| 25 | VIV | 1333 |
| 26 | PGT | 1331 |
| 27 | Air France | 1327 |
| 28 | Wizz Air | 1319 |
| 29 | JetBlue | 1204 |
| 30 | AEE | 1202 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 201594 |
| 2 | 🇪🇸 ES | 15646 |
| 3 | 🇧🇷 BR | 14187 |
| 4 | 🇦🇺 AU | 13830 |
| 5 | 🇨🇦 CA | 13546 |
| 6 | 🇮🇹 IT | 13333 |
| 7 | 🇮🇳 IN | 12738 |
| 8 | 🇩🇪 DE | 12004 |
| 9 | 🇬🇧 GB | 11491 |
| 10 | 🇨🇴 CO | 10504 |
| 11 | 🇫🇷 FR | 9813 |
| 12 | 🇯🇵 JP | 9733 |
| 13 | 🇹🇷 TR | 7239 |
| 14 | 🇬🇷 GR | 7177 |
| 15 | 🇲🇽 MX | 6714 |
| 16 | 🇨🇭 CH | 6550 |
| 17 | 🇳🇴 NO | 6016 |
| 18 | 🇹🇭 TH | 4400 |
| 19 | 🇲🇾 MY | 4307 |
| 20 | 🇿🇦 ZA | 4239 |
| 21 | 🇵🇱 PL | 4095 |
| 22 | 🇳🇿 NZ | 3345 |
| 23 | 🇵🇭 PH | 3338 |
| 24 | 🇬🇹 GT | 3060 |
| 25 | 🇰🇷 KR | 2864 |
| 26 | 🇭🇷 HR | 2806 |
| 27 | 🇲🇦 MA | 2464 |
| 28 | 🇲🇪 ME | 2272 |
| 29 | 🇳🇱 NL | 2201 |
| 30 | 🇮🇩 ID | 2123 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5020 |
| 2 | Denver International Airport |  | US | 3918 |
| 3 | Indira Gandhi International Airport |  | IN | 2969 |
| 4 | Tokyo International Airport |  | JP | 2899 |
| 5 | Guaymaral Airport |  | CO | 2707 |
| 6 | Harry Reid International Airport |  | US | 2589 |
| 7 | Zurich Airport |  | CH | 2557 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2485 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2427 |
| 10 | El Dorado International Airport |  | CO | 2385 |
| 11 | La Aurora Airport |  | GT | 2329 |
| 12 | Salt Lake City International Airport |  | US | 2152 |
| 13 | Chicago O'Hare International Airport |  | US | 2151 |
| 14 | Congonhas Airport |  | BR | 2077 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2017 |
| 16 | Frankfurt am Main International Airport |  | DE | 1923 |
| 17 | Capua Airport |  | IT | 1917 |
| 18 | Madrid Barajas International Airport |  | ES | 1915 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1826 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1790 |
| 21 | Malpensa International Airport |  | IT | 1740 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1720 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1707 |
| 24 | Charles de Gaulle International Airport |  | FR | 1705 |
| 25 | Ninoy Aquino International Airport |  | PH | 1624 |
| 26 | Macau International Airport |  | MO | 1624 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1558 |
| 28 | Charlotte/Douglas International Airport |  | US | 1555 |
| 29 | Kuala Lumpur International Airport |  | MY | 1551 |
| 30 | Barcelona International Airport |  | ES | 1545 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1471 |
| 32 | Viracopos International Airport |  | BR | 1445 |
| 33 | Seattle-Tacoma International Airport |  | US | 1425 |
| 34 | Don Mueang International Airport |  | TH | 1418 |
| 35 | Bengaluru International Airport |  | IN | 1412 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1410 |
| 37 | Calgary International Airport |  | CA | 1397 |
| 38 | Oslo Gardermoen Airport |  | NO | 1368 |
| 39 | Vancouver International Airport |  | CA | 1354 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1330 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1097 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 897 | 21m | 244 km | 3,777.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 628 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 621 | 24m | 225 km | 2,409.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 615 | 1h 6m | 770 km | 8,169.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 548 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 400 | 27m | 275 km | 1,895.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 384 | 1h 50m | 1,423 km | 9,424.0 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 372 | 44m | 555 km | 3,562.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 356 | 44m | 241 km | 1,478.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 347 | 21m | 250 km | 1,498.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 334 | 24m | 218 km | 1,258.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 324 | 1h 39m | 1,156 km | 6,463.7 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 322 | 22m | 55 km | 306.1 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 302 | 19m | 99 km | 517.3 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 296 | 26m | 215 km | 1,096.3 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 287 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 282 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 279 | 1h 14m | 961 km | 4,624.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 275 | 19m | 144 km | 684.0 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 265 | 15m | 154 km | 702.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 262 | 1h 50m | 1,304 km | 5,894.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| THY70 | Turkish Airlines | Istanbul Hezarfen Airfield (LTBW) | Zhuhai Airport (ZGSD) | 2026-08-31 23:06 UTC | 2026-09-01 08:24 UTC | 9h 18m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-09-01 07:39 UTC | 2026-09-01 08:21 UTC | 41m |
| CAN12 | CAN | Pescara International Airport (LIBP) | Pescara International Airport (LIBP) | 2026-09-01 07:39 UTC | 2026-09-01 08:12 UTC | 33m |
| CMA560 | CMA | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-08-31 21:09 UTC | 2026-09-01 08:01 UTC | 10h 52m |
| R20571 |  | Lakloey Air Park (AK22) | Lakloey Air Park (AK22) | 2026-09-01 06:43 UTC | 2026-09-01 08:00 UTC | 1h 16m |
| N232LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | 2026-09-01 06:16 UTC | 2026-09-01 07:55 UTC | 1h 39m |
| N8EU |  | Cannes-Mandelieu Airport (LFMD) | Nice-Cote d'Azur Airport (LFMN) | 2026-09-01 07:42 UTC | 2026-09-01 07:54 UTC | 12m |
| ASL4010 | ASL | Belgrade Nikola Tesla Airport (LYBE) | Belgrade Nikola Tesla Airport (LYBE) | 2026-09-01 07:21 UTC | 2026-09-01 07:52 UTC | 31m |
| TRA78V | TRA | Amsterdam Airport Schiphol (EHAM) | Chania International Airport (LGSA) | 2026-09-01 05:02 UTC | 2026-09-01 07:51 UTC | 2h 48m |
| ZSHIB | ZSH | O. R. Tambo International Airport (FAOR) | O. R. Tambo International Airport (FAOR) | 2026-09-01 07:30 UTC | 2026-09-01 07:50 UTC | 19m |
| SUNDOG1 | SUN | Nordholz Airport (ETMN) | Diepholz Airport (ETND) | 2026-09-01 07:34 UTC | 2026-09-01 07:47 UTC | 12m |
| EJU36XM | EJU | Faro Airport (LPFR) | Annecy-Haute-Savoie-Mont Blanc Airport (LFLP) | 2026-09-01 05:22 UTC | 2026-09-01 07:44 UTC | 2h 21m |
| UPS2 | UPS | Cologne Bonn Airport (EDDK) | Zhuhai Airport (ZGSD) | 2026-08-31 21:13 UTC | 2026-09-01 07:42 UTC | 10h 29m |
| SWR138 | Swiss International | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-08-31 20:53 UTC | 2026-09-01 07:39 UTC | 10h 46m |
| AFR38SN | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-09-01 06:54 UTC | 2026-09-01 07:39 UTC | 44m |
| WIF1DK | WIF | Sogndal Airport (ENSG) | Bringeland Airport (ENBL) | 2026-09-01 07:02 UTC | 2026-09-01 07:38 UTC | 35m |
| FFT2045 | FFT | Harry Reid International Airport (KLAS) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-01 06:23 UTC | 2026-09-01 07:38 UTC | 1h 15m |
| AEE4SR | AEE | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-09-01 07:17 UTC | 2026-09-01 07:36 UTC | 19m |
| GTI9476 | GTI | Madrid Barajas International Airport (LEMD) | Macau International Airport (VMMC) | 2026-08-31 19:53 UTC | 2026-09-01 07:35 UTC | 11h 41m |
| FHULC | FHU | L'alpe D'huez Airport (LFHU) | L'alpe D'huez Airport (LFHU) | 2026-09-01 07:15 UTC | 2026-09-01 07:32 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
