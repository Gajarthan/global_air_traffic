# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_05:20:34_UTC-green)

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

**Latest saved flight:** 2026-07-06 05:20:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-06 05:20:34 UTC

- **130,641** saved flights
- **44,426** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **130,641** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,576,937.0 tonnes** estimated CO2 emissions
- **91,416,635 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5311 |
| 2 | SkyWest Airlines | 4842 |
| 3 | EJA | 2560 |
| 4 | IndiGo | 2446 |
| 5 | American Airlines | 2026 |
| 6 | Southwest Airlines | 1970 |
| 7 | ENY | 1644 |
| 8 | Delta Air Lines | 1568 |
| 9 | Lufthansa | 1368 |
| 10 | LATAM Airlines | 1196 |
| 11 | Vueling | 1154 |
| 12 | WIF | 1138 |
| 13 | AZU | 1112 |
| 14 | AXM | 1011 |
| 15 | LXJ | 1010 |
| 16 | Swiss International | 912 |
| 17 | All Nippon Airways | 861 |
| 18 | Alaska Airlines | 837 |
| 19 | easyJet | 837 |
| 20 | QLK | 819 |
| 21 | EJU | 805 |
| 22 | VIV | 723 |
| 23 | Cathay Pacific | 716 |
| 24 | AEE | 709 |
| 25 | Air France | 709 |
| 26 | CXK | 697 |
| 27 | United Airlines | 696 |
| 28 | JetBlue | 686 |
| 29 | MXY | 682 |
| 30 | GLO | 670 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 111941 |
| 2 | 🇪🇸 ES | 8695 |
| 3 | 🇮🇳 IN | 7664 |
| 4 | 🇦🇺 AU | 7551 |
| 5 | 🇧🇷 BR | 7360 |
| 6 | 🇨🇦 CA | 6896 |
| 7 | 🇩🇪 DE | 6850 |
| 8 | 🇮🇹 IT | 6823 |
| 9 | 🇬🇧 GB | 5804 |
| 10 | 🇯🇵 JP | 5636 |
| 11 | 🇫🇷 FR | 5187 |
| 12 | 🇨🇴 CO | 4102 |
| 13 | 🇲🇽 MX | 3818 |
| 14 | 🇬🇷 GR | 3727 |
| 15 | 🇳🇴 NO | 3538 |
| 16 | 🇨🇭 CH | 3352 |
| 17 | 🇹🇷 TR | 2887 |
| 18 | 🇲🇾 MY | 2620 |
| 19 | 🇿🇦 ZA | 2159 |
| 20 | 🇵🇱 PL | 2144 |
| 21 | 🇳🇿 NZ | 2082 |
| 22 | 🇹🇭 TH | 2026 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1815 |
| 25 | 🇬🇹 GT | 1779 |
| 26 | 🇲🇦 MA | 1394 |
| 27 | 🇲🇪 ME | 1295 |
| 28 | 🇳🇱 NL | 1226 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1144 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2731 |
| 2 | Denver International Airport |  | US | 2217 |
| 3 | Tokyo International Airport |  | JP | 1853 |
| 4 | Indira Gandhi International Airport |  | IN | 1691 |
| 5 | Harry Reid International Airport |  | US | 1627 |
| 6 | Guaymaral Airport |  | CO | 1587 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1541 |
| 8 | Zurich Airport |  | CH | 1440 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1393 |
| 10 | La Aurora Airport |  | GT | 1376 |
| 11 | Frankfurt am Main International Airport |  | DE | 1324 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1265 |
| 13 | Chicago O'Hare International Airport |  | US | 1257 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1163 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1113 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1073 |
| 19 | Madrid Barajas International Airport |  | ES | 1070 |
| 20 | Capua Airport |  | IT | 1070 |
| 21 | Congonhas Airport |  | BR | 1039 |
| 22 | Kuala Lumpur International Airport |  | MY | 1017 |
| 23 | Charlotte/Douglas International Airport |  | US | 974 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 952 |
| 25 | Charles de Gaulle International Airport |  | FR | 945 |
| 26 | Bengaluru International Airport |  | IN | 926 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 888 |
| 28 | Malpensa International Airport |  | IT | 878 |
| 29 | Ninoy Aquino International Airport |  | PH | 842 |
| 30 | Daniel K Inouye International Airport |  | US | 821 |
| 31 | Barcelona International Airport |  | ES | 809 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 796 |
| 33 | Tenerife Norte Airport |  | ES | 792 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 770 |
| 35 | Calgary International Airport |  | CA | 764 |
| 36 | Seattle-Tacoma International Airport |  | US | 754 |
| 37 | Viracopos International Airport |  | BR | 750 |
| 38 | Vitoria/Foronda Airport |  | ES | 750 |
| 39 | Scottsdale Airport |  | US | 747 |
| 40 | Amsterdam Airport Schiphol |  | NL | 742 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 666 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 474 | 21m | 244 km | 1,995.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 328 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 316 | 1h 10m | 770 km | 4,197.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 247 | 26m | 275 km | 1,170.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 240 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 190 | 22m | 55 km | 180.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 183 | 44m | 241 km | 760.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 174 | 27m | 152 km | 454.7 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 170 | 1h 45m | 1,423 km | 4,172.1 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 164 | 31m | 369 km | 1,043.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 160 | 20m | 250 km | 691.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 160 | 18m | 144 km | 398.0 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 157 | 30m | 49 km | 132.7 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 154 | 1h 1m | 695 km | 1,846.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 150 | 54m | 136 km | 351.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 148 | 1h 38m | 1,156 km | 2,952.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 146 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SWR12K | Swiss International | Václav Havel Airport (LKPR) | Zurich Airport (LSZH) | 2026-07-06 04:23 UTC | 2026-07-06 05:20 UTC | 56m |
| N374YJ |  | Yokota Air Base (RJTY) | Yokota Air Base (RJTY) | 2026-07-06 05:01 UTC | 2026-07-06 05:14 UTC | 12m |
| VTGRB | VTG | Shimla Airport (VISM) | Bharkot Airport (VI82) | 2026-07-06 04:21 UTC | 2026-07-06 05:12 UTC | 50m |
| GFA502 | Gulf Air | Bahrain International Airport (OBBI) | Sirri Island Airport (OIBS) | 2026-07-06 04:38 UTC | 2026-07-06 05:11 UTC | 32m |
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-07-05 14:19 UTC | 2026-07-06 05:08 UTC | 14h 49m |
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-07-05 17:49 UTC | 2026-07-06 05:06 UTC | 11h 17m |
| N853MB |  | Vance Brand Airport (KLMO) | Tall Timber Airport (CD28) | 2026-07-06 04:42 UTC | 2026-07-06 05:04 UTC | 22m |
| UAL2248 | United Airlines | San Francisco International Airport (KSFO) | Chicago O'Hare International Airport (KORD) | 2026-07-05 23:08 UTC | 2026-07-06 04:53 UTC | 5h 44m |
| N6382D |  | Modesto City-County-Harry Sham Field (KMOD) | Meadows Field (KBFL) | 2026-07-06 03:00 UTC | 2026-07-06 04:51 UTC | 1h 51m |
| AYT101 | AYT | Hatzor Air Base (LLHS) | Mitzpe Ramon Airfield (LLMR) | 2026-07-06 04:29 UTC | 2026-07-06 04:45 UTC | 16m |
| JBU860 | JetBlue | Sandy Point Airport (MYAS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-06 01:44 UTC | 2026-07-06 04:44 UTC | 2h 59m |
| KLM878 | KLM Royal Dutch | Juhu Aerodrome (VAJJ) | Frydlant Airport (LKFR) | 2026-07-05 21:40 UTC | 2026-07-06 04:39 UTC | 6h 59m |
| KAI | KAI | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-07-06 03:42 UTC | 2026-07-06 04:36 UTC | 54m |
| XCN81 | XCN | Ogden-Hinckley Airport (KOGD) | Aztec Municipal Airport (KN19) | 2026-07-06 02:26 UTC | 2026-07-06 04:35 UTC | 2h 8m |
| LND913 | LND | San Carlos Airport (KSQL) | Santa Monica Municipal Airport (KSMO) | 2026-07-06 03:19 UTC | 2026-07-06 04:34 UTC | 1h 14m |
| N874SP |  | Ted Stevens Anchorage International Airport (PANC) | Sparrevohn Lrrs Airport (PASV) | 2026-07-06 04:03 UTC | 2026-07-06 04:34 UTC | 30m |
| SWR2069 | Swiss International | Francisco de Sá Carneiro Airport (LPPR) | Zurich Airport (LSZH) | 2026-07-06 02:16 UTC | 2026-07-06 04:34 UTC | 2h 18m |
| FD536 |  | Adelaide International Airport (YPAD) | Hubert Wilkins Airstrip (YJST) | 2026-07-06 04:05 UTC | 2026-07-06 04:33 UTC | 27m |
| ZHJ | ZHJ | Bacchus Marsh Airport (YBSS) | Melbourne Moorabbin Airport (YMMB) | 2026-07-06 04:08 UTC | 2026-07-06 04:32 UTC | 23m |
|  |  | Photharam Airport (VTPR) | Photharam Airport (VTPR) | 2026-07-06 04:29 UTC | 2026-07-06 04:29 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
