# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_01:45:26_UTC-green)

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

**Latest saved flight:** 2026-06-01 01:45:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-01 01:45:26 UTC

- **100,166** saved flights
- **35,583** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **100,166** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,226,634.0 tonnes** estimated CO2 emissions
- **71,109,216 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4147 |
| 2 | SkyWest Airlines | 3756 |
| 3 | IndiGo | 2023 |
| 4 | EJA | 1915 |
| 5 | American Airlines | 1624 |
| 6 | Southwest Airlines | 1516 |
| 7 | ENY | 1248 |
| 8 | Delta Air Lines | 1179 |
| 9 | Lufthansa | 1175 |
| 10 | Vueling | 938 |
| 11 | LATAM Airlines | 892 |
| 12 | WIF | 876 |
| 13 | AXM | 863 |
| 14 | AZU | 808 |
| 15 | LXJ | 760 |
| 16 | Swiss International | 731 |
| 17 | All Nippon Airways | 713 |
| 18 | Alaska Airlines | 701 |
| 19 | QLK | 676 |
| 20 | easyJet | 654 |
| 21 | EJU | 630 |
| 22 | Cathay Pacific | 596 |
| 23 | AEE | 588 |
| 24 | VIV | 581 |
| 25 | Air France | 580 |
| 26 | United Airlines | 561 |
| 27 | CXK | 540 |
| 28 | MXY | 536 |
| 29 | Japan Airlines | 505 |
| 30 | AXB | 495 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 83885 |
| 2 | 🇪🇸 ES | 6955 |
| 3 | 🇮🇳 IN | 6383 |
| 4 | 🇦🇺 AU | 6054 |
| 5 | 🇧🇷 BR | 5484 |
| 6 | 🇩🇪 DE | 5434 |
| 7 | 🇮🇹 IT | 5347 |
| 8 | 🇨🇦 CA | 5143 |
| 9 | 🇯🇵 JP | 4651 |
| 10 | 🇬🇧 GB | 4263 |
| 11 | 🇫🇷 FR | 4007 |
| 12 | 🇨🇴 CO | 3489 |
| 13 | 🇲🇽 MX | 3041 |
| 14 | 🇬🇷 GR | 2866 |
| 15 | 🇳🇴 NO | 2777 |
| 16 | 🇨🇭 CH | 2586 |
| 17 | 🇲🇾 MY | 2194 |
| 18 | 🇹🇷 TR | 1904 |
| 19 | 🇿🇦 ZA | 1751 |
| 20 | 🇳🇿 NZ | 1677 |
| 21 | 🇹🇭 TH | 1656 |
| 22 | 🇰🇷 KR | 1619 |
| 23 | 🇵🇱 PL | 1605 |
| 24 | 🇬🇹 GT | 1489 |
| 25 | 🇵🇭 PH | 1465 |
| 26 | 🇲🇦 MA | 1123 |
| 27 | 🇲🇴 MO | 1057 |
| 28 | 🇳🇱 NL | 1002 |
| 29 | 🇲🇪 ME | 959 |
| 30 | 🇭🇷 HR | 888 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2190 |
| 2 | Denver International Airport |  | US | 1719 |
| 3 | Tokyo International Airport |  | JP | 1540 |
| 4 | Indira Gandhi International Airport |  | IN | 1390 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1294 |
| 6 | Harry Reid International Airport |  | US | 1278 |
| 7 | Guaymaral Airport |  | CO | 1256 |
| 8 | Frankfurt am Main International Airport |  | DE | 1179 |
| 9 | Zurich Airport |  | CH | 1149 |
| 10 | La Aurora Airport |  | GT | 1145 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1084 |
| 12 | El Dorado International Airport |  | CO | 1074 |
| 13 | Macau International Airport |  | MO | 1057 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1020 |
| 15 | Chicago O'Hare International Airport |  | US | 1005 |
| 16 | Madrid Barajas International Airport |  | ES | 875 |
| 17 | Kuala Lumpur International Airport |  | MY | 867 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 865 |
| 19 | Salt Lake City International Airport |  | US | 847 |
| 20 | Capua Airport |  | IT | 827 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 781 |
| 22 | Charlotte/Douglas International Airport |  | US | 779 |
| 23 | Charles de Gaulle International Airport |  | FR | 769 |
| 24 | Malpensa International Airport |  | IT | 765 |
| 25 | Bengaluru International Airport |  | IN | 764 |
| 26 | Congonhas Airport |  | BR | 763 |
| 27 | Daniel K Inouye International Airport |  | US | 695 |
| 28 | Tenerife Norte Airport |  | ES | 691 |
| 29 | Ninoy Aquino International Airport |  | PH | 669 |
| 30 | Barcelona International Airport |  | ES | 662 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 656 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 653 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 639 |
| 34 | Amsterdam Airport Schiphol |  | NL | 618 |
| 35 | Vitoria/Foronda Airport |  | ES | 611 |
| 36 | Don Mueang International Airport |  | TH | 606 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 587 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 573 |
| 40 | Seattle-Tacoma International Airport |  | US | 573 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 517 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 365 | 21m | 244 km | 1,536.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 269 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 264 | 24m | 225 km | 1,024.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 245 | 1h 26m | 910 km | 3,844.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 243 | 28m | 304 km | 1,273.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 227 | 1h 10m | 770 km | 3,015.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 210 | 19m | 165 km | 597.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 197 | 26m | 275 km | 933.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 156 | 20m | 99 km | 267.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 149 | 27m | 215 km | 551.8 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 141 | 31m | 369 km | 897.5 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 141 | 22m | 55 km | 134.0 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 131 | 13m | - | - |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 130 | 20m | 147 km | 329.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 129 | 18m | 144 km | 320.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 127 | 1h 39m | 1,156 km | 2,533.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 126 | 1h 1m | 695 km | 1,510.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N34GR |  | Quillayute Airport (KUIL) | William R Fairchild International Airport (KCLM) | 2026-06-01 01:23 UTC | 2026-06-01 01:45 UTC | 22m |
| WSG907T | WSG | Thunder Bay Airport (CYQT) | CED8 (CED8) | 2026-06-01 01:33 UTC | 2026-06-01 01:43 UTC | 10m |
| LJY286 | LJY | Charlottesville-Albemarle Airport (KCHO) | Lehigh Valley International Airport (KABE) | 2026-06-01 00:49 UTC | 2026-06-01 01:30 UTC | 41m |
| N821TN |  | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Kinsley Municipal Airport (K33K) | 2026-06-01 00:58 UTC | 2026-06-01 01:20 UTC | 21m |
| JTE922 | JTE | Brisbane International Airport (YBBN) | Cooma Snowy Mountains Airport (YCOM) | 2026-05-31 23:13 UTC | 2026-06-01 01:18 UTC | 2h 5m |
| N334AM |  | CA40 (CA40) | Bob Hope Airport (KBUR) | 2026-06-01 00:39 UTC | 2026-06-01 01:14 UTC | 35m |
| N772DF |  | Capital City Airport (KCXY) | Capital City Airport (KCXY) | 2026-06-01 01:05 UTC | 2026-06-01 01:06 UTC | 0m |
| N75141 |  | Bishop International Airport (KFNT) | Oakland/Troy Airport (KVLL) | 2026-06-01 00:42 UTC | 2026-06-01 01:04 UTC | 21m |
| N20236 |  | Pierce County/Thun Field (KPLU) | Tacoma Narrows Airport (KTIW) | 2026-06-01 00:45 UTC | 2026-06-01 01:03 UTC | 18m |
| BIE | BIE | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-06-01 00:30 UTC | 2026-06-01 01:02 UTC | 31m |
| JAL454 | Japan Airlines | Tokushima Airport (RJOS) | Tokyo International Airport (RJTT) | 2026-06-01 00:06 UTC | 2026-06-01 01:01 UTC | 55m |
| JJA104 | JJA | G 710 Airport (RK6D) | Gimpo International Airport (RKSS) | 2026-06-01 00:19 UTC | 2026-06-01 00:53 UTC | 34m |
| CHP21 | CHP | Auburn Municipal Airport (KAUN) | Truckee-Tahoe Airport (KTRK) | 2026-06-01 00:30 UTC | 2026-06-01 00:50 UTC | 19m |
| THA002 | Thai Airways | Suvarnabhumi Airport (VTBS) | Khon Kaen Airport (VTUK) | 2026-06-01 00:11 UTC | 2026-06-01 00:48 UTC | 36m |
| AXM6051 | AXM | Kuala Lumpur International Airport (WMKK) | Kluang Airport (WMAP) | 2026-06-01 00:24 UTC | 2026-06-01 00:45 UTC | 20m |
| SKU178 | SKU | Vinasutil Airport (SCSV) | Chicureo Airport (SCHC) | 2026-06-01 00:31 UTC | 2026-06-01 00:45 UTC | 14m |
| ASA64 | Alaska Airlines | Wrangell Airport (PAWG) | Ketchikan International Airport (PAKT) | 2026-06-01 00:32 UTC | 2026-06-01 00:45 UTC | 13m |
| NOK360 | NOK | Don Mueang International Airport (VTBD) | Nam Phung Dam Airport (VTUZ) | 2026-06-01 00:06 UTC | 2026-06-01 00:45 UTC | 38m |
| N361ML |  | Lake Havasu City Airport (KHII) | AZ77 (AZ77) | 2026-06-01 00:19 UTC | 2026-06-01 00:44 UTC | 25m |
| SWA2337 | Southwest Airlines | San Diego International Airport (KSAN) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-31 23:44 UTC | 2026-06-01 00:44 UTC | 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
