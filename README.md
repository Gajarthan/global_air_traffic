# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_09:07:20_UTC-green)

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

**Latest saved flight:** 2026-04-07 09:07:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-07 09:07:20 UTC

- **21,522** saved flights
- **10,651** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **21,522** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **269,206.7 tonnes** estimated CO2 emissions
- **15,606,183 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 933 |
| 2 | Ryanair | 894 |
| 3 | IndiGo | 604 |
| 4 | American Airlines | 411 |
| 5 | EJA | 404 |
| 6 | Southwest Airlines | 308 |
| 7 | ENY | 292 |
| 8 | Lufthansa | 267 |
| 9 | Vueling | 228 |
| 10 | LATAM Airlines | 226 |
| 11 | AXM | 207 |
| 12 | Delta Air Lines | 190 |
| 13 | LXJ | 186 |
| 14 | All Nippon Airways | 185 |
| 15 | QLK | 182 |
| 16 | AZU | 169 |
| 17 | Swiss International | 159 |
| 18 | VIV | 157 |
| 19 | Alaska Airlines | 147 |
| 20 | easyJet | 146 |
| 21 | Japan Airlines | 144 |
| 22 | United Airlines | 143 |
| 23 | Avianca | 139 |
| 24 | EJU | 138 |
| 25 | AEE | 134 |
| 26 | WIF | 132 |
| 27 | EDV | 127 |
| 28 | AXB | 123 |
| 29 | Air France | 115 |
| 30 | BRC | 111 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 16969 |
| 2 | 🇮🇳 IN | 1839 |
| 3 | 🇪🇸 ES | 1686 |
| 4 | 🇦🇺 AU | 1533 |
| 5 | 🇧🇷 BR | 1231 |
| 6 | 🇨🇴 CO | 1175 |
| 7 | 🇯🇵 JP | 1169 |
| 8 | 🇮🇹 IT | 1067 |
| 9 | 🇩🇪 DE | 1054 |
| 10 | 🇨🇦 CA | 960 |
| 11 | 🇬🇧 GB | 841 |
| 12 | 🇫🇷 FR | 786 |
| 13 | 🇲🇽 MX | 727 |
| 14 | 🇬🇷 GR | 600 |
| 15 | 🇨🇭 CH | 582 |
| 16 | 🇲🇾 MY | 484 |
| 17 | 🇿🇦 ZA | 474 |
| 18 | 🇬🇹 GT | 464 |
| 19 | 🇳🇴 NO | 451 |
| 20 | 🇳🇿 NZ | 444 |
| 21 | 🇹🇷 TR | 420 |
| 22 | 🇵🇭 PH | 409 |
| 23 | 🇰🇷 KR | 377 |
| 24 | 🇹🇭 TH | 324 |
| 25 | 🇵🇱 PL | 313 |
| 26 | 🇲🇦 MA | 263 |
| 27 | 🇧🇸 BS | 235 |
| 28 | 🇮🇩 ID | 226 |
| 29 | 🇲🇪 ME | 224 |
| 30 | 🇳🇱 NL | 211 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 531 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 396 |
| 4 | Denver International Airport |  | US | 393 |
| 5 | Indira Gandhi International Airport |  | IN | 374 |
| 6 | La Aurora Airport |  | GT | 319 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 285 |
| 8 | Harry Reid International Airport |  | US | 283 |
| 9 | Zurich Airport |  | CH | 263 |
| 10 | Frankfurt am Main International Airport |  | DE | 241 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 232 |
| 12 | Chicago O'Hare International Airport |  | US | 232 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 231 |
| 14 | Guaymaral Airport |  | CO | 230 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 216 |
| 16 | Bengaluru International Airport |  | IN | 210 |
| 17 | Charlotte/Douglas International Airport |  | US | 208 |
| 18 | Macau International Airport |  | MO | 200 |
| 19 | Madrid Barajas International Airport |  | ES | 196 |
| 20 | Tenerife Norte Airport |  | ES | 193 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 191 |
| 22 | Ninoy Aquino International Airport |  | PH | 187 |
| 23 | Congonhas Airport |  | BR | 181 |
| 24 | Salt Lake City International Airport |  | US | 170 |
| 25 | Malpensa International Airport |  | IT | 169 |
| 26 | Daniel K Inouye International Airport |  | US | 169 |
| 27 | Kuala Lumpur International Airport |  | MY | 169 |
| 28 | Reno/Tahoe International Airport |  | US | 168 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 162 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 159 |
| 31 | Charles de Gaulle International Airport |  | FR | 158 |
| 32 | Miami International Airport |  | US | 153 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 147 |
| 34 | O. R. Tambo International Airport |  | ZA | 147 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 146 |
| 36 | Vitoria/Foronda Airport |  | ES | 146 |
| 37 | Pune Airport |  | IN | 143 |
| 38 | Barcelona International Airport |  | ES | 142 |
| 39 | Seattle-Tacoma International Airport |  | US | 138 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 137 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 101 | 1h 8m | 706 km | 1,229.7 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 84 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 82 | 24m | 225 km | 318.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 75 | 28m | 304 km | 393.2 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 63 | 1h 28m | 910 km | 988.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 61 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 60 | 1h 43m | 1,156 km | 1,197.0 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 48 | 19m | 165 km | 136.5 t |
| 14 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 47 | 1h 13m | 770 km | 624.4 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 44 | 55m | 546 km | 414.3 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 43 | 52m | 556 km | 412.2 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 42 | 30m | 369 km | 267.3 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 41 | 9m | - | - |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 40 | 4m | - | - |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 40 | 20m | 250 km | 172.8 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 37 | 58m | 723 km | 461.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 37 | 46m | 452 km | 288.4 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 32 | 20m | 147 km | 81.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WASP81 | WAS | Kecskemet Airport (LHKE) | Debrecen International Airport (LHDC) | 2026-04-07 08:50 UTC | 2026-04-07 09:07 UTC | 16m |
| N252EA |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-04-07 07:49 UTC | 2026-04-07 09:06 UTC | 1h 16m |
| KFN | KFN | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-07 08:14 UTC | 2026-04-07 08:53 UTC | 39m |
| FHSMB | FHS | Lyon-Bron Airport (LFLY) | Lyon-Bron Airport (LFLY) | 2026-04-07 08:09 UTC | 2026-04-07 08:50 UTC | 41m |
| DMLSH | DML | Worms Airport (EDFV) | Worms Airport (EDFV) | 2026-04-07 08:17 UTC | 2026-04-07 08:46 UTC | 29m |
| 2612 |  | Chiang Mai International Airport (VTCC) | Chiang Mai International Airport (VTCC) | 2026-04-07 07:51 UTC | 2026-04-07 08:42 UTC | 51m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-04-07 08:16 UTC | 2026-04-07 08:40 UTC | 23m |
| AA9999 |  | Phoenix Sky Harbor International Airport (KPHX) | Phoenix Sky Harbor International Airport (KPHX) | 2026-04-07 08:33 UTC | 2026-04-07 08:36 UTC | 2m |
| YOI | YOI | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-07 08:03 UTC | 2026-04-07 08:35 UTC | 32m |
| HTY204 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-04-07 07:27 UTC | 2026-04-07 08:29 UTC | 1h 1m |
| SAS71K | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Malpensa International Airport (LIMC) | 2026-04-07 06:36 UTC | 2026-04-07 08:29 UTC | 1h 52m |
| HBZZZ | HBZ | Hausen am Albis Airport (LSZN) | Wangen-Lachen Airport (LSPV) | 2026-04-07 07:12 UTC | 2026-04-07 08:26 UTC | 1h 14m |
| MILAN79 | MIL | Nimes-Arles-Camargue Airport (LFTW) | Fayence Airport (LFMF) | 2026-04-07 07:56 UTC | 2026-04-07 08:20 UTC | 24m |
| FDX1426 | FDX | Frederick W Smith International Airport (KMEM) | Austin-Bergstrom International Airport (KAUS) | 2026-04-07 07:01 UTC | 2026-04-07 08:19 UTC | 1h 17m |
| JL2325 |  | Osaka International Airport (RJOO) | Tajima Airport (RJBT) | 2026-04-07 08:05 UTC | 2026-04-07 08:19 UTC | 14m |
| ABL8821 | ABL | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-04-07 07:53 UTC | 2026-04-07 08:19 UTC | 25m |
| DAL2186 | Delta Air Lines | Seattle-Tacoma International Airport (KSEA) | Fairbanks International Airport (PAFA) | 2026-04-07 04:29 UTC | 2026-04-07 08:18 UTC | 3h 49m |
| AAH11 | AAH | Daniel K Inouye International Airport (PHNL) | Wheeler Army Air Field (PHHI) | 2026-04-07 08:04 UTC | 2026-04-07 08:18 UTC | 13m |
| NJE295K | NJE | Zurich Airport (LSZH) | Twenthe Airport (EHTW) | 2026-04-07 07:08 UTC | 2026-04-07 08:18 UTC | 1h 9m |
| DAH6180 | DAH | DAAX (DAAX) | Mostaganem Airport (DA14) | 2026-04-07 07:32 UTC | 2026-04-07 08:14 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
