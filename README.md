# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_16:55:36_UTC-green)

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

**Latest saved flight:** 2026-09-07 16:55:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-07 16:55:36 UTC

- **250,586** saved flights
- **75,233** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **250,586** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,016,563.2 tonnes** estimated CO2 emissions
- **174,873,231 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10031 |
| 2 | SkyWest Airlines | 8750 |
| 3 | EJA | 4833 |
| 4 | IndiGo | 4193 |
| 5 | American Airlines | 4008 |
| 6 | Southwest Airlines | 3719 |
| 7 | Delta Air Lines | 3175 |
| 8 | ENY | 2997 |
| 9 | LATAM Airlines | 2417 |
| 10 | AZU | 2329 |
| 11 | Vueling | 2139 |
| 12 | WIF | 2009 |
| 13 | Lufthansa | 1986 |
| 14 | LXJ | 1946 |
| 15 | easyJet | 1725 |
| 16 | Swiss International | 1684 |
| 17 | AXM | 1628 |
| 18 | EJU | 1612 |
| 19 | QLK | 1609 |
| 20 | United Airlines | 1568 |
| 21 | Alaska Airlines | 1496 |
| 22 | All Nippon Airways | 1469 |
| 23 | WMT | 1423 |
| 24 | GLO | 1392 |
| 25 | PGT | 1376 |
| 26 | VIV | 1372 |
| 27 | Air France | 1365 |
| 28 | Wizz Air | 1364 |
| 29 | AEE | 1229 |
| 30 | JetBlue | 1227 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 207758 |
| 2 | 🇪🇸 ES | 16040 |
| 3 | 🇧🇷 BR | 14620 |
| 4 | 🇦🇺 AU | 14234 |
| 5 | 🇨🇦 CA | 13917 |
| 6 | 🇮🇹 IT | 13733 |
| 7 | 🇮🇳 IN | 13086 |
| 8 | 🇩🇪 DE | 12325 |
| 9 | 🇬🇧 GB | 11751 |
| 10 | 🇨🇴 CO | 11004 |
| 11 | 🇫🇷 FR | 10102 |
| 12 | 🇯🇵 JP | 9876 |
| 13 | 🇹🇷 TR | 7485 |
| 14 | 🇬🇷 GR | 7371 |
| 15 | 🇲🇽 MX | 6921 |
| 16 | 🇨🇭 CH | 6759 |
| 17 | 🇳🇴 NO | 6211 |
| 18 | 🇹🇭 TH | 4512 |
| 19 | 🇲🇾 MY | 4371 |
| 20 | 🇿🇦 ZA | 4313 |
| 21 | 🇵🇱 PL | 4187 |
| 22 | 🇳🇿 NZ | 3423 |
| 23 | 🇵🇭 PH | 3404 |
| 24 | 🇬🇹 GT | 3135 |
| 25 | 🇰🇷 KR | 2902 |
| 26 | 🇭🇷 HR | 2879 |
| 27 | 🇲🇦 MA | 2536 |
| 28 | 🇲🇪 ME | 2359 |
| 29 | 🇳🇱 NL | 2264 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5176 |
| 2 | Denver International Airport |  | US | 4053 |
| 3 | Indira Gandhi International Airport |  | IN | 3052 |
| 4 | Tokyo International Airport |  | JP | 2948 |
| 5 | Guaymaral Airport |  | CO | 2738 |
| 6 | Harry Reid International Airport |  | US | 2667 |
| 7 | Zurich Airport |  | CH | 2624 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2542 |
| 9 | El Dorado International Airport |  | CO | 2537 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2482 |
| 11 | La Aurora Airport |  | GT | 2390 |
| 12 | Salt Lake City International Airport |  | US | 2215 |
| 13 | Chicago O'Hare International Airport |  | US | 2186 |
| 14 | Congonhas Airport |  | BR | 2147 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2060 |
| 16 | Capua Airport |  | IT | 1976 |
| 17 | Madrid Barajas International Airport |  | ES | 1973 |
| 18 | Frankfurt am Main International Airport |  | DE | 1957 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1880 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1824 |
| 21 | Malpensa International Airport |  | IT | 1802 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1759 |
| 23 | Charles de Gaulle International Airport |  | FR | 1756 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1746 |
| 25 | Ninoy Aquino International Airport |  | PH | 1661 |
| 26 | Macau International Airport |  | MO | 1648 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1646 |
| 28 | Charlotte/Douglas International Airport |  | US | 1586 |
| 29 | Barcelona International Airport |  | ES | 1585 |
| 30 | Kuala Lumpur International Airport |  | MY | 1574 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1535 |
| 32 | Viracopos International Airport |  | BR | 1496 |
| 33 | Seattle-Tacoma International Airport |  | US | 1477 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1452 |
| 35 | Don Mueang International Airport |  | TH | 1446 |
| 36 | Calgary International Airport |  | CA | 1440 |
| 37 | Bengaluru International Airport |  | IN | 1433 |
| 38 | Oslo Gardermoen Airport |  | NO | 1413 |
| 39 | Vancouver International Airport |  | CA | 1400 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1359 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 931 | 21m | 244 km | 3,920.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 660 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 635 | 24m | 225 km | 2,463.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 629 | 1h 6m | 770 km | 8,355.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 563 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 411 | 27m | 275 km | 1,947.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 400 | 1h 50m | 1,423 km | 9,816.6 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 391 | 44m | 555 km | 3,744.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 373 | 44m | 241 km | 1,549.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 352 | 21m | 250 km | 1,520.4 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 349 | 24m | 218 km | 1,314.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 335 | 23m | 55 km | 318.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 310 | 26m | 215 km | 1,148.1 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 291 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 288 | 19m | 144 km | 716.4 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 257 | 41m | 535 km | 2,373.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5866Q |  | Dallas Executive Airport (KRBD) | David Wayne Hooks Memorial Airport (KDWH) | 2026-09-07 15:30 UTC | 2026-09-07 16:55 UTC | 1h 25m |
| N359SP |  | Lemons Field (2ID6) | Ontario Municipal Airport (KONO) | 2026-09-07 16:23 UTC | 2026-09-07 16:54 UTC | 30m |
| N9993E |  | Pratermill Flight Park Airport (GA72) | Flying G Ranch Airport (86GA) | 2026-09-07 16:42 UTC | 2026-09-07 16:53 UTC | 10m |
| N122Q |  | Stoltzfus Airfield (OH22) | Stoltzfus Airfield (OH22) | 2026-09-07 16:36 UTC | 2026-09-07 16:52 UTC | 15m |
| N40JF |  | 0OI4 (0OI4) | 1OI1 (1OI1) | 2026-09-07 16:30 UTC | 2026-09-07 16:42 UTC | 12m |
| N6033F |  | Kyle-Oakley Field (KCEY) | Kyle-Oakley Field (KCEY) | 2026-09-07 16:41 UTC | 2026-09-07 16:41 UTC | 0m |
| N682AC |  | Bb Airpark (TE88) | Bb Airpark (TE88) | 2026-09-07 15:37 UTC | 2026-09-07 16:37 UTC | 1h 0m |
| IGO1164 | IndiGo | Singapore Changi International Airport (WSSS) | Pune Airport (VAPO) | 2026-09-07 11:52 UTC | 2026-09-07 16:37 UTC | 4h 44m |
| T857 |  | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-09-07 15:00 UTC | 2026-09-07 16:36 UTC | 1h 35m |
| CXK276 | CXK | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-09-07 16:11 UTC | 2026-09-07 16:35 UTC | 24m |
| IGO19K | IndiGo | Dubai International Airport (OMDB) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-07 14:04 UTC | 2026-09-07 16:35 UTC | 2h 31m |
| ITDUE | ITD | Olbia / Costa Smeralda Airport (LIEO) | Alghero / Fertilia Airport (LIEA) | 2026-09-07 16:19 UTC | 2026-09-07 16:30 UTC | 10m |
| TJT37DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-09-07 15:14 UTC | 2026-09-07 16:30 UTC | 1h 15m |
| N859A |  | Capital City Airport (KCXY) | Capital City Airport (KCXY) | 2026-09-07 15:47 UTC | 2026-09-07 16:29 UTC | 41m |
| N41101 |  | Summit Airport (PAST) | Helio Airport (2AK7) | 2026-09-07 16:11 UTC | 2026-09-07 16:28 UTC | 17m |
| N974CS |  | Summit Airport (PAST) | Summit Airport (PAST) | 2026-09-07 16:11 UTC | 2026-09-07 16:24 UTC | 13m |
| MGL138 | MGL | Frankfurt am Main International Airport (EDDF) | Ukhta Airport (UUYH) | 2026-09-07 12:56 UTC | 2026-09-07 16:24 UTC | 3h 27m |
| N814SS |  | Kenai Municipal Airport (PAEN) | Trading Bay Production Airport (5AK0) | 2026-09-07 16:08 UTC | 2026-09-07 16:21 UTC | 12m |
| JANET09 | JAN | Harry Reid International Airport (KLAS) | Tonopah Test Range (KTNX) | 2026-09-07 15:50 UTC | 2026-09-07 16:19 UTC | 28m |
| LVRCZ | LVR | Mariano Moreno Airport (SADJ) | Mariano Moreno Airport (SADJ) | 2026-09-07 16:02 UTC | 2026-09-07 16:19 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
