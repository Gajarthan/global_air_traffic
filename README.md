# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_16:44:01_UTC-green)

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

**Latest saved flight:** 2026-04-04 16:44:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 16:44:01 UTC

- **16,129** saved flights
- **8,592** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **16,129** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **199,804.5 tonnes** estimated CO2 emissions
- **11,582,872 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 681 |
| 2 | Ryanair | 654 |
| 3 | IndiGo | 471 |
| 4 | EJA | 305 |
| 5 | American Airlines | 285 |
| 6 | Lufthansa | 231 |
| 7 | Southwest Airlines | 229 |
| 8 | ENY | 202 |
| 9 | Vueling | 178 |
| 10 | LATAM Airlines | 173 |
| 11 | AXM | 160 |
| 12 | All Nippon Airways | 141 |
| 13 | LXJ | 137 |
| 14 | QLK | 137 |
| 15 | Delta Air Lines | 131 |
| 16 | Swiss International | 123 |
| 17 | AZU | 122 |
| 18 | VIV | 118 |
| 19 | EJU | 108 |
| 20 | Japan Airlines | 107 |
| 21 | Alaska Airlines | 104 |
| 22 | Avianca | 104 |
| 23 | AEE | 102 |
| 24 | WIF | 102 |
| 25 | AXB | 101 |
| 26 | easyJet | 98 |
| 27 | United Airlines | 98 |
| 28 | EDV | 97 |
| 29 | GLO | 93 |
| 30 | BRC | 92 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12663 |
| 2 | 🇮🇳 IN | 1434 |
| 3 | 🇪🇸 ES | 1323 |
| 4 | 🇦🇺 AU | 1207 |
| 5 | 🇧🇷 BR | 939 |
| 6 | 🇯🇵 JP | 860 |
| 7 | 🇩🇪 DE | 846 |
| 8 | 🇨🇴 CO | 820 |
| 9 | 🇮🇹 IT | 740 |
| 10 | 🇨🇦 CA | 710 |
| 11 | 🇬🇧 GB | 628 |
| 12 | 🇫🇷 FR | 593 |
| 13 | 🇲🇽 MX | 544 |
| 14 | 🇬🇷 GR | 449 |
| 15 | 🇨🇭 CH | 436 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 368 |
| 18 | 🇿🇦 ZA | 346 |
| 19 | 🇳🇴 NO | 337 |
| 20 | 🇵🇭 PH | 305 |
| 21 | 🇹🇷 TR | 296 |
| 22 | 🇬🇹 GT | 291 |
| 23 | 🇰🇷 KR | 290 |
| 24 | 🇹🇭 TH | 231 |
| 25 | 🇵🇱 PL | 231 |
| 26 | 🇲🇦 MA | 196 |
| 27 | 🇮🇩 ID | 177 |
| 28 | 🇧🇸 BS | 173 |
| 29 | 🇲🇪 ME | 167 |
| 30 | 🇲🇴 MO | 163 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 378 |
| 2 | El Dorado International Airport |  | CO | 307 |
| 3 | Tokyo International Airport |  | JP | 299 |
| 4 | Indira Gandhi International Airport |  | IN | 295 |
| 5 | Denver International Airport |  | US | 287 |
| 6 | Harry Reid International Airport |  | US | 215 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 210 |
| 8 | Frankfurt am Main International Airport |  | DE | 210 |
| 9 | La Aurora Airport |  | GT | 205 |
| 10 | Zurich Airport |  | CH | 197 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Guaymaral Airport |  | CO | 171 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 167 |
| 14 | Macau International Airport |  | MO | 163 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 162 |
| 16 | Bengaluru International Airport |  | IN | 157 |
| 17 | Chicago O'Hare International Airport |  | US | 150 |
| 18 | Congonhas Airport |  | BR | 150 |
| 19 | Charlotte/Douglas International Airport |  | US | 149 |
| 20 | Madrid Barajas International Airport |  | ES | 147 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 141 |
| 22 | Ninoy Aquino International Airport |  | PH | 140 |
| 23 | Tenerife Norte Airport |  | ES | 140 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 135 |
| 25 | Kuala Lumpur International Airport |  | MY | 130 |
| 26 | Malpensa International Airport |  | IT | 125 |
| 27 | Salt Lake City International Airport |  | US | 125 |
| 28 | Reno/Tahoe International Airport |  | US | 124 |
| 29 | Daniel K Inouye International Airport |  | US | 123 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 123 |
| 31 | Charles de Gaulle International Airport |  | FR | 120 |
| 32 | Vitoria/Foronda Airport |  | ES | 117 |
| 33 | Barcelona International Airport |  | ES | 115 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 108 |
| 35 | Pune Airport |  | IN | 108 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 107 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 103 |
| 38 | Austin-Bergstrom International Airport |  | US | 103 |
| 39 | Gimpo International Airport |  | KR | 101 |
| 40 | O. R. Tambo International Airport |  | ZA | 101 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 74 | 14m | 114 km | 145.1 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 65 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 49 | 1h 45m | 1,156 km | 977.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 49 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 41 | 26m | 152 km | 107.1 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 39 | 16m | 206 km | 138.7 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 39 | 22m | 99 km | 66.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 37 | 28m | 275 km | 175.3 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 14 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 35 | 53m | 556 km | 335.5 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 33 | 1h 54m | 1,304 km | 742.4 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 29 | 1h 42m | 1,423 km | 711.7 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 28 | 13m | 99 km | 48.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 28 | 9m | - | - |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 27 | 59m | 723 km | 336.6 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 26 | 20m | 147 km | 65.8 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 24 | 52m | 493 km | 204.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 24 | 1h 20m | 961 km | 397.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK181 | CXK | Long Island Mac Arthur Airport (KISP) | Long Island Mac Arthur Airport (KISP) | 2026-04-04 15:27 UTC | 2026-04-04 16:44 UTC | 1h 16m |
| CXK674 | CXK | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-04-04 15:28 UTC | 2026-04-04 16:35 UTC | 1h 6m |
| N2444H |  | Buchanan Field (KCCR) | Buchanan Field (KCCR) | 2026-04-04 15:44 UTC | 2026-04-04 16:29 UTC | 45m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-04-04 15:48 UTC | 2026-04-04 16:23 UTC | 35m |
| DRAG157 | DRA | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | 2026-04-04 16:20 UTC | 2026-04-04 16:21 UTC | 0m |
| CAP3935 | CAP | Marsh Point Airport (SC74) | Marsh Point Airport (SC74) | 2026-04-04 16:13 UTC | 2026-04-04 16:20 UTC | 6m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-04-04 14:57 UTC | 2026-04-04 16:18 UTC | 1h 21m |
| N47296 |  | Marennes Le Bournet Airport (LFJI) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-04-04 16:06 UTC | 2026-04-04 16:16 UTC | 9m |
| N65474 |  | Angel Fire Airport (KAXX) | Ohkay Owingeh Airport (KE14) | 2026-04-04 15:55 UTC | 2026-04-04 16:16 UTC | 20m |
| GPD177 | GPD | Luis Munoz Marin International Airport (TJSJ) | Cyril E King Airport (TIST) | 2026-04-04 16:00 UTC | 2026-04-04 16:14 UTC | 14m |
| N734NK |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-04-04 16:02 UTC | 2026-04-04 16:14 UTC | 11m |
| RYR83SA | Ryanair | Memmingen Allgau Airport (EDJA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-04 14:54 UTC | 2026-04-04 16:11 UTC | 1h 17m |
| N750AU |  | Auburn University Regional Airport (KAUO) | Columbus Airport (KCSG) | 2026-04-04 15:58 UTC | 2026-04-04 16:11 UTC | 13m |
| TGASR | TGA | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-04 16:09 UTC | 2026-04-04 16:11 UTC | 1m |
| DKQAX | DKQ | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-04-04 16:04 UTC | 2026-04-04 16:10 UTC | 6m |
| N8604Q |  | Pueblo Memorial Airport (KPUB) | Cuchara Valley At La Veta Airport (K07V) | 2026-04-04 15:30 UTC | 2026-04-04 16:09 UTC | 38m |
| N38HL |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-04 15:45 UTC | 2026-04-04 16:08 UTC | 22m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-04-04 15:47 UTC | 2026-04-04 16:04 UTC | 17m |
| N44BZ |  | Double Eagle Ii Airport (KAEG) | Runway Bay Airport (NM61) | 2026-04-04 15:45 UTC | 2026-04-04 16:03 UTC | 17m |
| N967SA |  | Elizabeth City Cg Air Station/Regional Airport (KECG) | Northeastern Regional Airport (KEDE) | 2026-04-04 15:29 UTC | 2026-04-04 16:03 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
