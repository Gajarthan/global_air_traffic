# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_11:23:15_UTC-green)

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

**Latest saved flight:** 2026-04-15 11:23:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-15 11:23:15 UTC

- **35,534** saved flights
- **15,601** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **35,534** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **432,818.3 tonnes** estimated CO2 emissions
- **25,090,916 km** total distance flown
- **843 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1523 |
| 2 | SkyWest Airlines | 1412 |
| 3 | IndiGo | 889 |
| 4 | EJA | 612 |
| 5 | American Airlines | 607 |
| 6 | Southwest Airlines | 507 |
| 7 | ENY | 469 |
| 8 | Lufthansa | 382 |
| 9 | AXM | 380 |
| 10 | Vueling | 360 |
| 11 | LATAM Airlines | 355 |
| 12 | All Nippon Airways | 321 |
| 13 | AZU | 316 |
| 14 | QLK | 302 |
| 15 | Delta Air Lines | 301 |
| 16 | LXJ | 281 |
| 17 | Swiss International | 273 |
| 18 | WIF | 259 |
| 19 | AEE | 239 |
| 20 | Alaska Airlines | 237 |
| 21 | easyJet | 236 |
| 22 | EJU | 231 |
| 23 | VIV | 229 |
| 24 | Japan Airlines | 219 |
| 25 | EDV | 201 |
| 26 | Air France | 199 |
| 27 | United Airlines | 199 |
| 28 | GLO | 192 |
| 29 | JetBlue | 187 |
| 30 | AIQ | 186 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 27771 |
| 2 | 🇮🇳 IN | 2721 |
| 3 | 🇪🇸 ES | 2651 |
| 4 | 🇦🇺 AU | 2537 |
| 5 | 🇧🇷 BR | 2088 |
| 6 | 🇯🇵 JP | 1953 |
| 7 | 🇮🇹 IT | 1909 |
| 8 | 🇩🇪 DE | 1824 |
| 9 | 🇨🇴 CO | 1763 |
| 10 | 🇨🇦 CA | 1730 |
| 11 | 🇬🇧 GB | 1468 |
| 12 | 🇫🇷 FR | 1326 |
| 13 | 🇲🇽 MX | 1132 |
| 14 | 🇬🇷 GR | 1064 |
| 15 | 🇨🇭 CH | 981 |
| 16 | 🇲🇾 MY | 916 |
| 17 | 🇳🇴 NO | 841 |
| 18 | 🇳🇿 NZ | 772 |
| 19 | 🇿🇦 ZA | 744 |
| 20 | 🇵🇭 PH | 680 |
| 21 | 🇹🇭 TH | 656 |
| 22 | 🇹🇷 TR | 643 |
| 23 | 🇬🇹 GT | 616 |
| 24 | 🇰🇷 KR | 609 |
| 25 | 🇵🇱 PL | 560 |
| 26 | 🇲🇦 MA | 444 |
| 27 | 🇳🇱 NL | 350 |
| 28 | 🇲🇪 ME | 348 |
| 29 | 🇧🇸 BS | 346 |
| 30 | 🇮🇩 ID | 341 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 842 |
| 2 | Tokyo International Airport |  | JP | 663 |
| 3 | El Dorado International Airport |  | CO | 628 |
| 4 | Denver International Airport |  | US | 597 |
| 5 | Indira Gandhi International Airport |  | IN | 577 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 524 |
| 7 | Harry Reid International Airport |  | US | 467 |
| 8 | La Aurora Airport |  | GT | 452 |
| 9 | Zurich Airport |  | CH | 443 |
| 10 | Guaymaral Airport |  | CO | 441 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 361 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 356 |
| 13 | Chicago O'Hare International Airport |  | US | 355 |
| 14 | Kuala Lumpur International Airport |  | MY | 354 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 345 |
| 16 | Frankfurt am Main International Airport |  | DE | 335 |
| 17 | Macau International Airport |  | MO | 321 |
| 18 | Madrid Barajas International Airport |  | ES | 320 |
| 19 | Charlotte/Douglas International Airport |  | US | 319 |
| 20 | Bengaluru International Airport |  | IN | 315 |
| 21 | Ninoy Aquino International Airport |  | PH | 314 |
| 22 | Tenerife Norte Airport |  | ES | 314 |
| 23 | Congonhas Airport |  | BR | 311 |
| 24 | Malpensa International Airport |  | IT | 290 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 281 |
| 26 | Salt Lake City International Airport |  | US | 270 |
| 27 | Daniel K Inouye International Airport |  | US | 269 |
| 28 | Charles de Gaulle International Airport |  | FR | 263 |
| 29 | Capua Airport |  | IT | 262 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 248 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 248 |
| 32 | Reno/Tahoe International Airport |  | US | 247 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 244 |
| 34 | O. R. Tambo International Airport |  | ZA | 239 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 234 |
| 36 | Vitoria/Foronda Airport |  | ES | 232 |
| 37 | Barcelona International Airport |  | ES | 231 |
| 38 | Seattle-Tacoma International Airport |  | US | 223 |
| 39 | Viracopos International Airport |  | BR | 222 |
| 40 | Don Mueang International Airport |  | TH | 222 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 173 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 168 | 1h 8m | 706 km | 2,045.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 147 | 14m | 114 km | 288.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 134 | 24m | 225 km | 519.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 102 | 1h 27m | 910 km | 1,600.6 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 95 | 19m | 165 km | 270.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 91 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 87 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 84 | 21m | 244 km | 353.7 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 76 | 27m | 275 km | 360.1 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 74 | 1h 12m | 770 km | 983.0 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 68 | 45m | 452 km | 530.0 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 68 | 31m | 369 km | 432.8 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 60 | 20m | 250 km | 259.2 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 58 | 20m | 147 km | 146.8 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 53 | 13m | 99 km | 90.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 53 | 14m | 154 km | 140.4 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 52 | 16m | 162 km | 145.8 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 50 | 12m | 15 km | 13.2 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 50 | 1h 20m | 961 km | 828.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 50 | 1h 53m | 1,304 km | 1,124.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AIQ3441 | AIQ | Don Mueang International Airport (VTBD) | Chiang Mai International Airport (VTCC) | 2026-04-15 10:35 UTC | 2026-04-15 11:23 UTC | 47m |
| YOQ | YOQ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-15 10:30 UTC | 2026-04-15 11:15 UTC | 44m |
| NHD431 | NHD | Esbjerg Airport (EKEB) | Borkum Airport (EDWR) | 2026-04-15 10:13 UTC | 2026-04-15 11:10 UTC | 57m |
| FXJ69N | FXJ | Paris-Le Bourget Airport (LFPB) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-15 08:09 UTC | 2026-04-15 11:01 UTC | 2h 51m |
| HBZWD | HBZ | Saanen Airport (LSGK) | Courchevel Airport (LFLJ) | 2026-04-15 09:49 UTC | 2026-04-15 10:56 UTC | 1h 6m |
| RYR59LA | Ryanair | London Stansted Airport (EGSS) | Olsztyn Dajtki Airport (EPOD) | 2026-04-15 09:09 UTC | 2026-04-15 10:48 UTC | 1h 38m |
| EWG1 | EWG | Leipzig Halle Airport (EDDP) | Leipzig Halle Airport (EDDP) | 2026-04-15 09:37 UTC | 2026-04-15 10:40 UTC | 1h 2m |
| TMN1 | TMN | Auckland International Airport (NZAA) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-15 07:40 UTC | 2026-04-15 10:38 UTC | 2h 57m |
| HNL24A | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-04-15 10:07 UTC | 2026-04-15 10:37 UTC | 29m |
| DRAGO74 | DRA | Sallanches Airport (LFHZ) | Megeve Airport (LFHM) | 2026-04-15 10:15 UTC | 2026-04-15 10:33 UTC | 17m |
| URSA30 | URS | Fairbanks International Airport (PAFA) | Ladd Army Air Field (PAFB) | 2026-04-15 09:03 UTC | 2026-04-15 10:28 UTC | 1h 24m |
| SRB501 | SRB | Batajnica Air Base (LYBT) | Batajnica Air Base (LYBT) | 2026-04-15 08:55 UTC | 2026-04-15 10:28 UTC | 1h 33m |
| DLA9800 | DLA | Trieste / Ronchi Dei Legionari (LIPQ) | Trieste / Ronchi Dei Legionari (LIPQ) | 2026-04-15 09:58 UTC | 2026-04-15 10:26 UTC | 27m |
| EZY21QW | easyJet | London Luton Airport (EGGW) | Madeira Airport (LPMA) | 2026-04-15 06:40 UTC | 2026-04-15 10:26 UTC | 3h 46m |
| RYR75SE | Ryanair | Brussels South Charleroi Airport (EBCI) | LIAL (LIAL) | 2026-04-15 09:07 UTC | 2026-04-15 10:26 UTC | 1h 18m |
| N126TS |  | Boise Air Trml/Gowen Field (KBOI) | Cottonwood Municipal Airport (KS84) | 2026-04-15 09:39 UTC | 2026-04-15 10:25 UTC | 46m |
| CJT623 | CJT | East Gore Eco Airpark (CCY4) | Montréal (Mirabel) Airport (CYMX) | 2026-04-15 08:59 UTC | 2026-04-15 10:24 UTC | 1h 25m |
| DSF15MO | DSF | Deauville-Saint-Gatien Airport (LFRG) | Nice-Cote d'Azur Airport (LFMN) | 2026-04-15 09:04 UTC | 2026-04-15 10:23 UTC | 1h 19m |
| BBC437 | BBC | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-15 09:52 UTC | 2026-04-15 10:20 UTC | 27m |
| DHYAH | DHY | Bonn-Hangelar Airport (EDKB) | Bonn-Hangelar Airport (EDKB) | 2026-04-15 09:32 UTC | 2026-04-15 10:18 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
