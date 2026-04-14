# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_16:42:43_UTC-green)

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

**Latest saved flight:** 2026-04-14 16:42:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 16:42:43 UTC

- **34,271** saved flights
- **15,189** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **34,271** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **420,266.4 tonnes** estimated CO2 emissions
- **24,363,271 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1471 |
| 2 | SkyWest Airlines | 1360 |
| 3 | IndiGo | 869 |
| 4 | American Airlines | 586 |
| 5 | EJA | 578 |
| 6 | Southwest Airlines | 489 |
| 7 | ENY | 451 |
| 8 | Lufthansa | 381 |
| 9 | AXM | 363 |
| 10 | Vueling | 350 |
| 11 | LATAM Airlines | 343 |
| 12 | All Nippon Airways | 310 |
| 13 | AZU | 303 |
| 14 | Delta Air Lines | 289 |
| 15 | QLK | 289 |
| 16 | LXJ | 274 |
| 17 | Swiss International | 263 |
| 18 | WIF | 250 |
| 19 | AEE | 231 |
| 20 | easyJet | 230 |
| 21 | Alaska Airlines | 228 |
| 22 | EJU | 228 |
| 23 | VIV | 222 |
| 24 | Japan Airlines | 216 |
| 25 | EDV | 195 |
| 26 | United Airlines | 194 |
| 27 | Air France | 192 |
| 28 | GLO | 184 |
| 29 | Avianca | 182 |
| 30 | JetBlue | 181 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26749 |
| 2 | 🇮🇳 IN | 2658 |
| 3 | 🇪🇸 ES | 2578 |
| 4 | 🇦🇺 AU | 2416 |
| 5 | 🇧🇷 BR | 2015 |
| 6 | 🇯🇵 JP | 1873 |
| 7 | 🇮🇹 IT | 1847 |
| 8 | 🇩🇪 DE | 1766 |
| 9 | 🇨🇴 CO | 1706 |
| 10 | 🇨🇦 CA | 1668 |
| 11 | 🇬🇧 GB | 1412 |
| 12 | 🇫🇷 FR | 1284 |
| 13 | 🇲🇽 MX | 1084 |
| 14 | 🇬🇷 GR | 1023 |
| 15 | 🇨🇭 CH | 955 |
| 16 | 🇲🇾 MY | 877 |
| 17 | 🇳🇴 NO | 807 |
| 18 | 🇳🇿 NZ | 726 |
| 19 | 🇿🇦 ZA | 724 |
| 20 | 🇵🇭 PH | 652 |
| 21 | 🇹🇷 TR | 635 |
| 22 | 🇹🇭 TH | 625 |
| 23 | 🇬🇹 GT | 603 |
| 24 | 🇰🇷 KR | 585 |
| 25 | 🇵🇱 PL | 544 |
| 26 | 🇲🇦 MA | 436 |
| 27 | 🇳🇱 NL | 345 |
| 28 | 🇧🇸 BS | 343 |
| 29 | 🇲🇪 ME | 339 |
| 30 | 🇮🇩 ID | 326 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 808 |
| 2 | Tokyo International Airport |  | JP | 640 |
| 3 | El Dorado International Airport |  | CO | 611 |
| 4 | Denver International Airport |  | US | 573 |
| 5 | Indira Gandhi International Airport |  | IN | 564 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 501 |
| 7 | Harry Reid International Airport |  | US | 452 |
| 8 | La Aurora Airport |  | GT | 440 |
| 9 | Zurich Airport |  | CH | 428 |
| 10 | Guaymaral Airport |  | CO | 416 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 343 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 343 |
| 13 | Chicago O'Hare International Airport |  | US | 343 |
| 14 | Kuala Lumpur International Airport |  | MY | 337 |
| 15 | Frankfurt am Main International Airport |  | DE | 334 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 331 |
| 17 | Macau International Airport |  | MO | 320 |
| 18 | Madrid Barajas International Airport |  | ES | 311 |
| 19 | Charlotte/Douglas International Airport |  | US | 306 |
| 20 | Bengaluru International Airport |  | IN | 306 |
| 21 | Ninoy Aquino International Airport |  | PH | 301 |
| 22 | Tenerife Norte Airport |  | ES | 301 |
| 23 | Congonhas Airport |  | BR | 299 |
| 24 | Malpensa International Airport |  | IT | 282 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 262 |
| 26 | Daniel K Inouye International Airport |  | US | 260 |
| 27 | Salt Lake City International Airport |  | US | 257 |
| 28 | Charles de Gaulle International Airport |  | FR | 256 |
| 29 | Capua Airport |  | IT | 250 |
| 30 | Reno/Tahoe International Airport |  | US | 243 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 241 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 240 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 236 |
| 34 | O. R. Tambo International Airport |  | ZA | 234 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 230 |
| 36 | Vitoria/Foronda Airport |  | ES | 228 |
| 37 | Barcelona International Airport |  | ES | 223 |
| 38 | Miami International Airport |  | US | 214 |
| 39 | Seattle-Tacoma International Airport |  | US | 212 |
| 40 | Viracopos International Airport |  | BR | 211 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 161 | 1h 8m | 706 km | 1,960.2 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 161 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 141 | 14m | 114 km | 276.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 126 | 24m | 225 km | 488.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 100 | 1h 27m | 910 km | 1,569.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 90 | 19m | 165 km | 256.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 85 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 82 | 9m | - | - |
| 10 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 77 | 21m | 244 km | 324.2 t |
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
| DFIRE | DFI | Dusseldorf International Airport (EDDL) | Stuttgart Airport (EDDS) | 2026-04-14 15:53 UTC | 2026-04-14 16:42 UTC | 48m |
| TCF612 | TCF | Melbourne Orlando International Airport (KMLB) | Valkaria Airport (KX59) | 2026-04-14 16:26 UTC | 2026-04-14 16:41 UTC | 14m |
| N54PV |  | Long Beach (Daugherty Field) Airport (KLGB) | Riverside Airport (KRAL) | 2026-04-14 16:15 UTC | 2026-04-14 16:35 UTC | 20m |
| LOGO1 | LOG | Randolph Afb Airport (KRND) | South Texas Regional At Hondo Airport (KHDO) | 2026-04-14 16:03 UTC | 2026-04-14 16:33 UTC | 30m |
| ABK202 | ABK | Montréal (Mirabel) Airport (CYMX) | Montréal (Mirabel) Airport (CYMX) | 2026-04-14 15:26 UTC | 2026-04-14 16:32 UTC | 1h 5m |
| N73784 |  | 27XA (27XA) | Flying D Ranch Airport (TX94) | 2026-04-14 16:02 UTC | 2026-04-14 16:31 UTC | 29m |
| KAP1237 | KAP | Long Island Mac Arthur Airport (KISP) | Francis S Gabreski Airport (KFOK) | 2026-04-14 15:49 UTC | 2026-04-14 16:29 UTC | 40m |
| BOE704 | BOE | Seattle Paine Field International Airport (KPAE) | Basin City Airfield (97WA) | 2026-04-14 15:22 UTC | 2026-04-14 16:27 UTC | 1h 4m |
| TEXN094 | TEX | J-22 Ranch Airport (16FL) | Flomaton Airport (0AL5) | 2026-04-14 15:57 UTC | 2026-04-14 16:26 UTC | 29m |
| PSOMH | PSO | Leite Lopes Airport (SBRP) | Fazenda Mata Velha Airport (SIMV) | 2026-04-14 16:09 UTC | 2026-04-14 16:25 UTC | 15m |
| N321WA |  | Nantucket Memorial Airport (KACK) | Laurence G Hanscom Field (KBED) | 2026-04-14 15:55 UTC | 2026-04-14 16:25 UTC | 29m |
| N63FS |  | Clark Regional Airport (KJVY) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-04-14 15:38 UTC | 2026-04-14 16:23 UTC | 44m |
| N336MA |  | Orlando Apopka Airport (KX04) | Orlando Apopka Airport (KX04) | 2026-04-14 15:28 UTC | 2026-04-14 16:22 UTC | 54m |
| PHSVD | PHS | Eelde Airport (EHGG) | Eelde Airport (EHGG) | 2026-04-14 15:22 UTC | 2026-04-14 16:22 UTC | 1h 0m |
| ARCAS15 | ARC | Danaher Airport (7TX0) | Arledge Field (KF56) | 2026-04-14 16:09 UTC | 2026-04-14 16:22 UTC | 12m |
| COBRA57 | COB | 91CL (91CL) | Boron Airstrip (57CL) | 2026-04-14 16:08 UTC | 2026-04-14 16:21 UTC | 12m |
| N3011B |  | Chester County G O Carlson Airport (KMQS) | Lancaster Airport (KLNS) | 2026-04-14 14:44 UTC | 2026-04-14 16:20 UTC | 1h 35m |
| N44BY |  | Ja Field (SC58) | WV10 (WV10) | 2026-04-14 15:36 UTC | 2026-04-14 16:16 UTC | 40m |
| N99FF |  | Nanaimo Airport (CYCD) | Boeing Field/King County International Airport (KBFI) | 2026-04-14 15:52 UTC | 2026-04-14 16:16 UTC | 23m |
| N647SP |  | Elizabeth City Cg Air Station/Regional Airport (KECG) | Currituck County Regional Airport (KONX) | 2026-04-14 15:45 UTC | 2026-04-14 16:15 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
