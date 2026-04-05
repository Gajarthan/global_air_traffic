# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_16:04:11_UTC-green)

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

**Latest saved flight:** 2026-04-05 16:04:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 16:04:11 UTC

- **18,243** saved flights
- **9,324** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **18,243** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **231,025.2 tonnes** estimated CO2 emissions
- **13,392,764 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 776 |
| 2 | Ryanair | 749 |
| 3 | IndiGo | 534 |
| 4 | EJA | 330 |
| 5 | American Airlines | 327 |
| 6 | Lufthansa | 255 |
| 7 | Southwest Airlines | 253 |
| 8 | ENY | 241 |
| 9 | Vueling | 201 |
| 10 | LATAM Airlines | 194 |
| 11 | AXM | 190 |
| 12 | All Nippon Airways | 161 |
| 13 | Delta Air Lines | 156 |
| 14 | QLK | 154 |
| 15 | LXJ | 153 |
| 16 | AZU | 140 |
| 17 | Swiss International | 139 |
| 18 | VIV | 134 |
| 19 | Japan Airlines | 124 |
| 20 | Alaska Airlines | 123 |
| 21 | easyJet | 121 |
| 22 | AEE | 119 |
| 23 | Avianca | 119 |
| 24 | United Airlines | 117 |
| 25 | EJU | 116 |
| 26 | AXB | 113 |
| 27 | EDV | 110 |
| 28 | WIF | 108 |
| 29 | Cathay Pacific | 105 |
| 30 | BRC | 101 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 14130 |
| 2 | 🇮🇳 IN | 1624 |
| 3 | 🇪🇸 ES | 1520 |
| 4 | 🇦🇺 AU | 1312 |
| 5 | 🇧🇷 BR | 1061 |
| 6 | 🇯🇵 JP | 994 |
| 7 | 🇨🇴 CO | 955 |
| 8 | 🇩🇪 DE | 945 |
| 9 | 🇮🇹 IT | 866 |
| 10 | 🇨🇦 CA | 789 |
| 11 | 🇬🇧 GB | 719 |
| 12 | 🇫🇷 FR | 676 |
| 13 | 🇲🇽 MX | 615 |
| 14 | 🇬🇷 GR | 526 |
| 15 | 🇨🇭 CH | 491 |
| 16 | 🇲🇾 MY | 436 |
| 17 | 🇿🇦 ZA | 405 |
| 18 | 🇳🇿 NZ | 396 |
| 19 | 🇬🇹 GT | 376 |
| 20 | 🇳🇴 NO | 362 |
| 21 | 🇵🇭 PH | 354 |
| 22 | 🇹🇷 TR | 347 |
| 23 | 🇰🇷 KR | 325 |
| 24 | 🇹🇭 TH | 273 |
| 25 | 🇵🇱 PL | 266 |
| 26 | 🇲🇦 MA | 227 |
| 27 | 🇮🇩 ID | 205 |
| 28 | 🇧🇸 BS | 199 |
| 29 | 🇲🇴 MO | 198 |
| 30 | 🇲🇪 ME | 192 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 428 |
| 2 | El Dorado International Airport |  | CO | 364 |
| 3 | Indira Gandhi International Airport |  | IN | 340 |
| 4 | Tokyo International Airport |  | JP | 340 |
| 5 | Denver International Airport |  | US | 328 |
| 6 | La Aurora Airport |  | GT | 262 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 248 |
| 8 | Harry Reid International Airport |  | US | 233 |
| 9 | Frankfurt am Main International Airport |  | DE | 227 |
| 10 | Zurich Airport |  | CH | 224 |
| 11 | Macau International Airport |  | MO | 198 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 191 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 191 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 189 |
| 15 | Guaymaral Airport |  | CO | 188 |
| 16 | Bengaluru International Airport |  | IN | 180 |
| 17 | Madrid Barajas International Airport |  | ES | 178 |
| 18 | Chicago O'Hare International Airport |  | US | 176 |
| 19 | Charlotte/Douglas International Airport |  | US | 170 |
| 20 | Tenerife Norte Airport |  | ES | 169 |
| 21 | Ninoy Aquino International Airport |  | PH | 162 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 160 |
| 23 | Congonhas Airport |  | BR | 158 |
| 24 | Kuala Lumpur International Airport |  | MY | 155 |
| 25 | Daniel K Inouye International Airport |  | US | 146 |
| 26 | Salt Lake City International Airport |  | US | 144 |
| 27 | Vitoria/Foronda Airport |  | ES | 142 |
| 28 | Malpensa International Airport |  | IT | 141 |
| 29 | Charles de Gaulle International Airport |  | FR | 138 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 138 |
| 31 | Reno/Tahoe International Airport |  | US | 137 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 137 |
| 33 | Miami International Airport |  | US | 129 |
| 34 | Barcelona International Airport |  | ES | 126 |
| 35 | Pune Airport |  | IN | 125 |
| 36 | O. R. Tambo International Airport |  | ZA | 125 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 123 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 119 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 117 |
| 40 | Seattle-Tacoma International Airport |  | US | 115 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 85 | 1h 7m | 706 km | 1,034.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 81 | 14m | 114 km | 158.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 70 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 57 | 27m | 152 km | 149.0 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 54 | 1h 44m | 1,156 km | 1,077.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 50 | 16m | 206 km | 177.8 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 50 | 22m | 99 km | 85.6 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 40 | 1h 11m | 770 km | 531.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 39 | 1h 54m | 1,304 km | 877.4 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 38 | 52m | 556 km | 364.3 t |
| 18 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 37 | 23m | 252 km | 160.6 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 36 | 1h 43m | 1,423 km | 883.5 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 33 | 58m | 723 km | 411.4 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 33 | 13m | 99 km | 56.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 26 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 33 | 9m | - | - |
| 27 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 30 | 17m | 183 km | 94.6 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 29 | 20m | 147 km | 73.4 t |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 29 | 20m | 250 km | 125.3 t |
| 30 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 29 | 30m | 114 km | 57.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N16NW |  | Jim Kelly Field (KLXN) | 71NE (71NE) | 2026-04-05 15:35 UTC | 2026-04-05 16:04 UTC | 28m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-05 15:45 UTC | 2026-04-05 16:00 UTC | 15m |
| N67405 |  | University Airport (KEDU) | Yolo County Airport (KDWA) | 2026-04-05 15:26 UTC | 2026-04-05 15:58 UTC | 31m |
| N337MC |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-04-05 15:21 UTC | 2026-04-05 15:45 UTC | 24m |
| N47PW |  | Vero Beach Regional Airport (KVRB) | Georgetown County Airport (KGGE) | 2026-04-05 14:36 UTC | 2026-04-05 15:44 UTC | 1h 8m |
| TCAHK | TCA | Balikesir Korfez Airport (LTFD) | Balikesir Korfez Airport (LTFD) | 2026-04-05 15:24 UTC | 2026-04-05 15:34 UTC | 10m |
| TGOME | TGO | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-04-05 14:51 UTC | 2026-04-05 15:32 UTC | 40m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-05 15:16 UTC | 2026-04-05 15:32 UTC | 15m |
| ZXP02 | ZXP | Rotterdam Airport (EHRD) | Midden-Zeeland Airport (EHMZ) | 2026-04-05 14:06 UTC | 2026-04-05 15:29 UTC | 1h 23m |
| AVR4880 | AVR | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 2026-04-05 15:08 UTC | 2026-04-05 15:25 UTC | 17m |
| YV3351 |  | Mamon Airport (SVMM) | Adicora Airport (SVAR) | 2026-04-05 15:18 UTC | 2026-04-05 15:25 UTC | 6m |
| OAL8SK | OAL | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-04-05 15:03 UTC | 2026-04-05 15:25 UTC | 21m |
| EWG5MU | EWG | London Heathrow Airport (EGLL) | Hamburg Airport (EDDH) | 2026-04-05 14:16 UTC | 2026-04-05 15:24 UTC | 1h 8m |
| CXK579 | CXK | Brackett Field (KPOC) | Riverside Airport (KRAL) | 2026-04-05 15:02 UTC | 2026-04-05 15:19 UTC | 17m |
| N16NW |  | Arapahoe Municipal Airport (K37V) | 71NE (71NE) | 2026-04-05 14:50 UTC | 2026-04-05 15:18 UTC | 28m |
| RSC16VV | RSC | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-04-05 15:07 UTC | 2026-04-05 15:18 UTC | 10m |
| HK5122G |  | Guaymaral Airport (SKGY) | Madrid Air Base (SKMA) | 2026-04-05 15:07 UTC | 2026-04-05 15:17 UTC | 10m |
| N157U |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-04-05 14:47 UTC | 2026-04-05 15:17 UTC | 29m |
| PSPMM | PSP | Campo de Marte Airport (SBMT) | Campo de Marte Airport (SBMT) | 2026-04-05 15:08 UTC | 2026-04-05 15:15 UTC | 6m |
| RYR21XE | Ryanair | Valencia Airport (LEVC) | Grazzanise Airport (LIRM) | 2026-04-05 13:35 UTC | 2026-04-05 15:13 UTC | 1h 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
