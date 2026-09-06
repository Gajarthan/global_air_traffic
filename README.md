# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--06_11:35:07_UTC-green)

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

**Latest saved flight:** 2026-09-06 11:35:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-06 11:35:07 UTC

- **249,264** saved flights
- **74,954** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **249,264** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,001,307.0 tonnes** estimated CO2 emissions
- **173,988,810 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9978 |
| 2 | SkyWest Airlines | 8703 |
| 3 | EJA | 4812 |
| 4 | IndiGo | 4166 |
| 5 | American Airlines | 3989 |
| 6 | Southwest Airlines | 3705 |
| 7 | Delta Air Lines | 3160 |
| 8 | ENY | 2983 |
| 9 | LATAM Airlines | 2404 |
| 10 | AZU | 2319 |
| 11 | Vueling | 2127 |
| 12 | WIF | 1988 |
| 13 | Lufthansa | 1977 |
| 14 | LXJ | 1936 |
| 15 | easyJet | 1719 |
| 16 | Swiss International | 1676 |
| 17 | AXM | 1628 |
| 18 | EJU | 1605 |
| 19 | QLK | 1597 |
| 20 | United Airlines | 1565 |
| 21 | Alaska Airlines | 1491 |
| 22 | All Nippon Airways | 1465 |
| 23 | WMT | 1412 |
| 24 | GLO | 1391 |
| 25 | PGT | 1367 |
| 26 | VIV | 1367 |
| 27 | Air France | 1359 |
| 28 | Wizz Air | 1350 |
| 29 | JetBlue | 1226 |
| 30 | AEE | 1224 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 206696 |
| 2 | 🇪🇸 ES | 15956 |
| 3 | 🇧🇷 BR | 14564 |
| 4 | 🇦🇺 AU | 14152 |
| 5 | 🇨🇦 CA | 13847 |
| 6 | 🇮🇹 IT | 13662 |
| 7 | 🇮🇳 IN | 12997 |
| 8 | 🇩🇪 DE | 12249 |
| 9 | 🇬🇧 GB | 11697 |
| 10 | 🇨🇴 CO | 10920 |
| 11 | 🇫🇷 FR | 10044 |
| 12 | 🇯🇵 JP | 9861 |
| 13 | 🇹🇷 TR | 7428 |
| 14 | 🇬🇷 GR | 7337 |
| 15 | 🇲🇽 MX | 6891 |
| 16 | 🇨🇭 CH | 6721 |
| 17 | 🇳🇴 NO | 6164 |
| 18 | 🇹🇭 TH | 4498 |
| 19 | 🇲🇾 MY | 4368 |
| 20 | 🇿🇦 ZA | 4297 |
| 21 | 🇵🇱 PL | 4165 |
| 22 | 🇳🇿 NZ | 3405 |
| 23 | 🇵🇭 PH | 3392 |
| 24 | 🇬🇹 GT | 3123 |
| 25 | 🇰🇷 KR | 2895 |
| 26 | 🇭🇷 HR | 2868 |
| 27 | 🇲🇦 MA | 2517 |
| 28 | 🇲🇪 ME | 2337 |
| 29 | 🇳🇱 NL | 2253 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5139 |
| 2 | Denver International Airport |  | US | 4029 |
| 3 | Indira Gandhi International Airport |  | IN | 3033 |
| 4 | Tokyo International Airport |  | JP | 2944 |
| 5 | Guaymaral Airport |  | CO | 2730 |
| 6 | Harry Reid International Airport |  | US | 2652 |
| 7 | Zurich Airport |  | CH | 2612 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2530 |
| 9 | El Dorado International Airport |  | CO | 2509 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2472 |
| 11 | La Aurora Airport |  | GT | 2380 |
| 12 | Salt Lake City International Airport |  | US | 2208 |
| 13 | Chicago O'Hare International Airport |  | US | 2181 |
| 14 | Congonhas Airport |  | BR | 2140 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2055 |
| 16 | Capua Airport |  | IT | 1965 |
| 17 | Madrid Barajas International Airport |  | ES | 1961 |
| 18 | Frankfurt am Main International Airport |  | DE | 1948 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1872 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1816 |
| 21 | Malpensa International Airport |  | IT | 1794 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1750 |
| 23 | Charles de Gaulle International Airport |  | FR | 1748 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1731 |
| 25 | Ninoy Aquino International Airport |  | PH | 1652 |
| 26 | Macau International Airport |  | MO | 1646 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1639 |
| 28 | Barcelona International Airport |  | ES | 1577 |
| 29 | Charlotte/Douglas International Airport |  | US | 1576 |
| 30 | Kuala Lumpur International Airport |  | MY | 1573 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1527 |
| 32 | Viracopos International Airport |  | BR | 1489 |
| 33 | Seattle-Tacoma International Airport |  | US | 1467 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1449 |
| 35 | Don Mueang International Airport |  | TH | 1441 |
| 36 | Calgary International Airport |  | CA | 1433 |
| 37 | Bengaluru International Airport |  | IN | 1432 |
| 38 | Oslo Gardermoen Airport |  | NO | 1401 |
| 39 | Vancouver International Airport |  | CA | 1395 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1356 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1103 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 928 | 21m | 244 km | 3,907.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 657 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 633 | 24m | 225 km | 2,455.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 629 | 1h 6m | 770 km | 8,355.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 561 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 410 | 27m | 275 km | 1,942.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 397 | 1h 50m | 1,423 km | 9,743.0 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 387 | 44m | 555 km | 3,705.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 369 | 44m | 241 km | 1,532.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 351 | 21m | 250 km | 1,516.1 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 348 | 24m | 218 km | 1,311.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 334 | 23m | 55 km | 317.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 307 | 26m | 215 km | 1,137.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 288 | 1h 14m | 961 km | 4,773.8 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 287 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 285 | 19m | 144 km | 708.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 256 | 28m | 152 km | 669.0 t |
| 30 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 255 | 41m | 535 km | 2,355.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DECAO | DEC | Kiel-Holtenau Airport (EDHK) | Kiel-Holtenau Airport (EDHK) | 2026-09-06 11:22 UTC | 2026-09-06 11:35 UTC | 12m |
| DEGGL | DEG | Braunschweig Wolfsburg Airport (EDVE) | Braunschweig Wolfsburg Airport (EDVE) | 2026-09-06 10:31 UTC | 2026-09-06 11:34 UTC | 1h 3m |
| DECAO | DEC | Kiel-Holtenau Airport (EDHK) | Kiel-Holtenau Airport (EDHK) | 2026-09-06 10:59 UTC | 2026-09-06 11:12 UTC | 12m |
| PHHLF | PHH | Midden-Zeeland Airport (EHMZ) | Midden-Zeeland Airport (EHMZ) | 2026-09-06 10:07 UTC | 2026-09-06 11:06 UTC | 58m |
| DEFIC | DEF | Neustadt/Aisch Airport (EDQN) | Neustadt/Aisch Airport (EDQN) | 2026-09-06 10:41 UTC | 2026-09-06 10:57 UTC | 15m |
| ZSOEE | ZSO | O. R. Tambo International Airport (FAOR) | Middelburg Airport (FAMB) | 2026-09-06 10:25 UTC | 2026-09-06 10:57 UTC | 31m |
| D8338 |  | Twenthe Airport (EHTW) | Twenthe Airport (EHTW) | 2026-09-06 10:10 UTC | 2026-09-06 10:54 UTC | 43m |
| HFA808 | HFA | Larnaca International Airport (LCLK) | Haifa International Airport (LLHA) | 2026-09-06 10:08 UTC | 2026-09-06 10:53 UTC | 44m |
| WIF77P | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-09-06 10:00 UTC | 2026-09-06 10:52 UTC | 52m |
| PSAPM | PSA | Ibiza Airport (LEIB) | Nice-Cote d'Azur Airport (LFMN) | 2026-09-06 09:35 UTC | 2026-09-06 10:51 UTC | 1h 16m |
| IGO7642 | IndiGo | Safdarjung Airport (VIDD) | Jaipur International Airport (VIJP) | 2026-09-06 10:19 UTC | 2026-09-06 10:50 UTC | 31m |
| RTV2M | RTV | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-09-06 10:34 UTC | 2026-09-06 10:49 UTC | 15m |
| TGZ627 | TGZ | Tbilisi International Airport (UGTB) | UKFB (UKFB) | 2026-09-06 08:43 UTC | 2026-09-06 10:44 UTC | 2h 0m |
| THY3DW | Turkish Airlines | Istanbul Airport (LTFM) | Bezymyanka Airfield (UWWG) | 2026-09-06 07:14 UTC | 2026-09-06 10:42 UTC | 3h 28m |
| WZZ97 | Wizz Air | Copernicus Wrocław Airport (EPWR) | Mollis Airport (LSZM) | 2026-09-06 09:22 UTC | 2026-09-06 10:36 UTC | 1h 14m |
| RYR45TN | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Bari / Palese International Airport (LIBD) | 2026-09-06 09:37 UTC | 2026-09-06 10:35 UTC | 57m |
|  |  | Asiago Airport (LIDA) | Trento / Mattarello Airport (LIDT) | 2026-09-06 10:28 UTC | 2026-09-06 10:33 UTC | 4m |
| MNE311 | MNE | Zurich Airport (LSZH) | Dubrovnik Airport (LDDU) | 2026-09-06 09:22 UTC | 2026-09-06 10:31 UTC | 1h 9m |
| N146SM |  | Boise Air Trml/Gowen Field (KBOI) | Oregon Sky Ranch Airport (OG33) | 2026-09-06 09:57 UTC | 2026-09-06 10:27 UTC | 29m |
| WZZ5K | Wizz Air | Comiso Airport Vincenzo Magliocco (LICB) | Katowice International Airport (EPKT) | 2026-09-06 08:07 UTC | 2026-09-06 10:23 UTC | 2h 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
