# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_21:47:16_UTC-green)

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

**Latest saved flight:** 2026-04-05 21:47:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 21:47:16 UTC

- **19,085** saved flights
- **9,661** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **19,085** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **241,487.4 tonnes** estimated CO2 emissions
- **13,999,270 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 839 |
| 2 | Ryanair | 789 |
| 3 | IndiGo | 540 |
| 4 | American Airlines | 364 |
| 5 | EJA | 354 |
| 6 | Southwest Airlines | 277 |
| 7 | ENY | 262 |
| 8 | Lufthansa | 256 |
| 9 | Vueling | 210 |
| 10 | LATAM Airlines | 203 |
| 11 | AXM | 191 |
| 12 | Delta Air Lines | 169 |
| 13 | LXJ | 167 |
| 14 | All Nippon Airways | 161 |
| 15 | QLK | 155 |
| 16 | AZU | 148 |
| 17 | VIV | 144 |
| 18 | Swiss International | 142 |
| 19 | United Airlines | 131 |
| 20 | Alaska Airlines | 128 |
| 21 | Avianca | 126 |
| 22 | easyJet | 124 |
| 23 | Japan Airlines | 124 |
| 24 | EJU | 122 |
| 25 | AEE | 121 |
| 26 | WIF | 116 |
| 27 | EDV | 115 |
| 28 | AXB | 113 |
| 29 | Air France | 105 |
| 30 | Cathay Pacific | 105 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 15005 |
| 2 | 🇮🇳 IN | 1638 |
| 3 | 🇪🇸 ES | 1568 |
| 4 | 🇦🇺 AU | 1318 |
| 5 | 🇧🇷 BR | 1111 |
| 6 | 🇨🇴 CO | 1034 |
| 7 | 🇯🇵 JP | 998 |
| 8 | 🇩🇪 DE | 966 |
| 9 | 🇮🇹 IT | 908 |
| 10 | 🇨🇦 CA | 837 |
| 11 | 🇬🇧 GB | 743 |
| 12 | 🇫🇷 FR | 699 |
| 13 | 🇲🇽 MX | 654 |
| 14 | 🇬🇷 GR | 539 |
| 15 | 🇨🇭 CH | 505 |
| 16 | 🇬🇹 GT | 444 |
| 17 | 🇲🇾 MY | 441 |
| 18 | 🇿🇦 ZA | 411 |
| 19 | 🇳🇿 NZ | 404 |
| 20 | 🇳🇴 NO | 387 |
| 21 | 🇹🇷 TR | 367 |
| 22 | 🇵🇭 PH | 355 |
| 23 | 🇰🇷 KR | 325 |
| 24 | 🇵🇱 PL | 277 |
| 25 | 🇹🇭 TH | 274 |
| 26 | 🇲🇦 MA | 241 |
| 27 | 🇧🇸 BS | 215 |
| 28 | 🇮🇩 ID | 205 |
| 29 | 🇲🇴 MO | 198 |
| 30 | 🇲🇪 ME | 196 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 469 |
| 2 | El Dorado International Airport |  | CO | 393 |
| 3 | Denver International Airport |  | US | 355 |
| 4 | Indira Gandhi International Airport |  | IN | 343 |
| 5 | Tokyo International Airport |  | JP | 340 |
| 6 | La Aurora Airport |  | GT | 305 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 254 |
| 8 | Harry Reid International Airport |  | US | 249 |
| 9 | Zurich Airport |  | CH | 233 |
| 10 | Frankfurt am Main International Airport |  | DE | 228 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 208 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 205 |
| 13 | Chicago O'Hare International Airport |  | US | 201 |
| 14 | Guaymaral Airport |  | CO | 199 |
| 15 | Macau International Airport |  | MO | 198 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 191 |
| 17 | Charlotte/Douglas International Airport |  | US | 186 |
| 18 | Madrid Barajas International Airport |  | ES | 184 |
| 19 | Bengaluru International Airport |  | IN | 182 |
| 20 | Tenerife Norte Airport |  | ES | 174 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 173 |
| 22 | Congonhas Airport |  | BR | 164 |
| 23 | Ninoy Aquino International Airport |  | PH | 162 |
| 24 | Salt Lake City International Airport |  | US | 155 |
| 25 | Kuala Lumpur International Airport |  | MY | 155 |
| 26 | Daniel K Inouye International Airport |  | US | 151 |
| 27 | Reno/Tahoe International Airport |  | US | 150 |
| 28 | Malpensa International Airport |  | IT | 146 |
| 29 | Vitoria/Foronda Airport |  | ES | 144 |
| 30 | Charles de Gaulle International Airport |  | FR | 143 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 143 |
| 32 | Miami International Airport |  | US | 140 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 140 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 131 |
| 35 | Barcelona International Airport |  | ES | 130 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 129 |
| 37 | Pune Airport |  | IN | 128 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 127 |
| 39 | O. R. Tambo International Airport |  | ZA | 127 |
| 40 | Seattle-Tacoma International Airport |  | US | 121 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 86 | 14m | 114 km | 168.7 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 85 | 1h 7m | 706 km | 1,034.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 65 | 22m | 99 km | 111.3 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 55 | 1h 44m | 1,156 km | 1,097.2 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 53 | 16m | 206 km | 188.4 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 42 | 1h 53m | 1,304 km | 944.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 40 | 1h 11m | 770 km | 531.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 18 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 38 | 4m | - | - |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 37 | 1h 43m | 1,423 km | 908.0 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 37 | 23m | 252 km | 160.6 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 37 | 9m | - | - |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 35 | 13m | 99 km | 60.0 t |
| 24 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 35 | 30m | 114 km | 68.9 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 33 | 58m | 723 km | 411.4 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 30 | 20m | 250 km | 129.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 29 | 20m | 147 km | 73.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| XBUOC | XBU | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | Plan De Guadalupe International Airport (MMIO) | 2026-04-05 18:22 UTC | 2026-04-05 21:47 UTC | 3h 24m |
| EJA777 | EJA | Westchester County Airport (KHPN) | KHTO (KHTO) | 2026-04-05 21:25 UTC | 2026-04-05 21:45 UTC | 19m |
| N9100H |  | Warren "Bud" Woods Palmer Municipal Airport (PAAQ) | Wasilla Airport (PAWS) | 2026-04-05 20:47 UTC | 2026-04-05 21:40 UTC | 52m |
| N713CT |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-04-05 21:25 UTC | 2026-04-05 21:35 UTC | 10m |
| N432CA |  | Kalaeloa (John Rodgers Field) Airport (PHJR) | Daniel K Inouye International Airport (PHNL) | 2026-04-05 21:13 UTC | 2026-04-05 21:28 UTC | 14m |
| LOT7JF | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | EPGY (EPGY) | 2026-04-05 21:04 UTC | 2026-04-05 21:15 UTC | 10m |
| N483LP |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-04-05 20:11 UTC | 2026-04-05 21:11 UTC | 1h 0m |
| LXJ339 | LXJ | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-05 21:09 UTC | 2026-04-05 21:09 UTC | 0m |
| CNS1030 | CNS | Portsmouth International At Pease Airport (KPSM) | KHTO (KHTO) | 2026-04-05 20:11 UTC | 2026-04-05 21:07 UTC | 56m |
| JUMP4 | JUM | Eloy Municipal Airport (KE60) | Eloy Municipal Airport (KE60) | 2026-04-05 19:07 UTC | 2026-04-05 21:05 UTC | 1h 58m |
| CNS1209 | CNS | Jekyll Island Airport (K09J) | The Florida Keys Marathon International Airport (KMTH) | 2026-04-05 19:24 UTC | 2026-04-05 21:00 UTC | 1h 36m |
| QLK1519 | QLK | Canberra International Airport (YSCB) | Melbourne International Airport (YMML) | 2026-04-05 20:07 UTC | 2026-04-05 21:00 UTC | 52m |
| N423MG |  | Fort Lauderdale/Hollywood International Airport (KFLL) | The Florida Keys Marathon International Airport (KMTH) | 2026-04-05 20:24 UTC | 2026-04-05 20:56 UTC | 31m |
| EJA676 | EJA | Sarasota/Bradenton International Airport (KSRQ) | WV11 (WV11) | 2026-04-05 19:26 UTC | 2026-04-05 20:55 UTC | 1h 29m |
| WIF1H | WIF | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 2026-04-05 20:47 UTC | 2026-04-05 20:53 UTC | 5m |
| N459FG |  | Fort Lauderdale/Hollywood International Airport (KFLL) | Albert Whitted Airport (KSPG) | 2026-04-05 19:43 UTC | 2026-04-05 20:52 UTC | 1h 8m |
| ASA1068 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Bradshaw Army Airfield (PHSF) | 2026-04-05 20:34 UTC | 2026-04-05 20:52 UTC | 17m |
| PNC0995 | PNC | El Dorado International Airport (SKBO) | El Dorado International Airport (SKBO) | 2026-04-05 20:39 UTC | 2026-04-05 20:51 UTC | 12m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-05 20:39 UTC | 2026-04-05 20:51 UTC | 11m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-05 20:29 UTC | 2026-04-05 20:51 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
