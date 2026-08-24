# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_18:50:55_UTC-green)

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

**Latest saved flight:** 2026-08-24 18:50:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 18:50:55 UTC

- **232,959** saved flights
- **71,597** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **232,959** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,807,716.6 tonnes** estimated CO2 emissions
- **162,766,178 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9353 |
| 2 | SkyWest Airlines | 8240 |
| 3 | EJA | 4519 |
| 4 | IndiGo | 3940 |
| 5 | American Airlines | 3800 |
| 6 | Southwest Airlines | 3587 |
| 7 | Delta Air Lines | 2973 |
| 8 | ENY | 2836 |
| 9 | LATAM Airlines | 2239 |
| 10 | AZU | 2169 |
| 11 | Vueling | 1991 |
| 12 | Lufthansa | 1900 |
| 13 | WIF | 1852 |
| 14 | LXJ | 1834 |
| 15 | easyJet | 1630 |
| 16 | Swiss International | 1561 |
| 17 | AXM | 1551 |
| 18 | EJU | 1492 |
| 19 | United Airlines | 1479 |
| 20 | QLK | 1474 |
| 21 | Alaska Airlines | 1399 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1297 |
| 24 | WMT | 1293 |
| 25 | VIV | 1280 |
| 26 | PGT | 1273 |
| 27 | Air France | 1266 |
| 28 | Wizz Air | 1230 |
| 29 | AEE | 1159 |
| 30 | JetBlue | 1159 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 193933 |
| 2 | 🇪🇸 ES | 14963 |
| 3 | 🇧🇷 BR | 13609 |
| 4 | 🇦🇺 AU | 13164 |
| 5 | 🇨🇦 CA | 12837 |
| 6 | 🇮🇹 IT | 12674 |
| 7 | 🇮🇳 IN | 12276 |
| 8 | 🇩🇪 DE | 11490 |
| 9 | 🇬🇧 GB | 10988 |
| 10 | 🇨🇴 CO | 9737 |
| 11 | 🇯🇵 JP | 9448 |
| 12 | 🇫🇷 FR | 9327 |
| 13 | 🇹🇷 TR | 6897 |
| 14 | 🇬🇷 GR | 6856 |
| 15 | 🇲🇽 MX | 6470 |
| 16 | 🇨🇭 CH | 6215 |
| 17 | 🇳🇴 NO | 5763 |
| 18 | 🇲🇾 MY | 4144 |
| 19 | 🇹🇭 TH | 4108 |
| 20 | 🇿🇦 ZA | 4071 |
| 21 | 🇵🇱 PL | 3881 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3185 |
| 24 | 🇬🇹 GT | 2923 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2681 |
| 27 | 🇲🇦 MA | 2367 |
| 28 | 🇲🇪 ME | 2147 |
| 29 | 🇳🇱 NL | 2089 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4846 |
| 2 | Denver International Airport |  | US | 3778 |
| 3 | Indira Gandhi International Airport |  | IN | 2841 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2671 |
| 6 | Harry Reid International Airport |  | US | 2503 |
| 7 | Zurich Airport |  | CH | 2435 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2380 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2339 |
| 10 | La Aurora Airport |  | GT | 2226 |
| 11 | El Dorado International Airport |  | CO | 2167 |
| 12 | Chicago O'Hare International Airport |  | US | 2106 |
| 13 | Salt Lake City International Airport |  | US | 2049 |
| 14 | Congonhas Airport |  | BR | 1984 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1965 |
| 16 | Frankfurt am Main International Airport |  | DE | 1860 |
| 17 | Capua Airport |  | IT | 1833 |
| 18 | Madrid Barajas International Airport |  | ES | 1830 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1752 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1726 |
| 21 | Malpensa International Airport |  | IT | 1671 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1662 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1619 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1534 |
| 27 | Charlotte/Douglas International Airport |  | US | 1510 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1471 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1425 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1408 |
| 32 | Viracopos International Airport |  | BR | 1387 |
| 33 | Bengaluru International Airport |  | IN | 1372 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1365 |
| 35 | Seattle-Tacoma International Airport |  | US | 1365 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1322 |
| 38 | Oslo Gardermoen Airport |  | NO | 1307 |
| 39 | O. R. Tambo International Airport |  | ZA | 1265 |
| 40 | Vitoria/Foronda Airport |  | ES | 1264 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1084 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 850 | 21m | 244 km | 3,579.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 579 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 520 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 384 | 27m | 275 km | 1,819.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 360 | 1h 50m | 1,423 km | 8,835.0 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 359 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 339 | 44m | 241 km | 1,408.1 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 308 | 24m | 218 km | 1,160.4 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 304 | 1h 38m | 1,156 km | 6,064.7 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 289 | 19m | 99 km | 495.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 285 | 27m | 215 km | 1,055.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 269 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 265 | 19m | 144 km | 659.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 251 | 15m | 154 km | 665.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 249 | 1h 50m | 1,304 km | 5,601.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KNIFE01 | KNI | Los Alamitos Army Air Field (KSLI) | Mc Conville Airstrip (CA42) | 2026-08-24 17:48 UTC | 2026-08-24 18:50 UTC | 1h 2m |
| N5872H |  | Homer Airport (PAHO) | Bradley Lake Hydroelectric Project Airstrip (0AK7) | 2026-08-24 18:31 UTC | 2026-08-24 18:49 UTC | 17m |
| G20905 |  | 7PS4 (7PS4) | Fairview Farm Airfield (PS20) | 2026-08-24 17:13 UTC | 2026-08-24 18:41 UTC | 1h 28m |
| N509SB |  | Vancouver International Airport (CYVR) | Boeing Field/King County International Airport (KBFI) | 2026-08-24 18:05 UTC | 2026-08-24 18:36 UTC | 31m |
| N642SP |  | Solberg/Hunterdon Airport (KN51) | Solberg/Hunterdon Airport (KN51) | 2026-08-24 17:33 UTC | 2026-08-24 18:35 UTC | 1h 2m |
| N7578G |  | John C Tune Airport (KJWN) | Springfield Robertson County Airport (KM91) | 2026-08-24 17:53 UTC | 2026-08-24 18:35 UTC | 42m |
| ES801 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-08-24 18:28 UTC | 2026-08-24 18:33 UTC | 5m |
| UAE954 | Emirates | Beirut Rafic Hariri International Airport (OLBA) | Dubai International Airport (OMDB) | 2026-08-24 15:57 UTC | 2026-08-24 18:33 UTC | 2h 35m |
| N831VF |  | Bend Municipal Airport (KBDN) | Goering Ranches / Chocheta Estates Airport (50OR) | 2026-08-24 17:34 UTC | 2026-08-24 18:29 UTC | 54m |
| N149GT |  | Rochester International Airport (KRST) | Brainerd Lakes Regional Airport (KBRD) | 2026-08-24 17:44 UTC | 2026-08-24 18:28 UTC | 44m |
| SWA278 | Southwest Airlines | Ontario International Airport (KONT) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-24 17:35 UTC | 2026-08-24 18:28 UTC | 53m |
| N715JR |  | Boeing Field/King County International Airport (KBFI) | Boeing Field/King County International Airport (KBFI) | 2026-08-24 18:12 UTC | 2026-08-24 18:21 UTC | 9m |
| N23581 |  | Gillespie Field (KSEE) | Ramona Airport (KRNM) | 2026-08-24 17:05 UTC | 2026-08-24 18:21 UTC | 1h 16m |
| DESERT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-24 18:08 UTC | 2026-08-24 18:21 UTC | 13m |
| UAL271 | United Airlines | Shannon Airport (EINN) | Newark Liberty International Airport (KEWR) | 2026-08-24 11:36 UTC | 2026-08-24 18:21 UTC | 6h 45m |
| AIZ363 | AIZ | Ben Gurion International Airport (LLBG) | Sofia Airport (LBSF) | 2026-08-24 16:17 UTC | 2026-08-24 18:20 UTC | 2h 3m |
| THY4YM | Turkish Airlines | Istanbul Hezarfen Airfield (LTBW) | HE42 (HE42) | 2026-08-24 16:41 UTC | 2026-08-24 18:18 UTC | 1h 37m |
| BOMR705 | BOM | Calhoun County Airport (KPKV) | Whatley Flying Service Airport (8TA1) | 2026-08-24 17:48 UTC | 2026-08-24 18:17 UTC | 28m |
| N465PA |  | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | Oxnard Airport (KOXR) | 2026-08-24 17:21 UTC | 2026-08-24 18:16 UTC | 55m |
| N5726B |  | Mariposa-Yosemite Airport (KMPI) | Mariposa-Yosemite Airport (KMPI) | 2026-08-24 17:51 UTC | 2026-08-24 18:14 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
