# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_03:44:36_UTC-green)

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

**Latest saved flight:** 2026-07-12 03:44:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-12 03:44:36 UTC

- **138,239** saved flights
- **46,616** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **138,239** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,660,792.3 tonnes** estimated CO2 emissions
- **96,277,815 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5618 |
| 2 | SkyWest Airlines | 5076 |
| 3 | EJA | 2714 |
| 4 | IndiGo | 2540 |
| 5 | American Airlines | 2182 |
| 6 | Southwest Airlines | 2088 |
| 7 | ENY | 1736 |
| 8 | Delta Air Lines | 1645 |
| 9 | Lufthansa | 1409 |
| 10 | LATAM Airlines | 1271 |
| 11 | Vueling | 1195 |
| 12 | WIF | 1190 |
| 13 | AZU | 1187 |
| 14 | LXJ | 1061 |
| 15 | AXM | 1034 |
| 16 | Swiss International | 983 |
| 17 | easyJet | 895 |
| 18 | All Nippon Airways | 891 |
| 19 | Alaska Airlines | 873 |
| 20 | QLK | 860 |
| 21 | EJU | 848 |
| 22 | VIV | 759 |
| 23 | AEE | 747 |
| 24 | CXK | 740 |
| 25 | Air France | 738 |
| 26 | United Airlines | 729 |
| 27 | Cathay Pacific | 727 |
| 28 | JetBlue | 726 |
| 29 | MXY | 721 |
| 30 | GLO | 708 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 118857 |
| 2 | 🇪🇸 ES | 9087 |
| 3 | 🇮🇳 IN | 7962 |
| 4 | 🇦🇺 AU | 7892 |
| 5 | 🇧🇷 BR | 7800 |
| 6 | 🇨🇦 CA | 7278 |
| 7 | 🇮🇹 IT | 7213 |
| 8 | 🇩🇪 DE | 7205 |
| 9 | 🇬🇧 GB | 6261 |
| 10 | 🇯🇵 JP | 5831 |
| 11 | 🇫🇷 FR | 5494 |
| 12 | 🇨🇴 CO | 4371 |
| 13 | 🇲🇽 MX | 4011 |
| 14 | 🇬🇷 GR | 3943 |
| 15 | 🇳🇴 NO | 3723 |
| 16 | 🇨🇭 CH | 3577 |
| 17 | 🇹🇷 TR | 3227 |
| 18 | 🇲🇾 MY | 2687 |
| 19 | 🇵🇱 PL | 2316 |
| 20 | 🇿🇦 ZA | 2260 |
| 21 | 🇳🇿 NZ | 2126 |
| 22 | 🇹🇭 TH | 2093 |
| 23 | 🇰🇷 KR | 1998 |
| 24 | 🇵🇭 PH | 1883 |
| 25 | 🇬🇹 GT | 1839 |
| 26 | 🇲🇦 MA | 1455 |
| 27 | 🇲🇪 ME | 1369 |
| 28 | 🇳🇱 NL | 1287 |
| 29 | 🇭🇷 HR | 1250 |
| 30 | 🇲🇴 MO | 1188 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2870 |
| 2 | Denver International Airport |  | US | 2319 |
| 3 | Tokyo International Airport |  | JP | 1898 |
| 4 | Indira Gandhi International Airport |  | IN | 1759 |
| 5 | Harry Reid International Airport |  | US | 1728 |
| 6 | Guaymaral Airport |  | CO | 1684 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1602 |
| 8 | Zurich Airport |  | CH | 1533 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1458 |
| 10 | La Aurora Airport |  | GT | 1421 |
| 11 | Frankfurt am Main International Airport |  | DE | 1364 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1326 |
| 13 | Chicago O'Hare International Airport |  | US | 1306 |
| 14 | El Dorado International Airport |  | CO | 1231 |
| 15 | Salt Lake City International Airport |  | US | 1227 |
| 16 | Macau International Airport |  | MO | 1188 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1186 |
| 18 | Capua Airport |  | IT | 1133 |
| 19 | Madrid Barajas International Airport |  | ES | 1125 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1117 |
| 21 | Congonhas Airport |  | BR | 1113 |
| 22 | Kuala Lumpur International Airport |  | MY | 1042 |
| 23 | Charlotte/Douglas International Airport |  | US | 1012 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 994 |
| 25 | Charles de Gaulle International Airport |  | FR | 982 |
| 26 | Bengaluru International Airport |  | IN | 958 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 953 |
| 28 | Malpensa International Airport |  | IT | 903 |
| 29 | Ninoy Aquino International Airport |  | PH | 876 |
| 30 | Daniel K Inouye International Airport |  | US | 850 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 841 |
| 32 | Barcelona International Airport |  | ES | 840 |
| 33 | Tenerife Norte Airport |  | ES | 812 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 811 |
| 35 | Calgary International Airport |  | CA | 801 |
| 36 | Viracopos International Airport |  | BR | 791 |
| 37 | Scottsdale Airport |  | US | 791 |
| 38 | Seattle-Tacoma International Airport |  | US | 788 |
| 39 | Vitoria/Foronda Airport |  | ES | 775 |
| 40 | Amsterdam Airport Schiphol |  | NL | 772 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 709 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 500 | 21m | 244 km | 2,105.4 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 340 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 338 | 24m | 225 km | 1,311.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 297 | 14m | 114 km | 582.5 t |
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
| AAL2189 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Philadelphia International Airport (KPHL) | 2026-07-12 02:37 UTC | 2026-07-12 03:44 UTC | 1h 7m |
| N3534S |  | OR19 (OR19) | 2OR7 (2OR7) | 2026-07-12 03:11 UTC | 2026-07-12 03:36 UTC | 25m |
| DAL2703 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Philadelphia International Airport (KPHL) | 2026-07-12 01:21 UTC | 2026-07-12 03:28 UTC | 2h 7m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-07-12 02:54 UTC | 2026-07-12 03:23 UTC | 28m |
| BBC471 | BBC | VGZR (VGZR) | Barisal Airport (VGBR) | 2026-07-12 02:59 UTC | 2026-07-12 03:21 UTC | 21m |
| CAP4680 | CAP | Boeing Field/King County International Airport (KBFI) | William R Fairchild International Airport (KCLM) | 2026-07-12 02:34 UTC | 2026-07-12 03:18 UTC | 43m |
| CFR82 | CFR | Nevada County Airport (KGOO) | Sierraville Dearwater Airport (KO79) | 2026-07-12 03:08 UTC | 2026-07-12 03:17 UTC | 8m |
| QLK22D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Woodville Airport (YWVL) | 2026-07-12 02:26 UTC | 2026-07-12 03:10 UTC | 43m |
| CFR94 | CFR | Redding Regional Airport (KRDD) | Rogers Field (KO05) | 2026-07-12 02:38 UTC | 2026-07-12 03:08 UTC | 29m |
| N359BG |  | Wood County Airport (K1G0) | Steinman Airport (53II) | 2026-07-12 02:37 UTC | 2026-07-12 03:06 UTC | 29m |
| DAL1169 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | Philadelphia International Airport (KPHL) | 2026-07-12 01:29 UTC | 2026-07-12 02:58 UTC | 1h 28m |
| QLK109D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-07-12 02:23 UTC | 2026-07-12 02:58 UTC | 34m |
| AXM6077 | AXM | Kota Kinabalu International Airport (WBKK) | Marudi Airport (WBGM) | 2026-07-12 02:32 UTC | 2026-07-12 02:57 UTC | 25m |
| UBG183 | UBG | VGZR (VGZR) | Saidpur Airport (VGSD) | 2026-07-12 02:26 UTC | 2026-07-12 02:57 UTC | 30m |
| FFT4844 | FFT | Raleigh-Durham International Airport (KRDU) | Philadelphia International Airport (KPHL) | 2026-07-12 02:00 UTC | 2026-07-12 02:56 UTC | 55m |
| N690JK |  | Nevada County Airport (KGOO) | Nervino Airport (KO02) | 2026-07-12 02:38 UTC | 2026-07-12 02:52 UTC | 13m |
| CXK138 | CXK | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-07-12 01:45 UTC | 2026-07-12 02:52 UTC | 1h 6m |
| VAR708 | VAR | Phoenix Goodyear Airport (KGYR) | Chiriaco Summit Airport (KL77) | 2026-07-12 01:33 UTC | 2026-07-12 02:47 UTC | 1h 13m |
| N539SH |  | Denali Airport (AK06) | Healy River Airport (PAHV) | 2026-07-12 02:40 UTC | 2026-07-12 02:46 UTC | 6m |
| JAL3106 | Japan Airlines | New Chitose Airport (RJCC) | Chubu Centrair International Airport (RJGG) | 2026-07-12 01:34 UTC | 2026-07-12 02:46 UTC | 1h 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
