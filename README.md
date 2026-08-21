# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_13:03:14_UTC-green)

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

**Latest saved flight:** 2026-08-21 13:03:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 13:03:14 UTC

- **222,048** saved flights
- **69,489** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **222,048** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,673,964.3 tonnes** estimated CO2 emissions
- **155,012,423 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8902 |
| 2 | SkyWest Airlines | 7891 |
| 3 | EJA | 4289 |
| 4 | IndiGo | 3771 |
| 5 | American Airlines | 3671 |
| 6 | Southwest Airlines | 3491 |
| 7 | Delta Air Lines | 2852 |
| 8 | ENY | 2724 |
| 9 | LATAM Airlines | 2109 |
| 10 | AZU | 2035 |
| 11 | Vueling | 1872 |
| 12 | Lufthansa | 1837 |
| 13 | WIF | 1776 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1537 |
| 16 | Swiss International | 1477 |
| 17 | AXM | 1466 |
| 18 | QLK | 1405 |
| 19 | United Airlines | 1391 |
| 20 | EJU | 1388 |
| 21 | Alaska Airlines | 1353 |
| 22 | All Nippon Airways | 1332 |
| 23 | PGT | 1217 |
| 24 | GLO | 1212 |
| 25 | VIV | 1206 |
| 26 | Air France | 1204 |
| 27 | WMT | 1182 |
| 28 | Wizz Air | 1140 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1109 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186362 |
| 2 | 🇪🇸 ES | 14237 |
| 3 | 🇧🇷 BR | 12815 |
| 4 | 🇦🇺 AU | 12651 |
| 5 | 🇨🇦 CA | 12253 |
| 6 | 🇮🇹 IT | 11824 |
| 7 | 🇮🇳 IN | 11763 |
| 8 | 🇩🇪 DE | 10963 |
| 9 | 🇬🇧 GB | 10418 |
| 10 | 🇨🇴 CO | 9121 |
| 11 | 🇯🇵 JP | 9053 |
| 12 | 🇫🇷 FR | 8854 |
| 13 | 🇬🇷 GR | 6485 |
| 14 | 🇹🇷 TR | 6443 |
| 15 | 🇲🇽 MX | 6157 |
| 16 | 🇨🇭 CH | 5857 |
| 17 | 🇳🇴 NO | 5522 |
| 18 | 🇲🇾 MY | 3883 |
| 19 | 🇿🇦 ZA | 3821 |
| 20 | 🇹🇭 TH | 3756 |
| 21 | 🇵🇱 PL | 3685 |
| 22 | 🇳🇿 NZ | 3089 |
| 23 | 🇵🇭 PH | 3016 |
| 24 | 🇬🇹 GT | 2796 |
| 25 | 🇰🇷 KR | 2656 |
| 26 | 🇭🇷 HR | 2476 |
| 27 | 🇲🇦 MA | 2233 |
| 28 | 🇳🇱 NL | 1971 |
| 29 | 🇲🇪 ME | 1970 |
| 30 | 🇮🇩 ID | 1900 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4649 |
| 2 | Denver International Airport |  | US | 3615 |
| 3 | Tokyo International Airport |  | JP | 2714 |
| 4 | Indira Gandhi International Airport |  | IN | 2701 |
| 5 | Guaymaral Airport |  | CO | 2610 |
| 6 | Harry Reid International Airport |  | US | 2444 |
| 7 | Zurich Airport |  | CH | 2302 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2276 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2255 |
| 10 | La Aurora Airport |  | GT | 2130 |
| 11 | El Dorado International Airport |  | CO | 2076 |
| 12 | Chicago O'Hare International Airport |  | US | 2026 |
| 13 | Salt Lake City International Airport |  | US | 1948 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1909 |
| 15 | Congonhas Airport |  | BR | 1871 |
| 16 | Frankfurt am Main International Airport |  | DE | 1802 |
| 17 | Madrid Barajas International Airport |  | ES | 1739 |
| 18 | Capua Airport |  | IT | 1696 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1661 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1635 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1587 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1555 |
| 25 | Charles de Gaulle International Airport |  | FR | 1529 |
| 26 | Charlotte/Douglas International Airport |  | US | 1471 |
| 27 | Ninoy Aquino International Airport |  | PH | 1436 |
| 28 | Kuala Lumpur International Airport |  | MY | 1418 |
| 29 | Barcelona International Airport |  | ES | 1368 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1346 |
| 31 | Bengaluru International Airport |  | IN | 1332 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1315 |
| 33 | Seattle-Tacoma International Airport |  | US | 1313 |
| 34 | Viracopos International Airport |  | BR | 1301 |
| 35 | Calgary International Airport |  | CA | 1256 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1239 |
| 37 | Oslo Gardermoen Airport |  | NO | 1237 |
| 38 | Don Mueang International Airport |  | TH | 1235 |
| 39 | Vitoria/Foronda Airport |  | ES | 1232 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1193 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1066 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 800 | 21m | 244 km | 3,368.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 556 | 1h 7m | 770 km | 7,386.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 499 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 499 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 374 | 27m | 275 km | 1,772.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 351 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 330 | 1h 50m | 1,423 km | 8,098.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 325 | 44m | 241 km | 1,350.0 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 295 | 21m | 250 km | 1,274.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 279 | 1h 39m | 1,156 km | 5,565.9 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 277 | 24m | 218 km | 1,043.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 273 | 27m | 215 km | 1,011.1 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 273 | 19m | 99 km | 467.6 t |
| 20 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 271 | 44m | 555 km | 2,595.0 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 253 | 19m | 144 km | 629.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 239 | 1h 49m | 1,304 km | 5,376.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 233 | 28m | 152 km | 608.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6018K |  | Atlanta Regional Falcon Field (KFFC) | K4A7 (K4A7) | 2026-08-21 12:47 UTC | 2026-08-21 13:03 UTC | 15m |
| N98FF |  | KFTG (KFTG) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-21 12:15 UTC | 2026-08-21 13:02 UTC | 46m |
| N275CV |  | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-08-21 12:25 UTC | 2026-08-21 12:59 UTC | 34m |
| TVS9Q6 | TVS | Václav Havel Airport (LKPR) | Karain Airport (LTXE) | 2026-08-21 10:02 UTC | 2026-08-21 12:58 UTC | 2h 55m |
| N789TX |  | Arlington Municipal Airport (KGKY) | Tyler Pounds Regional Airport (KTYR) | 2026-08-21 12:24 UTC | 2026-08-21 12:56 UTC | 32m |
| N727BR |  | Chicago Executive Airport (KPWK) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-21 11:50 UTC | 2026-08-21 12:51 UTC | 1h 0m |
| AFL2126 | AFL | Batumi International Airport (UGSB) | Isparta Airport (LTBM) | 2026-08-21 10:58 UTC | 2026-08-21 12:48 UTC | 1h 49m |
| N5NJ |  | NJ47 (NJ47) | Somerset Airport (KSMQ) | 2026-08-21 12:26 UTC | 2026-08-21 12:48 UTC | 21m |
| DENTS62 | DEN | Enterprise Municipal Airport (KEDN) | Enterprise Municipal Airport (KEDN) | 2026-08-21 12:27 UTC | 2026-08-21 12:47 UTC | 20m |
| ISR336 | ISR | Catania / Fontanarossa Airport (LICC) | Ben Gurion International Airport (LLBG) | 2026-08-21 10:14 UTC | 2026-08-21 12:47 UTC | 2h 32m |
| N17NA |  | Northampton Airport (K7B2) | Northampton Airport (K7B2) | 2026-08-21 12:33 UTC | 2026-08-21 12:47 UTC | 13m |
| DHK528 | DHK | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-08-21 02:26 UTC | 2026-08-21 12:46 UTC | 10h 19m |
| HK5019G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-21 12:30 UTC | 2026-08-21 12:43 UTC | 13m |
| HBKZG | HBK | Nuremberg Airport (EDDN) | Friedrichshafen Airport (EDNY) | 2026-08-21 11:37 UTC | 2026-08-21 12:42 UTC | 1h 5m |
| EZY76EZ | easyJet | London Gatwick Airport (EGKK) | Karain Airport (LTXE) | 2026-08-21 08:47 UTC | 2026-08-21 12:42 UTC | 3h 54m |
| FHPCJ | FHP | Marennes Le Bournet Airport (LFJI) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-08-21 12:32 UTC | 2026-08-21 12:41 UTC | 9m |
| N486LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-21 11:16 UTC | 2026-08-21 12:38 UTC | 1h 21m |
| N527PB |  | Wiley Post Airport (KPWA) | Stillwater Regional Airport (KSWO) | 2026-08-21 12:22 UTC | 2026-08-21 12:34 UTC | 12m |
| FGJBC | FGJ | Quiberon Airport (LFEQ) | Quiberon Airport (LFEQ) | 2026-08-21 12:28 UTC | 2026-08-21 12:34 UTC | 5m |
| THY3445 | Turkish Airlines | Beirut Rafic Hariri International Airport (OLBA) | Isparta Airport (LTBM) | 2026-08-21 11:31 UTC | 2026-08-21 12:33 UTC | 1h 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
