# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_20:42:56_UTC-green)

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

**Latest saved flight:** 2026-08-10 20:42:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 20:42:56 UTC

- **185,175** saved flights
- **58,880** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **185,175** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,223,878.1 tonnes** estimated CO2 emissions
- **128,920,467 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7348 |
| 2 | SkyWest Airlines | 6739 |
| 3 | EJA | 3663 |
| 4 | IndiGo | 3237 |
| 5 | Southwest Airlines | 2904 |
| 6 | American Airlines | 2889 |
| 7 | ENY | 2307 |
| 8 | Delta Air Lines | 2180 |
| 9 | LATAM Airlines | 1731 |
| 10 | AZU | 1662 |
| 11 | Lufthansa | 1627 |
| 12 | WIF | 1532 |
| 13 | Vueling | 1528 |
| 14 | LXJ | 1456 |
| 15 | easyJet | 1270 |
| 16 | Swiss International | 1268 |
| 17 | AXM | 1235 |
| 18 | EJU | 1144 |
| 19 | QLK | 1135 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1107 |
| 22 | VIV | 1020 |
| 23 | GLO | 992 |
| 24 | AEE | 961 |
| 25 | Air France | 961 |
| 26 | CXK | 960 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 945 |
| 29 | PGT | 944 |
| 30 | MXY | 920 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 158285 |
| 2 | 🇪🇸 ES | 11902 |
| 3 | 🇧🇷 BR | 10631 |
| 4 | 🇦🇺 AU | 10306 |
| 5 | 🇮🇳 IN | 10141 |
| 6 | 🇨🇦 CA | 10098 |
| 7 | 🇮🇹 IT | 9575 |
| 8 | 🇩🇪 DE | 9147 |
| 9 | 🇬🇧 GB | 8596 |
| 10 | 🇯🇵 JP | 7511 |
| 11 | 🇫🇷 FR | 7403 |
| 12 | 🇨🇴 CO | 6980 |
| 13 | 🇬🇷 GR | 5430 |
| 14 | 🇲🇽 MX | 5285 |
| 15 | 🇨🇭 CH | 4946 |
| 16 | 🇹🇷 TR | 4853 |
| 17 | 🇳🇴 NO | 4760 |
| 18 | 🇲🇾 MY | 3221 |
| 19 | 🇿🇦 ZA | 3110 |
| 20 | 🇵🇱 PL | 3089 |
| 21 | 🇹🇭 TH | 2862 |
| 22 | 🇳🇿 NZ | 2631 |
| 23 | 🇵🇭 PH | 2441 |
| 24 | 🇬🇹 GT | 2371 |
| 25 | 🇰🇷 KR | 2287 |
| 26 | 🇲🇦 MA | 1875 |
| 27 | 🇭🇷 HR | 1863 |
| 28 | 🇲🇪 ME | 1668 |
| 29 | 🇳🇱 NL | 1657 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3839 |
| 2 | Denver International Airport |  | US | 3061 |
| 3 | Tokyo International Airport |  | JP | 2329 |
| 4 | Indira Gandhi International Airport |  | IN | 2274 |
| 5 | Guaymaral Airport |  | CO | 2271 |
| 6 | Harry Reid International Airport |  | US | 2164 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1982 |
| 8 | Zurich Airport |  | CH | 1978 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1921 |
| 10 | La Aurora Airport |  | GT | 1819 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1688 |
| 12 | El Dorado International Airport |  | CO | 1660 |
| 13 | Salt Lake City International Airport |  | US | 1650 |
| 14 | Chicago O'Hare International Airport |  | US | 1650 |
| 15 | Frankfurt am Main International Airport |  | DE | 1595 |
| 16 | Congonhas Airport |  | BR | 1545 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | Madrid Barajas International Airport |  | ES | 1458 |
| 19 | Capua Airport |  | IT | 1455 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1451 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1382 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1321 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1278 |
| 25 | Charles de Gaulle International Airport |  | FR | 1264 |
| 26 | Charlotte/Douglas International Airport |  | US | 1253 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1201 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1159 |
| 30 | Ninoy Aquino International Airport |  | PH | 1151 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1135 |
| 32 | Barcelona International Airport |  | ES | 1096 |
| 33 | Viracopos International Airport |  | BR | 1066 |
| 34 | Reno/Tahoe International Airport |  | US | 1064 |
| 35 | Seattle-Tacoma International Airport |  | US | 1061 |
| 36 | Calgary International Airport |  | CA | 1053 |
| 37 | Daniel K Inouye International Airport |  | US | 1051 |
| 38 | Oslo Gardermoen Airport |  | NO | 1032 |
| 39 | Tenerife Norte Airport |  | ES | 1010 |
| 40 | Vitoria/Foronda Airport |  | ES | 1004 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 936 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 679 | 21m | 244 km | 2,859.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 444 | 1h 8m | 770 km | 5,898.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 431 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 311 | 27m | 275 km | 1,473.7 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 277 | 44m | 241 km | 1,150.6 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 264 | 8m | - | - |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 262 | 1h 49m | 1,423 km | 6,429.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 249 | 20m | 250 km | 1,075.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 232 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 228 | 19m | 99 km | 390.5 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 227 | 1h 15m | 961 km | 3,762.6 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 226 | 12m | - | - |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 224 | 50m | 556 km | 2,147.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 219 | 1h 38m | 1,156 km | 4,369.0 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 218 | 24m | 218 km | 821.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 215 | 31m | 369 km | 1,368.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NIT264 | NIT | Perry-Houston County Airport (KPXE) | Perry-Houston County Airport (KPXE) | 2026-08-10 20:10 UTC | 2026-08-10 20:42 UTC | 32m |
| COBRA31 | COB | Mojave Air & Space Port/Rutan Field (KMHV) | Boron Airstrip (57CL) | 2026-08-10 20:28 UTC | 2026-08-10 20:41 UTC | 12m |
| N233S |  | Minden-Tahoe Airport (KMEV) | Dayton Valley Airpark (KA34) | 2026-08-10 19:07 UTC | 2026-08-10 20:37 UTC | 1h 30m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-10 20:13 UTC | 2026-08-10 20:26 UTC | 12m |
| N6097F |  | Scottsdale Airport (KSDL) | Phoenix Deer Valley Airport (KDVT) | 2026-08-10 19:38 UTC | 2026-08-10 20:19 UTC | 40m |
| N725CS |  | Dillant/Hopkins Airport (KEEN) | Laurence G Hanscom Field (KBED) | 2026-08-10 20:05 UTC | 2026-08-10 20:19 UTC | 13m |
| TKR210 | TKR | Casper/Natrona County International Airport (KCPR) | Allen H Tigert Airport (KU78) | 2026-08-10 19:25 UTC | 2026-08-10 20:17 UTC | 51m |
| BPX213 | BPX | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-08-10 19:54 UTC | 2026-08-10 20:14 UTC | 19m |
| N6885S |  | Charles M Schulz/Sonoma County Airport (KSTS) | Truckee-Tahoe Airport (KTRK) | 2026-08-10 19:38 UTC | 2026-08-10 20:12 UTC | 33m |
| FHY753 | FHY | Antalya International Airport (LTAI) | LBBZ (LBBZ) | 2026-08-10 19:02 UTC | 2026-08-10 20:11 UTC | 1h 8m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-10 19:59 UTC | 2026-08-10 20:10 UTC | 10m |
| N713DH |  | Shady International Airport (FA49) | James H Easom Field (KM23) | 2026-08-10 19:10 UTC | 2026-08-10 20:09 UTC | 59m |
| N121TS |  | Cincinnati Municipal/Lunken Field (KLUK) | Kalkaska City Airport (KY89) | 2026-08-10 19:03 UTC | 2026-08-10 20:08 UTC | 1h 5m |
| N910RW |  | Fazenda Royal Airport (SIVE) | Lencois Paulista Airport (SDLP) | 2026-08-10 19:51 UTC | 2026-08-10 20:08 UTC | 16m |
| N52654 |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-08-10 19:43 UTC | 2026-08-10 20:05 UTC | 21m |
| N182KQ |  | Renton Municipal Airport (KRNT) | Boeing Field/King County International Airport (KBFI) | 2026-08-10 19:54 UTC | 2026-08-10 20:05 UTC | 10m |
| N503JD |  | Aurora State Airport (KUAO) | Independence State Airport (K7S5) | 2026-08-10 19:39 UTC | 2026-08-10 20:04 UTC | 24m |
| EVAL04 | EVA Air | Big Sky Airport (AL93) | Redstone Army Air Field (KHUA) | 2026-08-10 19:50 UTC | 2026-08-10 20:04 UTC | 13m |
| MRS1437 | MRS | Rabat-Sale Airport (GMME) | Bassatine Airport (GMFM) | 2026-08-10 19:46 UTC | 2026-08-10 20:00 UTC | 13m |
| ZKTAS | ZKT | Ardmore Airport (NZAR) | Ardmore Airport (NZAR) | 2026-08-10 19:34 UTC | 2026-08-10 19:57 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
