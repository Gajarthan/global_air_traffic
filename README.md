# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_15:52:06_UTC-green)

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

**Latest saved flight:** 2026-06-22 15:52:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-22 15:52:06 UTC

- **117,262** saved flights
- **40,532** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **117,262** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,423,726.9 tonnes** estimated CO2 emissions
- **82,534,894 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4846 |
| 2 | SkyWest Airlines | 4344 |
| 3 | IndiGo | 2270 |
| 4 | EJA | 2269 |
| 5 | American Airlines | 1827 |
| 6 | Southwest Airlines | 1750 |
| 7 | ENY | 1465 |
| 8 | Delta Air Lines | 1385 |
| 9 | Lufthansa | 1296 |
| 10 | Vueling | 1054 |
| 11 | LATAM Airlines | 1036 |
| 12 | WIF | 1034 |
| 13 | AZU | 977 |
| 14 | AXM | 963 |
| 15 | LXJ | 893 |
| 16 | Swiss International | 829 |
| 17 | All Nippon Airways | 805 |
| 18 | Alaska Airlines | 780 |
| 19 | QLK | 754 |
| 20 | easyJet | 749 |
| 21 | EJU | 733 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 658 |
| 24 | VIV | 648 |
| 25 | United Airlines | 645 |
| 26 | Air France | 644 |
| 27 | CXK | 629 |
| 28 | MXY | 620 |
| 29 | AXB | 580 |
| 30 | GLO | 575 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 99090 |
| 2 | 🇪🇸 ES | 7998 |
| 3 | 🇮🇳 IN | 7136 |
| 4 | 🇦🇺 AU | 6927 |
| 5 | 🇧🇷 BR | 6470 |
| 6 | 🇮🇹 IT | 6270 |
| 7 | 🇩🇪 DE | 6243 |
| 8 | 🇨🇦 CA | 6147 |
| 9 | 🇯🇵 JP | 5256 |
| 10 | 🇬🇧 GB | 5123 |
| 11 | 🇫🇷 FR | 4671 |
| 12 | 🇨🇴 CO | 3992 |
| 13 | 🇲🇽 MX | 3451 |
| 14 | 🇬🇷 GR | 3355 |
| 15 | 🇳🇴 NO | 3218 |
| 16 | 🇨🇭 CH | 3007 |
| 17 | 🇲🇾 MY | 2500 |
| 18 | 🇹🇷 TR | 2387 |
| 19 | 🇿🇦 ZA | 1975 |
| 20 | 🇵🇱 PL | 1929 |
| 21 | 🇳🇿 NZ | 1918 |
| 22 | 🇹🇭 TH | 1895 |
| 23 | 🇰🇷 KR | 1892 |
| 24 | 🇵🇭 PH | 1698 |
| 25 | 🇬🇹 GT | 1657 |
| 26 | 🇲🇦 MA | 1275 |
| 27 | 🇲🇴 MO | 1169 |
| 28 | 🇲🇪 ME | 1154 |
| 29 | 🇳🇱 NL | 1130 |
| 30 | 🇭🇷 HR | 1020 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2472 |
| 2 | Denver International Airport |  | US | 1970 |
| 3 | Tokyo International Airport |  | JP | 1742 |
| 4 | Indira Gandhi International Airport |  | IN | 1564 |
| 5 | Guaymaral Airport |  | CO | 1482 |
| 6 | Harry Reid International Airport |  | US | 1462 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1432 |
| 8 | Zurich Airport |  | CH | 1311 |
| 9 | La Aurora Airport |  | GT | 1280 |
| 10 | Frankfurt am Main International Airport |  | DE | 1260 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1246 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1169 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1163 |
| 15 | Chicago O'Hare International Airport |  | US | 1151 |
| 16 | Capua Airport |  | IT | 1016 |
| 17 | Salt Lake City International Airport |  | US | 1003 |
| 18 | Madrid Barajas International Airport |  | ES | 992 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 981 |
| 20 | Kuala Lumpur International Airport |  | MY | 965 |
| 21 | Congonhas Airport |  | BR | 902 |
| 22 | Charlotte/Douglas International Airport |  | US | 893 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 872 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 871 |
| 25 | Bengaluru International Airport |  | IN | 863 |
| 26 | Charles de Gaulle International Airport |  | FR | 862 |
| 27 | Malpensa International Airport |  | IT | 831 |
| 28 | Ninoy Aquino International Airport |  | PH | 784 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 767 |
| 30 | Daniel K Inouye International Airport |  | US | 761 |
| 31 | Tenerife Norte Airport |  | ES | 759 |
| 32 | Barcelona International Airport |  | ES | 743 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 734 |
| 34 | Calgary International Airport |  | CA | 688 |
| 35 | Amsterdam Airport Schiphol |  | NL | 687 |
| 36 | Don Mueang International Airport |  | TH | 686 |
| 37 | Vitoria/Foronda Airport |  | ES | 686 |
| 38 | Seattle-Tacoma International Airport |  | US | 673 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 671 |
| 40 | Viracopos International Airport |  | BR | 665 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 615 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 425 | 21m | 244 km | 1,789.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 313 | 24m | 225 km | 1,214.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 303 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 286 | 1h 25m | 910 km | 4,488.0 t |
| 7 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 282 | 1h 10m | 770 km | 3,746.2 t |
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
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 154 | 31m | 369 km | 980.2 t |
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
| N8314W |  | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-06-22 14:47 UTC | 2026-06-22 15:52 UTC | 1h 4m |
| N3038N |  | Brigham City Regional Airport (KBMC) | Brigham City Regional Airport (KBMC) | 2026-06-22 14:42 UTC | 2026-06-22 15:46 UTC | 1h 3m |
| N35543 |  | Dallas Executive Airport (KRBD) | Dallas Executive Airport (KRBD) | 2026-06-22 15:18 UTC | 2026-06-22 15:45 UTC | 27m |
| ASI84 | ASI | Phoenix Deer Valley Airport (KDVT) | Wickenburg Municipal Airport (KE25) | 2026-06-22 14:32 UTC | 2026-06-22 15:45 UTC | 1h 12m |
| N917CD |  | City Of Colorado Springs Municipal Airport (KCOS) | 1CO7 (1CO7) | 2026-06-22 15:03 UTC | 2026-06-22 15:43 UTC | 40m |
| ETD36V | Etihad Airways | Malpensa International Airport (LIMC) | Futaysi Airport (OMAF) | 2026-06-22 10:02 UTC | 2026-06-22 15:41 UTC | 5h 38m |
| N423FP |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-06-22 15:31 UTC | 2026-06-22 15:40 UTC | 9m |
| CONGO63 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-06-22 15:24 UTC | 2026-06-22 15:39 UTC | 14m |
| N928GP |  | Bishop-Windham Airport (K07R) | Bishop-Windham Airport (K07R) | 2026-06-22 14:13 UTC | 2026-06-22 15:38 UTC | 1h 25m |
| ORO1042 | ORO | Cannes-Mandelieu Airport (LFMD) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-22 15:19 UTC | 2026-06-22 15:37 UTC | 17m |
| DESERT7 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-06-22 15:23 UTC | 2026-06-22 15:36 UTC | 13m |
| CXK1004 | CXK | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-06-22 15:21 UTC | 2026-06-22 15:35 UTC | 13m |
| ETD3XA | Etihad Airways | Dublin Airport (EIDW) | Al Bateen Executive Airport (OMAD) | 2026-06-22 08:29 UTC | 2026-06-22 15:33 UTC | 7h 4m |
| N470BL |  | Pensacola International Airport (KPNS) | Mc Kinnon Airpark (48FL) | 2026-06-22 15:06 UTC | 2026-06-22 15:32 UTC | 26m |
| CXK624 | CXK | Sacramento Executive Airport (KSAC) | Mc Clellan Airfield (KMCC) | 2026-06-22 15:18 UTC | 2026-06-22 15:31 UTC | 12m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-06-22 13:57 UTC | 2026-06-22 15:25 UTC | 1h 27m |
| HZAL65 | HZA | Ras Tanura Airport (OERT) | Ras Tanura Airport (OERT) | 2026-06-22 15:21 UTC | 2026-06-22 15:22 UTC | 1m |
| N15AN |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-06-22 15:16 UTC | 2026-06-22 15:22 UTC | 5m |
| N717SK |  | UT09 (UT09) | K36U (K36U) | 2026-06-22 14:59 UTC | 2026-06-22 15:21 UTC | 22m |
| N158U |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-06-22 14:47 UTC | 2026-06-22 15:18 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
