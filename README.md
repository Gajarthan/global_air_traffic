# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_14:57:43_UTC-green)

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

**Latest saved flight:** 2026-04-17 14:57:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 14:57:43 UTC

- **39,084** saved flights
- **16,763** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **39,084** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **472,499.2 tonnes** estimated CO2 emissions
- **27,391,257 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1648 |
| 2 | SkyWest Airlines | 1513 |
| 3 | IndiGo | 969 |
| 4 | EJA | 669 |
| 5 | American Airlines | 652 |
| 6 | Southwest Airlines | 538 |
| 7 | ENY | 500 |
| 8 | AXM | 413 |
| 9 | Vueling | 394 |
| 10 | LATAM Airlines | 390 |
| 11 | Lufthansa | 385 |
| 12 | All Nippon Airways | 351 |
| 13 | AZU | 346 |
| 14 | Delta Air Lines | 327 |
| 15 | QLK | 327 |
| 16 | LXJ | 310 |
| 17 | WIF | 307 |
| 18 | Swiss International | 295 |
| 19 | AEE | 260 |
| 20 | Alaska Airlines | 258 |
| 21 | easyJet | 258 |
| 22 | EJU | 254 |
| 23 | VIV | 246 |
| 24 | Japan Airlines | 238 |
| 25 | Air France | 220 |
| 26 | United Airlines | 213 |
| 27 | EDV | 212 |
| 28 | AIQ | 202 |
| 29 | GLO | 202 |
| 30 | AXB | 201 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 30661 |
| 2 | 🇮🇳 IN | 2956 |
| 3 | 🇪🇸 ES | 2913 |
| 4 | 🇦🇺 AU | 2785 |
| 5 | 🇧🇷 BR | 2291 |
| 6 | 🇯🇵 JP | 2129 |
| 7 | 🇮🇹 IT | 2050 |
| 8 | 🇩🇪 DE | 1989 |
| 9 | 🇨🇦 CA | 1914 |
| 10 | 🇨🇴 CO | 1901 |
| 11 | 🇬🇧 GB | 1611 |
| 12 | 🇫🇷 FR | 1491 |
| 13 | 🇲🇽 MX | 1219 |
| 14 | 🇬🇷 GR | 1178 |
| 15 | 🇨🇭 CH | 1075 |
| 16 | 🇲🇾 MY | 1003 |
| 17 | 🇳🇴 NO | 978 |
| 18 | 🇿🇦 ZA | 821 |
| 19 | 🇳🇿 NZ | 811 |
| 20 | 🇵🇭 PH | 722 |
| 21 | 🇹🇭 TH | 715 |
| 22 | 🇹🇷 TR | 694 |
| 23 | 🇬🇹 GT | 659 |
| 24 | 🇰🇷 KR | 641 |
| 25 | 🇵🇱 PL | 612 |
| 26 | 🇲🇦 MA | 485 |
| 27 | 🇳🇱 NL | 397 |
| 28 | 🇲🇪 ME | 388 |
| 29 | 🇧🇸 BS | 377 |
| 30 | 🇮🇩 ID | 365 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 905 |
| 2 | Tokyo International Airport |  | JP | 728 |
| 3 | El Dorado International Airport |  | CO | 670 |
| 4 | Denver International Airport |  | US | 650 |
| 5 | Indira Gandhi International Airport |  | IN | 637 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 585 |
| 7 | Harry Reid International Airport |  | US | 508 |
| 8 | Guaymaral Airport |  | CO | 496 |
| 9 | La Aurora Airport |  | GT | 484 |
| 10 | Zurich Airport |  | CH | 470 |
| 11 | Kuala Lumpur International Airport |  | MY | 394 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 383 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 381 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 379 |
| 15 | Chicago O'Hare International Airport |  | US | 377 |
| 16 | Macau International Airport |  | MO | 362 |
| 17 | Tenerife Norte Airport |  | ES | 354 |
| 18 | Madrid Barajas International Airport |  | ES | 353 |
| 19 | Frankfurt am Main International Airport |  | DE | 349 |
| 20 | Charlotte/Douglas International Airport |  | US | 347 |
| 21 | Bengaluru International Airport |  | IN | 343 |
| 22 | Congonhas Airport |  | BR | 339 |
| 23 | Ninoy Aquino International Airport |  | PH | 335 |
| 24 | Malpensa International Airport |  | IT | 318 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 302 |
| 26 | Salt Lake City International Airport |  | US | 293 |
| 27 | Daniel K Inouye International Airport |  | US | 290 |
| 28 | Charles de Gaulle International Airport |  | FR | 287 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 285 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 273 |
| 31 | Vitoria/Foronda Airport |  | ES | 268 |
| 32 | O. R. Tambo International Airport |  | ZA | 263 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 263 |
| 34 | Capua Airport |  | IT | 263 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 258 |
| 36 | Reno/Tahoe International Airport |  | US | 258 |
| 37 | Barcelona International Airport |  | ES | 254 |
| 38 | Don Mueang International Airport |  | TH | 239 |
| 39 | Viracopos International Airport |  | BR | 238 |
| 40 | Calgary International Airport |  | CA | 233 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 198 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 183 | 1h 8m | 706 km | 2,228.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 157 | 14m | 114 km | 307.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 114 | 28m | 304 km | 597.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 105 | 19m | 165 km | 298.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 101 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 99 | 21m | 244 km | 416.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 96 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 90 | 26m | 275 km | 426.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 82 | 21m | 99 km | 140.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 77 | 45m | 452 km | 600.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 72 | 31m | 369 km | 458.3 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 60 | 1h 41m | 1,423 km | 1,472.5 t |
| 23 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 59 | 26m | 215 km | 218.5 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 59 | 13m | 99 km | 101.2 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 59 | 16m | 162 km | 165.4 t |
| 26 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 55 | 1h 53m | 1,304 km | 1,237.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 54 | 1h 21m | 961 km | 895.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N169BA |  | Bb Airpark (TE88) | TE77 (TE77) | 2026-04-17 14:47 UTC | 2026-04-17 14:57 UTC | 10m |
| WMN711 | WMN | Easton/Newnam Field (KESN) | Harrisburg International Airport (KMDT) | 2026-04-17 14:25 UTC | 2026-04-17 14:51 UTC | 25m |
| JINX31 | JIN | Randolph Afb Airport (KRND) | Tee Pee Creek Airport (8TE0) | 2026-04-17 14:15 UTC | 2026-04-17 14:48 UTC | 32m |
| HKS51 | HKS | Humberside Airport (EGNJ) | EGYO (EGYO) | 2026-04-17 14:23 UTC | 2026-04-17 14:48 UTC | 24m |
| N540DB |  | Luis Munoz Marin International Airport (TJSJ) | Fernando Luis Ribas Dominicci Airport (TJIG) | 2026-04-17 14:43 UTC | 2026-04-17 14:46 UTC | 3m |
| VLG8QU | Vueling | Barcelona International Airport (LEBL) | A Coruna Airport (LECO) | 2026-04-17 13:15 UTC | 2026-04-17 14:46 UTC | 1h 30m |
| DAWG11 | DAW | Savannah/Hilton Head International Airport (KSAV) | Savannah/Hilton Head International Airport (KSAV) | 2026-04-17 14:00 UTC | 2026-04-17 14:45 UTC | 44m |
| N734NA |  | Malone Airport (NJ61) | Malone Airport (NJ61) | 2026-04-17 14:33 UTC | 2026-04-17 14:43 UTC | 9m |
| N736PB |  | Double Eagle Ii Airport (KAEG) | NM74 (NM74) | 2026-04-17 14:16 UTC | 2026-04-17 14:41 UTC | 24m |
| N186QS |  | Tokyo International Airport (RJTT) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-17 02:55 UTC | 2026-04-17 14:39 UTC | 11h 43m |
| N8024Q |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-17 13:52 UTC | 2026-04-17 14:39 UTC | 46m |
| EJA434 | EJA | Columbus Airport (KCSG) | Tweed/New Haven Airport (KHVN) | 2026-04-17 12:28 UTC | 2026-04-17 14:35 UTC | 2h 7m |
| RPA5698 | Republic Airways | Ronald Reagan Washington Ntl Airport (KDCA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-17 13:33 UTC | 2026-04-17 14:32 UTC | 59m |
| TRF553 | TRF | Addison Airport (KADS) | Mesquite Metro Airport (KHQZ) | 2026-04-17 13:33 UTC | 2026-04-17 14:28 UTC | 54m |
| PPSCN | PPS | Santos Dumont Airport (SBRJ) | Pindamonhangaba Airport (SDPD) | 2026-04-17 12:44 UTC | 2026-04-17 14:26 UTC | 1h 42m |
| GPD435 | GPD | Sarasota/Bradenton International Airport (KSRQ) | Merritt Island Airport (KCOI) | 2026-04-17 13:50 UTC | 2026-04-17 14:25 UTC | 35m |
| N144C |  | Cecil Ranch Airport (37CN) | NV13 (NV13) | 2026-04-17 13:46 UTC | 2026-04-17 14:21 UTC | 35m |
| AAL1894 | American Airlines | Miami International Airport (KMIA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-17 11:37 UTC | 2026-04-17 14:19 UTC | 2h 42m |
| GAO304 | GAO | Sir Grantley Adams International Airport (TBPB) | Point Salines International Airport (TGPY) | 2026-04-17 13:53 UTC | 2026-04-17 14:18 UTC | 25m |
| WIF7DT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-17 14:07 UTC | 2026-04-17 14:17 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
