# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_19:32:39_UTC-green)

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

**Latest saved flight:** 2026-05-10 19:32:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-10 19:32:39 UTC

- **77,421** saved flights
- **28,310** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **77,421** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **959,607.4 tonnes** estimated CO2 emissions
- **55,629,417 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3324 |
| 2 | SkyWest Airlines | 2871 |
| 3 | IndiGo | 1724 |
| 4 | EJA | 1422 |
| 5 | American Airlines | 1207 |
| 6 | Southwest Airlines | 1136 |
| 7 | Lufthansa | 1015 |
| 8 | ENY | 965 |
| 9 | Delta Air Lines | 822 |
| 10 | Vueling | 741 |
| 11 | AXM | 720 |
| 12 | LATAM Airlines | 709 |
| 13 | WIF | 667 |
| 14 | All Nippon Airways | 625 |
| 15 | AZU | 616 |
| 16 | QLK | 591 |
| 17 | Swiss International | 588 |
| 18 | LXJ | 567 |
| 19 | Alaska Airlines | 543 |
| 20 | easyJet | 518 |
| 21 | EJU | 503 |
| 22 | AEE | 500 |
| 23 | Cathay Pacific | 498 |
| 24 | VIV | 462 |
| 25 | Air France | 457 |
| 26 | Japan Airlines | 449 |
| 27 | AXB | 431 |
| 28 | CXK | 397 |
| 29 | MXY | 387 |
| 30 | AIQ | 386 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 62445 |
| 2 | 🇪🇸 ES | 5555 |
| 3 | 🇮🇳 IN | 5409 |
| 4 | 🇦🇺 AU | 5029 |
| 5 | 🇩🇪 DE | 4390 |
| 6 | 🇧🇷 BR | 4303 |
| 7 | 🇮🇹 IT | 4278 |
| 8 | 🇯🇵 JP | 4018 |
| 9 | 🇨🇦 CA | 3835 |
| 10 | 🇬🇧 GB | 3333 |
| 11 | 🇫🇷 FR | 3079 |
| 12 | 🇨🇴 CO | 2700 |
| 13 | 🇲🇽 MX | 2367 |
| 14 | 🇬🇷 GR | 2290 |
| 15 | 🇳🇴 NO | 2126 |
| 16 | 🇨🇭 CH | 2092 |
| 17 | 🇲🇾 MY | 1800 |
| 18 | 🇿🇦 ZA | 1478 |
| 19 | 🇹🇷 TR | 1392 |
| 20 | 🇳🇿 NZ | 1391 |
| 21 | 🇹🇭 TH | 1379 |
| 22 | 🇵🇱 PL | 1293 |
| 23 | 🇵🇭 PH | 1242 |
| 24 | 🇰🇷 KR | 1214 |
| 25 | 🇬🇹 GT | 1202 |
| 26 | 🇲🇦 MA | 915 |
| 27 | 🇲🇴 MO | 911 |
| 28 | 🇲🇪 ME | 825 |
| 29 | 🇳🇱 NL | 809 |
| 30 | 🇭🇷 HR | 673 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1712 |
| 2 | Tokyo International Airport |  | JP | 1349 |
| 3 | Denver International Airport |  | US | 1289 |
| 4 | Indira Gandhi International Airport |  | IN | 1144 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1124 |
| 6 | Frankfurt am Main International Airport |  | DE | 1018 |
| 7 | Harry Reid International Airport |  | US | 962 |
| 8 | Zurich Airport |  | CH | 914 |
| 9 | Macau International Airport |  | MO | 911 |
| 10 | La Aurora Airport |  | GT | 903 |
| 11 | Guaymaral Airport |  | CO | 892 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 803 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 774 |
| 15 | Chicago O'Hare International Airport |  | US | 756 |
| 16 | Kuala Lumpur International Airport |  | MY | 722 |
| 17 | Madrid Barajas International Airport |  | ES | 721 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 685 |
| 19 | Malpensa International Airport |  | IT | 673 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 672 |
| 21 | Bengaluru International Airport |  | IN | 670 |
| 22 | Salt Lake City International Airport |  | US | 635 |
| 23 | Capua Airport |  | IT | 614 |
| 24 | Charles de Gaulle International Airport |  | FR | 611 |
| 25 | Charlotte/Douglas International Airport |  | US | 610 |
| 26 | Congonhas Airport |  | BR | 607 |
| 27 | Tenerife Norte Airport |  | ES | 576 |
| 28 | Ninoy Aquino International Airport |  | PH | 565 |
| 29 | Daniel K Inouye International Airport |  | US | 561 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 555 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 526 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 525 |
| 33 | Barcelona International Airport |  | ES | 524 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 505 |
| 35 | Vitoria/Foronda Airport |  | ES | 492 |
| 36 | Don Mueang International Airport |  | TH | 490 |
| 37 | Amsterdam Airport Schiphol |  | NL | 487 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 482 |
| 39 | O. R. Tambo International Airport |  | ZA | 464 |
| 40 | Calgary International Airport |  | CA | 459 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 371 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 276 | 21m | 244 km | 1,162.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 224 | 24m | 225 km | 869.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 209 | 1h 27m | 910 km | 3,279.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 196 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 184 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 183 | 19m | 165 km | 520.5 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 172 | 1h 12m | 770 km | 2,284.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 166 | 26m | 275 km | 786.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 139 | 20m | 99 km | 238.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 136 | 44m | 452 km | 1,059.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 123 | 31m | 369 km | 782.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 118 | 27m | 215 km | 437.0 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 110 | 14m | 154 km | 291.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 103 | 1h 1m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 103 | 1h 42m | 1,423 km | 2,527.8 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 103 | 57m | 493 km | 876.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 101 | 23m | 55 km | 96.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 97 | 12m | - | - |
| 29 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 97 | 18m | 144 km | 241.3 t |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 96 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N464TT |  | Mc Clellan Airfield (KMCC) | Byron Airport (KC83) | 2026-05-10 19:16 UTC | 2026-05-10 19:32 UTC | 15m |
| TRP2 | TRP | Robinson Airport (MD14) | Joint Base Andrews Airport (KADW) | 2026-05-10 19:18 UTC | 2026-05-10 19:29 UTC | 11m |
| AR3 |  | Miami Executive Airport (KTMB) | Miami-Opa Locka Executive Airport (KOPF) | 2026-05-10 18:47 UTC | 2026-05-10 19:23 UTC | 36m |
| XSN90 | XSN | Mc Clellan-Palomar Airport (KCRQ) | San Carlos Airport (KSQL) | 2026-05-10 17:55 UTC | 2026-05-10 19:22 UTC | 1h 26m |
| SWR47D | Swiss International | Firenze / Peretola Airport (LIRQ) | Zurich Airport (LSZH) | 2026-05-10 18:30 UTC | 2026-05-10 19:20 UTC | 49m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-10 19:04 UTC | 2026-05-10 19:17 UTC | 12m |
| N323CW |  | Aurora Municipal Airport (KARR) | 95LL (95LL) | 2026-05-10 19:05 UTC | 2026-05-10 19:11 UTC | 5m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-10 18:57 UTC | 2026-05-10 19:10 UTC | 13m |
| N5931S |  | Renton Municipal Airport (KRNT) | Windsock Airport (4WA4) | 2026-05-10 18:29 UTC | 2026-05-10 19:06 UTC | 37m |
| N5244N |  | Montgomery County Airpark (KGAI) | Ocean City Municipal Airport (KOXB) | 2026-05-10 18:07 UTC | 2026-05-10 19:06 UTC | 58m |
|  |  | 36MI (36MI) | 36MI (36MI) | 2026-05-10 18:49 UTC | 2026-05-10 19:02 UTC | 13m |
| N282AM |  | Rancho Hielo Brazos Airport (TA35) | Howard County Airport (KM77) | 2026-05-10 18:02 UTC | 2026-05-10 19:01 UTC | 58m |
| EJA544 | EJA | KNY2 (KNY2) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 16:49 UTC | 2026-05-10 19:01 UTC | 2h 11m |
| GPD433 | GPD | Lebanon Municipal Airport (KLEB) | Teterboro Airport (KTEB) | 2026-05-10 18:04 UTC | 2026-05-10 18:58 UTC | 54m |
| EJA520 | EJA | Chicago Midway International Airport (KMDW) | Truckee-Tahoe Airport (KTRK) | 2026-05-10 14:58 UTC | 2026-05-10 18:58 UTC | 3h 59m |
| WIF83M | WIF | Bergen Airport Flesland (ENBR) | Sogndal Airport (ENSG) | 2026-05-10 18:35 UTC | 2026-05-10 18:57 UTC | 22m |
| N886EP |  | San Antonio International Airport (KSAT) | Browns Landing Airport (32MS) | 2026-05-10 18:01 UTC | 2026-05-10 18:54 UTC | 53m |
| SIS49 | SIS | Monroe County Airport (KBMG) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-10 14:52 UTC | 2026-05-10 18:54 UTC | 4h 1m |
| AEE5SA | AEE | Chania International Airport (LGSA) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-10 18:20 UTC | 2026-05-10 18:52 UTC | 32m |
| RTY131 | RTY | Northern Colorado Regional Airport (KFNL) | Northern Colorado Regional Airport (KFNL) | 2026-05-10 18:00 UTC | 2026-05-10 18:49 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
