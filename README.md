# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_13:11:55_UTC-green)

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

**Latest saved flight:** 2026-07-06 13:11:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-06 13:11:55 UTC

- **130,876** saved flights
- **44,485** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **130,876** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,580,020.2 tonnes** estimated CO2 emissions
- **91,595,376 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5327 |
| 2 | SkyWest Airlines | 4842 |
| 3 | EJA | 2561 |
| 4 | IndiGo | 2454 |
| 5 | American Airlines | 2028 |
| 6 | Southwest Airlines | 1970 |
| 7 | ENY | 1644 |
| 8 | Delta Air Lines | 1571 |
| 9 | Lufthansa | 1370 |
| 10 | LATAM Airlines | 1200 |
| 11 | Vueling | 1155 |
| 12 | WIF | 1141 |
| 13 | AZU | 1114 |
| 14 | AXM | 1012 |
| 15 | LXJ | 1010 |
| 16 | Swiss International | 915 |
| 17 | All Nippon Airways | 863 |
| 18 | easyJet | 840 |
| 19 | Alaska Airlines | 838 |
| 20 | QLK | 820 |
| 21 | EJU | 812 |
| 22 | VIV | 724 |
| 23 | Cathay Pacific | 716 |
| 24 | Air France | 712 |
| 25 | AEE | 711 |
| 26 | CXK | 697 |
| 27 | United Airlines | 697 |
| 28 | JetBlue | 686 |
| 29 | MXY | 682 |
| 30 | GLO | 671 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 112017 |
| 2 | 🇪🇸 ES | 8722 |
| 3 | 🇮🇳 IN | 7694 |
| 4 | 🇦🇺 AU | 7567 |
| 5 | 🇧🇷 BR | 7376 |
| 6 | 🇨🇦 CA | 6900 |
| 7 | 🇩🇪 DE | 6868 |
| 8 | 🇮🇹 IT | 6837 |
| 9 | 🇬🇧 GB | 5837 |
| 10 | 🇯🇵 JP | 5653 |
| 11 | 🇫🇷 FR | 5207 |
| 12 | 🇨🇴 CO | 4102 |
| 13 | 🇲🇽 MX | 3819 |
| 14 | 🇬🇷 GR | 3738 |
| 15 | 🇳🇴 NO | 3547 |
| 16 | 🇨🇭 CH | 3366 |
| 17 | 🇹🇷 TR | 2906 |
| 18 | 🇲🇾 MY | 2623 |
| 19 | 🇿🇦 ZA | 2167 |
| 20 | 🇵🇱 PL | 2150 |
| 21 | 🇳🇿 NZ | 2082 |
| 22 | 🇹🇭 TH | 2033 |
| 23 | 🇰🇷 KR | 1966 |
| 24 | 🇵🇭 PH | 1815 |
| 25 | 🇬🇹 GT | 1780 |
| 26 | 🇲🇦 MA | 1397 |
| 27 | 🇲🇪 ME | 1296 |
| 28 | 🇳🇱 NL | 1231 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1150 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2732 |
| 2 | Denver International Airport |  | US | 2217 |
| 3 | Tokyo International Airport |  | JP | 1856 |
| 4 | Indira Gandhi International Airport |  | IN | 1698 |
| 5 | Harry Reid International Airport |  | US | 1628 |
| 6 | Guaymaral Airport |  | CO | 1587 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1544 |
| 8 | Zurich Airport |  | CH | 1443 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1393 |
| 10 | La Aurora Airport |  | GT | 1377 |
| 11 | Frankfurt am Main International Airport |  | DE | 1325 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1265 |
| 13 | Chicago O'Hare International Airport |  | US | 1258 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1163 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1113 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1074 |
| 19 | Capua Airport |  | IT | 1074 |
| 20 | Madrid Barajas International Airport |  | ES | 1073 |
| 21 | Congonhas Airport |  | BR | 1039 |
| 22 | Kuala Lumpur International Airport |  | MY | 1018 |
| 23 | Charlotte/Douglas International Airport |  | US | 975 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 952 |
| 25 | Charles de Gaulle International Airport |  | FR | 950 |
| 26 | Bengaluru International Airport |  | IN | 929 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 893 |
| 28 | Malpensa International Airport |  | IT | 878 |
| 29 | Ninoy Aquino International Airport |  | PH | 842 |
| 30 | Daniel K Inouye International Airport |  | US | 821 |
| 31 | Barcelona International Airport |  | ES | 812 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 797 |
| 33 | Tenerife Norte Airport |  | ES | 792 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 770 |
| 35 | Calgary International Airport |  | CA | 764 |
| 36 | Seattle-Tacoma International Airport |  | US | 756 |
| 37 | Viracopos International Airport |  | BR | 752 |
| 38 | Vitoria/Foronda Airport |  | ES | 750 |
| 39 | Scottsdale Airport |  | US | 748 |
| 40 | Amsterdam Airport Schiphol |  | NL | 743 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 666 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 474 | 21m | 244 km | 1,995.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 328 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 317 | 1h 10m | 770 km | 4,211.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 247 | 26m | 275 km | 1,170.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 241 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 190 | 22m | 55 km | 180.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 184 | 44m | 241 km | 764.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 172 | 1h 45m | 1,423 km | 4,221.2 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 164 | 31m | 369 km | 1,043.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 161 | 18m | 144 km | 400.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 158 | 44m | 452 km | 1,231.4 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 157 | 30m | 49 km | 132.7 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 154 | 1h 1m | 695 km | 1,846.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 153 | 54m | 136 km | 358.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 149 | 1h 38m | 1,156 km | 2,972.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 146 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
|  |  | Bastia-Poretta Airport (LFKB) | Bastia-Poretta Airport (LFKB) | 2026-07-06 12:56 UTC | 2026-07-06 13:11 UTC | 15m |
| SGE64 | SGE | Fort Worth Meacham International Airport (KFTW) | Kenneth Copeland Airport (K4T2) | 2026-07-06 12:59 UTC | 2026-07-06 13:11 UTC | 12m |
| PDT5929 | PDT | Salisbury-Ocean City Wicomico Regional Airport (KSBY) | Philadelphia International Airport (KPHL) | 2026-07-06 12:37 UTC | 2026-07-06 13:08 UTC | 30m |
| N32990 |  | Easton/Newnam Field (KESN) | Cambridge-Dorchester Regional Airport (KCGE) | 2026-07-06 12:40 UTC | 2026-07-06 13:08 UTC | 27m |
| QTR1066 | Qatar Airways | Hamad International Airport (OTHH) | Sirri Island Airport (OIBS) | 2026-07-06 12:40 UTC | 2026-07-06 13:05 UTC | 24m |
| HDB1 | HDB | Al Minhad Air Base (OMDM) | Al Minhad Air Base (OMDM) | 2026-07-06 12:45 UTC | 2026-07-06 13:05 UTC | 20m |
| NWX208 | NWX | Beggs Ranch/Aledo/ Airport (TX15) | Beggs Ranch/Aledo/ Airport (TX15) | 2026-07-06 12:06 UTC | 2026-07-06 13:01 UTC | 55m |
| N141L |  | Nantucket Memorial Airport (KACK) | Laurence G Hanscom Field (KBED) | 2026-07-06 12:26 UTC | 2026-07-06 12:52 UTC | 25m |
| N271SG |  | Merritt Island Airport (KCOI) | Merritt Island Airport (KCOI) | 2026-07-06 12:05 UTC | 2026-07-06 12:48 UTC | 43m |
| N980MH |  | Wangen-Lachen Airport (LSPV) | LSMF (LSMF) | 2026-07-06 12:14 UTC | 2026-07-06 12:45 UTC | 31m |
| JIA5494 | JIA | Gerald R Ford International Airport (KGRR) | Philadelphia International Airport (KPHL) | 2026-07-06 11:28 UTC | 2026-07-06 12:45 UTC | 1h 17m |
| WIF69D | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-07-06 12:11 UTC | 2026-07-06 12:45 UTC | 33m |
| BLVG | BLV | Shek Kong Air Base (VHSK) | Shek Kong Air Base (VHSK) | 2026-07-06 12:31 UTC | 2026-07-06 12:42 UTC | 11m |
| N747DW |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-07-06 12:18 UTC | 2026-07-06 12:42 UTC | 24m |
| N347WS |  | Charlotte/Douglas International Airport (KCLT) | Weaver Field (SC94) | 2026-07-06 12:20 UTC | 2026-07-06 12:40 UTC | 19m |
| EOZONO | EOZ | Anisakan Airport (VYAS) | Eulogio Sanchez Airport (SCTB) | 2026-07-06 11:47 UTC | 2026-07-06 12:39 UTC | 52m |
| AIQ3372 | AIQ | Don Mueang International Airport (VTBD) | Ubon Ratchathani Airport (VTUU) | 2026-07-06 11:58 UTC | 2026-07-06 12:38 UTC | 39m |
| SCU33 | SCU | Haskell Airport (K2K9) | Haskell Airport (K2K9) | 2026-07-06 12:34 UTC | 2026-07-06 12:36 UTC | 1m |
| N825TJ |  | KU77 (KU77) | KU77 (KU77) | 2026-07-06 12:23 UTC | 2026-07-06 12:36 UTC | 12m |
| LNGMA | LNG | Ringebu Airfield Frya (ENRI) | Leirin Airport (ENFG) | 2026-07-06 12:21 UTC | 2026-07-06 12:34 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
