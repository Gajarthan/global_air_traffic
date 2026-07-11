# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_21:59:46_UTC-green)

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

**Latest saved flight:** 2026-07-11 21:59:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-11 21:59:46 UTC

- **138,163** saved flights
- **46,602** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **138,163** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,660,078.7 tonnes** estimated CO2 emissions
- **96,236,448 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5618 |
| 2 | SkyWest Airlines | 5076 |
| 3 | EJA | 2714 |
| 4 | IndiGo | 2535 |
| 5 | American Airlines | 2179 |
| 6 | Southwest Airlines | 2088 |
| 7 | ENY | 1736 |
| 8 | Delta Air Lines | 1643 |
| 9 | Lufthansa | 1409 |
| 10 | LATAM Airlines | 1271 |
| 11 | Vueling | 1195 |
| 12 | WIF | 1190 |
| 13 | AZU | 1187 |
| 14 | LXJ | 1061 |
| 15 | AXM | 1032 |
| 16 | Swiss International | 983 |
| 17 | easyJet | 895 |
| 18 | All Nippon Airways | 890 |
| 19 | Alaska Airlines | 872 |
| 20 | QLK | 856 |
| 21 | EJU | 848 |
| 22 | VIV | 758 |
| 23 | AEE | 747 |
| 24 | CXK | 739 |
| 25 | Air France | 738 |
| 26 | United Airlines | 729 |
| 27 | Cathay Pacific | 727 |
| 28 | JetBlue | 725 |
| 29 | MXY | 721 |
| 30 | GLO | 708 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 118797 |
| 2 | 🇪🇸 ES | 9087 |
| 3 | 🇮🇳 IN | 7947 |
| 4 | 🇦🇺 AU | 7876 |
| 5 | 🇧🇷 BR | 7800 |
| 6 | 🇨🇦 CA | 7276 |
| 7 | 🇮🇹 IT | 7213 |
| 8 | 🇩🇪 DE | 7203 |
| 9 | 🇬🇧 GB | 6259 |
| 10 | 🇯🇵 JP | 5816 |
| 11 | 🇫🇷 FR | 5494 |
| 12 | 🇨🇴 CO | 4369 |
| 13 | 🇲🇽 MX | 4009 |
| 14 | 🇬🇷 GR | 3942 |
| 15 | 🇳🇴 NO | 3721 |
| 16 | 🇨🇭 CH | 3577 |
| 17 | 🇹🇷 TR | 3224 |
| 18 | 🇲🇾 MY | 2682 |
| 19 | 🇵🇱 PL | 2316 |
| 20 | 🇿🇦 ZA | 2260 |
| 21 | 🇳🇿 NZ | 2124 |
| 22 | 🇹🇭 TH | 2093 |
| 23 | 🇰🇷 KR | 1997 |
| 24 | 🇵🇭 PH | 1883 |
| 25 | 🇬🇹 GT | 1839 |
| 26 | 🇲🇦 MA | 1455 |
| 27 | 🇲🇪 ME | 1369 |
| 28 | 🇳🇱 NL | 1287 |
| 29 | 🇭🇷 HR | 1250 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2869 |
| 2 | Denver International Airport |  | US | 2319 |
| 3 | Tokyo International Airport |  | JP | 1897 |
| 4 | Indira Gandhi International Airport |  | IN | 1757 |
| 5 | Harry Reid International Airport |  | US | 1728 |
| 6 | Guaymaral Airport |  | CO | 1684 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1602 |
| 8 | Zurich Airport |  | CH | 1533 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1457 |
| 10 | La Aurora Airport |  | GT | 1421 |
| 11 | Frankfurt am Main International Airport |  | DE | 1364 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1325 |
| 13 | Chicago O'Hare International Airport |  | US | 1306 |
| 14 | El Dorado International Airport |  | CO | 1230 |
| 15 | Salt Lake City International Airport |  | US | 1227 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1185 |
| 18 | Capua Airport |  | IT | 1133 |
| 19 | Madrid Barajas International Airport |  | ES | 1125 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1115 |
| 21 | Congonhas Airport |  | BR | 1113 |
| 22 | Kuala Lumpur International Airport |  | MY | 1040 |
| 23 | Charlotte/Douglas International Airport |  | US | 1011 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 990 |
| 25 | Charles de Gaulle International Airport |  | FR | 982 |
| 26 | Bengaluru International Airport |  | IN | 955 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 953 |
| 28 | Malpensa International Airport |  | IT | 903 |
| 29 | Ninoy Aquino International Airport |  | PH | 876 |
| 30 | Daniel K Inouye International Airport |  | US | 849 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 840 |
| 32 | Barcelona International Airport |  | ES | 840 |
| 33 | Tenerife Norte Airport |  | ES | 812 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 810 |
| 35 | Calgary International Airport |  | CA | 800 |
| 36 | Viracopos International Airport |  | BR | 791 |
| 37 | Scottsdale Airport |  | US | 791 |
| 38 | Seattle-Tacoma International Airport |  | US | 788 |
| 39 | Vitoria/Foronda Airport |  | ES | 775 |
| 40 | Amsterdam Airport Schiphol |  | NL | 772 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 709 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 499 | 21m | 244 km | 2,101.2 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 340 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 338 | 24m | 225 km | 1,311.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 296 | 14m | 114 km | 580.6 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 251 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 206 | 22m | 55 km | 195.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 189 | 26m | 215 km | 700.0 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 186 | 1h 46m | 1,423 km | 4,564.7 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 182 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 171 | 20m | 250 km | 738.6 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 166 | 18m | 144 km | 412.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 161 | 1h 16m | 961 km | 2,668.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 159 | 1h 1m | 695 km | 1,905.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 156 | 1h 38m | 1,156 km | 3,112.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 152 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JIA5281 | JIA | Nashville International Airport (KBNA) | Philadelphia International Airport (KPHL) | 2026-07-11 20:29 UTC | 2026-07-11 21:59 UTC | 1h 30m |
| T825 |  | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-07-11 21:44 UTC | 2026-07-11 21:56 UTC | 12m |
| N52LB |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-07-11 19:55 UTC | 2026-07-11 21:56 UTC | 2h 1m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-07-11 20:46 UTC | 2026-07-11 21:50 UTC | 1h 3m |
| ERU72 | ERU | Robin Airport (59AZ) | Robin Airport (59AZ) | 2026-07-11 21:13 UTC | 2026-07-11 21:31 UTC | 17m |
| T815 |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-11 20:58 UTC | 2026-07-11 21:29 UTC | 30m |
| CFR657 | CFR | Charles M Schulz/Sonoma County Airport (KSTS) | Fall River Mills Airport (KO89) | 2026-07-11 20:47 UTC | 2026-07-11 21:27 UTC | 40m |
| AAL2045 | American Airlines | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-11 20:10 UTC | 2026-07-11 21:26 UTC | 1h 15m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-07-11 10:49 UTC | 2026-07-11 21:26 UTC | 10h 37m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | UT99 (UT99) | 2026-07-11 21:15 UTC | 2026-07-11 21:25 UTC | 10m |
| N999VP |  | IS95 (IS95) | Vogen Airport (IS41) | 2026-07-11 20:41 UTC | 2026-07-11 21:24 UTC | 42m |
| AAL741 | American Airlines | Madrid Barajas International Airport (LEMD) | Philadelphia International Airport (KPHL) | 2026-07-11 13:49 UTC | 2026-07-11 21:24 UTC | 7h 34m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | UT99 (UT99) | 2026-07-11 21:14 UTC | 2026-07-11 21:23 UTC | 9m |
| AAL9601 | American Airlines | Miami International Airport (KMIA) | Philadelphia International Airport (KPHL) | 2026-07-11 19:07 UTC | 2026-07-11 21:23 UTC | 2h 15m |
| N133SW |  | Minden-Tahoe Airport (KMEV) | Desert Creek Airport (NV97) | 2026-07-11 19:50 UTC | 2026-07-11 21:20 UTC | 1h 29m |
| N565E |  | Smith Airport (WA73) | Quail Field (OG42) | 2026-07-11 19:47 UTC | 2026-07-11 21:19 UTC | 1h 32m |
| N100JF |  | Plantation Airpark (KJYL) | Plantation Airpark (KJYL) | 2026-07-11 21:00 UTC | 2026-07-11 21:19 UTC | 18m |
| N838GK |  | Eulogio Sanchez Airport (SCTB) | San Alfonso Airport (SCAF) | 2026-07-11 21:03 UTC | 2026-07-11 21:18 UTC | 14m |
| LND3 | LND | Centennial Airport (KAPA) | Telluride Regional Airport (KTEX) | 2026-07-11 20:26 UTC | 2026-07-11 21:13 UTC | 46m |
|  |  | Hill Afb Airport (KHIF) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-07-11 20:56 UTC | 2026-07-11 21:13 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
