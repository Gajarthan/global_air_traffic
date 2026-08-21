# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_08:40:36_UTC-green)

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

**Latest saved flight:** 2026-08-21 08:40:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 08:40:36 UTC

- **221,503** saved flights
- **69,394** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **221,503** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,666,043.7 tonnes** estimated CO2 emissions
- **154,553,255 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8870 |
| 2 | SkyWest Airlines | 7891 |
| 3 | EJA | 4289 |
| 4 | IndiGo | 3753 |
| 5 | American Airlines | 3670 |
| 6 | Southwest Airlines | 3491 |
| 7 | Delta Air Lines | 2852 |
| 8 | ENY | 2724 |
| 9 | LATAM Airlines | 2103 |
| 10 | AZU | 2032 |
| 11 | Vueling | 1863 |
| 12 | Lufthansa | 1831 |
| 13 | WIF | 1770 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1530 |
| 16 | Swiss International | 1471 |
| 17 | AXM | 1461 |
| 18 | QLK | 1399 |
| 19 | United Airlines | 1390 |
| 20 | EJU | 1382 |
| 21 | Alaska Airlines | 1353 |
| 22 | All Nippon Airways | 1328 |
| 23 | GLO | 1211 |
| 24 | PGT | 1207 |
| 25 | VIV | 1206 |
| 26 | Air France | 1197 |
| 27 | WMT | 1170 |
| 28 | Wizz Air | 1129 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1107 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186295 |
| 2 | 🇪🇸 ES | 14186 |
| 3 | 🇧🇷 BR | 12790 |
| 4 | 🇦🇺 AU | 12623 |
| 5 | 🇨🇦 CA | 12245 |
| 6 | 🇮🇹 IT | 11769 |
| 7 | 🇮🇳 IN | 11702 |
| 8 | 🇩🇪 DE | 10919 |
| 9 | 🇬🇧 GB | 10369 |
| 10 | 🇨🇴 CO | 9102 |
| 11 | 🇯🇵 JP | 9011 |
| 12 | 🇫🇷 FR | 8801 |
| 13 | 🇬🇷 GR | 6459 |
| 14 | 🇹🇷 TR | 6383 |
| 15 | 🇲🇽 MX | 6157 |
| 16 | 🇨🇭 CH | 5842 |
| 17 | 🇳🇴 NO | 5497 |
| 18 | 🇲🇾 MY | 3867 |
| 19 | 🇿🇦 ZA | 3777 |
| 20 | 🇹🇭 TH | 3716 |
| 21 | 🇵🇱 PL | 3669 |
| 22 | 🇳🇿 NZ | 3089 |
| 23 | 🇵🇭 PH | 3011 |
| 24 | 🇬🇹 GT | 2793 |
| 25 | 🇰🇷 KR | 2643 |
| 26 | 🇭🇷 HR | 2453 |
| 27 | 🇲🇦 MA | 2221 |
| 28 | 🇳🇱 NL | 1965 |
| 29 | 🇲🇪 ME | 1957 |
| 30 | 🇮🇩 ID | 1892 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4649 |
| 2 | Denver International Airport |  | US | 3615 |
| 3 | Tokyo International Airport |  | JP | 2704 |
| 4 | Indira Gandhi International Airport |  | IN | 2689 |
| 5 | Guaymaral Airport |  | CO | 2606 |
| 6 | Harry Reid International Airport |  | US | 2443 |
| 7 | Zurich Airport |  | CH | 2293 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2276 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2246 |
| 10 | La Aurora Airport |  | GT | 2128 |
| 11 | El Dorado International Airport |  | CO | 2073 |
| 12 | Chicago O'Hare International Airport |  | US | 2024 |
| 13 | Salt Lake City International Airport |  | US | 1948 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1909 |
| 15 | Congonhas Airport |  | BR | 1869 |
| 16 | Frankfurt am Main International Airport |  | DE | 1798 |
| 17 | Madrid Barajas International Airport |  | ES | 1734 |
| 18 | Capua Airport |  | IT | 1688 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1661 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1630 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1586 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1568 |
| 24 | Malpensa International Airport |  | IT | 1552 |
| 25 | Charles de Gaulle International Airport |  | FR | 1521 |
| 26 | Charlotte/Douglas International Airport |  | US | 1471 |
| 27 | Ninoy Aquino International Airport |  | PH | 1435 |
| 28 | Kuala Lumpur International Airport |  | MY | 1414 |
| 29 | Barcelona International Airport |  | ES | 1359 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1346 |
| 31 | Bengaluru International Airport |  | IN | 1328 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1315 |
| 33 | Seattle-Tacoma International Airport |  | US | 1313 |
| 34 | Viracopos International Airport |  | BR | 1299 |
| 35 | Calgary International Airport |  | CA | 1256 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1235 |
| 37 | Vitoria/Foronda Airport |  | ES | 1229 |
| 38 | Oslo Gardermoen Airport |  | NO | 1228 |
| 39 | Don Mueang International Airport |  | TH | 1222 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1189 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1064 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 800 | 21m | 244 km | 3,368.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 550 | 1h 7m | 770 km | 7,306.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 499 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 499 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 373 | 27m | 275 km | 1,767.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 351 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 328 | 1h 50m | 1,423 km | 8,049.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 324 | 44m | 241 km | 1,345.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 277 | 1h 38m | 1,156 km | 5,526.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 276 | 24m | 218 km | 1,039.8 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 273 | 19m | 99 km | 467.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 263 | 44m | 555 km | 2,518.3 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 252 | 19m | 144 km | 626.8 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 239 | 1h 49m | 1,304 km | 5,376.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NIVAL07 | NIV | Rota Naval Station Airport (LERT) | Rota Naval Station Airport (LERT) | 2026-08-21 08:06 UTC | 2026-08-21 08:40 UTC | 34m |
| DAL292 | Delta Air Lines | Detroit Metro Wayne County Airport (KDTW) | Dublin Airport (EIDW) | 2026-08-21 02:08 UTC | 2026-08-21 08:31 UTC | 6h 23m |
| J014KT |  | Adi Sutjipto International Airport (WARJ) | Adi Sutjipto International Airport (WARJ) | 2026-08-21 08:01 UTC | 2026-08-21 08:27 UTC | 25m |
| 3AMAX |  | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-21 08:14 UTC | 2026-08-21 08:26 UTC | 12m |
| WWF287 | WWF | Boise Air Trml/Gowen Field (KBOI) | OG12 (OG12) | 2026-08-21 05:56 UTC | 2026-08-21 08:23 UTC | 2h 26m |
| N988MD |  | Kota Kinabalu International Airport (WBKK) | Kota Kinabalu International Airport (WBKK) | 2026-08-21 08:01 UTC | 2026-08-21 08:19 UTC | 17m |
| R21231 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-21 06:26 UTC | 2026-08-21 08:18 UTC | 1h 51m |
| QTR650 | Qatar Airways | Hamad International Airport (OTHH) | Simara Airport (VNSI) | 2026-08-21 04:02 UTC | 2026-08-21 08:07 UTC | 4h 5m |
| AKJ590 | AKJ | Bengaluru International Airport (VOBL) | Al Ain International Airport (OMAL) | 2026-08-21 05:01 UTC | 2026-08-21 08:03 UTC | 3h 1m |
| BNO91J | BNO | Oslo Gardermoen Airport (ENGM) | Kristiansand Airport (ENCN) | 2026-08-21 07:32 UTC | 2026-08-21 08:03 UTC | 30m |
| HFA602 | HFA | LLYO (LLYO) | Haifa International Airport (LLHA) | 2026-08-21 07:07 UTC | 2026-08-21 07:57 UTC | 50m |
| WZZ4XM | Wizz Air | M. R. Stefanik Airport (LZIB) | Pristina International Airport (BKPR) | 2026-08-21 06:47 UTC | 2026-08-21 07:46 UTC | 59m |
| SUNDOG1 | SUN | Nordholz Airport (ETMN) | Gerstetten Airport (EDPT) | 2026-08-21 06:58 UTC | 2026-08-21 07:45 UTC | 47m |
| WIF8XA | WIF | Trondheim Airport Vaernes (ENVA) | Bardufoss Airport (ENDU) | 2026-08-21 06:28 UTC | 2026-08-21 07:43 UTC | 1h 14m |
| IGO5316 | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Pithorgarh Airport (VIDF) | 2026-08-21 05:52 UTC | 2026-08-21 07:42 UTC | 1h 49m |
| SDG234 | SDG | Hindon Airport (VIDX) | Chandigarh Airport (VICG) | 2026-08-21 07:09 UTC | 2026-08-21 07:39 UTC | 29m |
| VOE9TX | VOE | Sevilla Airport (LEZL) | La Morgal Airport (LEMR) | 2026-08-21 06:41 UTC | 2026-08-21 07:38 UTC | 57m |
| FIN489 | Finnair | Helsinki Vantaa Airport (EFHK) | Suomussalmi Airport (EFSU) | 2026-08-21 06:27 UTC | 2026-08-21 07:37 UTC | 1h 10m |
| FJJJY | FJJ | Saint-Nazaire-Montoir Airport (LFRZ) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-08-21 07:14 UTC | 2026-08-21 07:37 UTC | 22m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-08-21 07:16 UTC | 2026-08-21 07:36 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
