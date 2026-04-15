# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_12:21:10_UTC-green)

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

**Latest saved flight:** 2026-04-15 12:21:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-15 12:21:10 UTC

- **35,633** saved flights
- **15,624** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **35,633** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **433,787.2 tonnes** estimated CO2 emissions
- **25,147,086 km** total distance flown
- **843 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1530 |
| 2 | SkyWest Airlines | 1412 |
| 3 | IndiGo | 894 |
| 4 | EJA | 612 |
| 5 | American Airlines | 607 |
| 6 | Southwest Airlines | 507 |
| 7 | ENY | 469 |
| 8 | AXM | 384 |
| 9 | Lufthansa | 382 |
| 10 | Vueling | 362 |
| 11 | LATAM Airlines | 359 |
| 12 | All Nippon Airways | 321 |
| 13 | AZU | 316 |
| 14 | QLK | 302 |
| 15 | Delta Air Lines | 301 |
| 16 | LXJ | 281 |
| 17 | Swiss International | 273 |
| 18 | WIF | 260 |
| 19 | AEE | 240 |
| 20 | easyJet | 239 |
| 21 | Alaska Airlines | 237 |
| 22 | EJU | 232 |
| 23 | VIV | 229 |
| 24 | Japan Airlines | 222 |
| 25 | EDV | 201 |
| 26 | Air France | 200 |
| 27 | United Airlines | 199 |
| 28 | GLO | 192 |
| 29 | AIQ | 188 |
| 30 | JetBlue | 188 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 27806 |
| 2 | 🇮🇳 IN | 2732 |
| 3 | 🇪🇸 ES | 2662 |
| 4 | 🇦🇺 AU | 2545 |
| 5 | 🇧🇷 BR | 2096 |
| 6 | 🇯🇵 JP | 1967 |
| 7 | 🇮🇹 IT | 1915 |
| 8 | 🇩🇪 DE | 1835 |
| 9 | 🇨🇴 CO | 1763 |
| 10 | 🇨🇦 CA | 1730 |
| 11 | 🇬🇧 GB | 1478 |
| 12 | 🇫🇷 FR | 1334 |
| 13 | 🇲🇽 MX | 1132 |
| 14 | 🇬🇷 GR | 1070 |
| 15 | 🇨🇭 CH | 983 |
| 16 | 🇲🇾 MY | 923 |
| 17 | 🇳🇴 NO | 844 |
| 18 | 🇳🇿 NZ | 772 |
| 19 | 🇿🇦 ZA | 750 |
| 20 | 🇵🇭 PH | 683 |
| 21 | 🇹🇭 TH | 660 |
| 22 | 🇹🇷 TR | 649 |
| 23 | 🇬🇹 GT | 616 |
| 24 | 🇰🇷 KR | 611 |
| 25 | 🇵🇱 PL | 563 |
| 26 | 🇲🇦 MA | 445 |
| 27 | 🇳🇱 NL | 350 |
| 28 | 🇲🇪 ME | 349 |
| 29 | 🇧🇸 BS | 346 |
| 30 | 🇮🇩 ID | 341 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 842 |
| 2 | Tokyo International Airport |  | JP | 667 |
| 3 | El Dorado International Airport |  | CO | 628 |
| 4 | Denver International Airport |  | US | 597 |
| 5 | Indira Gandhi International Airport |  | IN | 579 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 527 |
| 7 | Harry Reid International Airport |  | US | 470 |
| 8 | La Aurora Airport |  | GT | 452 |
| 9 | Zurich Airport |  | CH | 443 |
| 10 | Guaymaral Airport |  | CO | 441 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 361 |
| 12 | Kuala Lumpur International Airport |  | MY | 357 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 356 |
| 14 | Chicago O'Hare International Airport |  | US | 355 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 345 |
| 16 | Frankfurt am Main International Airport |  | DE | 335 |
| 17 | Madrid Barajas International Airport |  | ES | 322 |
| 18 | Macau International Airport |  | MO | 321 |
| 19 | Charlotte/Douglas International Airport |  | US | 319 |
| 20 | Ninoy Aquino International Airport |  | PH | 316 |
| 21 | Bengaluru International Airport |  | IN | 315 |
| 22 | Tenerife Norte Airport |  | ES | 314 |
| 23 | Congonhas Airport |  | BR | 313 |
| 24 | Malpensa International Airport |  | IT | 292 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 281 |
| 26 | Daniel K Inouye International Airport |  | US | 270 |
| 27 | Salt Lake City International Airport |  | US | 270 |
| 28 | Charles de Gaulle International Airport |  | FR | 264 |
| 29 | Capua Airport |  | IT | 262 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 251 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 249 |
| 32 | Reno/Tahoe International Airport |  | US | 247 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 245 |
| 34 | O. R. Tambo International Airport |  | ZA | 240 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 235 |
| 36 | Barcelona International Airport |  | ES | 234 |
| 37 | Vitoria/Foronda Airport |  | ES | 232 |
| 38 | Don Mueang International Airport |  | TH | 224 |
| 39 | Seattle-Tacoma International Airport |  | US | 223 |
| 40 | Viracopos International Airport |  | BR | 222 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 173 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 168 | 1h 8m | 706 km | 2,045.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 147 | 14m | 114 km | 288.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 134 | 24m | 225 km | 519.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 104 | 1h 27m | 910 km | 1,632.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 96 | 19m | 165 km | 273.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 91 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 87 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 84 | 21m | 244 km | 353.7 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 76 | 27m | 275 km | 360.1 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 75 | 1h 11m | 770 km | 996.3 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 69 | 31m | 369 km | 439.2 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 68 | 45m | 452 km | 530.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 60 | 20m | 250 km | 259.2 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 58 | 20m | 147 km | 146.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 54 | 14m | 154 km | 143.1 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 53 | 13m | 99 km | 90.9 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 52 | 16m | 162 km | 145.8 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 50 | 12m | 15 km | 13.2 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 50 | 1h 20m | 961 km | 828.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 50 | 1h 53m | 1,304 km | 1,124.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N968CC |  | Cape Girardeau Regional Airport (KCGI) | Jonesboro Municipal Airport (KJBR) | 2026-04-15 11:37 UTC | 2026-04-15 12:21 UTC | 43m |
| N758EE |  | Beaufort Executive Airport (KARW) | Marsh Point Airport (SC74) | 2026-04-15 12:17 UTC | 2026-04-15 12:20 UTC | 3m |
| DHYAH | DHY | Bonn-Hangelar Airport (EDKB) | Bonn-Hangelar Airport (EDKB) | 2026-04-15 11:23 UTC | 2026-04-15 12:15 UTC | 51m |
| EPI232 | EPI | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-04-15 11:26 UTC | 2026-04-15 12:05 UTC | 39m |
| N491LP |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-04-15 10:55 UTC | 2026-04-15 12:03 UTC | 1h 7m |
| N358EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-15 10:58 UTC | 2026-04-15 11:57 UTC | 58m |
| FHRMN | FHR | Colmar-Houssen Airport (LFGA) | Nancy-Essey Airport (LFSN) | 2026-04-15 11:17 UTC | 2026-04-15 11:53 UTC | 35m |
| N254EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-15 10:53 UTC | 2026-04-15 11:52 UTC | 58m |
| EWG1 | EWG | Leipzig Halle Airport (EDDP) | Leipzig Halle Airport (EDDP) | 2026-04-15 10:50 UTC | 2026-04-15 11:51 UTC | 1h 1m |
| N24144 |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-04-15 11:23 UTC | 2026-04-15 11:47 UTC | 24m |
| AA9391AB |  | Buochs Airport (LSZC) | Buochs Airport (LSZC) | 2026-04-15 11:34 UTC | 2026-04-15 11:46 UTC | 11m |
| YGQ | YGQ | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-04-15 11:01 UTC | 2026-04-15 11:43 UTC | 42m |
| DRAGO74 | DRA | Sallanches Airport (LFHZ) | Megeve Airport (LFHM) | 2026-04-15 11:26 UTC | 2026-04-15 11:42 UTC | 16m |
| AXM6038 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-15 11:24 UTC | 2026-04-15 11:42 UTC | 18m |
| AAH222 | AAH | Daniel K Inouye International Airport (PHNL) | Kahului Airport (PHOG) | 2026-04-15 11:22 UTC | 2026-04-15 11:41 UTC | 19m |
| N325AT |  | Baton Rouge Metro, Ryan Field (KBTR) | Brookhaven-Lincoln County Airport (K1R7) | 2026-04-15 11:25 UTC | 2026-04-15 11:41 UTC | 15m |
| N107MS |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-15 11:32 UTC | 2026-04-15 11:39 UTC | 7m |
| N5198E |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-04-15 11:02 UTC | 2026-04-15 11:38 UTC | 36m |
| NHZ31 | NHZ | Blackpool International Airport (EGNH) | RAF Woodvale (EGOW) | 2026-04-15 11:21 UTC | 2026-04-15 11:37 UTC | 16m |
| YOX | YOX | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-15 10:40 UTC | 2026-04-15 11:35 UTC | 55m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
