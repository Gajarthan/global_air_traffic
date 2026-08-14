# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_09:09:38_UTC-green)

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

**Latest saved flight:** 2026-08-14 09:09:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 09:09:38 UTC

- **194,774** saved flights
- **61,297** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **194,774** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,327,600.8 tonnes** estimated CO2 emissions
- **134,933,382 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7749 |
| 2 | SkyWest Airlines | 7016 |
| 3 | EJA | 3835 |
| 4 | IndiGo | 3355 |
| 5 | Southwest Airlines | 3031 |
| 6 | American Airlines | 3015 |
| 7 | ENY | 2410 |
| 8 | Delta Air Lines | 2298 |
| 9 | LATAM Airlines | 1825 |
| 10 | AZU | 1752 |
| 11 | Lufthansa | 1683 |
| 12 | Vueling | 1623 |
| 13 | WIF | 1610 |
| 14 | LXJ | 1542 |
| 15 | easyJet | 1343 |
| 16 | Swiss International | 1319 |
| 17 | AXM | 1267 |
| 18 | QLK | 1205 |
| 19 | EJU | 1204 |
| 20 | All Nippon Airways | 1181 |
| 21 | Alaska Airlines | 1158 |
| 22 | VIV | 1071 |
| 23 | GLO | 1047 |
| 24 | Air France | 1018 |
| 25 | PGT | 1013 |
| 26 | AEE | 1001 |
| 27 | United Airlines | 994 |
| 28 | CXK | 989 |
| 29 | WMT | 971 |
| 30 | Wizz Air | 963 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 165702 |
| 2 | 🇪🇸 ES | 12573 |
| 3 | 🇧🇷 BR | 11179 |
| 4 | 🇦🇺 AU | 10995 |
| 5 | 🇨🇦 CA | 10657 |
| 6 | 🇮🇳 IN | 10508 |
| 7 | 🇮🇹 IT | 10131 |
| 8 | 🇩🇪 DE | 9657 |
| 9 | 🇬🇧 GB | 9134 |
| 10 | 🇯🇵 JP | 7941 |
| 11 | 🇫🇷 FR | 7771 |
| 12 | 🇨🇴 CO | 7569 |
| 13 | 🇬🇷 GR | 5714 |
| 14 | 🇲🇽 MX | 5510 |
| 15 | 🇹🇷 TR | 5267 |
| 16 | 🇨🇭 CH | 5255 |
| 17 | 🇳🇴 NO | 4991 |
| 18 | 🇲🇾 MY | 3318 |
| 19 | 🇿🇦 ZA | 3274 |
| 20 | 🇵🇱 PL | 3200 |
| 21 | 🇹🇭 TH | 3022 |
| 22 | 🇳🇿 NZ | 2739 |
| 23 | 🇵🇭 PH | 2578 |
| 24 | 🇬🇹 GT | 2468 |
| 25 | 🇰🇷 KR | 2374 |
| 26 | 🇭🇷 HR | 2021 |
| 27 | 🇲🇦 MA | 1975 |
| 28 | 🇳🇱 NL | 1754 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1568 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4053 |
| 2 | Denver International Airport |  | US | 3183 |
| 3 | Tokyo International Airport |  | JP | 2439 |
| 4 | Guaymaral Airport |  | CO | 2412 |
| 5 | Indira Gandhi International Airport |  | IN | 2371 |
| 6 | Harry Reid International Airport |  | US | 2252 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2061 |
| 8 | Zurich Airport |  | CH | 2060 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2016 |
| 10 | La Aurora Airport |  | GT | 1898 |
| 11 | El Dorado International Airport |  | CO | 1774 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1746 |
| 13 | Salt Lake City International Airport |  | US | 1734 |
| 14 | Chicago O'Hare International Airport |  | US | 1702 |
| 15 | Frankfurt am Main International Airport |  | DE | 1648 |
| 16 | Congonhas Airport |  | BR | 1627 |
| 17 | Madrid Barajas International Airport |  | ES | 1532 |
| 18 | Macau International Airport |  | MO | 1529 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1493 |
| 20 | Capua Airport |  | IT | 1493 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1437 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1397 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1362 |
| 24 | Malpensa International Airport |  | IT | 1348 |
| 25 | Charles de Gaulle International Airport |  | FR | 1333 |
| 26 | Charlotte/Douglas International Airport |  | US | 1291 |
| 27 | Bengaluru International Airport |  | IN | 1239 |
| 28 | Kuala Lumpur International Airport |  | MY | 1235 |
| 29 | Ninoy Aquino International Airport |  | PH | 1218 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1215 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1197 |
| 32 | Barcelona International Airport |  | ES | 1169 |
| 33 | Viracopos International Airport |  | BR | 1128 |
| 34 | Seattle-Tacoma International Airport |  | US | 1121 |
| 35 | Calgary International Airport |  | CA | 1111 |
| 36 | Reno/Tahoe International Airport |  | US | 1104 |
| 37 | Oslo Gardermoen Airport |  | NO | 1098 |
| 38 | Daniel K Inouye International Airport |  | US | 1086 |
| 39 | Tenerife Norte Airport |  | ES | 1067 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1064 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 996 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 714 | 21m | 244 km | 3,006.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 471 | 1h 7m | 770 km | 6,256.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 455 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 453 | 24m | 225 km | 1,757.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 327 | 27m | 275 km | 1,549.5 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 321 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 291 | 44m | 241 km | 1,208.8 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 279 | 1h 49m | 1,423 km | 6,847.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 277 | 22m | 55 km | 263.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 260 | 21m | 250 km | 1,123.0 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 242 | 27m | 215 km | 896.3 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 239 | 24m | 218 km | 900.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 237 | 1h 15m | 961 km | 3,928.4 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 229 | 1h 38m | 1,156 km | 4,568.5 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 229 | 19m | 144 km | 569.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 221 | 31m | 369 km | 1,406.7 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 212 | 28m | 152 km | 554.0 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 211 | 1h 3m | 695 km | 2,529.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GCPSS | GCP | Netheravon Airfield (EGDN) | Netheravon Airfield (EGDN) | 2026-08-14 08:42 UTC | 2026-08-14 09:09 UTC | 27m |
| FR139 |  | Al Ain International Airport (OMAL) | Al Ain International Airport (OMAL) | 2026-08-14 08:18 UTC | 2026-08-14 09:08 UTC | 50m |
| EFC28D | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-14 08:50 UTC | 2026-08-14 09:00 UTC | 10m |
| KEQ | KEQ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-08-14 08:15 UTC | 2026-08-14 08:55 UTC | 39m |
| GBYHJ | GBY | White Waltham Airfield (EGLM) | Isle of Wight / Sandown Airport (EGHN) | 2026-08-14 08:18 UTC | 2026-08-14 08:54 UTC | 36m |
| LNPFG | LNP | Kjeller Airport (ENKJ) | Kristiansand Airport (ENCN) | 2026-08-14 07:07 UTC | 2026-08-14 08:54 UTC | 1h 46m |
| UIT61E | UIT | Bardufoss Airport (ENDU) | Bardufoss Airport (ENDU) | 2026-08-14 07:54 UTC | 2026-08-14 08:49 UTC | 55m |
| EAI51C | EAI | Edinburgh Airport (EGPH) | Dublin Airport (EIDW) | 2026-08-14 07:49 UTC | 2026-08-14 08:46 UTC | 57m |
| NOZ30BF | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Bardufoss Airport (ENDU) | 2026-08-14 07:18 UTC | 2026-08-14 08:44 UTC | 1h 25m |
| OKAGE | OKA | Nymburk Ul Ploch Airport (LKNY) | Václav Havel Airport (LKPR) | 2026-08-14 08:25 UTC | 2026-08-14 08:42 UTC | 17m |
| RYR8607 | Ryanair | Valencia Airport (LEVC) | Frankfurt-Hahn Airport (EDFH) | 2026-08-14 06:44 UTC | 2026-08-14 08:42 UTC | 1h 57m |
| OKDSV | OKD | Hradec Kralove Airport (LKHK) | Ostrava Leos Janacek Airport (LKMT) | 2026-08-14 07:41 UTC | 2026-08-14 08:40 UTC | 59m |
| AFR57GA | Air France | Charles de Gaulle International Airport (LFPG) | Malpensa International Airport (LIMC) | 2026-08-14 07:37 UTC | 2026-08-14 08:40 UTC | 1h 2m |
| HBZVQ | HBZ | Meiringen Airport (LSMM) | Raron Airport (LSTA) | 2026-08-14 08:33 UTC | 2026-08-14 08:40 UTC | 7m |
| GEIMS | GEI | Chichester/Goodwood Airport (EGHR) | Bembridge Airport (EGHJ) | 2026-08-14 08:28 UTC | 2026-08-14 08:39 UTC | 11m |
| JAL3337 | Japan Airlines | Fukuoka Airport (RJFF) | Kumamoto Airport (RJFT) | 2026-08-14 08:27 UTC | 2026-08-14 08:38 UTC | 10m |
| HBZWE | HBZ | Bern Belp Airport (LSZB) | Reichenbach Air Base (LSGR) | 2026-08-14 07:57 UTC | 2026-08-14 08:36 UTC | 39m |
| SFU55 | SFU | RNAS Lee-On-Solent (EGHF) | Isle of Wight / Sandown Airport (EGHN) | 2026-08-14 08:04 UTC | 2026-08-14 08:32 UTC | 27m |
| HBXVS | HBX | Triengen Airport (LSPN) | Langenthal Airport (LSPL) | 2026-08-14 08:02 UTC | 2026-08-14 08:31 UTC | 29m |
| JST952 | JST | Sydney Kingsford Smith International Airport (YSSY) | Melbourne International Airport (YMML) | 2026-08-14 01:06 UTC | 2026-08-14 08:31 UTC | 7h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
