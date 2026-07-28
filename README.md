# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_18:22:50_UTC-green)

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

**Latest saved flight:** 2026-07-28 18:22:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-28 18:22:50 UTC

- **156,944** saved flights
- **52,113** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **156,944** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,882,228.5 tonnes** estimated CO2 emissions
- **109,114,697 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6316 |
| 2 | SkyWest Airlines | 5737 |
| 3 | EJA | 3108 |
| 4 | IndiGo | 2775 |
| 5 | American Airlines | 2499 |
| 6 | Southwest Airlines | 2465 |
| 7 | ENY | 1962 |
| 8 | Delta Air Lines | 1865 |
| 9 | Lufthansa | 1507 |
| 10 | LATAM Airlines | 1462 |
| 11 | AZU | 1372 |
| 12 | WIF | 1326 |
| 13 | Vueling | 1317 |
| 14 | LXJ | 1208 |
| 15 | AXM | 1102 |
| 16 | Swiss International | 1090 |
| 17 | easyJet | 1024 |
| 18 | Alaska Airlines | 981 |
| 19 | All Nippon Airways | 973 |
| 20 | QLK | 972 |
| 21 | EJU | 961 |
| 22 | VIV | 861 |
| 23 | United Airlines | 837 |
| 24 | CXK | 832 |
| 25 | GLO | 823 |
| 26 | AEE | 822 |
| 27 | Cathay Pacific | 818 |
| 28 | MXY | 817 |
| 29 | Air France | 816 |
| 30 | JetBlue | 815 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 135418 |
| 2 | 🇪🇸 ES | 10120 |
| 3 | 🇧🇷 BR | 8941 |
| 4 | 🇦🇺 AU | 8857 |
| 5 | 🇮🇳 IN | 8726 |
| 6 | 🇨🇦 CA | 8468 |
| 7 | 🇮🇹 IT | 8098 |
| 8 | 🇩🇪 DE | 7966 |
| 9 | 🇬🇧 GB | 7215 |
| 10 | 🇯🇵 JP | 6420 |
| 11 | 🇫🇷 FR | 6215 |
| 12 | 🇨🇴 CO | 5486 |
| 13 | 🇲🇽 MX | 4498 |
| 14 | 🇬🇷 GR | 4471 |
| 15 | 🇳🇴 NO | 4153 |
| 16 | 🇨🇭 CH | 4113 |
| 17 | 🇹🇷 TR | 3748 |
| 18 | 🇲🇾 MY | 2871 |
| 19 | 🇵🇱 PL | 2680 |
| 20 | 🇿🇦 ZA | 2546 |
| 21 | 🇳🇿 NZ | 2329 |
| 22 | 🇹🇭 TH | 2261 |
| 23 | 🇰🇷 KR | 2091 |
| 24 | 🇵🇭 PH | 2066 |
| 25 | 🇬🇹 GT | 2018 |
| 26 | 🇲🇦 MA | 1602 |
| 27 | 🇲🇪 ME | 1515 |
| 28 | 🇭🇷 HR | 1446 |
| 29 | 🇳🇱 NL | 1434 |
| 30 | 🇲🇴 MO | 1292 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3225 |
| 2 | Denver International Airport |  | US | 2631 |
| 3 | Tokyo International Airport |  | JP | 2035 |
| 4 | Guaymaral Airport |  | CO | 1972 |
| 5 | Indira Gandhi International Airport |  | IN | 1941 |
| 6 | Harry Reid International Airport |  | US | 1920 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1737 |
| 8 | Zurich Airport |  | CH | 1691 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1643 |
| 10 | La Aurora Airport |  | GT | 1565 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1464 |
| 12 | Frankfurt am Main International Airport |  | DE | 1457 |
| 13 | Chicago O'Hare International Airport |  | US | 1428 |
| 14 | El Dorado International Airport |  | CO | 1422 |
| 15 | Salt Lake City International Airport |  | US | 1412 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1321 |
| 17 | Macau International Airport |  | MO | 1292 |
| 18 | Congonhas Airport |  | BR | 1285 |
| 19 | Madrid Barajas International Airport |  | ES | 1246 |
| 20 | Capua Airport |  | IT | 1231 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1204 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1124 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1114 |
| 24 | Charlotte/Douglas International Airport |  | US | 1111 |
| 25 | Kuala Lumpur International Airport |  | MY | 1099 |
| 26 | Charles de Gaulle International Airport |  | FR | 1077 |
| 27 | Bengaluru International Airport |  | IN | 1037 |
| 28 | Malpensa International Airport |  | IT | 1031 |
| 29 | Ninoy Aquino International Airport |  | PH | 968 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 953 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 946 |
| 32 | Barcelona International Airport |  | ES | 937 |
| 33 | Daniel K Inouye International Airport |  | US | 926 |
| 34 | Seattle-Tacoma International Airport |  | US | 914 |
| 35 | Calgary International Airport |  | CA | 899 |
| 36 | Tenerife Norte Airport |  | ES | 893 |
| 37 | Viracopos International Airport |  | BR | 889 |
| 38 | Scottsdale Airport |  | US | 889 |
| 39 | Oslo Gardermoen Airport |  | NO | 868 |
| 40 | Amsterdam Airport Schiphol |  | NL | 865 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 828 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 565 | 21m | 244 km | 2,379.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 376 | 24m | 225 km | 1,458.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 376 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 361 | 1h 9m | 770 km | 4,795.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 288 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 277 | 27m | 275 km | 1,312.6 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 219 | 44m | 241 km | 909.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 213 | 1h 47m | 1,423 km | 5,227.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 206 | 26m | 215 km | 762.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 201 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 199 | 20m | 250 km | 859.6 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 186 | 18m | 144 km | 462.7 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 185 | 1h 15m | 961 km | 3,066.5 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 182 | 31m | 369 km | 1,158.5 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 181 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 177 | 50m | 556 km | 1,696.7 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 176 | 1h 39m | 1,156 km | 3,511.1 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 176 | 44m | 452 km | 1,371.7 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 174 | 1h 1m | 695 km | 2,085.7 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 50m | 1,304 km | 3,712.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JBU223 | JetBlue | John F Kennedy International Airport (KJFK) | San Gabriel Valley Airport (KEMT) | 2026-07-28 13:03 UTC | 2026-07-28 18:22 UTC | 5h 19m |
| CXK1041 | CXK | Page Field (KFMY) | Page Field (KFMY) | 2026-07-28 17:44 UTC | 2026-07-28 18:22 UTC | 37m |
| THY6350 | Turkish Airlines | Istanbul Airport (LTFM) | Zhuhai Airport (ZGSD) | 2026-07-28 04:49 UTC | 2026-07-28 18:18 UTC | 13h 29m |
| N777ZA |  | Essex County Airport (KCDW) | Newark Liberty International Airport (KEWR) | 2026-07-28 17:14 UTC | 2026-07-28 18:17 UTC | 1h 3m |
| MSC806 | MSC | Malpensa International Airport (LIMC) | Giza Embaba Airport (HEEM) | 2026-07-28 14:58 UTC | 2026-07-28 18:15 UTC | 3h 17m |
| 7TVIV |  | Mostaganem Airport (DA14) | Mostaganem Airport (DA14) | 2026-07-28 17:59 UTC | 2026-07-28 18:14 UTC | 14m |
| EVATRN7 | EVA Air | Taiwan Taoyuan International Airport (RCTP) | Taiwan Taoyuan International Airport (RCTP) | 2026-07-28 17:54 UTC | 2026-07-28 18:13 UTC | 18m |
| WIF9PM | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-07-28 17:11 UTC | 2026-07-28 18:03 UTC | 52m |
| N627KL |  | Mt Pleasant Regional-Faison Field (KLRO) | Laurel Hill Farms Airport (2SC7) | 2026-07-28 17:59 UTC | 2026-07-28 18:02 UTC | 3m |
| N407RW |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-07-28 16:53 UTC | 2026-07-28 18:01 UTC | 1h 8m |
| DRAG153 | DRA | Alzate Brianza Airport (LILB) | Malpensa International Airport (LIMC) | 2026-07-28 17:51 UTC | 2026-07-28 18:01 UTC | 10m |
| N97CJ |  | Oakland County International Airport (KPTK) | Lakes Of The North Airport (K4Y4) | 2026-07-28 17:30 UTC | 2026-07-28 18:01 UTC | 30m |
| N619HW |  | Biplane Ranch Airport (NM02) | Payson Airport (KPAN) | 2026-07-28 16:10 UTC | 2026-07-28 18:00 UTC | 1h 50m |
| N307SH |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-07-28 17:28 UTC | 2026-07-28 17:56 UTC | 27m |
| N4047Q |  | Johnstone Point Airport (2AK5) | Chenega Bay Airport (PFCB) | 2026-07-28 17:13 UTC | 2026-07-28 17:56 UTC | 42m |
| N485G |  | Peace And Plenty Farm Airport (VA92) | Tangier Island Airport (KTGI) | 2026-07-28 16:49 UTC | 2026-07-28 17:55 UTC | 1h 5m |
| N4203P |  | Roberts Field (KRDM) | OG05 (OG05) | 2026-07-28 17:32 UTC | 2026-07-28 17:55 UTC | 23m |
| DAWG1 | DAW | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-07-28 17:28 UTC | 2026-07-28 17:52 UTC | 23m |
| N998AK |  | Merrill Field (PAMR) | Big Creek Airport (AK51) | 2026-07-28 17:09 UTC | 2026-07-28 17:51 UTC | 41m |
| WIF1VR | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-07-28 17:08 UTC | 2026-07-28 17:51 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
