# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_06:02:09_UTC-green)

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

**Latest saved flight:** 2026-08-31 06:02:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-31 06:02:09 UTC

- **242,511** saved flights
- **73,475** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **242,511** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,919,019.8 tonnes** estimated CO2 emissions
- **169,218,540 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9730 |
| 2 | SkyWest Airlines | 8507 |
| 3 | EJA | 4695 |
| 4 | IndiGo | 4079 |
| 5 | American Airlines | 3903 |
| 6 | Southwest Airlines | 3643 |
| 7 | Delta Air Lines | 3093 |
| 8 | ENY | 2924 |
| 9 | LATAM Airlines | 2322 |
| 10 | AZU | 2248 |
| 11 | Vueling | 2081 |
| 12 | Lufthansa | 1950 |
| 13 | WIF | 1923 |
| 14 | LXJ | 1878 |
| 15 | easyJet | 1690 |
| 16 | Swiss International | 1637 |
| 17 | AXM | 1601 |
| 18 | EJU | 1550 |
| 19 | QLK | 1550 |
| 20 | United Airlines | 1525 |
| 21 | Alaska Airlines | 1451 |
| 22 | All Nippon Airways | 1434 |
| 23 | WMT | 1364 |
| 24 | GLO | 1353 |
| 25 | VIV | 1330 |
| 26 | PGT | 1327 |
| 27 | Air France | 1323 |
| 28 | Wizz Air | 1311 |
| 29 | AEE | 1200 |
| 30 | JetBlue | 1198 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 200968 |
| 2 | 🇪🇸 ES | 15586 |
| 3 | 🇧🇷 BR | 14115 |
| 4 | 🇦🇺 AU | 13785 |
| 5 | 🇨🇦 CA | 13493 |
| 6 | 🇮🇹 IT | 13279 |
| 7 | 🇮🇳 IN | 12701 |
| 8 | 🇩🇪 DE | 11961 |
| 9 | 🇬🇧 GB | 11439 |
| 10 | 🇨🇴 CO | 10466 |
| 11 | 🇫🇷 FR | 9763 |
| 12 | 🇯🇵 JP | 9717 |
| 13 | 🇹🇷 TR | 7193 |
| 14 | 🇬🇷 GR | 7151 |
| 15 | 🇲🇽 MX | 6692 |
| 16 | 🇨🇭 CH | 6515 |
| 17 | 🇳🇴 NO | 5992 |
| 18 | 🇹🇭 TH | 4395 |
| 19 | 🇲🇾 MY | 4294 |
| 20 | 🇿🇦 ZA | 4227 |
| 21 | 🇵🇱 PL | 4071 |
| 22 | 🇳🇿 NZ | 3340 |
| 23 | 🇵🇭 PH | 3325 |
| 24 | 🇬🇹 GT | 3050 |
| 25 | 🇰🇷 KR | 2860 |
| 26 | 🇭🇷 HR | 2797 |
| 27 | 🇲🇦 MA | 2457 |
| 28 | 🇲🇪 ME | 2265 |
| 29 | 🇳🇱 NL | 2192 |
| 30 | 🇮🇩 ID | 2118 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5011 |
| 2 | Denver International Airport |  | US | 3909 |
| 3 | Indira Gandhi International Airport |  | IN | 2959 |
| 4 | Tokyo International Airport |  | JP | 2892 |
| 5 | Guaymaral Airport |  | CO | 2705 |
| 6 | Harry Reid International Airport |  | US | 2574 |
| 7 | Zurich Airport |  | CH | 2549 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2480 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2418 |
| 10 | El Dorado International Airport |  | CO | 2372 |
| 11 | La Aurora Airport |  | GT | 2322 |
| 12 | Chicago O'Hare International Airport |  | US | 2149 |
| 13 | Salt Lake City International Airport |  | US | 2142 |
| 14 | Congonhas Airport |  | BR | 2066 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2009 |
| 16 | Frankfurt am Main International Airport |  | DE | 1920 |
| 17 | Capua Airport |  | IT | 1912 |
| 18 | Madrid Barajas International Airport |  | ES | 1905 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1818 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1784 |
| 21 | Malpensa International Airport |  | IT | 1734 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1712 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1703 |
| 24 | Charles de Gaulle International Airport |  | FR | 1695 |
| 25 | Macau International Airport |  | MO | 1618 |
| 26 | Ninoy Aquino International Airport |  | PH | 1616 |
| 27 | Charlotte/Douglas International Airport |  | US | 1551 |
| 28 | Enrique Olaya Herrera Airport |  | CO | 1549 |
| 29 | Kuala Lumpur International Airport |  | MY | 1549 |
| 30 | Barcelona International Airport |  | ES | 1544 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1466 |
| 32 | Viracopos International Airport |  | BR | 1438 |
| 33 | Seattle-Tacoma International Airport |  | US | 1422 |
| 34 | Don Mueang International Airport |  | TH | 1415 |
| 35 | Bengaluru International Airport |  | IN | 1409 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1408 |
| 37 | Calgary International Airport |  | CA | 1393 |
| 38 | Oslo Gardermoen Airport |  | NO | 1365 |
| 39 | Vancouver International Airport |  | CA | 1346 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1322 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1096 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 895 | 21m | 244 km | 3,768.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 625 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 617 | 24m | 225 km | 2,393.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 614 | 1h 6m | 770 km | 8,156.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 546 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 399 | 27m | 275 km | 1,890.7 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 382 | 1h 50m | 1,423 km | 9,374.9 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 371 | 44m | 555 km | 3,552.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 366 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 354 | 44m | 241 km | 1,470.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 346 | 21m | 250 km | 1,494.5 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 333 | 24m | 218 km | 1,254.5 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 322 | 1h 40m | 1,156 km | 6,423.8 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 301 | 19m | 99 km | 515.6 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 295 | 26m | 215 km | 1,092.6 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 286 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 281 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 278 | 1h 14m | 961 km | 4,608.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 274 | 19m | 144 km | 681.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 265 | 15m | 154 km | 702.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 261 | 1h 50m | 1,304 km | 5,871.8 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YGI | YGI | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-08-31 05:17 UTC | 2026-08-31 06:02 UTC | 45m |
| CAN24 | CAN | Trapani / Birgi Airport (LICT) | Reggio Calabria Airport (LICR) | 2026-08-31 05:23 UTC | 2026-08-31 06:00 UTC | 37m |
| NOZ802 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Stockholm-Arlanda Airport (ESSA) | 2026-08-31 05:15 UTC | 2026-08-31 05:58 UTC | 42m |
| APJ927 | APJ | Naha Airport (ROAH) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-31 04:39 UTC | 2026-08-31 05:45 UTC | 1h 5m |
| UPG | UPG | Melbourne Moorabbin Airport (YMMB) | Tyabb Airport (YTYA) | 2026-08-31 05:17 UTC | 2026-08-31 05:32 UTC | 14m |
| FIN37N | Finnair | Helsinki Vantaa Airport (EFHK) | Kemi-Tornio Airport (EFKE) | 2026-08-31 04:15 UTC | 2026-08-31 05:30 UTC | 1h 14m |
| WIF57H | WIF | Mo i Rana Airport Rossvoll (ENRA) | Trondheim Airport Vaernes (ENVA) | 2026-08-31 04:28 UTC | 2026-08-31 05:26 UTC | 58m |
| BHA703 | BHA | Tribhuvan International Airport (VNKT) | Thamkharka Airport (VNTH) | 2026-08-31 04:55 UTC | 2026-08-31 05:24 UTC | 28m |
| VTCVV | VTC | Indira Gandhi International Airport (VIDP) | Shimla Airport (VISM) | 2026-08-31 04:56 UTC | 2026-08-31 05:20 UTC | 24m |
| AIQ3209 | AIQ | Don Mueang International Airport (VTBD) | Kengtung Airport (VYKG) | 2026-08-31 04:30 UTC | 2026-08-31 05:20 UTC | 50m |
| N626Q |  | Skypark Airport (KBTF) | Malad City Airport (KMLD) | 2026-08-31 04:23 UTC | 2026-08-31 05:15 UTC | 51m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-08-31 04:31 UTC | 2026-08-31 05:15 UTC | 43m |
| FR126 |  | Al Ain International Airport (OMAL) | Al Minhad Air Base (OMDM) | 2026-08-31 04:52 UTC | 2026-08-31 05:11 UTC | 19m |
| RXA2125 | RXA | Perth International Airport (YPPH) | Frankland Airport (YFRK) | 2026-08-31 04:31 UTC | 2026-08-31 05:09 UTC | 38m |
| DLH6EJ | Lufthansa | Billund Airport (EKBI) | Frankfurt am Main International Airport (EDDF) | 2026-08-31 04:03 UTC | 2026-08-31 05:08 UTC | 1h 4m |
| IGO573E | IndiGo | Juhu Aerodrome (VAJJ) | Dehradun Airport (VIDN) | 2026-08-31 03:19 UTC | 2026-08-31 05:03 UTC | 1h 44m |
| 5YZBP |  | Nairobi Wilson Airport (HKNW) | Narok Airport (HKNO) | 2026-08-31 04:34 UTC | 2026-08-31 05:02 UTC | 28m |
| ACA155 | Air Canada | Toronto Pearson International Airport (CYYZ) | Calgary International Airport (CYYC) | 2026-08-31 01:10 UTC | 2026-08-31 05:02 UTC | 3h 51m |
| RYR45TN | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Bari / Palese International Airport (LIBD) | 2026-08-31 04:06 UTC | 2026-08-31 05:02 UTC | 55m |
| DLH5JV | Lufthansa | Leipzig Halle Airport (EDDP) | Frankfurt am Main International Airport (EDDF) | 2026-08-31 04:22 UTC | 2026-08-31 05:01 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
