# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_17:48:34_UTC-green)

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

**Latest saved flight:** 2026-04-05 17:48:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 17:48:34 UTC

- **18,474** saved flights
- **9,415** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **18,474** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **233,873.0 tonnes** estimated CO2 emissions
- **13,557,854 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 787 |
| 2 | Ryanair | 762 |
| 3 | IndiGo | 537 |
| 4 | American Airlines | 336 |
| 5 | EJA | 333 |
| 6 | Lufthansa | 256 |
| 7 | Southwest Airlines | 256 |
| 8 | ENY | 247 |
| 9 | Vueling | 203 |
| 10 | LATAM Airlines | 196 |
| 11 | AXM | 191 |
| 12 | All Nippon Airways | 161 |
| 13 | Delta Air Lines | 159 |
| 14 | LXJ | 159 |
| 15 | QLK | 154 |
| 16 | AZU | 140 |
| 17 | Swiss International | 140 |
| 18 | VIV | 135 |
| 19 | Alaska Airlines | 124 |
| 20 | Japan Airlines | 124 |
| 21 | easyJet | 122 |
| 22 | AEE | 120 |
| 23 | Avianca | 120 |
| 24 | United Airlines | 120 |
| 25 | EJU | 119 |
| 26 | AXB | 113 |
| 27 | WIF | 112 |
| 28 | EDV | 111 |
| 29 | Cathay Pacific | 105 |
| 30 | Air France | 103 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 14338 |
| 2 | 🇮🇳 IN | 1633 |
| 3 | 🇪🇸 ES | 1538 |
| 4 | 🇦🇺 AU | 1312 |
| 5 | 🇧🇷 BR | 1069 |
| 6 | 🇯🇵 JP | 994 |
| 7 | 🇨🇴 CO | 973 |
| 8 | 🇩🇪 DE | 956 |
| 9 | 🇮🇹 IT | 882 |
| 10 | 🇨🇦 CA | 803 |
| 11 | 🇬🇧 GB | 724 |
| 12 | 🇫🇷 FR | 690 |
| 13 | 🇲🇽 MX | 618 |
| 14 | 🇬🇷 GR | 533 |
| 15 | 🇨🇭 CH | 500 |
| 16 | 🇲🇾 MY | 437 |
| 17 | 🇿🇦 ZA | 407 |
| 18 | 🇬🇹 GT | 397 |
| 19 | 🇳🇿 NZ | 396 |
| 20 | 🇳🇴 NO | 374 |
| 21 | 🇵🇭 PH | 355 |
| 22 | 🇹🇷 TR | 354 |
| 23 | 🇰🇷 KR | 325 |
| 24 | 🇹🇭 TH | 273 |
| 25 | 🇵🇱 PL | 272 |
| 26 | 🇲🇦 MA | 234 |
| 27 | 🇮🇩 ID | 205 |
| 28 | 🇧🇸 BS | 205 |
| 29 | 🇲🇴 MO | 198 |
| 30 | 🇲🇪 ME | 193 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 437 |
| 2 | El Dorado International Airport |  | CO | 369 |
| 3 | Indira Gandhi International Airport |  | IN | 342 |
| 4 | Tokyo International Airport |  | JP | 340 |
| 5 | Denver International Airport |  | US | 336 |
| 6 | La Aurora Airport |  | GT | 277 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 253 |
| 8 | Harry Reid International Airport |  | US | 237 |
| 9 | Zurich Airport |  | CH | 229 |
| 10 | Frankfurt am Main International Airport |  | DE | 228 |
| 11 | Macau International Airport |  | MO | 198 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 195 |
| 13 | Guaymaral Airport |  | CO | 195 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 193 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 191 |
| 16 | Chicago O'Hare International Airport |  | US | 181 |
| 17 | Madrid Barajas International Airport |  | ES | 181 |
| 18 | Bengaluru International Airport |  | IN | 181 |
| 19 | Charlotte/Douglas International Airport |  | US | 175 |
| 20 | Tenerife Norte Airport |  | ES | 170 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 162 |
| 22 | Ninoy Aquino International Airport |  | PH | 162 |
| 23 | Congonhas Airport |  | BR | 160 |
| 24 | Kuala Lumpur International Airport |  | MY | 155 |
| 25 | Salt Lake City International Airport |  | US | 148 |
| 26 | Daniel K Inouye International Airport |  | US | 146 |
| 27 | Vitoria/Foronda Airport |  | ES | 143 |
| 28 | Malpensa International Airport |  | IT | 142 |
| 29 | Charles de Gaulle International Airport |  | FR | 141 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 140 |
| 31 | Reno/Tahoe International Airport |  | US | 139 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 138 |
| 33 | Miami International Airport |  | US | 131 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 128 |
| 35 | Barcelona International Airport |  | ES | 128 |
| 36 | Pune Airport |  | IN | 126 |
| 37 | O. R. Tambo International Airport |  | ZA | 125 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 120 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 119 |
| 40 | Seattle-Tacoma International Airport |  | US | 116 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 85 | 1h 7m | 706 km | 1,034.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 82 | 14m | 114 km | 160.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 59 | 27m | 152 km | 154.2 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 55 | 22m | 99 km | 94.2 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 54 | 1h 44m | 1,156 km | 1,077.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 50 | 16m | 206 km | 177.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 40 | 1h 11m | 770 km | 531.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 39 | 1h 54m | 1,304 km | 877.4 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 38 | 52m | 556 km | 364.3 t |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 37 | 1h 43m | 1,423 km | 908.0 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 37 | 23m | 252 km | 160.6 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 36 | 9m | - | - |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 35 | 13m | 99 km | 60.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 33 | 58m | 723 km | 411.4 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 27 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 30 | 17m | 183 km | 94.6 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 29 | 20m | 147 km | 73.4 t |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 29 | 20m | 250 km | 125.3 t |
| 30 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 29 | 30m | 114 km | 57.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EAX9D | EAX | Sabadell Airport (LELL) | Sabadell Airport (LELL) | 2026-04-05 16:55 UTC | 2026-04-05 17:48 UTC | 52m |
| N158AM |  | Nassau Airport (83FL) | K4J6 (K4J6) | 2026-04-05 17:27 UTC | 2026-04-05 17:43 UTC | 16m |
| N723AJ |  | KU42 (KU42) | Nephi Municipal Airport (KU14) | 2026-04-05 17:14 UTC | 2026-04-05 17:42 UTC | 28m |
| TGSSS | TGS | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-05 17:25 UTC | 2026-04-05 17:40 UTC | 15m |
| N744ND |  | Oxnard Airport (KOXR) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-04-05 17:03 UTC | 2026-04-05 17:36 UTC | 33m |
| N383AC |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-04-05 17:08 UTC | 2026-04-05 17:36 UTC | 28m |
| N54DB |  | Robert S Kerr Airport (KRKR) | Addington Field (KEKX) | 2026-04-05 15:32 UTC | 2026-04-05 17:31 UTC | 1h 58m |
| NDU787 | NDU | Ryan Field (KRYN) | Benson Municipal/Paul Kerchum Field (KE95) | 2026-04-05 16:59 UTC | 2026-04-05 17:30 UTC | 30m |
| AKJ902C | AKJ | Chhatrapati Shivaji International Airport (VABB) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-05 14:29 UTC | 2026-04-05 17:28 UTC | 2h 59m |
| N725CS |  | Dillant/Hopkins Airport (KEEN) | Laurence G Hanscom Field (KBED) | 2026-04-05 17:05 UTC | 2026-04-05 17:23 UTC | 18m |
| N314LM |  | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-04-05 17:01 UTC | 2026-04-05 17:23 UTC | 22m |
| TGLOP | TGL | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-04-05 17:02 UTC | 2026-04-05 17:20 UTC | 18m |
| CGPCL | CGP | Vancouver International Airport (CYVR) | Schmidt Ranch Airport (1WN0) | 2026-04-05 16:31 UTC | 2026-04-05 17:19 UTC | 48m |
| TGFYL | TGF | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-04-05 17:00 UTC | 2026-04-05 17:19 UTC | 18m |
| OKALT | OKA | Bolzano Airport (LIPB) | Brno-Turany Airport (LKTB) | 2026-04-05 16:06 UTC | 2026-04-05 17:18 UTC | 1h 11m |
| TGPWO | TGP | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-05 16:50 UTC | 2026-04-05 17:11 UTC | 21m |
| MSR788 | EgyptAir | Munich International Airport (EDDM) | HE42 (HE42) | 2026-04-05 14:08 UTC | 2026-04-05 17:10 UTC | 3h 2m |
| N7882N |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-04-05 16:40 UTC | 2026-04-05 17:09 UTC | 28m |
| SWU1954 | SWU | Bolzano Airport (LIPB) | Hamburg Airport (EDDH) | 2026-04-05 15:31 UTC | 2026-04-05 17:07 UTC | 1h 36m |
| RYR45GL | Ryanair | Niederrhein Airport (EDLV) | Sepurine Training Base (LD57) | 2026-04-05 15:44 UTC | 2026-04-05 17:07 UTC | 1h 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
