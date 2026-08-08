# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_21:27:21_UTC-green)

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

**Latest saved flight:** 2026-08-08 21:27:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 21:27:21 UTC

- **179,691** saved flights
- **57,621** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **179,691** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,160,181.2 tonnes** estimated CO2 emissions
- **125,227,893 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7123 |
| 2 | SkyWest Airlines | 6559 |
| 3 | EJA | 3542 |
| 4 | IndiGo | 3144 |
| 5 | Southwest Airlines | 2829 |
| 6 | American Airlines | 2808 |
| 7 | ENY | 2239 |
| 8 | Delta Air Lines | 2135 |
| 9 | LATAM Airlines | 1675 |
| 10 | AZU | 1607 |
| 11 | Lufthansa | 1600 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1486 |
| 14 | LXJ | 1406 |
| 15 | easyJet | 1227 |
| 16 | Swiss International | 1225 |
| 17 | AXM | 1211 |
| 18 | EJU | 1094 |
| 19 | QLK | 1093 |
| 20 | Alaska Airlines | 1089 |
| 21 | All Nippon Airways | 1088 |
| 22 | VIV | 989 |
| 23 | GLO | 958 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 946 |
| 26 | AEE | 935 |
| 27 | United Airlines | 927 |
| 28 | Air France | 924 |
| 29 | MXY | 903 |
| 30 | PGT | 894 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154158 |
| 2 | 🇪🇸 ES | 11547 |
| 3 | 🇧🇷 BR | 10308 |
| 4 | 🇦🇺 AU | 10071 |
| 5 | 🇮🇳 IN | 9857 |
| 6 | 🇨🇦 CA | 9804 |
| 7 | 🇮🇹 IT | 9276 |
| 8 | 🇩🇪 DE | 8894 |
| 9 | 🇬🇧 GB | 8302 |
| 10 | 🇯🇵 JP | 7227 |
| 11 | 🇫🇷 FR | 7152 |
| 12 | 🇨🇴 CO | 6671 |
| 13 | 🇬🇷 GR | 5239 |
| 14 | 🇲🇽 MX | 5142 |
| 15 | 🇨🇭 CH | 4788 |
| 16 | 🇳🇴 NO | 4645 |
| 17 | 🇹🇷 TR | 4572 |
| 18 | 🇲🇾 MY | 3160 |
| 19 | 🇵🇱 PL | 2999 |
| 20 | 🇿🇦 ZA | 2922 |
| 21 | 🇹🇭 TH | 2718 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2360 |
| 24 | 🇬🇹 GT | 2290 |
| 25 | 🇰🇷 KR | 2240 |
| 26 | 🇲🇦 MA | 1815 |
| 27 | 🇭🇷 HR | 1790 |
| 28 | 🇲🇪 ME | 1634 |
| 29 | 🇳🇱 NL | 1616 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3715 |
| 2 | Denver International Airport |  | US | 2983 |
| 3 | Tokyo International Airport |  | JP | 2245 |
| 4 | Guaymaral Airport |  | CO | 2220 |
| 5 | Indira Gandhi International Airport |  | IN | 2195 |
| 6 | Harry Reid International Airport |  | US | 2121 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1933 |
| 8 | Zurich Airport |  | CH | 1909 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1873 |
| 10 | La Aurora Airport |  | GT | 1760 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1645 |
| 12 | Chicago O'Hare International Airport |  | US | 1621 |
| 13 | Salt Lake City International Airport |  | US | 1609 |
| 14 | El Dorado International Airport |  | CO | 1603 |
| 15 | Frankfurt am Main International Airport |  | DE | 1564 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1496 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1433 |
| 19 | Madrid Barajas International Airport |  | ES | 1408 |
| 20 | Capua Airport |  | IT | 1401 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1344 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1280 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1238 |
| 25 | Charlotte/Douglas International Airport |  | US | 1223 |
| 26 | Charles de Gaulle International Airport |  | FR | 1215 |
| 27 | Kuala Lumpur International Airport |  | MY | 1191 |
| 28 | Bengaluru International Airport |  | IN | 1175 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1118 |
| 30 | Ninoy Aquino International Airport |  | PH | 1110 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1104 |
| 32 | Barcelona International Airport |  | ES | 1069 |
| 33 | Seattle-Tacoma International Airport |  | US | 1034 |
| 34 | Daniel K Inouye International Airport |  | US | 1032 |
| 35 | Viracopos International Airport |  | BR | 1032 |
| 36 | Reno/Tahoe International Airport |  | US | 1027 |
| 37 | Calgary International Airport |  | CA | 1021 |
| 38 | Oslo Gardermoen Airport |  | NO | 997 |
| 39 | Tenerife Norte Airport |  | ES | 983 |
| 40 | Amsterdam Airport Schiphol |  | NL | 973 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 917 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 662 | 21m | 244 km | 2,787.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 420 | 1h 8m | 770 km | 5,579.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 301 | 27m | 275 km | 1,426.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 252 | 1h 48m | 1,423 km | 6,184.5 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 240 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 217 | 50m | 556 km | 2,080.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 216 | 1h 15m | 961 km | 3,580.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 215 | 19m | 144 km | 534.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 214 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 209 | 1h 38m | 1,156 km | 4,169.5 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 206 | 31m | 369 km | 1,311.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 205 | 24m | 218 km | 772.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 195 | 1h 2m | 695 km | 2,337.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CAP5157 | CAP | Ellison Onizuka Kona International At Keahole Airport (PHKO) | HI13 (HI13) | 2026-08-08 21:10 UTC | 2026-08-08 21:27 UTC | 16m |
| N55218 |  | 2OL2 (2OL2) | Gregg Airport (7OK1) | 2026-08-08 20:47 UTC | 2026-08-08 21:25 UTC | 37m |
| AFR91AG | Air France | Charles de Gaulle International Airport (LFPG) | Dublin Airport (EIDW) | 2026-08-08 20:06 UTC | 2026-08-08 21:24 UTC | 1h 18m |
| N232TB |  | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-08-08 21:19 UTC | 2026-08-08 21:20 UTC | 1m |
| N259LA |  | Minder Airport (37IL) | Litchfield Airport (4IS7) | 2026-08-08 21:03 UTC | 2026-08-08 21:18 UTC | 14m |
| ABY842 | ABY | Ras Al Khaimah International Airport (OMRK) | Hulwan (HE15) | 2026-08-08 18:16 UTC | 2026-08-08 21:16 UTC | 3h 0m |
| N46132 |  | Preston Airport (KU10) | Logan-Cache Airport (KLGU) | 2026-08-08 20:26 UTC | 2026-08-08 21:16 UTC | 49m |
| VJT683 | VJT | Ancona / Falconara Airport (LIPY) | HE12 (HE12) | 2026-08-08 18:24 UTC | 2026-08-08 21:11 UTC | 2h 47m |
| SCU27 | SCU | Mc Crays Airport (OK46) | Tulsa International Airport (KTUL) | 2026-08-08 20:05 UTC | 2026-08-08 21:11 UTC | 1h 5m |
| N419BR |  | Montgomery-Gibbs Executive Airport (KMYF) | Reno/Tahoe International Airport (KRNO) | 2026-08-08 20:05 UTC | 2026-08-08 21:11 UTC | 1h 5m |
| N455LF |  | Black Diamond Airport (95WA) | Boeing Field/King County International Airport (KBFI) | 2026-08-08 20:53 UTC | 2026-08-08 21:08 UTC | 14m |
| N29AF |  | Brackett Field (KPOC) | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | 2026-08-08 19:50 UTC | 2026-08-08 21:05 UTC | 1h 14m |
| TKR15 | TKR | Boise Air Trml/Gowen Field (KBOI) | High Valley Airport (ID35) | 2026-08-08 20:54 UTC | 2026-08-08 21:04 UTC | 10m |
| N19650 |  | Dupage Airport (KDPA) | 26LL (26LL) | 2026-08-08 20:35 UTC | 2026-08-08 21:03 UTC | 28m |
| VACA11 | VAC | Kelly Field (KSKF) | XA64 (XA64) | 2026-08-08 20:24 UTC | 2026-08-08 21:02 UTC | 38m |
| CXK149 | CXK | Georgetown Executive Airport (KGTU) | Easterwood Field (KCLL) | 2026-08-08 20:08 UTC | 2026-08-08 21:02 UTC | 54m |
| N540AW |  | Palo Alto Airport (KPAO) | Las Trancas Airport (17CL) | 2026-08-08 20:49 UTC | 2026-08-08 21:02 UTC | 12m |
| N365AV |  | Van Nuys Airport (KVNY) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-08 19:57 UTC | 2026-08-08 21:02 UTC | 1h 4m |
| FTO501 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-08 20:27 UTC | 2026-08-08 21:01 UTC | 34m |
| LXJ581 | LXJ | Washington Dulles International Airport (KIAD) | Mc Elroy Airfield (K20V) | 2026-08-08 17:45 UTC | 2026-08-08 20:59 UTC | 3h 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
