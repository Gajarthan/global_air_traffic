# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_22:56:26_UTC-green)

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

**Latest saved flight:** 2026-08-02 22:56:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 22:56:26 UTC

- **167,951** saved flights
- **54,914** unique routes
- **139** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **167,951** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **2,024,994.9 tonnes** estimated CO2 emissions
- **117,391,006 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6701 |
| 2 | SkyWest Airlines | 6136 |
| 3 | EJA | 3342 |
| 4 | IndiGo | 2952 |
| 5 | American Airlines | 2650 |
| 6 | Southwest Airlines | 2645 |
| 7 | ENY | 2094 |
| 8 | Delta Air Lines | 2007 |
| 9 | LATAM Airlines | 1556 |
| 10 | Lufthansa | 1543 |
| 11 | AZU | 1479 |
| 12 | WIF | 1401 |
| 13 | Vueling | 1383 |
| 14 | LXJ | 1317 |
| 15 | AXM | 1154 |
| 16 | Swiss International | 1151 |
| 17 | easyJet | 1130 |
| 18 | EJU | 1033 |
| 19 | Alaska Airlines | 1029 |
| 20 | QLK | 1020 |
| 21 | All Nippon Airways | 1017 |
| 22 | VIV | 925 |
| 23 | Cathay Pacific | 897 |
| 24 | CXK | 892 |
| 25 | United Airlines | 887 |
| 26 | GLO | 881 |
| 27 | AEE | 880 |
| 28 | Air France | 865 |
| 29 | MXY | 863 |
| 30 | JetBlue | 849 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 144912 |
| 2 | 🇪🇸 ES | 10762 |
| 3 | 🇧🇷 BR | 9564 |
| 4 | 🇦🇺 AU | 9352 |
| 5 | 🇮🇳 IN | 9255 |
| 6 | 🇨🇦 CA | 9109 |
| 7 | 🇮🇹 IT | 8675 |
| 8 | 🇩🇪 DE | 8369 |
| 9 | 🇬🇧 GB | 7802 |
| 10 | 🇯🇵 JP | 6740 |
| 11 | 🇫🇷 FR | 6660 |
| 12 | 🇨🇴 CO | 6058 |
| 13 | 🇬🇷 GR | 4878 |
| 14 | 🇲🇽 MX | 4801 |
| 15 | 🇨🇭 CH | 4417 |
| 16 | 🇳🇴 NO | 4385 |
| 17 | 🇹🇷 TR | 4060 |
| 18 | 🇲🇾 MY | 3009 |
| 19 | 🇵🇱 PL | 2831 |
| 20 | 🇿🇦 ZA | 2723 |
| 21 | 🇳🇿 NZ | 2440 |
| 22 | 🇹🇭 TH | 2424 |
| 23 | 🇵🇭 PH | 2221 |
| 24 | 🇬🇹 GT | 2171 |
| 25 | 🇰🇷 KR | 2147 |
| 26 | 🇲🇦 MA | 1703 |
| 27 | 🇭🇷 HR | 1608 |
| 28 | 🇲🇪 ME | 1553 |
| 29 | 🇳🇱 NL | 1527 |
| 30 | 🇲🇴 MO | 1426 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3451 |
| 2 | Denver International Airport |  | US | 2794 |
| 3 | Tokyo International Airport |  | JP | 2117 |
| 4 | Guaymaral Airport |  | CO | 2094 |
| 5 | Indira Gandhi International Airport |  | IN | 2050 |
| 6 | Harry Reid International Airport |  | US | 2024 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1841 |
| 8 | Zurich Airport |  | CH | 1786 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1768 |
| 10 | La Aurora Airport |  | GT | 1677 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1547 |
| 12 | El Dorado International Airport |  | CO | 1524 |
| 13 | Chicago O'Hare International Airport |  | US | 1523 |
| 14 | Frankfurt am Main International Airport |  | DE | 1511 |
| 15 | Salt Lake City International Airport |  | US | 1505 |
| 16 | Macau International Airport |  | MO | 1426 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1393 |
| 18 | Congonhas Airport |  | BR | 1378 |
| 19 | Madrid Barajas International Airport |  | ES | 1325 |
| 20 | Capua Airport |  | IT | 1307 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1278 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1184 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1176 |
| 24 | Charlotte/Douglas International Airport |  | US | 1171 |
| 25 | Charles de Gaulle International Airport |  | FR | 1144 |
| 26 | Kuala Lumpur International Airport |  | MY | 1137 |
| 27 | Malpensa International Airport |  | IT | 1129 |
| 28 | Bengaluru International Airport |  | IN | 1096 |
| 29 | Ninoy Aquino International Airport |  | PH | 1044 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1039 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1031 |
| 32 | Barcelona International Airport |  | ES | 991 |
| 33 | Daniel K Inouye International Airport |  | US | 977 |
| 34 | Seattle-Tacoma International Airport |  | US | 976 |
| 35 | Viracopos International Airport |  | BR | 958 |
| 36 | Calgary International Airport |  | CA | 952 |
| 37 | Tenerife Norte Airport |  | ES | 938 |
| 38 | Reno/Tahoe International Airport |  | US | 933 |
| 39 | Oslo Gardermoen Airport |  | NO | 932 |
| 40 | Scottsdale Airport |  | US | 930 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 871 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 610 | 21m | 244 km | 2,568.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 401 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 400 | 24m | 225 km | 1,551.8 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 381 | 1h 9m | 770 km | 5,061.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 316 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 288 | 27m | 275 km | 1,364.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 245 | 19m | 165 km | 696.9 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 244 | 44m | 241 km | 1,013.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 231 | 1h 47m | 1,423 km | 5,669.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 221 | 20m | 250 km | 954.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 218 | 26m | 215 km | 807.4 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 215 | 31m | 49 km | 181.7 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 199 | 19m | 144 km | 495.0 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 196 | 31m | 369 km | 1,247.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 195 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 194 | 50m | 556 km | 1,859.7 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 187 | 1h 38m | 1,156 km | 3,730.6 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 184 | 24m | 218 km | 693.2 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 183 | 1h 1m | 695 km | 2,193.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FXC22 | FXC | Bridgeport/Sikorsky Airport (KBDR) | Teterboro Airport (KTEB) | 2026-08-02 22:33 UTC | 2026-08-02 22:56 UTC | 23m |
| N1314T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-02 20:40 UTC | 2026-08-02 22:53 UTC | 2h 12m |
| N3288 |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-08-02 22:34 UTC | 2026-08-02 22:51 UTC | 17m |
| N15MJ |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-08-02 21:46 UTC | 2026-08-02 22:38 UTC | 51m |
| N622TP |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-02 22:10 UTC | 2026-08-02 22:33 UTC | 23m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-08-02 11:57 UTC | 2026-08-02 22:31 UTC | 10h 33m |
| N417CF |  | Granbury Regional Airport (KGDJ) | Nassau Bay Airport (0TX0) | 2026-08-02 22:23 UTC | 2026-08-02 22:28 UTC | 5m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Zhuhai Airport (ZGSD) | 2026-08-02 11:19 UTC | 2026-08-02 22:28 UTC | 11h 9m |
| CAP451 | CAP | Riverside Airport (KRAL) | Big Bear City Airport (KL35) | 2026-08-02 21:56 UTC | 2026-08-02 22:26 UTC | 30m |
| N508TJ |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-02 22:22 UTC | 2026-08-02 22:26 UTC | 3m |
| FTO501 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-02 22:00 UTC | 2026-08-02 22:26 UTC | 26m |
| XE1182 |  | Harry Reid International Airport (KLAS) | Santa Monica Municipal Airport (KSMO) | 2026-08-02 21:22 UTC | 2026-08-02 22:24 UTC | 1h 1m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-08-02 10:47 UTC | 2026-08-02 22:23 UTC | 11h 36m |
| N144AL |  | Mineral Wells Regional Airport (KMWL) | Big Bear City Airport (KL35) | 2026-08-02 19:55 UTC | 2026-08-02 22:22 UTC | 2h 26m |
| YGF | YGF | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-08-02 21:40 UTC | 2026-08-02 22:14 UTC | 33m |
| IHDOL | IHD | Bolzano Airport (LIPB) | Bolzano Airport (LIPB) | 2026-08-02 22:04 UTC | 2026-08-02 22:11 UTC | 6m |
| NTW14 | NTW | Patrick Leahy Burlington International Airport (KBTV) | Alpena County Regional Airport (KAPN) | 2026-08-02 20:51 UTC | 2026-08-02 22:09 UTC | 1h 17m |
| GTI8254 | GTI | Chicago O'Hare International Airport (KORD) | Valleyview Airport (CEL5) | 2026-08-02 18:49 UTC | 2026-08-02 22:09 UTC | 3h 20m |
| N5810F |  | Long Beach (Daugherty Field) Airport (KLGB) | NV44 (NV44) | 2026-08-02 21:11 UTC | 2026-08-02 22:09 UTC | 58m |
| NAY9901 | NAY | Gran Canaria Airport (GCLP) | Tenerife Norte Airport (GCXO) | 2026-08-02 21:50 UTC | 2026-08-02 22:08 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
