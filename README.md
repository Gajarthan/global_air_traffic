# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_05:40:35_UTC-green)

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

**Latest saved flight:** 2026-06-26 05:40:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-26 05:40:35 UTC

- **120,683** saved flights
- **41,479** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **120,683** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,458,596.4 tonnes** estimated CO2 emissions
- **84,556,311 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4943 |
| 2 | SkyWest Airlines | 4465 |
| 3 | EJA | 2335 |
| 4 | IndiGo | 2313 |
| 5 | American Airlines | 1872 |
| 6 | Southwest Airlines | 1800 |
| 7 | ENY | 1506 |
| 8 | Delta Air Lines | 1426 |
| 9 | Lufthansa | 1318 |
| 10 | Vueling | 1082 |
| 11 | LATAM Airlines | 1071 |
| 12 | WIF | 1068 |
| 13 | AZU | 1006 |
| 14 | AXM | 980 |
| 15 | LXJ | 918 |
| 16 | Swiss International | 845 |
| 17 | All Nippon Airways | 824 |
| 18 | Alaska Airlines | 797 |
| 19 | easyJet | 776 |
| 20 | QLK | 774 |
| 21 | EJU | 754 |
| 22 | Cathay Pacific | 676 |
| 23 | AEE | 670 |
| 24 | VIV | 660 |
| 25 | Air France | 659 |
| 26 | United Airlines | 659 |
| 27 | CXK | 646 |
| 28 | MXY | 635 |
| 29 | JetBlue | 602 |
| 30 | AXB | 598 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 102437 |
| 2 | 🇪🇸 ES | 8171 |
| 3 | 🇮🇳 IN | 7267 |
| 4 | 🇦🇺 AU | 7116 |
| 5 | 🇧🇷 BR | 6640 |
| 6 | 🇩🇪 DE | 6432 |
| 7 | 🇮🇹 IT | 6410 |
| 8 | 🇨🇦 CA | 6344 |
| 9 | 🇯🇵 JP | 5377 |
| 10 | 🇬🇧 GB | 5294 |
| 11 | 🇫🇷 FR | 4790 |
| 12 | 🇨🇴 CO | 4018 |
| 13 | 🇲🇽 MX | 3519 |
| 14 | 🇬🇷 GR | 3445 |
| 15 | 🇳🇴 NO | 3314 |
| 16 | 🇨🇭 CH | 3089 |
| 17 | 🇲🇾 MY | 2543 |
| 18 | 🇹🇷 TR | 2481 |
| 19 | 🇿🇦 ZA | 2021 |
| 20 | 🇵🇱 PL | 1982 |
| 21 | 🇳🇿 NZ | 1960 |
| 22 | 🇹🇭 TH | 1916 |
| 23 | 🇰🇷 KR | 1908 |
| 24 | 🇵🇭 PH | 1736 |
| 25 | 🇬🇹 GT | 1680 |
| 26 | 🇲🇦 MA | 1300 |
| 27 | 🇲🇪 ME | 1200 |
| 28 | 🇲🇴 MO | 1174 |
| 29 | 🇳🇱 NL | 1150 |
| 30 | 🇭🇷 HR | 1040 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2536 |
| 2 | Denver International Airport |  | US | 2033 |
| 3 | Tokyo International Airport |  | JP | 1781 |
| 4 | Indira Gandhi International Airport |  | IN | 1600 |
| 5 | Guaymaral Airport |  | CO | 1508 |
| 6 | Harry Reid International Airport |  | US | 1504 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1463 |
| 8 | Zurich Airport |  | CH | 1341 |
| 9 | La Aurora Airport |  | GT | 1297 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1282 |
| 11 | Frankfurt am Main International Airport |  | DE | 1273 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1193 |
| 13 | Chicago O'Hare International Airport |  | US | 1175 |
| 14 | Macau International Airport |  | MO | 1174 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1047 |
| 17 | Capua Airport |  | IT | 1035 |
| 18 | Madrid Barajas International Airport |  | ES | 1011 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1005 |
| 20 | Kuala Lumpur International Airport |  | MY | 984 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 943 |
| 22 | Congonhas Airport |  | BR | 929 |
| 23 | Charlotte/Douglas International Airport |  | US | 912 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 900 |
| 25 | Charles de Gaulle International Airport |  | FR | 884 |
| 26 | Bengaluru International Airport |  | IN | 875 |
| 27 | Malpensa International Airport |  | IT | 841 |
| 28 | Ninoy Aquino International Airport |  | PH | 805 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 787 |
| 30 | Daniel K Inouye International Airport |  | US | 778 |
| 31 | Tenerife Norte Airport |  | ES | 762 |
| 32 | Barcelona International Airport |  | ES | 761 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 741 |
| 34 | Calgary International Airport |  | CA | 705 |
| 35 | Vitoria/Foronda Airport |  | ES | 704 |
| 36 | Amsterdam Airport Schiphol |  | NL | 696 |
| 37 | Don Mueang International Airport |  | TH | 694 |
| 38 | Seattle-Tacoma International Airport |  | US | 694 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 692 |
| 40 | Scottsdale Airport |  | US | 686 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 628 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 439 | 21m | 244 km | 1,848.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 318 | 24m | 225 km | 1,233.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 308 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 292 | 1h 25m | 910 km | 4,582.2 t |
| 6 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 291 | 1h 10m | 770 km | 3,865.7 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 237 | 26m | 275 km | 1,123.0 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 224 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 174 | 27m | 215 km | 644.4 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 173 | 20m | 99 km | 296.3 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 165 | 44m | 241 km | 685.4 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 161 | 27m | 152 km | 420.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 156 | 31m | 369 km | 993.0 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 154 | 44m | 452 km | 1,200.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 151 | 1h 44m | 1,423 km | 3,705.8 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 150 | 18m | 144 km | 373.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 141 | 1h 38m | 1,156 km | 2,812.9 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 136 | 1h 17m | 961 km | 2,254.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N410W |  | 71IS (71IS) | Frasca Field (KC16) | 2026-06-26 05:26 UTC | 2026-06-26 05:40 UTC | 13m |
| N371PD |  | Hartsfield/Jackson Atlanta International Airport (KATL) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-06-26 04:21 UTC | 2026-06-26 05:38 UTC | 1h 17m |
| BMW | BMW | Sydney Kingsford Smith International Airport (YSSY) | Shute Harbour/Whitsunday Airport (YSHR) | 2026-06-26 03:30 UTC | 2026-06-26 05:35 UTC | 2h 4m |
| SPWBK | SPW | Elbląg Airport (EPEL) | Jastarnia Airport (EPJA) | 2026-06-26 05:04 UTC | 2026-06-26 05:25 UTC | 21m |
| DCBEN | DCB | Adolf Wurth Airport (EDTY) | Friedrichshafen Airport (EDNY) | 2026-06-26 04:45 UTC | 2026-06-26 05:10 UTC | 25m |
| MXY761 | MXY | Grayce Farms Airport (PA82) | Orlando International Airport (KMCO) | 2026-06-26 03:01 UTC | 2026-06-26 05:10 UTC | 2h 8m |
| WNK | WNK | Holbrook Airport (YHBK) | Albury Airport (YMAY) | 2026-06-26 04:45 UTC | 2026-06-26 05:03 UTC | 17m |
| N72MZ |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-06-26 03:57 UTC | 2026-06-26 05:02 UTC | 1h 4m |
| N542MT |  | R M Harris Airport (4GA4) | 37GA (37GA) | 2026-06-26 04:54 UTC | 2026-06-26 04:58 UTC | 4m |
| TYA104 | TYA | Ukhta Airport (UUYH) | Ukhta Airport (UUYH) | 2026-06-25 22:47 UTC | 2026-06-26 04:54 UTC | 6h 7m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-06-26 04:31 UTC | 2026-06-26 04:52 UTC | 21m |
| WWF287 | WWF | Nampa Municipal Airport (KMAN) | Rainbow Ranch Airport (ID87) | 2026-06-26 03:58 UTC | 2026-06-26 04:49 UTC | 51m |
| N616ML |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-06-26 04:05 UTC | 2026-06-26 04:47 UTC | 41m |
| ASA1102 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-06-26 04:22 UTC | 2026-06-26 04:44 UTC | 21m |
| UBG143 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-06-26 04:07 UTC | 2026-06-26 04:41 UTC | 34m |
| WMT3ZD | WMT | Malpensa International Airport (LIMC) | Kukes Airport (LAKU) | 2026-06-26 03:17 UTC | 2026-06-26 04:39 UTC | 1h 21m |
| WIF7GT | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-06-26 04:20 UTC | 2026-06-26 04:37 UTC | 17m |
| ERU38 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | Robin Airport (59AZ) | 2026-06-26 03:53 UTC | 2026-06-26 04:36 UTC | 43m |
| STALK51 | STA | Albuquerque International Sunport Airport (KABQ) | Los Alamos Airport (KLAM) | 2026-06-26 03:14 UTC | 2026-06-26 04:35 UTC | 1h 21m |
| SWR2069 | Swiss International | Francisco de Sá Carneiro Airport (LPPR) | Zurich Airport (LSZH) | 2026-06-26 02:14 UTC | 2026-06-26 04:34 UTC | 2h 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
