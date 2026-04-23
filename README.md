# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_10:36:41_UTC-green)

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

**Latest saved flight:** 2026-04-23 10:36:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-23 10:36:41 UTC

- **49,497** saved flights
- **19,992** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **49,497** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **591,296.2 tonnes** estimated CO2 emissions
- **34,278,038 km** total distance flown
- **832 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2095 |
| 2 | SkyWest Airlines | 1899 |
| 3 | IndiGo | 1160 |
| 4 | EJA | 852 |
| 5 | American Airlines | 810 |
| 6 | Southwest Airlines | 703 |
| 7 | ENY | 639 |
| 8 | Lufthansa | 568 |
| 9 | AXM | 493 |
| 10 | Vueling | 491 |
| 11 | LATAM Airlines | 482 |
| 12 | All Nippon Airways | 451 |
| 13 | AZU | 422 |
| 14 | WIF | 412 |
| 15 | Delta Air Lines | 406 |
| 16 | QLK | 404 |
| 17 | LXJ | 377 |
| 18 | Swiss International | 374 |
| 19 | AEE | 336 |
| 20 | Alaska Airlines | 330 |
| 21 | EJU | 320 |
| 22 | easyJet | 314 |
| 23 | VIV | 312 |
| 24 | Japan Airlines | 298 |
| 25 | Air France | 280 |
| 26 | AXB | 265 |
| 27 | Cathay Pacific | 259 |
| 28 | United Airlines | 258 |
| 29 | JetBlue | 257 |
| 30 | AIQ | 254 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 39242 |
| 2 | 🇮🇳 IN | 3638 |
| 3 | 🇪🇸 ES | 3580 |
| 4 | 🇦🇺 AU | 3465 |
| 5 | 🇧🇷 BR | 2874 |
| 6 | 🇯🇵 JP | 2725 |
| 7 | 🇮🇹 IT | 2665 |
| 8 | 🇩🇪 DE | 2621 |
| 9 | 🇨🇦 CA | 2456 |
| 10 | 🇨🇴 CO | 2289 |
| 11 | 🇬🇧 GB | 2038 |
| 12 | 🇫🇷 FR | 1882 |
| 13 | 🇲🇽 MX | 1528 |
| 14 | 🇬🇷 GR | 1507 |
| 15 | 🇨🇭 CH | 1362 |
| 16 | 🇳🇴 NO | 1318 |
| 17 | 🇲🇾 MY | 1201 |
| 18 | 🇿🇦 ZA | 1014 |
| 19 | 🇳🇿 NZ | 956 |
| 20 | 🇹🇭 TH | 905 |
| 21 | 🇹🇷 TR | 870 |
| 22 | 🇵🇭 PH | 867 |
| 23 | 🇰🇷 KR | 820 |
| 24 | 🇵🇱 PL | 791 |
| 25 | 🇬🇹 GT | 759 |
| 26 | 🇲🇦 MA | 603 |
| 27 | 🇲🇪 ME | 527 |
| 28 | 🇳🇱 NL | 503 |
| 29 | 🇲🇴 MO | 457 |
| 30 | 🇧🇸 BS | 437 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1156 |
| 2 | Tokyo International Airport |  | JP | 925 |
| 3 | Denver International Airport |  | US | 822 |
| 4 | El Dorado International Airport |  | CO | 787 |
| 5 | Indira Gandhi International Airport |  | IN | 774 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 746 |
| 7 | Guaymaral Airport |  | CO | 661 |
| 8 | Harry Reid International Airport |  | US | 642 |
| 9 | Zurich Airport |  | CH | 583 |
| 10 | La Aurora Airport |  | GT | 565 |
| 11 | Frankfurt am Main International Airport |  | DE | 548 |
| 12 | Chicago O'Hare International Airport |  | US | 488 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 487 |
| 14 | Kuala Lumpur International Airport |  | MY | 480 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 466 |
| 16 | Macau International Airport |  | MO | 457 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 457 |
| 18 | Madrid Barajas International Airport |  | ES | 450 |
| 19 | Bengaluru International Airport |  | IN | 436 |
| 20 | Charlotte/Douglas International Airport |  | US | 418 |
| 21 | Congonhas Airport |  | BR | 414 |
| 22 | Malpensa International Airport |  | IT | 408 |
| 23 | Tenerife Norte Airport |  | ES | 406 |
| 24 | Ninoy Aquino International Airport |  | PH | 400 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 377 |
| 26 | Salt Lake City International Airport |  | US | 369 |
| 27 | Daniel K Inouye International Airport |  | US | 367 |
| 28 | Charles de Gaulle International Airport |  | FR | 367 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 364 |
| 30 | Capua Airport |  | IT | 354 |
| 31 | Vitoria/Foronda Airport |  | ES | 337 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 335 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 333 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 330 |
| 35 | Reno/Tahoe International Airport |  | US | 329 |
| 36 | O. R. Tambo International Airport |  | ZA | 325 |
| 37 | Barcelona International Airport |  | ES | 323 |
| 38 | Don Mueang International Airport |  | TH | 307 |
| 39 | Calgary International Airport |  | CA | 298 |
| 40 | Viracopos International Airport |  | BR | 294 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 267 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 234 | 1h 7m | 706 km | 2,849.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 189 | 14m | 114 km | 370.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 171 | 24m | 225 km | 663.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 148 | 21m | 244 km | 623.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 148 | 28m | 304 km | 775.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 143 | 1h 27m | 910 km | 2,244.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 132 | 19m | 165 km | 375.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 126 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 119 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 116 | 26m | 275 km | 549.7 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 103 | 54m | 546 km | 969.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 102 | 44m | 452 km | 794.9 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 87 | 1h 11m | 770 km | 1,155.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 86 | 31m | 369 km | 547.4 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 84 | 20m | 250 km | 362.8 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 80 | 26m | 215 km | 296.3 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 79 | 20m | 147 km | 199.9 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 73 | 1h 41m | 1,156 km | 1,456.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 69 | 58m | 493 km | 587.0 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 69 | 1h 0m | 695 km | 827.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AIC219 | Air India | Indira Gandhi International Airport (VIDP) | Simara Airport (VNSI) | 2026-04-23 09:21 UTC | 2026-04-23 10:36 UTC | 1h 15m |
| AKJ1324 | AKJ | Agartala Airport (VEAT) | Yongphulla Airport (VQ10) | 2026-04-23 10:01 UTC | 2026-04-23 10:21 UTC | 19m |
| N743AM |  | Livermore Municipal Airport (KLVK) | Tracy Municipal Airport (KTCY) | 2026-04-23 09:59 UTC | 2026-04-23 10:12 UTC | 13m |
| SWR37X | Swiss International | Poznań-Ławica Airport (EPPO) | Zurich Airport (LSZH) | 2026-04-23 09:02 UTC | 2026-04-23 10:11 UTC | 1h 9m |
| TAM3900 | LATAM Airlines | Congonhas Airport (SBSP) | Santa Cruz Airport (SBSC) | 2026-04-23 09:32 UTC | 2026-04-23 10:07 UTC | 35m |
| SHA738 | SHA | Phaplu Airport (VNPL) | Langtang Airport (VNLT) | 2026-04-23 09:31 UTC | 2026-04-23 10:03 UTC | 32m |
| RYR8NQ | Ryanair | Bari / Palese International Airport (LIBD) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-23 08:22 UTC | 2026-04-23 10:01 UTC | 1h 38m |
| KLM1 | KLM Royal Dutch | Maastricht Aachen Airport (EHBK) | Maastricht Aachen Airport (EHBK) | 2026-04-23 09:26 UTC | 2026-04-23 10:00 UTC | 33m |
| QLK1531 | QLK | Canberra International Airport (YSCB) | Melbourne International Airport (YMML) | 2026-04-23 09:00 UTC | 2026-04-23 09:55 UTC | 55m |
| RYR59SQ | Ryanair | Palma De Mallorca Airport (LEPA) | Munster Osnabruck Airport (EDDG) | 2026-04-23 07:28 UTC | 2026-04-23 09:50 UTC | 2h 22m |
| RYR2495 | Ryanair | Barcelona International Airport (LEBL) | Son Bonet Airport (LESB) | 2026-04-23 09:16 UTC | 2026-04-23 09:49 UTC | 32m |
| SHA225 | SHA | Tribhuvan International Airport (VNKT) | Tikapur Airport (VNTP) | 2026-04-23 08:58 UTC | 2026-04-23 09:45 UTC | 46m |
| WIF9VK | WIF | Bergen Airport Flesland (ENBR) | Kristiansund Airport Kvernberget (ENKB) | 2026-04-23 08:51 UTC | 2026-04-23 09:44 UTC | 52m |
| TAP62JR | TAP Air Portugal | Lisbon Portela Airport (LPPT) | Vitoria/Foronda Airport (LEVT) | 2026-04-23 08:47 UTC | 2026-04-23 09:43 UTC | 56m |
| IGO7VH | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Jamshedpur Airport (VEJS) | 2026-04-23 08:58 UTC | 2026-04-23 09:40 UTC | 41m |
| 5YFDG |  | Lanseria Airport (FALA) | Hendrik Potgieter Airport (FABO) | 2026-04-23 09:20 UTC | 2026-04-23 09:38 UTC | 18m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-23 09:09 UTC | 2026-04-23 09:37 UTC | 28m |
| N843FF |  | Farnborough Airport (EGLF) | Perugia / San Egidio Airport (LIRZ) | 2026-04-23 07:42 UTC | 2026-04-23 09:37 UTC | 1h 54m |
| IHBCR | IHB | Pavullo Airport (LIDP) | Modena / Marzaglia Airport (LIPM) | 2026-04-23 09:28 UTC | 2026-04-23 09:36 UTC | 8m |
| GES121L | GES | Madrid Barajas International Airport (LEMD) | Bilbao Airport (LEBB) | 2026-04-23 09:08 UTC | 2026-04-23 09:35 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
