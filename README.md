# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_16:28:21_UTC-green)

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

**Latest saved flight:** 2026-04-02 16:28:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 16:28:21 UTC

- **11,328** saved flights
- **6,542** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **11,328** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **139,895.5 tonnes** estimated CO2 emissions
- **8,109,883 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 481 |
| 2 | Ryanair | 454 |
| 3 | IndiGo | 322 |
| 4 | EJA | 218 |
| 5 | American Airlines | 196 |
| 6 | Lufthansa | 191 |
| 7 | Southwest Airlines | 168 |
| 8 | ENY | 142 |
| 9 | Vueling | 122 |
| 10 | AXM | 120 |
| 11 | LATAM Airlines | 116 |
| 12 | LXJ | 106 |
| 13 | All Nippon Airways | 103 |
| 14 | QLK | 99 |
| 15 | Swiss International | 92 |
| 16 | WIF | 92 |
| 17 | Delta Air Lines | 88 |
| 18 | AZU | 81 |
| 19 | AXB | 79 |
| 20 | VIV | 78 |
| 21 | Japan Airlines | 77 |
| 22 | Alaska Airlines | 72 |
| 23 | Cathay Pacific | 69 |
| 24 | EDV | 68 |
| 25 | easyJet | 68 |
| 26 | EJU | 67 |
| 27 | United Airlines | 67 |
| 28 | Avianca | 65 |
| 29 | BRC | 64 |
| 30 | GLO | 59 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8931 |
| 2 | 🇮🇳 IN | 993 |
| 3 | 🇦🇺 AU | 904 |
| 4 | 🇪🇸 ES | 900 |
| 5 | 🇩🇪 DE | 650 |
| 6 | 🇧🇷 BR | 609 |
| 7 | 🇯🇵 JP | 593 |
| 8 | 🇨🇴 CO | 565 |
| 9 | 🇨🇦 CA | 523 |
| 10 | 🇮🇹 IT | 521 |
| 11 | 🇬🇧 GB | 428 |
| 12 | 🇲🇽 MX | 402 |
| 13 | 🇫🇷 FR | 371 |
| 14 | 🇳🇴 NO | 294 |
| 15 | 🇬🇷 GR | 288 |
| 16 | 🇨🇭 CH | 279 |
| 17 | 🇲🇾 MY | 272 |
| 18 | 🇳🇿 NZ | 260 |
| 19 | 🇿🇦 ZA | 231 |
| 20 | 🇬🇹 GT | 221 |
| 21 | 🇵🇭 PH | 216 |
| 22 | 🇰🇷 KR | 204 |
| 23 | 🇹🇷 TR | 187 |
| 24 | 🇵🇱 PL | 163 |
| 25 | 🇹🇭 TH | 147 |
| 26 | 🇮🇩 ID | 143 |
| 27 | 🇲🇦 MA | 135 |
| 28 | 🇲🇴 MO | 134 |
| 29 | 🇳🇱 NL | 116 |
| 30 | 🇲🇪 ME | 114 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 262 |
| 2 | Tokyo International Airport |  | JP | 213 |
| 3 | Indira Gandhi International Airport |  | IN | 213 |
| 4 | Denver International Airport |  | US | 196 |
| 5 | El Dorado International Airport |  | CO | 191 |
| 6 | Frankfurt am Main International Airport |  | DE | 182 |
| 7 | Harry Reid International Airport |  | US | 156 |
| 8 | La Aurora Airport |  | GT | 154 |
| 9 | Guaymaral Airport |  | CO | 152 |
| 10 | Macau International Airport |  | MO | 134 |
| 11 | Zurich Airport |  | CH | 134 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 133 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 131 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 127 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 112 |
| 16 | Chicago O'Hare International Airport |  | US | 110 |
| 17 | Bengaluru International Airport |  | IN | 110 |
| 18 | Kuala Lumpur International Airport |  | MY | 104 |
| 19 | Madrid Barajas International Airport |  | ES | 102 |
| 20 | Tenerife Norte Airport |  | ES | 102 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 99 |
| 22 | Charlotte/Douglas International Airport |  | US | 97 |
| 23 | Ninoy Aquino International Airport |  | PH | 97 |
| 24 | Reno/Tahoe International Airport |  | US | 96 |
| 25 | Congonhas Airport |  | BR | 93 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 92 |
| 27 | Malpensa International Airport |  | IT | 87 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 86 |
| 29 | Vitoria/Foronda Airport |  | ES | 85 |
| 30 | Daniel K Inouye International Airport |  | US | 82 |
| 31 | Barcelona International Airport |  | ES | 81 |
| 32 | Charles de Gaulle International Airport |  | FR | 79 |
| 33 | Pune Airport |  | IN | 78 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 77 |
| 35 | Bodø Airport |  | NO | 76 |
| 36 | Austin-Bergstrom International Airport |  | US | 75 |
| 37 | Gimpo International Airport |  | KR | 75 |
| 38 | Salt Lake City International Airport |  | US | 75 |
| 39 | Seattle-Tacoma International Airport |  | US | 72 |
| 40 | Amsterdam Airport Schiphol |  | NL | 71 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 53 | 14m | 114 km | 104.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 36 | 1h 46m | 1,156 km | 718.2 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 35 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 34 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 31 | 23m | 99 km | 53.1 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 29 | 1h 26m | 910 km | 455.1 t |
| 13 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 28 | 15m | 206 km | 99.5 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 27 | 29m | 275 km | 127.9 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 26 | 53m | 546 km | 244.8 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 25 | 1h 43m | 1,423 km | 613.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 25 | 30m | 369 km | 159.1 t |
| 19 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 23 | 8m | - | - |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 22 | 1h 10m | 770 km | 292.3 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 22 | 1h 57m | 1,304 km | 494.9 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 21 | 23m | 252 km | 91.2 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 21 | 11m | 127 km | 46.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 18 | 20m | 147 km | 45.6 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 18 | 13m | 99 km | 30.9 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 17 | 44m | 452 km | 132.5 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 17 | 19m | - | - |
| 30 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 17 | 8h 31m | 38 km | 11.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FFAB123 | FFA | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-02 15:40 UTC | 2026-04-02 16:28 UTC | 47m |
| FHAAT | FHA | Toussus-le-Noble Airport (LFPN) | Bailleau Armenonville Airport (LFFL) | 2026-04-02 15:55 UTC | 2026-04-02 16:27 UTC | 31m |
| CGDFN | CGD | Thunder Bay Airport (CYQT) | Thunder Bay Airport (CYQT) | 2026-04-02 15:24 UTC | 2026-04-02 16:26 UTC | 1h 1m |
| NL851D |  | Kissimmee Gateway Airport (KISM) | Bartow Executive Airport (KBOW) | 2026-04-02 15:42 UTC | 2026-04-02 16:26 UTC | 44m |
| WAH | WAH | Kenai Municipal Airport (PAEN) | Trading Bay Production Airport (5AK0) | 2026-04-02 16:11 UTC | 2026-04-02 16:24 UTC | 12m |
| SCU36 | SCU | 2OL2 (2OL2) | Gregg Airport (7OK1) | 2026-04-02 15:46 UTC | 2026-04-02 16:22 UTC | 35m |
| N7189L |  | Rocky Mountain Metro Airport (KBJC) | Erie Municipal Airport (KEIK) | 2026-04-02 15:36 UTC | 2026-04-02 16:21 UTC | 45m |
| N739NP |  | Denton Enterprise Airport (KDTO) | Windwood Farm Airport (65TE) | 2026-04-02 15:54 UTC | 2026-04-02 16:17 UTC | 22m |
| SHARK49 | SHA | Usaf Academy Davis Airfield (KAFF) | Limon Municipal Airport (KLIC) | 2026-04-02 15:49 UTC | 2026-04-02 16:14 UTC | 24m |
| DESRT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-04-02 15:57 UTC | 2026-04-02 16:10 UTC | 12m |
| N281MG |  | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-04-02 15:10 UTC | 2026-04-02 16:10 UTC | 1h 0m |
| N4000K |  | Gerald R Ford International Airport (KGRR) | Iowa City Municipal Airport (KIOW) | 2026-04-02 15:13 UTC | 2026-04-02 16:09 UTC | 56m |
| N7485G |  | Ralph M Hall/Rockwall Municipal Airport (KF46) | Van Zandt County Regional Airport (K76F) | 2026-04-02 15:15 UTC | 2026-04-02 16:07 UTC | 51m |
| N2087E |  | San Gabriel Valley Airport (KEMT) | San Bernardino International Airport (KSBD) | 2026-04-02 15:31 UTC | 2026-04-02 16:04 UTC | 33m |
| N38HL |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-02 15:41 UTC | 2026-04-02 16:02 UTC | 21m |
| N96SW |  | Flying M & M Ranch Airport (0CO6) | Telluride Regional Airport (KTEX) | 2026-04-02 15:50 UTC | 2026-04-02 16:01 UTC | 10m |
| UPS2633 | UPS | Oakland San Francisco Bay Airport (KOAK) | Dallas-Fort Worth International Airport (KDFW) | 2026-04-02 13:20 UTC | 2026-04-02 16:01 UTC | 2h 40m |
| N5114K |  | Brookneal/Campbell County Airport (K0V4) | Brookneal/Campbell County Airport (K0V4) | 2026-04-02 15:14 UTC | 2026-04-02 15:56 UTC | 42m |
| TASI312 | TAS | Perot Field/Fort Worth Alliance Airport (KAFW) | Sherman Municipal Airport (KSWI) | 2026-04-02 15:34 UTC | 2026-04-02 15:56 UTC | 21m |
| SKW499U | SkyWest Airlines | Chicago O'Hare International Airport (KORD) | Huber Airport (39MI) | 2026-04-02 15:15 UTC | 2026-04-02 15:53 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
