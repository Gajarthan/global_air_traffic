# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_14:41:36_UTC-green)

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

**Latest saved flight:** 2026-08-11 14:41:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 14:41:36 UTC

- **186,899** saved flights
- **59,272** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **186,899** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,242,899.8 tonnes** estimated CO2 emissions
- **130,023,177 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7429 |
| 2 | SkyWest Airlines | 6787 |
| 3 | EJA | 3678 |
| 4 | IndiGo | 3265 |
| 5 | Southwest Airlines | 2926 |
| 6 | American Airlines | 2905 |
| 7 | ENY | 2320 |
| 8 | Delta Air Lines | 2196 |
| 9 | LATAM Airlines | 1750 |
| 10 | AZU | 1681 |
| 11 | Lufthansa | 1641 |
| 12 | WIF | 1547 |
| 13 | Vueling | 1543 |
| 14 | LXJ | 1461 |
| 15 | easyJet | 1285 |
| 16 | Swiss International | 1276 |
| 17 | AXM | 1247 |
| 18 | EJU | 1155 |
| 19 | QLK | 1154 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1117 |
| 22 | VIV | 1029 |
| 23 | GLO | 1000 |
| 24 | Air France | 971 |
| 25 | AEE | 967 |
| 26 | CXK | 961 |
| 27 | PGT | 958 |
| 28 | United Airlines | 953 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 926 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 159334 |
| 2 | 🇪🇸 ES | 12033 |
| 3 | 🇧🇷 BR | 10727 |
| 4 | 🇦🇺 AU | 10482 |
| 5 | 🇮🇳 IN | 10231 |
| 6 | 🇨🇦 CA | 10197 |
| 7 | 🇮🇹 IT | 9688 |
| 8 | 🇩🇪 DE | 9257 |
| 9 | 🇬🇧 GB | 8699 |
| 10 | 🇯🇵 JP | 7644 |
| 11 | 🇫🇷 FR | 7486 |
| 12 | 🇨🇴 CO | 7059 |
| 13 | 🇬🇷 GR | 5485 |
| 14 | 🇲🇽 MX | 5324 |
| 15 | 🇨🇭 CH | 5016 |
| 16 | 🇹🇷 TR | 4926 |
| 17 | 🇳🇴 NO | 4810 |
| 18 | 🇲🇾 MY | 3262 |
| 19 | 🇿🇦 ZA | 3146 |
| 20 | 🇵🇱 PL | 3105 |
| 21 | 🇹🇭 TH | 2892 |
| 22 | 🇳🇿 NZ | 2666 |
| 23 | 🇵🇭 PH | 2477 |
| 24 | 🇬🇹 GT | 2379 |
| 25 | 🇰🇷 KR | 2313 |
| 26 | 🇲🇦 MA | 1903 |
| 27 | 🇭🇷 HR | 1893 |
| 28 | 🇲🇪 ME | 1678 |
| 29 | 🇳🇱 NL | 1671 |
| 30 | 🇲🇴 MO | 1523 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3870 |
| 2 | Denver International Airport |  | US | 3071 |
| 3 | Tokyo International Airport |  | JP | 2364 |
| 4 | Indira Gandhi International Airport |  | IN | 2301 |
| 5 | Guaymaral Airport |  | CO | 2286 |
| 6 | Harry Reid International Airport |  | US | 2187 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1992 |
| 8 | Zurich Airport |  | CH | 1991 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1933 |
| 10 | La Aurora Airport |  | GT | 1826 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1696 |
| 12 | El Dorado International Airport |  | CO | 1676 |
| 13 | Salt Lake City International Airport |  | US | 1662 |
| 14 | Chicago O'Hare International Airport |  | US | 1653 |
| 15 | Frankfurt am Main International Airport |  | DE | 1609 |
| 16 | Congonhas Airport |  | BR | 1558 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1473 |
| 19 | Capua Airport |  | IT | 1459 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1455 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1391 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1339 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1307 |
| 24 | Malpensa International Airport |  | IT | 1290 |
| 25 | Charles de Gaulle International Airport |  | FR | 1277 |
| 26 | Charlotte/Douglas International Airport |  | US | 1257 |
| 27 | Kuala Lumpur International Airport |  | MY | 1221 |
| 28 | Bengaluru International Airport |  | IN | 1208 |
| 29 | Ninoy Aquino International Airport |  | PH | 1169 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1168 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1144 |
| 32 | Barcelona International Airport |  | ES | 1113 |
| 33 | Viracopos International Airport |  | BR | 1077 |
| 34 | Seattle-Tacoma International Airport |  | US | 1074 |
| 35 | Reno/Tahoe International Airport |  | US | 1073 |
| 36 | Calgary International Airport |  | CA | 1060 |
| 37 | Daniel K Inouye International Airport |  | US | 1057 |
| 38 | Oslo Gardermoen Airport |  | NO | 1045 |
| 39 | Tenerife Norte Airport |  | ES | 1024 |
| 40 | Vitoria/Foronda Airport |  | ES | 1012 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 942 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 685 | 21m | 244 km | 2,884.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 454 | 1h 7m | 770 km | 6,031.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 434 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 329 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 313 | 27m | 275 km | 1,483.2 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 303 | 14m | 114 km | 594.3 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 280 | 44m | 241 km | 1,163.1 t |
| 12 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 271 | 8m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 266 | 1h 49m | 1,423 km | 6,528.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 233 | 27m | 215 km | 862.9 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 233 | 13m | - | - |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 230 | 12m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 229 | 19m | 99 km | 392.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 228 | 1h 15m | 961 km | 3,779.2 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 228 | 50m | 556 km | 2,185.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 222 | 1h 38m | 1,156 km | 4,428.8 t |
| 26 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 219 | 24m | 218 km | 825.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N669FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-08-11 14:20 UTC | 2026-08-11 14:41 UTC | 21m |
| GAM901 | GAM | Celle Airport (ETHC) | Celle Airport (ETHC) | 2026-08-11 13:16 UTC | 2026-08-11 14:41 UTC | 1h 24m |
| N850FS |  | Page Field (KFMY) | La Belle Municipal Airport (KX14) | 2026-08-11 14:18 UTC | 2026-08-11 14:36 UTC | 17m |
| N269TD |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-08-11 14:11 UTC | 2026-08-11 14:36 UTC | 24m |
| FUSION31 | FUS | Dunbar Ranch Airport (0XS8) | Dunbar Ranch Airport (0XS8) | 2026-08-11 14:23 UTC | 2026-08-11 14:35 UTC | 11m |
| N75972 |  | Airlake Airport (KLVN) | Airlake Airport (KLVN) | 2026-08-11 13:57 UTC | 2026-08-11 14:33 UTC | 36m |
| CAP823 | CAP | Miami-Opa Locka Executive Airport (KOPF) | North Perry Airport (KHWO) | 2026-08-11 14:19 UTC | 2026-08-11 14:31 UTC | 11m |
| N5522X |  | Tulsa Riverside Airport (KRVS) | Gregg Airport (7OK1) | 2026-08-11 14:03 UTC | 2026-08-11 14:30 UTC | 27m |
| HB2194 |  | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-08-11 10:57 UTC | 2026-08-11 14:26 UTC | 3h 28m |
| CGDEQ | CGD | Brampton Airport (CNC3) | Brampton Airport (CNC3) | 2026-08-11 13:46 UTC | 2026-08-11 14:25 UTC | 38m |
| N779AM |  | Montgomery-Gibbs Executive Airport (KMYF) | Apple Valley Airport (KAPV) | 2026-08-11 13:58 UTC | 2026-08-11 14:22 UTC | 23m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-08-11 13:52 UTC | 2026-08-11 14:21 UTC | 29m |
| N91PR |  | St Paul Downtown Holman Field (KSTP) | Brookings Regional Airport (KBKX) | 2026-08-11 13:30 UTC | 2026-08-11 14:20 UTC | 49m |
| N261PJ |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-11 13:46 UTC | 2026-08-11 14:19 UTC | 32m |
| MSEXY | MSE | Ben Gurion International Airport (LLBG) | LLYO (LLYO) | 2026-08-11 13:48 UTC | 2026-08-11 14:18 UTC | 29m |
| N200WL |  | Plymouth Municipal Airport (KPYM) | Teterboro Airport (KTEB) | 2026-08-11 13:24 UTC | 2026-08-11 14:17 UTC | 53m |
| EPI243 | EPI | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-08-11 12:50 UTC | 2026-08-11 14:16 UTC | 1h 25m |
| TFHAH | TFH | Keflavik International Airport (BIKF) | Reykjavik Airport (BIRK) | 2026-08-11 14:05 UTC | 2026-08-11 14:16 UTC | 10m |
| AFL273 | AFL | Suvarnabhumi Airport (VTBS) | Bezymyanka Airfield (UWWG) | 2026-08-11 07:02 UTC | 2026-08-11 14:15 UTC | 7h 12m |
| EJU67AD | EJU | Amsterdam Airport Schiphol (EHAM) | La Gomera Airport (GCGM) | 2026-08-11 10:09 UTC | 2026-08-11 14:15 UTC | 4h 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
