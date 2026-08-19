# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_10:52:20_UTC-green)

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

**Latest saved flight:** 2026-08-19 10:52:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 10:52:20 UTC

- **214,995** saved flights
- **67,847** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **214,995** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,586,353.3 tonnes** estimated CO2 emissions
- **149,933,522 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8546 |
| 2 | SkyWest Airlines | 7695 |
| 3 | EJA | 4184 |
| 4 | IndiGo | 3675 |
| 5 | American Airlines | 3579 |
| 6 | Southwest Airlines | 3430 |
| 7 | Delta Air Lines | 2767 |
| 8 | ENY | 2660 |
| 9 | LATAM Airlines | 2028 |
| 10 | AZU | 1962 |
| 11 | Vueling | 1806 |
| 12 | Lufthansa | 1791 |
| 13 | WIF | 1722 |
| 14 | LXJ | 1694 |
| 15 | easyJet | 1489 |
| 16 | Swiss International | 1433 |
| 17 | AXM | 1411 |
| 18 | United Airlines | 1362 |
| 19 | QLK | 1346 |
| 20 | EJU | 1330 |
| 21 | Alaska Airlines | 1324 |
| 22 | All Nippon Airways | 1303 |
| 23 | VIV | 1183 |
| 24 | GLO | 1164 |
| 25 | PGT | 1161 |
| 26 | Air France | 1160 |
| 27 | WMT | 1115 |
| 28 | JetBlue | 1091 |
| 29 | Wizz Air | 1082 |
| 30 | AEE | 1081 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181419 |
| 2 | 🇪🇸 ES | 13753 |
| 3 | 🇧🇷 BR | 12346 |
| 4 | 🇦🇺 AU | 12153 |
| 5 | 🇨🇦 CA | 11859 |
| 6 | 🇮🇳 IN | 11439 |
| 7 | 🇮🇹 IT | 11353 |
| 8 | 🇩🇪 DE | 10606 |
| 9 | 🇬🇧 GB | 10022 |
| 10 | 🇯🇵 JP | 8862 |
| 11 | 🇨🇴 CO | 8745 |
| 12 | 🇫🇷 FR | 8556 |
| 13 | 🇬🇷 GR | 6300 |
| 14 | 🇹🇷 TR | 6162 |
| 15 | 🇲🇽 MX | 6023 |
| 16 | 🇨🇭 CH | 5700 |
| 17 | 🇳🇴 NO | 5340 |
| 18 | 🇲🇾 MY | 3731 |
| 19 | 🇿🇦 ZA | 3640 |
| 20 | 🇵🇱 PL | 3538 |
| 21 | 🇹🇭 TH | 3507 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2888 |
| 24 | 🇬🇹 GT | 2732 |
| 25 | 🇰🇷 KR | 2605 |
| 26 | 🇭🇷 HR | 2349 |
| 27 | 🇲🇦 MA | 2163 |
| 28 | 🇳🇱 NL | 1912 |
| 29 | 🇲🇪 ME | 1867 |
| 30 | 🇮🇩 ID | 1808 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4514 |
| 2 | Denver International Airport |  | US | 3508 |
| 3 | Tokyo International Airport |  | JP | 2660 |
| 4 | Indira Gandhi International Airport |  | IN | 2613 |
| 5 | Guaymaral Airport |  | CO | 2561 |
| 6 | Harry Reid International Airport |  | US | 2396 |
| 7 | Zurich Airport |  | CH | 2233 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2212 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2204 |
| 10 | La Aurora Airport |  | GT | 2077 |
| 11 | El Dorado International Airport |  | CO | 1998 |
| 12 | Chicago O'Hare International Airport |  | US | 1979 |
| 13 | Salt Lake City International Airport |  | US | 1900 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1889 |
| 15 | Congonhas Airport |  | BR | 1799 |
| 16 | Frankfurt am Main International Airport |  | DE | 1750 |
| 17 | Madrid Barajas International Airport |  | ES | 1675 |
| 18 | Capua Airport |  | IT | 1631 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1617 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1605 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1574 |
| 22 | Macau International Airport |  | MO | 1561 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 24 | Malpensa International Airport |  | IT | 1506 |
| 25 | Charles de Gaulle International Airport |  | FR | 1479 |
| 26 | Charlotte/Douglas International Airport |  | US | 1443 |
| 27 | Kuala Lumpur International Airport |  | MY | 1374 |
| 28 | Ninoy Aquino International Airport |  | PH | 1371 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1319 |
| 30 | Barcelona International Airport |  | ES | 1314 |
| 31 | Bengaluru International Airport |  | IN | 1311 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1288 |
| 33 | Seattle-Tacoma International Airport |  | US | 1281 |
| 34 | Viracopos International Airport |  | BR | 1254 |
| 35 | Calgary International Airport |  | CA | 1217 |
| 36 | Oslo Gardermoen Airport |  | NO | 1191 |
| 37 | Vitoria/Foronda Airport |  | ES | 1189 |
| 38 | Reno/Tahoe International Airport |  | US | 1164 |
| 39 | Don Mueang International Airport |  | TH | 1159 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1157 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1047 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 769 | 21m | 244 km | 3,238.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 533 | 1h 7m | 770 km | 7,080.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 483 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 458 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 356 | 27m | 275 km | 1,686.9 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 316 | 1h 49m | 1,423 km | 7,755.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 314 | 44m | 241 km | 1,304.3 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 281 | 21m | 250 km | 1,213.8 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 268 | 1h 38m | 1,156 km | 5,346.5 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 267 | 19m | 99 km | 457.4 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 263 | 27m | 215 km | 974.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 254 | 1h 14m | 961 km | 4,210.2 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 253 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 250 | 31m | 369 km | 1,591.3 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 231 | 1h 49m | 1,304 km | 5,196.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 230 | 44m | 555 km | 2,202.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SJX803 | SJX | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-19 08:04 UTC | 2026-08-19 10:52 UTC | 2h 47m |
| DRAG381 | DRA | Grenoble Le Versoud Airport (LFLG) | Saint-Jean-en-Royans Airport (LFKE) | 2026-08-19 10:41 UTC | 2026-08-19 10:52 UTC | 10m |
| N54CA |  | Triangle North Executive Airport (KLHZ) | Charlotte/Douglas International Airport (KCLT) | 2026-08-19 10:09 UTC | 2026-08-19 10:48 UTC | 38m |
| EJU53FT | EJU | Charles de Gaulle International Airport (LFPG) | Southend Airport (EGMC) | 2026-08-19 09:56 UTC | 2026-08-19 10:47 UTC | 51m |
| BAH3 | BAH | Abu Dhabi International Airport (OMAA) | Sirri Island Airport (OIBS) | 2026-08-19 10:10 UTC | 2026-08-19 10:46 UTC | 36m |
| N346GR |  | Oak Glen Ranch Airport (3TS9) | Addison Airport (KADS) | 2026-08-19 10:01 UTC | 2026-08-19 10:44 UTC | 42m |
| HBZVU | HBZ | Meiringen Airport (LSMM) | Megeve Airport (LFHM) | 2026-08-19 09:56 UTC | 2026-08-19 10:43 UTC | 46m |
| UAE382 | Emirates | Dubai International Airport (OMDB) | Zhuhai Airport (ZGSD) | 2026-08-19 03:43 UTC | 2026-08-19 10:34 UTC | 6h 51m |
| MNB6200 | MNB | Istanbul Hezarfen Airfield (LTBW) | Sirri Island Airport (OIBS) | 2026-08-19 06:46 UTC | 2026-08-19 10:34 UTC | 3h 47m |
| DLH2KH | Lufthansa | Munich International Airport (EDDM) | Stuttgart Airport (EDDS) | 2026-08-19 10:01 UTC | 2026-08-19 10:32 UTC | 30m |
| 4XCCM |  | Haifa International Airport (LLHA) | Rayak Air Base (OLRA) | 2026-08-19 09:03 UTC | 2026-08-19 10:31 UTC | 1h 28m |
| BNO92J | BNO | Bodø Airport (ENBO) | Trondheim Airport Vaernes (ENVA) | 2026-08-19 09:43 UTC | 2026-08-19 10:28 UTC | 44m |
| FFT1650 | FFT | Harry Reid International Airport (KLAS) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-19 08:09 UTC | 2026-08-19 10:24 UTC | 2h 14m |
| DHK814 | DHK | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-08-19 00:09 UTC | 2026-08-19 10:24 UTC | 10h 15m |
| WZZ1HK | Wizz Air | LRPV (LRPV) | Dortmund Airport (EDLW) | 2026-08-19 07:54 UTC | 2026-08-19 10:19 UTC | 2h 24m |
| THY3008 | Turkish Airlines | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-08-19 06:54 UTC | 2026-08-19 10:18 UTC | 3h 24m |
| MYBLS | MYB | Fairoaks Airport (EGTF) | Islay Airport (EGPI) | 2026-08-19 08:50 UTC | 2026-08-19 10:18 UTC | 1h 27m |
| 3AMTT |  | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-19 10:08 UTC | 2026-08-19 10:15 UTC | 7m |
| YEL9 | YEL | Dekalb-Peachtree Airport (KPDK) | Weaver Field (SC94) | 2026-08-19 09:29 UTC | 2026-08-19 10:08 UTC | 38m |
| URSA30 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-19 08:51 UTC | 2026-08-19 10:05 UTC | 1h 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
