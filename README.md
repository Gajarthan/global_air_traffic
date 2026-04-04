# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_20:53:52_UTC-green)

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

**Latest saved flight:** 2026-04-04 20:53:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 20:53:52 UTC

- **16,844** saved flights
- **8,881** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **16,844** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **210,379.0 tonnes** estimated CO2 emissions
- **12,195,882 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 737 |
| 2 | Ryanair | 684 |
| 3 | IndiGo | 480 |
| 4 | EJA | 322 |
| 5 | American Airlines | 306 |
| 6 | Lufthansa | 238 |
| 7 | Southwest Airlines | 238 |
| 8 | ENY | 224 |
| 9 | Vueling | 189 |
| 10 | LATAM Airlines | 181 |
| 11 | AXM | 161 |
| 12 | LXJ | 146 |
| 13 | Delta Air Lines | 143 |
| 14 | All Nippon Airways | 141 |
| 15 | QLK | 137 |
| 16 | AZU | 129 |
| 17 | VIV | 125 |
| 18 | Swiss International | 124 |
| 19 | Alaska Airlines | 111 |
| 20 | United Airlines | 111 |
| 21 | EJU | 109 |
| 22 | Avianca | 107 |
| 23 | Japan Airlines | 107 |
| 24 | easyJet | 106 |
| 25 | AEE | 105 |
| 26 | AXB | 105 |
| 27 | EDV | 103 |
| 28 | WIF | 102 |
| 29 | BRC | 100 |
| 30 | GLO | 97 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13429 |
| 2 | 🇮🇳 IN | 1464 |
| 3 | 🇪🇸 ES | 1397 |
| 4 | 🇦🇺 AU | 1210 |
| 5 | 🇧🇷 BR | 984 |
| 6 | 🇩🇪 DE | 871 |
| 7 | 🇨🇴 CO | 866 |
| 8 | 🇯🇵 JP | 860 |
| 9 | 🇮🇹 IT | 783 |
| 10 | 🇨🇦 CA | 751 |
| 11 | 🇬🇧 GB | 658 |
| 12 | 🇫🇷 FR | 608 |
| 13 | 🇲🇽 MX | 577 |
| 14 | 🇬🇷 GR | 457 |
| 15 | 🇨🇭 CH | 444 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 369 |
| 18 | 🇿🇦 ZA | 350 |
| 19 | 🇳🇴 NO | 339 |
| 20 | 🇬🇹 GT | 324 |
| 21 | 🇹🇷 TR | 308 |
| 22 | 🇵🇭 PH | 305 |
| 23 | 🇰🇷 KR | 291 |
| 24 | 🇵🇱 PL | 239 |
| 25 | 🇹🇭 TH | 232 |
| 26 | 🇲🇦 MA | 206 |
| 27 | 🇧🇸 BS | 190 |
| 28 | 🇮🇩 ID | 177 |
| 29 | 🇲🇪 ME | 173 |
| 30 | 🇲🇴 MO | 169 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 403 |
| 2 | El Dorado International Airport |  | CO | 324 |
| 3 | Denver International Airport |  | US | 311 |
| 4 | Indira Gandhi International Airport |  | IN | 303 |
| 5 | Tokyo International Airport |  | JP | 299 |
| 6 | La Aurora Airport |  | GT | 227 |
| 7 | Harry Reid International Airport |  | US | 223 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 215 |
| 9 | Frankfurt am Main International Airport |  | DE | 212 |
| 10 | Zurich Airport |  | CH | 203 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 182 |
| 12 | Guaymaral Airport |  | CO | 180 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 174 |
| 15 | Macau International Airport |  | MO | 169 |
| 16 | Chicago O'Hare International Airport |  | US | 163 |
| 17 | Bengaluru International Airport |  | IN | 161 |
| 18 | Charlotte/Douglas International Airport |  | US | 156 |
| 19 | Madrid Barajas International Airport |  | ES | 156 |
| 20 | Congonhas Airport |  | BR | 152 |
| 21 | Tenerife Norte Airport |  | ES | 150 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 148 |
| 23 | Ninoy Aquino International Airport |  | PH | 140 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 136 |
| 25 | Salt Lake City International Airport |  | US | 135 |
| 26 | Malpensa International Airport |  | IT | 132 |
| 27 | Reno/Tahoe International Airport |  | US | 132 |
| 28 | Kuala Lumpur International Airport |  | MY | 131 |
| 29 | Daniel K Inouye International Airport |  | US | 129 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 128 |
| 31 | Vitoria/Foronda Airport |  | ES | 125 |
| 32 | Charles de Gaulle International Airport |  | FR | 123 |
| 33 | Barcelona International Airport |  | ES | 119 |
| 34 | Miami International Airport |  | US | 118 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 115 |
| 36 | Pune Airport |  | IN | 115 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 110 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 109 |
| 39 | Seattle-Tacoma International Airport |  | US | 106 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 106 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 76 | 14m | 114 km | 149.1 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 68 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 51 | 1h 45m | 1,156 km | 1,017.4 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 49 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 46 | 26m | 152 km | 120.2 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 44 | 22m | 99 km | 75.4 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 43 | 16m | 206 km | 152.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 40 | 28m | 275 km | 189.5 t |
| 13 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 15 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 35 | 1h 54m | 1,304 km | 787.4 t |
| 17 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 32 | 1h 43m | 1,423 km | 785.3 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 30 | 58m | 723 km | 374.0 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 30 | 13m | 99 km | 51.4 t |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 25 | 1h 24m | 961 km | 414.4 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 24 | 12m | 15 km | 6.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRCAT14 | BRC | Roswell Air Center Airport (KROW) | 81NM (81NM) | 2026-04-04 19:54 UTC | 2026-04-04 20:53 UTC | 59m |
| N9454B |  | Byron Airport (KC83) | Byron Airport (KC83) | 2026-04-04 20:11 UTC | 2026-04-04 20:53 UTC | 41m |
| BRG530 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-04-04 20:21 UTC | 2026-04-04 20:50 UTC | 29m |
| N18KH |  | Naples Municipal Airport (KAPF) | Marco Island Executive Airport (KMKY) | 2026-04-04 20:21 UTC | 2026-04-04 20:44 UTC | 23m |
|  |  | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-04-04 20:25 UTC | 2026-04-04 20:36 UTC | 10m |
| N3288 |  | Palo Alto Airport (KPAO) | Livermore Municipal Airport (KLVK) | 2026-04-04 19:51 UTC | 2026-04-04 20:33 UTC | 42m |
|  |  | Clifford Field (1CO4) | Clifford Field (1CO4) | 2026-04-04 20:32 UTC | 2026-04-04 20:32 UTC | 0m |
| PBD6816 | PBD | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-04-04 20:31 UTC | 2026-04-04 20:31 UTC | 0m |
| SVX45 | SVX | Ted Stevens Anchorage International Airport (PANC) | Ralph M Calhoun Memorial Airport (PATA) | 2026-04-04 19:40 UTC | 2026-04-04 20:27 UTC | 47m |
| N339XA |  | Mesa Gateway Airport (KIWA) | Benson Municipal/Paul Kerchum Field (KE95) | 2026-04-04 19:20 UTC | 2026-04-04 20:24 UTC | 1h 3m |
| OTA56 | OTA | Henderson Executive Airport (KHND) | Wagonhound Airport (WY27) | 2026-04-04 17:59 UTC | 2026-04-04 20:21 UTC | 2h 21m |
| N735RR |  | Aero Valley Airport (K52F) | Flat Bush Airport (XA99) | 2026-04-04 20:04 UTC | 2026-04-04 20:18 UTC | 14m |
| RYR78XT | Ryanair | Palma De Mallorca Airport (LEPA) | Munster Osnabruck Airport (EDDG) | 2026-04-04 17:59 UTC | 2026-04-04 20:16 UTC | 2h 17m |
| N684BB |  | John F Kennedy International Airport (KJFK) | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | 2026-04-04 19:14 UTC | 2026-04-04 20:14 UTC | 1h 0m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-04 06:06 UTC | 2026-04-04 20:12 UTC | 14h 6m |
| N996WW |  | Wings-N-Wheels Airport (FA50) | Bartow Executive Airport (KBOW) | 2026-04-04 19:21 UTC | 2026-04-04 20:12 UTC | 50m |
| ENY4320 | ENY | Miami International Airport (KMIA) | Benjamin Rivera Noriega Airport (TJCP) | 2026-04-04 17:54 UTC | 2026-04-04 20:11 UTC | 2h 17m |
| FFT1082 | FFT | Hartsfield/Jackson Atlanta International Airport (KATL) | Washington Dulles International Airport (KIAD) | 2026-04-04 18:49 UTC | 2026-04-04 20:09 UTC | 1h 20m |
| AZG1011 | AZG | Tbilisi International Airport (UGTB) | Zhuhai Airport (ZGSD) | 2026-04-04 09:22 UTC | 2026-04-04 20:09 UTC | 10h 47m |
| EJA740 | EJA | Cleveland-Hopkins International Airport (KCLE) | Mc Elroy Airfield (K20V) | 2026-04-04 17:22 UTC | 2026-04-04 20:09 UTC | 2h 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
