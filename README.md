# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_16:16:26_UTC-green)

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

**Latest saved flight:** 2026-08-02 16:16:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 16:16:26 UTC

- **166,893** saved flights
- **54,640** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **166,893** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,010,240.9 tonnes** estimated CO2 emissions
- **116,535,706 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6659 |
| 2 | SkyWest Airlines | 6064 |
| 3 | EJA | 3302 |
| 4 | IndiGo | 2943 |
| 5 | American Airlines | 2628 |
| 6 | Southwest Airlines | 2622 |
| 7 | ENY | 2071 |
| 8 | Delta Air Lines | 1991 |
| 9 | LATAM Airlines | 1550 |
| 10 | Lufthansa | 1543 |
| 11 | AZU | 1469 |
| 12 | WIF | 1398 |
| 13 | Vueling | 1376 |
| 14 | LXJ | 1296 |
| 15 | AXM | 1154 |
| 16 | Swiss International | 1147 |
| 17 | easyJet | 1116 |
| 18 | EJU | 1029 |
| 19 | Alaska Airlines | 1026 |
| 20 | QLK | 1020 |
| 21 | All Nippon Airways | 1017 |
| 22 | VIV | 919 |
| 23 | Cathay Pacific | 888 |
| 24 | CXK | 888 |
| 25 | United Airlines | 878 |
| 26 | AEE | 876 |
| 27 | GLO | 876 |
| 28 | Air France | 862 |
| 29 | MXY | 859 |
| 30 | JetBlue | 841 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 143754 |
| 2 | 🇪🇸 ES | 10695 |
| 3 | 🇧🇷 BR | 9505 |
| 4 | 🇦🇺 AU | 9344 |
| 5 | 🇮🇳 IN | 9234 |
| 6 | 🇨🇦 CA | 9041 |
| 7 | 🇮🇹 IT | 8633 |
| 8 | 🇩🇪 DE | 8346 |
| 9 | 🇬🇧 GB | 7743 |
| 10 | 🇯🇵 JP | 6740 |
| 11 | 🇫🇷 FR | 6627 |
| 12 | 🇨🇴 CO | 6004 |
| 13 | 🇬🇷 GR | 4842 |
| 14 | 🇲🇽 MX | 4772 |
| 15 | 🇨🇭 CH | 4407 |
| 16 | 🇳🇴 NO | 4372 |
| 17 | 🇹🇷 TR | 4034 |
| 18 | 🇲🇾 MY | 3007 |
| 19 | 🇵🇱 PL | 2823 |
| 20 | 🇿🇦 ZA | 2719 |
| 21 | 🇳🇿 NZ | 2430 |
| 22 | 🇹🇭 TH | 2424 |
| 23 | 🇵🇭 PH | 2211 |
| 24 | 🇰🇷 KR | 2147 |
| 25 | 🇬🇹 GT | 2145 |
| 26 | 🇲🇦 MA | 1684 |
| 27 | 🇭🇷 HR | 1593 |
| 28 | 🇲🇪 ME | 1550 |
| 29 | 🇳🇱 NL | 1518 |
| 30 | 🇲🇴 MO | 1425 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3408 |
| 2 | Denver International Airport |  | US | 2768 |
| 3 | Tokyo International Airport |  | JP | 2117 |
| 4 | Guaymaral Airport |  | CO | 2085 |
| 5 | Indira Gandhi International Airport |  | IN | 2045 |
| 6 | Harry Reid International Airport |  | US | 2006 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1835 |
| 8 | Zurich Airport |  | CH | 1782 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1751 |
| 10 | La Aurora Airport |  | GT | 1660 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1540 |
| 12 | El Dorado International Airport |  | CO | 1521 |
| 13 | Frankfurt am Main International Airport |  | DE | 1505 |
| 14 | Chicago O'Hare International Airport |  | US | 1504 |
| 15 | Salt Lake City International Airport |  | US | 1490 |
| 16 | Macau International Airport |  | MO | 1425 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1388 |
| 18 | Congonhas Airport |  | BR | 1374 |
| 19 | Madrid Barajas International Airport |  | ES | 1317 |
| 20 | Capua Airport |  | IT | 1301 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1269 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1177 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1176 |
| 24 | Charlotte/Douglas International Airport |  | US | 1164 |
| 25 | Charles de Gaulle International Airport |  | FR | 1138 |
| 26 | Kuala Lumpur International Airport |  | MY | 1136 |
| 27 | Malpensa International Airport |  | IT | 1121 |
| 28 | Bengaluru International Airport |  | IN | 1095 |
| 29 | Ninoy Aquino International Airport |  | PH | 1039 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1025 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1020 |
| 32 | Barcelona International Airport |  | ES | 985 |
| 33 | Daniel K Inouye International Airport |  | US | 972 |
| 34 | Seattle-Tacoma International Airport |  | US | 965 |
| 35 | Viracopos International Airport |  | BR | 952 |
| 36 | Calgary International Airport |  | CA | 944 |
| 37 | Oslo Gardermoen Airport |  | NO | 929 |
| 38 | Tenerife Norte Airport |  | ES | 929 |
| 39 | Scottsdale Airport |  | US | 928 |
| 40 | Reno/Tahoe International Airport |  | US | 919 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 607 | 21m | 244 km | 2,555.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 400 | 24m | 225 km | 1,551.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 399 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 381 | 1h 9m | 770 km | 5,061.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 315 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 288 | 27m | 275 km | 1,364.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 245 | 19m | 165 km | 696.9 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 244 | 44m | 241 km | 1,013.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 230 | 1h 47m | 1,423 km | 5,644.6 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 221 | 20m | 250 km | 954.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 216 | 26m | 215 km | 800.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 210 | 31m | 49 km | 177.5 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 197 | 19m | 144 km | 490.0 t |
| 23 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 194 | 31m | 369 km | 1,234.9 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 190 | 50m | 556 km | 1,821.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 189 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 187 | 1h 38m | 1,156 km | 3,730.6 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 182 | 24m | 218 km | 685.7 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 182 | 1h 1m | 695 km | 2,181.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JPR92 | JPR | Hopkins Field (KAIB) | Cortez Municipal Airport (KCEZ) | 2026-08-02 15:56 UTC | 2026-08-02 16:16 UTC | 19m |
| GPJCD | GPJ | Norwich International Airport (EGSH) | Norwich International Airport (EGSH) | 2026-08-02 15:31 UTC | 2026-08-02 16:06 UTC | 35m |
| HUE40H | HUE | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Samedan Airport (LSZS) | 2026-08-02 15:13 UTC | 2026-08-02 16:05 UTC | 51m |
| DCDSO | DCD | Reichelsheim Airport (EDFB) | Hamburg Airport (EDDH) | 2026-08-02 15:18 UTC | 2026-08-02 16:03 UTC | 45m |
| SPSDW | SPS | Lubin Airport (EPLU) | Lubin Airport (EPLU) | 2026-08-02 15:35 UTC | 2026-08-02 16:02 UTC | 26m |
| CARNL32 | CAR | Medina River Ranch Airport (XS43) | Benson Airstrip (2XS8) | 2026-08-02 15:44 UTC | 2026-08-02 15:57 UTC | 13m |
| N543TH |  | Trenton Mercer Airport (KTTN) | Lehigh Valley International Airport (KABE) | 2026-08-02 15:23 UTC | 2026-08-02 15:56 UTC | 32m |
| N33LS |  | Aurora State Airport (KUAO) | Venell Airport (OR52) | 2026-08-02 15:17 UTC | 2026-08-02 15:53 UTC | 36m |
| N997TX |  | Lexington Airfield (TE75) | Lexington Airfield (TE75) | 2026-08-02 15:19 UTC | 2026-08-02 15:49 UTC | 29m |
| MNB552 | MNB | Belgrade Nikola Tesla Airport (LYBE) | Macau International Airport (VMMC) | 2026-08-01 23:05 UTC | 2026-08-02 15:47 UTC | 16h 42m |
| N582TC |  | Skypark Airport (KBTF) | Preston Airport (KU10) | 2026-08-02 15:06 UTC | 2026-08-02 15:45 UTC | 39m |
| N310LS |  | Minden-Tahoe Airport (KMEV) | Desert Creek Airport (NV97) | 2026-08-02 15:23 UTC | 2026-08-02 15:44 UTC | 21m |
| N529LF |  | Albuquerque International Sunport Airport (KABQ) | Skywagon Farm Airport (NM88) | 2026-08-02 15:16 UTC | 2026-08-02 15:43 UTC | 27m |
| TGKME | TGK | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-08-02 15:15 UTC | 2026-08-02 15:41 UTC | 26m |
| WIF158 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-02 14:47 UTC | 2026-08-02 15:40 UTC | 52m |
| LDX344C | LDX | Dusseldorf International Airport (EDDL) | Raron Airport (LSTA) | 2026-08-02 14:44 UTC | 2026-08-02 15:39 UTC | 55m |
| DHAIU | DHA | Warsaw Chopin Airport (EPWA) | Warsaw Chopin Airport (EPWA) | 2026-08-02 15:30 UTC | 2026-08-02 15:37 UTC | 7m |
| ENSAIO39 | ENS | Sitio Sao Jose Airport (SDZZ) | Fazenda Santa Maria Airport (SDDJ) | 2026-08-02 15:05 UTC | 2026-08-02 15:35 UTC | 29m |
| NSZ3152 | NSZ | Copenhagen Kastrup Airport (EKCH) | Helsinki Vantaa Airport (EFHK) | 2026-08-02 14:15 UTC | 2026-08-02 15:35 UTC | 1h 19m |
| N401SS |  | Boulder Municipal Airport (KBDU) | CO86 (CO86) | 2026-08-02 15:11 UTC | 2026-08-02 15:35 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
