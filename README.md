# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_14:26:48_UTC-green)

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

**Latest saved flight:** 2026-04-09 14:26:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-09 14:26:48 UTC

- **25,123** saved flights
- **12,049** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **25,123** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **311,622.5 tonnes** estimated CO2 emissions
- **18,065,072 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1042 |
| 2 | SkyWest Airlines | 1023 |
| 3 | IndiGo | 699 |
| 4 | American Airlines | 451 |
| 5 | EJA | 449 |
| 6 | Southwest Airlines | 354 |
| 7 | Lufthansa | 332 |
| 8 | ENY | 324 |
| 9 | Vueling | 260 |
| 10 | AXM | 259 |
| 11 | LATAM Airlines | 249 |
| 12 | All Nippon Airways | 231 |
| 13 | QLK | 230 |
| 14 | Delta Air Lines | 210 |
| 15 | LXJ | 198 |
| 16 | AZU | 197 |
| 17 | Swiss International | 181 |
| 18 | Alaska Airlines | 175 |
| 19 | Japan Airlines | 171 |
| 20 | VIV | 167 |
| 21 | easyJet | 165 |
| 22 | EJU | 162 |
| 23 | WIF | 159 |
| 24 | AEE | 158 |
| 25 | United Airlines | 149 |
| 26 | EDV | 147 |
| 27 | Avianca | 146 |
| 28 | AXB | 143 |
| 29 | Cathay Pacific | 131 |
| 30 | BRC | 129 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 19506 |
| 2 | 🇮🇳 IN | 2140 |
| 3 | 🇪🇸 ES | 1893 |
| 4 | 🇦🇺 AU | 1876 |
| 5 | 🇯🇵 JP | 1434 |
| 6 | 🇧🇷 BR | 1401 |
| 7 | 🇩🇪 DE | 1319 |
| 8 | 🇮🇹 IT | 1284 |
| 9 | 🇨🇴 CO | 1274 |
| 10 | 🇨🇦 CA | 1161 |
| 11 | 🇬🇧 GB | 1025 |
| 12 | 🇫🇷 FR | 929 |
| 13 | 🇲🇽 MX | 799 |
| 14 | 🇬🇷 GR | 723 |
| 15 | 🇨🇭 CH | 703 |
| 16 | 🇲🇾 MY | 622 |
| 17 | 🇳🇿 NZ | 550 |
| 18 | 🇳🇴 NO | 544 |
| 19 | 🇿🇦 ZA | 528 |
| 20 | 🇬🇹 GT | 482 |
| 21 | 🇹🇷 TR | 480 |
| 22 | 🇵🇭 PH | 478 |
| 23 | 🇰🇷 KR | 447 |
| 24 | 🇹🇭 TH | 432 |
| 25 | 🇵🇱 PL | 375 |
| 26 | 🇲🇦 MA | 309 |
| 27 | 🇮🇩 ID | 258 |
| 28 | 🇲🇪 ME | 256 |
| 29 | 🇳🇱 NL | 254 |
| 30 | 🇲🇴 MO | 253 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 586 |
| 2 | Tokyo International Airport |  | JP | 480 |
| 3 | El Dorado International Airport |  | CO | 474 |
| 4 | Indira Gandhi International Airport |  | IN | 441 |
| 5 | Denver International Airport |  | US | 433 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 351 |
| 7 | La Aurora Airport |  | GT | 332 |
| 8 | Harry Reid International Airport |  | US | 329 |
| 9 | Zurich Airport |  | CH | 298 |
| 10 | Frankfurt am Main International Airport |  | DE | 278 |
| 11 | Guaymaral Airport |  | CO | 263 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 262 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 256 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 256 |
| 15 | Chicago O'Hare International Airport |  | US | 254 |
| 16 | Macau International Airport |  | MO | 253 |
| 17 | Bengaluru International Airport |  | IN | 235 |
| 18 | Charlotte/Douglas International Airport |  | US | 232 |
| 19 | Kuala Lumpur International Airport |  | MY | 229 |
| 20 | Ninoy Aquino International Airport |  | PH | 222 |
| 21 | Madrid Barajas International Airport |  | ES | 217 |
| 22 | Tenerife Norte Airport |  | ES | 216 |
| 23 | Malpensa International Airport |  | IT | 202 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 200 |
| 25 | Congonhas Airport |  | BR | 199 |
| 26 | Salt Lake City International Airport |  | US | 194 |
| 27 | Daniel K Inouye International Airport |  | US | 193 |
| 28 | Reno/Tahoe International Airport |  | US | 184 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 179 |
| 30 | Charles de Gaulle International Airport |  | FR | 177 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 175 |
| 32 | O. R. Tambo International Airport |  | ZA | 166 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 165 |
| 34 | Miami International Airport |  | US | 165 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 165 |
| 36 | Barcelona International Airport |  | ES | 163 |
| 37 | Seattle-Tacoma International Airport |  | US | 162 |
| 38 | Pune Airport |  | IN | 160 |
| 39 | Vitoria/Foronda Airport |  | ES | 157 |
| 40 | Don Mueang International Airport |  | TH | 150 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 122 | 1h 8m | 706 km | 1,485.4 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 103 | 14m | 114 km | 202.0 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 98 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 95 | 24m | 225 km | 368.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 86 | 28m | 304 km | 450.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 74 | 1h 27m | 910 km | 1,161.2 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 65 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 64 | 19m | 165 km | 182.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 59 | 1h 12m | 770 km | 783.8 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 54 | 55m | 546 km | 508.4 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 51 | 27m | 275 km | 241.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 50 | 31m | 369 km | 318.3 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 47 | 45m | 452 km | 366.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 45 | 20m | 250 km | 194.4 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 42 | 13m | 99 km | 72.0 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 38 | 21m | 147 km | 96.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 36 | 12m | 15 km | 9.5 t |
| 29 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 35 | 1h 21m | 961 km | 580.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N74639 |  | Northeast Philadelphia Airport (KPNE) | Blairstown Airport (K1N7) | 2026-04-09 13:59 UTC | 2026-04-09 14:26 UTC | 26m |
| N49CG |  | Bend Municipal Airport (KBDN) | Prineville Airport (KS39) | 2026-04-09 14:03 UTC | 2026-04-09 14:26 UTC | 22m |
| N383SF |  | Tulsa International Airport (KTUL) | Dodge City Regional Airport (KDDC) | 2026-04-09 13:45 UTC | 2026-04-09 14:18 UTC | 32m |
| N8677E |  | Centennial Airport (KAPA) | Athanasiou Valley Airport (CO07) | 2026-04-09 14:02 UTC | 2026-04-09 14:16 UTC | 14m |
| HB3472 |  | Mont-Dauphin - St-Crepin Airport (LFNC) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-04-09 12:39 UTC | 2026-04-09 14:15 UTC | 1h 36m |
| SHARK66 | SHA | Usaf Academy Davis Airfield (KAFF) | Geary Ranch Airport (CO65) | 2026-04-09 13:16 UTC | 2026-04-09 14:13 UTC | 57m |
| RNGR843 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | XS10 (XS10) | 2026-04-09 13:48 UTC | 2026-04-09 14:11 UTC | 23m |
| RDHK705 | RDH | Norfolk Ns (Chambers Field) Airport (KNGU) | VA33 (VA33) | 2026-04-09 13:48 UTC | 2026-04-09 14:08 UTC | 20m |
| LYRE71 | LYR | Randolph Afb Airport (KRND) | Tee Pee Creek Airport (8TE0) | 2026-04-09 13:25 UTC | 2026-04-09 14:07 UTC | 41m |
| N757CC |  | St Louis Lambert International Airport (KSTL) | Chicago Midway International Airport (KMDW) | 2026-04-09 13:21 UTC | 2026-04-09 14:06 UTC | 45m |
| N940W |  | Rocky Mountain Metro Airport (KBJC) | CO86 (CO86) | 2026-04-09 12:56 UTC | 2026-04-09 14:06 UTC | 1h 9m |
| N502FS |  | Sequoia Ranch Airport (CA44) | Porterville Municipal Airport (KPTV) | 2026-04-09 13:56 UTC | 2026-04-09 14:06 UTC | 9m |
| N3189Z |  | Caldwell Executive Airport (KEUL) | Caldwell Executive Airport (KEUL) | 2026-04-09 13:54 UTC | 2026-04-09 14:05 UTC | 11m |
| N779US |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-04-09 13:48 UTC | 2026-04-09 14:04 UTC | 16m |
| BRCAT11 | BRC | Champion Ranch Airport (01NM) | Artesia Municipal Airport (KATS) | 2026-04-09 13:42 UTC | 2026-04-09 14:03 UTC | 21m |
| HB2436 |  | Speck-Fehraltorf Airport (LSZK) | Ambri Airport (LSPM) | 2026-04-09 09:36 UTC | 2026-04-09 14:00 UTC | 4h 24m |
| WIF3NL | WIF | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-09 13:09 UTC | 2026-04-09 13:59 UTC | 50m |
| SYERTN2 | SYE | RAF Syerston (EGXY) | RAF Syerston (EGXY) | 2026-04-09 13:53 UTC | 2026-04-09 13:59 UTC | 6m |
| N183TS |  | Fort Lauderdale/Hollywood International Airport (KFLL) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-09 12:30 UTC | 2026-04-09 13:59 UTC | 1h 29m |
| UPS64 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Ted Stevens Anchorage International Airport (PANC) | 2026-04-09 07:33 UTC | 2026-04-09 13:59 UTC | 6h 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
