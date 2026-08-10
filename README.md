# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_12:20:31_UTC-green)

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

**Latest saved flight:** 2026-08-10 12:20:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 12:20:31 UTC

- **183,852** saved flights
- **58,563** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **183,852** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,210,157.2 tonnes** estimated CO2 emissions
- **128,125,057 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7296 |
| 2 | SkyWest Airlines | 6684 |
| 3 | EJA | 3629 |
| 4 | IndiGo | 3221 |
| 5 | Southwest Airlines | 2882 |
| 6 | American Airlines | 2868 |
| 7 | ENY | 2290 |
| 8 | Delta Air Lines | 2172 |
| 9 | LATAM Airlines | 1717 |
| 10 | AZU | 1648 |
| 11 | Lufthansa | 1625 |
| 12 | WIF | 1522 |
| 13 | Vueling | 1518 |
| 14 | LXJ | 1451 |
| 15 | easyJet | 1262 |
| 16 | Swiss International | 1262 |
| 17 | AXM | 1234 |
| 18 | QLK | 1135 |
| 19 | EJU | 1130 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1104 |
| 22 | VIV | 1013 |
| 23 | GLO | 985 |
| 24 | AEE | 957 |
| 25 | CXK | 954 |
| 26 | Air France | 953 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 941 |
| 29 | PGT | 937 |
| 30 | MXY | 915 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 157033 |
| 2 | 🇪🇸 ES | 11818 |
| 3 | 🇧🇷 BR | 10543 |
| 4 | 🇦🇺 AU | 10300 |
| 5 | 🇮🇳 IN | 10095 |
| 6 | 🇨🇦 CA | 9996 |
| 7 | 🇮🇹 IT | 9509 |
| 8 | 🇩🇪 DE | 9102 |
| 9 | 🇬🇧 GB | 8532 |
| 10 | 🇯🇵 JP | 7511 |
| 11 | 🇫🇷 FR | 7335 |
| 12 | 🇨🇴 CO | 6872 |
| 13 | 🇬🇷 GR | 5393 |
| 14 | 🇲🇽 MX | 5249 |
| 15 | 🇨🇭 CH | 4918 |
| 16 | 🇹🇷 TR | 4799 |
| 17 | 🇳🇴 NO | 4734 |
| 18 | 🇲🇾 MY | 3216 |
| 19 | 🇵🇱 PL | 3079 |
| 20 | 🇿🇦 ZA | 3075 |
| 21 | 🇹🇭 TH | 2851 |
| 22 | 🇳🇿 NZ | 2629 |
| 23 | 🇵🇭 PH | 2435 |
| 24 | 🇬🇹 GT | 2351 |
| 25 | 🇰🇷 KR | 2287 |
| 26 | 🇲🇦 MA | 1857 |
| 27 | 🇭🇷 HR | 1842 |
| 28 | 🇲🇪 ME | 1663 |
| 29 | 🇳🇱 NL | 1648 |
| 30 | 🇲🇴 MO | 1520 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3808 |
| 2 | Denver International Airport |  | US | 3036 |
| 3 | Tokyo International Airport |  | JP | 2329 |
| 4 | Indira Gandhi International Airport |  | IN | 2260 |
| 5 | Guaymaral Airport |  | CO | 2237 |
| 6 | Harry Reid International Airport |  | US | 2151 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1972 |
| 8 | Zurich Airport |  | CH | 1970 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1908 |
| 10 | La Aurora Airport |  | GT | 1804 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1673 |
| 12 | El Dorado International Airport |  | CO | 1647 |
| 13 | Salt Lake City International Airport |  | US | 1639 |
| 14 | Chicago O'Hare International Airport |  | US | 1637 |
| 15 | Frankfurt am Main International Airport |  | DE | 1589 |
| 16 | Congonhas Airport |  | BR | 1530 |
| 17 | Macau International Airport |  | MO | 1520 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1450 |
| 19 | Madrid Barajas International Airport |  | ES | 1446 |
| 20 | Capua Airport |  | IT | 1439 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1373 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1314 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1273 |
| 25 | Charles de Gaulle International Airport |  | FR | 1253 |
| 26 | Charlotte/Douglas International Airport |  | US | 1245 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1196 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1149 |
| 30 | Ninoy Aquino International Airport |  | PH | 1148 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1129 |
| 32 | Barcelona International Airport |  | ES | 1089 |
| 33 | Seattle-Tacoma International Airport |  | US | 1057 |
| 34 | Viracopos International Airport |  | BR | 1056 |
| 35 | Reno/Tahoe International Airport |  | US | 1049 |
| 36 | Daniel K Inouye International Airport |  | US | 1046 |
| 37 | Calgary International Airport |  | CA | 1046 |
| 38 | Oslo Gardermoen Airport |  | NO | 1022 |
| 39 | Tenerife Norte Airport |  | ES | 1004 |
| 40 | Vitoria/Foronda Airport |  | ES | 995 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 922 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 674 | 21m | 244 km | 2,838.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 444 | 1h 8m | 770 km | 5,898.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 427 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 309 | 27m | 275 km | 1,464.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 272 | 44m | 241 km | 1,129.8 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 260 | 1h 49m | 1,423 km | 6,380.8 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 255 | 8m | - | - |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 248 | 20m | 250 km | 1,071.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 231 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 226 | 19m | 99 km | 387.1 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 224 | 1h 15m | 961 km | 3,712.9 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 220 | 19m | 144 km | 547.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 217 | 1h 38m | 1,156 km | 4,329.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 216 | 24m | 218 km | 813.8 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 214 | 31m | 369 km | 1,362.2 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 201 | 1h 1m | 695 km | 2,409.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3712C |  | Hector International Airport (KFAR) | Winnipeg James Armstrong Richardson International Airport (CYWG) | 2026-08-10 11:46 UTC | 2026-08-10 12:20 UTC | 33m |
| N893AP |  | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-08-10 11:40 UTC | 2026-08-10 12:15 UTC | 34m |
| N72AC |  | Evansville Regional Airport (KEVV) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-08-10 11:02 UTC | 2026-08-10 12:11 UTC | 1h 8m |
| N8388Y |  | Sebastian Municipal Airport (KX26) | Sebastian Municipal Airport (KX26) | 2026-08-10 11:49 UTC | 2026-08-10 12:09 UTC | 19m |
| CXK620 | CXK | Morristown Municipal Airport (KMMU) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-10 10:38 UTC | 2026-08-10 12:03 UTC | 1h 25m |
| N13DQ |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-10 11:26 UTC | 2026-08-10 12:01 UTC | 34m |
| FTO381 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-10 11:31 UTC | 2026-08-10 12:01 UTC | 29m |
| FXC11 | FXC | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-08-10 11:20 UTC | 2026-08-10 12:00 UTC | 40m |
| N309EB |  | Brandywine Regional Airport (KOQN) | Brandywine Regional Airport (KOQN) | 2026-08-10 11:22 UTC | 2026-08-10 11:57 UTC | 35m |
| N622TP |  | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-08-10 11:20 UTC | 2026-08-10 11:54 UTC | 33m |
| N193AE |  | Coles County Memorial Airport (KMTO) | Frasca Field (KC16) | 2026-08-10 11:37 UTC | 2026-08-10 11:53 UTC | 16m |
| HBZWE | HBZ | Bern Belp Airport (LSZB) | Raron Airport (LSTA) | 2026-08-10 10:25 UTC | 2026-08-10 11:53 UTC | 1h 28m |
| N709PT |  | Oasis Ranger Station-U S Government Airport (9FL7) | Marco Island Executive Airport (KMKY) | 2026-08-10 11:27 UTC | 2026-08-10 11:51 UTC | 23m |
| N916SY |  | Scottsdale Airport (KSDL) | Sedona Airport (KSEZ) | 2026-08-10 11:21 UTC | 2026-08-10 11:49 UTC | 28m |
| N27BN |  | Pueblo Memorial Airport (KPUB) | Centennial Airport (KAPA) | 2026-08-10 11:27 UTC | 2026-08-10 11:49 UTC | 21m |
| YUAPR | YUA | Mollis Airport (LSZM) | Zurich Airport (LSZH) | 2026-08-10 11:29 UTC | 2026-08-10 11:45 UTC | 16m |
| FNA571 | FNA | Stykkishólmur Airport (BIST) | Reykjavik Airport (BIRK) | 2026-08-10 11:25 UTC | 2026-08-10 11:42 UTC | 17m |
| MME120 | MME | Thabazimbi Airport (FATI) | Tedderfield Air Park (FATA) | 2026-08-10 11:11 UTC | 2026-08-10 11:40 UTC | 29m |
| EZY21QW | easyJet | London Luton Airport (EGGW) | Madeira Airport (LPMA) | 2026-08-10 08:26 UTC | 2026-08-10 11:37 UTC | 3h 11m |
| PAV410 | PAV | Nice-Cote d'Azur Airport (LFMN) | Lausanne-la Blecherette Airport (LSGL) | 2026-08-10 10:43 UTC | 2026-08-10 11:34 UTC | 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
