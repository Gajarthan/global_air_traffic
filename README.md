# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_11:22:40_UTC-green)

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

**Latest saved flight:** 2026-06-23 11:22:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-23 11:22:40 UTC

- **117,496** saved flights
- **40,578** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **117,496** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,426,227.9 tonnes** estimated CO2 emissions
- **82,679,879 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4850 |
| 2 | SkyWest Airlines | 4353 |
| 3 | IndiGo | 2274 |
| 4 | EJA | 2270 |
| 5 | American Airlines | 1832 |
| 6 | Southwest Airlines | 1752 |
| 7 | ENY | 1468 |
| 8 | Delta Air Lines | 1385 |
| 9 | Lufthansa | 1297 |
| 10 | Vueling | 1058 |
| 11 | LATAM Airlines | 1039 |
| 12 | WIF | 1035 |
| 13 | AZU | 980 |
| 14 | AXM | 967 |
| 15 | LXJ | 894 |
| 16 | Swiss International | 830 |
| 17 | All Nippon Airways | 811 |
| 18 | Alaska Airlines | 781 |
| 19 | QLK | 759 |
| 20 | easyJet | 750 |
| 21 | EJU | 733 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 658 |
| 24 | VIV | 649 |
| 25 | Air France | 645 |
| 26 | United Airlines | 645 |
| 27 | CXK | 629 |
| 28 | MXY | 620 |
| 29 | AXB | 580 |
| 30 | GLO | 576 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 99227 |
| 2 | 🇪🇸 ES | 8012 |
| 3 | 🇮🇳 IN | 7143 |
| 4 | 🇦🇺 AU | 6980 |
| 5 | 🇧🇷 BR | 6484 |
| 6 | 🇮🇹 IT | 6279 |
| 7 | 🇩🇪 DE | 6263 |
| 8 | 🇨🇦 CA | 6153 |
| 9 | 🇯🇵 JP | 5294 |
| 10 | 🇬🇧 GB | 5140 |
| 11 | 🇫🇷 FR | 4681 |
| 12 | 🇨🇴 CO | 3992 |
| 13 | 🇲🇽 MX | 3455 |
| 14 | 🇬🇷 GR | 3356 |
| 15 | 🇳🇴 NO | 3222 |
| 16 | 🇨🇭 CH | 3012 |
| 17 | 🇲🇾 MY | 2513 |
| 18 | 🇹🇷 TR | 2398 |
| 19 | 🇿🇦 ZA | 1979 |
| 20 | 🇵🇱 PL | 1929 |
| 21 | 🇳🇿 NZ | 1919 |
| 22 | 🇹🇭 TH | 1897 |
| 23 | 🇰🇷 KR | 1896 |
| 24 | 🇵🇭 PH | 1706 |
| 25 | 🇬🇹 GT | 1657 |
| 26 | 🇲🇦 MA | 1275 |
| 27 | 🇲🇴 MO | 1169 |
| 28 | 🇲🇪 ME | 1160 |
| 29 | 🇳🇱 NL | 1133 |
| 30 | 🇭🇷 HR | 1023 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2478 |
| 2 | Denver International Airport |  | US | 1978 |
| 3 | Tokyo International Airport |  | JP | 1754 |
| 4 | Indira Gandhi International Airport |  | IN | 1565 |
| 5 | Guaymaral Airport |  | CO | 1482 |
| 6 | Harry Reid International Airport |  | US | 1465 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1432 |
| 8 | Zurich Airport |  | CH | 1313 |
| 9 | La Aurora Airport |  | GT | 1280 |
| 10 | Frankfurt am Main International Airport |  | DE | 1260 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1246 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1169 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1166 |
| 15 | Chicago O'Hare International Airport |  | US | 1151 |
| 16 | Capua Airport |  | IT | 1017 |
| 17 | Salt Lake City International Airport |  | US | 1008 |
| 18 | Madrid Barajas International Airport |  | ES | 993 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 981 |
| 20 | Kuala Lumpur International Airport |  | MY | 972 |
| 21 | Congonhas Airport |  | BR | 905 |
| 22 | Charlotte/Douglas International Airport |  | US | 894 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 878 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 876 |
| 25 | Charles de Gaulle International Airport |  | FR | 864 |
| 26 | Bengaluru International Airport |  | IN | 864 |
| 27 | Malpensa International Airport |  | IT | 831 |
| 28 | Ninoy Aquino International Airport |  | PH | 788 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 769 |
| 30 | Daniel K Inouye International Airport |  | US | 762 |
| 31 | Tenerife Norte Airport |  | ES | 759 |
| 32 | Barcelona International Airport |  | ES | 746 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 734 |
| 34 | Calgary International Airport |  | CA | 688 |
| 35 | Amsterdam Airport Schiphol |  | NL | 688 |
| 36 | Vitoria/Foronda Airport |  | ES | 687 |
| 37 | Don Mueang International Airport |  | TH | 686 |
| 38 | Seattle-Tacoma International Airport |  | US | 673 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 671 |
| 40 | Viracopos International Airport |  | BR | 666 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 615 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 426 | 21m | 244 km | 1,793.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 313 | 24m | 225 km | 1,214.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 303 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 289 | 1h 25m | 910 km | 4,535.1 t |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 7 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 285 | 1h 10m | 770 km | 3,786.0 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 233 | 26m | 275 km | 1,104.1 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 233 | 19m | 165 km | 662.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 218 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 175 | 22m | 55 km | 166.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 170 | 20m | 99 km | 291.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 168 | 26m | 215 km | 622.2 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 160 | 27m | 152 km | 418.1 t |
| 18 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 157 | 44m | 241 km | 652.1 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 153 | 44m | 452 km | 1,192.4 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 148 | 20m | 250 km | 639.3 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 146 | 1h 44m | 1,423 km | 3,583.1 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 136 | 1h 39m | 1,156 km | 2,713.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 133 | 1h 17m | 961 km | 2,204.5 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N488SA |  | Elkhart Municipal Airport (KEKM) | Nappanee Municipal Airport (KC03) | 2026-06-23 11:11 UTC | 2026-06-23 11:22 UTC | 10m |
| HLE10 | HLE | Henstridge Airfield (EGHS) | Bristol International Airport (EGGD) | 2026-06-23 11:06 UTC | 2026-06-23 11:18 UTC | 12m |
| SHERPA3 | SHE | Bishop Airfield (1AZ0) | Hidden Valley Airport (AZ43) | 2026-06-23 10:38 UTC | 2026-06-23 11:14 UTC | 36m |
| PHJVZ | PHJ | Seppe Airport (EHSE) | Rotterdam Airport (EHRD) | 2026-06-23 10:13 UTC | 2026-06-23 11:13 UTC | 1h 0m |
| TMN1 | TMN | Auckland International Airport (NZAA) | Sydney Kingsford Smith International Airport (YSSY) | 2026-06-23 08:00 UTC | 2026-06-23 11:09 UTC | 3h 8m |
| VPCPF | VPC | Allendorf/Eder Airport (EDFQ) | Innsbruck Airport (LOWI) | 2026-06-23 10:21 UTC | 2026-06-23 11:06 UTC | 44m |
| YOJ | YOJ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-23 10:28 UTC | 2026-06-23 11:05 UTC | 37m |
| YGI | YGI | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-06-23 10:17 UTC | 2026-06-23 10:54 UTC | 36m |
| YGU | YGU | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-23 10:09 UTC | 2026-06-23 10:51 UTC | 42m |
| 5YMSM |  | Nairobi Wilson Airport (HKNW) | Nairobi Wilson Airport (HKNW) | 2026-06-23 10:46 UTC | 2026-06-23 10:49 UTC | 2m |
| EZY9 | easyJet | London Gatwick Airport (EGKK) | Durham Tees Valley Airport (EGNV) | 2026-06-23 08:37 UTC | 2026-06-23 10:44 UTC | 2h 6m |
| FHBVA | FHB | Ste Leocadie Airport (LFYS) | Ste Leocadie Airport (LFYS) | 2026-06-23 10:36 UTC | 2026-06-23 10:38 UTC | 1m |
| AAL155G | American Airlines | Charlotte/Douglas International Airport (KCLT) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-06-23 09:20 UTC | 2026-06-23 10:37 UTC | 1h 17m |
| AXM6032 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-06-23 10:16 UTC | 2026-06-23 10:35 UTC | 18m |
| D9730 |  | Schanis Airport (LSZX) | LSMF (LSMF) | 2026-06-23 09:46 UTC | 2026-06-23 10:34 UTC | 48m |
| LHX3VJ | LHX | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-06-23 09:48 UTC | 2026-06-23 10:33 UTC | 44m |
| BBC437 | BBC | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-06-23 10:02 UTC | 2026-06-23 10:33 UTC | 31m |
| IGO6724 | IndiGo | Agartala Airport (VEAT) | Shillong Airport (VEBI) | 2026-06-23 10:12 UTC | 2026-06-23 10:33 UTC | 20m |
| ICC03 | ICC | Ste Leocadie Airport (LFYS) | Manresa Airport (LEMS) | 2026-06-23 10:06 UTC | 2026-06-23 10:32 UTC | 25m |
| ROT703E | ROT | Henri Coanda International Airport (LROP) | Suceava Stefan cel Mare Airport (LRSV) | 2026-06-23 09:51 UTC | 2026-06-23 10:30 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
