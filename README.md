# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_11:02:14_UTC-green)

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

**Latest saved flight:** 2026-04-03 11:02:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 11:02:14 UTC

- **13,058** saved flights
- **7,320** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **13,058** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **162,475.4 tonnes** estimated CO2 emissions
- **9,418,864 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 559 |
| 2 | Ryanair | 495 |
| 3 | IndiGo | 369 |
| 4 | EJA | 255 |
| 5 | American Airlines | 235 |
| 6 | Lufthansa | 203 |
| 7 | Southwest Airlines | 189 |
| 8 | ENY | 166 |
| 9 | Vueling | 137 |
| 10 | AXM | 136 |
| 11 | LATAM Airlines | 132 |
| 12 | QLK | 123 |
| 13 | All Nippon Airways | 122 |
| 14 | LXJ | 117 |
| 15 | Delta Air Lines | 102 |
| 16 | Swiss International | 101 |
| 17 | WIF | 97 |
| 18 | AZU | 95 |
| 19 | VIV | 93 |
| 20 | Alaska Airlines | 87 |
| 21 | Japan Airlines | 86 |
| 22 | AXB | 85 |
| 23 | Cathay Pacific | 85 |
| 24 | United Airlines | 84 |
| 25 | easyJet | 80 |
| 26 | EDV | 78 |
| 27 | EJU | 77 |
| 28 | ANZ | 72 |
| 29 | BRC | 72 |
| 30 | AEE | 71 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10369 |
| 2 | 🇮🇳 IN | 1135 |
| 3 | 🇦🇺 AU | 1076 |
| 4 | 🇪🇸 ES | 994 |
| 5 | 🇧🇷 BR | 721 |
| 6 | 🇯🇵 JP | 709 |
| 7 | 🇩🇪 DE | 700 |
| 8 | 🇨🇴 CO | 619 |
| 9 | 🇨🇦 CA | 605 |
| 10 | 🇮🇹 IT | 581 |
| 11 | 🇬🇧 GB | 492 |
| 12 | 🇲🇽 MX | 462 |
| 13 | 🇫🇷 FR | 435 |
| 14 | 🇬🇷 GR | 336 |
| 15 | 🇨🇭 CH | 336 |
| 16 | 🇳🇿 NZ | 325 |
| 17 | 🇲🇾 MY | 309 |
| 18 | 🇳🇴 NO | 305 |
| 19 | 🇵🇭 PH | 262 |
| 20 | 🇿🇦 ZA | 261 |
| 21 | 🇹🇷 TR | 236 |
| 22 | 🇰🇷 KR | 235 |
| 23 | 🇬🇹 GT | 234 |
| 24 | 🇵🇱 PL | 181 |
| 25 | 🇹🇭 TH | 171 |
| 26 | 🇮🇩 ID | 162 |
| 27 | 🇲🇴 MO | 155 |
| 28 | 🇲🇦 MA | 154 |
| 29 | 🇲🇪 ME | 133 |
| 30 | 🇳🇱 NL | 128 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 314 |
| 2 | Tokyo International Airport |  | JP | 248 |
| 3 | Indira Gandhi International Airport |  | IN | 242 |
| 4 | Denver International Airport |  | US | 233 |
| 5 | El Dorado International Airport |  | CO | 216 |
| 6 | Frankfurt am Main International Airport |  | DE | 192 |
| 7 | Harry Reid International Airport |  | US | 178 |
| 8 | La Aurora Airport |  | GT | 163 |
| 9 | Zurich Airport |  | CH | 160 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 159 |
| 11 | Macau International Airport |  | MO | 155 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 154 |
| 13 | Guaymaral Airport |  | CO | 153 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 145 |
| 15 | Bengaluru International Airport |  | IN | 127 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 125 |
| 17 | Chicago O'Hare International Airport |  | US | 123 |
| 18 | Ninoy Aquino International Airport |  | PH | 119 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 114 |
| 20 | Madrid Barajas International Airport |  | ES | 113 |
| 21 | Kuala Lumpur International Airport |  | MY | 113 |
| 22 | Charlotte/Douglas International Airport |  | US | 112 |
| 23 | Congonhas Airport |  | BR | 111 |
| 24 | Tenerife Norte Airport |  | ES | 108 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 103 |
| 26 | Salt Lake City International Airport |  | US | 98 |
| 27 | Daniel K Inouye International Airport |  | US | 97 |
| 28 | Reno/Tahoe International Airport |  | US | 97 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 96 |
| 30 | Vitoria/Foronda Airport |  | ES | 95 |
| 31 | Charles de Gaulle International Airport |  | FR | 95 |
| 32 | Malpensa International Airport |  | IT | 94 |
| 33 | Barcelona International Airport |  | ES | 91 |
| 34 | Pune Airport |  | IN | 90 |
| 35 | Seattle-Tacoma International Airport |  | US | 86 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 86 |
| 37 | Austin-Bergstrom International Airport |  | US | 85 |
| 38 | Gimpo International Airport |  | KR | 85 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 82 |
| 40 | Miami International Airport |  | US | 79 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 60 | 1h 7m | 706 km | 730.5 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 60 | 14m | 114 km | 117.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 40 | 1h 46m | 1,156 km | 798.0 t |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 35 | 1h 26m | 910 km | 549.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 32 | 23m | 99 km | 54.8 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 30 | 28m | 275 km | 142.2 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 30 | 53m | 546 km | 282.5 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 29 | 30m | 369 km | 184.6 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 27 | 1h 55m | 1,304 km | 607.4 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 26 | 1h 10m | 770 km | 345.4 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 23 | 20m | 147 km | 58.2 t |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 23 | 23m | 252 km | 99.9 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 23 | 11m | 127 km | 50.3 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 22 | 1h 0m | 723 km | 274.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 21 | 44m | 452 km | 163.7 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 21 | 13m | 99 km | 36.0 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 19 | 1h 16m | 924 km | 303.0 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 19 | 32m | - | - |
| 30 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 18 | 17m | 183 km | 56.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| XAX604 | XAX | Kuala Lumpur International Airport (WMKK) | UG27 (UG27) | 2026-04-03 02:30 UTC | 2026-04-03 11:02 UTC | 8h 31m |
| N144CH |  | Birmingham-Shuttlesworth International Airport (KBHM) | Birmingham-Shuttlesworth International Airport (KBHM) | 2026-04-03 10:54 UTC | 2026-04-03 10:56 UTC | 1m |
| QLK1257 | QLK | Brisbane International Airport (YBBN) | Melbourne International Airport (YMML) | 2026-04-03 08:22 UTC | 2026-04-03 10:41 UTC | 2h 19m |
| ALFT6 | ALF | WN40 (WN40) | Boeing Field/King County International Airport (KBFI) | 2026-04-03 10:16 UTC | 2026-04-03 10:39 UTC | 22m |
| CAL131 | CAL | New Chitose Airport (RJCC) | Longtan Air Base (RCDI) | 2026-04-03 06:35 UTC | 2026-04-03 10:24 UTC | 3h 48m |
| NJE208P | NJE | Zurich Airport (LSZH) | Lyon-Bron Airport (LFLY) | 2026-04-03 09:38 UTC | 2026-04-03 10:16 UTC | 37m |
| HBXDA | HBX | Muenster Aero Airport (LSPU) | Sion Airport (LSGS) | 2026-04-03 10:12 UTC | 2026-04-03 10:14 UTC | 1m |
| ADO87 | ADO | Tokyo International Airport (RJTT) | Asahikawa Airport (RJEC) | 2026-04-03 08:57 UTC | 2026-04-03 10:12 UTC | 1h 14m |
| URSA10 | URS | Clear Creek Airport (2AK2) | Ladd Army Air Field (PAFB) | 2026-04-03 09:11 UTC | 2026-04-03 10:08 UTC | 57m |
| IGO402 | IndiGo | Dehradun Airport (VIDN) | Pune Airport (VAPO) | 2026-04-03 08:13 UTC | 2026-04-03 10:05 UTC | 1h 52m |
| AEA54NL | AEA | Palma De Mallorca Airport (LEPA) | Federico Garcia Lorca Airport (LEGR) | 2026-04-03 09:06 UTC | 2026-04-03 10:04 UTC | 57m |
| PHSVD | PHS | Eelde Airport (EHGG) | Eelde Airport (EHGG) | 2026-04-03 10:01 UTC | 2026-04-03 10:02 UTC | 0m |
| ZKIME | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-04-03 09:43 UTC | 2026-04-03 10:02 UTC | 18m |
| SYERSTON | SYE | RAF Syerston (EGXY) | RAF Syerston (EGXY) | 2026-04-03 09:43 UTC | 2026-04-03 10:00 UTC | 17m |
| IBB18XQ | IBB | Gran Canaria Airport (GCLP) | Federico Garcia Lorca Airport (LEGR) | 2026-04-03 07:59 UTC | 2026-04-03 09:59 UTC | 2h 0m |
| RYR400P | Ryanair | John Paul II International Airport Kraków-Balice Airport (EPKK) | Perugia / San Egidio Airport (LIRZ) | 2026-04-03 08:27 UTC | 2026-04-03 09:58 UTC | 1h 30m |
| N118RK |  | Northwest Arkansas Ntl Airport (KXNA) | Morrilton Airport (07AR) | 2026-04-03 09:40 UTC | 2026-04-03 09:56 UTC | 15m |
| IGO6547 | IndiGo | Bengaluru International Airport (VOBL) | Ozar Airport (VAOZ) | 2026-04-03 08:54 UTC | 2026-04-03 09:56 UTC | 1h 1m |
| ANA407 | All Nippon Airways | Tokyo International Airport (RJTT) | Yamagata Airport (RJSC) | 2026-04-03 09:25 UTC | 2026-04-03 09:55 UTC | 30m |
| EZY42CA | easyJet | Belfast International Airport (EGAA) | Liverpool John Lennon Airport (EGGP) | 2026-04-03 09:23 UTC | 2026-04-03 09:55 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
