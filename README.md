# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_18:24:24_UTC-green)

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

**Latest saved flight:** 2026-07-25 18:24:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 18:24:24 UTC

- **150,780** saved flights
- **50,157** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **150,780** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,804,037.8 tonnes** estimated CO2 emissions
- **104,581,902 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6085 |
| 2 | SkyWest Airlines | 5508 |
| 3 | EJA | 2986 |
| 4 | IndiGo | 2694 |
| 5 | American Airlines | 2392 |
| 6 | Southwest Airlines | 2288 |
| 7 | ENY | 1880 |
| 8 | Delta Air Lines | 1772 |
| 9 | Lufthansa | 1477 |
| 10 | LATAM Airlines | 1393 |
| 11 | AZU | 1308 |
| 12 | WIF | 1276 |
| 13 | Vueling | 1269 |
| 14 | LXJ | 1161 |
| 15 | AXM | 1081 |
| 16 | Swiss International | 1061 |
| 17 | easyJet | 979 |
| 18 | All Nippon Airways | 952 |
| 19 | Alaska Airlines | 937 |
| 20 | QLK | 931 |
| 21 | EJU | 924 |
| 22 | VIV | 831 |
| 23 | CXK | 809 |
| 24 | AEE | 795 |
| 25 | MXY | 788 |
| 26 | Air France | 786 |
| 27 | JetBlue | 786 |
| 28 | GLO | 783 |
| 29 | Cathay Pacific | 781 |
| 30 | United Airlines | 773 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 129965 |
| 2 | 🇪🇸 ES | 9748 |
| 3 | 🇧🇷 BR | 8541 |
| 4 | 🇦🇺 AU | 8505 |
| 5 | 🇮🇳 IN | 8478 |
| 6 | 🇨🇦 CA | 8056 |
| 7 | 🇮🇹 IT | 7805 |
| 8 | 🇩🇪 DE | 7741 |
| 9 | 🇬🇧 GB | 6912 |
| 10 | 🇯🇵 JP | 6249 |
| 11 | 🇫🇷 FR | 5978 |
| 12 | 🇨🇴 CO | 5126 |
| 13 | 🇲🇽 MX | 4350 |
| 14 | 🇬🇷 GR | 4287 |
| 15 | 🇳🇴 NO | 3998 |
| 16 | 🇨🇭 CH | 3972 |
| 17 | 🇹🇷 TR | 3570 |
| 18 | 🇲🇾 MY | 2817 |
| 19 | 🇵🇱 PL | 2562 |
| 20 | 🇿🇦 ZA | 2460 |
| 21 | 🇳🇿 NZ | 2267 |
| 22 | 🇹🇭 TH | 2192 |
| 23 | 🇰🇷 KR | 2065 |
| 24 | 🇵🇭 PH | 2005 |
| 25 | 🇬🇹 GT | 1972 |
| 26 | 🇲🇦 MA | 1533 |
| 27 | 🇲🇪 ME | 1480 |
| 28 | 🇳🇱 NL | 1392 |
| 29 | 🇭🇷 HR | 1378 |
| 30 | 🇲🇴 MO | 1249 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3099 |
| 2 | Denver International Airport |  | US | 2523 |
| 3 | Tokyo International Airport |  | JP | 1993 |
| 4 | Guaymaral Airport |  | CO | 1897 |
| 5 | Indira Gandhi International Airport |  | IN | 1882 |
| 6 | Harry Reid International Airport |  | US | 1863 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1693 |
| 8 | Zurich Airport |  | CH | 1645 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1580 |
| 10 | La Aurora Airport |  | GT | 1527 |
| 11 | Frankfurt am Main International Airport |  | DE | 1428 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1414 |
| 13 | Chicago O'Hare International Airport |  | US | 1392 |
| 14 | El Dorado International Airport |  | CO | 1357 |
| 15 | Salt Lake City International Airport |  | US | 1355 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1290 |
| 17 | Macau International Airport |  | MO | 1249 |
| 18 | Congonhas Airport |  | BR | 1224 |
| 19 | Capua Airport |  | IT | 1200 |
| 20 | Madrid Barajas International Airport |  | ES | 1199 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1168 |
| 22 | Kuala Lumpur International Airport |  | MY | 1085 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1076 |
| 24 | Charlotte/Douglas International Airport |  | US | 1072 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1060 |
| 26 | Charles de Gaulle International Airport |  | FR | 1037 |
| 27 | Bengaluru International Airport |  | IN | 1011 |
| 28 | Malpensa International Airport |  | IT | 987 |
| 29 | Ninoy Aquino International Airport |  | PH | 939 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 913 |
| 31 | Barcelona International Airport |  | ES | 905 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 900 |
| 33 | Daniel K Inouye International Airport |  | US | 900 |
| 34 | Tenerife Norte Airport |  | ES | 865 |
| 35 | Seattle-Tacoma International Airport |  | US | 862 |
| 36 | Calgary International Airport |  | CA | 856 |
| 37 | Viracopos International Airport |  | BR | 852 |
| 38 | Scottsdale Airport |  | US | 851 |
| 39 | Amsterdam Airport Schiphol |  | NL | 836 |
| 40 | Oslo Gardermoen Airport |  | NO | 828 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 800 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 546 | 21m | 244 km | 2,299.1 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 367 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 364 | 24m | 225 km | 1,412.1 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 353 | 1h 9m | 770 km | 4,689.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 277 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 269 | 27m | 275 km | 1,274.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 225 | 22m | 55 km | 213.9 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 205 | 44m | 241 km | 851.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 204 | 1h 47m | 1,423 km | 5,006.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 198 | 20m | 99 km | 339.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 184 | 27m | 152 km | 480.9 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 179 | 1h 16m | 961 km | 2,967.0 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 177 | 31m | 369 km | 1,126.6 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 177 | 18m | 144 km | 440.3 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 177 | 30m | 49 km | 149.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 175 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 173 | 44m | 452 km | 1,348.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 170 | 1h 1m | 695 km | 2,037.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 169 | 1h 39m | 1,156 km | 3,371.5 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DLH6RW | Lufthansa | Pula Airport (LDPL) | Frankfurt am Main International Airport (EDDF) | 2026-07-25 17:16 UTC | 2026-07-25 18:24 UTC | 1h 8m |
| DLH12K | Lufthansa | Barcelona International Airport (LEBL) | Frankfurt am Main International Airport (EDDF) | 2026-07-25 16:53 UTC | 2026-07-25 18:22 UTC | 1h 29m |
| CGNND | CGN | Colonial Airport (NY24) | Colonial Airport (NY24) | 2026-07-25 17:54 UTC | 2026-07-25 18:16 UTC | 21m |
| TKR160 | TKR | Boise Air Trml/Gowen Field (KBOI) | Josephine Ranch Airport (2ID3) | 2026-07-25 18:02 UTC | 2026-07-25 18:14 UTC | 12m |
| SCR137 | SCR | Nice-Cote d'Azur Airport (LFMN) | London Biggin Hill Airport (EGKB) | 2026-07-25 16:25 UTC | 2026-07-25 18:13 UTC | 1h 48m |
| MSHRM | MSH | London Stansted Airport (EGSS) | London City Airport (EGLC) | 2026-07-25 17:54 UTC | 2026-07-25 18:11 UTC | 16m |
| TKR140 | TKR | Boise Air Trml/Gowen Field (KBOI) | Josephine Ranch Airport (2ID3) | 2026-07-25 17:51 UTC | 2026-07-25 18:08 UTC | 16m |
| N602LA |  | Mount Hawley Auxiliary Airport (K3MY) | 75LL (75LL) | 2026-07-25 17:54 UTC | 2026-07-25 18:06 UTC | 12m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-07-25 17:45 UTC | 2026-07-25 18:04 UTC | 19m |
| N987MT |  | Santa Monica Municipal Airport (KSMO) | Van Nuys Airport (KVNY) | 2026-07-25 17:28 UTC | 2026-07-25 18:04 UTC | 35m |
| DEALZ | DEA | Varrelbusch Airport (EDWU) | Varrelbusch Airport (EDWU) | 2026-07-25 17:31 UTC | 2026-07-25 18:02 UTC | 31m |
| N817FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-07-25 17:16 UTC | 2026-07-25 17:59 UTC | 42m |
| VAR528 | VAR | Avi Suquilla Airport (KP20) | Lake Havasu City Airport (KHII) | 2026-07-25 17:33 UTC | 2026-07-25 17:59 UTC | 25m |
| N531LM |  | Fairbanks International Airport (PAFA) | Ruby Airport (PARY) | 2026-07-25 17:12 UTC | 2026-07-25 17:58 UTC | 45m |
| N316AS |  | Greenwood Lake Airport (K4N1) | Greenwood Lake Airport (K4N1) | 2026-07-25 17:43 UTC | 2026-07-25 17:58 UTC | 14m |
| N36MN |  | KO70 (KO70) | Truckee-Tahoe Airport (KTRK) | 2026-07-25 17:36 UTC | 2026-07-25 17:57 UTC | 21m |
| N43VS |  | 5MN7 (5MN7) | Park Falls Municipal Airport (KPKF) | 2026-07-25 17:27 UTC | 2026-07-25 17:54 UTC | 26m |
| N98VL |  | Pillow Hill Airport (3LL4) | Pillow Hill Airport (3LL4) | 2026-07-25 17:43 UTC | 2026-07-25 17:53 UTC | 10m |
| N132TS |  | Logan-Cache Airport (KLGU) | Downey/Hyde Memorial/ Airport (KU58) | 2026-07-25 17:34 UTC | 2026-07-25 17:53 UTC | 19m |
| N81ER |  | Oakland County International Airport (KPTK) | K8M8 (K8M8) | 2026-07-25 17:25 UTC | 2026-07-25 17:51 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
