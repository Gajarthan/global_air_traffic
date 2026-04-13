# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_08:00:27_UTC-green)

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

**Latest saved flight:** 2026-04-13 08:00:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 08:00:27 UTC

- **31,797** saved flights
- **14,374** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **31,797** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **391,529.2 tonnes** estimated CO2 emissions
- **22,697,344 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1334 |
| 2 | SkyWest Airlines | 1295 |
| 3 | IndiGo | 814 |
| 4 | EJA | 556 |
| 5 | American Airlines | 554 |
| 6 | Southwest Airlines | 464 |
| 7 | ENY | 429 |
| 8 | Lufthansa | 375 |
| 9 | AXM | 338 |
| 10 | LATAM Airlines | 324 |
| 11 | Vueling | 323 |
| 12 | All Nippon Airways | 290 |
| 13 | AZU | 284 |
| 14 | Delta Air Lines | 265 |
| 15 | QLK | 265 |
| 16 | LXJ | 254 |
| 17 | Swiss International | 236 |
| 18 | Alaska Airlines | 215 |
| 19 | easyJet | 211 |
| 20 | WIF | 209 |
| 21 | EJU | 206 |
| 22 | VIV | 204 |
| 23 | Japan Airlines | 202 |
| 24 | AEE | 201 |
| 25 | EDV | 189 |
| 26 | United Airlines | 184 |
| 27 | GLO | 173 |
| 28 | Avianca | 171 |
| 29 | Air France | 169 |
| 30 | JetBlue | 169 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 25047 |
| 2 | 🇮🇳 IN | 2495 |
| 3 | 🇪🇸 ES | 2369 |
| 4 | 🇦🇺 AU | 2233 |
| 5 | 🇧🇷 BR | 1890 |
| 6 | 🇯🇵 JP | 1740 |
| 7 | 🇮🇹 IT | 1670 |
| 8 | 🇩🇪 DE | 1608 |
| 9 | 🇨🇴 CO | 1598 |
| 10 | 🇨🇦 CA | 1539 |
| 11 | 🇬🇧 GB | 1284 |
| 12 | 🇫🇷 FR | 1167 |
| 13 | 🇲🇽 MX | 1015 |
| 14 | 🇬🇷 GR | 911 |
| 15 | 🇨🇭 CH | 885 |
| 16 | 🇲🇾 MY | 815 |
| 17 | 🇳🇴 NO | 702 |
| 18 | 🇳🇿 NZ | 688 |
| 19 | 🇿🇦 ZA | 650 |
| 20 | 🇵🇭 PH | 598 |
| 21 | 🇬🇹 GT | 587 |
| 22 | 🇹🇷 TR | 584 |
| 23 | 🇹🇭 TH | 579 |
| 24 | 🇰🇷 KR | 551 |
| 25 | 🇵🇱 PL | 480 |
| 26 | 🇲🇦 MA | 408 |
| 27 | 🇧🇸 BS | 331 |
| 28 | 🇲🇪 ME | 315 |
| 29 | 🇮🇩 ID | 303 |
| 30 | 🇲🇴 MO | 303 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 766 |
| 2 | Tokyo International Airport |  | JP | 587 |
| 3 | El Dorado International Airport |  | CO | 568 |
| 4 | Denver International Airport |  | US | 538 |
| 5 | Indira Gandhi International Airport |  | IN | 530 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 446 |
| 7 | La Aurora Airport |  | GT | 425 |
| 8 | Harry Reid International Airport |  | US | 415 |
| 9 | Zurich Airport |  | CH | 390 |
| 10 | Guaymaral Airport |  | CO | 388 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 330 |
| 12 | Chicago O'Hare International Airport |  | US | 330 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 327 |
| 14 | Frankfurt am Main International Airport |  | DE | 320 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 310 |
| 16 | Kuala Lumpur International Airport |  | MY | 310 |
| 17 | Macau International Airport |  | MO | 303 |
| 18 | Charlotte/Douglas International Airport |  | US | 289 |
| 19 | Madrid Barajas International Airport |  | ES | 285 |
| 20 | Tenerife Norte Airport |  | ES | 284 |
| 21 | Bengaluru International Airport |  | IN | 284 |
| 22 | Congonhas Airport |  | BR | 277 |
| 23 | Ninoy Aquino International Airport |  | PH | 276 |
| 24 | Malpensa International Airport |  | IT | 257 |
| 25 | Daniel K Inouye International Airport |  | US | 245 |
| 26 | Salt Lake City International Airport |  | US | 244 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 243 |
| 28 | Reno/Tahoe International Airport |  | US | 242 |
| 29 | Charles de Gaulle International Airport |  | FR | 230 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 229 |
| 31 | John Paul II International Airport Kraków-Balice Airport |  | PL | 218 |
| 32 | Capua Airport |  | IT | 218 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 217 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 216 |
| 35 | O. R. Tambo International Airport |  | ZA | 211 |
| 36 | Miami International Airport |  | US | 210 |
| 37 | Vitoria/Foronda Airport |  | ES | 208 |
| 38 | Barcelona International Airport |  | ES | 202 |
| 39 | Seattle-Tacoma International Airport |  | US | 202 |
| 40 | Viracopos International Airport |  | BR | 196 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 151 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 147 | 1h 8m | 706 km | 1,789.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 134 | 14m | 114 km | 262.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 118 | 24m | 225 km | 457.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 105 | 28m | 304 km | 550.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 92 | 1h 28m | 910 km | 1,443.7 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 82 | 19m | 165 km | 233.3 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 76 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 76 | 9m | - | - |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 72 | 55m | 546 km | 677.9 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 68 | 27m | 275 km | 322.2 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 67 | 1h 12m | 770 km | 890.0 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 66 | 21m | 244 km | 277.9 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 62 | 31m | 369 km | 394.6 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 19 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 58 | 45m | 452 km | 452.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 55 | 20m | 250 km | 237.6 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 50 | 20m | 147 km | 126.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 50 | 1h 42m | 1,423 km | 1,227.1 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 47 | 16m | 162 km | 131.7 t |
| 27 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 44 | 12m | 15 km | 11.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ARCTS11 | ARC | Wunstorf Airport (ETNW) | Jever Airport (ETNJ) | 2026-04-13 06:50 UTC | 2026-04-13 08:00 UTC | 1h 10m |
| OEDCC | OED | Graz Airport (LOWG) | Graz Airport (LOWG) | 2026-04-13 07:26 UTC | 2026-04-13 07:57 UTC | 30m |
| N115SE |  | Brown Field Municipal Airport (KSDM) | Van Nuys Airport (KVNY) | 2026-04-13 07:09 UTC | 2026-04-13 07:39 UTC | 29m |
| DKAGX | DKA | Juist Airport (EDWJ) | Juist Airport (EDWJ) | 2026-04-13 06:18 UTC | 2026-04-13 07:38 UTC | 1h 20m |
| N95VB |  | Sleap Airport (EGCV) | Denham Aerodrome (EGLD) | 2026-04-13 06:52 UTC | 2026-04-13 07:37 UTC | 45m |
| ELY067 | ELY | Ben Gurion International Airport (LLBG) | Don Mueang International Airport (VTBD) | 2026-04-12 21:27 UTC | 2026-04-13 07:36 UTC | 10h 9m |
| HL1269 |  | G 530 Airport (RK49) | RKTA (RKTA) | 2026-04-13 07:34 UTC | 2026-04-13 07:35 UTC | 1m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-13 07:14 UTC | 2026-04-13 07:35 UTC | 20m |
| DRAG152 | DRA | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | 2026-04-13 07:27 UTC | 2026-04-13 07:31 UTC | 3m |
| AAR702 | AAR | Ninoy Aquino International Airport (RPLL) | Incheon International Airport (RKSI) | 2026-04-13 04:21 UTC | 2026-04-13 07:31 UTC | 3h 9m |
| ZES | ZES | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-13 06:49 UTC | 2026-04-13 07:25 UTC | 36m |
| AAR512 | AAR | Barcelona International Airport (LEBL) | Incheon International Airport (RKSI) | 2026-04-12 19:43 UTC | 2026-04-13 07:25 UTC | 11h 41m |
| J044KT |  | Adi Sutjipto International Airport (WARJ) | Gading Wonosari Airport (WI1G) | 2026-04-13 07:20 UTC | 2026-04-13 07:23 UTC | 3m |
| OAL4NX | OAL | Eleftherios Venizelos International Airport (LGAV) | Naxos Airport (LGNX) | 2026-04-13 06:56 UTC | 2026-04-13 07:17 UTC | 21m |
| AIQ510 | AIQ | Don Mueang International Airport (VTBD) | Mersing Airport (WMAU) | 2026-04-13 05:28 UTC | 2026-04-13 07:16 UTC | 1h 48m |
| SAS1314 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-13 06:38 UTC | 2026-04-13 07:07 UTC | 29m |
| EJU4183 | EJU | Grazzanise Airport (LIRM) | Paris-Orly Airport (LFPO) | 2026-04-13 05:26 UTC | 2026-04-13 07:07 UTC | 1h 40m |
| SEH470 | SEH | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-04-13 06:49 UTC | 2026-04-13 07:06 UTC | 17m |
| IGO1153 | IndiGo | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-04-13 05:51 UTC | 2026-04-13 07:05 UTC | 1h 13m |
| SWR4WF | Swiss International | Zurich Airport (LSZH) | Václav Havel Airport (LKPR) | 2026-04-13 06:02 UTC | 2026-04-13 07:01 UTC | 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
