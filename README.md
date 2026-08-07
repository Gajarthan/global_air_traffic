# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_19:45:32_UTC-green)

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

**Latest saved flight:** 2026-08-07 19:45:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 19:45:32 UTC

- **176,441** saved flights
- **56,900** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **176,441** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,121,167.8 tonnes** estimated CO2 emissions
- **122,966,248 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6993 |
| 2 | SkyWest Airlines | 6443 |
| 3 | EJA | 3485 |
| 4 | IndiGo | 3093 |
| 5 | Southwest Airlines | 2777 |
| 6 | American Airlines | 2753 |
| 7 | ENY | 2197 |
| 8 | Delta Air Lines | 2084 |
| 9 | LATAM Airlines | 1633 |
| 10 | Lufthansa | 1584 |
| 11 | AZU | 1567 |
| 12 | WIF | 1480 |
| 13 | Vueling | 1456 |
| 14 | LXJ | 1388 |
| 15 | Swiss International | 1205 |
| 16 | AXM | 1196 |
| 17 | easyJet | 1194 |
| 18 | EJU | 1082 |
| 19 | QLK | 1082 |
| 20 | All Nippon Airways | 1069 |
| 21 | Alaska Airlines | 1068 |
| 22 | VIV | 971 |
| 23 | Cathay Pacific | 944 |
| 24 | CXK | 938 |
| 25 | GLO | 928 |
| 26 | AEE | 921 |
| 27 | United Airlines | 912 |
| 28 | Air France | 911 |
| 29 | MXY | 889 |
| 30 | JetBlue | 872 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 151681 |
| 2 | 🇪🇸 ES | 11307 |
| 3 | 🇧🇷 BR | 10059 |
| 4 | 🇦🇺 AU | 9951 |
| 5 | 🇮🇳 IN | 9694 |
| 6 | 🇨🇦 CA | 9650 |
| 7 | 🇮🇹 IT | 9121 |
| 8 | 🇩🇪 DE | 8739 |
| 9 | 🇬🇧 GB | 8158 |
| 10 | 🇯🇵 JP | 7076 |
| 11 | 🇫🇷 FR | 7020 |
| 12 | 🇨🇴 CO | 6476 |
| 13 | 🇬🇷 GR | 5141 |
| 14 | 🇲🇽 MX | 5040 |
| 15 | 🇨🇭 CH | 4683 |
| 16 | 🇳🇴 NO | 4599 |
| 17 | 🇹🇷 TR | 4382 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2934 |
| 20 | 🇿🇦 ZA | 2880 |
| 21 | 🇹🇭 TH | 2623 |
| 22 | 🇳🇿 NZ | 2555 |
| 23 | 🇵🇭 PH | 2326 |
| 24 | 🇬🇹 GT | 2252 |
| 25 | 🇰🇷 KR | 2203 |
| 26 | 🇲🇦 MA | 1783 |
| 27 | 🇭🇷 HR | 1729 |
| 28 | 🇲🇪 ME | 1606 |
| 29 | 🇳🇱 NL | 1589 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3643 |
| 2 | Denver International Airport |  | US | 2914 |
| 3 | Tokyo International Airport |  | JP | 2208 |
| 4 | Guaymaral Airport |  | CO | 2166 |
| 5 | Indira Gandhi International Airport |  | IN | 2155 |
| 6 | Harry Reid International Airport |  | US | 2102 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1912 |
| 8 | Zurich Airport |  | CH | 1876 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1844 |
| 10 | La Aurora Airport |  | GT | 1732 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1616 |
| 12 | Chicago O'Hare International Airport |  | US | 1588 |
| 13 | El Dorado International Airport |  | CO | 1581 |
| 14 | Salt Lake City International Airport |  | US | 1575 |
| 15 | Frankfurt am Main International Airport |  | DE | 1551 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1460 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1424 |
| 19 | Capua Airport |  | IT | 1380 |
| 20 | Madrid Barajas International Airport |  | ES | 1375 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1313 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1239 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1235 |
| 24 | Malpensa International Airport |  | IT | 1206 |
| 25 | Charlotte/Douglas International Airport |  | US | 1206 |
| 26 | Charles de Gaulle International Airport |  | FR | 1202 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1153 |
| 29 | Ninoy Aquino International Airport |  | PH | 1094 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1093 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1088 |
| 32 | Barcelona International Airport |  | ES | 1049 |
| 33 | Seattle-Tacoma International Airport |  | US | 1014 |
| 34 | Daniel K Inouye International Airport |  | US | 1013 |
| 35 | Viracopos International Airport |  | BR | 1004 |
| 36 | Reno/Tahoe International Airport |  | US | 1003 |
| 37 | Calgary International Airport |  | CA | 998 |
| 38 | Oslo Gardermoen Airport |  | NO | 984 |
| 39 | Tenerife Norte Airport |  | ES | 970 |
| 40 | Amsterdam Airport Schiphol |  | NL | 955 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 644 | 21m | 244 km | 2,711.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 412 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 406 | 1h 8m | 770 km | 5,393.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 325 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 296 | 27m | 275 km | 1,402.6 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 269 | 44m | 241 km | 1,117.4 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 244 | 1h 48m | 1,423 km | 5,988.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 226 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 218 | 20m | 99 km | 373.4 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 21 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 216 | 8m | - | - |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 213 | 51m | 556 km | 2,041.8 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 211 | 1h 15m | 961 km | 3,497.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 210 | 19m | 144 km | 522.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 206 | 1h 38m | 1,156 km | 4,109.6 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 206 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 203 | 31m | 369 km | 1,292.1 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 201 | 24m | 218 km | 757.2 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 192 | 1h 2m | 695 km | 2,301.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TKR169 | TKR | Mineral County Memorial Airport (KC24) | Ohkay Owingeh Airport (KE14) | 2026-08-07 19:32 UTC | 2026-08-07 19:45 UTC | 12m |
| BLZR293 | BLZ | Kingsville Nas Airport (KNQI) | Seven C's Ranch Airport (0XA4) | 2026-08-07 19:26 UTC | 2026-08-07 19:39 UTC | 12m |
| WMT5AC | WMT | Mollis Airport (LSZM) | Malpensa International Airport (LIMC) | 2026-08-07 13:59 UTC | 2026-08-07 19:37 UTC | 5h 37m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-07 19:22 UTC | 2026-08-07 19:37 UTC | 14m |
| SCHNR06 | SCH | Los Alamitos Army Air Field (KSLI) | Los Alamitos Army Air Field (KSLI) | 2026-08-07 19:20 UTC | 2026-08-07 19:31 UTC | 11m |
| MSR706 | EgyptAir | Malpensa International Airport (LIMC) | HE42 (HE42) | 2026-08-07 16:25 UTC | 2026-08-07 19:31 UTC | 3h 5m |
| RYR74RR | Ryanair | Malpensa International Airport (LIMC) | Malpensa International Airport (LIMC) | 2026-08-07 19:10 UTC | 2026-08-07 19:29 UTC | 19m |
| MSR5061 | EgyptAir | Frankfurt-Hahn Airport (EDFH) | HE42 (HE42) | 2026-08-07 16:01 UTC | 2026-08-07 19:27 UTC | 3h 25m |
| PSBTA | PSB | Eurico de Aguiar Salles Airport (SBVT) | Guarapari Airport (SNGA) | 2026-08-07 18:53 UTC | 2026-08-07 19:25 UTC | 32m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-07 19:14 UTC | 2026-08-07 19:25 UTC | 10m |
| TSTR71 | TST | Patuxent River Nas (Trapnell Field) Airport (KNHK) | Webster Nolf Airport (KNUI) | 2026-08-07 18:23 UTC | 2026-08-07 19:22 UTC | 59m |
| TGTUK | TGT | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-07 18:57 UTC | 2026-08-07 19:20 UTC | 22m |
| EJA416 | EJA | Willow Run Airport (KYIP) | Eugene F Kranz Toledo Express Airport (KTOL) | 2026-08-07 19:06 UTC | 2026-08-07 19:19 UTC | 12m |
| N135RF |  | Lee Vining Airport (KO24) | Groveland/Yosemite Airport (KE45) | 2026-08-07 18:41 UTC | 2026-08-07 19:19 UTC | 38m |
| N67BD |  | Boeing Field/King County International Airport (KBFI) | 74WT (74WT) | 2026-08-07 19:04 UTC | 2026-08-07 19:17 UTC | 13m |
| N76KA |  | Wilding Farm Airport (6WA5) | Boeing Field/King County International Airport (KBFI) | 2026-08-07 18:40 UTC | 2026-08-07 19:14 UTC | 33m |
| CXK269 | CXK | Mid-Carolina Regional Airport (KRUQ) | Mid-Carolina Regional Airport (KRUQ) | 2026-08-07 19:11 UTC | 2026-08-07 19:13 UTC | 2m |
| THY1DY | Turkish Airlines | Istanbul Airport (LTFM) | Smolensk North Airport (XUBS) | 2026-08-07 17:10 UTC | 2026-08-07 19:12 UTC | 2h 2m |
| BOE467 | BOE | Boeing Field/King County International Airport (KBFI) | Othello Municipal Airport (KS70) | 2026-08-07 17:54 UTC | 2026-08-07 19:12 UTC | 1h 18m |
| RAM997 | Royal Air Maroc | Francisco de Sá Carneiro Airport (LPPR) | Tit Mellil Airport (GMMT) | 2026-08-07 18:02 UTC | 2026-08-07 19:11 UTC | 1h 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
