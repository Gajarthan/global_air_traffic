# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_23:41:27_UTC-green)

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

**Latest saved flight:** 2026-06-05 23:41:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-05 23:41:27 UTC

- **103,331** saved flights
- **36,555** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **103,331** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,261,552.2 tonnes** estimated CO2 emissions
- **73,133,463 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4238 |
| 2 | SkyWest Airlines | 3896 |
| 3 | IndiGo | 2059 |
| 4 | EJA | 1982 |
| 5 | American Airlines | 1671 |
| 6 | Southwest Airlines | 1566 |
| 7 | ENY | 1289 |
| 8 | Delta Air Lines | 1226 |
| 9 | Lufthansa | 1191 |
| 10 | Vueling | 952 |
| 11 | LATAM Airlines | 916 |
| 12 | WIF | 907 |
| 13 | AXM | 888 |
| 14 | AZU | 830 |
| 15 | LXJ | 782 |
| 16 | Swiss International | 744 |
| 17 | All Nippon Airways | 727 |
| 18 | Alaska Airlines | 722 |
| 19 | QLK | 694 |
| 20 | easyJet | 669 |
| 21 | EJU | 645 |
| 22 | Cathay Pacific | 618 |
| 23 | AEE | 600 |
| 24 | VIV | 594 |
| 25 | Air France | 590 |
| 26 | United Airlines | 573 |
| 27 | MXY | 560 |
| 28 | CXK | 553 |
| 29 | Japan Airlines | 511 |
| 30 | AXB | 506 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 87092 |
| 2 | 🇪🇸 ES | 7089 |
| 3 | 🇮🇳 IN | 6507 |
| 4 | 🇦🇺 AU | 6279 |
| 5 | 🇧🇷 BR | 5650 |
| 6 | 🇩🇪 DE | 5540 |
| 7 | 🇮🇹 IT | 5470 |
| 8 | 🇨🇦 CA | 5385 |
| 9 | 🇯🇵 JP | 4754 |
| 10 | 🇬🇧 GB | 4350 |
| 11 | 🇫🇷 FR | 4089 |
| 12 | 🇨🇴 CO | 3549 |
| 13 | 🇲🇽 MX | 3110 |
| 14 | 🇬🇷 GR | 2935 |
| 15 | 🇳🇴 NO | 2872 |
| 16 | 🇨🇭 CH | 2639 |
| 17 | 🇲🇾 MY | 2262 |
| 18 | 🇹🇷 TR | 1952 |
| 19 | 🇿🇦 ZA | 1790 |
| 20 | 🇳🇿 NZ | 1735 |
| 21 | 🇹🇭 TH | 1701 |
| 22 | 🇰🇷 KR | 1691 |
| 23 | 🇵🇱 PL | 1648 |
| 24 | 🇵🇭 PH | 1516 |
| 25 | 🇬🇹 GT | 1509 |
| 26 | 🇲🇦 MA | 1138 |
| 27 | 🇲🇴 MO | 1078 |
| 28 | 🇳🇱 NL | 1017 |
| 29 | 🇲🇪 ME | 970 |
| 30 | 🇭🇷 HR | 903 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2253 |
| 2 | Denver International Airport |  | US | 1774 |
| 3 | Tokyo International Airport |  | JP | 1578 |
| 4 | Indira Gandhi International Airport |  | IN | 1412 |
| 5 | Harry Reid International Airport |  | US | 1330 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1316 |
| 7 | Guaymaral Airport |  | CO | 1287 |
| 8 | Frankfurt am Main International Airport |  | DE | 1191 |
| 9 | Zurich Airport |  | CH | 1173 |
| 10 | La Aurora Airport |  | GT | 1162 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1120 |
| 12 | El Dorado International Airport |  | CO | 1086 |
| 13 | Macau International Airport |  | MO | 1078 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1049 |
| 15 | Chicago O'Hare International Airport |  | US | 1037 |
| 16 | Madrid Barajas International Airport |  | ES | 899 |
| 17 | Kuala Lumpur International Airport |  | MY | 891 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 888 |
| 19 | Salt Lake City International Airport |  | US | 878 |
| 20 | Capua Airport |  | IT | 856 |
| 21 | Charlotte/Douglas International Airport |  | US | 806 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 800 |
| 23 | Charles de Gaulle International Airport |  | FR | 785 |
| 24 | Congonhas Airport |  | BR | 785 |
| 25 | Bengaluru International Airport |  | IN | 779 |
| 26 | Malpensa International Airport |  | IT | 775 |
| 27 | Daniel K Inouye International Airport |  | US | 710 |
| 28 | Tenerife Norte Airport |  | ES | 703 |
| 29 | Ninoy Aquino International Airport |  | PH | 691 |
| 30 | Barcelona International Airport |  | ES | 678 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 671 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 668 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 662 |
| 34 | Amsterdam Airport Schiphol |  | NL | 629 |
| 35 | Don Mueang International Airport |  | TH | 623 |
| 36 | Vitoria/Foronda Airport |  | ES | 621 |
| 37 | Calgary International Airport |  | CA | 616 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 600 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 589 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 531 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 378 | 21m | 244 km | 1,591.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 273 | 24m | 225 km | 1,059.1 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 273 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 257 | 14m | 114 km | 504.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 251 | 1h 26m | 910 km | 3,938.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 250 | 28m | 304 km | 1,310.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 237 | 1h 10m | 770 km | 3,148.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 134 | 18m | 144 km | 333.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 132 | 20m | 147 km | 334.0 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 121 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 52m | 1,304 km | 2,677.2 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |
| 30 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 118 | 44m | 241 km | 490.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N7301P |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-06-05 23:22 UTC | 2026-06-05 23:41 UTC | 18m |
| N814SS |  | Beluga Airport (PABG) | Trading Bay Production Airport (5AK0) | 2026-06-05 23:21 UTC | 2026-06-05 23:37 UTC | 16m |
| N4777H |  | Loeber Mcdaniel Field (WI50) | Loeber Mcdaniel Field (WI50) | 2026-06-05 22:56 UTC | 2026-06-05 23:33 UTC | 36m |
| N261PJ |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-06-05 22:53 UTC | 2026-06-05 23:26 UTC | 33m |
| N559HF |  | North Las Vegas Airport (KVGT) | Santa Monica Municipal Airport (KSMO) | 2026-06-05 22:31 UTC | 2026-06-05 23:23 UTC | 51m |
| N93SP |  | Van Nuys Airport (KVNY) | Sequoia Field (KD86) | 2026-06-05 22:52 UTC | 2026-06-05 23:17 UTC | 25m |
| N27DD |  | Baton Rouge Metro, Ryan Field (KBTR) | 8LA9 (8LA9) | 2026-06-05 23:01 UTC | 2026-06-05 23:16 UTC | 15m |
| SKW4766 | SkyWest Airlines | Chicago O'Hare International Airport (KORD) | Okc Will Rogers International Airport (KOKC) | 2026-06-05 21:29 UTC | 2026-06-05 23:16 UTC | 1h 47m |
| N402AA |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-06-05 22:34 UTC | 2026-06-05 23:14 UTC | 40m |
| N4871V |  | Stockton Metro Airport (KSCK) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-05 22:32 UTC | 2026-06-05 23:13 UTC | 41m |
| N584LP |  | NC45 (NC45) | Coastal Carolina Regional Airport (KEWN) | 2026-06-05 22:51 UTC | 2026-06-05 23:11 UTC | 19m |
| EJA343 | EJA | John Wayne/Orange County Airport (KSNA) | Scottsdale Airport (KSDL) | 2026-06-05 22:12 UTC | 2026-06-05 23:10 UTC | 57m |
| HMZ | HMZ | Perth Jandakot Airport (YPJT) | Dongara Airport (YDRA) | 2026-06-05 22:28 UTC | 2026-06-05 23:09 UTC | 40m |
| N904SH |  | Hector International Airport (KFAR) | Hagens Airport (78MN) | 2026-06-05 22:43 UTC | 2026-06-05 23:09 UTC | 25m |
| LIFELN2 | LIF | City Of Colorado Springs Municipal Airport (KCOS) | Desiderata Ranch Airport (30CO) | 2026-06-05 22:55 UTC | 2026-06-05 23:08 UTC | 13m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-06-05 22:48 UTC | 2026-06-05 23:07 UTC | 19m |
| XSN06 | XSN | Buchanan Field (KCCR) | Truckee-Tahoe Airport (KTRK) | 2026-06-05 22:37 UTC | 2026-06-05 23:07 UTC | 29m |
| N79228 |  | Charleston Executive Airport (KJZI) | Raven's Run Airport (SC65) | 2026-06-05 22:49 UTC | 2026-06-05 23:07 UTC | 17m |
| SIA216 | Singapore Airlines | Perth International Airport (YPPH) | Hang Nadim Airport (WIDD) | 2026-06-05 18:32 UTC | 2026-06-05 23:07 UTC | 4h 35m |
| EJA837 | EJA | Santa Barbara Municipal Airport (KSBA) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-05 22:25 UTC | 2026-06-05 23:06 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
