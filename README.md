# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_04:05:47_UTC-green)

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

**Latest saved flight:** 2026-08-23 04:05:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 04:05:47 UTC

- **227,569** saved flights
- **70,569** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **227,569** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,743,259.8 tonnes** estimated CO2 emissions
- **159,029,554 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9121 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4392 |
| 4 | IndiGo | 3841 |
| 5 | American Airlines | 3739 |
| 6 | Southwest Airlines | 3548 |
| 7 | Delta Air Lines | 2919 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2183 |
| 10 | AZU | 2110 |
| 11 | Vueling | 1925 |
| 12 | Lufthansa | 1860 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1579 |
| 16 | Swiss International | 1514 |
| 17 | AXM | 1500 |
| 18 | United Airlines | 1444 |
| 19 | EJU | 1435 |
| 20 | QLK | 1433 |
| 21 | Alaska Airlines | 1384 |
| 22 | All Nippon Airways | 1363 |
| 23 | GLO | 1264 |
| 24 | VIV | 1253 |
| 25 | PGT | 1251 |
| 26 | Air France | 1235 |
| 27 | WMT | 1229 |
| 28 | Wizz Air | 1178 |
| 29 | JetBlue | 1141 |
| 30 | AEE | 1130 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190611 |
| 2 | 🇪🇸 ES | 14567 |
| 3 | 🇧🇷 BR | 13288 |
| 4 | 🇦🇺 AU | 12861 |
| 5 | 🇨🇦 CA | 12608 |
| 6 | 🇮🇹 IT | 12213 |
| 7 | 🇮🇳 IN | 11963 |
| 8 | 🇩🇪 DE | 11181 |
| 9 | 🇬🇧 GB | 10688 |
| 10 | 🇨🇴 CO | 9384 |
| 11 | 🇯🇵 JP | 9237 |
| 12 | 🇫🇷 FR | 9094 |
| 13 | 🇹🇷 TR | 6679 |
| 14 | 🇬🇷 GR | 6643 |
| 15 | 🇲🇽 MX | 6355 |
| 16 | 🇨🇭 CH | 5996 |
| 17 | 🇳🇴 NO | 5601 |
| 18 | 🇲🇾 MY | 4002 |
| 19 | 🇿🇦 ZA | 3923 |
| 20 | 🇹🇭 TH | 3902 |
| 21 | 🇵🇱 PL | 3776 |
| 22 | 🇳🇿 NZ | 3161 |
| 23 | 🇵🇭 PH | 3103 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2693 |
| 26 | 🇭🇷 HR | 2568 |
| 27 | 🇲🇦 MA | 2296 |
| 28 | 🇲🇪 ME | 2053 |
| 29 | 🇳🇱 NL | 2027 |
| 30 | 🇮🇩 ID | 1960 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3713 |
| 3 | Tokyo International Airport |  | JP | 2761 |
| 4 | Indira Gandhi International Airport |  | IN | 2756 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2473 |
| 7 | Zurich Airport |  | CH | 2361 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2332 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2292 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2084 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2008 |
| 14 | Congonhas Airport |  | BR | 1939 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1937 |
| 16 | Frankfurt am Main International Airport |  | DE | 1823 |
| 17 | Madrid Barajas International Airport |  | ES | 1771 |
| 18 | Capua Airport |  | IT | 1761 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1702 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1698 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1647 |
| 22 | Malpensa International Airport |  | IT | 1614 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1599 |
| 24 | Macau International Airport |  | MO | 1594 |
| 25 | Charles de Gaulle International Airport |  | FR | 1573 |
| 26 | Charlotte/Douglas International Airport |  | US | 1491 |
| 27 | Ninoy Aquino International Airport |  | PH | 1485 |
| 28 | Kuala Lumpur International Airport |  | MY | 1452 |
| 29 | Barcelona International Airport |  | ES | 1413 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1382 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 32 | Viracopos International Airport |  | BR | 1347 |
| 33 | Bengaluru International Airport |  | IN | 1347 |
| 34 | Seattle-Tacoma International Airport |  | US | 1346 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Calgary International Airport |  | CA | 1298 |
| 37 | Don Mueang International Airport |  | TH | 1279 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1228 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 830 | 21m | 244 km | 3,494.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 567 | 1h 6m | 770 km | 7,532.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 558 | 24m | 225 km | 2,164.8 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 344 | 1h 50m | 1,423 km | 8,442.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 306 | 21m | 250 km | 1,321.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 294 | 44m | 555 km | 2,815.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 292 | 1h 38m | 1,156 km | 5,825.3 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 288 | 24m | 218 km | 1,085.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 259 | 19m | 144 km | 644.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CCA719 | Air China | Singapore Changi International Airport (WSSS) | Smolensk North Airport (XUBS) | 2026-08-22 12:33 UTC | 2026-08-23 04:05 UTC | 15h 32m |
| KAL2021 | Korean Air | Incheon International Airport (RKSI) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-23 01:59 UTC | 2026-08-23 03:55 UTC | 1h 56m |
| APG221 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-08-23 03:19 UTC | 2026-08-23 03:40 UTC | 20m |
| UBG187 | UBG | VGZR (VGZR) | Paro Airport (VQPR) | 2026-08-23 03:03 UTC | 2026-08-23 03:39 UTC | 35m |
| NIW | NIW | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-08-23 03:26 UTC | 2026-08-23 03:39 UTC | 12m |
| AAH54 | AAH | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-08-23 03:14 UTC | 2026-08-23 03:36 UTC | 21m |
| EPI436 | EPI | Glenmar Airport (TS11) | Majors Airport (KGVT) | 2026-08-23 03:02 UTC | 2026-08-23 03:34 UTC | 31m |
| UZB102 | UZB | John F Kennedy International Airport (KJFK) | Bezymyanka Airfield (UWWG) | 2026-08-22 18:28 UTC | 2026-08-23 03:34 UTC | 9h 5m |
| CCA2818 | Air China | Shenzhen Bao'an International Airport (ZGSZ) | Tianjin Binhai International Airport (ZBTJ) | 2026-08-23 00:48 UTC | 2026-08-23 03:33 UTC | 2h 45m |
| KBZ780 | KBZ | Imphal Airport (VEIM) | Pinlebu Airport (VYPL) | 2026-08-23 01:44 UTC | 2026-08-23 03:32 UTC | 1h 48m |
| AVA9567 | Avianca | Rafael Nunez International Airport (SKCG) | Jose Maria Cordova International Airport (SKRG) | 2026-08-23 02:46 UTC | 2026-08-23 03:31 UTC | 44m |
| JST890 | JST | Sydney Kingsford Smith International Airport (YSSY) | Hervey Bay Airport (YHBA) | 2026-08-23 02:17 UTC | 2026-08-23 03:29 UTC | 1h 12m |
| NOK322 | NOK | Don Mueang International Airport (VTBD) | Surin Airport (VTUJ) | 2026-08-23 02:56 UTC | 2026-08-23 03:29 UTC | 33m |
| AM376 |  | Melbourne Essendon Airport (YMEN) | West Sale Airport (YWSL) | 2026-08-23 03:02 UTC | 2026-08-23 03:27 UTC | 25m |
| LR8154 |  | Brisbane International Airport (YBBN) | Woodville Airport (YWVL) | 2026-08-23 02:36 UTC | 2026-08-23 03:24 UTC | 47m |
| THA205 | Thai Airways | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 2026-08-23 02:41 UTC | 2026-08-23 03:23 UTC | 42m |
| VIV4308 | VIV | General Mariano Escobedo International Airport (MMMY) | General Pedro Jose Mendez International Airport (MMCV) | 2026-08-23 03:01 UTC | 2026-08-23 03:23 UTC | 21m |
| UPEM022 | UPE | Seletar Airport (WSSL) | Noi Bai International Airport (VVNB) | 2026-08-23 00:13 UTC | 2026-08-23 03:22 UTC | 3h 9m |
| RXA6123 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-08-23 02:36 UTC | 2026-08-23 03:17 UTC | 41m |
| ASA1102 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-08-23 02:53 UTC | 2026-08-23 03:14 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
