# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_19:16:50_UTC-green)

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

**Latest saved flight:** 2026-08-24 19:16:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 19:16:50 UTC

- **233,075** saved flights
- **71,617** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **233,075** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,808,975.8 tonnes** estimated CO2 emissions
- **162,839,174 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9356 |
| 2 | SkyWest Airlines | 8241 |
| 3 | EJA | 4526 |
| 4 | IndiGo | 3941 |
| 5 | American Airlines | 3802 |
| 6 | Southwest Airlines | 3589 |
| 7 | Delta Air Lines | 2975 |
| 8 | ENY | 2838 |
| 9 | LATAM Airlines | 2240 |
| 10 | AZU | 2171 |
| 11 | Vueling | 1992 |
| 12 | Lufthansa | 1901 |
| 13 | WIF | 1854 |
| 14 | LXJ | 1835 |
| 15 | easyJet | 1631 |
| 16 | Swiss International | 1563 |
| 17 | AXM | 1551 |
| 18 | EJU | 1493 |
| 19 | United Airlines | 1479 |
| 20 | QLK | 1474 |
| 21 | Alaska Airlines | 1399 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1299 |
| 24 | WMT | 1295 |
| 25 | VIV | 1280 |
| 26 | PGT | 1273 |
| 27 | Air France | 1266 |
| 28 | Wizz Air | 1231 |
| 29 | AEE | 1160 |
| 30 | JetBlue | 1159 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 194043 |
| 2 | 🇪🇸 ES | 14970 |
| 3 | 🇧🇷 BR | 13619 |
| 4 | 🇦🇺 AU | 13164 |
| 5 | 🇨🇦 CA | 12846 |
| 6 | 🇮🇹 IT | 12679 |
| 7 | 🇮🇳 IN | 12277 |
| 8 | 🇩🇪 DE | 11494 |
| 9 | 🇬🇧 GB | 10995 |
| 10 | 🇨🇴 CO | 9743 |
| 11 | 🇯🇵 JP | 9448 |
| 12 | 🇫🇷 FR | 9332 |
| 13 | 🇹🇷 TR | 6904 |
| 14 | 🇬🇷 GR | 6860 |
| 15 | 🇲🇽 MX | 6470 |
| 16 | 🇨🇭 CH | 6222 |
| 17 | 🇳🇴 NO | 5766 |
| 18 | 🇲🇾 MY | 4144 |
| 19 | 🇹🇭 TH | 4108 |
| 20 | 🇿🇦 ZA | 4071 |
| 21 | 🇵🇱 PL | 3882 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3185 |
| 24 | 🇬🇹 GT | 2926 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2681 |
| 27 | 🇲🇦 MA | 2367 |
| 28 | 🇲🇪 ME | 2148 |
| 29 | 🇳🇱 NL | 2092 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4847 |
| 2 | Denver International Airport |  | US | 3780 |
| 3 | Indira Gandhi International Airport |  | IN | 2842 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2671 |
| 6 | Harry Reid International Airport |  | US | 2504 |
| 7 | Zurich Airport |  | CH | 2439 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2381 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2340 |
| 10 | La Aurora Airport |  | GT | 2229 |
| 11 | El Dorado International Airport |  | CO | 2169 |
| 12 | Chicago O'Hare International Airport |  | US | 2107 |
| 13 | Salt Lake City International Airport |  | US | 2051 |
| 14 | Congonhas Airport |  | BR | 1987 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1965 |
| 16 | Frankfurt am Main International Airport |  | DE | 1861 |
| 17 | Capua Airport |  | IT | 1835 |
| 18 | Madrid Barajas International Airport |  | ES | 1830 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1752 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1727 |
| 21 | Malpensa International Airport |  | IT | 1672 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1662 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1619 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1534 |
| 27 | Charlotte/Douglas International Airport |  | US | 1510 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1471 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1427 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1408 |
| 32 | Viracopos International Airport |  | BR | 1388 |
| 33 | Bengaluru International Airport |  | IN | 1372 |
| 34 | Seattle-Tacoma International Airport |  | US | 1366 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1365 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1322 |
| 38 | Oslo Gardermoen Airport |  | NO | 1307 |
| 39 | O. R. Tambo International Airport |  | ZA | 1265 |
| 40 | Vancouver International Airport |  | CA | 1264 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1084 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 850 | 21m | 244 km | 3,579.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 580 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 521 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 384 | 27m | 275 km | 1,819.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 361 | 1h 50m | 1,423 km | 8,859.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 359 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 339 | 44m | 241 km | 1,408.1 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 309 | 24m | 218 km | 1,164.1 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 304 | 1h 38m | 1,156 km | 6,064.7 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 289 | 19m | 99 km | 495.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 285 | 27m | 215 km | 1,055.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 270 | 13m | - | - |
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
| N406M |  | Merrill Field (PAMR) | Kenai Municipal Airport (PAEN) | 2026-08-24 18:50 UTC | 2026-08-24 19:16 UTC | 26m |
| CXK311 | CXK | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-08-24 19:00 UTC | 2026-08-24 19:16 UTC | 15m |
| N1029T |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-08-24 19:02 UTC | 2026-08-24 19:14 UTC | 11m |
| N5NJ |  | Lehigh Valley International Airport (KABE) | Linden Airport (KLDJ) | 2026-08-24 18:31 UTC | 2026-08-24 19:12 UTC | 41m |
| N762AT |  | Jefferson County International Airport (K0S9) | William R Fairchild International Airport (KCLM) | 2026-08-24 18:51 UTC | 2026-08-24 19:11 UTC | 20m |
| BOE738 | BOE | Boeing Field/King County International Airport (KBFI) | Franz Ranch Airport (33WA) | 2026-08-24 17:32 UTC | 2026-08-24 19:09 UTC | 1h 37m |
| TKR03 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | Jecan Airport (06CO) | 2026-08-24 18:49 UTC | 2026-08-24 19:09 UTC | 20m |
| N64942 |  | Roberts Field/Redmond Municipal Airport (KRDM) | Prineville Airport (KS39) | 2026-08-24 18:53 UTC | 2026-08-24 19:08 UTC | 15m |
| N339BG |  | Wood County Regional Airport (K1G0) | Donald P Miller Airport (KFZI) | 2026-08-24 18:52 UTC | 2026-08-24 19:07 UTC | 14m |
| N808TA |  | Quast Airport (MN62) | Hutchinson Municipal/Butler Field (KHCD) | 2026-08-24 18:54 UTC | 2026-08-24 19:06 UTC | 12m |
| N8846J |  | KFTG (KFTG) | Metrogro Farm Airport (CO25) | 2026-08-24 18:48 UTC | 2026-08-24 19:06 UTC | 18m |
| N947MT |  | Casper/Natrona County International Airport (KCPR) | Chamberlain Brothers Ranch Airport (WY66) | 2026-08-24 18:46 UTC | 2026-08-24 19:02 UTC | 15m |
| NIT239 | NIT | Heart Of Georgia Regional Airport (KEZM) | Hawkinsville-Pulaski County Airport (K51A) | 2026-08-24 18:20 UTC | 2026-08-24 19:00 UTC | 40m |
| N100BW |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-08-24 18:40 UTC | 2026-08-24 19:00 UTC | 20m |
| N739WR |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-24 18:44 UTC | 2026-08-24 19:00 UTC | 15m |
| N42LC |  | Wings Field (KLOM) | Wings Field (KLOM) | 2026-08-24 18:48 UTC | 2026-08-24 18:59 UTC | 11m |
| N509AF |  | Morristown Municipal Airport (KMMU) | Sky Manor Airport (KN40) | 2026-08-24 17:54 UTC | 2026-08-24 18:58 UTC | 1h 4m |
| RNGR710 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-08-24 18:17 UTC | 2026-08-24 18:55 UTC | 37m |
| ARCAS06 | ARC | Danaher Airport (7TX0) | Haskell Municipal Airport (K15F) | 2026-08-24 18:42 UTC | 2026-08-24 18:53 UTC | 10m |
| N930FY |  | Laconia Municipal Airport (KLCI) | Bangor International Airport (KBGR) | 2026-08-24 18:18 UTC | 2026-08-24 18:51 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
