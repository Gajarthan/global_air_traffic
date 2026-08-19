# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_08:47:14_UTC-green)

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

**Latest saved flight:** 2026-08-19 08:47:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 08:47:14 UTC

- **214,716** saved flights
- **67,795** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **214,716** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,581,527.6 tonnes** estimated CO2 emissions
- **149,653,776 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8528 |
| 2 | SkyWest Airlines | 7695 |
| 3 | EJA | 4184 |
| 4 | IndiGo | 3669 |
| 5 | American Airlines | 3579 |
| 6 | Southwest Airlines | 3430 |
| 7 | Delta Air Lines | 2767 |
| 8 | ENY | 2660 |
| 9 | LATAM Airlines | 2028 |
| 10 | AZU | 1962 |
| 11 | Vueling | 1799 |
| 12 | Lufthansa | 1787 |
| 13 | WIF | 1721 |
| 14 | LXJ | 1694 |
| 15 | easyJet | 1485 |
| 16 | Swiss International | 1431 |
| 17 | AXM | 1406 |
| 18 | United Airlines | 1362 |
| 19 | QLK | 1345 |
| 20 | EJU | 1325 |
| 21 | Alaska Airlines | 1324 |
| 22 | All Nippon Airways | 1300 |
| 23 | VIV | 1183 |
| 24 | GLO | 1163 |
| 25 | PGT | 1157 |
| 26 | Air France | 1156 |
| 27 | WMT | 1108 |
| 28 | JetBlue | 1091 |
| 29 | AEE | 1081 |
| 30 | Wizz Air | 1073 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181396 |
| 2 | 🇪🇸 ES | 13728 |
| 3 | 🇧🇷 BR | 12344 |
| 4 | 🇦🇺 AU | 12140 |
| 5 | 🇨🇦 CA | 11854 |
| 6 | 🇮🇳 IN | 11418 |
| 7 | 🇮🇹 IT | 11314 |
| 8 | 🇩🇪 DE | 10583 |
| 9 | 🇬🇧 GB | 9990 |
| 10 | 🇯🇵 JP | 8837 |
| 11 | 🇨🇴 CO | 8744 |
| 12 | 🇫🇷 FR | 8522 |
| 13 | 🇬🇷 GR | 6289 |
| 14 | 🇹🇷 TR | 6144 |
| 15 | 🇲🇽 MX | 6023 |
| 16 | 🇨🇭 CH | 5678 |
| 17 | 🇳🇴 NO | 5330 |
| 18 | 🇲🇾 MY | 3719 |
| 19 | 🇿🇦 ZA | 3622 |
| 20 | 🇵🇱 PL | 3535 |
| 21 | 🇹🇭 TH | 3482 |
| 22 | 🇳🇿 NZ | 2997 |
| 23 | 🇵🇭 PH | 2885 |
| 24 | 🇬🇹 GT | 2732 |
| 25 | 🇰🇷 KR | 2601 |
| 26 | 🇭🇷 HR | 2336 |
| 27 | 🇲🇦 MA | 2158 |
| 28 | 🇳🇱 NL | 1907 |
| 29 | 🇲🇪 ME | 1859 |
| 30 | 🇮🇩 ID | 1794 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4513 |
| 2 | Denver International Airport |  | US | 3508 |
| 3 | Tokyo International Airport |  | JP | 2655 |
| 4 | Indira Gandhi International Airport |  | IN | 2608 |
| 5 | Guaymaral Airport |  | CO | 2561 |
| 6 | Harry Reid International Airport |  | US | 2395 |
| 7 | Zurich Airport |  | CH | 2229 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2212 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2203 |
| 10 | La Aurora Airport |  | GT | 2077 |
| 11 | El Dorado International Airport |  | CO | 1998 |
| 12 | Chicago O'Hare International Airport |  | US | 1979 |
| 13 | Salt Lake City International Airport |  | US | 1900 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1889 |
| 15 | Congonhas Airport |  | BR | 1798 |
| 16 | Frankfurt am Main International Airport |  | DE | 1747 |
| 17 | Madrid Barajas International Airport |  | ES | 1674 |
| 18 | Capua Airport |  | IT | 1625 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1617 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1605 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1574 |
| 22 | Macau International Airport |  | MO | 1559 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1515 |
| 24 | Malpensa International Airport |  | IT | 1501 |
| 25 | Charles de Gaulle International Airport |  | FR | 1475 |
| 26 | Charlotte/Douglas International Airport |  | US | 1442 |
| 27 | Kuala Lumpur International Airport |  | MY | 1372 |
| 28 | Ninoy Aquino International Airport |  | PH | 1370 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1319 |
| 30 | Barcelona International Airport |  | ES | 1311 |
| 31 | Bengaluru International Airport |  | IN | 1310 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1288 |
| 33 | Seattle-Tacoma International Airport |  | US | 1281 |
| 34 | Viracopos International Airport |  | BR | 1254 |
| 35 | Calgary International Airport |  | CA | 1217 |
| 36 | Oslo Gardermoen Airport |  | NO | 1187 |
| 37 | Vitoria/Foronda Airport |  | ES | 1184 |
| 38 | Reno/Tahoe International Airport |  | US | 1164 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1154 |
| 40 | Don Mueang International Airport |  | TH | 1150 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1047 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 769 | 21m | 244 km | 3,238.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 532 | 1h 7m | 770 km | 7,067.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 506 | 24m | 225 km | 1,963.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 483 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 458 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 356 | 27m | 275 km | 1,686.9 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 315 | 1h 49m | 1,423 km | 7,730.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 313 | 44m | 241 km | 1,300.1 t |
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
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 225 | 44m | 555 km | 2,154.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DUKE51 | DUK | Wiesbaden Army Airfield (ETOU) | Stuttgart Airport (EDDS) | 2026-08-19 08:15 UTC | 2026-08-19 08:47 UTC | 31m |
| SXCAE | SXC | Eleftherios Venizelos International Airport (LGAV) | Milos Airport (LGML) | 2026-08-19 07:34 UTC | 2026-08-19 08:36 UTC | 1h 1m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-08-18 21:39 UTC | 2026-08-19 08:29 UTC | 10h 49m |
| HSIPA | HSI | Don Mueang International Airport (VTBD) | Buri Ram Airport (VTUO) | 2026-08-19 07:47 UTC | 2026-08-19 08:28 UTC | 40m |
| RDF30 | RDF | Ingolstadt Manching Airport (ETSI) | Ingolstadt Manching Airport (ETSI) | 2026-08-19 07:35 UTC | 2026-08-19 08:25 UTC | 50m |
| N997SD |  | Hemet-Ryan Airport (KHMT) | 8CA5 (8CA5) | 2026-08-19 07:15 UTC | 2026-08-19 08:25 UTC | 1h 9m |
| N80FS |  | Salzburg Airport (LOWS) | Gmunden-Laakirchen Airport (LOLU) | 2026-08-19 08:12 UTC | 2026-08-19 08:21 UTC | 8m |
| EVA165 | EVA Air | New Chitose Airport (RJCC) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-19 04:41 UTC | 2026-08-19 08:18 UTC | 3h 37m |
| SJX801 | SJX | Narita International Airport (RJAA) | Longtan Air Base (RCDI) | 2026-08-19 05:30 UTC | 2026-08-19 08:16 UTC | 2h 45m |
| ZAM17 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-08-19 07:29 UTC | 2026-08-19 08:14 UTC | 44m |
| ZSTKB | ZST | Mmabatho International Airport (FAMM) | Dwaalboom Airport (FADB) | 2026-08-19 07:43 UTC | 2026-08-19 08:10 UTC | 26m |
| OKBUD69 | OKB | Rana Loumy Airport (LKRA) | Panensky Tynec Airport (LKPC) | 2026-08-19 08:04 UTC | 2026-08-19 08:09 UTC | 4m |
| N339CA |  | Santa Maria Ranch Airport (0TE5) | 80TX (80TX) | 2026-08-19 01:17 UTC | 2026-08-19 08:08 UTC | 6h 50m |
| HBEFT | HBE | Lommis Airfield (LSZT) | Speck-Fehraltorf Airport (LSZK) | 2026-08-19 07:48 UTC | 2026-08-19 08:07 UTC | 19m |
| DLH9MT | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-08-19 07:36 UTC | 2026-08-19 08:07 UTC | 31m |
| SPAIK | SPA | Gdańsk Lech Wałęsa Airport (EPGD) | Malbork Military Air Base (EPMB) | 2026-08-19 07:33 UTC | 2026-08-19 08:05 UTC | 32m |
| MOLOCH65 | MOL | Cognac-Chateaubernard (BA 709) Air Base (LFBG) | Cognac-Chateaubernard (BA 709) Air Base (LFBG) | 2026-08-19 07:42 UTC | 2026-08-19 08:03 UTC | 21m |
| WMT9984 | WMT | Budapest Ferenc Liszt International Airport (LHBP) | Malpensa International Airport (LIMC) | 2026-08-19 06:31 UTC | 2026-08-19 08:02 UTC | 1h 31m |
| A6FHE |  | Das Island Airport (OMAS) | Das Island Airport (OMAS) | 2026-08-19 07:21 UTC | 2026-08-19 07:59 UTC | 38m |
| ZKICU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-08-19 07:46 UTC | 2026-08-19 07:56 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
