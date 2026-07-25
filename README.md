# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_17:13:56_UTC-green)

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

**Latest saved flight:** 2026-07-25 17:13:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 17:13:56 UTC

- **150,566** saved flights
- **50,087** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **150,566** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,801,398.1 tonnes** estimated CO2 emissions
- **104,428,875 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6076 |
| 2 | SkyWest Airlines | 5498 |
| 3 | EJA | 2978 |
| 4 | IndiGo | 2692 |
| 5 | American Airlines | 2388 |
| 6 | Southwest Airlines | 2280 |
| 7 | ENY | 1874 |
| 8 | Delta Air Lines | 1770 |
| 9 | Lufthansa | 1475 |
| 10 | LATAM Airlines | 1389 |
| 11 | AZU | 1305 |
| 12 | WIF | 1276 |
| 13 | Vueling | 1269 |
| 14 | LXJ | 1160 |
| 15 | AXM | 1081 |
| 16 | Swiss International | 1061 |
| 17 | easyJet | 975 |
| 18 | All Nippon Airways | 952 |
| 19 | Alaska Airlines | 936 |
| 20 | QLK | 931 |
| 21 | EJU | 919 |
| 22 | VIV | 831 |
| 23 | CXK | 809 |
| 24 | AEE | 795 |
| 25 | MXY | 787 |
| 26 | Air France | 785 |
| 27 | GLO | 783 |
| 28 | JetBlue | 783 |
| 29 | Cathay Pacific | 781 |
| 30 | United Airlines | 773 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 129732 |
| 2 | 🇪🇸 ES | 9739 |
| 3 | 🇧🇷 BR | 8523 |
| 4 | 🇦🇺 AU | 8505 |
| 5 | 🇮🇳 IN | 8474 |
| 6 | 🇨🇦 CA | 8046 |
| 7 | 🇮🇹 IT | 7789 |
| 8 | 🇩🇪 DE | 7734 |
| 9 | 🇬🇧 GB | 6899 |
| 10 | 🇯🇵 JP | 6249 |
| 11 | 🇫🇷 FR | 5969 |
| 12 | 🇨🇴 CO | 5108 |
| 13 | 🇲🇽 MX | 4347 |
| 14 | 🇬🇷 GR | 4284 |
| 15 | 🇳🇴 NO | 3998 |
| 16 | 🇨🇭 CH | 3966 |
| 17 | 🇹🇷 TR | 3561 |
| 18 | 🇲🇾 MY | 2817 |
| 19 | 🇵🇱 PL | 2560 |
| 20 | 🇿🇦 ZA | 2458 |
| 21 | 🇳🇿 NZ | 2267 |
| 22 | 🇹🇭 TH | 2192 |
| 23 | 🇰🇷 KR | 2065 |
| 24 | 🇵🇭 PH | 2005 |
| 25 | 🇬🇹 GT | 1967 |
| 26 | 🇲🇦 MA | 1531 |
| 27 | 🇲🇪 ME | 1479 |
| 28 | 🇳🇱 NL | 1391 |
| 29 | 🇭🇷 HR | 1374 |
| 30 | 🇲🇴 MO | 1249 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3094 |
| 2 | Denver International Airport |  | US | 2522 |
| 3 | Tokyo International Airport |  | JP | 1993 |
| 4 | Guaymaral Airport |  | CO | 1892 |
| 5 | Indira Gandhi International Airport |  | IN | 1879 |
| 6 | Harry Reid International Airport |  | US | 1860 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1693 |
| 8 | Zurich Airport |  | CH | 1644 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1578 |
| 10 | La Aurora Airport |  | GT | 1523 |
| 11 | Frankfurt am Main International Airport |  | DE | 1426 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1410 |
| 13 | Chicago O'Hare International Airport |  | US | 1387 |
| 14 | El Dorado International Airport |  | CO | 1355 |
| 15 | Salt Lake City International Airport |  | US | 1350 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1289 |
| 17 | Macau International Airport |  | MO | 1249 |
| 18 | Congonhas Airport |  | BR | 1221 |
| 19 | Madrid Barajas International Airport |  | ES | 1199 |
| 20 | Capua Airport |  | IT | 1199 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1166 |
| 22 | Kuala Lumpur International Airport |  | MY | 1085 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1076 |
| 24 | Charlotte/Douglas International Airport |  | US | 1071 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1058 |
| 26 | Charles de Gaulle International Airport |  | FR | 1036 |
| 27 | Bengaluru International Airport |  | IN | 1011 |
| 28 | Malpensa International Airport |  | IT | 984 |
| 29 | Ninoy Aquino International Airport |  | PH | 939 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 913 |
| 31 | Barcelona International Airport |  | ES | 904 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 900 |
| 33 | Daniel K Inouye International Airport |  | US | 898 |
| 34 | Tenerife Norte Airport |  | ES | 864 |
| 35 | Seattle-Tacoma International Airport |  | US | 861 |
| 36 | Calgary International Airport |  | CA | 855 |
| 37 | Viracopos International Airport |  | BR | 851 |
| 38 | Scottsdale Airport |  | US | 851 |
| 39 | Amsterdam Airport Schiphol |  | NL | 835 |
| 40 | Oslo Gardermoen Airport |  | NO | 828 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 798 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 544 | 21m | 244 km | 2,290.6 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 366 | 9m | - | - |
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
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 202 | 1h 47m | 1,423 km | 4,957.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 197 | 20m | 99 km | 337.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 190 | 20m | 250 km | 820.7 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 184 | 27m | 152 km | 480.9 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 178 | 1h 16m | 961 km | 2,950.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 177 | 31m | 369 km | 1,126.6 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 177 | 18m | 144 km | 440.3 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 175 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 173 | 44m | 452 km | 1,348.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 170 | 1h 1m | 695 km | 2,037.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 169 | 1h 39m | 1,156 km | 3,371.5 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL381 | United Airlines | Gioia Del Colle Airport (LIBV) | Newark Liberty International Airport (KEWR) | 2026-07-25 08:01 UTC | 2026-07-25 17:13 UTC | 9h 11m |
| WLDLD28 | WLD | Grand Junction Regional Airport (KGJT) | Shively Field (KSAA) | 2026-07-25 16:19 UTC | 2026-07-25 17:08 UTC | 48m |
| VAR486 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-07-25 15:56 UTC | 2026-07-25 17:08 UTC | 1h 11m |
| N694DA |  | Fort Morgan Municipal Airport (KFMM) | Fort Morgan Municipal Airport (KFMM) | 2026-07-25 16:54 UTC | 2026-07-25 17:06 UTC | 12m |
| N405SW |  | 80XS (80XS) | Dallas Love Field (KDAL) | 2026-07-25 16:40 UTC | 2026-07-25 17:03 UTC | 23m |
| N87RM |  | Perrotti Skyranch Airfield (09ME) | Skydive New England Airport (ME64) | 2026-07-25 15:43 UTC | 2026-07-25 17:02 UTC | 1h 19m |
| N5QD |  | 0PA0 (0PA0) | 0PA0 (0PA0) | 2026-07-25 16:59 UTC | 2026-07-25 16:59 UTC | 0m |
| ALFT5 | ALF | Bellingham International Airport (KBLI) | Anacortes Airport (K74S) | 2026-07-25 16:49 UTC | 2026-07-25 16:58 UTC | 9m |
| DEALZ | DEA | Varrelbusch Airport (EDWU) | Varrelbusch Airport (EDWU) | 2026-07-25 16:35 UTC | 2026-07-25 16:57 UTC | 22m |
| MAFFS6 | MAF | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | Lone Pine/Death Valley Airport (KO26) | 2026-07-25 16:22 UTC | 2026-07-25 16:56 UTC | 34m |
| PHPBL | PHP | Texel Airport (EHTX) | Texel Airport (EHTX) | 2026-07-25 16:37 UTC | 2026-07-25 16:55 UTC | 18m |
| TGSQK | TGS | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-07-25 16:25 UTC | 2026-07-25 16:55 UTC | 29m |
| N7998U |  | Morrow County Airport (K4I9) | Morrow County Airport (K4I9) | 2026-07-25 16:54 UTC | 2026-07-25 16:54 UTC | 0m |
| HK5220 |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-07-25 16:17 UTC | 2026-07-25 16:54 UTC | 36m |
| SCU34 | SCU | 2OL2 (2OL2) | 84OL (84OL) | 2026-07-25 14:57 UTC | 2026-07-25 16:52 UTC | 1h 55m |
| N200JT |  | Addison Airport (KADS) | CO86 (CO86) | 2026-07-25 15:22 UTC | 2026-07-25 16:52 UTC | 1h 30m |
| LOG49XC | LOG | Glasgow International Airport (EGPF) | Glasgow International Airport (EGPF) | 2026-07-25 14:16 UTC | 2026-07-25 16:50 UTC | 2h 33m |
| OXF4658 | OXF | Falcon Field (KFFZ) | Rimrock Airport (48AZ) | 2026-07-25 16:04 UTC | 2026-07-25 16:50 UTC | 45m |
| N1144G |  | Erie Municipal Airport (KEIK) | Rocky Mountain Metro Airport (KBJC) | 2026-07-25 16:23 UTC | 2026-07-25 16:45 UTC | 22m |
| N5122U |  | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-07-25 16:11 UTC | 2026-07-25 16:45 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
