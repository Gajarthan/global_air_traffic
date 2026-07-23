# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_22:52:35_UTC-green)

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

**Latest saved flight:** 2026-07-23 22:52:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-23 22:52:35 UTC

- **146,883** saved flights
- **49,116** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **146,883** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,760,034.6 tonnes** estimated CO2 emissions
- **102,030,988 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5944 |
| 2 | SkyWest Airlines | 5396 |
| 3 | EJA | 2909 |
| 4 | IndiGo | 2645 |
| 5 | American Airlines | 2343 |
| 6 | Southwest Airlines | 2221 |
| 7 | ENY | 1826 |
| 8 | Delta Air Lines | 1742 |
| 9 | Lufthansa | 1450 |
| 10 | LATAM Airlines | 1351 |
| 11 | AZU | 1266 |
| 12 | Vueling | 1245 |
| 13 | WIF | 1245 |
| 14 | LXJ | 1132 |
| 15 | AXM | 1066 |
| 16 | Swiss International | 1037 |
| 17 | easyJet | 947 |
| 18 | All Nippon Airways | 932 |
| 19 | Alaska Airlines | 921 |
| 20 | QLK | 914 |
| 21 | EJU | 900 |
| 22 | VIV | 817 |
| 23 | CXK | 788 |
| 24 | AEE | 777 |
| 25 | JetBlue | 773 |
| 26 | Air France | 770 |
| 27 | Cathay Pacific | 770 |
| 28 | MXY | 770 |
| 29 | United Airlines | 765 |
| 30 | GLO | 760 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 126818 |
| 2 | 🇪🇸 ES | 9501 |
| 3 | 🇦🇺 AU | 8349 |
| 4 | 🇧🇷 BR | 8292 |
| 5 | 🇮🇳 IN | 8285 |
| 6 | 🇨🇦 CA | 7863 |
| 7 | 🇮🇹 IT | 7620 |
| 8 | 🇩🇪 DE | 7537 |
| 9 | 🇬🇧 GB | 6687 |
| 10 | 🇯🇵 JP | 6098 |
| 11 | 🇫🇷 FR | 5817 |
| 12 | 🇨🇴 CO | 4871 |
| 13 | 🇲🇽 MX | 4273 |
| 14 | 🇬🇷 GR | 4157 |
| 15 | 🇳🇴 NO | 3908 |
| 16 | 🇨🇭 CH | 3818 |
| 17 | 🇹🇷 TR | 3439 |
| 18 | 🇲🇾 MY | 2781 |
| 19 | 🇵🇱 PL | 2468 |
| 20 | 🇿🇦 ZA | 2372 |
| 21 | 🇳🇿 NZ | 2227 |
| 22 | 🇹🇭 TH | 2141 |
| 23 | 🇰🇷 KR | 2047 |
| 24 | 🇵🇭 PH | 1941 |
| 25 | 🇬🇹 GT | 1906 |
| 26 | 🇲🇦 MA | 1514 |
| 27 | 🇲🇪 ME | 1454 |
| 28 | 🇳🇱 NL | 1364 |
| 29 | 🇭🇷 HR | 1337 |
| 30 | 🇲🇴 MO | 1225 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3029 |
| 2 | Denver International Airport |  | US | 2467 |
| 3 | Tokyo International Airport |  | JP | 1960 |
| 4 | Indira Gandhi International Airport |  | IN | 1841 |
| 5 | Harry Reid International Airport |  | US | 1835 |
| 6 | Guaymaral Airport |  | CO | 1812 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1659 |
| 8 | Zurich Airport |  | CH | 1614 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1548 |
| 10 | La Aurora Airport |  | GT | 1477 |
| 11 | Frankfurt am Main International Airport |  | DE | 1401 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1382 |
| 13 | Chicago O'Hare International Airport |  | US | 1364 |
| 14 | Salt Lake City International Airport |  | US | 1326 |
| 15 | El Dorado International Airport |  | CO | 1318 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1273 |
| 17 | Macau International Airport |  | MO | 1225 |
| 18 | Capua Airport |  | IT | 1190 |
| 19 | Congonhas Airport |  | BR | 1182 |
| 20 | Madrid Barajas International Airport |  | ES | 1169 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1153 |
| 22 | Kuala Lumpur International Airport |  | MY | 1074 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1054 |
| 24 | Charlotte/Douglas International Airport |  | US | 1048 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1028 |
| 26 | Charles de Gaulle International Airport |  | FR | 1016 |
| 27 | Bengaluru International Airport |  | IN | 991 |
| 28 | Malpensa International Airport |  | IT | 946 |
| 29 | Ninoy Aquino International Airport |  | PH | 906 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 897 |
| 31 | Barcelona International Airport |  | ES | 889 |
| 32 | Daniel K Inouye International Airport |  | US | 883 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 880 |
| 34 | Tenerife Norte Airport |  | ES | 844 |
| 35 | Seattle-Tacoma International Airport |  | US | 843 |
| 36 | Calgary International Airport |  | CA | 839 |
| 37 | Scottsdale Airport |  | US | 833 |
| 38 | Viracopos International Airport |  | BR | 831 |
| 39 | Amsterdam Airport Schiphol |  | NL | 824 |
| 40 | Oslo Gardermoen Airport |  | NO | 809 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 764 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 532 | 21m | 244 km | 2,240.1 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 355 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 352 | 24m | 225 km | 1,365.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 345 | 1h 9m | 770 km | 4,583.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 264 | 27m | 275 km | 1,251.0 t |
| 10 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 262 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 220 | 22m | 55 km | 209.1 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 197 | 44m | 241 km | 818.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 196 | 1h 46m | 1,423 km | 4,810.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 193 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 180 | 20m | 250 km | 777.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 180 | 28m | 152 km | 470.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 174 | 18m | 144 km | 432.8 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 172 | 1h 16m | 961 km | 2,851.0 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 170 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 169 | 44m | 452 km | 1,317.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 166 | 1h 39m | 1,156 km | 3,311.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 160 | 55m | 136 km | 375.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N50KA |  | Roche Harbor Airport (WA09) | Boeing Field/King County International Airport (KBFI) | 2026-07-23 22:12 UTC | 2026-07-23 22:52 UTC | 40m |
| KOW523 | KOW | Van Nuys Airport (KVNY) | Quail Lake Sky Park Airport (CL46) | 2026-07-23 22:22 UTC | 2026-07-23 22:52 UTC | 29m |
| N8452R |  | Saginaw County/H W Browne Airport (KHYX) | Saginaw County/H W Browne Airport (KHYX) | 2026-07-23 22:36 UTC | 2026-07-23 22:50 UTC | 14m |
| FXC66 | FXC | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-07-23 22:06 UTC | 2026-07-23 22:45 UTC | 39m |
| N20932 |  | Hammond Northshore Regional Airport (KHDC) | Hammond Northshore Regional Airport (KHDC) | 2026-07-23 21:34 UTC | 2026-07-23 22:42 UTC | 1h 8m |
| N222YZ |  | Portland-Hillsboro Airport (KHIO) | Aurora State Airport (KUAO) | 2026-07-23 21:58 UTC | 2026-07-23 22:40 UTC | 42m |
| N261PJ |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-07-23 22:11 UTC | 2026-07-23 22:39 UTC | 28m |
| N3744Y |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-07-23 21:56 UTC | 2026-07-23 22:39 UTC | 42m |
| BOE160 | BOE | Boeing Field/King County International Airport (KBFI) | Boeing Field/King County International Airport (KBFI) | 2026-07-23 22:16 UTC | 2026-07-23 22:36 UTC | 20m |
| N30AV |  | Butler County Regional/Hogan Field (KHAO) | KW38 (KW38) | 2026-07-23 22:00 UTC | 2026-07-23 22:30 UTC | 29m |
| HKW221 | HKW | Dvoracek Field (23MI) | Mason County Airport (KLDM) | 2026-07-23 22:05 UTC | 2026-07-23 22:28 UTC | 22m |
| N816RW |  | Gulfport-Biloxi International Airport (KGPT) | Smith County Airport (MS39) | 2026-07-23 21:59 UTC | 2026-07-23 22:27 UTC | 28m |
| N2335E |  | Council Bluffs Municipal Airport (KCBF) | Council Bluffs Municipal Airport (KCBF) | 2026-07-23 21:56 UTC | 2026-07-23 22:27 UTC | 31m |
| N20BQ |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-07-23 21:16 UTC | 2026-07-23 22:26 UTC | 1h 10m |
|  |  | Ak Su Airport (CO61) | Ak Su Airport (CO61) | 2026-07-23 22:03 UTC | 2026-07-23 22:26 UTC | 22m |
| N12704 |  | Frederick Municipal Airport (KFDK) | Carroll County Regional/Jack B Poage Field (KDMW) | 2026-07-23 21:40 UTC | 2026-07-23 22:23 UTC | 42m |
| N784CA |  | Norwood Memorial Airport (KOWD) | Lancaster Airport (KLNS) | 2026-07-23 20:40 UTC | 2026-07-23 22:23 UTC | 1h 42m |
| N8636Q |  | Boeing Field/King County International Airport (KBFI) | 3WA1 (3WA1) | 2026-07-23 21:53 UTC | 2026-07-23 22:21 UTC | 27m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Macau International Airport (VMMC) | 2026-07-23 11:27 UTC | 2026-07-23 22:21 UTC | 10h 54m |
| N322FJ |  | Harrisburg International Airport (KMDT) | Addison Airport (KADS) | 2026-07-23 19:33 UTC | 2026-07-23 22:21 UTC | 2h 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
