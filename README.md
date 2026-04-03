# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_09:18:25_UTC-green)

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

**Latest saved flight:** 2026-04-03 09:18:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 09:18:25 UTC

- **12,915** saved flights
- **7,273** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **12,915** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **160,537.2 tonnes** estimated CO2 emissions
- **9,306,504 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 559 |
| 2 | Ryanair | 490 |
| 3 | IndiGo | 356 |
| 4 | EJA | 255 |
| 5 | American Airlines | 235 |
| 6 | Lufthansa | 202 |
| 7 | Southwest Airlines | 189 |
| 8 | ENY | 166 |
| 9 | Vueling | 135 |
| 10 | AXM | 131 |
| 11 | LATAM Airlines | 130 |
| 12 | QLK | 121 |
| 13 | All Nippon Airways | 117 |
| 14 | LXJ | 117 |
| 15 | Delta Air Lines | 102 |
| 16 | Swiss International | 98 |
| 17 | AZU | 95 |
| 18 | WIF | 95 |
| 19 | VIV | 93 |
| 20 | Alaska Airlines | 87 |
| 21 | Cathay Pacific | 85 |
| 22 | Japan Airlines | 85 |
| 23 | AXB | 84 |
| 24 | United Airlines | 84 |
| 25 | EDV | 78 |
| 26 | easyJet | 78 |
| 27 | EJU | 76 |
| 28 | ANZ | 72 |
| 29 | BRC | 72 |
| 30 | Avianca | 71 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10358 |
| 2 | 🇮🇳 IN | 1099 |
| 3 | 🇦🇺 AU | 1063 |
| 4 | 🇪🇸 ES | 981 |
| 5 | 🇧🇷 BR | 713 |
| 6 | 🇩🇪 DE | 696 |
| 7 | 🇯🇵 JP | 685 |
| 8 | 🇨🇴 CO | 619 |
| 9 | 🇨🇦 CA | 605 |
| 10 | 🇮🇹 IT | 575 |
| 11 | 🇬🇧 GB | 480 |
| 12 | 🇲🇽 MX | 462 |
| 13 | 🇫🇷 FR | 415 |
| 14 | 🇬🇷 GR | 323 |
| 15 | 🇳🇿 NZ | 323 |
| 16 | 🇨🇭 CH | 321 |
| 17 | 🇳🇴 NO | 301 |
| 18 | 🇲🇾 MY | 294 |
| 19 | 🇵🇭 PH | 258 |
| 20 | 🇿🇦 ZA | 251 |
| 21 | 🇬🇹 GT | 234 |
| 22 | 🇹🇷 TR | 231 |
| 23 | 🇰🇷 KR | 226 |
| 24 | 🇵🇱 PL | 179 |
| 25 | 🇹🇭 TH | 171 |
| 26 | 🇮🇩 ID | 160 |
| 27 | 🇲🇴 MO | 155 |
| 28 | 🇲🇦 MA | 152 |
| 29 | 🇧🇸 BS | 128 |
| 30 | 🇲🇪 ME | 127 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 314 |
| 2 | Tokyo International Airport |  | JP | 239 |
| 3 | Denver International Airport |  | US | 233 |
| 4 | Indira Gandhi International Airport |  | IN | 233 |
| 5 | El Dorado International Airport |  | CO | 216 |
| 6 | Frankfurt am Main International Airport |  | DE | 190 |
| 7 | Harry Reid International Airport |  | US | 178 |
| 8 | La Aurora Airport |  | GT | 163 |
| 9 | Sydney Kingsford Smith International Airport |  | AU | 158 |
| 10 | Zurich Airport |  | CH | 156 |
| 11 | Macau International Airport |  | MO | 155 |
| 12 | Guaymaral Airport |  | CO | 153 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 147 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 145 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 125 |
| 16 | Bengaluru International Airport |  | IN | 124 |
| 17 | Chicago O'Hare International Airport |  | US | 123 |
| 18 | Ninoy Aquino International Airport |  | PH | 117 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 114 |
| 20 | Charlotte/Douglas International Airport |  | US | 112 |
| 21 | Madrid Barajas International Airport |  | ES | 112 |
| 22 | Kuala Lumpur International Airport |  | MY | 109 |
| 23 | Congonhas Airport |  | BR | 109 |
| 24 | Tenerife Norte Airport |  | ES | 107 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 98 |
| 26 | Salt Lake City International Airport |  | US | 98 |
| 27 | Daniel K Inouye International Airport |  | US | 97 |
| 28 | Reno/Tahoe International Airport |  | US | 97 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 96 |
| 30 | Vitoria/Foronda Airport |  | ES | 94 |
| 31 | Malpensa International Airport |  | IT | 92 |
| 32 | Barcelona International Airport |  | ES | 91 |
| 33 | Charles de Gaulle International Airport |  | FR | 90 |
| 34 | Pune Airport |  | IN | 87 |
| 35 | Seattle-Tacoma International Airport |  | US | 86 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 86 |
| 37 | Austin-Bergstrom International Airport |  | US | 85 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 82 |
| 39 | Gimpo International Airport |  | KR | 81 |
| 40 | Miami International Airport |  | US | 79 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 60 | 14m | 114 km | 117.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 58 | 1h 7m | 706 km | 706.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 43 | 29m | 304 km | 225.4 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 39 | 1h 46m | 1,156 km | 778.0 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 39 | 31m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 34 | 1h 26m | 910 km | 533.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 32 | 23m | 99 km | 54.8 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 30 | 28m | 275 km | 142.2 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 30 | 53m | 546 km | 282.5 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 16 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 28 | 30m | 369 km | 178.2 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 27 | 1h 55m | 1,304 km | 607.4 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 26 | 1h 42m | 1,423 km | 638.1 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 25 | 1h 10m | 770 km | 332.1 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 23 | 23m | 252 km | 99.9 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 23 | 11m | 127 km | 50.3 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 22 | 1h 0m | 723 km | 274.3 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 21 | 20m | 147 km | 53.1 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 21 | 13m | 99 km | 36.0 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 20 | 44m | 452 km | 155.9 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 19 | 1h 16m | 924 km | 303.0 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 19 | 32m | - | - |
| 30 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 18 | 17m | 183 km | 56.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FHBTI | FHB | Toussus-le-Noble Airport (LFPN) | Etampes Mondesir Airport (LFOX) | 2026-04-03 08:22 UTC | 2026-04-03 09:18 UTC | 56m |
| OKEUE46 | OKE | Olomouc Glider Airport (LKOL) | LKSP (LKSP) | 2026-04-03 08:58 UTC | 2026-04-03 09:16 UTC | 17m |
| HBWAK | HBW | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-04-03 08:34 UTC | 2026-04-03 09:16 UTC | 41m |
| HBLVB | HBL | Bern Belp Airport (LSZB) | Friedrichshafen Airport (EDNY) | 2026-04-03 07:22 UTC | 2026-04-03 08:57 UTC | 1h 34m |
| 2611 |  | Chiang Mai International Airport (VTCC) | Mae Sariang Airport (VTCS) | 2026-04-03 08:33 UTC | 2026-04-03 08:52 UTC | 19m |
| OKHTO | OKH | Tocna Praha Glider Airport (LKTC) | Vlasin Glider Airport (LKVL) | 2026-04-03 08:06 UTC | 2026-04-03 08:44 UTC | 38m |
| CSI532 | CSI | Las Cruces International Airport (KLRU) | Sacaton Airport (NM16) | 2026-04-03 07:35 UTC | 2026-04-03 08:34 UTC | 58m |
| SWR1XG | Swiss International | Munich International Airport (EDDM) | Zurich Airport (LSZH) | 2026-04-03 07:59 UTC | 2026-04-03 08:34 UTC | 35m |
| FPFLC | FPF | Chambery-Challes-les-Eaux Airport (LFLE) | L'alpe D'huez Airport (LFHU) | 2026-04-03 08:13 UTC | 2026-04-03 08:34 UTC | 20m |
| SHT12N | SHT | London Heathrow Airport (EGLL) | Newcastle Airport (EGNT) | 2026-04-03 07:45 UTC | 2026-04-03 08:32 UTC | 46m |
| ITY218 | ITY | Linate Airport (LIML) | London City Airport (EGLC) | 2026-04-03 06:47 UTC | 2026-04-03 08:30 UTC | 1h 42m |
| N483LP |  | Glendale Regional Airport (KGEU) | Western Sky Airpark (0AZ2) | 2026-04-03 07:06 UTC | 2026-04-03 08:27 UTC | 1h 20m |
| AFL1002 | AFL | Sheremetyevo International Airport (UUEE) | Narva Estonia Airport (EENA) | 2026-04-03 07:20 UTC | 2026-04-03 08:25 UTC | 1h 5m |
| ANA697 | All Nippon Airways | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-03 07:09 UTC | 2026-04-03 08:22 UTC | 1h 13m |
| ZKIDU | ZKI | Invercargill Airport (NZNV) | Taieri Airport (NZTI) | 2026-04-03 07:34 UTC | 2026-04-03 08:21 UTC | 47m |
| JL2325 |  | Osaka International Airport (RJOO) | Tajima Airport (RJBT) | 2026-04-03 08:06 UTC | 2026-04-03 08:17 UTC | 11m |
| IGO6542 | IndiGo | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-04-03 07:55 UTC | 2026-04-03 08:14 UTC | 19m |
| ANA319 | All Nippon Airways | Tokyo International Airport (RJTT) | Toyama Airport (RJNT) | 2026-04-03 07:45 UTC | 2026-04-03 08:12 UTC | 27m |
| IGO612Y | IndiGo | Indira Gandhi International Airport (VIDP) | Lengpui Airport (VELP) | 2026-04-03 06:03 UTC | 2026-04-03 08:11 UTC | 2h 8m |
| SCR762 | SCR | Gothenburg-Landvetter Airport (ESGG) | Raron Airport (LSTA) | 2026-04-03 06:18 UTC | 2026-04-03 08:11 UTC | 1h 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
