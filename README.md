# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_20:06:54_UTC-green)

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

**Latest saved flight:** 2026-09-17 20:06:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-17 20:06:54 UTC

- **261,556** saved flights
- **77,451** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **261,556** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,167,392.8 tonnes** estimated CO2 emissions
- **183,616,975 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10358 |
| 2 | SkyWest Airlines | 9113 |
| 3 | EJA | 5071 |
| 4 | IndiGo | 4385 |
| 5 | American Airlines | 4107 |
| 6 | Southwest Airlines | 3843 |
| 7 | Delta Air Lines | 3268 |
| 8 | ENY | 3091 |
| 9 | LATAM Airlines | 2521 |
| 10 | AZU | 2453 |
| 11 | Vueling | 2203 |
| 12 | WIF | 2111 |
| 13 | LXJ | 2043 |
| 14 | Lufthansa | 2028 |
| 15 | easyJet | 1772 |
| 16 | Swiss International | 1735 |
| 17 | QLK | 1688 |
| 18 | AXM | 1651 |
| 19 | EJU | 1649 |
| 20 | United Airlines | 1606 |
| 21 | Alaska Airlines | 1551 |
| 22 | All Nippon Airways | 1515 |
| 23 | WMT | 1474 |
| 24 | GLO | 1459 |
| 25 | PGT | 1459 |
| 26 | Air France | 1435 |
| 27 | VIV | 1430 |
| 28 | Wizz Air | 1420 |
| 29 | TKR | 1275 |
| 30 | AEE | 1264 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 217260 |
| 2 | 🇪🇸 ES | 16531 |
| 3 | 🇧🇷 BR | 15308 |
| 4 | 🇦🇺 AU | 14968 |
| 5 | 🇨🇦 CA | 14569 |
| 6 | 🇮🇹 IT | 14235 |
| 7 | 🇮🇳 IN | 13831 |
| 8 | 🇩🇪 DE | 12668 |
| 9 | 🇬🇧 GB | 12157 |
| 10 | 🇨🇴 CO | 11797 |
| 11 | 🇫🇷 FR | 10467 |
| 12 | 🇯🇵 JP | 10153 |
| 13 | 🇹🇷 TR | 7898 |
| 14 | 🇬🇷 GR | 7589 |
| 15 | 🇲🇽 MX | 7203 |
| 16 | 🇨🇭 CH | 6998 |
| 17 | 🇳🇴 NO | 6461 |
| 18 | 🇹🇭 TH | 4685 |
| 19 | 🇲🇾 MY | 4450 |
| 20 | 🇿🇦 ZA | 4420 |
| 21 | 🇵🇱 PL | 4318 |
| 22 | 🇳🇿 NZ | 3623 |
| 23 | 🇵🇭 PH | 3494 |
| 24 | 🇬🇹 GT | 3332 |
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
| 2 | Denver International Airport |  | US | 4233 |
| 3 | Indira Gandhi International Airport |  | IN | 3145 |
| 4 | Tokyo International Airport |  | JP | 3030 |
| 5 | Harry Reid International Airport |  | US | 2778 |
| 6 | Guaymaral Airport |  | CO | 2777 |
| 7 | El Dorado International Airport |  | CO | 2753 |
| 8 | Zurich Airport |  | CH | 2731 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2635 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2538 |
| 11 | La Aurora Airport |  | GT | 2529 |
| 12 | Salt Lake City International Airport |  | US | 2311 |
| 13 | Chicago O'Hare International Airport |  | US | 2261 |
| 14 | Congonhas Airport |  | BR | 2235 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2135 |
| 16 | Capua Airport |  | IT | 2043 |
| 17 | Madrid Barajas International Airport |  | ES | 2026 |
| 18 | Frankfurt am Main International Airport |  | DE | 1998 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1972 |
| 20 | Malpensa International Airport |  | IT | 1884 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1877 |
| 22 | Charles de Gaulle International Airport |  | FR | 1848 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1843 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1795 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1795 |
| 26 | Macau International Airport |  | MO | 1733 |
| 27 | Ninoy Aquino International Airport |  | PH | 1714 |
| 28 | Barcelona International Airport |  | ES | 1632 |
| 29 | Charlotte/Douglas International Airport |  | US | 1629 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1611 |
| 31 | Kuala Lumpur International Airport |  | MY | 1597 |
| 32 | Viracopos International Airport |  | BR | 1584 |
| 33 | Seattle-Tacoma International Airport |  | US | 1533 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1522 |
| 35 | Don Mueang International Airport |  | TH | 1495 |
| 36 | Calgary International Airport |  | CA | 1494 |
| 37 | Bengaluru International Airport |  | IN | 1484 |
| 38 | Oslo Gardermoen Airport |  | NO | 1471 |
| 39 | Vancouver International Airport |  | CA | 1465 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1401 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1112 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 976 | 21m | 244 km | 4,109.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 711 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 656 | 1h 6m | 770 km | 8,714.5 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 653 | 24m | 225 km | 2,533.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 585 | 12m | - | - |
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
| HCCRE | HCC | Santo Domingo de Los Colorados Airport (SESD) | Nuevo Aeropuerto Internacional Mariscal Sucre (SEQM) | 2026-09-17 17:22 UTC | 2026-09-17 20:06 UTC | 2h 44m |
| CFIAQ | CFI | CEB4 (CEB4) | CEB4 (CEB4) | 2026-09-17 19:11 UTC | 2026-09-17 20:01 UTC | 50m |
| STW011 | STW | Isparta Airport (LTBM) | Smolensk North Airport (XUBS) | 2026-09-17 17:33 UTC | 2026-09-17 20:01 UTC | 2h 27m |
| N447BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-09-17 19:01 UTC | 2026-09-17 19:59 UTC | 58m |
| N1737A |  | Camp Bullis Als (Cals) Airport (9TX5) | New Braunfels Ntl Airport (KBAZ) | 2026-09-17 19:28 UTC | 2026-09-17 19:58 UTC | 30m |
| N264FA |  | Wings Field (KLOM) | Lehigh Valley International Airport (KABE) | 2026-09-17 19:25 UTC | 2026-09-17 19:58 UTC | 32m |
| EB638 |  | Whiting Field Nas South Airport (KNDZ) | 93FD (93FD) | 2026-09-17 19:45 UTC | 2026-09-17 19:57 UTC | 11m |
| HK2899 |  | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-09-17 19:43 UTC | 2026-09-17 19:56 UTC | 13m |
| YETI44 | YET | Jewell Airport (AK72) | Elmendorf Afb Airport (PAED) | 2026-09-17 18:45 UTC | 2026-09-17 19:53 UTC | 1h 8m |
| N44605 |  | Columbus Airport (KCSG) | Columbus Airport (KCSG) | 2026-09-17 19:51 UTC | 2026-09-17 19:53 UTC | 2m |
| LSXX | LSX | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-17 19:17 UTC | 2026-09-17 19:53 UTC | 35m |
| BOX542 | BOX | Suvarnabhumi Airport (VTBS) | Zhuhai Airport (ZGSD) | 2026-09-17 17:43 UTC | 2026-09-17 19:51 UTC | 2h 7m |
| ZPBLB | ZPB | Bella Vista Sur Airport (SGBA) | Encarnacion Airport (SGEN) | 2026-09-17 19:29 UTC | 2026-09-17 19:49 UTC | 20m |
| PREMK | PRE | Americana Airport (SDAI) | Americana Airport (SDAI) | 2026-09-17 19:46 UTC | 2026-09-17 19:49 UTC | 2m |
| CXK114 | CXK | Mesa Gateway Airport (KIWA) | Chandler Municipal Airport (KCHD) | 2026-09-17 18:56 UTC | 2026-09-17 19:49 UTC | 52m |
| FTO381 | FTO | Essex County Airport (KCDW) | Laguardia Airport (KLGA) | 2026-09-17 19:36 UTC | 2026-09-17 19:47 UTC | 11m |
| CXK1080 | CXK | Concord-Padgett Regional Airport (KJQF) | Flying S Ranch Airport (0NC8) | 2026-09-17 19:29 UTC | 2026-09-17 19:46 UTC | 16m |
| NORTH48 | NOR | Elmendorf Afb Airport (PAED) | Port Clarence Cgs Airport (PAPC) | 2026-09-17 17:28 UTC | 2026-09-17 19:46 UTC | 2h 18m |
| N66VG |  | Sacramento Mather Airport (KMHR) | Hayward Executive Airport (KHWD) | 2026-09-17 19:07 UTC | 2026-09-17 19:43 UTC | 35m |
| QTR8410 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-09-17 12:16 UTC | 2026-09-17 19:41 UTC | 7h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
