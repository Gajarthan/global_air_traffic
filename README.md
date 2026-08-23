# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_21:03:53_UTC-green)

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

**Latest saved flight:** 2026-08-23 21:03:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 21:03:53 UTC

- **230,156** saved flights
- **71,055** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **230,156** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,775,998.1 tonnes** estimated CO2 emissions
- **160,927,425 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9244 |
| 2 | SkyWest Airlines | 8170 |
| 3 | EJA | 4450 |
| 4 | IndiGo | 3882 |
| 5 | American Airlines | 3774 |
| 6 | Southwest Airlines | 3559 |
| 7 | Delta Air Lines | 2945 |
| 8 | ENY | 2807 |
| 9 | LATAM Airlines | 2213 |
| 10 | AZU | 2139 |
| 11 | Vueling | 1958 |
| 12 | Lufthansa | 1874 |
| 13 | LXJ | 1816 |
| 14 | WIF | 1812 |
| 15 | easyJet | 1606 |
| 16 | Swiss International | 1538 |
| 17 | AXM | 1520 |
| 18 | EJU | 1467 |
| 19 | United Airlines | 1461 |
| 20 | QLK | 1448 |
| 21 | Alaska Airlines | 1387 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1284 |
| 24 | VIV | 1263 |
| 25 | WMT | 1261 |
| 26 | PGT | 1258 |
| 27 | Air France | 1253 |
| 28 | Wizz Air | 1212 |
| 29 | JetBlue | 1148 |
| 30 | AEE | 1147 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 192130 |
| 2 | 🇪🇸 ES | 14776 |
| 3 | 🇧🇷 BR | 13464 |
| 4 | 🇦🇺 AU | 12964 |
| 5 | 🇨🇦 CA | 12703 |
| 6 | 🇮🇹 IT | 12463 |
| 7 | 🇮🇳 IN | 12101 |
| 8 | 🇩🇪 DE | 11326 |
| 9 | 🇬🇧 GB | 10836 |
| 10 | 🇨🇴 CO | 9535 |
| 11 | 🇯🇵 JP | 9314 |
| 12 | 🇫🇷 FR | 9218 |
| 13 | 🇹🇷 TR | 6799 |
| 14 | 🇬🇷 GR | 6769 |
| 15 | 🇲🇽 MX | 6403 |
| 16 | 🇨🇭 CH | 6116 |
| 17 | 🇳🇴 NO | 5656 |
| 18 | 🇲🇾 MY | 4063 |
| 19 | 🇿🇦 ZA | 4015 |
| 20 | 🇹🇭 TH | 3997 |
| 21 | 🇵🇱 PL | 3827 |
| 22 | 🇳🇿 NZ | 3173 |
| 23 | 🇵🇭 PH | 3146 |
| 24 | 🇬🇹 GT | 2900 |
| 25 | 🇰🇷 KR | 2706 |
| 26 | 🇭🇷 HR | 2636 |
| 27 | 🇲🇦 MA | 2334 |
| 28 | 🇲🇪 ME | 2110 |
| 29 | 🇳🇱 NL | 2059 |
| 30 | 🇮🇩 ID | 1978 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4807 |
| 2 | Denver International Airport |  | US | 3749 |
| 3 | Indira Gandhi International Airport |  | IN | 2800 |
| 4 | Tokyo International Airport |  | JP | 2781 |
| 5 | Guaymaral Airport |  | CO | 2654 |
| 6 | Harry Reid International Airport |  | US | 2485 |
| 7 | Zurich Airport |  | CH | 2403 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2354 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2318 |
| 10 | La Aurora Airport |  | GT | 2210 |
| 11 | El Dorado International Airport |  | CO | 2121 |
| 12 | Chicago O'Hare International Airport |  | US | 2085 |
| 13 | Salt Lake City International Airport |  | US | 2028 |
| 14 | Congonhas Airport |  | BR | 1965 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1948 |
| 16 | Frankfurt am Main International Airport |  | DE | 1842 |
| 17 | Madrid Barajas International Airport |  | ES | 1806 |
| 18 | Capua Airport |  | IT | 1806 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1726 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1711 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1653 |
| 22 | Malpensa International Airport |  | IT | 1644 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Charles de Gaulle International Airport |  | FR | 1598 |
| 25 | Macau International Airport |  | MO | 1597 |
| 26 | Ninoy Aquino International Airport |  | PH | 1510 |
| 27 | Charlotte/Douglas International Airport |  | US | 1504 |
| 28 | Kuala Lumpur International Airport |  | MY | 1472 |
| 29 | Barcelona International Airport |  | ES | 1442 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1397 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1381 |
| 32 | Viracopos International Airport |  | BR | 1369 |
| 33 | Bengaluru International Airport |  | IN | 1358 |
| 34 | Seattle-Tacoma International Airport |  | US | 1356 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1350 |
| 36 | Don Mueang International Airport |  | TH | 1307 |
| 37 | Calgary International Airport |  | CA | 1306 |
| 38 | Oslo Gardermoen Airport |  | NO | 1283 |
| 39 | Vitoria/Foronda Airport |  | ES | 1252 |
| 40 | O. R. Tambo International Airport |  | ZA | 1250 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 835 | 21m | 244 km | 3,516.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 575 | 1h 6m | 770 km | 7,638.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 560 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 517 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 380 | 27m | 275 km | 1,800.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 353 | 1h 50m | 1,423 km | 8,663.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 334 | 44m | 241 km | 1,387.4 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 325 | 21m | 250 km | 1,403.8 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 310 | 44m | 555 km | 2,968.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 306 | 22m | 55 km | 290.8 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 298 | 24m | 218 km | 1,122.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 297 | 1h 38m | 1,156 km | 5,925.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 280 | 27m | 215 km | 1,037.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 270 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 269 | 1h 14m | 961 km | 4,458.8 t |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 264 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 262 | 19m | 144 km | 651.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 244 | 28m | 152 km | 637.7 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK1115 | CXK | Long Island Mac Arthur Airport (KISP) | Long Island Mac Arthur Airport (KISP) | 2026-08-23 20:10 UTC | 2026-08-23 21:03 UTC | 53m |
| FTO501 | FTO | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-23 20:21 UTC | 2026-08-23 21:03 UTC | 42m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-23 20:43 UTC | 2026-08-23 21:00 UTC | 16m |
| N10TR |  | Dallas Love Field (KDAL) | Easterwood Field (KCLL) | 2026-08-23 20:29 UTC | 2026-08-23 20:59 UTC | 29m |
|  |  | Mid-Carolina Regional Airport (KRUQ) | Mid-Carolina Regional Airport (KRUQ) | 2026-08-23 20:56 UTC | 2026-08-23 20:56 UTC | 0m |
| N62494 |  | Portland-Hillsboro Airport (KHIO) | Nelson Ranch Airport (19OR) | 2026-08-23 20:01 UTC | 2026-08-23 20:48 UTC | 47m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-23 20:39 UTC | 2026-08-23 20:46 UTC | 7m |
| PXT150 | PXT | Stone Field (44TN) | San Francisco International Airport (KSFO) | 2026-08-23 16:02 UTC | 2026-08-23 20:45 UTC | 4h 43m |
| N1701T |  | Auburn University Regional Airport (KAUO) | Lanett Regional Airport (K7A3) | 2026-08-23 20:25 UTC | 2026-08-23 20:38 UTC | 13m |
| N9774F |  | Perry-Houston County Airport (KPXE) | Perry-Houston County Airport (KPXE) | 2026-08-23 20:25 UTC | 2026-08-23 20:34 UTC | 9m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-23 20:23 UTC | 2026-08-23 20:34 UTC | 11m |
| TCCFD | TCC | London Biggin Hill Airport (EGKB) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-23 18:54 UTC | 2026-08-23 20:34 UTC | 1h 39m |
| N778VW |  | Hammond Northshore Regional Airport (KHDC) | Le Gros Memorial Airport (K3R2) | 2026-08-23 20:08 UTC | 2026-08-23 20:33 UTC | 25m |
| N17WG |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-08-23 20:07 UTC | 2026-08-23 20:31 UTC | 24m |
| N780JH |  | Logan-Cache Airport (KLGU) | KU42 (KU42) | 2026-08-23 20:09 UTC | 2026-08-23 20:31 UTC | 21m |
| N786FG |  | Trenton Mercer Airport (KTTN) | Flying W Airport (KN14) | 2026-08-23 19:23 UTC | 2026-08-23 20:30 UTC | 1h 7m |
| TKR16 | TKR | 18XS (18XS) | K14F (K14F) | 2026-08-23 20:11 UTC | 2026-08-23 20:26 UTC | 14m |
| LIFELN1 | LIF | Rocky Mountain Metro Airport (KBJC) | Buckley Space Force Base Airport (KBKF) | 2026-08-23 20:13 UTC | 2026-08-23 20:23 UTC | 9m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-23 20:10 UTC | 2026-08-23 20:23 UTC | 12m |
| CSI532 | CSI | Albuquerque International Sunport Airport (KABQ) | Socorro Municipal Airport (KONM) | 2026-08-23 20:08 UTC | 2026-08-23 20:22 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
