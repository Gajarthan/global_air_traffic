# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_15:57:33_UTC-green)

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

**Latest saved flight:** 2026-07-11 15:57:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-11 15:57:33 UTC

- **137,193** saved flights
- **46,280** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **137,193** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,647,885.6 tonnes** estimated CO2 emissions
- **95,529,598 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5573 |
| 2 | SkyWest Airlines | 5019 |
| 3 | EJA | 2683 |
| 4 | IndiGo | 2532 |
| 5 | American Airlines | 2151 |
| 6 | Southwest Airlines | 2066 |
| 7 | ENY | 1718 |
| 8 | Delta Air Lines | 1632 |
| 9 | Lufthansa | 1406 |
| 10 | LATAM Airlines | 1263 |
| 11 | Vueling | 1190 |
| 12 | WIF | 1190 |
| 13 | AZU | 1177 |
| 14 | LXJ | 1051 |
| 15 | AXM | 1032 |
| 16 | Swiss International | 981 |
| 17 | All Nippon Airways | 890 |
| 18 | easyJet | 889 |
| 19 | Alaska Airlines | 864 |
| 20 | QLK | 856 |
| 21 | EJU | 842 |
| 22 | VIV | 749 |
| 23 | AEE | 742 |
| 24 | Air France | 735 |
| 25 | CXK | 733 |
| 26 | Cathay Pacific | 726 |
| 27 | JetBlue | 720 |
| 28 | United Airlines | 718 |
| 29 | MXY | 711 |
| 30 | GLO | 704 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 117699 |
| 2 | 🇪🇸 ES | 9042 |
| 3 | 🇮🇳 IN | 7940 |
| 4 | 🇦🇺 AU | 7874 |
| 5 | 🇧🇷 BR | 7750 |
| 6 | 🇨🇦 CA | 7223 |
| 7 | 🇩🇪 DE | 7172 |
| 8 | 🇮🇹 IT | 7155 |
| 9 | 🇬🇧 GB | 6225 |
| 10 | 🇯🇵 JP | 5816 |
| 11 | 🇫🇷 FR | 5457 |
| 12 | 🇨🇴 CO | 4319 |
| 13 | 🇲🇽 MX | 3972 |
| 14 | 🇬🇷 GR | 3911 |
| 15 | 🇳🇴 NO | 3715 |
| 16 | 🇨🇭 CH | 3566 |
| 17 | 🇹🇷 TR | 3183 |
| 18 | 🇲🇾 MY | 2682 |
| 19 | 🇵🇱 PL | 2287 |
| 20 | 🇿🇦 ZA | 2256 |
| 21 | 🇳🇿 NZ | 2122 |
| 22 | 🇹🇭 TH | 2091 |
| 23 | 🇰🇷 KR | 1997 |
| 24 | 🇵🇭 PH | 1883 |
| 25 | 🇬🇹 GT | 1836 |
| 26 | 🇲🇦 MA | 1442 |
| 27 | 🇲🇪 ME | 1364 |
| 28 | 🇳🇱 NL | 1279 |
| 29 | 🇭🇷 HR | 1241 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2849 |
| 2 | Denver International Airport |  | US | 2294 |
| 3 | Tokyo International Airport |  | JP | 1897 |
| 4 | Indira Gandhi International Airport |  | IN | 1755 |
| 5 | Harry Reid International Airport |  | US | 1714 |
| 6 | Guaymaral Airport |  | CO | 1663 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1597 |
| 8 | Zurich Airport |  | CH | 1529 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1449 |
| 10 | La Aurora Airport |  | GT | 1418 |
| 11 | Frankfurt am Main International Airport |  | DE | 1361 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1313 |
| 13 | Chicago O'Hare International Airport |  | US | 1294 |
| 14 | El Dorado International Airport |  | CO | 1221 |
| 15 | Salt Lake City International Airport |  | US | 1213 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1181 |
| 18 | Madrid Barajas International Airport |  | ES | 1116 |
| 19 | Capua Airport |  | IT | 1114 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1111 |
| 21 | Congonhas Airport |  | BR | 1106 |
| 22 | Kuala Lumpur International Airport |  | MY | 1040 |
| 23 | Charlotte/Douglas International Airport |  | US | 1003 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 990 |
| 25 | Charles de Gaulle International Airport |  | FR | 978 |
| 26 | Bengaluru International Airport |  | IN | 953 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 948 |
| 28 | Malpensa International Airport |  | IT | 897 |
| 29 | Ninoy Aquino International Airport |  | PH | 876 |
| 30 | Daniel K Inouye International Airport |  | US | 844 |
| 31 | Barcelona International Airport |  | ES | 838 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 834 |
| 33 | Tenerife Norte Airport |  | ES | 812 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 806 |
| 35 | Calgary International Airport |  | CA | 797 |
| 36 | Viracopos International Airport |  | BR | 785 |
| 37 | Scottsdale Airport |  | US | 785 |
| 38 | Seattle-Tacoma International Airport |  | US | 781 |
| 39 | Vitoria/Foronda Airport |  | ES | 771 |
| 40 | Amsterdam Airport Schiphol |  | NL | 767 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 699 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 494 | 21m | 244 km | 2,080.1 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 339 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 338 | 24m | 225 km | 1,311.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 294 | 14m | 114 km | 576.6 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 256 | 26m | 275 km | 1,213.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 251 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 202 | 22m | 55 km | 192.0 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 189 | 26m | 215 km | 700.0 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 185 | 1h 46m | 1,423 km | 4,540.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 182 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 170 | 20m | 250 km | 734.3 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 165 | 18m | 144 km | 410.4 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 164 | 30m | 49 km | 138.6 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 159 | 1h 16m | 961 km | 2,635.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 158 | 1h 1m | 695 km | 1,893.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 156 | 1h 38m | 1,156 km | 3,112.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 149 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N973HA |  | Rocky Mountain Metro Airport (KBJC) | Erie Municipal Airport (KEIK) | 2026-07-11 15:28 UTC | 2026-07-11 15:57 UTC | 28m |
| IZZPE | IZZ | Bologna / Borgo Panigale Airport (LIPE) | Forli Airport (LIPK) | 2026-07-11 15:24 UTC | 2026-07-11 15:53 UTC | 29m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-11 15:24 UTC | 2026-07-11 15:53 UTC | 29m |
| GFOXP | GFO | EG32 (EG32) | EG32 (EG32) | 2026-07-11 15:26 UTC | 2026-07-11 15:48 UTC | 21m |
| N3444Q |  | Chippewa Valley Regional Airport (KEAU) | MI92 (MI92) | 2026-07-11 13:12 UTC | 2026-07-11 15:47 UTC | 2h 35m |
| N205FG |  | Trenton Mercer Airport (KTTN) | Hammonton Municipal Airport (KN81) | 2026-07-11 14:42 UTC | 2026-07-11 15:46 UTC | 1h 3m |
| N95422 |  | Fulton County Airport (KUSE) | Fulton County Airport (KUSE) | 2026-07-11 15:15 UTC | 2026-07-11 15:38 UTC | 23m |
| N970SJ |  | Monmouth Executive Airport (KBLM) | Rocky Mountain Metro Airport (KBJC) | 2026-07-11 11:57 UTC | 2026-07-11 15:35 UTC | 3h 37m |
| N801TH |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-07-11 15:27 UTC | 2026-07-11 15:32 UTC | 5m |
| N72HR |  | Melbourne Orlando International Airport (KMLB) | North Perry Airport (KHWO) | 2026-07-11 14:31 UTC | 2026-07-11 15:31 UTC | 1h 0m |
| N702LU |  | Lynchburg Regional/Preston Glenn Field (KLYH) | Brookneal/Campbell County Airport (K0V4) | 2026-07-11 15:10 UTC | 2026-07-11 15:30 UTC | 20m |
| SPPAC | SPP | Poznań-Kobylnica Airport (EPPK) | Poznań-Kobylnica Airport (EPPK) | 2026-07-11 14:35 UTC | 2026-07-11 15:28 UTC | 52m |
| SD2 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-07-11 15:09 UTC | 2026-07-11 15:26 UTC | 17m |
| DFLYC | DFL | Włocławek-Kruszyn Airport (EPWK) | Włocławek-Kruszyn Airport (EPWK) | 2026-07-11 14:42 UTC | 2026-07-11 15:25 UTC | 43m |
| TWB101 | TWB | Incheon International Airport (RKSI) | Don Mueang International Airport (VTBD) | 2026-07-11 10:27 UTC | 2026-07-11 15:24 UTC | 4h 57m |
| N71560 |  | Abilene Municipal Airport (KK78) | Abilene Municipal Airport (KK78) | 2026-07-11 15:10 UTC | 2026-07-11 15:24 UTC | 14m |
| DFALL | DFA | Hildesheim Airport (EDVM) | Hildesheim Airport (EDVM) | 2026-07-11 15:01 UTC | 2026-07-11 15:23 UTC | 21m |
| SPSDW | SPS | Lubin Airport (EPLU) | Lubin Airport (EPLU) | 2026-07-11 14:29 UTC | 2026-07-11 15:23 UTC | 53m |
| N951BA |  | Lake X Airport (57FA) | Lake X Airport (57FA) | 2026-07-11 15:18 UTC | 2026-07-11 15:22 UTC | 4m |
| AAH442 | AAH | Daniel K Inouye International Airport (PHNL) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-07-11 14:54 UTC | 2026-07-11 15:22 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
