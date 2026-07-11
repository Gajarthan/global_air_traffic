# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_19:20:30_UTC-green)

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

**Latest saved flight:** 2026-07-11 19:20:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-11 19:20:30 UTC

- **137,834** saved flights
- **46,493** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **137,834** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,655,152.9 tonnes** estimated CO2 emissions
- **95,950,896 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5600 |
| 2 | SkyWest Airlines | 5057 |
| 3 | EJA | 2705 |
| 4 | IndiGo | 2535 |
| 5 | American Airlines | 2163 |
| 6 | Southwest Airlines | 2077 |
| 7 | ENY | 1729 |
| 8 | Delta Air Lines | 1637 |
| 9 | Lufthansa | 1409 |
| 10 | LATAM Airlines | 1267 |
| 11 | Vueling | 1192 |
| 12 | WIF | 1190 |
| 13 | AZU | 1184 |
| 14 | LXJ | 1058 |
| 15 | AXM | 1032 |
| 16 | Swiss International | 983 |
| 17 | easyJet | 891 |
| 18 | All Nippon Airways | 890 |
| 19 | Alaska Airlines | 868 |
| 20 | QLK | 856 |
| 21 | EJU | 847 |
| 22 | VIV | 756 |
| 23 | AEE | 746 |
| 24 | Air France | 738 |
| 25 | CXK | 737 |
| 26 | Cathay Pacific | 726 |
| 27 | JetBlue | 724 |
| 28 | United Airlines | 722 |
| 29 | MXY | 717 |
| 30 | GLO | 708 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 118400 |
| 2 | 🇪🇸 ES | 9072 |
| 3 | 🇮🇳 IN | 7947 |
| 4 | 🇦🇺 AU | 7874 |
| 5 | 🇧🇷 BR | 7784 |
| 6 | 🇨🇦 CA | 7256 |
| 7 | 🇩🇪 DE | 7200 |
| 8 | 🇮🇹 IT | 7192 |
| 9 | 🇬🇧 GB | 6243 |
| 10 | 🇯🇵 JP | 5816 |
| 11 | 🇫🇷 FR | 5489 |
| 12 | 🇨🇴 CO | 4349 |
| 13 | 🇲🇽 MX | 3997 |
| 14 | 🇬🇷 GR | 3935 |
| 15 | 🇳🇴 NO | 3719 |
| 16 | 🇨🇭 CH | 3575 |
| 17 | 🇹🇷 TR | 3210 |
| 18 | 🇲🇾 MY | 2682 |
| 19 | 🇵🇱 PL | 2312 |
| 20 | 🇿🇦 ZA | 2260 |
| 21 | 🇳🇿 NZ | 2122 |
| 22 | 🇹🇭 TH | 2092 |
| 23 | 🇰🇷 KR | 1997 |
| 24 | 🇵🇭 PH | 1883 |
| 25 | 🇬🇹 GT | 1839 |
| 26 | 🇲🇦 MA | 1452 |
| 27 | 🇲🇪 ME | 1366 |
| 28 | 🇳🇱 NL | 1283 |
| 29 | 🇭🇷 HR | 1248 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2863 |
| 2 | Denver International Airport |  | US | 2303 |
| 3 | Tokyo International Airport |  | JP | 1897 |
| 4 | Indira Gandhi International Airport |  | IN | 1757 |
| 5 | Harry Reid International Airport |  | US | 1722 |
| 6 | Guaymaral Airport |  | CO | 1678 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1601 |
| 8 | Zurich Airport |  | CH | 1533 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1452 |
| 10 | La Aurora Airport |  | GT | 1421 |
| 11 | Frankfurt am Main International Airport |  | DE | 1364 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1321 |
| 13 | Chicago O'Hare International Airport |  | US | 1301 |
| 14 | El Dorado International Airport |  | CO | 1227 |
| 15 | Salt Lake City International Airport |  | US | 1225 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1184 |
| 18 | Capua Airport |  | IT | 1125 |
| 19 | Madrid Barajas International Airport |  | ES | 1121 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1113 |
| 21 | Congonhas Airport |  | BR | 1110 |
| 22 | Kuala Lumpur International Airport |  | MY | 1040 |
| 23 | Charlotte/Douglas International Airport |  | US | 1006 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 990 |
| 25 | Charles de Gaulle International Airport |  | FR | 981 |
| 26 | Bengaluru International Airport |  | IN | 955 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 951 |
| 28 | Malpensa International Airport |  | IT | 901 |
| 29 | Ninoy Aquino International Airport |  | PH | 876 |
| 30 | Daniel K Inouye International Airport |  | US | 847 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 839 |
| 32 | Barcelona International Airport |  | ES | 839 |
| 33 | Tenerife Norte Airport |  | ES | 812 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 808 |
| 35 | Calgary International Airport |  | CA | 800 |
| 36 | Viracopos International Airport |  | BR | 790 |
| 37 | Scottsdale Airport |  | US | 790 |
| 38 | Seattle-Tacoma International Airport |  | US | 784 |
| 39 | Vitoria/Foronda Airport |  | ES | 774 |
| 40 | Amsterdam Airport Schiphol |  | NL | 769 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 706 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 497 | 21m | 244 km | 2,092.7 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 340 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 338 | 24m | 225 km | 1,311.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 296 | 14m | 114 km | 580.6 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 257 | 26m | 275 km | 1,217.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 251 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 205 | 22m | 55 km | 194.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 189 | 26m | 215 km | 700.0 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 186 | 1h 46m | 1,423 km | 4,564.7 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 182 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 171 | 20m | 250 km | 738.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 171 | 30m | 49 km | 144.5 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 165 | 18m | 144 km | 410.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 160 | 1h 16m | 961 km | 2,652.1 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 159 | 1h 1m | 695 km | 1,905.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 156 | 1h 38m | 1,156 km | 3,112.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 149 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-07-11 18:17 UTC | 2026-07-11 19:20 UTC | 1h 3m |
| N5366X |  | Wasilla Airport (PAWS) | Castle Mountain Airstrip (48AK) | 2026-07-11 16:08 UTC | 2026-07-11 19:18 UTC | 3h 9m |
| ASA1776 | Alaska Airlines | Portland International Airport (KPDX) | Philadelphia International Airport (KPHL) | 2026-07-11 14:40 UTC | 2026-07-11 19:14 UTC | 4h 34m |
| N8503M |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-07-11 18:20 UTC | 2026-07-11 19:13 UTC | 53m |
| N73784 |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-07-11 18:53 UTC | 2026-07-11 19:07 UTC | 13m |
| N820BH |  | K1J6 (K1J6) | K1J6 (K1J6) | 2026-07-11 18:20 UTC | 2026-07-11 19:07 UTC | 46m |
| IBS1903 | IBS | Madrid Barajas International Airport (LEMD) | Giza Embaba Airport (HEEM) | 2026-07-11 14:51 UTC | 2026-07-11 19:07 UTC | 4h 15m |
| T815 |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-11 18:33 UTC | 2026-07-11 19:06 UTC | 33m |
| N5306C |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-07-11 19:04 UTC | 2026-07-11 19:06 UTC | 1m |
| DAH3017 | DAH | Istanbul Airport (LTFM) | Houari Boumediene Airport (DAAG) | 2026-07-11 16:07 UTC | 2026-07-11 19:06 UTC | 2h 58m |
| T825 |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-11 18:33 UTC | 2026-07-11 19:05 UTC | 32m |
| TEST | TES | Vero Beach Regional Airport (KVRB) | Northeast Philadelphia Airport (KPNE) | 2026-07-11 16:58 UTC | 2026-07-11 19:01 UTC | 2h 2m |
| ELZ930 | ELZ | Asheville Regional Airport (KAVL) | Pilot Country Airport (KX05) | 2026-07-11 17:32 UTC | 2026-07-11 19:00 UTC | 1h 28m |
| ARES44 | ARE | Latina Airport (LIRL) | Latina Airport (LIRL) | 2026-07-11 18:42 UTC | 2026-07-11 19:00 UTC | 18m |
| N71560 |  | Abilene Municipal Airport (KK78) | Abilene Municipal Airport (KK78) | 2026-07-11 18:45 UTC | 2026-07-11 18:59 UTC | 14m |
| CXK610 | CXK | Dupage Airport (KDPA) | Jack W Watson Airport (0IL9) | 2026-07-11 18:39 UTC | 2026-07-11 18:55 UTC | 16m |
| HK5483X |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-07-11 18:28 UTC | 2026-07-11 18:51 UTC | 23m |
| N761TA |  | Fremont County Airport (K1V6) | Mann Ranch Airport (95CO) | 2026-07-11 17:59 UTC | 2026-07-11 18:49 UTC | 50m |
| N5328Z |  | Lake Wales Municipal Airport (KX07) | Winter Haven Regional Airport (KGIF) | 2026-07-11 18:40 UTC | 2026-07-11 18:49 UTC | 8m |
| N217EB |  | Ted Stevens Anchorage International Airport (PANC) | King Salmon Airport (PAKN) | 2026-07-11 17:18 UTC | 2026-07-11 18:49 UTC | 1h 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
