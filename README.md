# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_05:24:00_UTC-green)

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

**Latest saved flight:** 2026-04-15 05:24:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-15 05:24:00 UTC

- **35,242** saved flights
- **15,523** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **35,242** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **429,855.2 tonnes** estimated CO2 emissions
- **24,919,139 km** total distance flown
- **845 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1503 |
| 2 | SkyWest Airlines | 1412 |
| 3 | IndiGo | 872 |
| 4 | EJA | 612 |
| 5 | American Airlines | 607 |
| 6 | Southwest Airlines | 507 |
| 7 | ENY | 469 |
| 8 | Lufthansa | 381 |
| 9 | AXM | 370 |
| 10 | Vueling | 356 |
| 11 | LATAM Airlines | 353 |
| 12 | All Nippon Airways | 315 |
| 13 | AZU | 315 |
| 14 | Delta Air Lines | 300 |
| 15 | QLK | 300 |
| 16 | LXJ | 281 |
| 17 | Swiss International | 265 |
| 18 | WIF | 255 |
| 19 | AEE | 236 |
| 20 | Alaska Airlines | 236 |
| 21 | easyJet | 234 |
| 22 | EJU | 231 |
| 23 | VIV | 229 |
| 24 | Japan Airlines | 218 |
| 25 | EDV | 201 |
| 26 | United Airlines | 199 |
| 27 | Air France | 193 |
| 28 | GLO | 192 |
| 29 | JetBlue | 187 |
| 30 | Avianca | 184 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 27759 |
| 2 | 🇮🇳 IN | 2667 |
| 3 | 🇪🇸 ES | 2626 |
| 4 | 🇦🇺 AU | 2496 |
| 5 | 🇧🇷 BR | 2082 |
| 6 | 🇯🇵 JP | 1907 |
| 7 | 🇮🇹 IT | 1882 |
| 8 | 🇩🇪 DE | 1778 |
| 9 | 🇨🇴 CO | 1763 |
| 10 | 🇨🇦 CA | 1726 |
| 11 | 🇬🇧 GB | 1445 |
| 12 | 🇫🇷 FR | 1300 |
| 13 | 🇲🇽 MX | 1132 |
| 14 | 🇬🇷 GR | 1044 |
| 15 | 🇨🇭 CH | 959 |
| 16 | 🇲🇾 MY | 894 |
| 17 | 🇳🇴 NO | 824 |
| 18 | 🇳🇿 NZ | 769 |
| 19 | 🇿🇦 ZA | 730 |
| 20 | 🇵🇭 PH | 674 |
| 21 | 🇹🇷 TR | 638 |
| 22 | 🇹🇭 TH | 630 |
| 23 | 🇬🇹 GT | 616 |
| 24 | 🇰🇷 KR | 598 |
| 25 | 🇵🇱 PL | 551 |
| 26 | 🇲🇦 MA | 441 |
| 27 | 🇧🇸 BS | 346 |
| 28 | 🇳🇱 NL | 345 |
| 29 | 🇲🇪 ME | 344 |
| 30 | 🇮🇩 ID | 333 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 842 |
| 2 | Tokyo International Airport |  | JP | 650 |
| 3 | El Dorado International Airport |  | CO | 628 |
| 4 | Denver International Airport |  | US | 597 |
| 5 | Indira Gandhi International Airport |  | IN | 565 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 513 |
| 7 | Harry Reid International Airport |  | US | 467 |
| 8 | La Aurora Airport |  | GT | 452 |
| 9 | Guaymaral Airport |  | CO | 441 |
| 10 | Zurich Airport |  | CH | 432 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 361 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 356 |
| 13 | Chicago O'Hare International Airport |  | US | 355 |
| 14 | Kuala Lumpur International Airport |  | MY | 344 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 341 |
| 16 | Frankfurt am Main International Airport |  | DE | 334 |
| 17 | Macau International Airport |  | MO | 321 |
| 18 | Charlotte/Douglas International Airport |  | US | 319 |
| 19 | Madrid Barajas International Airport |  | ES | 318 |
| 20 | Ninoy Aquino International Airport |  | PH | 311 |
| 21 | Congonhas Airport |  | BR | 309 |
| 22 | Bengaluru International Airport |  | IN | 308 |
| 23 | Tenerife Norte Airport |  | ES | 307 |
| 24 | Malpensa International Airport |  | IT | 285 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 281 |
| 26 | Salt Lake City International Airport |  | US | 270 |
| 27 | Daniel K Inouye International Airport |  | US | 268 |
| 28 | Capua Airport |  | IT | 262 |
| 29 | Charles de Gaulle International Airport |  | FR | 257 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 248 |
| 31 | Reno/Tahoe International Airport |  | US | 247 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 241 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 240 |
| 34 | O. R. Tambo International Airport |  | ZA | 235 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 234 |
| 36 | Vitoria/Foronda Airport |  | ES | 232 |
| 37 | Barcelona International Airport |  | ES | 231 |
| 38 | Seattle-Tacoma International Airport |  | US | 222 |
| 39 | Viracopos International Airport |  | BR | 221 |
| 40 | Miami International Airport |  | US | 219 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 173 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 163 | 1h 8m | 706 km | 1,984.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 147 | 14m | 114 km | 288.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 131 | 24m | 225 km | 508.2 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 101 | 1h 27m | 910 km | 1,584.9 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 92 | 19m | 165 km | 261.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 87 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 87 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 84 | 21m | 244 km | 353.7 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 76 | 27m | 275 km | 360.1 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 74 | 1h 12m | 770 km | 983.0 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 68 | 31m | 369 km | 432.8 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 65 | 45m | 452 km | 506.6 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 60 | 20m | 250 km | 259.2 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 57 | 20m | 147 km | 144.2 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 53 | 13m | 99 km | 90.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 52 | 14m | 154 km | 137.8 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 51 | 16m | 162 km | 143.0 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 50 | 12m | 15 km | 13.2 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 50 | 1h 20m | 961 km | 828.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 50 | 1h 53m | 1,304 km | 1,124.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NYV | NYV | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-15 05:04 UTC | 2026-04-15 05:24 UTC | 19m |
|  |  | Osan Air Base (RKSO) | Osan Air Base (RKSO) | 2026-04-15 04:46 UTC | 2026-04-15 05:10 UTC | 24m |
| DAH6235 | DAH | Tsletsi Airport (DAFI) | Ain Oussera Airport (DAAQ) | 2026-04-15 05:09 UTC | 2026-04-15 05:09 UTC | 0m |
| HSOMR1 | HSO | Emden Airport (EDWE) | Borkum Airport (EDWR) | 2026-04-15 04:23 UTC | 2026-04-15 04:57 UTC | 33m |
| N424PE |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-04-15 04:10 UTC | 2026-04-15 04:55 UTC | 44m |
| FD521 |  | Adelaide International Airport (YPAD) | Waikerie Airport (YWKI) | 2026-04-15 04:25 UTC | 2026-04-15 04:47 UTC | 22m |
| CPP10 | CPP | Mantsala Airport (EFMN) | Mantsala Airport (EFMN) | 2026-04-15 04:43 UTC | 2026-04-15 04:47 UTC | 3m |
| ZSNHX | ZSN | Lanseria Airport (FALA) | Pilanesberg International Airport (FAPN) | 2026-04-15 04:25 UTC | 2026-04-15 04:45 UTC | 19m |
| AE998 |  | Albury Airport (YMAY) | Cowra Airport (YCWR) | 2026-04-15 04:08 UTC | 2026-04-15 04:41 UTC | 33m |
| PKART | PKA | Budiarto Airport (WICB) | Budiarto Airport (WICB) | 2026-04-15 03:13 UTC | 2026-04-15 04:39 UTC | 1h 26m |
| APG221 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-04-15 04:11 UTC | 2026-04-15 04:36 UTC | 24m |
| ZSNVE | ZSN | Lanseria Airport (FALA) | Pilanesberg International Airport (FAPN) | 2026-04-15 04:10 UTC | 2026-04-15 04:33 UTC | 22m |
| GRYHK21 | GRY | Lake Havasu City Airport (KHII) | Lake Havasu City Airport (KHII) | 2026-04-15 04:33 UTC | 2026-04-15 04:33 UTC | 0m |
| FC78 |  | Gimpo International Airport (RKSS) | Daegu Airport (RKTN) | 2026-04-15 04:09 UTC | 2026-04-15 04:32 UTC | 23m |
| WUJ | WUJ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-15 04:18 UTC | 2026-04-15 04:31 UTC | 13m |
| TGZ723 | TGZ | Tbilisi International Airport (UGTB) | Gyumri Shirak Airport (UDSG) | 2026-04-15 04:12 UTC | 2026-04-15 04:30 UTC | 18m |
| WMT401 | WMT | Belgrade Nikola Tesla Airport (LYBE) | Campia Turzii Air Base (LRCT) | 2026-04-15 03:58 UTC | 2026-04-15 04:28 UTC | 29m |
| WIF7GT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-15 04:12 UTC | 2026-04-15 04:24 UTC | 12m |
| AXM6304 | AXM | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 2026-04-15 04:08 UTC | 2026-04-15 04:23 UTC | 14m |
| SEH1CF | SEH | Eleftherios Venizelos International Airport (LGAV) | Aktion National Airport (LGPZ) | 2026-04-15 03:51 UTC | 2026-04-15 04:22 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
