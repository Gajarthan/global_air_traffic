# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_15:16:23_UTC-green)

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

**Latest saved flight:** 2026-08-02 15:16:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 15:16:23 UTC

- **166,722** saved flights
- **54,587** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **166,722** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,008,021.6 tonnes** estimated CO2 emissions
- **116,407,050 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6657 |
| 2 | SkyWest Airlines | 6060 |
| 3 | EJA | 3296 |
| 4 | IndiGo | 2942 |
| 5 | American Airlines | 2626 |
| 6 | Southwest Airlines | 2618 |
| 7 | ENY | 2069 |
| 8 | Delta Air Lines | 1988 |
| 9 | LATAM Airlines | 1550 |
| 10 | Lufthansa | 1541 |
| 11 | AZU | 1468 |
| 12 | WIF | 1397 |
| 13 | Vueling | 1375 |
| 14 | LXJ | 1295 |
| 15 | AXM | 1154 |
| 16 | Swiss International | 1144 |
| 17 | easyJet | 1110 |
| 18 | EJU | 1027 |
| 19 | Alaska Airlines | 1026 |
| 20 | QLK | 1020 |
| 21 | All Nippon Airways | 1017 |
| 22 | VIV | 918 |
| 23 | Cathay Pacific | 888 |
| 24 | CXK | 888 |
| 25 | United Airlines | 878 |
| 26 | AEE | 875 |
| 27 | GLO | 875 |
| 28 | Air France | 861 |
| 29 | MXY | 859 |
| 30 | JetBlue | 841 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 143624 |
| 2 | 🇪🇸 ES | 10674 |
| 3 | 🇧🇷 BR | 9497 |
| 4 | 🇦🇺 AU | 9342 |
| 5 | 🇮🇳 IN | 9226 |
| 6 | 🇨🇦 CA | 9038 |
| 7 | 🇮🇹 IT | 8625 |
| 8 | 🇩🇪 DE | 8333 |
| 9 | 🇬🇧 GB | 7727 |
| 10 | 🇯🇵 JP | 6740 |
| 11 | 🇫🇷 FR | 6618 |
| 12 | 🇨🇴 CO | 5996 |
| 13 | 🇬🇷 GR | 4829 |
| 14 | 🇲🇽 MX | 4766 |
| 15 | 🇨🇭 CH | 4400 |
| 16 | 🇳🇴 NO | 4370 |
| 17 | 🇹🇷 TR | 4030 |
| 18 | 🇲🇾 MY | 3007 |
| 19 | 🇵🇱 PL | 2817 |
| 20 | 🇿🇦 ZA | 2717 |
| 21 | 🇳🇿 NZ | 2430 |
| 22 | 🇹🇭 TH | 2424 |
| 23 | 🇵🇭 PH | 2211 |
| 24 | 🇰🇷 KR | 2147 |
| 25 | 🇬🇹 GT | 2141 |
| 26 | 🇲🇦 MA | 1683 |
| 27 | 🇭🇷 HR | 1590 |
| 28 | 🇲🇪 ME | 1550 |
| 29 | 🇳🇱 NL | 1516 |
| 30 | 🇲🇴 MO | 1424 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3405 |
| 2 | Denver International Airport |  | US | 2767 |
| 3 | Tokyo International Airport |  | JP | 2117 |
| 4 | Guaymaral Airport |  | CO | 2085 |
| 5 | Indira Gandhi International Airport |  | IN | 2043 |
| 6 | Harry Reid International Airport |  | US | 2005 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1832 |
| 8 | Zurich Airport |  | CH | 1778 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1749 |
| 10 | La Aurora Airport |  | GT | 1658 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1539 |
| 12 | El Dorado International Airport |  | CO | 1521 |
| 13 | Frankfurt am Main International Airport |  | DE | 1504 |
| 14 | Chicago O'Hare International Airport |  | US | 1503 |
| 15 | Salt Lake City International Airport |  | US | 1490 |
| 16 | Macau International Airport |  | MO | 1424 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1387 |
| 18 | Congonhas Airport |  | BR | 1373 |
| 19 | Madrid Barajas International Airport |  | ES | 1313 |
| 20 | Capua Airport |  | IT | 1300 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1264 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1177 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1175 |
| 24 | Charlotte/Douglas International Airport |  | US | 1163 |
| 25 | Charles de Gaulle International Airport |  | FR | 1138 |
| 26 | Kuala Lumpur International Airport |  | MY | 1136 |
| 27 | Malpensa International Airport |  | IT | 1118 |
| 28 | Bengaluru International Airport |  | IN | 1093 |
| 29 | Ninoy Aquino International Airport |  | PH | 1039 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1025 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1020 |
| 32 | Barcelona International Airport |  | ES | 985 |
| 33 | Daniel K Inouye International Airport |  | US | 971 |
| 34 | Seattle-Tacoma International Airport |  | US | 965 |
| 35 | Viracopos International Airport |  | BR | 951 |
| 36 | Calgary International Airport |  | CA | 944 |
| 37 | Oslo Gardermoen Airport |  | NO | 928 |
| 38 | Tenerife Norte Airport |  | ES | 928 |
| 39 | Scottsdale Airport |  | US | 926 |
| 40 | Reno/Tahoe International Airport |  | US | 917 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 606 | 21m | 244 km | 2,551.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 400 | 24m | 225 km | 1,551.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 399 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 381 | 1h 9m | 770 km | 5,061.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 314 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 287 | 27m | 275 km | 1,360.0 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 245 | 19m | 165 km | 696.9 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 243 | 44m | 241 km | 1,009.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 229 | 1h 47m | 1,423 km | 5,620.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 221 | 20m | 250 km | 954.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 216 | 26m | 215 km | 800.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 210 | 31m | 49 km | 177.5 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 197 | 19m | 144 km | 490.0 t |
| 23 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 194 | 31m | 369 km | 1,234.9 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 189 | 50m | 556 km | 1,811.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 189 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 186 | 1h 38m | 1,156 km | 3,710.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 182 | 1h 1m | 695 km | 2,181.6 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 181 | 24m | 218 km | 681.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGNSS | CGN | Calgary / Springbank Airport (CYBW) | Sparwood Elk Valley Airport (CYSW) | 2026-08-02 14:51 UTC | 2026-08-02 15:16 UTC | 25m |
| ACA807 | Air Canada | Edinburgh Airport (EGPH) | Toronto Pearson International Airport (CYYZ) | 2026-08-02 08:37 UTC | 2026-08-02 15:14 UTC | 6h 37m |
| VAR450 | VAR | Phoenix Goodyear Airport (KGYR) | North Las Vegas Airport (KVGT) | 2026-08-02 13:13 UTC | 2026-08-02 15:07 UTC | 1h 54m |
| XBPBH | XBP | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-08-02 14:22 UTC | 2026-08-02 15:03 UTC | 41m |
| N559SH |  | Gold King Creek Airport (PAAN) | Healy River Airport (PAHV) | 2026-08-02 14:56 UTC | 2026-08-02 15:02 UTC | 6m |
| AFL1747 | AFL | Ukhta Airport (UUYH) | Tunoshna Airport (UUDL) | 2026-08-02 13:54 UTC | 2026-08-02 15:00 UTC | 1h 5m |
| SCU3 | SCU | Jirik Field (OL23) | Ragwing Acres Airport (2OK4) | 2026-08-02 14:25 UTC | 2026-08-02 14:56 UTC | 31m |
| CHX22 | CHX | Gunzburg-Donauried Airport (EDMG) | Erbach Airport (EDNE) | 2026-08-02 14:45 UTC | 2026-08-02 14:52 UTC | 7m |
| N9RY |  | Skypark Airport (KBTF) | Wendover Airport (KENV) | 2026-08-02 14:11 UTC | 2026-08-02 14:52 UTC | 40m |
| FDX79 | FDX | Oakland San Francisco Bay Airport (KOAK) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-02 10:39 UTC | 2026-08-02 14:51 UTC | 4h 12m |
| SCU2 | SCU | Haskell Airport (K2K9) | Jantzen Airport (93OK) | 2026-08-02 14:37 UTC | 2026-08-02 14:49 UTC | 11m |
| CAN25 | CAN | Lamezia Terme Airport (LICA) | Lamezia Terme Airport (LICA) | 2026-08-02 14:20 UTC | 2026-08-02 14:49 UTC | 28m |
| CLX7956 | CLX | Na-San Airport (VVNS) | Zhuhai Airport (ZGSD) | 2026-08-02 13:44 UTC | 2026-08-02 14:46 UTC | 1h 1m |
| FTO501 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-02 14:17 UTC | 2026-08-02 14:46 UTC | 29m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-08-02 14:24 UTC | 2026-08-02 14:45 UTC | 20m |
| N221MF |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-08-02 14:41 UTC | 2026-08-02 14:44 UTC | 2m |
| TRF517 | TRF | Addison Airport (KADS) | Addison Airport (KADS) | 2026-08-02 13:10 UTC | 2026-08-02 14:43 UTC | 1h 32m |
| GBMSB | GBM | Newquay Cornwall Airport (EGHQ) | Truro Airport (EGHY) | 2026-08-02 14:35 UTC | 2026-08-02 14:42 UTC | 6m |
| SWA8503 | Southwest Airlines | Denver International Airport (KDEN) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-02 12:36 UTC | 2026-08-02 14:41 UTC | 2h 5m |
| HBZVU | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-08-02 14:39 UTC | 2026-08-02 14:41 UTC | 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
