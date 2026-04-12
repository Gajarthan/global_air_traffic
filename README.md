# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_03:13:04_UTC-green)

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

**Latest saved flight:** 2026-04-12 03:13:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 03:13:04 UTC

- **29,953** saved flights
- **13,773** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **29,953** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **365,723.5 tonnes** estimated CO2 emissions
- **21,201,362 km** total distance flown
- **845 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1230 |
| 2 | Ryanair | 1227 |
| 3 | IndiGo | 770 |
| 4 | American Airlines | 524 |
| 5 | EJA | 523 |
| 6 | Southwest Airlines | 435 |
| 7 | ENY | 408 |
| 8 | Lufthansa | 359 |
| 9 | AXM | 317 |
| 10 | Vueling | 306 |
| 11 | LATAM Airlines | 295 |
| 12 | All Nippon Airways | 266 |
| 13 | AZU | 262 |
| 14 | QLK | 255 |
| 15 | Delta Air Lines | 246 |
| 16 | LXJ | 240 |
| 17 | Swiss International | 217 |
| 18 | Alaska Airlines | 201 |
| 19 | VIV | 195 |
| 20 | EJU | 193 |
| 21 | easyJet | 193 |
| 22 | Japan Airlines | 192 |
| 23 | WIF | 187 |
| 24 | AEE | 186 |
| 25 | United Airlines | 179 |
| 26 | EDV | 178 |
| 27 | Avianca | 167 |
| 28 | GLO | 160 |
| 29 | JetBlue | 159 |
| 30 | Air France | 154 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23779 |
| 2 | 🇮🇳 IN | 2375 |
| 3 | 🇪🇸 ES | 2212 |
| 4 | 🇦🇺 AU | 2110 |
| 5 | 🇧🇷 BR | 1732 |
| 6 | 🇯🇵 JP | 1631 |
| 7 | 🇮🇹 IT | 1531 |
| 8 | 🇨🇴 CO | 1518 |
| 9 | 🇩🇪 DE | 1495 |
| 10 | 🇨🇦 CA | 1477 |
| 11 | 🇬🇧 GB | 1201 |
| 12 | 🇫🇷 FR | 1098 |
| 13 | 🇲🇽 MX | 971 |
| 14 | 🇬🇷 GR | 845 |
| 15 | 🇨🇭 CH | 840 |
| 16 | 🇲🇾 MY | 759 |
| 17 | 🇳🇿 NZ | 653 |
| 18 | 🇳🇴 NO | 632 |
| 19 | 🇿🇦 ZA | 609 |
| 20 | 🇵🇭 PH | 559 |
| 21 | 🇬🇹 GT | 551 |
| 22 | 🇹🇷 TR | 541 |
| 23 | 🇹🇭 TH | 537 |
| 24 | 🇰🇷 KR | 508 |
| 25 | 🇵🇱 PL | 450 |
| 26 | 🇲🇦 MA | 373 |
| 27 | 🇧🇸 BS | 318 |
| 28 | 🇲🇪 ME | 298 |
| 29 | 🇳🇱 NL | 286 |
| 30 | 🇮🇩 ID | 282 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 720 |
| 2 | Tokyo International Airport |  | JP | 547 |
| 3 | El Dorado International Airport |  | CO | 541 |
| 4 | Denver International Airport |  | US | 512 |
| 5 | Indira Gandhi International Airport |  | IN | 495 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 413 |
| 7 | La Aurora Airport |  | GT | 393 |
| 8 | Harry Reid International Airport |  | US | 389 |
| 9 | Guaymaral Airport |  | CO | 359 |
| 10 | Zurich Airport |  | CH | 358 |
| 11 | Chicago O'Hare International Airport |  | US | 314 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 313 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 311 |
| 14 | Frankfurt am Main International Airport |  | DE | 302 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 295 |
| 16 | Kuala Lumpur International Airport |  | MY | 286 |
| 17 | Macau International Airport |  | MO | 281 |
| 18 | Charlotte/Douglas International Airport |  | US | 271 |
| 19 | Bengaluru International Airport |  | IN | 270 |
| 20 | Madrid Barajas International Airport |  | ES | 263 |
| 21 | Tenerife Norte Airport |  | ES | 263 |
| 22 | Ninoy Aquino International Airport |  | PH | 257 |
| 23 | Congonhas Airport |  | BR | 253 |
| 24 | Malpensa International Airport |  | IT | 239 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 233 |
| 26 | Daniel K Inouye International Airport |  | US | 230 |
| 27 | Salt Lake City International Airport |  | US | 230 |
| 28 | Reno/Tahoe International Airport |  | US | 229 |
| 29 | Charles de Gaulle International Airport |  | FR | 211 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 207 |
| 31 | Capua Airport |  | IT | 205 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 202 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 201 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 200 |
| 35 | Miami International Airport |  | US | 200 |
| 36 | O. R. Tambo International Airport |  | ZA | 194 |
| 37 | Vitoria/Foronda Airport |  | ES | 193 |
| 38 | Seattle-Tacoma International Airport |  | US | 191 |
| 39 | Barcelona International Airport |  | ES | 189 |
| 40 | Viracopos International Airport |  | BR | 183 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 140 | 1h 8m | 706 km | 1,704.5 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 139 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 126 | 14m | 114 km | 247.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 110 | 24m | 225 km | 426.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 101 | 28m | 304 km | 529.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 87 | 1h 27m | 910 km | 1,365.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 76 | 19m | 165 km | 216.2 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 75 | 21m | 99 km | 128.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 66 | 55m | 546 km | 621.4 t |
| 13 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 65 | 9m | - | - |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 63 | 27m | 275 km | 298.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 63 | 1h 12m | 770 km | 836.9 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 58 | 31m | 369 km | 369.2 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 56 | 52m | 556 km | 536.8 t |
| 19 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 54 | 21m | 244 km | 227.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 54 | 45m | 452 km | 420.9 t |
| 21 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 50 | 20m | 250 km | 216.0 t |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 46 | 20m | 147 km | 116.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 42 | 1h 19m | 961 km | 696.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 41 | 12m | 15 km | 10.8 t |
| 30 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 40 | 55m | 630 km | 434.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UPS61 | UPS | Taiwan Taoyuan International Airport (RCTP) | Ted Stevens Anchorage International Airport (PANC) | 2026-04-11 19:30 UTC | 2026-04-12 03:13 UTC | 7h 42m |
| BHA400D | BHA | Tribhuvan International Airport (VNKT) | Jiri Airport (VNJI) | 2026-04-12 02:05 UTC | 2026-04-12 02:55 UTC | 49m |
| HIM766 | HIM | Tribhuvan International Airport (VNKT) | Simara Airport (VNSI) | 2026-04-11 17:27 UTC | 2026-04-12 02:47 UTC | 9h 19m |
| EXU | EXU | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-12 02:02 UTC | 2026-04-12 02:33 UTC | 30m |
| VTFSQ | VTF | Bhiwani Airport (VIBW) | Jhunjhunu Airport (VI69) | 2026-04-12 01:43 UTC | 2026-04-12 02:31 UTC | 48m |
| ANZ268L | ANZ | Auckland International Airport (NZAA) | Kaikohe Airport (NZKO) | 2026-04-12 01:58 UTC | 2026-04-12 02:25 UTC | 26m |
| N1303Q |  | Ocala International-Jim Taylor Field (KOCF) | Bartow Executive Airport (KBOW) | 2026-04-12 01:09 UTC | 2026-04-12 02:22 UTC | 1h 13m |
| EVANS11 | EVA Air | Perry Park Airport (CO93) | Perry Park Airport (CO93) | 2026-04-12 01:35 UTC | 2026-04-12 02:20 UTC | 45m |
| RXA6826 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-04-12 01:41 UTC | 2026-04-12 02:19 UTC | 37m |
| QLK322D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-04-12 01:49 UTC | 2026-04-12 02:18 UTC | 28m |
| UBG141 | UBG | VGZR (VGZR) | Cox's Bazar Airport (VGCB) | 2026-04-12 01:37 UTC | 2026-04-12 02:17 UTC | 40m |
| SHINR38 | SHI | Austin-Bergstrom International Airport (KAUS) | Austin-Bergstrom International Airport (KAUS) | 2026-04-12 01:51 UTC | 2026-04-12 02:14 UTC | 22m |
| SLI995 | SLI | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-12 01:09 UTC | 2026-04-12 02:13 UTC | 1h 4m |
| AM260 |  | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-04-12 01:53 UTC | 2026-04-12 02:12 UTC | 18m |
| IGO697L | IndiGo | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-04-12 01:48 UTC | 2026-04-12 02:08 UTC | 20m |
| BTN701 | BTN | Suvarnabhumi Airport (VTBS) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-11 23:47 UTC | 2026-04-12 02:07 UTC | 2h 20m |
| SNJ33 | SNJ | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-04-12 00:45 UTC | 2026-04-12 02:07 UTC | 1h 22m |
| ANA403 | All Nippon Airways | Tokyo International Airport (RJTT) | Yamagata Airport (RJSC) | 2026-04-12 01:36 UTC | 2026-04-12 02:06 UTC | 29m |
| KAL1811 | Korean Air | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-04-12 01:39 UTC | 2026-04-12 02:05 UTC | 25m |
| N83MR |  | Jacksonville International Airport (KJAX) | Bibb County Airport (K0A8) | 2026-04-12 00:52 UTC | 2026-04-12 02:05 UTC | 1h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
