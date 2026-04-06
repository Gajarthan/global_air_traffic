# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_20:14:32_UTC-green)

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

**Latest saved flight:** 2026-04-06 20:14:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 20:14:32 UTC

- **20,669** saved flights
- **10,324** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **20,669** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **259,260.9 tonnes** estimated CO2 emissions
- **15,029,618 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 896 |
| 2 | Ryanair | 860 |
| 3 | IndiGo | 580 |
| 4 | American Airlines | 398 |
| 5 | EJA | 383 |
| 6 | Southwest Airlines | 293 |
| 7 | ENY | 282 |
| 8 | Lufthansa | 264 |
| 9 | Vueling | 222 |
| 10 | LATAM Airlines | 213 |
| 11 | AXM | 198 |
| 12 | Delta Air Lines | 182 |
| 13 | LXJ | 178 |
| 14 | All Nippon Airways | 176 |
| 15 | QLK | 164 |
| 16 | AZU | 161 |
| 17 | Swiss International | 153 |
| 18 | VIV | 152 |
| 19 | easyJet | 141 |
| 20 | United Airlines | 140 |
| 21 | Alaska Airlines | 137 |
| 22 | EJU | 135 |
| 23 | Avianca | 134 |
| 24 | Japan Airlines | 134 |
| 25 | AEE | 127 |
| 26 | WIF | 126 |
| 27 | EDV | 122 |
| 28 | AXB | 119 |
| 29 | Air France | 111 |
| 30 | BRC | 110 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 16268 |
| 2 | 🇮🇳 IN | 1771 |
| 3 | 🇪🇸 ES | 1653 |
| 4 | 🇦🇺 AU | 1411 |
| 5 | 🇧🇷 BR | 1180 |
| 6 | 🇨🇴 CO | 1139 |
| 7 | 🇯🇵 JP | 1090 |
| 8 | 🇩🇪 DE | 1029 |
| 9 | 🇮🇹 IT | 1024 |
| 10 | 🇨🇦 CA | 913 |
| 11 | 🇬🇧 GB | 818 |
| 12 | 🇫🇷 FR | 756 |
| 13 | 🇲🇽 MX | 704 |
| 14 | 🇬🇷 GR | 579 |
| 15 | 🇨🇭 CH | 564 |
| 16 | 🇲🇾 MY | 464 |
| 17 | 🇬🇹 GT | 462 |
| 18 | 🇿🇦 ZA | 461 |
| 19 | 🇳🇴 NO | 433 |
| 20 | 🇳🇿 NZ | 418 |
| 21 | 🇹🇷 TR | 404 |
| 22 | 🇵🇭 PH | 380 |
| 23 | 🇰🇷 KR | 351 |
| 24 | 🇹🇭 TH | 307 |
| 25 | 🇵🇱 PL | 301 |
| 26 | 🇲🇦 MA | 256 |
| 27 | 🇧🇸 BS | 229 |
| 28 | 🇲🇪 ME | 218 |
| 29 | 🇮🇩 ID | 214 |
| 30 | 🇳🇱 NL | 208 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 511 |
| 2 | El Dorado International Airport |  | CO | 426 |
| 3 | Denver International Airport |  | US | 379 |
| 4 | Tokyo International Airport |  | JP | 377 |
| 5 | Indira Gandhi International Airport |  | IN | 364 |
| 6 | La Aurora Airport |  | GT | 317 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 274 |
| 8 | Harry Reid International Airport |  | US | 270 |
| 9 | Zurich Airport |  | CH | 254 |
| 10 | Frankfurt am Main International Airport |  | DE | 236 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 225 |
| 12 | Chicago O'Hare International Airport |  | US | 224 |
| 13 | Guaymaral Airport |  | CO | 224 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 220 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 204 |
| 16 | Macau International Airport |  | MO | 200 |
| 17 | Bengaluru International Airport |  | IN | 199 |
| 18 | Charlotte/Douglas International Airport |  | US | 198 |
| 19 | Madrid Barajas International Airport |  | ES | 194 |
| 20 | Tenerife Norte Airport |  | ES | 189 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 184 |
| 22 | Congonhas Airport |  | BR | 175 |
| 23 | Ninoy Aquino International Airport |  | PH | 172 |
| 24 | Salt Lake City International Airport |  | US | 166 |
| 25 | Reno/Tahoe International Airport |  | US | 162 |
| 26 | Kuala Lumpur International Airport |  | MY | 161 |
| 27 | Malpensa International Airport |  | IT | 160 |
| 28 | Daniel K Inouye International Airport |  | US | 158 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 154 |
| 30 | Charles de Gaulle International Airport |  | FR | 152 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 148 |
| 32 | Miami International Airport |  | US | 147 |
| 33 | Vitoria/Foronda Airport |  | ES | 145 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 144 |
| 35 | O. R. Tambo International Airport |  | ZA | 143 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 139 |
| 37 | Pune Airport |  | IN | 137 |
| 38 | Barcelona International Airport |  | ES | 136 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 133 |
| 40 | Seattle-Tacoma International Airport |  | US | 130 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 95 | 1h 8m | 706 km | 1,156.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 92 | 14m | 114 km | 180.4 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 82 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 74 | 24m | 225 km | 287.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 69 | 28m | 304 km | 361.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 60 | 1h 27m | 910 km | 941.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 59 | 1h 43m | 1,156 km | 1,177.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 58 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 55 | 16m | 206 km | 195.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 46 | 19m | 165 km | 130.8 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 44 | 23m | 252 km | 191.0 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 44 | 1h 12m | 770 km | 584.5 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 42 | 55m | 546 km | 395.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 42 | 52m | 556 km | 402.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 41 | 30m | 369 km | 261.0 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 40 | 10m | - | - |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 39 | 4m | - | - |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 39 | 20m | 250 km | 168.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 38 | 13m | 99 km | 65.2 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 36 | 46m | 452 km | 280.6 t |
| 26 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 35 | 58m | 723 km | 436.3 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 32 | 12m | 15 km | 8.4 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 31 | 20m | 147 km | 78.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N12442 |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-06 19:50 UTC | 2026-04-06 20:14 UTC | 23m |
| N525MG |  | Byron Airport (KC83) | Tracy Municipal Airport (KTCY) | 2026-04-06 19:49 UTC | 2026-04-06 20:13 UTC | 23m |
| RYR6LT | Ryanair | Dublin Airport (EIDW) | Glasgow International Airport (EGPF) | 2026-04-06 19:36 UTC | 2026-04-06 20:09 UTC | 33m |
| N188JB |  | Los Alamos Airport (KLAM) | Blanding Municipal Airport (KBDG) | 2026-04-06 18:51 UTC | 2026-04-06 20:04 UTC | 1h 13m |
| EJA312 | EJA | Phoenix Sky Harbor International Airport (KPHX) | Santa Monica Municipal Airport (KSMO) | 2026-04-06 18:57 UTC | 2026-04-06 20:03 UTC | 1h 5m |
| SCA43 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-04-06 19:55 UTC | 2026-04-06 20:02 UTC | 6m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-06 19:48 UTC | 2026-04-06 19:59 UTC | 10m |
| CNS1989 | CNS | Rockfish Airport (VG22) | Marion County Airport (KMAO) | 2026-04-06 18:57 UTC | 2026-04-06 19:57 UTC | 59m |
| SKW4262 | SkyWest Airlines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Hite Airport (SD49) | 2026-04-06 19:20 UTC | 2026-04-06 19:56 UTC | 36m |
| N48ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-04-06 18:24 UTC | 2026-04-06 19:55 UTC | 1h 30m |
| BRG594 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-04-06 19:29 UTC | 2026-04-06 19:55 UTC | 26m |
| RFS731 | RFS | Auburn Municipal Airport (KS50) | Portland-Hillsboro Airport (KHIO) | 2026-04-06 18:16 UTC | 2026-04-06 19:53 UTC | 1h 36m |
| HUSK06 | HUS | CFB Trenton (CYTR) | CFB Trenton (CYTR) | 2026-04-06 18:44 UTC | 2026-04-06 19:51 UTC | 1h 7m |
| N889CG |  | Napa County Airport (KAPC) | San Francisco International Airport (KSFO) | 2026-04-06 19:27 UTC | 2026-04-06 19:51 UTC | 24m |
| LYM3803 | LYM | Greenville Mid-Delta Airport (KGLH) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-04-06 18:46 UTC | 2026-04-06 19:49 UTC | 1h 2m |
| SWA9001 | Southwest Airlines | Dallas Love Field (KDAL) | Denver International Airport (KDEN) | 2026-04-06 18:13 UTC | 2026-04-06 19:49 UTC | 1h 36m |
| N733JP |  | Soldotna Airport (PASX) | Homer Airport (PAHO) | 2026-04-06 19:08 UTC | 2026-04-06 19:48 UTC | 39m |
| N770RM |  | Raleigh-Durham International Airport (KRDU) | Raleigh County Memorial Airport (KBKW) | 2026-04-06 19:20 UTC | 2026-04-06 19:48 UTC | 28m |
| N1DW |  | Long Beach (Daugherty Field) Airport (KLGB) | Henderson Executive Airport (KHND) | 2026-04-06 19:02 UTC | 2026-04-06 19:47 UTC | 45m |
| RAM811D | Royal Air Maroc | Frankfurt am Main International Airport (EDDF) | Ben Slimane Airport (GMMB) | 2026-04-06 16:48 UTC | 2026-04-06 19:46 UTC | 2h 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
