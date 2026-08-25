# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_07:37:20_UTC-green)

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

**Latest saved flight:** 2026-08-25 07:37:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 07:37:20 UTC

- **234,398** saved flights
- **71,850** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **234,398** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,823,493.5 tonnes** estimated CO2 emissions
- **163,680,785 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9395 |
| 2 | SkyWest Airlines | 8299 |
| 3 | EJA | 4553 |
| 4 | IndiGo | 3959 |
| 5 | American Airlines | 3815 |
| 6 | Southwest Airlines | 3599 |
| 7 | Delta Air Lines | 2991 |
| 8 | ENY | 2854 |
| 9 | LATAM Airlines | 2252 |
| 10 | AZU | 2184 |
| 11 | Vueling | 2002 |
| 12 | Lufthansa | 1903 |
| 13 | WIF | 1861 |
| 14 | LXJ | 1844 |
| 15 | easyJet | 1632 |
| 16 | Swiss International | 1566 |
| 17 | AXM | 1565 |
| 18 | EJU | 1497 |
| 19 | QLK | 1495 |
| 20 | United Airlines | 1484 |
| 21 | Alaska Airlines | 1417 |
| 22 | All Nippon Airways | 1396 |
| 23 | GLO | 1306 |
| 24 | WMT | 1299 |
| 25 | VIV | 1294 |
| 26 | PGT | 1278 |
| 27 | Air France | 1268 |
| 28 | Wizz Air | 1240 |
| 29 | AEE | 1164 |
| 30 | JetBlue | 1162 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195089 |
| 2 | 🇪🇸 ES | 15031 |
| 3 | 🇧🇷 BR | 13685 |
| 4 | 🇦🇺 AU | 13306 |
| 5 | 🇨🇦 CA | 12977 |
| 6 | 🇮🇹 IT | 12725 |
| 7 | 🇮🇳 IN | 12328 |
| 8 | 🇩🇪 DE | 11529 |
| 9 | 🇬🇧 GB | 11017 |
| 10 | 🇨🇴 CO | 9854 |
| 11 | 🇯🇵 JP | 9509 |
| 12 | 🇫🇷 FR | 9356 |
| 13 | 🇹🇷 TR | 6942 |
| 14 | 🇬🇷 GR | 6887 |
| 15 | 🇲🇽 MX | 6527 |
| 16 | 🇨🇭 CH | 6234 |
| 17 | 🇳🇴 NO | 5779 |
| 18 | 🇲🇾 MY | 4185 |
| 19 | 🇹🇭 TH | 4163 |
| 20 | 🇿🇦 ZA | 4085 |
| 21 | 🇵🇱 PL | 3905 |
| 22 | 🇳🇿 NZ | 3247 |
| 23 | 🇵🇭 PH | 3221 |
| 24 | 🇬🇹 GT | 2935 |
| 25 | 🇰🇷 KR | 2747 |
| 26 | 🇭🇷 HR | 2688 |
| 27 | 🇲🇦 MA | 2373 |
| 28 | 🇲🇪 ME | 2161 |
| 29 | 🇳🇱 NL | 2096 |
| 30 | 🇮🇩 ID | 2043 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4874 |
| 2 | Denver International Airport |  | US | 3799 |
| 3 | Indira Gandhi International Airport |  | IN | 2856 |
| 4 | Tokyo International Airport |  | JP | 2830 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2517 |
| 7 | Zurich Airport |  | CH | 2445 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2396 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2347 |
| 10 | La Aurora Airport |  | GT | 2236 |
| 11 | El Dorado International Airport |  | CO | 2197 |
| 12 | Chicago O'Hare International Airport |  | US | 2117 |
| 13 | Salt Lake City International Airport |  | US | 2069 |
| 14 | Congonhas Airport |  | BR | 1997 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1973 |
| 16 | Frankfurt am Main International Airport |  | DE | 1864 |
| 17 | Capua Airport |  | IT | 1846 |
| 18 | Madrid Barajas International Airport |  | ES | 1840 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1764 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1732 |
| 21 | Malpensa International Airport |  | IT | 1677 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1664 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1624 |
| 25 | Macau International Airport |  | MO | 1607 |
| 26 | Ninoy Aquino International Airport |  | PH | 1555 |
| 27 | Charlotte/Douglas International Airport |  | US | 1515 |
| 28 | Kuala Lumpur International Airport |  | MY | 1515 |
| 29 | Barcelona International Airport |  | ES | 1478 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1443 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1420 |
| 32 | Viracopos International Airport |  | BR | 1396 |
| 33 | Seattle-Tacoma International Airport |  | US | 1378 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1377 |
| 35 | Bengaluru International Airport |  | IN | 1376 |
| 36 | Don Mueang International Airport |  | TH | 1354 |
| 37 | Calgary International Airport |  | CA | 1345 |
| 38 | Oslo Gardermoen Airport |  | NO | 1309 |
| 39 | Vancouver International Airport |  | CA | 1282 |
| 40 | O. R. Tambo International Airport |  | ZA | 1269 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 862 | 21m | 244 km | 3,629.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 592 | 1h 6m | 770 km | 7,864.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 592 | 24m | 225 km | 2,296.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 584 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 523 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 386 | 27m | 275 km | 1,829.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 362 | 1h 50m | 1,423 km | 8,884.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 360 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 340 | 44m | 241 km | 1,412.3 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 336 | 44m | 555 km | 3,217.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 328 | 21m | 250 km | 1,416.8 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 311 | 24m | 218 km | 1,171.7 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 307 | 1h 40m | 1,156 km | 6,124.5 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 290 | 19m | 99 km | 496.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 286 | 27m | 215 km | 1,059.2 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 266 | 19m | 144 km | 661.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 258 | 15m | 154 km | 683.6 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 251 | 1h 50m | 1,304 km | 5,646.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| STNGR81 | STN | RAF Akrotiri (LCRA) | RAF Akrotiri (LCRA) | 2026-08-25 06:54 UTC | 2026-08-25 07:37 UTC | 43m |
| TVF63AB | TVF | Francisco de Sá Carneiro Airport (LPPR) | Paris-Orly Airport (LFPO) | 2026-08-25 05:50 UTC | 2026-08-25 07:33 UTC | 1h 42m |
| YASAT50 | YAS | Abu Dhabi International Airport (OMAA) | Al Minhad Air Base (OMDM) | 2026-08-25 07:07 UTC | 2026-08-25 07:28 UTC | 20m |
| HSOVJ2 | HSO | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-08-25 06:45 UTC | 2026-08-25 07:11 UTC | 26m |
| SUCCE | SUC | El Nouzha Airport (HEAX) | Borg El Arab International Airport (HEBA) | 2026-08-25 06:41 UTC | 2026-08-25 07:01 UTC | 20m |
| N486LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-25 03:58 UTC | 2026-08-25 06:56 UTC | 2h 58m |
| RYR7BV | Ryanair | Palma De Mallorca Airport (LEPA) | Berlin Brandenburg Airport (EDDB) | 2026-08-25 04:46 UTC | 2026-08-25 06:55 UTC | 2h 9m |
| 8AX |  | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-08-25 06:40 UTC | 2026-08-25 06:50 UTC | 10m |
| JJA1393 | JJA | Incheon International Airport (RKSI) | Kansai International Airport (RJBB) | 2026-08-25 05:23 UTC | 2026-08-25 06:48 UTC | 1h 25m |
| RYR3368 | Ryanair | Malaga Airport (LEMG) | Munster Osnabruck Airport (EDDG) | 2026-08-25 04:11 UTC | 2026-08-25 06:47 UTC | 2h 35m |
| LTZ212 | LTZ | Wonderboom Airport (FAWB) | Pilanesberg International Airport (FAPN) | 2026-08-25 06:24 UTC | 2026-08-25 06:47 UTC | 22m |
| EFC983U | EFC | Fujairah International Airport (OMFJ) | Al Minhad Air Base (OMDM) | 2026-08-25 06:30 UTC | 2026-08-25 06:46 UTC | 16m |
| MLDYS | MLD | Cannes-Mandelieu Airport (LFMD) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-25 06:35 UTC | 2026-08-25 06:43 UTC | 8m |
| JUST72 | JUS | Holsworthy (Military) Airport (YSHW) | Holsworthy (Military) Airport (YSHW) | 2026-08-25 05:45 UTC | 2026-08-25 06:41 UTC | 55m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-25 05:51 UTC | 2026-08-25 06:41 UTC | 49m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-08-25 05:59 UTC | 2026-08-25 06:37 UTC | 38m |
| RYR340F | Ryanair | Brussels South Charleroi Airport (EBCI) | Suceava Stefan cel Mare Airport (LRSV) | 2026-08-25 04:45 UTC | 2026-08-25 06:35 UTC | 1h 50m |
| EWG1A | EWG | Dusseldorf International Airport (EDDL) | London Heathrow Airport (EGLL) | 2026-08-25 05:27 UTC | 2026-08-25 06:33 UTC | 1h 6m |
| VLG3QU | Vueling | Barcelona International Airport (LEBL) | La Morgal Airport (LEMR) | 2026-08-25 05:27 UTC | 2026-08-25 06:30 UTC | 1h 2m |
| EZS1065 | EZS | Mollis Airport (LSZM) | San Sebastian Airport (LESO) | 2026-08-25 05:10 UTC | 2026-08-25 06:29 UTC | 1h 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
