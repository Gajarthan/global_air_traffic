# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_11:23:40_UTC-green)

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

**Latest saved flight:** 2026-04-04 11:23:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 11:23:40 UTC

- **15,471** saved flights
- **8,325** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **15,471** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **192,396.9 tonnes** estimated CO2 emissions
- **11,153,446 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 672 |
| 2 | Ryanair | 607 |
| 3 | IndiGo | 451 |
| 4 | EJA | 302 |
| 5 | American Airlines | 282 |
| 6 | Southwest Airlines | 226 |
| 7 | Lufthansa | 219 |
| 8 | ENY | 196 |
| 9 | Vueling | 167 |
| 10 | LATAM Airlines | 162 |
| 11 | AXM | 156 |
| 12 | All Nippon Airways | 141 |
| 13 | QLK | 137 |
| 14 | LXJ | 134 |
| 15 | Delta Air Lines | 125 |
| 16 | AZU | 117 |
| 17 | Swiss International | 117 |
| 18 | VIV | 111 |
| 19 | Japan Airlines | 105 |
| 20 | Alaska Airlines | 104 |
| 21 | EJU | 99 |
| 22 | WIF | 99 |
| 23 | United Airlines | 98 |
| 24 | AXB | 97 |
| 25 | AEE | 96 |
| 26 | Avianca | 96 |
| 27 | easyJet | 94 |
| 28 | EDV | 93 |
| 29 | Cathay Pacific | 88 |
| 30 | BRC | 87 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12271 |
| 2 | 🇮🇳 IN | 1375 |
| 3 | 🇪🇸 ES | 1219 |
| 4 | 🇦🇺 AU | 1205 |
| 5 | 🇧🇷 BR | 881 |
| 6 | 🇯🇵 JP | 849 |
| 7 | 🇩🇪 DE | 798 |
| 8 | 🇨🇴 CO | 755 |
| 9 | 🇨🇦 CA | 696 |
| 10 | 🇮🇹 IT | 686 |
| 11 | 🇬🇧 GB | 602 |
| 12 | 🇫🇷 FR | 546 |
| 13 | 🇲🇽 MX | 523 |
| 14 | 🇬🇷 GR | 432 |
| 15 | 🇨🇭 CH | 406 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 361 |
| 18 | 🇿🇦 ZA | 326 |
| 19 | 🇳🇴 NO | 325 |
| 20 | 🇵🇭 PH | 301 |
| 21 | 🇰🇷 KR | 286 |
| 22 | 🇹🇷 TR | 285 |
| 23 | 🇬🇹 GT | 267 |
| 24 | 🇵🇱 PL | 218 |
| 25 | 🇹🇭 TH | 214 |
| 26 | 🇲🇦 MA | 184 |
| 27 | 🇮🇩 ID | 173 |
| 28 | 🇲🇴 MO | 161 |
| 29 | 🇧🇸 BS | 159 |
| 30 | 🇲🇪 ME | 158 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 375 |
| 2 | Tokyo International Airport |  | JP | 295 |
| 3 | El Dorado International Airport |  | CO | 285 |
| 4 | Indira Gandhi International Airport |  | IN | 285 |
| 5 | Denver International Airport |  | US | 280 |
| 6 | Harry Reid International Airport |  | US | 214 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 203 |
| 8 | Frankfurt am Main International Airport |  | DE | 201 |
| 9 | La Aurora Airport |  | GT | 187 |
| 10 | Zurich Airport |  | CH | 186 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 166 |
| 13 | Macau International Airport |  | MO | 161 |
| 14 | Guaymaral Airport |  | CO | 157 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 153 |
| 16 | Bengaluru International Airport |  | IN | 153 |
| 17 | Chicago O'Hare International Airport |  | US | 147 |
| 18 | Charlotte/Douglas International Airport |  | US | 142 |
| 19 | Ninoy Aquino International Airport |  | PH | 138 |
| 20 | Madrid Barajas International Airport |  | ES | 138 |
| 21 | Congonhas Airport |  | BR | 137 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 135 |
| 23 | Netaji Subhash Chandra Bose International Airport |  | IN | 128 |
| 24 | Kuala Lumpur International Airport |  | MY | 127 |
| 25 | Tenerife Norte Airport |  | ES | 125 |
| 26 | Reno/Tahoe International Airport |  | US | 122 |
| 27 | Salt Lake City International Airport |  | US | 121 |
| 28 | Daniel K Inouye International Airport |  | US | 120 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 118 |
| 30 | Malpensa International Airport |  | IT | 117 |
| 31 | Charles de Gaulle International Airport |  | FR | 115 |
| 32 | Vitoria/Foronda Airport |  | ES | 113 |
| 33 | Barcelona International Airport |  | ES | 105 |
| 34 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 35 | Austin-Bergstrom International Airport |  | US | 103 |
| 36 | Pune Airport |  | IN | 103 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 101 |
| 38 | Gimpo International Airport |  | KR | 100 |
| 39 | Seattle-Tacoma International Airport |  | US | 98 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 98 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 70 | 14m | 114 km | 137.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 56 | 29m | 304 km | 293.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 47 | 31m | - | - |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 45 | 1h 26m | 910 km | 706.2 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 44 | 1h 46m | 1,156 km | 877.8 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 38 | 16m | 206 km | 135.1 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 37 | 22m | 99 km | 63.4 t |
| 11 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 35 | 28m | 275 km | 165.9 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 35 | 19m | 165 km | 99.6 t |
| 14 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 35 | 27m | 152 km | 91.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 16 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 34 | 53m | 556 km | 325.9 t |
| 17 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 32 | 1h 10m | 770 km | 425.1 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 32 | 1h 54m | 1,304 km | 719.9 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 28 | 1h 43m | 1,423 km | 687.2 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 27 | 23m | 252 km | 117.2 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 27 | 59m | 723 km | 336.6 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 27 | 11m | 127 km | 59.1 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 26 | 20m | 147 km | 65.8 t |
| 26 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 24 | 13m | 99 km | 41.2 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 22 | 16m | 183 km | 69.4 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 22 | 53m | 493 km | 187.2 t |
| 30 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 22 | 34m | 431 km | 163.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DEBFT | DEB | Gunzburg-Donauried Airport (EDMG) | Mengen-Hohentengen Airport (EDTM) | 2026-04-04 10:45 UTC | 2026-04-04 11:23 UTC | 38m |
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-04-04 11:13 UTC | 2026-04-04 11:23 UTC | 9m |
| N123KS |  | Lakeland Linder International Airport (KLAL) | Wauchula Municipal Airport (KCHN) | 2026-04-04 10:55 UTC | 2026-04-04 11:21 UTC | 25m |
| FIH40 | FIH | Hameenkyro Airport (EFHM) | Tampere-Pirkkala Airport (EFTP) | 2026-04-04 11:08 UTC | 2026-04-04 11:19 UTC | 11m |
| OKBIT | OKB | Letnany Airport (LKLT) | Letnany Airport (LKLT) | 2026-04-04 10:39 UTC | 2026-04-04 11:15 UTC | 36m |
| FD623 |  | Kalgoorlie-Boulder Airport (YPKG) | Kalgoorlie-Boulder Airport (YPKG) | 2026-04-04 10:55 UTC | 2026-04-04 11:07 UTC | 11m |
| N131HN |  | Marshall County Airport (KMPG) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-04-04 10:40 UTC | 2026-04-04 11:03 UTC | 23m |
| SAS50G | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Rakkestad Åstorp Airport (ENRK) | 2026-04-04 10:00 UTC | 2026-04-04 11:02 UTC | 1h 1m |
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-04-04 10:47 UTC | 2026-04-04 10:58 UTC | 11m |
| BNO92J | BNO | Bergen Airport Flesland (ENBR) | Eggemoen Airport (ENEG) | 2026-04-04 10:17 UTC | 2026-04-04 10:51 UTC | 34m |
| IGO6393 | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Ambala Air Force Station (VIAM) | 2026-04-04 09:19 UTC | 2026-04-04 10:49 UTC | 1h 29m |
| SAS4679 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Jayena Airport (LE84) | 2026-04-04 06:52 UTC | 2026-04-04 10:49 UTC | 3h 56m |
| RYR5933 | Ryanair | Niederrhein Airport (EDLV) | Dubrovnik Airport (LDDU) | 2026-04-04 08:54 UTC | 2026-04-04 10:48 UTC | 1h 53m |
| KAL1847 | Korean Air | Gimpo International Airport (RKSS) | Daegu Airport (RKTN) | 2026-04-04 10:16 UTC | 2026-04-04 10:42 UTC | 26m |
| ANA373 | All Nippon Airways | Chubu Centrair International Airport (RJGG) | Saga Airport (RJFS) | 2026-04-04 09:41 UTC | 2026-04-04 10:42 UTC | 1h 0m |
| ZSCTI | ZSC | Cape Town International Airport (FACT) | Morningside Farm Airport (FAMS) | 2026-04-04 07:54 UTC | 2026-04-04 10:41 UTC | 2h 47m |
| RYR88DM | Ryanair | London Stansted Airport (EGSS) | Argenton Sur Creuse Airport (LFEG) | 2026-04-04 09:40 UTC | 2026-04-04 10:41 UTC | 1h 1m |
| SAS2301 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Vinnu Airport (ENSU) | 2026-04-04 10:08 UTC | 2026-04-04 10:40 UTC | 31m |
| OAL098 | OAL | Limnos Airport (LGLM) | Olimboi Airport (LG56) | 2026-04-04 10:12 UTC | 2026-04-04 10:39 UTC | 27m |
| AIC6AB | Air India | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-04-04 10:19 UTC | 2026-04-04 10:38 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
