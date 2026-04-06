# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_22:32:33_UTC-green)

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

**Latest saved flight:** 2026-04-06 22:32:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 22:32:33 UTC

- **21,006** saved flights
- **10,471** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **21,006** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **263,275.2 tonnes** estimated CO2 emissions
- **15,262,329 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 921 |
| 2 | Ryanair | 872 |
| 3 | IndiGo | 583 |
| 4 | American Airlines | 405 |
| 5 | EJA | 395 |
| 6 | Southwest Airlines | 303 |
| 7 | ENY | 286 |
| 8 | Lufthansa | 264 |
| 9 | Vueling | 225 |
| 10 | LATAM Airlines | 217 |
| 11 | AXM | 198 |
| 12 | Delta Air Lines | 183 |
| 13 | LXJ | 183 |
| 14 | All Nippon Airways | 176 |
| 15 | QLK | 167 |
| 16 | AZU | 165 |
| 17 | Swiss International | 154 |
| 18 | VIV | 153 |
| 19 | Alaska Airlines | 143 |
| 20 | easyJet | 143 |
| 21 | United Airlines | 142 |
| 22 | Avianca | 136 |
| 23 | EJU | 135 |
| 24 | Japan Airlines | 134 |
| 25 | AEE | 128 |
| 26 | EDV | 126 |
| 27 | WIF | 126 |
| 28 | AXB | 119 |
| 29 | Air France | 111 |
| 30 | BRC | 111 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 16699 |
| 2 | 🇮🇳 IN | 1777 |
| 3 | 🇪🇸 ES | 1666 |
| 4 | 🇦🇺 AU | 1430 |
| 5 | 🇧🇷 BR | 1199 |
| 6 | 🇨🇴 CO | 1155 |
| 7 | 🇯🇵 JP | 1092 |
| 8 | 🇮🇹 IT | 1035 |
| 9 | 🇩🇪 DE | 1029 |
| 10 | 🇨🇦 CA | 942 |
| 11 | 🇬🇧 GB | 826 |
| 12 | 🇫🇷 FR | 758 |
| 13 | 🇲🇽 MX | 715 |
| 14 | 🇬🇷 GR | 582 |
| 15 | 🇨🇭 CH | 566 |
| 16 | 🇲🇾 MY | 464 |
| 17 | 🇬🇹 GT | 462 |
| 18 | 🇿🇦 ZA | 461 |
| 19 | 🇳🇴 NO | 433 |
| 20 | 🇳🇿 NZ | 426 |
| 21 | 🇹🇷 TR | 411 |
| 22 | 🇵🇭 PH | 383 |
| 23 | 🇰🇷 KR | 351 |
| 24 | 🇹🇭 TH | 307 |
| 25 | 🇵🇱 PL | 306 |
| 26 | 🇲🇦 MA | 258 |
| 27 | 🇧🇸 BS | 234 |
| 28 | 🇲🇪 ME | 219 |
| 29 | 🇮🇩 ID | 214 |
| 30 | 🇳🇱 NL | 209 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 523 |
| 2 | El Dorado International Airport |  | CO | 434 |
| 3 | Denver International Airport |  | US | 387 |
| 4 | Tokyo International Airport |  | JP | 378 |
| 5 | Indira Gandhi International Airport |  | IN | 364 |
| 6 | La Aurora Airport |  | GT | 317 |
| 7 | Harry Reid International Airport |  | US | 279 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 276 |
| 9 | Zurich Airport |  | CH | 256 |
| 10 | Frankfurt am Main International Airport |  | DE | 236 |
| 11 | Chicago O'Hare International Airport |  | US | 229 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 228 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 227 |
| 14 | Guaymaral Airport |  | CO | 227 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 205 |
| 16 | Charlotte/Douglas International Airport |  | US | 203 |
| 17 | Macau International Airport |  | MO | 200 |
| 18 | Bengaluru International Airport |  | IN | 200 |
| 19 | Madrid Barajas International Airport |  | ES | 195 |
| 20 | Tenerife Norte Airport |  | ES | 191 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 185 |
| 22 | Congonhas Airport |  | BR | 177 |
| 23 | Ninoy Aquino International Airport |  | PH | 174 |
| 24 | Salt Lake City International Airport |  | US | 166 |
| 25 | Reno/Tahoe International Airport |  | US | 165 |
| 26 | Daniel K Inouye International Airport |  | US | 163 |
| 27 | Malpensa International Airport |  | IT | 162 |
| 28 | Kuala Lumpur International Airport |  | MY | 161 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 155 |
| 30 | Charles de Gaulle International Airport |  | FR | 153 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 153 |
| 32 | Miami International Airport |  | US | 150 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 147 |
| 34 | Vitoria/Foronda Airport |  | ES | 145 |
| 35 | O. R. Tambo International Airport |  | ZA | 143 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 142 |
| 37 | Barcelona International Airport |  | ES | 140 |
| 38 | Pune Airport |  | IN | 140 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 137 |
| 40 | Seattle-Tacoma International Airport |  | US | 135 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 95 | 1h 8m | 706 km | 1,156.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 92 | 14m | 114 km | 180.4 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 83 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 74 | 24m | 225 km | 287.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 69 | 28m | 304 km | 361.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 60 | 1h 27m | 910 km | 941.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 59 | 1h 43m | 1,156 km | 1,177.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 58 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 56 | 16m | 206 km | 199.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 46 | 19m | 165 km | 130.8 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 45 | 1h 12m | 770 km | 597.8 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 44 | 23m | 252 km | 191.0 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 42 | 55m | 546 km | 395.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 42 | 30m | 369 km | 267.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 42 | 52m | 556 km | 402.6 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 40 | 10m | - | - |
| 21 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 39 | 4m | - | - |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 39 | 20m | 250 km | 168.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 36 | 58m | 723 km | 448.8 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 36 | 46m | 452 km | 280.6 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 33 | 12m | 15 km | 8.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 32 | 1h 22m | 961 km | 530.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6641R |  | Wiley Post Airport (KPWA) | Elk City Regional Business Airport (KELK) | 2026-04-06 21:59 UTC | 2026-04-06 22:32 UTC | 32m |
| N186CS |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-04-06 21:46 UTC | 2026-04-06 22:30 UTC | 43m |
| N659MW |  | Agro-West Airport (5CA7) | San Carlos Airport (KSQL) | 2026-04-06 21:50 UTC | 2026-04-06 22:30 UTC | 39m |
| N202SF |  | Moraine Air Park (KI73) | 2OH9 (2OH9) | 2026-04-06 21:58 UTC | 2026-04-06 22:23 UTC | 24m |
| N399MA |  | KU42 (KU42) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-06 21:58 UTC | 2026-04-06 22:21 UTC | 22m |
| N334HP |  | Yucca Valley Airport (KL22) | Van Nuys Airport (KVNY) | 2026-04-06 21:39 UTC | 2026-04-06 22:21 UTC | 41m |
| N24BQ |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-04-06 20:00 UTC | 2026-04-06 22:13 UTC | 2h 12m |
| N313RR |  | Johnston Farm Airport (10NC) | Northeastern Regional Airport (KEDE) | 2026-04-06 21:45 UTC | 2026-04-06 22:13 UTC | 27m |
| N798SD |  | Augusta Regional At Bush Field (KAGS) | Mc Kinnon Airpark (48FL) | 2026-04-06 20:54 UTC | 2026-04-06 22:08 UTC | 1h 13m |
| SCAT21 | SCA | Mojave Air & Space Port/Rutan Field (KMHV) | California City Municipal Airport (KL71) | 2026-04-06 21:29 UTC | 2026-04-06 22:06 UTC | 36m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-06 21:47 UTC | 2026-04-06 22:05 UTC | 17m |
| N36387 |  | FL57 (FL57) | Bartow Executive Airport (KBOW) | 2026-04-06 21:44 UTC | 2026-04-06 22:05 UTC | 20m |
| N135LK |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-04-06 20:51 UTC | 2026-04-06 21:59 UTC | 1h 7m |
| CSG2694 | CSG | Amsterdam Airport Schiphol (EHAM) | Sharypovo Airport (UNKO) | 2026-04-06 16:15 UTC | 2026-04-06 21:58 UTC | 5h 43m |
| XE1182 |  | Harry Reid International Airport (KLAS) | Santa Monica Municipal Airport (KSMO) | 2026-04-06 20:59 UTC | 2026-04-06 21:56 UTC | 57m |
| N100BW |  | Talkeetna Airport (PATK) | Mc Kinley Country Airport (81AK) | 2026-04-06 21:21 UTC | 2026-04-06 21:56 UTC | 34m |
| SKW5689 | SkyWest Airlines | Mc Elroy Airfield (K20V) | Denver International Airport (KDEN) | 2026-04-06 21:32 UTC | 2026-04-06 21:53 UTC | 20m |
| CFNCH | CFN | Banff Airport (CYBA) | Banff Airport (CYBA) | 2026-04-06 21:39 UTC | 2026-04-06 21:50 UTC | 11m |
| N610GG |  | Pompano Beach Airpark (KPMP) | Cape Canaveral Space Force Station Skid Strip (KXMR) | 2026-04-06 21:16 UTC | 2026-04-06 21:50 UTC | 34m |
| N288SF |  | Columbus Airport (KCSG) | Nashville International Airport (KBNA) | 2026-04-06 21:03 UTC | 2026-04-06 21:50 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
