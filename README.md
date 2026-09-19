# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_13:05:47_UTC-green)

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

**Latest saved flight:** 2026-09-19 13:05:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-19 13:05:47 UTC

- **263,341** saved flights
- **77,796** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **263,341** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,190,769.9 tonnes** estimated CO2 emissions
- **184,972,169 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10419 |
| 2 | SkyWest Airlines | 9157 |
| 3 | EJA | 5107 |
| 4 | IndiGo | 4431 |
| 5 | American Airlines | 4127 |
| 6 | Southwest Airlines | 3869 |
| 7 | Delta Air Lines | 3286 |
| 8 | ENY | 3103 |
| 9 | LATAM Airlines | 2538 |
| 10 | AZU | 2474 |
| 11 | Vueling | 2214 |
| 12 | WIF | 2127 |
| 13 | LXJ | 2063 |
| 14 | Lufthansa | 2031 |
| 15 | easyJet | 1780 |
| 16 | Swiss International | 1737 |
| 17 | QLK | 1701 |
| 18 | EJU | 1661 |
| 19 | AXM | 1660 |
| 20 | United Airlines | 1614 |
| 21 | Alaska Airlines | 1561 |
| 22 | All Nippon Airways | 1522 |
| 23 | PGT | 1481 |
| 24 | WMT | 1481 |
| 25 | GLO | 1469 |
| 26 | Air France | 1444 |
| 27 | VIV | 1438 |
| 28 | Wizz Air | 1429 |
| 29 | CXK | 1275 |
| 30 | TKR | 1275 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 218723 |
| 2 | 🇪🇸 ES | 16603 |
| 3 | 🇧🇷 BR | 15408 |
| 4 | 🇦🇺 AU | 15104 |
| 5 | 🇨🇦 CA | 14655 |
| 6 | 🇮🇹 IT | 14311 |
| 7 | 🇮🇳 IN | 14002 |
| 8 | 🇩🇪 DE | 12730 |
| 9 | 🇬🇧 GB | 12227 |
| 10 | 🇨🇴 CO | 11928 |
| 11 | 🇫🇷 FR | 10523 |
| 12 | 🇯🇵 JP | 10203 |
| 13 | 🇹🇷 TR | 7981 |
| 14 | 🇬🇷 GR | 7643 |
| 15 | 🇲🇽 MX | 7239 |
| 16 | 🇨🇭 CH | 7037 |
| 17 | 🇳🇴 NO | 6510 |
| 18 | 🇹🇭 TH | 4730 |
| 19 | 🇲🇾 MY | 4472 |
| 20 | 🇿🇦 ZA | 4440 |
| 21 | 🇵🇱 PL | 4346 |
| 22 | 🇳🇿 NZ | 3652 |
| 23 | 🇵🇭 PH | 3506 |
| 24 | 🇬🇹 GT | 3354 |
| 25 | 🇭🇷 HR | 3003 |
| 26 | 🇰🇷 KR | 2991 |
| 27 | 🇲🇦 MA | 2635 |
| 28 | 🇲🇪 ME | 2472 |
| 29 | 🇳🇱 NL | 2360 |
| 30 | 🇮🇩 ID | 2216 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5380 |
| 2 | Denver International Airport |  | US | 4257 |
| 3 | Indira Gandhi International Airport |  | IN | 3165 |
| 4 | Tokyo International Airport |  | JP | 3047 |
| 5 | Harry Reid International Airport |  | US | 2800 |
| 6 | El Dorado International Airport |  | CO | 2792 |
| 7 | Guaymaral Airport |  | CO | 2782 |
| 8 | Zurich Airport |  | CH | 2742 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2646 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2553 |
| 11 | La Aurora Airport |  | GT | 2549 |
| 12 | Salt Lake City International Airport |  | US | 2325 |
| 13 | Chicago O'Hare International Airport |  | US | 2266 |
| 14 | Congonhas Airport |  | BR | 2249 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2151 |
| 16 | Capua Airport |  | IT | 2055 |
| 17 | Madrid Barajas International Airport |  | ES | 2034 |
| 18 | Frankfurt am Main International Airport |  | DE | 2010 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1987 |
| 20 | Malpensa International Airport |  | IT | 1895 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1889 |
| 22 | Charles de Gaulle International Airport |  | FR | 1861 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1856 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1820 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1800 |
| 26 | Macau International Airport |  | MO | 1751 |
| 27 | Ninoy Aquino International Airport |  | PH | 1721 |
| 28 | Barcelona International Airport |  | ES | 1645 |
| 29 | Charlotte/Douglas International Airport |  | US | 1642 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1619 |
| 31 | Kuala Lumpur International Airport |  | MY | 1603 |
| 32 | Viracopos International Airport |  | BR | 1598 |
| 33 | Seattle-Tacoma International Airport |  | US | 1546 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1533 |
| 35 | Don Mueang International Airport |  | TH | 1502 |
| 36 | Calgary International Airport |  | CA | 1502 |
| 37 | Bengaluru International Airport |  | IN | 1497 |
| 38 | Oslo Gardermoen Airport |  | NO | 1484 |
| 39 | Vancouver International Airport |  | CA | 1472 |
| 40 | Antalya International Airport |  | TR | 1410 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1113 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 985 | 21m | 244 km | 4,147.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 720 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 662 | 1h 6m | 770 km | 8,794.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 657 | 24m | 225 km | 2,548.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 590 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 429 | 44m | 555 km | 4,107.9 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 424 | 27m | 275 km | 2,009.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 416 | 1h 50m | 1,423 km | 10,209.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 401 | 44m | 241 km | 1,665.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 375 | 24m | 218 km | 1,412.8 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 17 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 333 | 12m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 326 | 26m | 215 km | 1,207.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 326 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 284 | 1h 50m | 1,304 km | 6,389.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 282 | 42m | 535 km | 2,604.5 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 281 | 28m | 152 km | 734.4 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SPSDW | SPS | Lubin Airport (EPLU) | Lubin Airport (EPLU) | 2026-09-19 12:41 UTC | 2026-09-19 13:05 UTC | 24m |
| N65DM |  | William P Gwinn Airport (06FA) | William P Gwinn Airport (06FA) | 2026-09-19 12:49 UTC | 2026-09-19 12:56 UTC | 7m |
| CAL5824 | CAL | Chek Lap Kok International Airport (VHHH) | Hsinchu Air Base (RCPO) | 2026-09-19 11:41 UTC | 2026-09-19 12:55 UTC | 1h 13m |
| N352BG |  | Wood County Regional Airport (K1G0) | Wood County Regional Airport (K1G0) | 2026-09-19 11:55 UTC | 2026-09-19 12:51 UTC | 56m |
| HKE116 | HKE | Chek Lap Kok International Airport (VHHH) | Hsinchu Air Base (RCPO) | 2026-09-19 11:35 UTC | 2026-09-19 12:49 UTC | 1h 13m |
| HK741G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-09-19 12:30 UTC | 2026-09-19 12:46 UTC | 15m |
| SWA222 | Southwest Airlines | Orlando International Airport (KMCO) | Sandy Point Airport (MYAS) | 2026-09-19 12:07 UTC | 2026-09-19 12:45 UTC | 37m |
| JAL809 | Japan Airlines | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-09-19 09:49 UTC | 2026-09-19 12:41 UTC | 2h 52m |
| ARPIA | ARP | Nuevo Aeropuerto Internacional Mariscal Sucre (SEQM) | Nuevo Aeropuerto Internacional Mariscal Sucre (SEQM) | 2026-09-19 12:21 UTC | 2026-09-19 12:34 UTC | 13m |
| PH712 |  | Twenthe Airport (EHTW) | Twenthe Airport (EHTW) | 2026-09-19 12:24 UTC | 2026-09-19 12:33 UTC | 8m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Zhuhai Airport (ZGSD) | 2026-09-18 22:03 UTC | 2026-09-19 12:28 UTC | 14h 24m |
| RGA06 | RGA | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-09-19 12:24 UTC | 2026-09-19 12:27 UTC | 2m |
| ZKIWD | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-09-19 12:12 UTC | 2026-09-19 12:26 UTC | 14m |
| 4XDAN |  | Bar Yehuda Airfield (LLMZ) | Bar Yehuda Airfield (LLMZ) | 2026-09-19 12:09 UTC | 2026-09-19 12:21 UTC | 11m |
| WIF170 | WIF | Bergen Airport Flesland (ENBR) | Sandane Airport Anda (ENSD) | 2026-09-19 11:52 UTC | 2026-09-19 12:20 UTC | 28m |
| PH1529 |  | Terlet Airport (EHTL) | Terlet Airport (EHTL) | 2026-09-19 12:08 UTC | 2026-09-19 12:19 UTC | 10m |
| TGCYE | TGC | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-09-19 11:58 UTC | 2026-09-19 12:19 UTC | 20m |
| HBZZX | HBZ | Meiringen Airport (LSMM) | Raron Airport (LSTA) | 2026-09-19 11:06 UTC | 2026-09-19 12:17 UTC | 1h 11m |
| PH1693 |  | Terlet Airport (EHTL) | Terlet Airport (EHTL) | 2026-09-19 12:10 UTC | 2026-09-19 12:17 UTC | 6m |
| NJE745H | NJE | Stockholm-Bromma Airport (ESSB) | Raron Airport (LSTA) | 2026-09-19 09:53 UTC | 2026-09-19 12:14 UTC | 2h 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
