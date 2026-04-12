# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_23:04:52_UTC-green)

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

**Latest saved flight:** 2026-04-12 23:04:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 23:04:52 UTC

- **31,540** saved flights
- **14,304** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **31,540** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **387,571.5 tonnes** estimated CO2 emissions
- **22,467,911 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1315 |
| 2 | SkyWest Airlines | 1287 |
| 3 | IndiGo | 804 |
| 4 | EJA | 555 |
| 5 | American Airlines | 552 |
| 6 | Southwest Airlines | 460 |
| 7 | ENY | 427 |
| 8 | Lufthansa | 375 |
| 9 | AXM | 335 |
| 10 | LATAM Airlines | 320 |
| 11 | Vueling | 320 |
| 12 | All Nippon Airways | 287 |
| 13 | AZU | 281 |
| 14 | QLK | 263 |
| 15 | Delta Air Lines | 260 |
| 16 | LXJ | 249 |
| 17 | Swiss International | 233 |
| 18 | Alaska Airlines | 212 |
| 19 | easyJet | 211 |
| 20 | WIF | 206 |
| 21 | EJU | 205 |
| 22 | VIV | 203 |
| 23 | AEE | 197 |
| 24 | Japan Airlines | 197 |
| 25 | EDV | 188 |
| 26 | United Airlines | 184 |
| 27 | GLO | 172 |
| 28 | Avianca | 171 |
| 29 | Air France | 169 |
| 30 | JetBlue | 168 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 24924 |
| 2 | 🇮🇳 IN | 2471 |
| 3 | 🇪🇸 ES | 2339 |
| 4 | 🇦🇺 AU | 2190 |
| 5 | 🇧🇷 BR | 1874 |
| 6 | 🇯🇵 JP | 1713 |
| 7 | 🇮🇹 IT | 1650 |
| 8 | 🇨🇴 CO | 1594 |
| 9 | 🇩🇪 DE | 1593 |
| 10 | 🇨🇦 CA | 1532 |
| 11 | 🇬🇧 GB | 1275 |
| 12 | 🇫🇷 FR | 1158 |
| 13 | 🇲🇽 MX | 1013 |
| 14 | 🇬🇷 GR | 895 |
| 15 | 🇨🇭 CH | 880 |
| 16 | 🇲🇾 MY | 807 |
| 17 | 🇳🇴 NO | 695 |
| 18 | 🇳🇿 NZ | 671 |
| 19 | 🇿🇦 ZA | 646 |
| 20 | 🇬🇹 GT | 587 |
| 21 | 🇵🇭 PH | 579 |
| 22 | 🇹🇷 TR | 578 |
| 23 | 🇹🇭 TH | 569 |
| 24 | 🇰🇷 KR | 534 |
| 25 | 🇵🇱 PL | 478 |
| 26 | 🇲🇦 MA | 406 |
| 27 | 🇧🇸 BS | 331 |
| 28 | 🇲🇪 ME | 313 |
| 29 | 🇳🇱 NL | 300 |
| 30 | 🇮🇩 ID | 297 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 762 |
| 2 | Tokyo International Airport |  | JP | 576 |
| 3 | El Dorado International Airport |  | CO | 566 |
| 4 | Denver International Airport |  | US | 535 |
| 5 | Indira Gandhi International Airport |  | IN | 521 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 437 |
| 7 | La Aurora Airport |  | GT | 425 |
| 8 | Harry Reid International Airport |  | US | 410 |
| 9 | Guaymaral Airport |  | CO | 388 |
| 10 | Zurich Airport |  | CH | 387 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 329 |
| 12 | Chicago O'Hare International Airport |  | US | 327 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 326 |
| 14 | Frankfurt am Main International Airport |  | DE | 320 |
| 15 | Kuala Lumpur International Airport |  | MY | 306 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 305 |
| 17 | Macau International Airport |  | MO | 297 |
| 18 | Charlotte/Douglas International Airport |  | US | 286 |
| 19 | Tenerife Norte Airport |  | ES | 282 |
| 20 | Madrid Barajas International Airport |  | ES | 281 |
| 21 | Bengaluru International Airport |  | IN | 281 |
| 22 | Congonhas Airport |  | BR | 274 |
| 23 | Ninoy Aquino International Airport |  | PH | 266 |
| 24 | Malpensa International Airport |  | IT | 257 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 242 |
| 26 | Daniel K Inouye International Airport |  | US | 240 |
| 27 | Reno/Tahoe International Airport |  | US | 239 |
| 28 | Salt Lake City International Airport |  | US | 239 |
| 29 | Charles de Gaulle International Airport |  | FR | 230 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 227 |
| 31 | John Paul II International Airport Kraków-Balice Airport |  | PL | 217 |
| 32 | Capua Airport |  | IT | 216 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 215 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 215 |
| 35 | Miami International Airport |  | US | 210 |
| 36 | O. R. Tambo International Airport |  | ZA | 209 |
| 37 | Vitoria/Foronda Airport |  | ES | 207 |
| 38 | Seattle-Tacoma International Airport |  | US | 200 |
| 39 | Barcelona International Airport |  | ES | 197 |
| 40 | Calgary International Airport |  | CA | 193 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 151 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 145 | 1h 8m | 706 km | 1,765.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 133 | 14m | 114 km | 260.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 112 | 24m | 225 km | 434.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 104 | 28m | 304 km | 545.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 91 | 1h 28m | 910 km | 1,428.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 81 | 19m | 165 km | 230.4 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 76 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 75 | 31m | - | - |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 70 | 55m | 546 km | 659.1 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 67 | 27m | 275 km | 317.5 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 66 | 1h 12m | 770 km | 876.8 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 62 | 21m | 244 km | 261.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 62 | 31m | 369 km | 394.6 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 19 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 57 | 45m | 452 km | 444.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 54 | 20m | 250 km | 233.2 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 48 | 20m | 147 km | 121.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 48 | 1h 42m | 1,423 km | 1,178.0 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 46 | 16m | 162 km | 128.9 t |
| 27 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 44 | 12m | 15 km | 11.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LXJ449 | LXJ | Bermuda Dunes Airport (KUDD) | Van Nuys Airport (KVNY) | 2026-04-12 22:32 UTC | 2026-04-12 23:04 UTC | 32m |
| UAE9862 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-12 16:47 UTC | 2026-04-12 23:02 UTC | 6h 15m |
| CGFHA | CGF | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-04-12 22:42 UTC | 2026-04-12 22:58 UTC | 16m |
| BRG2682 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-04-12 22:20 UTC | 2026-04-12 22:54 UTC | 34m |
| RFS708 | RFS | Boeing Field/King County International Airport (KBFI) | Portland-Hillsboro Airport (KHIO) | 2026-04-12 21:34 UTC | 2026-04-12 22:54 UTC | 1h 20m |
| AUB1319 | AUB | Auburn University Regional Airport (KAUO) | Auburn University Regional Airport (KAUO) | 2026-04-12 21:49 UTC | 2026-04-12 22:52 UTC | 1h 2m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-04-12 12:03 UTC | 2026-04-12 22:45 UTC | 10h 42m |
| X2A |  | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-04-12 22:44 UTC | 2026-04-12 22:45 UTC | 1m |
| N100YC |  | Scottsdale Airport (KSDL) | City Of Las Animas - Bent County Airport (K7V9) | 2026-04-12 20:53 UTC | 2026-04-12 22:42 UTC | 1h 49m |
| BRG2652 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-04-12 22:09 UTC | 2026-04-12 22:38 UTC | 29m |
| RFS733 | RFS | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-04-12 22:03 UTC | 2026-04-12 22:27 UTC | 24m |
| N488RJ |  | Scottsdale Airport (KSDL) | Sedona Airport (KSEZ) | 2026-04-12 22:07 UTC | 2026-04-12 22:22 UTC | 15m |
| LXJ377 | LXJ | Cuyahoga County Airport (KCGF) | Norfolk International Airport (KORF) | 2026-04-12 21:09 UTC | 2026-04-12 22:19 UTC | 1h 9m |
| EJA914 | EJA | Waterbury-Oxford Airport (KOXC) | Austin-Bergstrom International Airport (KAUS) | 2026-04-12 17:38 UTC | 2026-04-12 22:17 UTC | 4h 39m |
| XAJSL | XAJ | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | 2026-04-12 22:01 UTC | 2026-04-12 22:16 UTC | 14m |
| N100BW |  | Talkeetna Airport (PATK) | Songlo Vista Airport (3AK3) | 2026-04-12 21:43 UTC | 2026-04-12 22:14 UTC | 30m |
| QHD681 | QHD | Drake Field (KFYV) | Tunica Municipal Airport (KUTA) | 2026-04-12 21:34 UTC | 2026-04-12 22:11 UTC | 36m |
| EOQ | EOQ | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-04-12 22:00 UTC | 2026-04-12 22:10 UTC | 10m |
| N333PN |  | Woodlake Airport (KO42) | 9CL4 (9CL4) | 2026-04-12 21:28 UTC | 2026-04-12 22:10 UTC | 42m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-04-12 20:02 UTC | 2026-04-12 22:09 UTC | 2h 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
