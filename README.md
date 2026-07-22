# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--22_17:33:32_UTC-green)

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

**Latest saved flight:** 2026-07-22 17:33:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-22 17:33:32 UTC

- **144,193** saved flights
- **48,306** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **144,193** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,727,637.7 tonnes** estimated CO2 emissions
- **100,152,908 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5856 |
| 2 | SkyWest Airlines | 5270 |
| 3 | EJA | 2841 |
| 4 | IndiGo | 2621 |
| 5 | American Airlines | 2307 |
| 6 | Southwest Airlines | 2177 |
| 7 | ENY | 1792 |
| 8 | Delta Air Lines | 1709 |
| 9 | Lufthansa | 1443 |
| 10 | LATAM Airlines | 1325 |
| 11 | AZU | 1240 |
| 12 | Vueling | 1236 |
| 13 | WIF | 1234 |
| 14 | LXJ | 1106 |
| 15 | AXM | 1063 |
| 16 | Swiss International | 1026 |
| 17 | easyJet | 939 |
| 18 | All Nippon Airways | 922 |
| 19 | Alaska Airlines | 909 |
| 20 | QLK | 906 |
| 21 | EJU | 884 |
| 22 | VIV | 801 |
| 23 | CXK | 773 |
| 24 | AEE | 764 |
| 25 | Air France | 764 |
| 26 | JetBlue | 763 |
| 27 | MXY | 749 |
| 28 | Cathay Pacific | 748 |
| 29 | United Airlines | 746 |
| 30 | GLO | 740 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 124129 |
| 2 | 🇪🇸 ES | 9366 |
| 3 | 🇦🇺 AU | 8242 |
| 4 | 🇮🇳 IN | 8209 |
| 5 | 🇧🇷 BR | 8134 |
| 6 | 🇨🇦 CA | 7622 |
| 7 | 🇮🇹 IT | 7518 |
| 8 | 🇩🇪 DE | 7448 |
| 9 | 🇬🇧 GB | 6586 |
| 10 | 🇯🇵 JP | 6036 |
| 11 | 🇫🇷 FR | 5744 |
| 12 | 🇨🇴 CO | 4660 |
| 13 | 🇲🇽 MX | 4196 |
| 14 | 🇬🇷 GR | 4089 |
| 15 | 🇳🇴 NO | 3858 |
| 16 | 🇨🇭 CH | 3747 |
| 17 | 🇹🇷 TR | 3388 |
| 18 | 🇲🇾 MY | 2775 |
| 19 | 🇵🇱 PL | 2427 |
| 20 | 🇿🇦 ZA | 2350 |
| 21 | 🇳🇿 NZ | 2209 |
| 22 | 🇹🇭 TH | 2129 |
| 23 | 🇰🇷 KR | 2037 |
| 24 | 🇵🇭 PH | 1934 |
| 25 | 🇬🇹 GT | 1885 |
| 26 | 🇲🇦 MA | 1498 |
| 27 | 🇲🇪 ME | 1430 |
| 28 | 🇳🇱 NL | 1354 |
| 29 | 🇭🇷 HR | 1313 |
| 30 | 🇲🇴 MO | 1207 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2974 |
| 2 | Denver International Airport |  | US | 2415 |
| 3 | Tokyo International Airport |  | JP | 1942 |
| 4 | Indira Gandhi International Airport |  | IN | 1821 |
| 5 | Harry Reid International Airport |  | US | 1807 |
| 6 | Guaymaral Airport |  | CO | 1765 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1640 |
| 8 | Zurich Airport |  | CH | 1597 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1510 |
| 10 | La Aurora Airport |  | GT | 1460 |
| 11 | Frankfurt am Main International Airport |  | DE | 1388 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1361 |
| 13 | Chicago O'Hare International Airport |  | US | 1344 |
| 14 | Salt Lake City International Airport |  | US | 1290 |
| 15 | El Dorado International Airport |  | CO | 1277 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1261 |
| 17 | Macau International Airport |  | MO | 1207 |
| 18 | Capua Airport |  | IT | 1176 |
| 19 | Congonhas Airport |  | BR | 1157 |
| 20 | Madrid Barajas International Airport |  | ES | 1150 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1138 |
| 22 | Kuala Lumpur International Airport |  | MY | 1072 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1043 |
| 24 | Charlotte/Douglas International Airport |  | US | 1035 |
| 25 | Charles de Gaulle International Airport |  | FR | 1008 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1006 |
| 27 | Bengaluru International Airport |  | IN | 979 |
| 28 | Malpensa International Airport |  | IT | 933 |
| 29 | Ninoy Aquino International Airport |  | PH | 903 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 882 |
| 31 | Barcelona International Airport |  | ES | 876 |
| 32 | Daniel K Inouye International Airport |  | US | 875 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 860 |
| 34 | Tenerife Norte Airport |  | ES | 827 |
| 35 | Seattle-Tacoma International Airport |  | US | 821 |
| 36 | Viracopos International Airport |  | BR | 819 |
| 37 | Calgary International Airport |  | CA | 819 |
| 38 | Scottsdale Airport |  | US | 815 |
| 39 | Amsterdam Airport Schiphol |  | NL | 814 |
| 40 | Oslo Gardermoen Airport |  | NO | 791 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 744 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 524 | 21m | 244 km | 2,206.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 351 | 24m | 225 km | 1,361.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 350 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 340 | 1h 9m | 770 km | 4,516.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 260 | 26m | 275 km | 1,232.0 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 257 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 217 | 22m | 55 km | 206.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 193 | 1h 46m | 1,423 km | 4,736.5 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 193 | 44m | 241 km | 801.7 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 190 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 179 | 20m | 250 km | 773.2 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 173 | 18m | 144 km | 430.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 168 | 44m | 452 km | 1,309.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 168 | 1h 16m | 961 km | 2,784.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 164 | 1h 38m | 1,156 km | 3,271.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 164 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGHHA | CGH | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-07-22 17:16 UTC | 2026-07-22 17:33 UTC | 17m |
| N567FL |  | Reading Regional/Carl A Spaatz Field (KRDG) | Lancaster Airport (KLNS) | 2026-07-22 17:18 UTC | 2026-07-22 17:30 UTC | 12m |
| OSPRY02 | OSP | Salisbury-Ocean City Wicomico Regional Airport (KSBY) | Delmarvair Airport (6MD8) | 2026-07-22 17:15 UTC | 2026-07-22 17:29 UTC | 14m |
| N538WH |  | CO09 (CO09) | CO09 (CO09) | 2026-07-22 16:50 UTC | 2026-07-22 17:29 UTC | 38m |
| N52654 |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-07-22 16:28 UTC | 2026-07-22 17:28 UTC | 59m |
| N4409X |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-07-22 17:01 UTC | 2026-07-22 17:27 UTC | 25m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-07-22 17:10 UTC | 2026-07-22 17:21 UTC | 11m |
| UAE9784 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-07-22 10:39 UTC | 2026-07-22 17:20 UTC | 6h 41m |
| N714XB |  | Sanctuary Ranch Airport (7TS4) | Denton Enterprise Airport (KDTO) | 2026-07-22 15:35 UTC | 2026-07-22 17:17 UTC | 1h 41m |
| HBDIH | HBD | Wangen-Lachen Airport (LSPV) | Bad Ragaz Airport (LSZE) | 2026-07-22 16:47 UTC | 2026-07-22 17:14 UTC | 26m |
| N13658 |  | Lake Elmo Airport (K21D) | Rochester International Airport (KRST) | 2026-07-22 16:31 UTC | 2026-07-22 17:14 UTC | 42m |
| N440EH |  | Sacramento Mather Airport (KMHR) | Circle L Ranch Airport (NV27) | 2026-07-22 15:44 UTC | 2026-07-22 17:12 UTC | 1h 28m |
| N8083L |  | Hermitage Airport (45CN) | Buchanan Field (KCCR) | 2026-07-22 16:24 UTC | 2026-07-22 17:11 UTC | 46m |
| AXEL21 | AXE | Whetstone Airport (11AZ) | Oakland San Francisco Bay Airport (KOAK) | 2026-07-22 15:28 UTC | 2026-07-22 17:10 UTC | 1h 42m |
| N66HC |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-07-22 15:41 UTC | 2026-07-22 17:10 UTC | 1h 29m |
| XBPNU | XBP | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-07-22 16:29 UTC | 2026-07-22 17:09 UTC | 40m |
| N564LM |  | St Mary's County Regional Airport (K2W6) | Easton/Newnam Field (KESN) | 2026-07-22 16:47 UTC | 2026-07-22 17:08 UTC | 20m |
| N1401E |  | Usaf Academy Davis Airfield (KAFF) | Limon Municipal Airport (KLIC) | 2026-07-22 16:33 UTC | 2026-07-22 17:07 UTC | 34m |
| ACW1731 | ACW | Del Norte International Airport (MMAN) | Del Norte International Airport (MMAN) | 2026-07-22 17:06 UTC | 2026-07-22 17:06 UTC | 0m |
| VAR450 | VAR | Gene Wash Reservoir Airport (5CL7) | Lake Havasu City Airport (KHII) | 2026-07-22 16:41 UTC | 2026-07-22 17:05 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
