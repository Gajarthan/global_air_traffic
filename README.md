# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_18:02:18_UTC-green)

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

**Latest saved flight:** 2026-04-14 18:02:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 18:02:18 UTC

- **34,424** saved flights
- **15,254** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **34,424** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **421,607.9 tonnes** estimated CO2 emissions
- **24,441,039 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1477 |
| 2 | SkyWest Airlines | 1369 |
| 3 | IndiGo | 870 |
| 4 | American Airlines | 590 |
| 5 | EJA | 586 |
| 6 | Southwest Airlines | 491 |
| 7 | ENY | 452 |
| 8 | Lufthansa | 381 |
| 9 | AXM | 363 |
| 10 | Vueling | 351 |
| 11 | LATAM Airlines | 343 |
| 12 | All Nippon Airways | 310 |
| 13 | AZU | 304 |
| 14 | Delta Air Lines | 291 |
| 15 | QLK | 289 |
| 16 | LXJ | 275 |
| 17 | Swiss International | 264 |
| 18 | WIF | 250 |
| 19 | easyJet | 232 |
| 20 | AEE | 231 |
| 21 | Alaska Airlines | 230 |
| 22 | EJU | 230 |
| 23 | VIV | 222 |
| 24 | Japan Airlines | 216 |
| 25 | EDV | 196 |
| 26 | United Airlines | 194 |
| 27 | Air France | 193 |
| 28 | GLO | 187 |
| 29 | Avianca | 182 |
| 30 | JetBlue | 182 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26914 |
| 2 | 🇮🇳 IN | 2660 |
| 3 | 🇪🇸 ES | 2589 |
| 4 | 🇦🇺 AU | 2416 |
| 5 | 🇧🇷 BR | 2023 |
| 6 | 🇯🇵 JP | 1873 |
| 7 | 🇮🇹 IT | 1854 |
| 8 | 🇩🇪 DE | 1772 |
| 9 | 🇨🇴 CO | 1714 |
| 10 | 🇨🇦 CA | 1674 |
| 11 | 🇬🇧 GB | 1421 |
| 12 | 🇫🇷 FR | 1291 |
| 13 | 🇲🇽 MX | 1089 |
| 14 | 🇬🇷 GR | 1026 |
| 15 | 🇨🇭 CH | 957 |
| 16 | 🇲🇾 MY | 877 |
| 17 | 🇳🇴 NO | 813 |
| 18 | 🇿🇦 ZA | 726 |
| 19 | 🇳🇿 NZ | 726 |
| 20 | 🇵🇭 PH | 652 |
| 21 | 🇹🇷 TR | 637 |
| 22 | 🇹🇭 TH | 625 |
| 23 | 🇬🇹 GT | 607 |
| 24 | 🇰🇷 KR | 585 |
| 25 | 🇵🇱 PL | 547 |
| 26 | 🇲🇦 MA | 437 |
| 27 | 🇧🇸 BS | 345 |
| 28 | 🇳🇱 NL | 345 |
| 29 | 🇲🇪 ME | 340 |
| 30 | 🇮🇩 ID | 326 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 812 |
| 2 | Tokyo International Airport |  | JP | 640 |
| 3 | El Dorado International Airport |  | CO | 611 |
| 4 | Denver International Airport |  | US | 575 |
| 5 | Indira Gandhi International Airport |  | IN | 564 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 503 |
| 7 | Harry Reid International Airport |  | US | 452 |
| 8 | La Aurora Airport |  | GT | 444 |
| 9 | Zurich Airport |  | CH | 430 |
| 10 | Guaymaral Airport |  | CO | 423 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 349 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 346 |
| 13 | Chicago O'Hare International Airport |  | US | 344 |
| 14 | Kuala Lumpur International Airport |  | MY | 337 |
| 15 | Frankfurt am Main International Airport |  | DE | 334 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 331 |
| 17 | Macau International Airport |  | MO | 320 |
| 18 | Madrid Barajas International Airport |  | ES | 312 |
| 19 | Charlotte/Douglas International Airport |  | US | 307 |
| 20 | Bengaluru International Airport |  | IN | 307 |
| 21 | Tenerife Norte Airport |  | ES | 303 |
| 22 | Ninoy Aquino International Airport |  | PH | 301 |
| 23 | Congonhas Airport |  | BR | 301 |
| 24 | Malpensa International Airport |  | IT | 282 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 264 |
| 26 | Daniel K Inouye International Airport |  | US | 261 |
| 27 | Salt Lake City International Airport |  | US | 258 |
| 28 | Charles de Gaulle International Airport |  | FR | 257 |
| 29 | Capua Airport |  | IT | 254 |
| 30 | Reno/Tahoe International Airport |  | US | 245 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 241 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 240 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 237 |
| 34 | O. R. Tambo International Airport |  | ZA | 235 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 230 |
| 36 | Vitoria/Foronda Airport |  | ES | 229 |
| 37 | Barcelona International Airport |  | ES | 224 |
| 38 | Miami International Airport |  | US | 214 |
| 39 | Seattle-Tacoma International Airport |  | US | 213 |
| 40 | Viracopos International Airport |  | BR | 211 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 164 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 161 | 1h 8m | 706 km | 1,960.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 141 | 14m | 114 km | 276.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 126 | 24m | 225 km | 488.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 100 | 1h 27m | 910 km | 1,569.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 90 | 19m | 165 km | 256.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 85 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 84 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 78 | 21m | 244 km | 328.4 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 74 | 27m | 275 km | 350.7 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 73 | 1h 12m | 770 km | 969.7 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 66 | 31m | 369 km | 420.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 63 | 45m | 452 km | 491.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 60 | 20m | 250 km | 259.2 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 57 | 20m | 147 km | 144.2 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 53 | 13m | 99 km | 90.9 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 51 | 16m | 162 km | 143.0 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 50 | 12m | 15 km | 13.2 t |
| 28 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 49 | 26m | 215 km | 181.5 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 49 | 14m | 154 km | 129.8 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 48 | 1h 20m | 961 km | 795.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N777ND |  | Santa Barbara Municipal Airport (KSBA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-04-14 17:40 UTC | 2026-04-14 18:02 UTC | 21m |
| BOBCT51 | BOB | Stennis International Airport (KHSA) | Magee Municipal Airport (K17M) | 2026-04-14 17:21 UTC | 2026-04-14 17:58 UTC | 37m |
| CXK153 | CXK | Long Island Mac Arthur Airport (KISP) | K3C8 (K3C8) | 2026-04-14 17:17 UTC | 2026-04-14 17:58 UTC | 40m |
| PATRT15 | PAT | 61MA (61MA) | 61MA (61MA) | 2026-04-14 16:57 UTC | 2026-04-14 17:54 UTC | 57m |
| DEVIL34 | DEV | 2TX3 (2TX3) | Hughes Ranch Airport (50XS) | 2026-04-14 17:34 UTC | 2026-04-14 17:53 UTC | 18m |
| N996PA |  | Mc Clellan-Palomar Airport (KCRQ) | Hemet-Ryan Airport (KHMT) | 2026-04-14 17:25 UTC | 2026-04-14 17:53 UTC | 27m |
| LLN211 | LLN | Perot Field/Fort Worth Alliance Airport (KAFW) | Giles Va Ranch Airport (TS57) | 2026-04-14 17:41 UTC | 2026-04-14 17:51 UTC | 10m |
|  |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-04-14 17:29 UTC | 2026-04-14 17:51 UTC | 21m |
| HTY292 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-04-14 16:51 UTC | 2026-04-14 17:50 UTC | 59m |
| LFA545 | LFA | Orlando Sanford International Airport (KSFB) | FL47 (FL47) | 2026-04-14 16:55 UTC | 2026-04-14 17:45 UTC | 50m |
| OST40 | OST | Stillwater Regional Airport (KSWO) | Tulsa International Airport (KTUL) | 2026-04-14 17:09 UTC | 2026-04-14 17:44 UTC | 35m |
| BRG621 | BRG | Bob Baker Memorial Airport (PAIK) | Ambler Airport (PAFM) | 2026-04-14 17:18 UTC | 2026-04-14 17:43 UTC | 24m |
| N103LU |  | Boca Raton Airport (KBCT) | Palm Beach County Park Airport (KLNA) | 2026-04-14 16:43 UTC | 2026-04-14 17:42 UTC | 58m |
| N717HD |  | Hammond Northshore Regional Airport (KHDC) | Colorado Plains Regional Airport (KAKO) | 2026-04-14 14:52 UTC | 2026-04-14 17:41 UTC | 2h 49m |
| N9957M |  | Longmere Lake Air Strip (AK07) | Longmere Lake Air Strip (AK07) | 2026-04-14 17:39 UTC | 2026-04-14 17:41 UTC | 2m |
| N261AT |  | Mariposa-Yosemite Airport (KMPI) | Truckee-Tahoe Airport (KTRK) | 2026-04-14 16:57 UTC | 2026-04-14 17:41 UTC | 43m |
| N211FD |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-04-14 16:59 UTC | 2026-04-14 17:33 UTC | 33m |
| N5253X |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-04-14 16:45 UTC | 2026-04-14 17:33 UTC | 47m |
| N637AS |  | Mc Clellan-Palomar Airport (KCRQ) | Scottsdale Airport (KSDL) | 2026-04-14 16:37 UTC | 2026-04-14 17:33 UTC | 56m |
| N5218U |  | Asheville Regional Airport (KAVL) | H & J Strip (0NC1) | 2026-04-14 17:06 UTC | 2026-04-14 17:31 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
