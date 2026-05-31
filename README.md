# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_23:28:39_UTC-green)

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

**Latest saved flight:** 2026-05-31 23:28:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-31 23:28:39 UTC

- **100,054** saved flights
- **35,554** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **100,054** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,225,682.8 tonnes** estimated CO2 emissions
- **71,054,076 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4147 |
| 2 | SkyWest Airlines | 3749 |
| 3 | IndiGo | 2021 |
| 4 | EJA | 1912 |
| 5 | American Airlines | 1624 |
| 6 | Southwest Airlines | 1513 |
| 7 | ENY | 1246 |
| 8 | Delta Air Lines | 1177 |
| 9 | Lufthansa | 1175 |
| 10 | Vueling | 938 |
| 11 | LATAM Airlines | 892 |
| 12 | WIF | 876 |
| 13 | AXM | 859 |
| 14 | AZU | 808 |
| 15 | LXJ | 760 |
| 16 | Swiss International | 731 |
| 17 | All Nippon Airways | 713 |
| 18 | Alaska Airlines | 698 |
| 19 | QLK | 674 |
| 20 | easyJet | 654 |
| 21 | EJU | 630 |
| 22 | Cathay Pacific | 596 |
| 23 | AEE | 588 |
| 24 | Air France | 580 |
| 25 | VIV | 579 |
| 26 | United Airlines | 561 |
| 27 | CXK | 540 |
| 28 | MXY | 536 |
| 29 | Japan Airlines | 500 |
| 30 | AXB | 495 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 83788 |
| 2 | 🇪🇸 ES | 6955 |
| 3 | 🇮🇳 IN | 6379 |
| 4 | 🇦🇺 AU | 6022 |
| 5 | 🇧🇷 BR | 5484 |
| 6 | 🇩🇪 DE | 5434 |
| 7 | 🇮🇹 IT | 5346 |
| 8 | 🇨🇦 CA | 5131 |
| 9 | 🇯🇵 JP | 4637 |
| 10 | 🇬🇧 GB | 4263 |
| 11 | 🇫🇷 FR | 4007 |
| 12 | 🇨🇴 CO | 3487 |
| 13 | 🇲🇽 MX | 3038 |
| 14 | 🇬🇷 GR | 2865 |
| 15 | 🇳🇴 NO | 2777 |
| 16 | 🇨🇭 CH | 2586 |
| 17 | 🇲🇾 MY | 2186 |
| 18 | 🇹🇷 TR | 1903 |
| 19 | 🇿🇦 ZA | 1751 |
| 20 | 🇳🇿 NZ | 1673 |
| 21 | 🇹🇭 TH | 1645 |
| 22 | 🇰🇷 KR | 1609 |
| 23 | 🇵🇱 PL | 1605 |
| 24 | 🇬🇹 GT | 1489 |
| 25 | 🇵🇭 PH | 1461 |
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
| 3 | Tokyo International Airport |  | JP | 1534 |
| 4 | Indira Gandhi International Airport |  | IN | 1388 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1293 |
| 6 | Harry Reid International Airport |  | US | 1276 |
| 7 | Guaymaral Airport |  | CO | 1256 |
| 8 | Frankfurt am Main International Airport |  | DE | 1179 |
| 9 | Zurich Airport |  | CH | 1149 |
| 10 | La Aurora Airport |  | GT | 1145 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1082 |
| 12 | El Dorado International Airport |  | CO | 1073 |
| 13 | Macau International Airport |  | MO | 1057 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1017 |
| 15 | Chicago O'Hare International Airport |  | US | 1003 |
| 16 | Madrid Barajas International Airport |  | ES | 875 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 864 |
| 18 | Kuala Lumpur International Airport |  | MY | 863 |
| 19 | Salt Lake City International Airport |  | US | 846 |
| 20 | Capua Airport |  | IT | 827 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 779 |
| 22 | Charlotte/Douglas International Airport |  | US | 779 |
| 23 | Charles de Gaulle International Airport |  | FR | 769 |
| 24 | Malpensa International Airport |  | IT | 765 |
| 25 | Bengaluru International Airport |  | IN | 764 |
| 26 | Congonhas Airport |  | BR | 763 |
| 27 | Daniel K Inouye International Airport |  | US | 693 |
| 28 | Tenerife Norte Airport |  | ES | 691 |
| 29 | Ninoy Aquino International Airport |  | PH | 667 |
| 30 | Barcelona International Airport |  | ES | 662 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 655 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 653 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 639 |
| 34 | Amsterdam Airport Schiphol |  | NL | 618 |
| 35 | Vitoria/Foronda Airport |  | ES | 611 |
| 36 | Don Mueang International Airport |  | TH | 603 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 586 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 573 |
| 40 | Seattle-Tacoma International Airport |  | US | 572 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 517 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 363 | 21m | 244 km | 1,528.5 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 269 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 244 | 1h 26m | 910 km | 3,828.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 243 | 28m | 304 km | 1,273.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 225 | 1h 10m | 770 km | 2,989.0 t |
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
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 126 | 1h 39m | 1,156 km | 2,513.7 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 125 | 1h 1m | 695 km | 1,498.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N523HD |  | Starshire Farm Airport (2KS9) | Henderson Executive Airport (KHND) | 2026-05-31 20:36 UTC | 2026-05-31 23:28 UTC | 2h 51m |
| UAL2845 | United Airlines | Orlando International Airport (KMCO) | Denver International Airport (KDEN) | 2026-05-31 19:50 UTC | 2026-05-31 23:24 UTC | 3h 33m |
| N649SP |  | Dane County Regional/Truax Field (KMSN) | Austin-Bergstrom International Airport (KAUS) | 2026-05-31 21:06 UTC | 2026-05-31 23:22 UTC | 2h 15m |
| BIE | BIE | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-05-31 22:41 UTC | 2026-05-31 23:18 UTC | 37m |
| VPN | VPN | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-05-31 22:45 UTC | 2026-05-31 23:15 UTC | 29m |
| N9305N |  | French Valley Airport (KF70) | Hemet-Ryan Airport (KHMT) | 2026-05-31 22:36 UTC | 2026-05-31 23:13 UTC | 37m |
| EYI | EYI | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-05-31 22:23 UTC | 2026-05-31 23:11 UTC | 47m |
| NTW14 | NTW | Kenosha Regional Airport (KENW) | Antrim County Airport (KACB) | 2026-05-31 22:41 UTC | 2026-05-31 23:08 UTC | 27m |
| N626GM |  | San Carlos Airport (KSQL) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-05-31 22:48 UTC | 2026-05-31 23:08 UTC | 19m |
| FTO115 | FTO | Francis S Gabreski Airport (KFOK) | Laguardia Airport (KLGA) | 2026-05-31 22:28 UTC | 2026-05-31 23:06 UTC | 37m |
| ZKIDU | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-05-31 22:54 UTC | 2026-05-31 23:05 UTC | 11m |
| N4975F |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-05-31 22:26 UTC | 2026-05-31 23:04 UTC | 38m |
| ROLR16 | ROL | Mount Hotham Airport (YHOT) | West Sale Airport (YWSL) | 2026-05-31 22:57 UTC | 2026-05-31 23:00 UTC | 2m |
| JRE856 | JRE | General Mitchell International Airport (KMKE) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-05-31 21:52 UTC | 2026-05-31 22:58 UTC | 1h 6m |
| JZA359 | JZA | Toronto Pearson International Airport (CYYZ) | Windsor Airport (CYQG) | 2026-05-31 22:17 UTC | 2026-05-31 22:57 UTC | 40m |
| N569Q |  | K00V (K00V) | Antelope Airpark (93CO) | 2026-05-31 22:29 UTC | 2026-05-31 22:57 UTC | 27m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-31 22:37 UTC | 2026-05-31 22:56 UTC | 19m |
| VAR403 | VAR | Phoenix Goodyear Airport (KGYR) | AZ00 (AZ00) | 2026-05-31 22:11 UTC | 2026-05-31 22:54 UTC | 42m |
| WXY | WXY | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-05-31 22:39 UTC | 2026-05-31 22:53 UTC | 14m |
| N812GH |  | Teterboro Airport (KTEB) | Coleman A Young Municipal Airport (KDET) | 2026-05-31 21:34 UTC | 2026-05-31 22:52 UTC | 1h 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
