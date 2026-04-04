# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_07:22:50_UTC-green)

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

**Latest saved flight:** 2026-04-04 07:22:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 07:22:50 UTC

- **15,094** saved flights
- **8,185** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **15,094** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **186,905.7 tonnes** estimated CO2 emissions
- **10,835,115 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 672 |
| 2 | Ryanair | 572 |
| 3 | IndiGo | 427 |
| 4 | EJA | 302 |
| 5 | American Airlines | 282 |
| 6 | Southwest Airlines | 226 |
| 7 | Lufthansa | 213 |
| 8 | ENY | 196 |
| 9 | LATAM Airlines | 161 |
| 10 | Vueling | 158 |
| 11 | AXM | 148 |
| 12 | QLK | 137 |
| 13 | LXJ | 134 |
| 14 | All Nippon Airways | 129 |
| 15 | Delta Air Lines | 125 |
| 16 | AZU | 115 |
| 17 | Swiss International | 111 |
| 18 | VIV | 111 |
| 19 | Alaska Airlines | 104 |
| 20 | Japan Airlines | 99 |
| 21 | United Airlines | 98 |
| 22 | WIF | 97 |
| 23 | Avianca | 95 |
| 24 | EDV | 93 |
| 25 | AEE | 92 |
| 26 | AXB | 92 |
| 27 | EJU | 90 |
| 28 | easyJet | 90 |
| 29 | BRC | 87 |
| 30 | Cathay Pacific | 87 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12250 |
| 2 | 🇮🇳 IN | 1293 |
| 3 | 🇦🇺 AU | 1191 |
| 4 | 🇪🇸 ES | 1126 |
| 5 | 🇧🇷 BR | 873 |
| 6 | 🇯🇵 JP | 790 |
| 7 | 🇩🇪 DE | 769 |
| 8 | 🇨🇴 CO | 752 |
| 9 | 🇨🇦 CA | 694 |
| 10 | 🇮🇹 IT | 639 |
| 11 | 🇬🇧 GB | 569 |
| 12 | 🇲🇽 MX | 523 |
| 13 | 🇫🇷 FR | 510 |
| 14 | 🇬🇷 GR | 407 |
| 15 | 🇨🇭 CH | 379 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 333 |
| 18 | 🇳🇴 NO | 315 |
| 19 | 🇿🇦 ZA | 307 |
| 20 | 🇵🇭 PH | 289 |
| 21 | 🇹🇷 TR | 281 |
| 22 | 🇬🇹 GT | 267 |
| 23 | 🇰🇷 KR | 262 |
| 24 | 🇵🇱 PL | 206 |
| 25 | 🇹🇭 TH | 201 |
| 26 | 🇲🇦 MA | 180 |
| 27 | 🇮🇩 ID | 167 |
| 28 | 🇧🇸 BS | 159 |
| 29 | 🇲🇴 MO | 158 |
| 30 | 🇲🇪 ME | 153 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 374 |
| 2 | El Dorado International Airport |  | CO | 283 |
| 3 | Denver International Airport |  | US | 280 |
| 4 | Tokyo International Airport |  | JP | 274 |
| 5 | Indira Gandhi International Airport |  | IN | 273 |
| 6 | Harry Reid International Airport |  | US | 212 |
| 7 | Frankfurt am Main International Airport |  | DE | 198 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 191 |
| 9 | La Aurora Airport |  | GT | 187 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 11 | Zurich Airport |  | CH | 175 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 166 |
| 13 | Macau International Airport |  | MO | 158 |
| 14 | Guaymaral Airport |  | CO | 157 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 153 |
| 16 | Chicago O'Hare International Airport |  | US | 147 |
| 17 | Bengaluru International Airport |  | IN | 146 |
| 18 | Charlotte/Douglas International Airport |  | US | 142 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 135 |
| 20 | Congonhas Airport |  | BR | 135 |
| 21 | Madrid Barajas International Airport |  | ES | 133 |
| 22 | Ninoy Aquino International Airport |  | PH | 132 |
| 23 | Reno/Tahoe International Airport |  | US | 122 |
| 24 | Salt Lake City International Airport |  | US | 121 |
| 25 | Kuala Lumpur International Airport |  | MY | 119 |
| 26 | Daniel K Inouye International Airport |  | US | 118 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 118 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 117 |
| 29 | Tenerife Norte Airport |  | ES | 114 |
| 30 | Vitoria/Foronda Airport |  | ES | 112 |
| 31 | Malpensa International Airport |  | IT | 106 |
| 32 | Charles de Gaulle International Airport |  | FR | 106 |
| 33 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 34 | Austin-Bergstrom International Airport |  | US | 102 |
| 35 | Pune Airport |  | IN | 102 |
| 36 | Barcelona International Airport |  | ES | 98 |
| 37 | Seattle-Tacoma International Airport |  | US | 98 |
| 38 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 98 |
| 39 | Miami International Airport |  | US | 96 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 95 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 70 | 14m | 114 km | 137.3 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 66 | 1h 7m | 706 km | 803.6 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 58 | 24m | 225 km | 225.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 50 | 29m | 304 km | 262.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 44 | 1h 46m | 1,156 km | 877.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 42 | 1h 26m | 910 km | 659.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 42 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 38 | 16m | 206 km | 135.1 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 37 | 22m | 99 km | 63.4 t |
| 11 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 35 | 28m | 275 km | 165.9 t |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 35 | 27m | 152 km | 91.5 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 34 | 53m | 556 km | 325.9 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 32 | 1h 54m | 1,304 km | 719.9 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 31 | 30m | 369 km | 197.3 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 30 | 1h 10m | 770 km | 398.5 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 27 | 59m | 723 km | 336.6 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 26 | 23m | 252 km | 112.9 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 23 | 45m | 452 km | 179.3 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 23 | 13m | 99 km | 39.4 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 22 | 16m | 183 km | 69.4 t |
| 29 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 21 | 1h 15m | 924 km | 334.9 t |
| 30 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 21 | 20m | 250 km | 90.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JLK | JLK | Wollongong Airport (YWOL) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-04 07:00 UTC | 2026-04-04 07:22 UTC | 22m |
| N57BF |  | KU77 (KU77) | Wendover Airport (KENV) | 2026-04-04 06:11 UTC | 2026-04-04 07:14 UTC | 1h 2m |
| HLE27 | HLE | RAF Northolt (EGWU) | London City Airport (EGLC) | 2026-04-04 06:56 UTC | 2026-04-04 07:06 UTC | 9m |
| ZKIDU | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-04-04 06:42 UTC | 2026-04-04 07:00 UTC | 17m |
| HBZVS | HBZ | Courchevel Airport (LFLJ) | Muenster Aero Airport (LSPU) | 2026-04-04 06:34 UTC | 2026-04-04 06:53 UTC | 18m |
| KAL902 | Korean Air | Charles de Gaulle International Airport (LFPG) | Incheon International Airport (RKSI) | 2026-04-03 19:18 UTC | 2026-04-04 06:49 UTC | 11h 30m |
| DLH6YA | Lufthansa | Munich International Airport (EDDM) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-04 05:43 UTC | 2026-04-04 06:46 UTC | 1h 3m |
| RYR45XQ | Ryanair | Budapest Ferenc Liszt International Airport (LHBP) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-04 04:59 UTC | 2026-04-04 06:40 UTC | 1h 41m |
| TROY702 | TRO | Ducote Airpark (TS65) | Eldorado Airport (K27R) | 2026-04-04 06:15 UTC | 2026-04-04 06:40 UTC | 25m |
| PSQ | PSQ | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-04-04 06:26 UTC | 2026-04-04 06:40 UTC | 14m |
| PAG14 | PAG | Winnipeg James Armstrong Richardson International Airport (CYWG) | Brandon Municipal Airport (CYBR) | 2026-04-04 06:07 UTC | 2026-04-04 06:36 UTC | 29m |
| ANE74KE | ANE | Madrid Barajas International Airport (LEMD) | Santo Tome Del Puerto Airport (LETP) | 2026-04-04 06:10 UTC | 2026-04-04 06:33 UTC | 22m |
| KAL908 | Korean Air | London Heathrow Airport (EGLL) | Incheon International Airport (RKSI) | 2026-04-03 18:57 UTC | 2026-04-04 06:31 UTC | 11h 33m |
| ANE82BX | ANE | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 2026-04-04 06:03 UTC | 2026-04-04 06:31 UTC | 27m |
| LOG28CG | LOG | Isle of Man Airport (EGNS) | Manchester Airport (EGCC) | 2026-04-04 06:00 UTC | 2026-04-04 06:30 UTC | 30m |
| OAL2MS | OAL | Eleftherios Venizelos International Airport (LGAV) | Milos Airport (LGML) | 2026-04-04 06:11 UTC | 2026-04-04 06:27 UTC | 16m |
| AXM5305 | AXM | Kota Kinabalu International Airport (WBKK) | Changi Air Base (WSAC) | 2026-04-04 04:35 UTC | 2026-04-04 06:26 UTC | 1h 50m |
| N122JM |  | Bob Hope Airport (KBUR) | Reno/Tahoe International Airport (KRNO) | 2026-04-04 05:01 UTC | 2026-04-04 06:25 UTC | 1h 23m |
| RYR62MD | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Ifrane Airport (GMFI) | 2026-04-04 04:17 UTC | 2026-04-04 06:23 UTC | 2h 5m |
| JAL375 | Japan Airlines | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-04 05:10 UTC | 2026-04-04 06:22 UTC | 1h 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
