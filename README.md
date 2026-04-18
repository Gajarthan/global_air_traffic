# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_21:03:32_UTC-green)

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

**Latest saved flight:** 2026-04-18 21:03:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 21:03:32 UTC

- **42,065** saved flights
- **17,728** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **42,065** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **505,536.2 tonnes** estimated CO2 emissions
- **29,306,448 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1766 |
| 2 | SkyWest Airlines | 1641 |
| 3 | IndiGo | 1027 |
| 4 | EJA | 728 |
| 5 | American Airlines | 698 |
| 6 | Southwest Airlines | 594 |
| 7 | ENY | 542 |
| 8 | AXM | 434 |
| 9 | Vueling | 422 |
| 10 | LATAM Airlines | 419 |
| 11 | Lufthansa | 414 |
| 12 | All Nippon Airways | 377 |
| 13 | AZU | 375 |
| 14 | Delta Air Lines | 359 |
| 15 | QLK | 341 |
| 16 | LXJ | 331 |
| 17 | Swiss International | 324 |
| 18 | WIF | 324 |
| 19 | Alaska Airlines | 285 |
| 20 | AEE | 282 |
| 21 | EJU | 277 |
| 22 | easyJet | 272 |
| 23 | VIV | 269 |
| 24 | Japan Airlines | 257 |
| 25 | Air France | 236 |
| 26 | United Airlines | 229 |
| 27 | JetBlue | 226 |
| 28 | GLO | 224 |
| 29 | AXB | 220 |
| 30 | EDV | 219 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33337 |
| 2 | 🇮🇳 IN | 3144 |
| 3 | 🇪🇸 ES | 3095 |
| 4 | 🇦🇺 AU | 2920 |
| 5 | 🇧🇷 BR | 2527 |
| 6 | 🇯🇵 JP | 2291 |
| 7 | 🇮🇹 IT | 2186 |
| 8 | 🇩🇪 DE | 2127 |
| 9 | 🇨🇦 CA | 2056 |
| 10 | 🇨🇴 CO | 1971 |
| 11 | 🇬🇧 GB | 1709 |
| 12 | 🇫🇷 FR | 1618 |
| 13 | 🇲🇽 MX | 1325 |
| 14 | 🇬🇷 GR | 1276 |
| 15 | 🇨🇭 CH | 1178 |
| 16 | 🇲🇾 MY | 1053 |
| 17 | 🇳🇴 NO | 1034 |
| 18 | 🇿🇦 ZA | 869 |
| 19 | 🇳🇿 NZ | 844 |
| 20 | 🇵🇭 PH | 756 |
| 21 | 🇹🇭 TH | 742 |
| 22 | 🇹🇷 TR | 732 |
| 23 | 🇬🇹 GT | 705 |
| 24 | 🇰🇷 KR | 687 |
| 25 | 🇵🇱 PL | 664 |
| 26 | 🇲🇦 MA | 522 |
| 27 | 🇳🇱 NL | 432 |
| 28 | 🇲🇪 ME | 429 |
| 29 | 🇧🇸 BS | 396 |
| 30 | 🇮🇩 ID | 380 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 977 |
| 2 | Tokyo International Airport |  | JP | 783 |
| 3 | Denver International Airport |  | US | 701 |
| 4 | El Dorado International Airport |  | CO | 689 |
| 5 | Indira Gandhi International Airport |  | IN | 678 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 632 |
| 7 | Harry Reid International Airport |  | US | 543 |
| 8 | Guaymaral Airport |  | CO | 533 |
| 9 | La Aurora Airport |  | GT | 520 |
| 10 | Zurich Airport |  | CH | 507 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 419 |
| 12 | Kuala Lumpur International Airport |  | MY | 415 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 409 |
| 14 | Chicago O'Hare International Airport |  | US | 406 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 394 |
| 16 | Frankfurt am Main International Airport |  | DE | 383 |
| 17 | Madrid Barajas International Airport |  | ES | 379 |
| 18 | Macau International Airport |  | MO | 377 |
| 19 | Bengaluru International Airport |  | IN | 370 |
| 20 | Tenerife Norte Airport |  | ES | 368 |
| 21 | Charlotte/Douglas International Airport |  | US | 365 |
| 22 | Congonhas Airport |  | BR | 365 |
| 23 | Ninoy Aquino International Airport |  | PH | 351 |
| 24 | Malpensa International Airport |  | IT | 341 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 325 |
| 26 | Salt Lake City International Airport |  | US | 323 |
| 27 | Daniel K Inouye International Airport |  | US | 314 |
| 28 | Charles de Gaulle International Airport |  | FR | 306 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 305 |
| 30 | Vitoria/Foronda Airport |  | ES | 299 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 294 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 289 |
| 33 | Reno/Tahoe International Airport |  | US | 289 |
| 34 | O. R. Tambo International Airport |  | ZA | 282 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 282 |
| 36 | Capua Airport |  | IT | 282 |
| 37 | Barcelona International Airport |  | ES | 268 |
| 38 | Viracopos International Airport |  | BR | 259 |
| 39 | Calgary International Airport |  | CA | 253 |
| 40 | Miami International Airport |  | US | 249 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 214 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 196 | 1h 7m | 706 km | 2,386.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 150 | 24m | 225 km | 581.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 124 | 28m | 304 km | 650.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 121 | 1h 27m | 910 km | 1,898.8 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 115 | 21m | 244 km | 484.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 112 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 112 | 19m | 165 km | 318.6 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 105 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 91 | 54m | 546 km | 856.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 88 | 21m | 99 km | 150.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 85 | 44m | 452 km | 662.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 82 | 1h 11m | 770 km | 1,089.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 75 | 31m | 369 km | 477.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 70 | 20m | 250 km | 302.4 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 68 | 52m | 556 km | 651.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 66 | 20m | 147 km | 167.0 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 59 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 28 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 58 | 1h 21m | 961 km | 961.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 57 | 14m | 154 km | 151.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGXAR | CGX | Calgary / Springbank Airport (CYBW) | Pincher Creek Airport (CZPC) | 2026-04-18 20:12 UTC | 2026-04-18 21:03 UTC | 51m |
| N9895Q |  | Harford County Airport (K0W3) | York Airport (KTHV) | 2026-04-18 20:38 UTC | 2026-04-18 20:59 UTC | 21m |
| DLH5EE | Lufthansa | Munich International Airport (EDDM) | Nida Airport (EYND) | 2026-04-18 19:34 UTC | 2026-04-18 20:58 UTC | 1h 24m |
| N898BR |  | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | Las Cruces International Airport (KLRU) | 2026-04-18 20:25 UTC | 2026-04-18 20:57 UTC | 32m |
| ZMV | ZMV | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-04-18 20:39 UTC | 2026-04-18 20:55 UTC | 16m |
| STAR7 | STA | Morden Airport (CJA3) | Winnipeg James Armstrong Richardson International Airport (CYWG) | 2026-04-18 20:10 UTC | 2026-04-18 20:40 UTC | 30m |
| N29GB |  | Double Eagle Ii Airport (KAEG) | Double Eagle Ii Airport (KAEG) | 2026-04-18 20:22 UTC | 2026-04-18 20:39 UTC | 16m |
| N218BJ |  | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-04-18 19:59 UTC | 2026-04-18 20:37 UTC | 38m |
| XBHCG | XBH | General Abelardo L. Rodriguez International Airport (MMTJ) | General Abelardo L. Rodriguez International Airport (MMTJ) | 2026-04-18 20:21 UTC | 2026-04-18 20:37 UTC | 15m |
| N20MB |  | Boise Air Trml/Gowen Field (KBOI) | Deer Creek Airport (95ID) | 2026-04-18 19:58 UTC | 2026-04-18 20:37 UTC | 38m |
| N9536M |  | La Crosse Regional Airport (KLSE) | Iowa City Municipal Airport (KIOW) | 2026-04-18 19:41 UTC | 2026-04-18 20:36 UTC | 54m |
| N74KM |  | Mc Allen International Airport (KMFE) | 12TE (12TE) | 2026-04-18 19:44 UTC | 2026-04-18 20:35 UTC | 51m |
| RNGR751 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-04-18 20:07 UTC | 2026-04-18 20:32 UTC | 24m |
| N545GC |  | Lompoc Airport (KLPC) | Lompoc Airport (KLPC) | 2026-04-18 20:11 UTC | 2026-04-18 20:32 UTC | 20m |
| PRJOS | PRJ | Tatui Airport (SDTF) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-18 19:45 UTC | 2026-04-18 20:29 UTC | 44m |
| N35121 |  | Olympia Regional Airport (KOLM) | Jim & Julie's Airport (96WA) | 2026-04-18 19:48 UTC | 2026-04-18 20:29 UTC | 40m |
| N856BB |  | Tulsa International Airport (KTUL) | Heifer Creek Ranch Airport (16AR) | 2026-04-18 20:01 UTC | 2026-04-18 20:28 UTC | 27m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-18 19:45 UTC | 2026-04-18 20:27 UTC | 41m |
| N929SG |  | Lubbock Preston Smith International Airport (KLBB) | Dyess Afb Airport (KDYS) | 2026-04-18 19:59 UTC | 2026-04-18 20:26 UTC | 27m |
| N24998 |  | Oakland San Francisco Bay Airport (KOAK) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-18 19:50 UTC | 2026-04-18 20:22 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
