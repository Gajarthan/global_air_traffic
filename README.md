# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_10:27:56_UTC-green)

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

**Latest saved flight:** 2026-04-07 10:27:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-07 10:27:56 UTC

- **21,614** saved flights
- **10,684** unique routes
- **117** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **21,614** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **270,229.4 tonnes** estimated CO2 emissions
- **15,665,474 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 933 |
| 2 | Ryanair | 902 |
| 3 | IndiGo | 609 |
| 4 | American Airlines | 411 |
| 5 | EJA | 404 |
| 6 | Southwest Airlines | 308 |
| 7 | ENY | 292 |
| 8 | Lufthansa | 270 |
| 9 | Vueling | 228 |
| 10 | LATAM Airlines | 226 |
| 11 | AXM | 212 |
| 12 | Delta Air Lines | 190 |
| 13 | All Nippon Airways | 188 |
| 14 | LXJ | 186 |
| 15 | QLK | 183 |
| 16 | AZU | 169 |
| 17 | Swiss International | 159 |
| 18 | VIV | 157 |
| 19 | easyJet | 148 |
| 20 | Alaska Airlines | 147 |
| 21 | Japan Airlines | 145 |
| 22 | United Airlines | 143 |
| 23 | Avianca | 139 |
| 24 | EJU | 139 |
| 25 | AEE | 136 |
| 26 | WIF | 134 |
| 27 | EDV | 127 |
| 28 | AXB | 123 |
| 29 | Air France | 117 |
| 30 | BRC | 111 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 16971 |
| 2 | 🇮🇳 IN | 1852 |
| 3 | 🇪🇸 ES | 1699 |
| 4 | 🇦🇺 AU | 1545 |
| 5 | 🇧🇷 BR | 1231 |
| 6 | 🇯🇵 JP | 1179 |
| 7 | 🇨🇴 CO | 1175 |
| 8 | 🇮🇹 IT | 1083 |
| 9 | 🇩🇪 DE | 1065 |
| 10 | 🇨🇦 CA | 960 |
| 11 | 🇬🇧 GB | 852 |
| 12 | 🇫🇷 FR | 791 |
| 13 | 🇲🇽 MX | 727 |
| 14 | 🇬🇷 GR | 608 |
| 15 | 🇨🇭 CH | 585 |
| 16 | 🇲🇾 MY | 493 |
| 17 | 🇿🇦 ZA | 480 |
| 18 | 🇬🇹 GT | 464 |
| 19 | 🇳🇴 NO | 460 |
| 20 | 🇳🇿 NZ | 444 |
| 21 | 🇹🇷 TR | 421 |
| 22 | 🇵🇭 PH | 409 |
| 23 | 🇰🇷 KR | 381 |
| 24 | 🇹🇭 TH | 337 |
| 25 | 🇵🇱 PL | 316 |
| 26 | 🇲🇦 MA | 264 |
| 27 | 🇧🇸 BS | 235 |
| 28 | 🇮🇩 ID | 229 |
| 29 | 🇲🇪 ME | 226 |
| 30 | 🇳🇱 NL | 212 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 531 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 399 |
| 4 | Denver International Airport |  | US | 393 |
| 5 | Indira Gandhi International Airport |  | IN | 374 |
| 6 | La Aurora Airport |  | GT | 319 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 290 |
| 8 | Harry Reid International Airport |  | US | 283 |
| 9 | Zurich Airport |  | CH | 263 |
| 10 | Frankfurt am Main International Airport |  | DE | 241 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 232 |
| 12 | Chicago O'Hare International Airport |  | US | 232 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 231 |
| 14 | Guaymaral Airport |  | CO | 230 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 217 |
| 16 | Bengaluru International Airport |  | IN | 210 |
| 17 | Charlotte/Douglas International Airport |  | US | 208 |
| 18 | Macau International Airport |  | MO | 201 |
| 19 | Madrid Barajas International Airport |  | ES | 197 |
| 20 | Tenerife Norte Airport |  | ES | 196 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 191 |
| 22 | Ninoy Aquino International Airport |  | PH | 187 |
| 23 | Congonhas Airport |  | BR | 181 |
| 24 | Kuala Lumpur International Airport |  | MY | 174 |
| 25 | Salt Lake City International Airport |  | US | 170 |
| 26 | Malpensa International Airport |  | IT | 169 |
| 27 | Daniel K Inouye International Airport |  | US | 169 |
| 28 | Reno/Tahoe International Airport |  | US | 168 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 167 |
| 30 | Charles de Gaulle International Airport |  | FR | 160 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 159 |
| 32 | Miami International Airport |  | US | 153 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 149 |
| 34 | O. R. Tambo International Airport |  | ZA | 148 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 147 |
| 36 | Vitoria/Foronda Airport |  | ES | 146 |
| 37 | Pune Airport |  | IN | 144 |
| 38 | Barcelona International Airport |  | ES | 142 |
| 39 | Seattle-Tacoma International Airport |  | US | 138 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 137 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 102 | 1h 8m | 706 km | 1,241.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 84 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 82 | 24m | 225 km | 318.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 75 | 28m | 304 km | 393.2 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 63 | 1h 28m | 910 km | 988.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 62 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 60 | 1h 43m | 1,156 km | 1,197.0 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 50 | 19m | 165 km | 142.2 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 14 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 47 | 1h 13m | 770 km | 624.4 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 44 | 55m | 546 km | 414.3 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 43 | 52m | 556 km | 412.2 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 42 | 30m | 369 km | 267.3 t |
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 41 | 4m | - | - |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 41 | 9m | - | - |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 40 | 20m | 250 km | 172.8 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 38 | 46m | 452 km | 296.2 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 37 | 58m | 723 km | 461.3 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 32 | 20m | 147 km | 81.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HTY206 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-04-07 10:01 UTC | 2026-04-07 10:27 UTC | 26m |
| EVA805 | EVA Air | Taiwan Taoyuan International Airport (RCTP) | Macau International Airport (VMMC) | 2026-04-07 09:07 UTC | 2026-04-07 10:22 UTC | 1h 15m |
| EZY9 | easyJet | London Gatwick Airport (EGKK) | Durham Tees Valley Airport (EGNV) | 2026-04-07 08:29 UTC | 2026-04-07 10:13 UTC | 1h 43m |
| HKS51 | HKS | Humberside Airport (EGNJ) | EGYO (EGYO) | 2026-04-07 09:47 UTC | 2026-04-07 10:08 UTC | 20m |
| CHX21 | CHX | Aachen-Merzbruck Airport (EDKA) | Aachen-Merzbruck Airport (EDKA) | 2026-04-07 09:57 UTC | 2026-04-07 10:01 UTC | 4m |
| AXM6037 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-07 09:31 UTC | 2026-04-07 09:52 UTC | 21m |
| BSV | BSV | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-07 09:27 UTC | 2026-04-07 09:47 UTC | 19m |
| FHRSJ | FHR | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-07 09:16 UTC | 2026-04-07 09:45 UTC | 28m |
| YGI | YGI | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-04-07 08:59 UTC | 2026-04-07 09:42 UTC | 43m |
| DHACB | DHA | Mannheim-City Airport (EDFM) | Coleman Army Air Field (ETOR) | 2026-04-07 09:27 UTC | 2026-04-07 09:38 UTC | 11m |
| SHT12K | SHT | London Heathrow Airport (EGLL) | RAF Spadeadam (EGOM) | 2026-04-07 08:38 UTC | 2026-04-07 09:37 UTC | 58m |
| ECCZO | ECC | Cuatro Vientos Airport (LECU) | Casarrubios Del Monte Airport (LEMT) | 2026-04-07 09:20 UTC | 2026-04-07 09:30 UTC | 10m |
| ERE | ERE | Toowoomba Airport (YTWB) | Toowoomba Airport (YTWB) | 2026-04-07 09:23 UTC | 2026-04-07 09:30 UTC | 6m |
| HBZWE | HBZ | Bern Belp Airport (LSZB) | Raron Airport (LSTA) | 2026-04-07 09:10 UTC | 2026-04-07 09:29 UTC | 18m |
| IGO7313 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-04-07 08:19 UTC | 2026-04-07 09:29 UTC | 1h 9m |
| IGO7VH | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Jamshedpur Airport (VEJS) | 2026-04-07 08:47 UTC | 2026-04-07 09:28 UTC | 41m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-07 09:00 UTC | 2026-04-07 09:26 UTC | 26m |
| PLF120 | PLF | Szczecin-Goleniow Solidarność Airport (EPSC) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-07 08:32 UTC | 2026-04-07 09:25 UTC | 52m |
| KAL399T | Korean Air | Gimpo International Airport (RKSS) | Daegu Airport (RKTN) | 2026-04-07 09:01 UTC | 2026-04-07 09:25 UTC | 23m |
| RYR1HU | Ryanair | Vienna International Airport (LOWW) | Olbia / Costa Smeralda Airport (LIEO) | 2026-04-07 08:09 UTC | 2026-04-07 09:24 UTC | 1h 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
