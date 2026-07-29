# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_07:08:26_UTC-green)

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

**Latest saved flight:** 2026-07-29 07:08:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-29 07:08:26 UTC

- **157,803** saved flights
- **52,328** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **157,803** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,893,634.6 tonnes** estimated CO2 emissions
- **109,775,918 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6343 |
| 2 | SkyWest Airlines | 5778 |
| 3 | EJA | 3123 |
| 4 | IndiGo | 2784 |
| 5 | American Airlines | 2515 |
| 6 | Southwest Airlines | 2482 |
| 7 | ENY | 1968 |
| 8 | Delta Air Lines | 1870 |
| 9 | Lufthansa | 1509 |
| 10 | LATAM Airlines | 1477 |
| 11 | AZU | 1384 |
| 12 | WIF | 1332 |
| 13 | Vueling | 1325 |
| 14 | LXJ | 1217 |
| 15 | AXM | 1107 |
| 16 | Swiss International | 1091 |
| 17 | easyJet | 1029 |
| 18 | Alaska Airlines | 991 |
| 19 | QLK | 986 |
| 20 | All Nippon Airways | 978 |
| 21 | EJU | 967 |
| 22 | VIV | 866 |
| 23 | United Airlines | 838 |
| 24 | CXK | 837 |
| 25 | Cathay Pacific | 831 |
| 26 | GLO | 828 |
| 27 | AEE | 825 |
| 28 | MXY | 821 |
| 29 | Air France | 817 |
| 30 | JetBlue | 817 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 136217 |
| 2 | 🇪🇸 ES | 10154 |
| 3 | 🇧🇷 BR | 9008 |
| 4 | 🇦🇺 AU | 8933 |
| 5 | 🇮🇳 IN | 8756 |
| 6 | 🇨🇦 CA | 8551 |
| 7 | 🇮🇹 IT | 8145 |
| 8 | 🇩🇪 DE | 7991 |
| 9 | 🇬🇧 GB | 7236 |
| 10 | 🇯🇵 JP | 6455 |
| 11 | 🇫🇷 FR | 6226 |
| 12 | 🇨🇴 CO | 5538 |
| 13 | 🇲🇽 MX | 4532 |
| 14 | 🇬🇷 GR | 4497 |
| 15 | 🇳🇴 NO | 4173 |
| 16 | 🇨🇭 CH | 4123 |
| 17 | 🇹🇷 TR | 3772 |
| 18 | 🇲🇾 MY | 2880 |
| 19 | 🇵🇱 PL | 2683 |
| 20 | 🇿🇦 ZA | 2552 |
| 21 | 🇳🇿 NZ | 2346 |
| 22 | 🇹🇭 TH | 2263 |
| 23 | 🇰🇷 KR | 2097 |
| 24 | 🇵🇭 PH | 2081 |
| 25 | 🇬🇹 GT | 2021 |
| 26 | 🇲🇦 MA | 1605 |
| 27 | 🇲🇪 ME | 1518 |
| 28 | 🇭🇷 HR | 1456 |
| 29 | 🇳🇱 NL | 1436 |
| 30 | 🇲🇴 MO | 1307 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3243 |
| 2 | Denver International Airport |  | US | 2639 |
| 3 | Tokyo International Airport |  | JP | 2042 |
| 4 | Guaymaral Airport |  | CO | 1982 |
| 5 | Indira Gandhi International Airport |  | IN | 1949 |
| 6 | Harry Reid International Airport |  | US | 1926 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1746 |
| 8 | Zurich Airport |  | CH | 1694 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1656 |
| 10 | La Aurora Airport |  | GT | 1567 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1475 |
| 12 | Frankfurt am Main International Airport |  | DE | 1459 |
| 13 | El Dorado International Airport |  | CO | 1437 |
| 14 | Chicago O'Hare International Airport |  | US | 1433 |
| 15 | Salt Lake City International Airport |  | US | 1422 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1324 |
| 17 | Macau International Airport |  | MO | 1307 |
| 18 | Congonhas Airport |  | BR | 1299 |
| 19 | Madrid Barajas International Airport |  | ES | 1250 |
| 20 | Capua Airport |  | IT | 1241 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1211 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1135 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1125 |
| 24 | Charlotte/Douglas International Airport |  | US | 1114 |
| 25 | Kuala Lumpur International Airport |  | MY | 1103 |
| 26 | Charles de Gaulle International Airport |  | FR | 1079 |
| 27 | Bengaluru International Airport |  | IN | 1041 |
| 28 | Malpensa International Airport |  | IT | 1040 |
| 29 | Ninoy Aquino International Airport |  | PH | 976 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 961 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 954 |
| 32 | Barcelona International Airport |  | ES | 942 |
| 33 | Daniel K Inouye International Airport |  | US | 933 |
| 34 | Seattle-Tacoma International Airport |  | US | 922 |
| 35 | Calgary International Airport |  | CA | 908 |
| 36 | Tenerife Norte Airport |  | ES | 895 |
| 37 | Viracopos International Airport |  | BR | 895 |
| 38 | Scottsdale Airport |  | US | 891 |
| 39 | Oslo Gardermoen Airport |  | NO | 874 |
| 40 | Amsterdam Airport Schiphol |  | NL | 867 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 832 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 572 | 21m | 244 km | 2,408.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 379 | 24m | 225 km | 1,470.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 376 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 363 | 1h 9m | 770 km | 4,822.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 291 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 277 | 27m | 275 km | 1,312.6 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 221 | 44m | 241 km | 918.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 213 | 1h 47m | 1,423 km | 5,227.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 207 | 26m | 215 km | 766.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 202 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 199 | 20m | 250 km | 859.6 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 190 | 30m | 49 km | 160.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 187 | 1h 15m | 961 km | 3,099.6 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 187 | 18m | 144 km | 465.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 185 | 31m | 369 km | 1,177.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 179 | 50m | 556 km | 1,715.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 176 | 1h 39m | 1,156 km | 3,511.1 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 176 | 44m | 452 km | 1,371.7 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 174 | 1h 1m | 695 km | 2,085.7 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 49m | 1,304 km | 3,779.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRU975 | BRU | Minsk International Airport (UMMS) | Sheremetyevo International Airport (UUEE) | 2026-07-29 04:47 UTC | 2026-07-29 07:08 UTC | 2h 21m |
| NHD421 | NHD | Emden Airport (EDWE) | Norderney Airport (EDWY) | 2026-07-29 06:45 UTC | 2026-07-29 07:05 UTC | 20m |
| SPICY55 | SPI | Niederstetten Airport (ETHN) | Niederstetten Airport (ETHN) | 2026-07-29 06:39 UTC | 2026-07-29 07:04 UTC | 25m |
| PUJ | PUJ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-29 06:46 UTC | 2026-07-29 07:03 UTC | 16m |
| N994SD |  | Hemet-Ryan Airport (KHMT) | Skylark Airport (CA89) | 2026-07-29 06:08 UTC | 2026-07-29 07:01 UTC | 52m |
| ZES | ZES | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-29 06:13 UTC | 2026-07-29 07:01 UTC | 48m |
| KLM887 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-07-28 20:14 UTC | 2026-07-29 06:53 UTC | 10h 38m |
| BSM | BSM | Toowoomba Airport (YTWB) | Sunshine Coast Airport (YBMC) | 2026-07-29 06:28 UTC | 2026-07-29 06:52 UTC | 24m |
| N85FF |  | Tucson International Airport (KTUS) | Scottsdale Airport (KSDL) | 2026-07-29 05:39 UTC | 2026-07-29 06:50 UTC | 1h 10m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-07-29 05:51 UTC | 2026-07-29 06:43 UTC | 51m |
| VKG012 | VKG | Trondheim Airport Vaernes (ENVA) | Khrabrovo Airport (UMKK) | 2026-07-29 05:19 UTC | 2026-07-29 06:42 UTC | 1h 23m |
| WIF3LP | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-07-29 05:46 UTC | 2026-07-29 06:41 UTC | 55m |
| AAL509 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Sacramento International Airport (KSMF) | 2026-07-29 03:38 UTC | 2026-07-29 06:31 UTC | 2h 53m |
| HBZVQ | HBZ | Meiringen Airport (LSMM) | Raron Airport (LSTA) | 2026-07-29 06:04 UTC | 2026-07-29 06:27 UTC | 23m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-07-29 05:51 UTC | 2026-07-29 06:27 UTC | 35m |
| SAS1314 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-07-29 05:49 UTC | 2026-07-29 06:21 UTC | 32m |
| ZHB | ZHB | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-29 05:51 UTC | 2026-07-29 06:16 UTC | 25m |
| SAS683 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Malpensa International Airport (LIMC) | 2026-07-29 04:26 UTC | 2026-07-29 06:16 UTC | 1h 49m |
| RYR5GE | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Otocac Airport (LDRO) | 2026-07-29 05:18 UTC | 2026-07-29 06:15 UTC | 57m |
| WIF8HM | WIF | Bergen Airport Flesland (ENBR) | Ålesund Airport (ENAL) | 2026-07-29 05:46 UTC | 2026-07-29 06:14 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
