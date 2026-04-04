# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_14:35:48_UTC-green)

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

**Latest saved flight:** 2026-04-04 14:35:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 14:35:48 UTC

- **15,746** saved flights
- **8,420** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **15,746** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **195,624.4 tonnes** estimated CO2 emissions
- **11,340,543 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 672 |
| 2 | Ryanair | 631 |
| 3 | IndiGo | 461 |
| 4 | EJA | 303 |
| 5 | American Airlines | 283 |
| 6 | Southwest Airlines | 226 |
| 7 | Lufthansa | 224 |
| 8 | ENY | 196 |
| 9 | Vueling | 171 |
| 10 | LATAM Airlines | 168 |
| 11 | AXM | 159 |
| 12 | All Nippon Airways | 141 |
| 13 | QLK | 137 |
| 14 | LXJ | 134 |
| 15 | Delta Air Lines | 127 |
| 16 | AZU | 122 |
| 17 | Swiss International | 121 |
| 18 | VIV | 114 |
| 19 | Japan Airlines | 107 |
| 20 | Alaska Airlines | 104 |
| 21 | EJU | 102 |
| 22 | WIF | 102 |
| 23 | AEE | 99 |
| 24 | Avianca | 99 |
| 25 | AXB | 98 |
| 26 | United Airlines | 98 |
| 27 | easyJet | 97 |
| 28 | EDV | 93 |
| 29 | BRC | 89 |
| 30 | Cathay Pacific | 88 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12365 |
| 2 | 🇮🇳 IN | 1405 |
| 3 | 🇪🇸 ES | 1259 |
| 4 | 🇦🇺 AU | 1207 |
| 5 | 🇧🇷 BR | 909 |
| 6 | 🇯🇵 JP | 860 |
| 7 | 🇩🇪 DE | 825 |
| 8 | 🇨🇴 CO | 780 |
| 9 | 🇮🇹 IT | 710 |
| 10 | 🇨🇦 CA | 698 |
| 11 | 🇬🇧 GB | 617 |
| 12 | 🇫🇷 FR | 564 |
| 13 | 🇲🇽 MX | 531 |
| 14 | 🇬🇷 GR | 439 |
| 15 | 🇨🇭 CH | 426 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 367 |
| 18 | 🇿🇦 ZA | 342 |
| 19 | 🇳🇴 NO | 331 |
| 20 | 🇵🇭 PH | 303 |
| 21 | 🇹🇷 TR | 292 |
| 22 | 🇰🇷 KR | 290 |
| 23 | 🇬🇹 GT | 276 |
| 24 | 🇹🇭 TH | 228 |
| 25 | 🇵🇱 PL | 225 |
| 26 | 🇲🇦 MA | 188 |
| 27 | 🇮🇩 ID | 177 |
| 28 | 🇲🇪 ME | 165 |
| 29 | 🇲🇴 MO | 163 |
| 30 | 🇧🇸 BS | 162 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 375 |
| 2 | Tokyo International Airport |  | JP | 299 |
| 3 | El Dorado International Airport |  | CO | 295 |
| 4 | Indira Gandhi International Airport |  | IN | 290 |
| 5 | Denver International Airport |  | US | 282 |
| 6 | Harry Reid International Airport |  | US | 214 |
| 7 | Frankfurt am Main International Airport |  | DE | 207 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 206 |
| 9 | La Aurora Airport |  | GT | 193 |
| 10 | Zurich Airport |  | CH | 192 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 166 |
| 13 | Macau International Airport |  | MO | 163 |
| 14 | Guaymaral Airport |  | CO | 162 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 154 |
| 16 | Bengaluru International Airport |  | IN | 154 |
| 17 | Chicago O'Hare International Airport |  | US | 147 |
| 18 | Charlotte/Douglas International Airport |  | US | 143 |
| 19 | Madrid Barajas International Airport |  | ES | 142 |
| 20 | Congonhas Airport |  | BR | 141 |
| 21 | Ninoy Aquino International Airport |  | PH | 139 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 138 |
| 23 | Tenerife Norte Airport |  | ES | 134 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 133 |
| 25 | Kuala Lumpur International Airport |  | MY | 130 |
| 26 | Malpensa International Airport |  | IT | 123 |
| 27 | Reno/Tahoe International Airport |  | US | 123 |
| 28 | Daniel K Inouye International Airport |  | US | 122 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 121 |
| 30 | Salt Lake City International Airport |  | US | 121 |
| 31 | Charles de Gaulle International Airport |  | FR | 117 |
| 32 | Vitoria/Foronda Airport |  | ES | 114 |
| 33 | Barcelona International Airport |  | ES | 107 |
| 34 | Pune Airport |  | IN | 106 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 105 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 37 | Austin-Bergstrom International Airport |  | US | 103 |
| 38 | Gimpo International Airport |  | KR | 101 |
| 39 | O. R. Tambo International Airport |  | ZA | 99 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 98 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 72 | 14m | 114 km | 141.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 62 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 48 | 31m | - | - |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 47 | 1h 45m | 1,156 km | 937.6 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 39 | 16m | 206 km | 138.7 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 39 | 22m | 99 km | 66.8 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 37 | 27m | 152 km | 96.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 13 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 35 | 28m | 275 km | 165.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 34 | 53m | 556 km | 325.9 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 33 | 1h 54m | 1,304 km | 742.4 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 29 | 1h 42m | 1,423 km | 711.7 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 27 | 59m | 723 km | 336.6 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 26 | 20m | 147 km | 65.8 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 26 | 13m | 99 km | 44.6 t |
| 27 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 23 | 16m | 183 km | 72.5 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 23 | 53m | 493 km | 195.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 22 | 1h 16m | 961 km | 364.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N844BC |  | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-04-04 13:50 UTC | 2026-04-04 14:35 UTC | 45m |
| DLH35M | Lufthansa | Lisbon Portela Airport (LPPT) | Frankfurt am Main International Airport (EDDF) | 2026-04-04 12:04 UTC | 2026-04-04 14:31 UTC | 2h 27m |
| N41DZ |  | Arthur Dunn Air Park (KX21) | Arthur Dunn Air Park (KX21) | 2026-04-04 14:09 UTC | 2026-04-04 14:24 UTC | 14m |
| N483P |  | Capital City Airport (KCXY) | York Airport (KTHV) | 2026-04-04 13:53 UTC | 2026-04-04 14:22 UTC | 29m |
| N65474 |  | Los Alamos Airport (KLAM) | Santa Fe Regional Airport (KSAF) | 2026-04-04 13:52 UTC | 2026-04-04 14:20 UTC | 27m |
| AIP1814 | AIP | City Of Colorado Springs Municipal Airport (KCOS) | Stevens Field (KPSO) | 2026-04-04 13:37 UTC | 2026-04-04 14:15 UTC | 38m |
| N47296 |  | Marennes Le Bournet Airport (LFJI) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-04-04 14:03 UTC | 2026-04-04 14:13 UTC | 10m |
| TCF604 | TCF | Melbourne Orlando International Airport (KMLB) | Valkaria Airport (KX59) | 2026-04-04 12:47 UTC | 2026-04-04 14:08 UTC | 1h 21m |
| N57UD |  | Fort Lauderdale Executive Airport (KFXE) | Duda Airstrip (FA69) | 2026-04-04 13:42 UTC | 2026-04-04 14:07 UTC | 25m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-04-04 13:41 UTC | 2026-04-04 14:01 UTC | 20m |
| EFY9104 | EFY | El Dorado International Airport (SKBO) | Berastegui Airport (SKBR) | 2026-04-04 11:14 UTC | 2026-04-04 13:59 UTC | 2h 44m |
| N2994R |  | KU77 (KU77) | KU77 (KU77) | 2026-04-04 13:42 UTC | 2026-04-04 13:56 UTC | 14m |
| TGLUC | TGL | Copan Ruinas Airport (MHRU) | La Aurora Airport (MGGT) | 2026-04-04 13:23 UTC | 2026-04-04 13:56 UTC | 33m |
| ERU115 | ERU | Massey Ranch Airpark (KX50) | Massey Ranch Airpark (KX50) | 2026-04-04 13:50 UTC | 2026-04-04 13:54 UTC | 4m |
| LYM640 | LYM | Denver International Airport (KDEN) | Cedar Creek Ranch Airport (96WY) | 2026-04-04 12:55 UTC | 2026-04-04 13:52 UTC | 57m |
| N905NY |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-04-04 13:41 UTC | 2026-04-04 13:51 UTC | 10m |
| CAP3104 | CAP | Long Island Mac Arthur Airport (KISP) | Talmage Field (03NY) | 2026-04-04 13:37 UTC | 2026-04-04 13:51 UTC | 14m |
| UBG159 | UBG | VGZR (VGZR) | Cox's Bazar Airport (VGCB) | 2026-04-04 13:10 UTC | 2026-04-04 13:49 UTC | 39m |
| N713WA |  | Van Aire Airport (CO12) | Westwater Airport (UT42) | 2026-04-04 12:46 UTC | 2026-04-04 13:48 UTC | 1h 1m |
| N156NS |  | San Bernardino International Airport (KSBD) | Mc Clellan-Palomar Airport (KCRQ) | 2026-04-04 13:24 UTC | 2026-04-04 13:42 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
