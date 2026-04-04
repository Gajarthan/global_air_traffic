# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_10:51:47_UTC-green)

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

**Latest saved flight:** 2026-04-04 10:51:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 10:51:47 UTC

- **15,373** saved flights
- **8,279** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **15,373** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **190,990.5 tonnes** estimated CO2 emissions
- **11,071,910 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 672 |
| 2 | Ryanair | 594 |
| 3 | IndiGo | 445 |
| 4 | EJA | 302 |
| 5 | American Airlines | 282 |
| 6 | Southwest Airlines | 226 |
| 7 | Lufthansa | 219 |
| 8 | ENY | 196 |
| 9 | Vueling | 165 |
| 10 | LATAM Airlines | 161 |
| 11 | AXM | 155 |
| 12 | QLK | 137 |
| 13 | All Nippon Airways | 135 |
| 14 | LXJ | 134 |
| 15 | Delta Air Lines | 125 |
| 16 | Swiss International | 117 |
| 17 | AZU | 115 |
| 18 | VIV | 111 |
| 19 | Alaska Airlines | 104 |
| 20 | Japan Airlines | 104 |
| 21 | EJU | 98 |
| 22 | United Airlines | 98 |
| 23 | WIF | 98 |
| 24 | AEE | 96 |
| 25 | Avianca | 96 |
| 26 | AXB | 96 |
| 27 | EDV | 93 |
| 28 | easyJet | 93 |
| 29 | Cathay Pacific | 88 |
| 30 | BRC | 87 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12263 |
| 2 | 🇮🇳 IN | 1360 |
| 3 | 🇦🇺 AU | 1203 |
| 4 | 🇪🇸 ES | 1195 |
| 5 | 🇧🇷 BR | 873 |
| 6 | 🇯🇵 JP | 831 |
| 7 | 🇩🇪 DE | 789 |
| 8 | 🇨🇴 CO | 755 |
| 9 | 🇨🇦 CA | 696 |
| 10 | 🇮🇹 IT | 675 |
| 11 | 🇬🇧 GB | 592 |
| 12 | 🇫🇷 FR | 540 |
| 13 | 🇲🇽 MX | 523 |
| 14 | 🇬🇷 GR | 430 |
| 15 | 🇨🇭 CH | 404 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 356 |
| 18 | 🇿🇦 ZA | 322 |
| 19 | 🇳🇴 NO | 319 |
| 20 | 🇵🇭 PH | 297 |
| 21 | 🇹🇷 TR | 284 |
| 22 | 🇰🇷 KR | 282 |
| 23 | 🇬🇹 GT | 267 |
| 24 | 🇵🇱 PL | 213 |
| 25 | 🇹🇭 TH | 208 |
| 26 | 🇲🇦 MA | 183 |
| 27 | 🇮🇩 ID | 171 |
| 28 | 🇲🇴 MO | 160 |
| 29 | 🇧🇸 BS | 159 |
| 30 | 🇲🇪 ME | 155 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 375 |
| 2 | Tokyo International Airport |  | JP | 288 |
| 3 | El Dorado International Airport |  | CO | 285 |
| 4 | Indira Gandhi International Airport |  | IN | 282 |
| 5 | Denver International Airport |  | US | 280 |
| 6 | Harry Reid International Airport |  | US | 214 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 203 |
| 8 | Frankfurt am Main International Airport |  | DE | 201 |
| 9 | La Aurora Airport |  | GT | 187 |
| 10 | Zurich Airport |  | CH | 186 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 166 |
| 13 | Macau International Airport |  | MO | 160 |
| 14 | Guaymaral Airport |  | CO | 157 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 153 |
| 16 | Bengaluru International Airport |  | IN | 152 |
| 17 | Chicago O'Hare International Airport |  | US | 147 |
| 18 | Charlotte/Douglas International Airport |  | US | 142 |
| 19 | Ninoy Aquino International Airport |  | PH | 136 |
| 20 | Madrid Barajas International Airport |  | ES | 136 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 135 |
| 22 | Congonhas Airport |  | BR | 135 |
| 23 | Netaji Subhash Chandra Bose International Airport |  | IN | 128 |
| 24 | Kuala Lumpur International Airport |  | MY | 126 |
| 25 | Tenerife Norte Airport |  | ES | 123 |
| 26 | Reno/Tahoe International Airport |  | US | 122 |
| 27 | Salt Lake City International Airport |  | US | 121 |
| 28 | Daniel K Inouye International Airport |  | US | 120 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 117 |
| 30 | Malpensa International Airport |  | IT | 115 |
| 31 | Charles de Gaulle International Airport |  | FR | 114 |
| 32 | Vitoria/Foronda Airport |  | ES | 113 |
| 33 | Barcelona International Airport |  | ES | 104 |
| 34 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 35 | Austin-Bergstrom International Airport |  | US | 103 |
| 36 | Pune Airport |  | IN | 103 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 100 |
| 38 | Gimpo International Airport |  | KR | 99 |
| 39 | Seattle-Tacoma International Airport |  | US | 98 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 98 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 70 | 1h 7m | 706 km | 852.3 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 70 | 14m | 114 km | 137.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 56 | 29m | 304 km | 293.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 46 | 31m | - | - |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 44 | 1h 46m | 1,156 km | 877.8 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 44 | 1h 26m | 910 km | 690.5 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 38 | 16m | 206 km | 135.1 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 37 | 22m | 99 km | 63.4 t |
| 11 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 35 | 28m | 275 km | 165.9 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 35 | 19m | 165 km | 99.6 t |
| 14 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 35 | 27m | 152 km | 91.5 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 34 | 53m | 556 km | 325.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 33 | 30m | 369 km | 210.1 t |
| 17 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 32 | 1h 10m | 770 km | 425.1 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 32 | 1h 54m | 1,304 km | 719.9 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 28 | 1h 43m | 1,423 km | 687.2 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 27 | 59m | 723 km | 336.6 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 26 | 20m | 147 km | 65.8 t |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 26 | 23m | 252 km | 112.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 26 | 46m | 452 km | 202.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 26 | 11m | 127 km | 56.9 t |
| 26 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 24 | 13m | 99 km | 41.2 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 22 | 16m | 183 km | 69.4 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 22 | 53m | 493 km | 187.2 t |
| 30 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 22 | 34m | 431 km | 163.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BNO92J | BNO | Bergen Airport Flesland (ENBR) | Eggemoen Airport (ENEG) | 2026-04-04 10:17 UTC | 2026-04-04 10:51 UTC | 34m |
| CNF419S | CNF | La Palma Airport (GCLA) | Tenerife Norte Airport (GCXO) | 2026-04-04 09:53 UTC | 2026-04-04 10:12 UTC | 18m |
| RYR9RQ | Ryanair | Barcelona International Airport (LEBL) | L'Aquila / Preturo Airport (LIAP) | 2026-04-04 08:46 UTC | 2026-04-04 10:04 UTC | 1h 18m |
| IGO7313 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-04-04 08:38 UTC | 2026-04-04 10:02 UTC | 1h 23m |
| EWG32ME | EWG | London Heathrow Airport (EGLL) | Stuttgart Airport (EDDS) | 2026-04-04 08:53 UTC | 2026-04-04 10:01 UTC | 1h 7m |
| DFALL | DFA | Hildesheim Airport (EDVM) | Hildesheim Airport (EDVM) | 2026-04-04 09:37 UTC | 2026-04-04 10:00 UTC | 22m |
| IBB55LF | IBB | Tenerife Norte Airport (GCXO) | Federico Garcia Lorca Airport (LEGR) | 2026-04-04 08:01 UTC | 2026-04-04 09:58 UTC | 1h 57m |
| SFJ0085 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-04 08:44 UTC | 2026-04-04 09:58 UTC | 1h 14m |
| RYR35CB | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Visoko Sport Airfield (LQVI) | 2026-04-04 08:42 UTC | 2026-04-04 09:55 UTC | 1h 13m |
| AGV02 | AGV | Saanen Airport (LSGK) | Bex Airport (LSGB) | 2026-04-04 09:52 UTC | 2026-04-04 09:54 UTC | 2m |
| FDX5015 | FDX | Narita International Airport (RJAA) | Akeno Airport (RJOE) | 2026-04-04 09:17 UTC | 2026-04-04 09:52 UTC | 34m |
| N299RP |  | Daniel K Inouye International Airport (PHNL) | Bradshaw Army Airfield (PHSF) | 2026-04-04 09:27 UTC | 2026-04-04 09:51 UTC | 23m |
| LLR875 | LLR | Dehradun Airport (VIDN) | Pantnagar Airport (VIPT) | 2026-04-04 09:22 UTC | 2026-04-04 09:49 UTC | 27m |
| RYR1963 | Ryanair | Memmingen Allgau Airport (EDJA) | Losinj Island Airport (LDLO) | 2026-04-04 09:03 UTC | 2026-04-04 09:47 UTC | 44m |
| EXS13LM | EXS | Glasgow International Airport (EGPF) | Dalaman International Airport (LTBS) | 2026-04-04 05:54 UTC | 2026-04-04 09:47 UTC | 3h 52m |
| SPGWM | SPG | John Paul II International Airport Kraków-Balice Airport (EPKK) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-04 09:34 UTC | 2026-04-04 09:47 UTC | 12m |
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-04-04 09:36 UTC | 2026-04-04 09:46 UTC | 10m |
| TVF37NP | TVF | Paris-Orly Airport (LFPO) | Mikonos Airport (LGMK) | 2026-04-04 06:50 UTC | 2026-04-04 09:46 UTC | 2h 55m |
| IBB95FY | IBB | Tenerife Norte Airport (GCXO) | Logrono-Agoncillo Airport (LELO) | 2026-04-04 07:11 UTC | 2026-04-04 09:44 UTC | 2h 32m |
| IBB97FU | IBB | Tenerife Norte Airport (GCXO) | La Morgal Airport (LEMR) | 2026-04-04 07:21 UTC | 2026-04-04 09:44 UTC | 2h 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
