# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_10:33:13_UTC-green)

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

**Latest saved flight:** 2026-04-08 10:33:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 10:33:13 UTC

- **23,100** saved flights
- **11,257** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **23,100** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **286,884.2 tonnes** estimated CO2 emissions
- **16,630,966 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 971 |
| 2 | Ryanair | 953 |
| 3 | IndiGo | 649 |
| 4 | EJA | 422 |
| 5 | American Airlines | 421 |
| 6 | Southwest Airlines | 330 |
| 7 | ENY | 302 |
| 8 | Lufthansa | 293 |
| 9 | Vueling | 242 |
| 10 | AXM | 238 |
| 11 | LATAM Airlines | 230 |
| 12 | All Nippon Airways | 215 |
| 13 | QLK | 215 |
| 14 | Delta Air Lines | 200 |
| 15 | LXJ | 189 |
| 16 | AZU | 183 |
| 17 | Swiss International | 170 |
| 18 | Japan Airlines | 162 |
| 19 | VIV | 162 |
| 20 | Alaska Airlines | 158 |
| 21 | easyJet | 157 |
| 22 | EJU | 151 |
| 23 | United Airlines | 147 |
| 24 | AEE | 146 |
| 25 | WIF | 142 |
| 26 | Avianca | 139 |
| 27 | EDV | 135 |
| 28 | AXB | 130 |
| 29 | Air France | 124 |
| 30 | ANZ | 118 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 18022 |
| 2 | 🇮🇳 IN | 1970 |
| 3 | 🇪🇸 ES | 1781 |
| 4 | 🇦🇺 AU | 1734 |
| 5 | 🇯🇵 JP | 1333 |
| 6 | 🇧🇷 BR | 1290 |
| 7 | 🇨🇴 CO | 1181 |
| 8 | 🇮🇹 IT | 1173 |
| 9 | 🇩🇪 DE | 1161 |
| 10 | 🇨🇦 CA | 1032 |
| 11 | 🇬🇧 GB | 923 |
| 12 | 🇫🇷 FR | 853 |
| 13 | 🇲🇽 MX | 747 |
| 14 | 🇬🇷 GR | 666 |
| 15 | 🇨🇭 CH | 642 |
| 16 | 🇲🇾 MY | 560 |
| 17 | 🇿🇦 ZA | 502 |
| 18 | 🇳🇿 NZ | 497 |
| 19 | 🇳🇴 NO | 493 |
| 20 | 🇬🇹 GT | 467 |
| 21 | 🇵🇭 PH | 444 |
| 22 | 🇹🇷 TR | 439 |
| 23 | 🇰🇷 KR | 424 |
| 24 | 🇹🇭 TH | 369 |
| 25 | 🇵🇱 PL | 336 |
| 26 | 🇲🇦 MA | 280 |
| 27 | 🇮🇩 ID | 248 |
| 28 | 🇧🇸 BS | 243 |
| 29 | 🇲🇪 ME | 236 |
| 30 | 🇳🇱 NL | 228 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 550 |
| 2 | Tokyo International Airport |  | JP | 444 |
| 3 | El Dorado International Airport |  | CO | 442 |
| 4 | Denver International Airport |  | US | 407 |
| 5 | Indira Gandhi International Airport |  | IN | 402 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 322 |
| 7 | La Aurora Airport |  | GT | 322 |
| 8 | Harry Reid International Airport |  | US | 308 |
| 9 | Zurich Airport |  | CH | 282 |
| 10 | Frankfurt am Main International Airport |  | DE | 255 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 241 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 241 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 241 |
| 14 | Chicago O'Hare International Airport |  | US | 238 |
| 15 | Guaymaral Airport |  | CO | 236 |
| 16 | Macau International Airport |  | MO | 223 |
| 17 | Bengaluru International Airport |  | IN | 222 |
| 18 | Charlotte/Douglas International Airport |  | US | 214 |
| 19 | Madrid Barajas International Airport |  | ES | 205 |
| 20 | Tenerife Norte Airport |  | ES | 205 |
| 21 | Ninoy Aquino International Airport |  | PH | 204 |
| 22 | Kuala Lumpur International Airport |  | MY | 202 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 192 |
| 24 | Malpensa International Airport |  | IT | 187 |
| 25 | Congonhas Airport |  | BR | 186 |
| 26 | Salt Lake City International Airport |  | US | 182 |
| 27 | Daniel K Inouye International Airport |  | US | 177 |
| 28 | Reno/Tahoe International Airport |  | US | 175 |
| 29 | Charles de Gaulle International Airport |  | FR | 172 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 170 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 162 |
| 32 | Miami International Airport |  | US | 156 |
| 33 | O. R. Tambo International Airport |  | ZA | 156 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 155 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 152 |
| 36 | Pune Airport |  | IN | 152 |
| 37 | Seattle-Tacoma International Airport |  | US | 150 |
| 38 | Vitoria/Foronda Airport |  | ES | 150 |
| 39 | Barcelona International Airport |  | ES | 148 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 140 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 113 | 1h 8m | 706 km | 1,375.8 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 90 | 24m | 225 km | 349.2 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 87 | 27m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 83 | 28m | 304 km | 435.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 70 | 1h 27m | 910 km | 1,098.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 66 | 27m | 152 km | 172.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 62 | 1h 42m | 1,156 km | 1,236.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 55 | 19m | 165 km | 156.4 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 51 | 55m | 546 km | 480.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 51 | 1h 13m | 770 km | 677.5 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 49 | 27m | 275 km | 232.2 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 46 | 31m | 369 km | 292.8 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 45 | 52m | 556 km | 431.4 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 43 | 46m | 452 km | 335.1 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 43 | 20m | 250 km | 185.7 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 42 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 39 | 1h 43m | 1,423 km | 957.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 33 | 20m | 147 km | 83.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HSGDZ | HSG | U-Tapao International Airport (VTBU) | U-Tapao International Airport (VTBU) | 2026-04-08 09:34 UTC | 2026-04-08 10:33 UTC | 58m |
| GPMMC | GPM | EGYO (EGYO) | Norwich International Airport (EGSH) | 2026-04-08 09:54 UTC | 2026-04-08 10:31 UTC | 37m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-07 20:02 UTC | 2026-04-08 10:30 UTC | 14h 28m |
| VLG9FT | Vueling | Palma De Mallorca Airport (LEPA) | Federico Garcia Lorca Airport (LEGR) | 2026-04-08 09:27 UTC | 2026-04-08 10:29 UTC | 1h 2m |
| DRAG381 | DRA | Grenoble Le Versoud Airport (LFLG) | L'alpe D'huez Airport (LFHU) | 2026-04-08 10:12 UTC | 2026-04-08 10:25 UTC | 12m |
| RYR6848 | Ryanair | Copenhagen Kastrup Airport (EKCH) | Oksywie Military Air Base (EPOK) | 2026-04-08 09:50 UTC | 2026-04-08 10:23 UTC | 33m |
| NIW | NIW | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-04-08 09:39 UTC | 2026-04-08 10:19 UTC | 40m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-07 19:19 UTC | 2026-04-08 10:19 UTC | 14h 59m |
| CARD56 | CAR | G 501 Airport (RK52) | A 511 Airport (RKSG) | 2026-04-08 08:53 UTC | 2026-04-08 10:16 UTC | 1h 23m |
| FC79 |  | Gimpo International Airport (RKSS) | Gimpo International Airport (RKSS) | 2026-04-08 10:01 UTC | 2026-04-08 10:13 UTC | 12m |
| HKS51 | HKS | Humberside Airport (EGNJ) | EGYO (EGYO) | 2026-04-08 09:52 UTC | 2026-04-08 10:12 UTC | 19m |
| QLK1531 | QLK | Canberra International Airport (YSCB) | Melbourne Essendon Airport (YMEN) | 2026-04-08 08:58 UTC | 2026-04-08 10:10 UTC | 1h 12m |
| RYR7KW | Ryanair | Ciampino Airport (LIRA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-08 08:19 UTC | 2026-04-08 10:10 UTC | 1h 50m |
| KEEP88 | KEE | A 511 Airport (RKSG) | A 511 Airport (RKSG) | 2026-04-08 09:00 UTC | 2026-04-08 10:08 UTC | 1h 7m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-04-08 09:25 UTC | 2026-04-08 10:03 UTC | 38m |
| URSA26 | URS | Ladd Army Air Field (PAFB) | Clear Creek Airport (2AK2) | 2026-04-08 08:25 UTC | 2026-04-08 10:00 UTC | 1h 35m |
| AXM348 | AXM | Kuala Lumpur International Airport (WMKK) | Tunggul Wulung Airport (WIHL) | 2026-04-08 08:07 UTC | 2026-04-08 09:54 UTC | 1h 47m |
| OOGQN | OOG | Antwerp International Airport (Deurne) (EBAW) | Rotterdam Airport (EHRD) | 2026-04-08 09:18 UTC | 2026-04-08 09:54 UTC | 36m |
| AFR11ZB | Air France | Charles de Gaulle International Airport (LFPG) | Stockholm-Arlanda Airport (ESSA) | 2026-04-08 07:42 UTC | 2026-04-08 09:53 UTC | 2h 10m |
| VLG1869 | Vueling | Stuttgart Airport (EDDS) | Barcelona International Airport (LEBL) | 2026-04-08 08:10 UTC | 2026-04-08 09:52 UTC | 1h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
