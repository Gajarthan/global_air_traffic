# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_14:22:59_UTC-green)

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

**Latest saved flight:** 2026-09-18 14:22:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-18 14:22:59 UTC

- **262,279** saved flights
- **77,594** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **262,279** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,177,224.8 tonnes** estimated CO2 emissions
- **184,186,946 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10382 |
| 2 | SkyWest Airlines | 9127 |
| 3 | EJA | 5083 |
| 4 | IndiGo | 4407 |
| 5 | American Airlines | 4113 |
| 6 | Southwest Airlines | 3847 |
| 7 | Delta Air Lines | 3276 |
| 8 | ENY | 3094 |
| 9 | LATAM Airlines | 2527 |
| 10 | AZU | 2464 |
| 11 | Vueling | 2206 |
| 12 | WIF | 2118 |
| 13 | LXJ | 2050 |
| 14 | Lufthansa | 2029 |
| 15 | easyJet | 1773 |
| 16 | Swiss International | 1735 |
| 17 | QLK | 1698 |
| 18 | AXM | 1655 |
| 19 | EJU | 1650 |
| 20 | United Airlines | 1609 |
| 21 | Alaska Airlines | 1555 |
| 22 | All Nippon Airways | 1518 |
| 23 | WMT | 1478 |
| 24 | PGT | 1472 |
| 25 | GLO | 1464 |
| 26 | Air France | 1437 |
| 27 | VIV | 1433 |
| 28 | Wizz Air | 1424 |
| 29 | TKR | 1275 |
| 30 | AEE | 1271 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 217787 |
| 2 | 🇪🇸 ES | 16550 |
| 3 | 🇧🇷 BR | 15355 |
| 4 | 🇦🇺 AU | 15072 |
| 5 | 🇨🇦 CA | 14596 |
| 6 | 🇮🇹 IT | 14264 |
| 7 | 🇮🇳 IN | 13910 |
| 8 | 🇩🇪 DE | 12689 |
| 9 | 🇬🇧 GB | 12188 |
| 10 | 🇨🇴 CO | 11839 |
| 11 | 🇫🇷 FR | 10493 |
| 12 | 🇯🇵 JP | 10179 |
| 13 | 🇹🇷 TR | 7938 |
| 14 | 🇬🇷 GR | 7612 |
| 15 | 🇲🇽 MX | 7219 |
| 16 | 🇨🇭 CH | 7008 |
| 17 | 🇳🇴 NO | 6480 |
| 18 | 🇹🇭 TH | 4707 |
| 19 | 🇲🇾 MY | 4462 |
| 20 | 🇿🇦 ZA | 4426 |
| 21 | 🇵🇱 PL | 4329 |
| 22 | 🇳🇿 NZ | 3639 |
| 23 | 🇵🇭 PH | 3499 |
| 24 | 🇬🇹 GT | 3343 |
| 25 | 🇭🇷 HR | 2993 |
| 26 | 🇰🇷 KR | 2987 |
| 27 | 🇲🇦 MA | 2619 |
| 28 | 🇲🇪 ME | 2465 |
| 29 | 🇳🇱 NL | 2342 |
| 30 | 🇮🇩 ID | 2213 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5363 |
| 2 | Denver International Airport |  | US | 4241 |
| 3 | Indira Gandhi International Airport |  | IN | 3156 |
| 4 | Tokyo International Airport |  | JP | 3038 |
| 5 | Harry Reid International Airport |  | US | 2788 |
| 6 | Guaymaral Airport |  | CO | 2777 |
| 7 | El Dorado International Airport |  | CO | 2764 |
| 8 | Zurich Airport |  | CH | 2733 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2639 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2545 |
| 11 | La Aurora Airport |  | GT | 2539 |
| 12 | Salt Lake City International Airport |  | US | 2314 |
| 13 | Chicago O'Hare International Airport |  | US | 2263 |
| 14 | Congonhas Airport |  | BR | 2240 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2140 |
| 16 | Capua Airport |  | IT | 2047 |
| 17 | Madrid Barajas International Airport |  | ES | 2028 |
| 18 | Frankfurt am Main International Airport |  | DE | 2002 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1978 |
| 20 | Malpensa International Airport |  | IT | 1887 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1880 |
| 22 | Charles de Gaulle International Airport |  | FR | 1853 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1850 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1800 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1797 |
| 26 | Macau International Airport |  | MO | 1743 |
| 27 | Ninoy Aquino International Airport |  | PH | 1716 |
| 28 | Barcelona International Airport |  | ES | 1636 |
| 29 | Charlotte/Douglas International Airport |  | US | 1632 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1614 |
| 31 | Kuala Lumpur International Airport |  | MY | 1601 |
| 32 | Viracopos International Airport |  | BR | 1592 |
| 33 | Seattle-Tacoma International Airport |  | US | 1540 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1525 |
| 35 | Don Mueang International Airport |  | TH | 1498 |
| 36 | Calgary International Airport |  | CA | 1496 |
| 37 | Bengaluru International Airport |  | IN | 1488 |
| 38 | Oslo Gardermoen Airport |  | NO | 1476 |
| 39 | Vancouver International Airport |  | CA | 1467 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1404 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1112 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 978 | 21m | 244 km | 4,118.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 712 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 659 | 1h 6m | 770 km | 8,754.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 655 | 24m | 225 km | 2,541.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 588 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 426 | 44m | 555 km | 4,079.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 424 | 27m | 275 km | 2,009.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 414 | 1h 50m | 1,423 km | 10,160.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 400 | 44m | 241 km | 1,661.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 369 | 24m | 218 km | 1,390.2 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 359 | 21m | 250 km | 1,550.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 330 | 1h 6m | 706 km | 4,017.8 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 327 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 325 | 26m | 215 km | 1,203.7 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 324 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 304 | 19m | 144 km | 756.2 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 284 | 1h 50m | 1,304 km | 6,389.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 280 | 42m | 535 km | 2,586.0 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 278 | 28m | 152 km | 726.5 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA337 | Cathay Pacific | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-09-18 11:53 UTC | 2026-09-18 14:22 UTC | 2h 29m |
| NOZ816 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Stockholm-Arlanda Airport (ESSA) | 2026-09-18 13:44 UTC | 2026-09-18 14:22 UTC | 37m |
| N5543A |  | Manchester Boston Regional Airport (KMHT) | Concord Municipal Airport (KCON) | 2026-09-18 14:10 UTC | 2026-09-18 14:21 UTC | 11m |
| N247DL |  | FL47 (FL47) | Orlando Executive Airport (KORL) | 2026-09-18 13:53 UTC | 2026-09-18 14:19 UTC | 26m |
| RTY592 | RTY | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-09-18 13:39 UTC | 2026-09-18 14:18 UTC | 39m |
| GOAT62 | GOA | Randolph Afb Airport (KRND) | New Braunfels Ntl Airport (KBAZ) | 2026-09-18 12:57 UTC | 2026-09-18 14:17 UTC | 1h 19m |
| SWC900 | SWC | Gothenburg-Landvetter Airport (ESGG) | Oresten Airport (ESGM) | 2026-09-18 14:03 UTC | 2026-09-18 14:16 UTC | 13m |
| N701NW |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-09-18 13:40 UTC | 2026-09-18 14:16 UTC | 35m |
| N757JY |  | Caldwell Executive Airport (KEUL) | Lanham Field (04ID) | 2026-09-18 13:44 UTC | 2026-09-18 14:11 UTC | 26m |
| NAK67N | NAK | Grenoble-Isere Airport (LFLS) | Nimes-Arles-Camargue Airport (LFTW) | 2026-09-18 13:27 UTC | 2026-09-18 14:10 UTC | 43m |
| CCA908 | Air China | Madrid Barajas International Airport (LEMD) | Elbląg Airport (EPEL) | 2026-09-18 11:29 UTC | 2026-09-18 14:09 UTC | 2h 39m |
| N737MT |  | Fort Worth Meacham International Airport (KFTW) | Austin-Bergstrom International Airport (KAUS) | 2026-09-18 13:37 UTC | 2026-09-18 14:08 UTC | 31m |
| N87RM |  | Skydive New England Airport (ME64) | Skydive New England Airport (ME64) | 2026-09-18 13:56 UTC | 2026-09-18 14:07 UTC | 11m |
| CXK664 | CXK | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-09-18 13:52 UTC | 2026-09-18 14:05 UTC | 12m |
| N486LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-09-18 13:04 UTC | 2026-09-18 14:02 UTC | 58m |
| N20AH |  | Grand Prairie Municipal Airport (KGPM) | Grand Prairie Municipal Airport (KGPM) | 2026-09-18 13:28 UTC | 2026-09-18 14:00 UTC | 31m |
| N402ER |  | Prescott Regional/Ernest A Love Field (KPRC) | Robin Airport (59AZ) | 2026-09-18 13:44 UTC | 2026-09-18 13:59 UTC | 15m |
| N72760 |  | Newark Liberty International Airport (KEWR) | John F Kennedy International Airport (KJFK) | 2026-09-18 13:18 UTC | 2026-09-18 13:59 UTC | 40m |
| N499SL |  | Baldwin County Regional Airport (KMLJ) | Baldwin County Regional Airport (KMLJ) | 2026-09-18 13:46 UTC | 2026-09-18 13:56 UTC | 9m |
| AIC2GQ | Air India | Chhatrapati Shivaji International Airport (VABB) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-18 11:21 UTC | 2026-09-18 13:53 UTC | 2h 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
