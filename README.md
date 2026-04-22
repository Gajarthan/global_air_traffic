# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_15:24:53_UTC-green)

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

**Latest saved flight:** 2026-04-22 15:24:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-22 15:24:53 UTC

- **48,095** saved flights
- **19,550** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **48,095** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **577,347.0 tonnes** estimated CO2 emissions
- **33,469,391 km** total distance flown
- **836 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2049 |
| 2 | SkyWest Airlines | 1849 |
| 3 | IndiGo | 1134 |
| 4 | EJA | 821 |
| 5 | American Airlines | 793 |
| 6 | Southwest Airlines | 681 |
| 7 | ENY | 622 |
| 8 | Lufthansa | 540 |
| 9 | AXM | 481 |
| 10 | Vueling | 479 |
| 11 | LATAM Airlines | 472 |
| 12 | All Nippon Airways | 437 |
| 13 | AZU | 412 |
| 14 | Delta Air Lines | 396 |
| 15 | WIF | 393 |
| 16 | QLK | 386 |
| 17 | LXJ | 371 |
| 18 | Swiss International | 365 |
| 19 | AEE | 326 |
| 20 | Alaska Airlines | 323 |
| 21 | EJU | 318 |
| 22 | easyJet | 308 |
| 23 | VIV | 305 |
| 24 | Japan Airlines | 290 |
| 25 | Air France | 270 |
| 26 | Cathay Pacific | 259 |
| 27 | AXB | 258 |
| 28 | JetBlue | 253 |
| 29 | United Airlines | 251 |
| 30 | AIQ | 244 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 38122 |
| 2 | 🇮🇳 IN | 3538 |
| 3 | 🇪🇸 ES | 3486 |
| 4 | 🇦🇺 AU | 3315 |
| 5 | 🇧🇷 BR | 2817 |
| 6 | 🇯🇵 JP | 2644 |
| 7 | 🇮🇹 IT | 2617 |
| 8 | 🇩🇪 DE | 2529 |
| 9 | 🇨🇦 CA | 2353 |
| 10 | 🇨🇴 CO | 2228 |
| 11 | 🇬🇧 GB | 1993 |
| 12 | 🇫🇷 FR | 1837 |
| 13 | 🇲🇽 MX | 1483 |
| 14 | 🇬🇷 GR | 1470 |
| 15 | 🇨🇭 CH | 1317 |
| 16 | 🇳🇴 NO | 1256 |
| 17 | 🇲🇾 MY | 1176 |
| 18 | 🇿🇦 ZA | 996 |
| 19 | 🇳🇿 NZ | 922 |
| 20 | 🇹🇭 TH | 871 |
| 21 | 🇹🇷 TR | 844 |
| 22 | 🇵🇭 PH | 843 |
| 23 | 🇰🇷 KR | 792 |
| 24 | 🇵🇱 PL | 766 |
| 25 | 🇬🇹 GT | 751 |
| 26 | 🇲🇦 MA | 590 |
| 27 | 🇲🇪 ME | 517 |
| 28 | 🇳🇱 NL | 492 |
| 29 | 🇲🇴 MO | 454 |
| 30 | 🇧🇸 BS | 427 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1125 |
| 2 | Tokyo International Airport |  | JP | 899 |
| 3 | Denver International Airport |  | US | 796 |
| 4 | El Dorado International Airport |  | CO | 772 |
| 5 | Indira Gandhi International Airport |  | IN | 750 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 729 |
| 7 | Guaymaral Airport |  | CO | 629 |
| 8 | Harry Reid International Airport |  | US | 623 |
| 9 | Zurich Airport |  | CH | 566 |
| 10 | La Aurora Airport |  | GT | 558 |
| 11 | Frankfurt am Main International Airport |  | DE | 512 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 477 |
| 13 | Kuala Lumpur International Airport |  | MY | 472 |
| 14 | Chicago O'Hare International Airport |  | US | 471 |
| 15 | Macau International Airport |  | MO | 454 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 454 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 439 |
| 18 | Madrid Barajas International Airport |  | ES | 429 |
| 19 | Bengaluru International Airport |  | IN | 429 |
| 20 | Charlotte/Douglas International Airport |  | US | 412 |
| 21 | Congonhas Airport |  | BR | 404 |
| 22 | Malpensa International Airport |  | IT | 402 |
| 23 | Tenerife Norte Airport |  | ES | 402 |
| 24 | Ninoy Aquino International Airport |  | PH | 390 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 363 |
| 26 | Salt Lake City International Airport |  | US | 360 |
| 27 | Daniel K Inouye International Airport |  | US | 355 |
| 28 | Charles de Gaulle International Airport |  | FR | 355 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 354 |
| 30 | Capua Airport |  | IT | 352 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 331 |
| 32 | Reno/Tahoe International Airport |  | US | 329 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 325 |
| 34 | Vitoria/Foronda Airport |  | ES | 324 |
| 35 | O. R. Tambo International Airport |  | ZA | 320 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 318 |
| 37 | Barcelona International Airport |  | ES | 316 |
| 38 | Don Mueang International Airport |  | TH | 295 |
| 39 | Viracopos International Airport |  | BR | 286 |
| 40 | Calgary International Airport |  | CA | 284 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 252 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 228 | 1h 7m | 706 km | 2,775.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 184 | 14m | 114 km | 360.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 167 | 24m | 225 km | 647.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 143 | 28m | 304 km | 749.6 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 140 | 21m | 244 km | 589.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 139 | 1h 27m | 910 km | 2,181.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 128 | 19m | 165 km | 364.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 116 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 111 | 26m | 275 km | 526.0 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 100 | 54m | 546 km | 941.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 99 | 44m | 452 km | 771.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 83 | 31m | 369 km | 528.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 81 | 20m | 250 km | 349.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 78 | 20m | 147 km | 197.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 76 | 26m | 215 km | 281.5 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 68 | 1h 42m | 1,156 km | 1,356.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 68 | 1h 0m | 695 km | 815.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OYPTR | OYP | Kolding Vamdrup Airport (EKVD) | Kolding Vamdrup Airport (EKVD) | 2026-04-22 13:39 UTC | 2026-04-22 15:24 UTC | 1h 45m |
| UFX62 | UFX | Humberside Airport (EGNJ) | Skegness (Ingoldmells) Aerodrome (EGNI) | 2026-04-22 14:26 UTC | 2026-04-22 15:20 UTC | 54m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-22 14:56 UTC | 2026-04-22 15:14 UTC | 18m |
| N12713 |  | Clearwater Executive Airport (KCLW) | Clearwater Executive Airport (KCLW) | 2026-04-22 14:18 UTC | 2026-04-22 15:10 UTC | 52m |
| N222SP |  | Avi Suquilla Airport (KP20) | Avi Suquilla Airport (KP20) | 2026-04-22 15:06 UTC | 2026-04-22 15:09 UTC | 2m |
| N214EL |  | Falcon Field (KFFZ) | Glendale Regional Airport (KGEU) | 2026-04-22 14:45 UTC | 2026-04-22 15:08 UTC | 22m |
| NHZ31 | NHZ | Blackpool International Airport (EGNH) | RAF Woodvale (EGOW) | 2026-04-22 14:56 UTC | 2026-04-22 15:07 UTC | 11m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-22 14:09 UTC | 2026-04-22 15:07 UTC | 58m |
| N787RP |  | Falcon Field (KFFZ) | Prescott Regional/Ernest A Love Field (KPRC) | 2026-04-22 14:15 UTC | 2026-04-22 15:05 UTC | 50m |
| AIC4BK | Air India | Indira Gandhi International Airport (VIDP) | Sarsawa Air Force Station (VISP) | 2026-04-22 14:47 UTC | 2026-04-22 15:04 UTC | 17m |
| 5YSLP |  | Nairobi Wilson Airport (HKNW) | Moi Air Base (HKRE) | 2026-04-22 14:18 UTC | 2026-04-22 14:56 UTC | 37m |
| N65112 |  | MY42 (MY42) | MY42 (MY42) | 2026-04-22 14:45 UTC | 2026-04-22 14:56 UTC | 11m |
| N881AC |  | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-04-22 14:36 UTC | 2026-04-22 14:54 UTC | 17m |
| MTN8310 | MTN | Newark Liberty International Airport (KEWR) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-22 13:34 UTC | 2026-04-22 14:53 UTC | 1h 19m |
| SMGLR44 | SMG | Kbely Air Base (LKKB) | Kbely Air Base (LKKB) | 2026-04-22 13:49 UTC | 2026-04-22 14:53 UTC | 1h 4m |
| N285ME |  | Witham Field (KSUA) | Peter O Knight Airport (KTPF) | 2026-04-22 13:58 UTC | 2026-04-22 14:53 UTC | 55m |
| HKS40 | HKS | Beccles Airport (EGSM) | Norwich International Airport (EGSH) | 2026-04-22 14:23 UTC | 2026-04-22 14:50 UTC | 27m |
| RYR9DA | Ryanair | Václav Havel Airport (LKPR) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-22 14:02 UTC | 2026-04-22 14:50 UTC | 47m |
| N739ZU |  | Melbourne Orlando International Airport (KMLB) | Melbourne Orlando International Airport (KMLB) | 2026-04-22 14:44 UTC | 2026-04-22 14:49 UTC | 5m |
| N261DC |  | Henderson Executive Airport (KHND) | Willow Springs Ranch Airport (1AZ8) | 2026-04-22 14:34 UTC | 2026-04-22 14:47 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
