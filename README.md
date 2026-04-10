# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_10:18:22_UTC-green)

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

**Latest saved flight:** 2026-04-10 10:18:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 10:18:22 UTC

- **26,566** saved flights
- **12,613** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **26,566** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **326,637.1 tonnes** estimated CO2 emissions
- **18,935,485 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1087 |
| 2 | SkyWest Airlines | 1082 |
| 3 | IndiGo | 714 |
| 4 | EJA | 473 |
| 5 | American Airlines | 471 |
| 6 | Southwest Airlines | 380 |
| 7 | ENY | 350 |
| 8 | Lufthansa | 338 |
| 9 | AXM | 275 |
| 10 | Vueling | 270 |
| 11 | LATAM Airlines | 259 |
| 12 | QLK | 245 |
| 13 | All Nippon Airways | 238 |
| 14 | Delta Air Lines | 220 |
| 15 | LXJ | 212 |
| 16 | AZU | 211 |
| 17 | Swiss International | 185 |
| 18 | Alaska Airlines | 180 |
| 19 | Japan Airlines | 177 |
| 20 | VIV | 176 |
| 21 | easyJet | 173 |
| 22 | WIF | 172 |
| 23 | EJU | 171 |
| 24 | AEE | 170 |
| 25 | United Airlines | 159 |
| 26 | EDV | 155 |
| 27 | Avianca | 150 |
| 28 | AXB | 146 |
| 29 | JetBlue | 140 |
| 30 | Air France | 138 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 20829 |
| 2 | 🇮🇳 IN | 2199 |
| 3 | 🇦🇺 AU | 1982 |
| 4 | 🇪🇸 ES | 1962 |
| 5 | 🇧🇷 BR | 1488 |
| 6 | 🇯🇵 JP | 1477 |
| 7 | 🇮🇹 IT | 1356 |
| 8 | 🇩🇪 DE | 1356 |
| 9 | 🇨🇴 CO | 1322 |
| 10 | 🇨🇦 CA | 1268 |
| 11 | 🇬🇧 GB | 1071 |
| 12 | 🇫🇷 FR | 999 |
| 13 | 🇲🇽 MX | 851 |
| 14 | 🇬🇷 GR | 763 |
| 15 | 🇨🇭 CH | 727 |
| 16 | 🇲🇾 MY | 662 |
| 17 | 🇳🇿 NZ | 602 |
| 18 | 🇳🇴 NO | 578 |
| 19 | 🇿🇦 ZA | 546 |
| 20 | 🇵🇭 PH | 508 |
| 21 | 🇹🇷 TR | 497 |
| 22 | 🇬🇹 GT | 490 |
| 23 | 🇰🇷 KR | 471 |
| 24 | 🇹🇭 TH | 469 |
| 25 | 🇵🇱 PL | 395 |
| 26 | 🇲🇦 MA | 324 |
| 27 | 🇧🇸 BS | 272 |
| 28 | 🇲🇪 ME | 267 |
| 29 | 🇮🇩 ID | 264 |
| 30 | 🇳🇱 NL | 262 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 623 |
| 2 | Tokyo International Airport |  | JP | 496 |
| 3 | El Dorado International Airport |  | CO | 492 |
| 4 | Indira Gandhi International Airport |  | IN | 453 |
| 5 | Denver International Airport |  | US | 448 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 372 |
| 7 | Harry Reid International Airport |  | US | 345 |
| 8 | La Aurora Airport |  | GT | 340 |
| 9 | Zurich Airport |  | CH | 310 |
| 10 | Frankfurt am Main International Airport |  | DE | 287 |
| 11 | Guaymaral Airport |  | CO | 276 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 275 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 274 |
| 14 | Chicago O'Hare International Airport |  | US | 272 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 269 |
| 16 | Macau International Airport |  | MO | 259 |
| 17 | Bengaluru International Airport |  | IN | 244 |
| 18 | Kuala Lumpur International Airport |  | MY | 244 |
| 19 | Charlotte/Douglas International Airport |  | US | 242 |
| 20 | Ninoy Aquino International Airport |  | PH | 236 |
| 21 | Tenerife Norte Airport |  | ES | 228 |
| 22 | Madrid Barajas International Airport |  | ES | 223 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 209 |
| 24 | Malpensa International Airport |  | IT | 209 |
| 25 | Salt Lake City International Airport |  | US | 206 |
| 26 | Congonhas Airport |  | BR | 205 |
| 27 | Daniel K Inouye International Airport |  | US | 201 |
| 28 | Reno/Tahoe International Airport |  | US | 194 |
| 29 | Charles de Gaulle International Airport |  | FR | 192 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 184 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 183 |
| 32 | Miami International Airport |  | US | 177 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 176 |
| 34 | O. R. Tambo International Airport |  | ZA | 173 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 172 |
| 36 | Barcelona International Airport |  | ES | 171 |
| 37 | Seattle-Tacoma International Airport |  | US | 169 |
| 38 | Capua Airport |  | IT | 167 |
| 39 | Vitoria/Foronda Airport |  | ES | 166 |
| 40 | Don Mueang International Airport |  | TH | 163 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 128 | 1h 8m | 706 km | 1,558.4 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 108 | 14m | 114 km | 211.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 104 | 24m | 225 km | 403.5 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 103 | 27m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 93 | 28m | 304 km | 487.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 77 | 1h 27m | 910 km | 1,208.3 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 68 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 68 | 27m | 152 km | 177.7 t |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 65 | 19m | 165 km | 184.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 60 | 1h 12m | 770 km | 797.1 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 57 | 55m | 546 km | 536.7 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 53 | 27m | 275 km | 251.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 53 | 31m | 369 km | 337.4 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 47 | 45m | 452 km | 366.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 22 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 45 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 43 | 13m | 99 km | 73.7 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 40 | 20m | 147 km | 101.2 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 29 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 36 | 26m | 215 km | 133.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 36 | 1h 21m | 961 km | 596.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SEJ709 | SEJ | Indira Gandhi International Airport (VIDP) | Adampur Air Force Station (VIAX) | 2026-04-10 09:42 UTC | 2026-04-10 10:18 UTC | 36m |
| PSABD | PSA | Fazenda Ponte Quinha Airport (SNWU) | Fazenda Ponte Quinha Airport (SNWU) | 2026-04-10 09:40 UTC | 2026-04-10 10:12 UTC | 32m |
| FHTIL | FHT | Barcelonnette - Saint-Pons Airport (LFMR) | Barcelonnette - Saint-Pons Airport (LFMR) | 2026-04-10 09:10 UTC | 2026-04-10 10:03 UTC | 53m |
| FGDJF | FGD | Peronne-Saint-Quentin Airport (LFAG) | Peronne-Saint-Quentin Airport (LFAG) | 2026-04-10 09:58 UTC | 2026-04-10 10:03 UTC | 5m |
| IAM1480 | IAM | Pratica Di Mare Airport (LIRE) | Napoli / Capodichino International Airport (LIRN) | 2026-04-10 09:30 UTC | 2026-04-10 10:02 UTC | 31m |
| BAF90 | BAF | Toulon-Hyeres Airport (LFTH) | Melsbroek Air Base (EBMB) | 2026-04-10 08:26 UTC | 2026-04-10 09:52 UTC | 1h 25m |
| OOAAC | OOA | Antwerp International Airport (Deurne) (EBAW) | Antwerp International Airport (Deurne) (EBAW) | 2026-04-10 09:07 UTC | 2026-04-10 09:48 UTC | 41m |
| SIA115 | Singapore Airlines | Kuala Lumpur International Airport (WMKK) | Hang Nadim Airport (WIDD) | 2026-04-10 08:48 UTC | 2026-04-10 09:43 UTC | 54m |
| OAL012 | OAL | Eleftherios Venizelos International Airport (LGAV) | Naxos Airport (LGNX) | 2026-04-10 09:22 UTC | 2026-04-10 09:43 UTC | 20m |
| PPXVJ | PPX | Fazenda Sao Francisco do Itaquere Airport (SDNL) | Fazenda Sao Francisco do Itaquere Airport (SDNL) | 2026-04-10 09:39 UTC | 2026-04-10 09:40 UTC | 1m |
| WZZ55 | Wizz Air | London Gatwick Airport (EGKK) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-10 07:48 UTC | 2026-04-10 09:39 UTC | 1h 51m |
| LOT3HB | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-10 08:48 UTC | 2026-04-10 09:31 UTC | 42m |
| RYR9AB | Ryanair | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-10 07:53 UTC | 2026-04-10 09:29 UTC | 1h 36m |
| WIF9VK | WIF | Bergen Airport Flesland (ENBR) | Molde Airport (ENML) | 2026-04-10 08:56 UTC | 2026-04-10 09:27 UTC | 30m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-10 09:03 UTC | 2026-04-10 09:27 UTC | 23m |
| PBD855 | PBD | Sheremetyevo International Airport (UUEE) | Gyumri Shirak Airport (UDSG) | 2026-04-10 06:25 UTC | 2026-04-10 09:23 UTC | 2h 57m |
| AUR501 | AUR | Alderney Airport (EGJA) | Southampton Airport (EGHI) | 2026-04-10 08:39 UTC | 2026-04-10 09:20 UTC | 40m |
| IBE05LL | Iberia | Madrid Barajas International Airport (LEMD) | Brussels Airport (EBBR) | 2026-04-10 07:23 UTC | 2026-04-10 09:19 UTC | 1h 56m |
| KLM1303 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Słupsk-Krępa Airport (EPSR) | 2026-04-10 08:13 UTC | 2026-04-10 09:19 UTC | 1h 6m |
|  |  | Winnipeg James Armstrong Richardson International Airport (CYWG) | Odessa / Strawberry Lakes Airstrip (CSL7) | 2026-04-10 08:34 UTC | 2026-04-10 09:17 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
