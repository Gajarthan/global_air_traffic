# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_07:20:07_UTC-green)

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

**Latest saved flight:** 2026-04-03 07:20:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 07:20:07 UTC

- **12,777** saved flights
- **7,222** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **12,777** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **158,859.5 tonnes** estimated CO2 emissions
- **9,209,249 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 559 |
| 2 | Ryanair | 484 |
| 3 | IndiGo | 344 |
| 4 | EJA | 255 |
| 5 | American Airlines | 235 |
| 6 | Lufthansa | 197 |
| 7 | Southwest Airlines | 189 |
| 8 | ENY | 166 |
| 9 | Vueling | 133 |
| 10 | LATAM Airlines | 130 |
| 11 | AXM | 129 |
| 12 | QLK | 120 |
| 13 | LXJ | 117 |
| 14 | All Nippon Airways | 114 |
| 15 | Delta Air Lines | 101 |
| 16 | Swiss International | 96 |
| 17 | AZU | 95 |
| 18 | WIF | 95 |
| 19 | VIV | 93 |
| 20 | Alaska Airlines | 87 |
| 21 | Cathay Pacific | 85 |
| 22 | United Airlines | 84 |
| 23 | AXB | 82 |
| 24 | Japan Airlines | 82 |
| 25 | EDV | 78 |
| 26 | easyJet | 77 |
| 27 | EJU | 73 |
| 28 | ANZ | 72 |
| 29 | BRC | 72 |
| 30 | Avianca | 71 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10350 |
| 2 | 🇮🇳 IN | 1063 |
| 3 | 🇦🇺 AU | 1046 |
| 4 | 🇪🇸 ES | 970 |
| 5 | 🇧🇷 BR | 711 |
| 6 | 🇩🇪 DE | 682 |
| 7 | 🇯🇵 JP | 662 |
| 8 | 🇨🇴 CO | 619 |
| 9 | 🇨🇦 CA | 601 |
| 10 | 🇮🇹 IT | 564 |
| 11 | 🇬🇧 GB | 469 |
| 12 | 🇲🇽 MX | 462 |
| 13 | 🇫🇷 FR | 403 |
| 14 | 🇳🇿 NZ | 318 |
| 15 | 🇬🇷 GR | 317 |
| 16 | 🇨🇭 CH | 307 |
| 17 | 🇳🇴 NO | 301 |
| 18 | 🇲🇾 MY | 291 |
| 19 | 🇵🇭 PH | 250 |
| 20 | 🇿🇦 ZA | 239 |
| 21 | 🇬🇹 GT | 234 |
| 22 | 🇰🇷 KR | 223 |
| 23 | 🇹🇷 TR | 222 |
| 24 | 🇵🇱 PL | 176 |
| 25 | 🇹🇭 TH | 167 |
| 26 | 🇮🇩 ID | 157 |
| 27 | 🇲🇴 MO | 154 |
| 28 | 🇲🇦 MA | 146 |
| 29 | 🇧🇸 BS | 128 |
| 30 | 🇲🇪 ME | 126 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 314 |
| 2 | Denver International Airport |  | US | 233 |
| 3 | Tokyo International Airport |  | JP | 232 |
| 4 | Indira Gandhi International Airport |  | IN | 226 |
| 5 | El Dorado International Airport |  | CO | 216 |
| 6 | Frankfurt am Main International Airport |  | DE | 187 |
| 7 | Harry Reid International Airport |  | US | 178 |
| 8 | La Aurora Airport |  | GT | 163 |
| 9 | Sydney Kingsford Smith International Airport |  | AU | 156 |
| 10 | Macau International Airport |  | MO | 154 |
| 11 | Guaymaral Airport |  | CO | 153 |
| 12 | Zurich Airport |  | CH | 151 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 145 |
| 14 | Eleftherios Venizelos International Airport |  | GR | 144 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 125 |
| 16 | Chicago O'Hare International Airport |  | US | 123 |
| 17 | Bengaluru International Airport |  | IN | 119 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 114 |
| 19 | Ninoy Aquino International Airport |  | PH | 113 |
| 20 | Charlotte/Douglas International Airport |  | US | 112 |
| 21 | Madrid Barajas International Airport |  | ES | 110 |
| 22 | Congonhas Airport |  | BR | 109 |
| 23 | Kuala Lumpur International Airport |  | MY | 108 |
| 24 | Tenerife Norte Airport |  | ES | 106 |
| 25 | Salt Lake City International Airport |  | US | 98 |
| 26 | Daniel K Inouye International Airport |  | US | 97 |
| 27 | Reno/Tahoe International Airport |  | US | 97 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 96 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 95 |
| 30 | Vitoria/Foronda Airport |  | ES | 93 |
| 31 | Malpensa International Airport |  | IT | 92 |
| 32 | Barcelona International Airport |  | ES | 90 |
| 33 | Charles de Gaulle International Airport |  | FR | 87 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 86 |
| 35 | Austin-Bergstrom International Airport |  | US | 85 |
| 36 | Pune Airport |  | IN | 85 |
| 37 | Seattle-Tacoma International Airport |  | US | 85 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 82 |
| 39 | Gimpo International Airport |  | KR | 80 |
| 40 | Miami International Airport |  | US | 79 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 60 | 14m | 114 km | 117.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 54 | 1h 7m | 706 km | 657.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 49 | 24m | 225 km | 190.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 43 | 29m | 304 km | 225.4 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 39 | 1h 46m | 1,156 km | 778.0 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 38 | 31m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 33 | 1h 26m | 910 km | 517.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 32 | 23m | 99 km | 54.8 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 30 | 28m | 275 km | 142.2 t |
| 14 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 29 | 53m | 546 km | 273.0 t |
| 16 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 28 | 30m | 369 km | 178.2 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 27 | 1h 55m | 1,304 km | 607.4 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 26 | 1h 42m | 1,423 km | 638.1 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 25 | 1h 10m | 770 km | 332.1 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 23 | 23m | 252 km | 99.9 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 23 | 11m | 127 km | 50.3 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 21 | 1h 0m | 723 km | 261.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 21 | 13m | 99 km | 36.0 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 20 | 20m | 147 km | 50.6 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 20 | 44m | 452 km | 155.9 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 19 | 1h 16m | 924 km | 303.0 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 19 | 32m | - | - |
| 30 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 18 | 17m | 183 km | 56.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| URSA20 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-03 07:04 UTC | 2026-04-03 07:20 UTC | 15m |
| HBXCL | HBX | Courchevel Airport (LFLJ) | Megeve Airport (LFHM) | 2026-04-03 07:01 UTC | 2026-04-03 07:16 UTC | 15m |
| N55169 |  | Merrill Field (PAMR) | Talkeetna Airport (PATK) | 2026-04-03 06:10 UTC | 2026-04-03 07:15 UTC | 1h 5m |
| FJKZH | FJK | Saint-Cyr-l'Ecole Airport (LFPZ) | Saint-Cyr-l'Ecole Airport (LFPZ) | 2026-04-03 06:47 UTC | 2026-04-03 06:53 UTC | 6m |
| DKMYG | DKM | Bern Belp Airport (LSZB) | Muenster Aero Airport (LSPU) | 2026-04-03 06:08 UTC | 2026-04-03 06:53 UTC | 44m |
| QFA629 | Qantas | Brisbane International Airport (YBBN) | Melbourne International Airport (YMML) | 2026-04-03 04:33 UTC | 2026-04-03 06:46 UTC | 2h 13m |
| N604TT |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-04-03 05:36 UTC | 2026-04-03 06:45 UTC | 1h 9m |
| SFR701 | SFR | Cape Town International Airport (FACT) | Rand Airport (FAGM) | 2026-04-03 05:08 UTC | 2026-04-03 06:43 UTC | 1h 35m |
| CFH23 | CFH | Newcastle Airport (YWLM) | Walcha Airport (YWCH) | 2026-04-03 06:12 UTC | 2026-04-03 06:42 UTC | 29m |
| AXM6496 | AXM | Kota Kinabalu International Airport (WBKK) | Telupid Airport (WBKE) | 2026-04-03 06:23 UTC | 2026-04-03 06:39 UTC | 15m |
| VOE3544 | VOE | Asturias Airport (LEAS) | Federico Garcia Lorca Airport (LEGR) | 2026-04-03 05:30 UTC | 2026-04-03 06:35 UTC | 1h 5m |
| VOZ660 | Virgin Australia | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-04-03 06:05 UTC | 2026-04-03 06:34 UTC | 29m |
| AE976 |  | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-04-03 06:13 UTC | 2026-04-03 06:34 UTC | 20m |
| TRA275T | TRA | Eindhoven Airport (EHEH) | Santa Cilia De Jaca Airport (LECI) | 2026-04-03 05:10 UTC | 2026-04-03 06:29 UTC | 1h 19m |
| IGO291 | IndiGo | Indira Gandhi International Airport (VIDP) | Lengpui Airport (VELP) | 2026-04-03 04:26 UTC | 2026-04-03 06:28 UTC | 2h 1m |
| EWG5B | EWG | Dusseldorf International Airport (EDDL) | Budapest Ferenc Liszt International Airport (LHBP) | 2026-04-03 04:57 UTC | 2026-04-03 06:27 UTC | 1h 30m |
| ASA1163 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Haiku Airstrip (HI33) | 2026-04-03 06:10 UTC | 2026-04-03 06:25 UTC | 14m |
| VOZ1715 | Virgin Australia | Brisbane International Airport (YBBN) | Monduran Airport (YMUA) | 2026-04-03 05:52 UTC | 2026-04-03 06:25 UTC | 32m |
| AL736 |  | Perth International Airport (YPPH) | Kondinin Airport (YKDN) | 2026-04-03 05:50 UTC | 2026-04-03 06:22 UTC | 32m |
| AXM5596 | AXM | Seletar Airport (WSSL) | Sepulot Airport (WBKO) | 2026-04-03 04:30 UTC | 2026-04-03 06:22 UTC | 1h 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
