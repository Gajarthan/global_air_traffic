# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_22:43:58_UTC-green)

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

**Latest saved flight:** 2026-09-17 22:43:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-17 22:43:58 UTC

- **261,739** saved flights
- **77,496** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **261,739** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,170,718.8 tonnes** estimated CO2 emissions
- **183,809,785 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10364 |
| 2 | SkyWest Airlines | 9119 |
| 3 | EJA | 5077 |
| 4 | IndiGo | 4385 |
| 5 | American Airlines | 4109 |
| 6 | Southwest Airlines | 3844 |
| 7 | Delta Air Lines | 3271 |
| 8 | ENY | 3091 |
| 9 | LATAM Airlines | 2523 |
| 10 | AZU | 2455 |
| 11 | Vueling | 2204 |
| 12 | WIF | 2111 |
| 13 | LXJ | 2048 |
| 14 | Lufthansa | 2028 |
| 15 | easyJet | 1772 |
| 16 | Swiss International | 1735 |
| 17 | QLK | 1689 |
| 18 | AXM | 1651 |
| 19 | EJU | 1650 |
| 20 | United Airlines | 1608 |
| 21 | Alaska Airlines | 1553 |
| 22 | All Nippon Airways | 1515 |
| 23 | WMT | 1474 |
| 24 | GLO | 1463 |
| 25 | PGT | 1460 |
| 26 | Air France | 1435 |
| 27 | VIV | 1430 |
| 28 | Wizz Air | 1420 |
| 29 | TKR | 1275 |
| 30 | AEE | 1264 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 217460 |
| 2 | 🇪🇸 ES | 16534 |
| 3 | 🇧🇷 BR | 15325 |
| 4 | 🇦🇺 AU | 14980 |
| 5 | 🇨🇦 CA | 14576 |
| 6 | 🇮🇹 IT | 14246 |
| 7 | 🇮🇳 IN | 13835 |
| 8 | 🇩🇪 DE | 12669 |
| 9 | 🇬🇧 GB | 12161 |
| 10 | 🇨🇴 CO | 11808 |
| 11 | 🇫🇷 FR | 10468 |
| 12 | 🇯🇵 JP | 10155 |
| 13 | 🇹🇷 TR | 7901 |
| 14 | 🇬🇷 GR | 7590 |
| 15 | 🇲🇽 MX | 7211 |
| 16 | 🇨🇭 CH | 6999 |
| 17 | 🇳🇴 NO | 6463 |
| 18 | 🇹🇭 TH | 4685 |
| 19 | 🇲🇾 MY | 4450 |
| 20 | 🇿🇦 ZA | 4420 |
| 21 | 🇵🇱 PL | 4320 |
| 22 | 🇳🇿 NZ | 3631 |
| 23 | 🇵🇭 PH | 3496 |
| 24 | 🇬🇹 GT | 3340 |
| 25 | 🇭🇷 HR | 2988 |
| 26 | 🇰🇷 KR | 2980 |
| 27 | 🇲🇦 MA | 2617 |
| 28 | 🇲🇪 ME | 2462 |
| 29 | 🇳🇱 NL | 2336 |
| 30 | 🇮🇩 ID | 2208 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5360 |
| 2 | Denver International Airport |  | US | 4235 |
| 3 | Indira Gandhi International Airport |  | IN | 3145 |
| 4 | Tokyo International Airport |  | JP | 3031 |
| 5 | Harry Reid International Airport |  | US | 2781 |
| 6 | Guaymaral Airport |  | CO | 2777 |
| 7 | El Dorado International Airport |  | CO | 2756 |
| 8 | Zurich Airport |  | CH | 2732 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2637 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2538 |
| 11 | La Aurora Airport |  | GT | 2537 |
| 12 | Salt Lake City International Airport |  | US | 2311 |
| 13 | Chicago O'Hare International Airport |  | US | 2261 |
| 14 | Congonhas Airport |  | BR | 2237 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2137 |
| 16 | Capua Airport |  | IT | 2045 |
| 17 | Madrid Barajas International Airport |  | ES | 2026 |
| 18 | Frankfurt am Main International Airport |  | DE | 1998 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1977 |
| 20 | Malpensa International Airport |  | IT | 1885 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1879 |
| 22 | Charles de Gaulle International Airport |  | FR | 1849 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1843 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1796 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1796 |
| 26 | Macau International Airport |  | MO | 1738 |
| 27 | Ninoy Aquino International Airport |  | PH | 1715 |
| 28 | Barcelona International Airport |  | ES | 1634 |
| 29 | Charlotte/Douglas International Airport |  | US | 1631 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1611 |
| 31 | Kuala Lumpur International Airport |  | MY | 1597 |
| 32 | Viracopos International Airport |  | BR | 1585 |
| 33 | Seattle-Tacoma International Airport |  | US | 1537 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1522 |
| 35 | Don Mueang International Airport |  | TH | 1495 |
| 36 | Calgary International Airport |  | CA | 1495 |
| 37 | Bengaluru International Airport |  | IN | 1485 |
| 38 | Oslo Gardermoen Airport |  | NO | 1471 |
| 39 | Vancouver International Airport |  | CA | 1465 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1401 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1112 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 976 | 21m | 244 km | 4,109.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 711 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 657 | 1h 6m | 770 km | 8,727.7 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 654 | 24m | 225 km | 2,537.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 588 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 424 | 27m | 275 km | 2,009.2 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 423 | 44m | 555 km | 4,050.4 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 399 | 44m | 241 km | 1,657.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 368 | 24m | 218 km | 1,386.4 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 359 | 21m | 250 km | 1,550.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 329 | 1h 6m | 706 km | 4,005.6 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 327 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 323 | 26m | 215 km | 1,196.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 321 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 302 | 1h 14m | 961 km | 5,005.8 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 302 | 19m | 144 km | 751.2 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 282 | 1h 50m | 1,304 km | 6,344.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 278 | 42m | 535 km | 2,567.5 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 278 | 28m | 152 km | 726.5 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OSU54 | OSU | Ohio State University Airport (KOSU) | Delaware Municipal/Jim Moore Field (KDLZ) | 2026-09-17 22:31 UTC | 2026-09-17 22:43 UTC | 12m |
| TAY534 | TAY | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-09-17 15:27 UTC | 2026-09-17 22:40 UTC | 7h 12m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-09-17 11:57 UTC | 2026-09-17 22:37 UTC | 10h 39m |
| ICL851 | ICL | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-09-17 13:33 UTC | 2026-09-17 22:33 UTC | 8h 59m |
| YGF | YGF | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-17 22:02 UTC | 2026-09-17 22:31 UTC | 29m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Zhuhai Airport (ZGSD) | 2026-09-17 11:16 UTC | 2026-09-17 22:30 UTC | 11h 14m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Macau International Airport (VMMC) | 2026-09-17 12:03 UTC | 2026-09-17 22:27 UTC | 10h 24m |
| VE11 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-17 21:14 UTC | 2026-09-17 22:27 UTC | 1h 12m |
| AIC2290 | Air India | Hamad International Airport (OTHH) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-17 19:23 UTC | 2026-09-17 22:26 UTC | 3h 3m |
| SND4 | SND | Corowa Airport (YCOR) | Corowa Airport (YCOR) | 2026-09-17 22:08 UTC | 2026-09-17 22:26 UTC | 18m |
| CPA294 | Cathay Pacific | Melsbroek Air Base (EBMB) | Macau International Airport (VMMC) | 2026-09-17 11:26 UTC | 2026-09-17 22:25 UTC | 10h 59m |
| CGCNR | CGC | John Wayne/Orange County Airport (KSNA) | Calgary International Airport (CYYC) | 2026-09-17 19:55 UTC | 2026-09-17 22:25 UTC | 2h 30m |
| AIC128 | Air India | London Heathrow Airport (EGLL) | Pune Airport (VAPO) | 2026-09-17 13:16 UTC | 2026-09-17 22:24 UTC | 9h 8m |
| YNV | YNV | Toowoomba Airport (YTWB) | Sunshine Coast Airport (YBMC) | 2026-09-17 21:29 UTC | 2026-09-17 22:23 UTC | 53m |
| N737CX |  | Daytona Beach International Airport (KDAB) | Arthur Dunn Air Park (KX21) | 2026-09-17 21:56 UTC | 2026-09-17 22:20 UTC | 24m |
| UAE9790 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-09-17 15:31 UTC | 2026-09-17 22:20 UTC | 6h 49m |
| BCS692 | BCS | Bengaluru International Airport (VOBL) | Zhuhai Airport (ZGSD) | 2026-09-17 17:02 UTC | 2026-09-17 22:18 UTC | 5h 16m |
| N415SP |  | Pompano Beach Airpark (KPMP) | Melbourne Orlando International Airport (KMLB) | 2026-09-17 20:27 UTC | 2026-09-17 22:14 UTC | 1h 47m |
| N688CB |  | Teterboro Airport (KTEB) | Laurence G Hanscom Field (KBED) | 2026-09-17 21:37 UTC | 2026-09-17 22:14 UTC | 36m |
| BRG2652 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-09-17 21:36 UTC | 2026-09-17 22:13 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
