# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_12:04:16_UTC-green)

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

**Latest saved flight:** 2026-07-08 12:04:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-08 12:04:16 UTC

- **133,039** saved flights
- **45,097** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **133,039** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,601,852.2 tonnes** estimated CO2 emissions
- **92,860,996 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5400 |
| 2 | SkyWest Airlines | 4906 |
| 3 | EJA | 2610 |
| 4 | IndiGo | 2487 |
| 5 | American Airlines | 2078 |
| 6 | Southwest Airlines | 2000 |
| 7 | ENY | 1669 |
| 8 | Delta Air Lines | 1591 |
| 9 | Lufthansa | 1383 |
| 10 | LATAM Airlines | 1223 |
| 11 | Vueling | 1168 |
| 12 | WIF | 1158 |
| 13 | AZU | 1129 |
| 14 | LXJ | 1020 |
| 15 | AXM | 1019 |
| 16 | Swiss International | 944 |
| 17 | All Nippon Airways | 871 |
| 18 | easyJet | 852 |
| 19 | Alaska Airlines | 845 |
| 20 | QLK | 830 |
| 21 | EJU | 817 |
| 22 | VIV | 734 |
| 23 | AEE | 723 |
| 24 | Cathay Pacific | 719 |
| 25 | Air France | 718 |
| 26 | CXK | 715 |
| 27 | United Airlines | 705 |
| 28 | JetBlue | 700 |
| 29 | MXY | 687 |
| 30 | GLO | 680 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 113951 |
| 2 | 🇪🇸 ES | 8845 |
| 3 | 🇮🇳 IN | 7793 |
| 4 | 🇦🇺 AU | 7700 |
| 5 | 🇧🇷 BR | 7493 |
| 6 | 🇨🇦 CA | 7029 |
| 7 | 🇩🇪 DE | 6957 |
| 8 | 🇮🇹 IT | 6927 |
| 9 | 🇬🇧 GB | 5952 |
| 10 | 🇯🇵 JP | 5719 |
| 11 | 🇫🇷 FR | 5282 |
| 12 | 🇨🇴 CO | 4167 |
| 13 | 🇲🇽 MX | 3877 |
| 14 | 🇬🇷 GR | 3811 |
| 15 | 🇳🇴 NO | 3603 |
| 16 | 🇨🇭 CH | 3437 |
| 17 | 🇹🇷 TR | 3000 |
| 18 | 🇲🇾 MY | 2647 |
| 19 | 🇿🇦 ZA | 2195 |
| 20 | 🇵🇱 PL | 2192 |
| 21 | 🇳🇿 NZ | 2097 |
| 22 | 🇹🇭 TH | 2053 |
| 23 | 🇰🇷 KR | 1973 |
| 24 | 🇵🇭 PH | 1836 |
| 25 | 🇬🇹 GT | 1808 |
| 26 | 🇲🇦 MA | 1413 |
| 27 | 🇲🇪 ME | 1323 |
| 28 | 🇳🇱 NL | 1250 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1179 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2771 |
| 2 | Denver International Airport |  | US | 2250 |
| 3 | Tokyo International Airport |  | JP | 1870 |
| 4 | Indira Gandhi International Airport |  | IN | 1721 |
| 5 | Harry Reid International Airport |  | US | 1651 |
| 6 | Guaymaral Airport |  | CO | 1621 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1563 |
| 8 | Zurich Airport |  | CH | 1480 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1412 |
| 10 | La Aurora Airport |  | GT | 1396 |
| 11 | Frankfurt am Main International Airport |  | DE | 1339 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1282 |
| 13 | Chicago O'Hare International Airport |  | US | 1275 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1184 |
| 16 | Salt Lake City International Airport |  | US | 1181 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1151 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1089 |
| 19 | Madrid Barajas International Airport |  | ES | 1089 |
| 20 | Capua Airport |  | IT | 1087 |
| 21 | Congonhas Airport |  | BR | 1061 |
| 22 | Kuala Lumpur International Airport |  | MY | 1029 |
| 23 | Charlotte/Douglas International Airport |  | US | 986 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 966 |
| 25 | Charles de Gaulle International Airport |  | FR | 957 |
| 26 | Bengaluru International Airport |  | IN | 939 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 911 |
| 28 | Malpensa International Airport |  | IT | 883 |
| 29 | Ninoy Aquino International Airport |  | PH | 853 |
| 30 | Daniel K Inouye International Airport |  | US | 830 |
| 31 | Barcelona International Airport |  | ES | 819 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 812 |
| 33 | Tenerife Norte Airport |  | ES | 800 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 781 |
| 35 | Calgary International Airport |  | CA | 775 |
| 36 | Seattle-Tacoma International Airport |  | US | 766 |
| 37 | Scottsdale Airport |  | US | 761 |
| 38 | Viracopos International Airport |  | BR | 758 |
| 39 | Vitoria/Foronda Airport |  | ES | 758 |
| 40 | Amsterdam Airport Schiphol |  | NL | 751 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 681 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 482 | 21m | 244 km | 2,029.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 333 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 322 | 1h 10m | 770 km | 4,277.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 285 | 14m | 114 km | 559.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 251 | 26m | 275 km | 1,189.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 242 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 194 | 22m | 55 km | 184.4 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 185 | 26m | 215 km | 685.2 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 185 | 44m | 241 km | 768.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 184 | 20m | 99 km | 315.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 179 | 1h 46m | 1,423 km | 4,392.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 179 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 162 | 18m | 144 km | 403.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 159 | 44m | 452 km | 1,239.2 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 156 | 1h 1m | 695 km | 1,870.0 t |
| 26 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 151 | 1h 38m | 1,156 km | 3,012.4 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GRIFN69 | GRI | Laupheim Airport (ETHL) | Laupheim Airport (ETHL) | 2026-07-08 11:30 UTC | 2026-07-08 12:04 UTC | 33m |
| JJA1395 | JJA | Incheon International Airport (RKSI) | Kansai International Airport (RJBB) | 2026-07-08 10:29 UTC | 2026-07-08 11:59 UTC | 1h 29m |
| N710HF |  | Schaumburg Regional Airport (K06C) | Chicago Midway International Airport (KMDW) | 2026-07-08 11:27 UTC | 2026-07-08 11:57 UTC | 30m |
| YOI | YOI | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-08 11:11 UTC | 2026-07-08 11:55 UTC | 43m |
| GTI537 | GTI | Miami International Airport (KMIA) | Fairview Airport (CEB5) | 2026-07-08 06:27 UTC | 2026-07-08 11:54 UTC | 5h 27m |
| EJA443 | EJA | Reading Regional/Carl A Spaatz Field (KRDG) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-07-08 11:28 UTC | 2026-07-08 11:44 UTC | 15m |
| N324AM |  | Green Bay/Austin Straubel International Airport (KGRB) | Pine Grove Airport (WI42) | 2026-07-08 11:18 UTC | 2026-07-08 11:40 UTC | 22m |
| BBC373 | BBC | VGZR (VGZR) | Tribhuvan International Airport (VNKT) | 2026-07-08 10:26 UTC | 2026-07-08 11:36 UTC | 1h 9m |
| KTR | KTR | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-08 11:09 UTC | 2026-07-08 11:26 UTC | 17m |
| BGA213J | BGA | Toulouse-Blagnac Airport (LFBO) | Hamburg-Finkenwerder Airport (EDHI) | 2026-07-08 09:07 UTC | 2026-07-08 11:26 UTC | 2h 19m |
| VLG8026 | Vueling | Paris-Orly Airport (LFPO) | Calaf-Sallavinera Airport (LECF) | 2026-07-08 10:15 UTC | 2026-07-08 11:26 UTC | 1h 10m |
| CXK119 | CXK | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-07-08 11:02 UTC | 2026-07-08 11:25 UTC | 22m |
| FDR515 | FDR | O. R. Tambo International Airport (FAOR) | Pilanesberg International Airport (FAPN) | 2026-07-08 10:51 UTC | 2026-07-08 11:23 UTC | 32m |
| JANET33 | JAN | Harry Reid International Airport (KLAS) | KDRA (KDRA) | 2026-07-08 11:11 UTC | 2026-07-08 11:22 UTC | 10m |
| RYR65BP | Ryanair | Dublin Airport (EIDW) | Birmingham International Airport (EGBB) | 2026-07-08 10:38 UTC | 2026-07-08 11:16 UTC | 37m |
| N48757 |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-07-08 11:07 UTC | 2026-07-08 11:15 UTC | 7m |
| AUA617 | Austrian Airlines | Vienna International Airport (LOWW) | Otocac Airport (LDRO) | 2026-07-08 10:38 UTC | 2026-07-08 11:14 UTC | 36m |
| TRF547 | TRF | Addison Airport (KADS) | Terrell Municipal Airport (KTRL) | 2026-07-08 10:40 UTC | 2026-07-08 11:11 UTC | 31m |
| DHL00 | DHL | Bordeaux-Merignac (BA 106) Airport (LFBD) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-07-08 10:52 UTC | 2026-07-08 11:10 UTC | 17m |
| N194W |  | New York Stewart International Airport (KSWF) | Princeton Municipal Airport (KPNN) | 2026-07-08 10:21 UTC | 2026-07-08 11:09 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
