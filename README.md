# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--27_04:46:35_UTC-green)

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

**Latest saved flight:** 2026-08-27 04:46:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-27 04:46:35 UTC

- **239,718** saved flights
- **72,850** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **239,718** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,887,767.7 tonnes** estimated CO2 emissions
- **167,406,823 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9623 |
| 2 | SkyWest Airlines | 8415 |
| 3 | EJA | 4639 |
| 4 | IndiGo | 4039 |
| 5 | American Airlines | 3873 |
| 6 | Southwest Airlines | 3616 |
| 7 | Delta Air Lines | 3053 |
| 8 | ENY | 2896 |
| 9 | LATAM Airlines | 2298 |
| 10 | AZU | 2231 |
| 11 | Vueling | 2061 |
| 12 | Lufthansa | 1935 |
| 13 | WIF | 1901 |
| 14 | LXJ | 1860 |
| 15 | easyJet | 1669 |
| 16 | Swiss International | 1611 |
| 17 | AXM | 1592 |
| 18 | EJU | 1536 |
| 19 | QLK | 1530 |
| 20 | United Airlines | 1512 |
| 21 | Alaska Airlines | 1434 |
| 22 | All Nippon Airways | 1423 |
| 23 | WMT | 1348 |
| 24 | GLO | 1336 |
| 25 | VIV | 1317 |
| 26 | Air France | 1310 |
| 27 | PGT | 1305 |
| 28 | Wizz Air | 1284 |
| 29 | JetBlue | 1189 |
| 30 | AEE | 1188 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 198662 |
| 2 | 🇪🇸 ES | 15412 |
| 3 | 🇧🇷 BR | 13978 |
| 4 | 🇦🇺 AU | 13617 |
| 5 | 🇨🇦 CA | 13315 |
| 6 | 🇮🇹 IT | 13109 |
| 7 | 🇮🇳 IN | 12581 |
| 8 | 🇩🇪 DE | 11837 |
| 9 | 🇬🇧 GB | 11319 |
| 10 | 🇨🇴 CO | 10252 |
| 11 | 🇯🇵 JP | 9657 |
| 12 | 🇫🇷 FR | 9652 |
| 13 | 🇹🇷 TR | 7116 |
| 14 | 🇬🇷 GR | 7061 |
| 15 | 🇲🇽 MX | 6631 |
| 16 | 🇨🇭 CH | 6427 |
| 17 | 🇳🇴 NO | 5925 |
| 18 | 🇹🇭 TH | 4346 |
| 19 | 🇲🇾 MY | 4266 |
| 20 | 🇿🇦 ZA | 4207 |
| 21 | 🇵🇱 PL | 3986 |
| 22 | 🇵🇭 PH | 3295 |
| 23 | 🇳🇿 NZ | 3295 |
| 24 | 🇬🇹 GT | 3004 |
| 25 | 🇰🇷 KR | 2843 |
| 26 | 🇭🇷 HR | 2771 |
| 27 | 🇲🇦 MA | 2426 |
| 28 | 🇲🇪 ME | 2244 |
| 29 | 🇳🇱 NL | 2172 |
| 30 | 🇮🇩 ID | 2103 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4955 |
| 2 | Denver International Airport |  | US | 3867 |
| 3 | Indira Gandhi International Airport |  | IN | 2929 |
| 4 | Tokyo International Airport |  | JP | 2874 |
| 5 | Guaymaral Airport |  | CO | 2692 |
| 6 | Harry Reid International Airport |  | US | 2548 |
| 7 | Zurich Airport |  | CH | 2510 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2456 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2393 |
| 10 | El Dorado International Airport |  | CO | 2314 |
| 11 | La Aurora Airport |  | GT | 2292 |
| 12 | Chicago O'Hare International Airport |  | US | 2141 |
| 13 | Salt Lake City International Airport |  | US | 2106 |
| 14 | Congonhas Airport |  | BR | 2039 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1995 |
| 16 | Frankfurt am Main International Airport |  | DE | 1898 |
| 17 | Capua Airport |  | IT | 1891 |
| 18 | Madrid Barajas International Airport |  | ES | 1881 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1806 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1764 |
| 21 | Malpensa International Airport |  | IT | 1719 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1691 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1683 |
| 24 | Charles de Gaulle International Airport |  | FR | 1676 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1599 |
| 27 | Kuala Lumpur International Airport |  | MY | 1542 |
| 28 | Charlotte/Douglas International Airport |  | US | 1537 |
| 29 | Barcelona International Airport |  | ES | 1525 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1516 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1451 |
| 32 | Viracopos International Airport |  | BR | 1429 |
| 33 | Don Mueang International Airport |  | TH | 1403 |
| 34 | Bengaluru International Airport |  | IN | 1400 |
| 35 | Seattle-Tacoma International Airport |  | US | 1396 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1393 |
| 37 | Calgary International Airport |  | CA | 1377 |
| 38 | Oslo Gardermoen Airport |  | NO | 1345 |
| 39 | Vancouver International Airport |  | CA | 1315 |
| 40 | O. R. Tambo International Airport |  | ZA | 1312 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1090 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 882 | 21m | 244 km | 3,713.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 613 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 609 | 24m | 225 km | 2,362.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 608 | 1h 6m | 770 km | 8,076.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 541 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 396 | 27m | 275 km | 1,876.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 376 | 1h 50m | 1,423 km | 9,227.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 365 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 363 | 44m | 555 km | 3,475.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 347 | 44m | 241 km | 1,441.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 326 | 24m | 218 km | 1,228.2 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 319 | 22m | 55 km | 303.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 318 | 1h 40m | 1,156 km | 6,344.0 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 297 | 19m | 99 km | 508.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 292 | 27m | 215 km | 1,081.4 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 277 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 271 | 19m | 144 km | 674.1 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 257 | 1h 50m | 1,304 km | 5,781.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YTR | YTR | Caboolture Airport (YCAB) | Sunshine Coast Airport (YBMC) | 2026-08-27 04:30 UTC | 2026-08-27 04:46 UTC | 16m |
| N712BC |  | Gerald R Ford International Airport (KGRR) | Mason County Airport (KLDM) | 2026-08-27 03:54 UTC | 2026-08-27 04:30 UTC | 35m |
| KUR | KUR | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-27 04:10 UTC | 2026-08-27 04:27 UTC | 17m |
| JAL6777 | Japan Airlines | Narita International Airport (RJAA) | Tianjin Binhai International Airport (ZBTJ) | 2026-08-27 01:23 UTC | 2026-08-27 04:26 UTC | 3h 2m |
| RYR75RG | Ryanair | Stockholm-Arlanda Airport (ESSA) | Olanda Airport (ESMZ) | 2026-08-27 04:01 UTC | 2026-08-27 04:25 UTC | 24m |
| ASP869 | ASP | Cape Girardeau Regional Airport (KCGI) | Calgary International Airport (CYYC) | 2026-08-27 00:46 UTC | 2026-08-27 04:23 UTC | 3h 37m |
| LT610 |  | San Clemente Island Nalf Airport (KNUC) | Catalina Airport (KAVX) | 2026-08-27 02:35 UTC | 2026-08-27 04:23 UTC | 1h 48m |
| N546LM |  | Fairbanks International Airport (PAFA) | Manley Hot Springs Airport (PAML) | 2026-08-27 03:59 UTC | 2026-08-27 04:21 UTC | 22m |
| N710SC |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-08-27 03:48 UTC | 2026-08-27 04:17 UTC | 29m |
| WNG52A | WNG | Denton Enterprise Airport (KDTO) | Seminole Municipal Airport (KSRE) | 2026-08-27 02:42 UTC | 2026-08-27 04:17 UTC | 1h 35m |
| N355FS |  | Harry Reid International Airport (KLAS) | Harry Reid International Airport (KLAS) | 2026-08-27 03:12 UTC | 2026-08-27 04:12 UTC | 1h 0m |
| OXM | OXM | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-27 03:59 UTC | 2026-08-27 04:11 UTC | 12m |
| N611MS |  | Auburn Municipal Airport (KS50) | Bremerton Ntl Airport (KPWT) | 2026-08-27 03:19 UTC | 2026-08-27 04:06 UTC | 47m |
| ECC751 | ECC | Václav Havel Airport (LKPR) | Brno-Turany Airport (LKTB) | 2026-08-27 03:43 UTC | 2026-08-27 04:05 UTC | 22m |
| N721AZ |  | John Wayne/Orange County Airport (KSNA) | Henderson Executive Airport (KHND) | 2026-08-27 03:24 UTC | 2026-08-27 04:04 UTC | 40m |
| YTU | YTU | Toowoomba Airport (YTWB) | Sunshine Coast Airport (YBMC) | 2026-08-27 03:09 UTC | 2026-08-27 03:59 UTC | 50m |
| AE962 |  | Wagga Wagga City Airport (YSWG) | Orange Airport (YORG) | 2026-08-27 03:34 UTC | 2026-08-27 03:57 UTC | 23m |
| KAL317 | Korean Air | Incheon International Airport (RKSI) | Tianjin Binhai International Airport (ZBTJ) | 2026-08-27 02:31 UTC | 2026-08-27 03:57 UTC | 1h 25m |
| A6FHD |  | Zirku Airport (OMAZ) | Das Island Airport (OMAS) | 2026-08-27 03:44 UTC | 2026-08-27 03:55 UTC | 11m |
| ZKICU | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-08-27 03:36 UTC | 2026-08-27 03:53 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
