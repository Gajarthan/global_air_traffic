# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_22:27:46_UTC-green)

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

**Latest saved flight:** 2026-04-12 22:27:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 22:27:46 UTC

- **31,457** saved flights
- **14,279** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **31,457** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **386,499.1 tonnes** estimated CO2 emissions
- **22,405,744 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1314 |
| 2 | SkyWest Airlines | 1281 |
| 3 | IndiGo | 804 |
| 4 | EJA | 551 |
| 5 | American Airlines | 550 |
| 6 | Southwest Airlines | 458 |
| 7 | ENY | 426 |
| 8 | Lufthansa | 375 |
| 9 | AXM | 335 |
| 10 | Vueling | 320 |
| 11 | LATAM Airlines | 318 |
| 12 | All Nippon Airways | 287 |
| 13 | AZU | 278 |
| 14 | QLK | 260 |
| 15 | Delta Air Lines | 259 |
| 16 | LXJ | 247 |
| 17 | Swiss International | 233 |
| 18 | Alaska Airlines | 212 |
| 19 | easyJet | 211 |
| 20 | WIF | 206 |
| 21 | EJU | 205 |
| 22 | VIV | 202 |
| 23 | AEE | 197 |
| 24 | Japan Airlines | 197 |
| 25 | EDV | 187 |
| 26 | United Airlines | 184 |
| 27 | Avianca | 170 |
| 28 | GLO | 170 |
| 29 | Air France | 169 |
| 30 | JetBlue | 168 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 24833 |
| 2 | 🇮🇳 IN | 2470 |
| 3 | 🇪🇸 ES | 2339 |
| 4 | 🇦🇺 AU | 2180 |
| 5 | 🇧🇷 BR | 1860 |
| 6 | 🇯🇵 JP | 1713 |
| 7 | 🇮🇹 IT | 1648 |
| 8 | 🇩🇪 DE | 1593 |
| 9 | 🇨🇴 CO | 1588 |
| 10 | 🇨🇦 CA | 1524 |
| 11 | 🇬🇧 GB | 1275 |
| 12 | 🇫🇷 FR | 1158 |
| 13 | 🇲🇽 MX | 1009 |
| 14 | 🇬🇷 GR | 895 |
| 15 | 🇨🇭 CH | 879 |
| 16 | 🇲🇾 MY | 807 |
| 17 | 🇳🇴 NO | 695 |
| 18 | 🇳🇿 NZ | 671 |
| 19 | 🇿🇦 ZA | 646 |
| 20 | 🇬🇹 GT | 581 |
| 21 | 🇹🇷 TR | 578 |
| 22 | 🇵🇭 PH | 575 |
| 23 | 🇹🇭 TH | 569 |
| 24 | 🇰🇷 KR | 532 |
| 25 | 🇵🇱 PL | 478 |
| 26 | 🇲🇦 MA | 404 |
| 27 | 🇧🇸 BS | 331 |
| 28 | 🇲🇪 ME | 313 |
| 29 | 🇳🇱 NL | 300 |
| 30 | 🇮🇩 ID | 296 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 758 |
| 2 | Tokyo International Airport |  | JP | 576 |
| 3 | El Dorado International Airport |  | CO | 563 |
| 4 | Denver International Airport |  | US | 534 |
| 5 | Indira Gandhi International Airport |  | IN | 521 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 437 |
| 7 | La Aurora Airport |  | GT | 420 |
| 8 | Harry Reid International Airport |  | US | 409 |
| 9 | Guaymaral Airport |  | CO | 388 |
| 10 | Zurich Airport |  | CH | 386 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 327 |
| 12 | Chicago O'Hare International Airport |  | US | 326 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 324 |
| 14 | Frankfurt am Main International Airport |  | DE | 320 |
| 15 | Kuala Lumpur International Airport |  | MY | 306 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 303 |
| 17 | Macau International Airport |  | MO | 295 |
| 18 | Charlotte/Douglas International Airport |  | US | 284 |
| 19 | Tenerife Norte Airport |  | ES | 282 |
| 20 | Madrid Barajas International Airport |  | ES | 281 |
| 21 | Bengaluru International Airport |  | IN | 281 |
| 22 | Congonhas Airport |  | BR | 270 |
| 23 | Ninoy Aquino International Airport |  | PH | 264 |
| 24 | Malpensa International Airport |  | IT | 255 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 241 |
| 26 | Daniel K Inouye International Airport |  | US | 240 |
| 27 | Reno/Tahoe International Airport |  | US | 239 |
| 28 | Salt Lake City International Airport |  | US | 238 |
| 29 | Charles de Gaulle International Airport |  | FR | 230 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 227 |
| 31 | John Paul II International Airport Kraków-Balice Airport |  | PL | 217 |
| 32 | Capua Airport |  | IT | 216 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 215 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 213 |
| 35 | Miami International Airport |  | US | 210 |
| 36 | O. R. Tambo International Airport |  | ZA | 209 |
| 37 | Vitoria/Foronda Airport |  | ES | 207 |
| 38 | Seattle-Tacoma International Airport |  | US | 200 |
| 39 | Barcelona International Airport |  | ES | 197 |
| 40 | Viracopos International Airport |  | BR | 192 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 151 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 145 | 1h 8m | 706 km | 1,765.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 132 | 14m | 114 km | 258.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 112 | 24m | 225 km | 434.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 104 | 28m | 304 km | 545.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 91 | 1h 28m | 910 km | 1,428.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 81 | 19m | 165 km | 230.4 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 75 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 74 | 9m | - | - |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 70 | 55m | 546 km | 659.1 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 67 | 27m | 275 km | 317.5 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 66 | 1h 12m | 770 km | 876.8 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 62 | 21m | 244 km | 261.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 60 | 31m | 369 km | 381.9 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 19 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 57 | 45m | 452 km | 444.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 54 | 20m | 250 km | 233.2 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 48 | 20m | 147 km | 121.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 48 | 1h 42m | 1,423 km | 1,178.0 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 44 | 12m | 15 km | 11.6 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 44 | 16m | 162 km | 123.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RFS733 | RFS | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-04-12 22:03 UTC | 2026-04-12 22:27 UTC | 24m |
| XAJSL | XAJ | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | 2026-04-12 22:01 UTC | 2026-04-12 22:16 UTC | 14m |
| EOQ | EOQ | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-04-12 22:00 UTC | 2026-04-12 22:10 UTC | 10m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-04-12 20:02 UTC | 2026-04-12 22:09 UTC | 2h 7m |
| N54HA |  | University Of Oklahoma Westheimer Airport (KOUN) | Aitkin Municipal/Steve Kurtz Field (KAIT) | 2026-04-12 20:37 UTC | 2026-04-12 22:05 UTC | 1h 27m |
| LRT424 | LRT | Laguardia Airport (KLGA) | John F Kennedy International Airport (KJFK) | 2026-04-12 21:53 UTC | 2026-04-12 22:05 UTC | 12m |
| N182N |  | Prairie Cottage Airport (8KS8) | Salina Regional Airport (KSLN) | 2026-04-12 21:45 UTC | 2026-04-12 22:03 UTC | 18m |
| EJM19 | EJM | St Paul Downtown Holman Field (KSTP) | Rocky Mountain Metro Airport (KBJC) | 2026-04-12 20:20 UTC | 2026-04-12 22:03 UTC | 1h 42m |
| SLH560 | SLH | Harry Reid International Airport (KLAS) | Lincoln Airport (KLNK) | 2026-04-12 19:52 UTC | 2026-04-12 22:02 UTC | 2h 9m |
| N62486 |  | Ohio State University Airport (KOSU) | Erie-Ottawa International Airport (KPCW) | 2026-04-12 21:17 UTC | 2026-04-12 22:01 UTC | 44m |
| N77ZR |  | Creve Coeur Airport (K1H0) | Blackhawk Airport (6MO0) | 2026-04-12 21:50 UTC | 2026-04-12 22:01 UTC | 10m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-04-12 11:01 UTC | 2026-04-12 22:00 UTC | 10h 59m |
| N38BL |  | Newark Liberty International Airport (KEWR) | John F Kennedy International Airport (KJFK) | 2026-04-12 20:58 UTC | 2026-04-12 21:55 UTC | 57m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-12 10:32 UTC | 2026-04-12 21:51 UTC | 11h 18m |
| ANVIL97 | ANV | Eastern Wv Regional/Shepherd Field (KMRB) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-04-12 21:22 UTC | 2026-04-12 21:48 UTC | 26m |
| N545GC |  | Lompoc Airport (KLPC) | Lompoc Airport (KLPC) | 2026-04-12 21:30 UTC | 2026-04-12 21:47 UTC | 17m |
| N362TW |  | Teterboro Airport (KTEB) | Habersham County Airport (KAJR) | 2026-04-12 20:15 UTC | 2026-04-12 21:45 UTC | 1h 29m |
| AAL418 | American Airlines | Chicago O'Hare International Airport (KORD) | St Louis Lambert International Airport (KSTL) | 2026-04-12 20:52 UTC | 2026-04-12 21:44 UTC | 51m |
| N7220J |  | Pompano Beach Airpark (KPMP) | Fort Lauderdale Executive Airport (KFXE) | 2026-04-12 19:02 UTC | 2026-04-12 21:43 UTC | 2h 41m |
| ZKIME | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-04-12 21:36 UTC | 2026-04-12 21:43 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
