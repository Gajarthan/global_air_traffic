# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_21:38:17_UTC-green)

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

**Latest saved flight:** 2026-08-01 21:38:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 21:38:17 UTC

- **165,652** saved flights
- **54,353** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **165,652** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,992,622.7 tonnes** estimated CO2 emissions
- **115,514,357 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6614 |
| 2 | SkyWest Airlines | 6043 |
| 3 | EJA | 3290 |
| 4 | IndiGo | 2912 |
| 5 | American Airlines | 2614 |
| 6 | Southwest Airlines | 2604 |
| 7 | ENY | 2059 |
| 8 | Delta Air Lines | 1979 |
| 9 | LATAM Airlines | 1544 |
| 10 | Lufthansa | 1537 |
| 11 | AZU | 1452 |
| 12 | WIF | 1388 |
| 13 | Vueling | 1367 |
| 14 | LXJ | 1288 |
| 15 | AXM | 1141 |
| 16 | Swiss International | 1134 |
| 17 | easyJet | 1093 |
| 18 | Alaska Airlines | 1021 |
| 19 | EJU | 1015 |
| 20 | QLK | 1011 |
| 21 | All Nippon Airways | 1009 |
| 22 | VIV | 912 |
| 23 | CXK | 886 |
| 24 | Cathay Pacific | 879 |
| 25 | United Airlines | 876 |
| 26 | AEE | 871 |
| 27 | GLO | 867 |
| 28 | Air France | 855 |
| 29 | MXY | 855 |
| 30 | JetBlue | 839 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 143084 |
| 2 | 🇪🇸 ES | 10594 |
| 3 | 🇧🇷 BR | 9432 |
| 4 | 🇦🇺 AU | 9260 |
| 5 | 🇮🇳 IN | 9136 |
| 6 | 🇨🇦 CA | 9007 |
| 7 | 🇮🇹 IT | 8558 |
| 8 | 🇩🇪 DE | 8286 |
| 9 | 🇬🇧 GB | 7630 |
| 10 | 🇯🇵 JP | 6660 |
| 11 | 🇫🇷 FR | 6565 |
| 12 | 🇨🇴 CO | 5967 |
| 13 | 🇬🇷 GR | 4785 |
| 14 | 🇲🇽 MX | 4742 |
| 15 | 🇨🇭 CH | 4355 |
| 16 | 🇳🇴 NO | 4343 |
| 17 | 🇹🇷 TR | 3984 |
| 18 | 🇲🇾 MY | 2968 |
| 19 | 🇵🇱 PL | 2806 |
| 20 | 🇿🇦 ZA | 2695 |
| 21 | 🇳🇿 NZ | 2410 |
| 22 | 🇹🇭 TH | 2369 |
| 23 | 🇵🇭 PH | 2173 |
| 24 | 🇬🇹 GT | 2141 |
| 25 | 🇰🇷 KR | 2133 |
| 26 | 🇲🇦 MA | 1668 |
| 27 | 🇭🇷 HR | 1573 |
| 28 | 🇲🇪 ME | 1544 |
| 29 | 🇳🇱 NL | 1501 |
| 30 | 🇲🇴 MO | 1405 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3387 |
| 2 | Denver International Airport |  | US | 2759 |
| 3 | Tokyo International Airport |  | JP | 2095 |
| 4 | Guaymaral Airport |  | CO | 2080 |
| 5 | Indira Gandhi International Airport |  | IN | 2025 |
| 6 | Harry Reid International Airport |  | US | 2003 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1819 |
| 8 | Zurich Airport |  | CH | 1760 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1740 |
| 10 | La Aurora Airport |  | GT | 1658 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1537 |
| 12 | El Dorado International Airport |  | CO | 1520 |
| 13 | Frankfurt am Main International Airport |  | DE | 1499 |
| 14 | Chicago O'Hare International Airport |  | US | 1495 |
| 15 | Salt Lake City International Airport |  | US | 1486 |
| 16 | Macau International Airport |  | MO | 1405 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1384 |
| 18 | Congonhas Airport |  | BR | 1367 |
| 19 | Madrid Barajas International Airport |  | ES | 1306 |
| 20 | Capua Airport |  | IT | 1296 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1262 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1172 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1163 |
| 24 | Charlotte/Douglas International Airport |  | US | 1159 |
| 25 | Charles de Gaulle International Airport |  | FR | 1131 |
| 26 | Kuala Lumpur International Airport |  | MY | 1124 |
| 27 | Malpensa International Airport |  | IT | 1107 |
| 28 | Bengaluru International Airport |  | IN | 1081 |
| 29 | Ninoy Aquino International Airport |  | PH | 1022 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1019 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1015 |
| 32 | Barcelona International Airport |  | ES | 978 |
| 33 | Daniel K Inouye International Airport |  | US | 966 |
| 34 | Seattle-Tacoma International Airport |  | US | 960 |
| 35 | Calgary International Airport |  | CA | 943 |
| 36 | Viracopos International Airport |  | BR | 939 |
| 37 | Scottsdale Airport |  | US | 925 |
| 38 | Tenerife Norte Airport |  | ES | 923 |
| 39 | Oslo Gardermoen Airport |  | NO | 920 |
| 40 | Reno/Tahoe International Airport |  | US | 914 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 604 | 21m | 244 km | 2,543.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 399 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 395 | 24m | 225 km | 1,532.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 377 | 1h 9m | 770 km | 5,008.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 308 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 242 | 19m | 165 km | 688.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 239 | 44m | 241 km | 992.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 228 | 1h 47m | 1,423 km | 5,595.5 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 217 | 20m | 250 km | 937.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 215 | 26m | 215 km | 796.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 205 | 31m | 49 km | 173.3 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 195 | 19m | 144 km | 485.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 191 | 31m | 369 km | 1,215.8 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 189 | 50m | 556 km | 1,811.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 189 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 186 | 1h 38m | 1,156 km | 3,710.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 181 | 44m | 452 km | 1,410.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 178 | 24m | 218 km | 670.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LHX948 | LHX | Frankfurt am Main International Airport (EDDF) | Manchester Airport (EGCC) | 2026-08-01 20:20 UTC | 2026-08-01 21:38 UTC | 1h 17m |
| TKR132 | TKR | Boise Air Trml/Gowen Field (KBOI) | Reek Ranch Airport (ID63) | 2026-08-01 21:24 UTC | 2026-08-01 21:36 UTC | 11m |
| BOX712 | BOX | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-08-01 14:44 UTC | 2026-08-01 21:31 UTC | 6h 46m |
| TKR140 | TKR | Hill Afb Airport (KHIF) | K43U (K43U) | 2026-08-01 21:05 UTC | 2026-08-01 21:26 UTC | 21m |
| N18MG |  | Sweetwater (Usmc) Airport (NV72) | Bryant Field (KO57) | 2026-08-01 20:51 UTC | 2026-08-01 21:16 UTC | 24m |
| TIBJJ | TIB | Las Piedras Airport (MRLP) | Juan Santamaria International Airport (MROC) | 2026-08-01 20:47 UTC | 2026-08-01 21:13 UTC | 25m |
| N616SP |  | 6SC1 (6SC1) | Bradley Field (NC29) | 2026-08-01 20:20 UTC | 2026-08-01 21:12 UTC | 51m |
| N80484 |  | Montgomery County Airpark (KGAI) | Capital City Airport (KCXY) | 2026-08-01 20:31 UTC | 2026-08-01 21:11 UTC | 40m |
|  |  | Rafael Nunez International Airport (SKCG) | Tolu Airport (SKTL) | 2026-08-01 20:52 UTC | 2026-08-01 21:06 UTC | 13m |
| AAL1917 | American Airlines | Miami International Airport (KMIA) | Clarence A. Bain Airport (MYAB) | 2026-08-01 16:52 UTC | 2026-08-01 21:03 UTC | 4h 11m |
| N6989M |  | Harnett Regional Jetport Airport (KHRJ) | Harnett Regional Jetport Airport (KHRJ) | 2026-08-01 20:27 UTC | 2026-08-01 21:03 UTC | 36m |
| AIZ1166 | AIZ | Larnaca International Airport (LCLK) | Larnaca International Airport (LCLK) | 2026-08-01 20:51 UTC | 2026-08-01 21:03 UTC | 11m |
| LXJ366 | LXJ | Napa County Airport (KAPC) | Rancho San Simeon Airport (66CA) | 2026-08-01 20:22 UTC | 2026-08-01 20:58 UTC | 36m |
| N814SS |  | Nikolai Creek Airport (9AK3) | Trading Bay Production Airport (5AK0) | 2026-08-01 20:47 UTC | 2026-08-01 20:57 UTC | 10m |
| AUD91 | AUD | Orlando Sanford International Airport (KSFB) | Abaco I Walker C Airport (MYAW) | 2026-08-01 20:02 UTC | 2026-08-01 20:56 UTC | 53m |
| FTO501 | FTO | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-01 20:11 UTC | 2026-08-01 20:55 UTC | 44m |
| N310WJ |  | Nampa Municipal Airport (KMAN) | Oasis Airpark (1ID4) | 2026-08-01 19:45 UTC | 2026-08-01 20:54 UTC | 1h 9m |
| JUMP16 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-01 20:28 UTC | 2026-08-01 20:53 UTC | 25m |
| N38EE |  | Dayton Valley Airpark (KA34) | Sweetwater (Usmc) Airport (NV72) | 2026-08-01 19:54 UTC | 2026-08-01 20:49 UTC | 55m |
| SKW3686 | SkyWest Airlines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Moose Lake Carlton County Airport (KMZH) | 2026-08-01 20:27 UTC | 2026-08-01 20:49 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
