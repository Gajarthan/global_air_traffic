# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_11:32:33_UTC-green)

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

**Latest saved flight:** 2026-09-07 11:32:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-07 11:32:33 UTC

- **250,352** saved flights
- **75,173** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **250,352** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,014,248.7 tonnes** estimated CO2 emissions
- **174,739,054 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10023 |
| 2 | SkyWest Airlines | 8737 |
| 3 | EJA | 4832 |
| 4 | IndiGo | 4186 |
| 5 | American Airlines | 4004 |
| 6 | Southwest Airlines | 3718 |
| 7 | Delta Air Lines | 3171 |
| 8 | ENY | 2995 |
| 9 | LATAM Airlines | 2416 |
| 10 | AZU | 2329 |
| 11 | Vueling | 2139 |
| 12 | WIF | 2003 |
| 13 | Lufthansa | 1986 |
| 14 | LXJ | 1940 |
| 15 | easyJet | 1724 |
| 16 | Swiss International | 1683 |
| 17 | AXM | 1628 |
| 18 | EJU | 1609 |
| 19 | QLK | 1609 |
| 20 | United Airlines | 1568 |
| 21 | Alaska Airlines | 1496 |
| 22 | All Nippon Airways | 1469 |
| 23 | WMT | 1422 |
| 24 | GLO | 1392 |
| 25 | PGT | 1376 |
| 26 | VIV | 1372 |
| 27 | Wizz Air | 1363 |
| 28 | Air France | 1362 |
| 29 | AEE | 1229 |
| 30 | JetBlue | 1227 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 207526 |
| 2 | 🇪🇸 ES | 16021 |
| 3 | 🇧🇷 BR | 14612 |
| 4 | 🇦🇺 AU | 14234 |
| 5 | 🇨🇦 CA | 13906 |
| 6 | 🇮🇹 IT | 13717 |
| 7 | 🇮🇳 IN | 13069 |
| 8 | 🇩🇪 DE | 12316 |
| 9 | 🇬🇧 GB | 11745 |
| 10 | 🇨🇴 CO | 10990 |
| 11 | 🇫🇷 FR | 10089 |
| 12 | 🇯🇵 JP | 9876 |
| 13 | 🇹🇷 TR | 7479 |
| 14 | 🇬🇷 GR | 7369 |
| 15 | 🇲🇽 MX | 6915 |
| 16 | 🇨🇭 CH | 6751 |
| 17 | 🇳🇴 NO | 6198 |
| 18 | 🇹🇭 TH | 4512 |
| 19 | 🇲🇾 MY | 4370 |
| 20 | 🇿🇦 ZA | 4309 |
| 21 | 🇵🇱 PL | 4182 |
| 22 | 🇳🇿 NZ | 3423 |
| 23 | 🇵🇭 PH | 3404 |
| 24 | 🇬🇹 GT | 3133 |
| 25 | 🇰🇷 KR | 2902 |
| 26 | 🇭🇷 HR | 2878 |
| 27 | 🇲🇦 MA | 2535 |
| 28 | 🇲🇪 ME | 2356 |
| 29 | 🇳🇱 NL | 2264 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5168 |
| 2 | Denver International Airport |  | US | 4045 |
| 3 | Indira Gandhi International Airport |  | IN | 3049 |
| 4 | Tokyo International Airport |  | JP | 2948 |
| 5 | Guaymaral Airport |  | CO | 2737 |
| 6 | Harry Reid International Airport |  | US | 2662 |
| 7 | Zurich Airport |  | CH | 2621 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2540 |
| 9 | El Dorado International Airport |  | CO | 2534 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2482 |
| 11 | La Aurora Airport |  | GT | 2389 |
| 12 | Salt Lake City International Airport |  | US | 2213 |
| 13 | Chicago O'Hare International Airport |  | US | 2185 |
| 14 | Congonhas Airport |  | BR | 2146 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2058 |
| 16 | Capua Airport |  | IT | 1975 |
| 17 | Madrid Barajas International Airport |  | ES | 1969 |
| 18 | Frankfurt am Main International Airport |  | DE | 1955 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1880 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1823 |
| 21 | Malpensa International Airport |  | IT | 1802 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1759 |
| 23 | Charles de Gaulle International Airport |  | FR | 1753 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1745 |
| 25 | Ninoy Aquino International Airport |  | PH | 1661 |
| 26 | Macau International Airport |  | MO | 1648 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1639 |
| 28 | Charlotte/Douglas International Airport |  | US | 1585 |
| 29 | Barcelona International Airport |  | ES | 1583 |
| 30 | Kuala Lumpur International Airport |  | MY | 1573 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1533 |
| 32 | Viracopos International Airport |  | BR | 1496 |
| 33 | Seattle-Tacoma International Airport |  | US | 1474 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1452 |
| 35 | Don Mueang International Airport |  | TH | 1446 |
| 36 | Calgary International Airport |  | CA | 1440 |
| 37 | Bengaluru International Airport |  | IN | 1433 |
| 38 | Oslo Gardermoen Airport |  | NO | 1411 |
| 39 | Vancouver International Airport |  | CA | 1400 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1359 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 930 | 21m | 244 km | 3,916.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 657 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 635 | 24m | 225 km | 2,463.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 629 | 1h 6m | 770 km | 8,355.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 563 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 410 | 27m | 275 km | 1,942.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 400 | 1h 50m | 1,423 km | 9,816.6 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 391 | 44m | 555 km | 3,744.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 372 | 44m | 241 km | 1,545.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 352 | 21m | 250 km | 1,520.4 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 349 | 24m | 218 km | 1,314.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 334 | 23m | 55 km | 317.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 309 | 26m | 215 km | 1,144.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 291 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 287 | 19m | 144 km | 713.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 257 | 41m | 535 km | 2,373.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DEAPR | DEA | Lubeck Blankensee Airport (EDHL) | Lubeck Blankensee Airport (EDHL) | 2026-09-07 09:28 UTC | 2026-09-07 11:32 UTC | 2h 3m |
| FHEGC | FHE | Amigdhaleon Airport (LGKM) | Amigdhaleon Airport (LGKM) | 2026-09-07 11:10 UTC | 2026-09-07 11:26 UTC | 16m |
| 304 |  | Be'er Sheva (Teyman) Airport (LLBS) | Be'er Sheva (Teyman) Airport (LLBS) | 2026-09-07 11:14 UTC | 2026-09-07 11:24 UTC | 10m |
| DLH9KW | Lufthansa | Munich International Airport (EDDM) | Belgrade Nikola Tesla Airport (LYBE) | 2026-09-07 09:21 UTC | 2026-09-07 11:20 UTC | 1h 59m |
| WIF7JE | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-09-07 10:15 UTC | 2026-09-07 11:12 UTC | 57m |
| WIF8HK | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-09-07 10:56 UTC | 2026-09-07 11:09 UTC | 13m |
| TJT31DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-09-07 09:49 UTC | 2026-09-07 11:04 UTC | 1h 15m |
| IGO390M | IndiGo | Indira Gandhi International Airport (VIDP) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-07 08:41 UTC | 2026-09-07 11:01 UTC | 2h 20m |
| N81NG |  | Cavern City Air Trml Airport (KCNM) | Casas Adobes Airpark (NM69) | 2026-09-07 10:03 UTC | 2026-09-07 10:54 UTC | 51m |
| AFR87GN | Air France | Charles de Gaulle International Airport (LFPG) | Marseille Provence Airport (LFML) | 2026-09-07 09:50 UTC | 2026-09-07 10:54 UTC | 1h 3m |
| AIC6BS | Air India | Juhu Aerodrome (VAJJ) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-07 07:46 UTC | 2026-09-07 10:51 UTC | 3h 5m |
| IGO7642 | IndiGo | Safdarjung Airport (VIDD) | Jaipur International Airport (VIJP) | 2026-09-07 10:24 UTC | 2026-09-07 10:51 UTC | 26m |
| AIQ3925 | AIQ | Don Mueang International Airport (VTBD) | Khunan Phumipol Airport (VTPY) | 2026-09-07 10:08 UTC | 2026-09-07 10:46 UTC | 37m |
| N904SH |  | Rochester International Airport (KRST) | Webb Lake Airport (MN00) | 2026-09-07 09:53 UTC | 2026-09-07 10:45 UTC | 51m |
| RAM972C | Royal Air Maroc | Tit Mellil Airport (GMMT) | Madrid Barajas International Airport (LEMD) | 2026-09-07 09:29 UTC | 2026-09-07 10:43 UTC | 1h 13m |
| FIN9VM | Finnair | Helsinki Vantaa Airport (EFHK) | Vaasa Airport (EFVA) | 2026-09-07 09:52 UTC | 2026-09-07 10:42 UTC | 50m |
| VLG3SZ | Vueling | Santiago de Compostela Airport (LEST) | Bilbao Airport (LEBB) | 2026-09-07 10:06 UTC | 2026-09-07 10:39 UTC | 32m |
| VTBVV | VTB | Indira Gandhi International Airport (VIDP) | Ambala Air Force Station (VIAM) | 2026-09-07 10:15 UTC | 2026-09-07 10:37 UTC | 21m |
| NOK546 | NOK | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 2026-09-07 09:53 UTC | 2026-09-07 10:36 UTC | 43m |
| EZS16RV | EZS | Mollis Airport (LSZM) | Zemunik Airport (LDZD) | 2026-09-07 09:39 UTC | 2026-09-07 10:35 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
