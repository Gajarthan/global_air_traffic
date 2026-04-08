# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_05:46:11_UTC-green)

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

**Latest saved flight:** 2026-04-08 05:46:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 05:46:11 UTC

- **22,708** saved flights
- **11,142** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **22,708** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **280,604.8 tonnes** estimated CO2 emissions
- **16,266,944 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 971 |
| 2 | Ryanair | 930 |
| 3 | IndiGo | 636 |
| 4 | EJA | 422 |
| 5 | American Airlines | 419 |
| 6 | Southwest Airlines | 330 |
| 7 | ENY | 302 |
| 8 | Lufthansa | 282 |
| 9 | Vueling | 233 |
| 10 | LATAM Airlines | 230 |
| 11 | AXM | 227 |
| 12 | All Nippon Airways | 203 |
| 13 | QLK | 202 |
| 14 | Delta Air Lines | 199 |
| 15 | LXJ | 189 |
| 16 | AZU | 181 |
| 17 | Swiss International | 162 |
| 18 | VIV | 162 |
| 19 | Alaska Airlines | 156 |
| 20 | Japan Airlines | 156 |
| 21 | easyJet | 149 |
| 22 | United Airlines | 146 |
| 23 | EJU | 143 |
| 24 | AEE | 139 |
| 25 | Avianca | 139 |
| 26 | EDV | 135 |
| 27 | WIF | 135 |
| 28 | AXB | 127 |
| 29 | Air France | 119 |
| 30 | ANZ | 116 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 17976 |
| 2 | 🇮🇳 IN | 1926 |
| 3 | 🇪🇸 ES | 1740 |
| 4 | 🇦🇺 AU | 1679 |
| 5 | 🇧🇷 BR | 1284 |
| 6 | 🇯🇵 JP | 1273 |
| 7 | 🇨🇴 CO | 1181 |
| 8 | 🇮🇹 IT | 1131 |
| 9 | 🇩🇪 DE | 1118 |
| 10 | 🇨🇦 CA | 1023 |
| 11 | 🇬🇧 GB | 885 |
| 12 | 🇫🇷 FR | 819 |
| 13 | 🇲🇽 MX | 747 |
| 14 | 🇬🇷 GR | 637 |
| 15 | 🇨🇭 CH | 605 |
| 16 | 🇲🇾 MY | 528 |
| 17 | 🇿🇦 ZA | 492 |
| 18 | 🇳🇿 NZ | 484 |
| 19 | 🇳🇴 NO | 469 |
| 20 | 🇬🇹 GT | 467 |
| 21 | 🇹🇷 TR | 434 |
| 22 | 🇵🇭 PH | 433 |
| 23 | 🇰🇷 KR | 404 |
| 24 | 🇹🇭 TH | 359 |
| 25 | 🇵🇱 PL | 324 |
| 26 | 🇲🇦 MA | 269 |
| 27 | 🇧🇸 BS | 243 |
| 28 | 🇮🇩 ID | 235 |
| 29 | 🇲🇪 ME | 231 |
| 30 | 🇳🇱 NL | 221 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 550 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 426 |
| 4 | Denver International Airport |  | US | 407 |
| 5 | Indira Gandhi International Airport |  | IN | 388 |
| 6 | La Aurora Airport |  | GT | 322 |
| 7 | Harry Reid International Airport |  | US | 307 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 306 |
| 9 | Zurich Airport |  | CH | 270 |
| 10 | Frankfurt am Main International Airport |  | DE | 248 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 241 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 241 |
| 13 | Chicago O'Hare International Airport |  | US | 237 |
| 14 | Guaymaral Airport |  | CO | 236 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 231 |
| 16 | Bengaluru International Airport |  | IN | 217 |
| 17 | Charlotte/Douglas International Airport |  | US | 214 |
| 18 | Macau International Airport |  | MO | 211 |
| 19 | Tenerife Norte Airport |  | ES | 202 |
| 20 | Madrid Barajas International Airport |  | ES | 200 |
| 21 | Ninoy Aquino International Airport |  | PH | 198 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 192 |
| 23 | Kuala Lumpur International Airport |  | MY | 192 |
| 24 | Congonhas Airport |  | BR | 186 |
| 25 | Salt Lake City International Airport |  | US | 182 |
| 26 | Malpensa International Airport |  | IT | 175 |
| 27 | Daniel K Inouye International Airport |  | US | 175 |
| 28 | Reno/Tahoe International Airport |  | US | 174 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 170 |
| 30 | Charles de Gaulle International Airport |  | FR | 165 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 162 |
| 32 | Miami International Airport |  | US | 155 |
| 33 | O. R. Tambo International Airport |  | ZA | 153 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 152 |
| 35 | Pune Airport |  | IN | 152 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 151 |
| 37 | Seattle-Tacoma International Airport |  | US | 149 |
| 38 | Vitoria/Foronda Airport |  | ES | 148 |
| 39 | Barcelona International Airport |  | ES | 145 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 140 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 107 | 1h 8m | 706 km | 1,302.7 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 87 | 24m | 225 km | 337.5 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 87 | 27m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 81 | 28m | 304 km | 424.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 68 | 1h 28m | 910 km | 1,067.1 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 66 | 27m | 152 km | 172.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 62 | 1h 42m | 1,156 km | 1,236.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 54 | 19m | 165 km | 153.6 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 50 | 1h 13m | 770 km | 664.2 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 49 | 55m | 546 km | 461.3 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 45 | 31m | 369 km | 286.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 45 | 52m | 556 km | 431.4 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 42 | 4m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 42 | 20m | 250 km | 181.4 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 42 | 9m | - | - |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 41 | 46m | 452 km | 319.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 39 | 1h 43m | 1,423 km | 957.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 33 | 1h 22m | 961 km | 547.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ASI633 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-04-08 05:04 UTC | 2026-04-08 05:46 UTC | 42m |
| THY8FW | Turkish Airlines | Istanbul Hezarfen Airfield (LTBW) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-08 04:48 UTC | 2026-04-08 05:42 UTC | 53m |
| NKD | NKD | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-08 04:58 UTC | 2026-04-08 05:32 UTC | 33m |
| ZEF | ZEF | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-08 04:53 UTC | 2026-04-08 05:30 UTC | 36m |
| KDI | KDI | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-08 05:15 UTC | 2026-04-08 05:30 UTC | 14m |
| WVU | WVU | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-08 04:57 UTC | 2026-04-08 05:13 UTC | 15m |
| ZHU | ZHU | Bacchus Marsh Airport (YBSS) | Melbourne Moorabbin Airport (YMMB) | 2026-04-08 04:46 UTC | 2026-04-08 05:08 UTC | 22m |
| IGO1721 | IndiGo | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-08 00:52 UTC | 2026-04-08 05:01 UTC | 4h 8m |
| SKW4297 | SkyWest Airlines | Green Bay/Austin Straubel International Airport (KGRB) | Ernie's Field (1MI4) | 2026-04-08 04:42 UTC | 2026-04-08 05:00 UTC | 18m |
| LR455 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-08 04:31 UTC | 2026-04-08 05:00 UTC | 28m |
| DLH5HR | Lufthansa | Nuremberg Airport (EDDN) | Frankfurt-Egelsbach Airport (EDFE) | 2026-04-08 04:24 UTC | 2026-04-08 04:59 UTC | 34m |
| SRR6646 | SRR | Cologne Bonn Airport (EDDK) | Francisco de Sá Carneiro Airport (LPPR) | 2026-04-08 02:38 UTC | 2026-04-08 04:57 UTC | 2h 18m |
| DAL2851 | Delta Air Lines | Seattle-Tacoma International Airport (KSEA) | Denver International Airport (KDEN) | 2026-04-08 02:52 UTC | 2026-04-08 04:55 UTC | 2h 3m |
| BRU975 | BRU | Minsk International Airport (UMMS) | Smolensk North Airport (XUBS) | 2026-04-08 04:42 UTC | 2026-04-08 04:53 UTC | 11m |
| VN04T |  | Winnipeg James Armstrong Richardson International Airport (CYWG) | Berens River Airport (CYBV) | 2026-04-08 04:16 UTC | 2026-04-08 04:53 UTC | 36m |
| NLY | NLY | Bendigo Airport (YBDG) | Melbourne Essendon Airport (YMEN) | 2026-04-08 03:33 UTC | 2026-04-08 04:52 UTC | 1h 19m |
| ASI477 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-04-08 04:33 UTC | 2026-04-08 04:52 UTC | 18m |
| SEH2HR | SEH | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-04-08 04:23 UTC | 2026-04-08 04:44 UTC | 21m |
| N113UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-04-08 03:36 UTC | 2026-04-08 04:44 UTC | 1h 7m |
| CWA922 | CWA | Calgary International Airport (CYYC) | Lumsden (Colhoun) Airport (CKH8) | 2026-04-08 03:25 UTC | 2026-04-08 04:42 UTC | 1h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
