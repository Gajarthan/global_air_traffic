# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_11:49:27_UTC-green)

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

**Latest saved flight:** 2026-09-25 11:49:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-25 11:49:27 UTC

- **269,006** saved flights
- **78,910** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **269,006** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,263,333.4 tonnes** estimated CO2 emissions
- **189,178,748 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10602 |
| 2 | SkyWest Airlines | 9356 |
| 3 | EJA | 5252 |
| 4 | IndiGo | 4510 |
| 5 | American Airlines | 4182 |
| 6 | Southwest Airlines | 3952 |
| 7 | Delta Air Lines | 3346 |
| 8 | ENY | 3159 |
| 9 | LATAM Airlines | 2596 |
| 10 | AZU | 2519 |
| 11 | Vueling | 2243 |
| 12 | WIF | 2190 |
| 13 | LXJ | 2116 |
| 14 | Lufthansa | 2045 |
| 15 | easyJet | 1805 |
| 16 | Swiss International | 1765 |
| 17 | QLK | 1736 |
| 18 | EJU | 1688 |
| 19 | AXM | 1674 |
| 20 | United Airlines | 1649 |
| 21 | Alaska Airlines | 1587 |
| 22 | All Nippon Airways | 1549 |
| 23 | PGT | 1512 |
| 24 | WMT | 1502 |
| 25 | GLO | 1498 |
| 26 | Air France | 1477 |
| 27 | VIV | 1468 |
| 28 | Wizz Air | 1462 |
| 29 | CXK | 1318 |
| 30 | AEE | 1293 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 223861 |
| 2 | 🇪🇸 ES | 16860 |
| 3 | 🇧🇷 BR | 15729 |
| 4 | 🇦🇺 AU | 15494 |
| 5 | 🇨🇦 CA | 15004 |
| 6 | 🇮🇹 IT | 14573 |
| 7 | 🇮🇳 IN | 14255 |
| 8 | 🇩🇪 DE | 12910 |
| 9 | 🇬🇧 GB | 12456 |
| 10 | 🇨🇴 CO | 12323 |
| 11 | 🇫🇷 FR | 10699 |
| 12 | 🇯🇵 JP | 10348 |
| 13 | 🇹🇷 TR | 8144 |
| 14 | 🇬🇷 GR | 7777 |
| 15 | 🇲🇽 MX | 7413 |
| 16 | 🇨🇭 CH | 7152 |
| 17 | 🇳🇴 NO | 6659 |
| 18 | 🇹🇭 TH | 4812 |
| 19 | 🇲🇾 MY | 4526 |
| 20 | 🇿🇦 ZA | 4498 |
| 21 | 🇵🇱 PL | 4406 |
| 22 | 🇳🇿 NZ | 3768 |
| 23 | 🇵🇭 PH | 3569 |
| 24 | 🇬🇹 GT | 3403 |
| 25 | 🇭🇷 HR | 3062 |
| 26 | 🇰🇷 KR | 3046 |
| 27 | 🇲🇦 MA | 2682 |
| 28 | 🇲🇪 ME | 2521 |
| 29 | 🇳🇱 NL | 2406 |
| 30 | 🇮🇩 ID | 2241 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5478 |
| 2 | Denver International Airport |  | US | 4372 |
| 3 | Indira Gandhi International Airport |  | IN | 3221 |
| 4 | Tokyo International Airport |  | JP | 3096 |
| 5 | El Dorado International Airport |  | CO | 2917 |
| 6 | Harry Reid International Airport |  | US | 2881 |
| 7 | Guaymaral Airport |  | CO | 2811 |
| 8 | Zurich Airport |  | CH | 2789 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2704 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2593 |
| 11 | La Aurora Airport |  | GT | 2586 |
| 12 | Salt Lake City International Airport |  | US | 2369 |
| 13 | Chicago O'Hare International Airport |  | US | 2301 |
| 14 | Congonhas Airport |  | BR | 2291 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2202 |
| 16 | Capua Airport |  | IT | 2093 |
| 17 | Madrid Barajas International Airport |  | ES | 2073 |
| 18 | Frankfurt am Main International Airport |  | DE | 2041 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2037 |
| 20 | Malpensa International Airport |  | IT | 1926 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1919 |
| 22 | Charles de Gaulle International Airport |  | FR | 1908 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1886 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1882 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1818 |
| 26 | Macau International Airport |  | MO | 1787 |
| 27 | Ninoy Aquino International Airport |  | PH | 1751 |
| 28 | Charlotte/Douglas International Airport |  | US | 1680 |
| 29 | Barcelona International Airport |  | ES | 1674 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1665 |
| 31 | Viracopos International Airport |  | BR | 1626 |
| 32 | Kuala Lumpur International Airport |  | MY | 1620 |
| 33 | Seattle-Tacoma International Airport |  | US | 1575 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1572 |
| 35 | Calgary International Airport |  | CA | 1533 |
| 36 | Don Mueang International Airport |  | TH | 1524 |
| 37 | Bengaluru International Airport |  | IN | 1518 |
| 38 | Oslo Gardermoen Airport |  | NO | 1511 |
| 39 | Vancouver International Airport |  | CA | 1507 |
| 40 | Antalya International Airport |  | TR | 1433 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1121 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1008 | 21m | 244 km | 4,244.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 742 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 678 | 1h 6m | 770 km | 9,006.7 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 671 | 24m | 225 km | 2,603.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 598 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 443 | 44m | 555 km | 4,241.9 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 431 | 27m | 275 km | 2,042.3 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 425 | 1h 50m | 1,423 km | 10,430.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 411 | 44m | 241 km | 1,707.2 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 385 | 24m | 218 km | 1,450.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 364 | 21m | 250 km | 1,572.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 360 | 23m | 55 km | 342.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 343 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 341 | 1h 6m | 706 km | 4,151.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 338 | 19m | 99 km | 579.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 335 | 26m | 215 km | 1,240.7 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 313 | 19m | 144 km | 778.6 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 294 | 42m | 535 km | 2,715.3 t |
| 26 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 289 | 18m | 14 km | 72.3 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 284 | 28m | 152 km | 742.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LRS4708 | LRS | Juan Santamaria International Airport (MROC) | Juan Santamaria International Airport (MROC) | 2026-09-25 11:31 UTC | 2026-09-25 11:49 UTC | 17m |
| EFY7812 | EFY | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-09-25 10:53 UTC | 2026-09-25 11:25 UTC | 32m |
| N2358P |  | Aerojaco Airport (SIUB) | Aerojaco Airport (SIUB) | 2026-09-25 10:32 UTC | 2026-09-25 11:19 UTC | 47m |
| HK4626G |  | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-09-25 11:10 UTC | 2026-09-25 11:16 UTC | 5m |
| GCEHV | GCE | Wroughton Airfield (EGDT) | Popham Airport (EGHP) | 2026-09-25 10:50 UTC | 2026-09-25 11:08 UTC | 18m |
| HK4820 |  | Enrique Olaya Herrera Airport (SKMD) | Amalfi Airport (SKAM) | 2026-09-25 10:56 UTC | 2026-09-25 11:08 UTC | 11m |
| RSD953 | RSD | Vnukovo International Airport (UUWW) | Talagi Airport (ULAA) | 2026-09-25 06:17 UTC | 2026-09-25 11:08 UTC | 4h 50m |
| SWR55Y | Swiss International | Geneva Cointrin International Airport (LSGG) | Stockholm-Arlanda Airport (ESSA) | 2026-09-25 08:22 UTC | 2026-09-25 11:04 UTC | 2h 42m |
| WIF7JE | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-09-25 10:10 UTC | 2026-09-25 11:03 UTC | 53m |
| WIF77P | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-09-25 10:12 UTC | 2026-09-25 11:02 UTC | 50m |
| N240GS |  | Old Sarum Airfield (EGLS) | Old Sarum Airfield (EGLS) | 2026-09-25 10:44 UTC | 2026-09-25 11:01 UTC | 17m |
| GTOUS | GTO | White Waltham Airfield (EGLM) | Rochester Airport (EGTO) | 2026-09-25 10:23 UTC | 2026-09-25 11:00 UTC | 37m |
| TAM3474 | LATAM Airlines | Congonhas Airport (SBSP) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-09-25 10:19 UTC | 2026-09-25 11:00 UTC | 41m |
| NAY868 | NAY | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-09-25 10:46 UTC | 2026-09-25 10:59 UTC | 12m |
| IGO6393 | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Ambala Air Force Station (VIAM) | 2026-09-25 09:19 UTC | 2026-09-25 10:56 UTC | 1h 37m |
| MAS1450 | Malaysia Airlines | Bentong Airport (WMAD) | Penang International Airport (WMKP) | 2026-09-25 10:24 UTC | 2026-09-25 10:55 UTC | 31m |
| JAP7318 | JAP | Jorge Chavez International Airport (SPJC) | Quiruvilca Airport (SPQR) | 2026-09-25 10:14 UTC | 2026-09-25 10:55 UTC | 41m |
| EJU59GR | EJU | Napoli / Capodichino International Airport (LIRN) | Lyon Saint-Exupery Airport (LFLL) | 2026-09-25 09:25 UTC | 2026-09-25 10:52 UTC | 1h 27m |
| TVF57LK | TVF | Paris-Orly Airport (LFPO) | Visoko Sport Airfield (LQVI) | 2026-09-25 09:02 UTC | 2026-09-25 10:52 UTC | 1h 50m |
| WIF48P | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-09-25 10:41 UTC | 2026-09-25 10:52 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
