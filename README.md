# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_21:43:48_UTC-green)

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

**Latest saved flight:** 2026-04-03 21:43:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 21:43:48 UTC

- **14,519** saved flights
- **7,978** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **14,519** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **179,595.8 tonnes** estimated CO2 emissions
- **10,411,352 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 642 |
| 2 | Ryanair | 561 |
| 3 | IndiGo | 404 |
| 4 | EJA | 291 |
| 5 | American Airlines | 272 |
| 6 | Southwest Airlines | 212 |
| 7 | Lufthansa | 210 |
| 8 | ENY | 190 |
| 9 | Vueling | 156 |
| 10 | LATAM Airlines | 154 |
| 11 | AXM | 142 |
| 12 | LXJ | 132 |
| 13 | QLK | 125 |
| 14 | All Nippon Airways | 123 |
| 15 | Delta Air Lines | 116 |
| 16 | AZU | 114 |
| 17 | Swiss International | 111 |
| 18 | VIV | 106 |
| 19 | WIF | 97 |
| 20 | United Airlines | 96 |
| 21 | Alaska Airlines | 94 |
| 22 | easyJet | 90 |
| 23 | AXB | 89 |
| 24 | Japan Airlines | 89 |
| 25 | AEE | 87 |
| 26 | EDV | 87 |
| 27 | EJU | 87 |
| 28 | BRC | 85 |
| 29 | Cathay Pacific | 85 |
| 30 | Avianca | 84 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 11768 |
| 2 | 🇮🇳 IN | 1230 |
| 3 | 🇪🇸 ES | 1107 |
| 4 | 🇦🇺 AU | 1090 |
| 5 | 🇧🇷 BR | 855 |
| 6 | 🇩🇪 DE | 757 |
| 7 | 🇯🇵 JP | 729 |
| 8 | 🇨🇴 CO | 719 |
| 9 | 🇨🇦 CA | 665 |
| 10 | 🇮🇹 IT | 627 |
| 11 | 🇬🇧 GB | 557 |
| 12 | 🇲🇽 MX | 506 |
| 13 | 🇫🇷 FR | 502 |
| 14 | 🇬🇷 GR | 388 |
| 15 | 🇨🇭 CH | 374 |
| 16 | 🇳🇿 NZ | 347 |
| 17 | 🇲🇾 MY | 319 |
| 18 | 🇳🇴 NO | 313 |
| 19 | 🇿🇦 ZA | 299 |
| 20 | 🇹🇷 TR | 267 |
| 21 | 🇬🇹 GT | 265 |
| 22 | 🇵🇭 PH | 265 |
| 23 | 🇰🇷 KR | 237 |
| 24 | 🇵🇱 PL | 201 |
| 25 | 🇹🇭 TH | 186 |
| 26 | 🇲🇦 MA | 176 |
| 27 | 🇮🇩 ID | 166 |
| 28 | 🇲🇴 MO | 157 |
| 29 | 🇧🇸 BS | 157 |
| 30 | 🇲🇪 ME | 149 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 360 |
| 2 | El Dorado International Airport |  | CO | 265 |
| 3 | Denver International Airport |  | US | 265 |
| 4 | Indira Gandhi International Airport |  | IN | 261 |
| 5 | Tokyo International Airport |  | JP | 253 |
| 6 | Harry Reid International Airport |  | US | 196 |
| 7 | Frankfurt am Main International Airport |  | DE | 196 |
| 8 | La Aurora Airport |  | GT | 185 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 180 |
| 10 | Zurich Airport |  | CH | 175 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 161 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 160 |
| 13 | Macau International Airport |  | MO | 157 |
| 14 | Guaymaral Airport |  | CO | 157 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 142 |
| 16 | Chicago O'Hare International Airport |  | US | 140 |
| 17 | Bengaluru International Airport |  | IN | 140 |
| 18 | Charlotte/Douglas International Airport |  | US | 135 |
| 19 | Congonhas Airport |  | BR | 133 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 130 |
| 21 | Madrid Barajas International Airport |  | ES | 127 |
| 22 | Ninoy Aquino International Airport |  | PH | 121 |
| 23 | Kuala Lumpur International Airport |  | MY | 117 |
| 24 | Salt Lake City International Airport |  | US | 115 |
| 25 | Tenerife Norte Airport |  | ES | 114 |
| 26 | Reno/Tahoe International Airport |  | US | 112 |
| 27 | Vitoria/Foronda Airport |  | ES | 111 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 110 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 110 |
| 30 | Daniel K Inouye International Airport |  | US | 106 |
| 31 | Charles de Gaulle International Airport |  | FR | 104 |
| 32 | Malpensa International Airport |  | IT | 102 |
| 33 | George Bush Intcntl/Houston Airport |  | US | 101 |
| 34 | Pune Airport |  | IN | 99 |
| 35 | Austin-Bergstrom International Airport |  | US | 98 |
| 36 | Barcelona International Airport |  | ES | 96 |
| 37 | Miami International Airport |  | US | 94 |
| 38 | Seattle-Tacoma International Airport |  | US | 94 |
| 39 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 93 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 90 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 67 | 14m | 114 km | 131.4 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 61 | 1h 7m | 706 km | 742.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 43 | 1h 46m | 1,156 km | 857.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 37 | 22m | 99 km | 63.4 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 36 | 1h 26m | 910 km | 564.9 t |
| 10 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 35 | 27m | 152 km | 91.5 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 34 | 15m | 206 km | 120.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 34 | 28m | 275 km | 161.1 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 32 | 53m | 556 km | 306.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 17 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 31 | 1h 54m | 1,304 km | 697.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 30 | 30m | 369 km | 191.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 27 | 1h 10m | 770 km | 358.7 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 26 | 59m | 723 km | 324.1 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 23 | 13m | 99 km | 39.4 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 21 | 1h 15m | 924 km | 334.9 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 21 | 16m | 183 km | 66.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 20 | 12m | 15 km | 5.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N500TD |  | Bald Mountain Airport (OG45) | OG04 (OG04) | 2026-04-03 21:15 UTC | 2026-04-03 21:43 UTC | 28m |
| N9683Q |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-04-03 20:59 UTC | 2026-04-03 21:37 UTC | 38m |
| N910VP |  | Mckinney Ntl Airport (KTKI) | Perry-Houston County Airport (KPXE) | 2026-04-03 20:00 UTC | 2026-04-03 21:29 UTC | 1h 28m |
| KING98 | KIN | Paxson Airport (PAXK) | Eielson Afb Airport (PAEI) | 2026-04-03 21:04 UTC | 2026-04-03 21:28 UTC | 24m |
| CNS333 | CNS | Bradley International Airport (KBDL) | Tweed/New Haven Airport (KHVN) | 2026-04-03 21:13 UTC | 2026-04-03 21:26 UTC | 13m |
| ZKTTS | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-04-03 20:40 UTC | 2026-04-03 21:18 UTC | 37m |
| N1NJ |  | Aeroflex/Andover Airport (K12N) | Morristown Municipal Airport (KMMU) | 2026-04-03 21:07 UTC | 2026-04-03 21:16 UTC | 9m |
| N888HH |  | West Michigan Regional Airport (KBIV) | Spokane International Airport (KGEG) | 2026-04-03 18:11 UTC | 2026-04-03 21:16 UTC | 3h 4m |
| N223RC |  | Ja Field (SC58) | Herold Airport (WV63) | 2026-04-03 20:29 UTC | 2026-04-03 21:15 UTC | 45m |
| N98485 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-03 20:50 UTC | 2026-04-03 21:14 UTC | 23m |
| N558R |  | Louisville Muhammad Ali International Airport (KSDF) | Singleton Airport (97VA) | 2026-04-03 20:30 UTC | 2026-04-03 21:12 UTC | 41m |
| N450CB |  | Somerset Airport (KSMQ) | Lehigh Valley International Airport (KABE) | 2026-04-03 20:46 UTC | 2026-04-03 21:10 UTC | 24m |
| N721SE |  | Salt Lake City International Airport (KSLC) | Cadiz Airstrip (CA90) | 2026-04-03 20:01 UTC | 2026-04-03 21:09 UTC | 1h 7m |
| FRG404 | FRG | Wichita Dwight D Eisenhower Ntl Airport (KICT) | 1PS4 (1PS4) | 2026-04-03 18:44 UTC | 2026-04-03 21:04 UTC | 2h 20m |
| SHADY05 | SHA | Porterville Municipal Airport (KPTV) | Porterville Municipal Airport (KPTV) | 2026-04-03 20:43 UTC | 2026-04-03 21:04 UTC | 20m |
| N525JJ |  | Troy Municipal At N Kenneth Campbell Field (KTOI) | Robert Sibley Airport (KSZY) | 2026-04-03 20:16 UTC | 2026-04-03 21:00 UTC | 43m |
| N931PA |  | Falcon Field (KFFZ) | Phoenix Deer Valley Airport (KDVT) | 2026-04-03 20:04 UTC | 2026-04-03 20:59 UTC | 54m |
| N5197R |  | Dayton Valley Airpark (KA34) | Dayton Valley Airpark (KA34) | 2026-04-03 20:46 UTC | 2026-04-03 20:58 UTC | 11m |
| N9303N |  | Denton Enterprise Airport (KDTO) | Addington Field (4TX8) | 2026-04-03 19:59 UTC | 2026-04-03 20:56 UTC | 56m |
| RYR6SW | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Tortoli' / Arbatax Airport (LIET) | 2026-04-03 20:07 UTC | 2026-04-03 20:54 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
