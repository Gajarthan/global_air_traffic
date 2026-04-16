# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_02:29:24_UTC-green)

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

**Latest saved flight:** 2026-04-16 02:29:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-16 02:29:24 UTC

- **36,812** saved flights
- **16,018** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **36,812** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **446,377.1 tonnes** estimated CO2 emissions
- **25,876,933 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1561 |
| 2 | SkyWest Airlines | 1460 |
| 3 | IndiGo | 909 |
| 4 | EJA | 630 |
| 5 | American Airlines | 623 |
| 6 | Southwest Airlines | 517 |
| 7 | ENY | 484 |
| 8 | AXM | 390 |
| 9 | Lufthansa | 383 |
| 10 | LATAM Airlines | 374 |
| 11 | Vueling | 370 |
| 12 | AZU | 327 |
| 13 | All Nippon Airways | 325 |
| 14 | Delta Air Lines | 313 |
| 15 | QLK | 304 |
| 16 | LXJ | 293 |
| 17 | Swiss International | 277 |
| 18 | WIF | 272 |
| 19 | AEE | 247 |
| 20 | Alaska Airlines | 245 |
| 21 | easyJet | 242 |
| 22 | EJU | 238 |
| 23 | VIV | 234 |
| 24 | Japan Airlines | 225 |
| 25 | Air France | 208 |
| 26 | EDV | 206 |
| 27 | United Airlines | 205 |
| 28 | GLO | 196 |
| 29 | JetBlue | 193 |
| 30 | AIQ | 192 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 29007 |
| 2 | 🇮🇳 IN | 2781 |
| 3 | 🇪🇸 ES | 2731 |
| 4 | 🇦🇺 AU | 2579 |
| 5 | 🇧🇷 BR | 2170 |
| 6 | 🇯🇵 JP | 1982 |
| 7 | 🇮🇹 IT | 1951 |
| 8 | 🇩🇪 DE | 1883 |
| 9 | 🇨🇦 CA | 1819 |
| 10 | 🇨🇴 CO | 1813 |
| 11 | 🇬🇧 GB | 1511 |
| 12 | 🇫🇷 FR | 1387 |
| 13 | 🇲🇽 MX | 1157 |
| 14 | 🇬🇷 GR | 1108 |
| 15 | 🇨🇭 CH | 1004 |
| 16 | 🇲🇾 MY | 939 |
| 17 | 🇳🇴 NO | 884 |
| 18 | 🇳🇿 NZ | 780 |
| 19 | 🇿🇦 ZA | 770 |
| 20 | 🇵🇭 PH | 693 |
| 21 | 🇹🇭 TH | 677 |
| 22 | 🇹🇷 TR | 664 |
| 23 | 🇬🇹 GT | 626 |
| 24 | 🇰🇷 KR | 616 |
| 25 | 🇵🇱 PL | 573 |
| 26 | 🇲🇦 MA | 465 |
| 27 | 🇳🇱 NL | 364 |
| 28 | 🇧🇸 BS | 356 |
| 29 | 🇲🇪 ME | 355 |
| 30 | 🇮🇩 ID | 345 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 871 |
| 2 | Tokyo International Airport |  | JP | 673 |
| 3 | El Dorado International Airport |  | CO | 646 |
| 4 | Denver International Airport |  | US | 624 |
| 5 | Indira Gandhi International Airport |  | IN | 597 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 545 |
| 7 | Harry Reid International Airport |  | US | 482 |
| 8 | La Aurora Airport |  | GT | 459 |
| 9 | Guaymaral Airport |  | CO | 458 |
| 10 | Zurich Airport |  | CH | 449 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 372 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 369 |
| 13 | Kuala Lumpur International Airport |  | MY | 365 |
| 14 | Chicago O'Hare International Airport |  | US | 362 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 347 |
| 16 | Frankfurt am Main International Airport |  | DE | 340 |
| 17 | Macau International Airport |  | MO | 337 |
| 18 | Madrid Barajas International Airport |  | ES | 333 |
| 19 | Charlotte/Douglas International Airport |  | US | 329 |
| 20 | Tenerife Norte Airport |  | ES | 325 |
| 21 | Bengaluru International Airport |  | IN | 323 |
| 22 | Congonhas Airport |  | BR | 322 |
| 23 | Ninoy Aquino International Airport |  | PH | 321 |
| 24 | Malpensa International Airport |  | IT | 299 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 287 |
| 26 | Daniel K Inouye International Airport |  | US | 277 |
| 27 | Salt Lake City International Airport |  | US | 277 |
| 28 | Charles de Gaulle International Airport |  | FR | 273 |
| 29 | Capua Airport |  | IT | 262 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 261 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 256 |
| 32 | Reno/Tahoe International Airport |  | US | 255 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 249 |
| 34 | O. R. Tambo International Airport |  | ZA | 248 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 241 |
| 36 | Vitoria/Foronda Airport |  | ES | 241 |
| 37 | Barcelona International Airport |  | ES | 238 |
| 38 | Viracopos International Airport |  | BR | 230 |
| 39 | Don Mueang International Airport |  | TH | 229 |
| 40 | Seattle-Tacoma International Airport |  | US | 227 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 180 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 170 | 1h 8m | 706 km | 2,069.8 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 151 | 14m | 114 km | 296.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 135 | 24m | 225 km | 523.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 105 | 1h 27m | 910 km | 1,647.7 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 98 | 19m | 165 km | 278.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 91 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 88 | 21m | 244 km | 370.5 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 88 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 80 | 27m | 275 km | 379.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 79 | 54m | 546 km | 743.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 79 | 21m | 99 km | 135.3 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 75 | 1h 11m | 770 km | 996.3 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 70 | 31m | 369 km | 445.6 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 69 | 45m | 452 km | 537.8 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 61 | 20m | 147 km | 154.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 56 | 13m | 99 km | 96.0 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 54 | 1h 41m | 1,423 km | 1,325.2 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 53 | 16m | 162 km | 148.6 t |
| 28 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 52 | 26m | 215 km | 192.6 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 52 | 12m | 15 km | 13.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 52 | 1h 21m | 961 km | 861.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BURNY12 | BUR | Danaher Airport (7TX0) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-04-16 02:09 UTC | 2026-04-16 02:29 UTC | 19m |
| AMU825 | AMU | Incheon International Airport (RKSI) | Macau International Airport (VMMC) | 2026-04-15 23:06 UTC | 2026-04-16 02:27 UTC | 3h 21m |
| BTN774 | BTN | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-04-16 01:06 UTC | 2026-04-16 02:21 UTC | 1h 15m |
| LBQ792 | LBQ | Syracuse Hancock International Airport (KSYR) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-04-16 01:58 UTC | 2026-04-16 02:21 UTC | 22m |
| UAE9836 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-15 19:49 UTC | 2026-04-16 02:20 UTC | 6h 31m |
| BURNY05 | BUR | Wichita Valley Airport (KF14) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-04-16 02:00 UTC | 2026-04-16 02:19 UTC | 18m |
| NX673 |  | Taichung Ching Chuang Kang Airport (RCMQ) | Macau International Airport (VMMC) | 2026-04-16 01:08 UTC | 2026-04-16 02:18 UTC | 1h 10m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-04-16 00:49 UTC | 2026-04-16 02:11 UTC | 1h 22m |
| LS18 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-16 00:38 UTC | 2026-04-16 02:01 UTC | 1h 23m |
| PAT11 | PAT | Maryland Airport (K2W5) | Davison Army Air Field (KDAA) | 2026-04-16 01:48 UTC | 2026-04-16 01:58 UTC | 10m |
| BBC491 | BBC | VGZR (VGZR) | Gelephu Airport (VQGP) | 2026-04-16 01:25 UTC | 2026-04-16 01:52 UTC | 27m |
| QLK1971 | QLK | Brisbane International Airport (YBBN) | Albury Airport (YMAY) | 2026-04-15 23:51 UTC | 2026-04-16 01:51 UTC | 2h 0m |
| FLE | FLE | Albury Airport (YMAY) | Albury Airport (YMAY) | 2026-04-16 01:46 UTC | 2026-04-16 01:51 UTC | 5m |
| TCF649 | TCF | Melbourne Orlando International Airport (KMLB) | Palm Beach County Park Airport (KLNA) | 2026-04-16 00:50 UTC | 2026-04-16 01:49 UTC | 58m |
| N872SP |  | Lancaster Airport (KLNS) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-16 01:33 UTC | 2026-04-16 01:48 UTC | 14m |
| AUB1350 | AUB | Auburn University Regional Airport (KAUO) | Auburn University Regional Airport (KAUO) | 2026-04-16 01:25 UTC | 2026-04-16 01:47 UTC | 21m |
| PAT087 | PAT | Upolu Airport (PHUP) | Haiku Airstrip (HI33) | 2026-04-16 00:53 UTC | 2026-04-16 01:46 UTC | 52m |
| RXA2113 | RXA | Perth International Airport (YPPH) | Denmark Airport (YDEK) | 2026-04-16 00:53 UTC | 2026-04-16 01:36 UTC | 43m |
| MERL | MER | Mount Hotham Airport (YHOT) | Yarram Airport (YYRM) | 2026-04-16 01:13 UTC | 2026-04-16 01:36 UTC | 22m |
| AXM6042 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-16 01:10 UTC | 2026-04-16 01:31 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
