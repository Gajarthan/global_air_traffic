# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_01:05:09_UTC-green)

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

**Latest saved flight:** 2026-06-23 01:05:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-23 01:05:09 UTC

- **117,387** saved flights
- **40,558** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **117,387** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,424,923.1 tonnes** estimated CO2 emissions
- **82,604,238 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4846 |
| 2 | SkyWest Airlines | 4353 |
| 3 | IndiGo | 2271 |
| 4 | EJA | 2270 |
| 5 | American Airlines | 1830 |
| 6 | Southwest Airlines | 1752 |
| 7 | ENY | 1468 |
| 8 | Delta Air Lines | 1385 |
| 9 | Lufthansa | 1296 |
| 10 | Vueling | 1055 |
| 11 | LATAM Airlines | 1038 |
| 12 | WIF | 1034 |
| 13 | AZU | 979 |
| 14 | AXM | 965 |
| 15 | LXJ | 894 |
| 16 | Swiss International | 829 |
| 17 | All Nippon Airways | 808 |
| 18 | Alaska Airlines | 781 |
| 19 | QLK | 759 |
| 20 | easyJet | 749 |
| 21 | EJU | 733 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 658 |
| 24 | VIV | 649 |
| 25 | United Airlines | 645 |
| 26 | Air France | 644 |
| 27 | CXK | 629 |
| 28 | MXY | 620 |
| 29 | AXB | 580 |
| 30 | GLO | 575 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 99217 |
| 2 | 🇪🇸 ES | 7999 |
| 3 | 🇮🇳 IN | 7137 |
| 4 | 🇦🇺 AU | 6967 |
| 5 | 🇧🇷 BR | 6478 |
| 6 | 🇮🇹 IT | 6271 |
| 7 | 🇩🇪 DE | 6243 |
| 8 | 🇨🇦 CA | 6149 |
| 9 | 🇯🇵 JP | 5276 |
| 10 | 🇬🇧 GB | 5123 |
| 11 | 🇫🇷 FR | 4671 |
| 12 | 🇨🇴 CO | 3992 |
| 13 | 🇲🇽 MX | 3455 |
| 14 | 🇬🇷 GR | 3355 |
| 15 | 🇳🇴 NO | 3218 |
| 16 | 🇨🇭 CH | 3007 |
| 17 | 🇲🇾 MY | 2505 |
| 18 | 🇹🇷 TR | 2389 |
| 19 | 🇿🇦 ZA | 1975 |
| 20 | 🇵🇱 PL | 1929 |
| 21 | 🇳🇿 NZ | 1918 |
| 22 | 🇹🇭 TH | 1895 |
| 23 | 🇰🇷 KR | 1892 |
| 24 | 🇵🇭 PH | 1704 |
| 25 | 🇬🇹 GT | 1657 |
| 26 | 🇲🇦 MA | 1275 |
| 27 | 🇲🇴 MO | 1169 |
| 28 | 🇲🇪 ME | 1155 |
| 29 | 🇳🇱 NL | 1130 |
| 30 | 🇭🇷 HR | 1020 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2477 |
| 2 | Denver International Airport |  | US | 1977 |
| 3 | Tokyo International Airport |  | JP | 1748 |
| 4 | Indira Gandhi International Airport |  | IN | 1564 |
| 5 | Guaymaral Airport |  | CO | 1482 |
| 6 | Harry Reid International Airport |  | US | 1465 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1432 |
| 8 | Zurich Airport |  | CH | 1311 |
| 9 | La Aurora Airport |  | GT | 1280 |
| 10 | Frankfurt am Main International Airport |  | DE | 1260 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1246 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1169 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1166 |
| 15 | Chicago O'Hare International Airport |  | US | 1151 |
| 16 | Capua Airport |  | IT | 1016 |
| 17 | Salt Lake City International Airport |  | US | 1008 |
| 18 | Madrid Barajas International Airport |  | ES | 992 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 981 |
| 20 | Kuala Lumpur International Airport |  | MY | 967 |
| 21 | Congonhas Airport |  | BR | 903 |
| 22 | Charlotte/Douglas International Airport |  | US | 893 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 877 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 875 |
| 25 | Bengaluru International Airport |  | IN | 863 |
| 26 | Charles de Gaulle International Airport |  | FR | 862 |
| 27 | Malpensa International Airport |  | IT | 831 |
| 28 | Ninoy Aquino International Airport |  | PH | 787 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 769 |
| 30 | Daniel K Inouye International Airport |  | US | 762 |
| 31 | Tenerife Norte Airport |  | ES | 759 |
| 32 | Barcelona International Airport |  | ES | 744 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 734 |
| 34 | Calgary International Airport |  | CA | 688 |
| 35 | Amsterdam Airport Schiphol |  | NL | 687 |
| 36 | Don Mueang International Airport |  | TH | 686 |
| 37 | Vitoria/Foronda Airport |  | ES | 686 |
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
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 288 | 1h 25m | 910 km | 4,519.4 t |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 7 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 283 | 1h 10m | 770 km | 3,759.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 232 | 26m | 275 km | 1,099.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 231 | 19m | 165 km | 657.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 217 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 175 | 22m | 55 km | 166.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 170 | 20m | 99 km | 291.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 168 | 26m | 215 km | 622.2 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 160 | 27m | 152 km | 418.1 t |
| 18 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 156 | 44m | 241 km | 648.0 t |
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
| N864SF |  | Nikolai Airport (PAFS) | Mc Grath Airport (PAMC) | 2026-06-23 00:49 UTC | 2026-06-23 01:05 UTC | 15m |
| SKW5480 | SkyWest Airlines | San Francisco International Airport (KSFO) | Hell'Er High Water Airport (45CL) | 2026-06-23 00:27 UTC | 2026-06-23 00:57 UTC | 29m |
| N3221B |  | Dallas Love Field (KDAL) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-06-22 23:20 UTC | 2026-06-23 00:52 UTC | 1h 31m |
| ZEH | ZEH | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-23 00:05 UTC | 2026-06-23 00:49 UTC | 43m |
| N813V |  | Dublin Airport (EIDW) | Bangor International Airport (KBGR) | 2026-06-22 18:47 UTC | 2026-06-23 00:49 UTC | 6h 1m |
| N4596U |  | Ted Stevens Anchorage International Airport (PANC) | Nugget Bench Airport (33AK) | 2026-06-22 23:57 UTC | 2026-06-23 00:48 UTC | 51m |
| MVK75 | MVK | South St Paul Municipal/Richard E Fleming Field (KSGS) | South St Paul Municipal/Richard E Fleming Field (KSGS) | 2026-06-23 00:30 UTC | 2026-06-23 00:31 UTC | 1m |
| N57UD |  | Fort Lauderdale Executive Airport (KFXE) | Melbourne Orlando International Airport (KMLB) | 2026-06-22 23:09 UTC | 2026-06-23 00:30 UTC | 1h 21m |
| SCPR285 | SCP | Ladd Army Air Field (PAFB) | Tolovana Hot Springs Airport (83AK) | 2026-06-22 23:33 UTC | 2026-06-23 00:29 UTC | 55m |
| N728MG |  | Huntsville Executive Tom Sharp Jr Field (KMDQ) | Parker Field (8NC7) | 2026-06-22 22:44 UTC | 2026-06-23 00:29 UTC | 1h 44m |
| COUGR41 | COU | Northwest Arkansas Ntl Airport (KXNA) | Russellville Regional Airport (KRUE) | 2026-06-23 00:11 UTC | 2026-06-23 00:28 UTC | 17m |
| N177BD |  | Roberts Field (KRDM) | Bombay Farms Airport (OG19) | 2026-06-22 23:49 UTC | 2026-06-23 00:26 UTC | 36m |
| NWX382 | NWX | Bridgeport Municipal Airport (KXBP) | 69XA (69XA) | 2026-06-23 00:13 UTC | 2026-06-23 00:23 UTC | 9m |
| DTF | DTF | Perth Jandakot Airport (YPJT) | Kalannie Airport (YKAE) | 2026-06-22 23:32 UTC | 2026-06-23 00:22 UTC | 50m |
| JAL605 | Japan Airlines | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-06-22 22:53 UTC | 2026-06-23 00:20 UTC | 1h 27m |
| N400NK |  | Logan-Cache Airport (KLGU) | Portland-Hillsboro Airport (KHIO) | 2026-06-22 22:45 UTC | 2026-06-23 00:19 UTC | 1h 34m |
| N304DB |  | Centennial Airport (KAPA) | Bijou Bottom Strip (9CO8) | 2026-06-22 23:53 UTC | 2026-06-23 00:18 UTC | 25m |
| SKW3895 | SkyWest Airlines | Salt Lake City International Airport (KSLC) | Logan-Cache Airport (KLGU) | 2026-06-22 23:24 UTC | 2026-06-23 00:14 UTC | 50m |
| HLJ | HLJ | Perth International Airport (YPPH) | Lake Grace Airport (YLGC) | 2026-06-22 23:30 UTC | 2026-06-23 00:12 UTC | 41m |
| ASA1062 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-06-22 23:50 UTC | 2026-06-23 00:12 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
