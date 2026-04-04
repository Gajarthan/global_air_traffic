# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_15:05:48_UTC-green)

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

**Latest saved flight:** 2026-04-04 15:05:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 15:05:48 UTC

- **15,830** saved flights
- **8,458** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **15,830** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **196,559.6 tonnes** estimated CO2 emissions
- **11,394,760 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 674 |
| 2 | Ryanair | 639 |
| 3 | IndiGo | 461 |
| 4 | EJA | 303 |
| 5 | American Airlines | 283 |
| 6 | Southwest Airlines | 226 |
| 7 | Lufthansa | 224 |
| 8 | ENY | 196 |
| 9 | Vueling | 172 |
| 10 | LATAM Airlines | 168 |
| 11 | AXM | 159 |
| 12 | All Nippon Airways | 141 |
| 13 | QLK | 137 |
| 14 | LXJ | 134 |
| 15 | Delta Air Lines | 128 |
| 16 | AZU | 122 |
| 17 | Swiss International | 121 |
| 18 | VIV | 115 |
| 19 | Japan Airlines | 107 |
| 20 | Alaska Airlines | 104 |
| 21 | Avianca | 103 |
| 22 | EJU | 102 |
| 23 | WIF | 102 |
| 24 | AEE | 101 |
| 25 | AXB | 98 |
| 26 | United Airlines | 98 |
| 27 | easyJet | 97 |
| 28 | EDV | 94 |
| 29 | BRC | 91 |
| 30 | GLO | 90 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12415 |
| 2 | 🇮🇳 IN | 1407 |
| 3 | 🇪🇸 ES | 1274 |
| 4 | 🇦🇺 AU | 1207 |
| 5 | 🇧🇷 BR | 919 |
| 6 | 🇯🇵 JP | 860 |
| 7 | 🇩🇪 DE | 827 |
| 8 | 🇨🇴 CO | 790 |
| 9 | 🇮🇹 IT | 716 |
| 10 | 🇨🇦 CA | 702 |
| 11 | 🇬🇧 GB | 620 |
| 12 | 🇫🇷 FR | 578 |
| 13 | 🇲🇽 MX | 537 |
| 14 | 🇬🇷 GR | 447 |
| 15 | 🇨🇭 CH | 428 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 367 |
| 18 | 🇿🇦 ZA | 342 |
| 19 | 🇳🇴 NO | 333 |
| 20 | 🇵🇭 PH | 303 |
| 21 | 🇹🇷 TR | 292 |
| 22 | 🇰🇷 KR | 290 |
| 23 | 🇬🇹 GT | 278 |
| 24 | 🇹🇭 TH | 230 |
| 25 | 🇵🇱 PL | 228 |
| 26 | 🇲🇦 MA | 189 |
| 27 | 🇮🇩 ID | 177 |
| 28 | 🇲🇪 ME | 166 |
| 29 | 🇲🇴 MO | 163 |
| 30 | 🇧🇸 BS | 162 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 375 |
| 2 | El Dorado International Airport |  | CO | 299 |
| 3 | Tokyo International Airport |  | JP | 299 |
| 4 | Indira Gandhi International Airport |  | IN | 291 |
| 5 | Denver International Airport |  | US | 283 |
| 6 | Harry Reid International Airport |  | US | 214 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 210 |
| 8 | Frankfurt am Main International Airport |  | DE | 207 |
| 9 | La Aurora Airport |  | GT | 194 |
| 10 | Zurich Airport |  | CH | 193 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 166 |
| 13 | Guaymaral Airport |  | CO | 164 |
| 14 | Macau International Airport |  | MO | 163 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 157 |
| 16 | Bengaluru International Airport |  | IN | 154 |
| 17 | Chicago O'Hare International Airport |  | US | 147 |
| 18 | Charlotte/Douglas International Airport |  | US | 145 |
| 19 | Madrid Barajas International Airport |  | ES | 144 |
| 20 | Congonhas Airport |  | BR | 144 |
| 21 | Ninoy Aquino International Airport |  | PH | 139 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 138 |
| 23 | Tenerife Norte Airport |  | ES | 136 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 133 |
| 25 | Kuala Lumpur International Airport |  | MY | 130 |
| 26 | Malpensa International Airport |  | IT | 123 |
| 27 | Reno/Tahoe International Airport |  | US | 123 |
| 28 | Daniel K Inouye International Airport |  | US | 122 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 122 |
| 30 | Salt Lake City International Airport |  | US | 121 |
| 31 | Charles de Gaulle International Airport |  | FR | 118 |
| 32 | Vitoria/Foronda Airport |  | ES | 115 |
| 33 | Barcelona International Airport |  | ES | 109 |
| 34 | Pune Airport |  | IN | 107 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 106 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 37 | Austin-Bergstrom International Airport |  | US | 103 |
| 38 | Gimpo International Airport |  | KR | 101 |
| 39 | O. R. Tambo International Airport |  | ZA | 99 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 98 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 73 | 14m | 114 km | 143.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 63 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 48 | 1h 45m | 1,156 km | 957.6 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 48 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 39 | 16m | 206 km | 138.7 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 39 | 22m | 99 km | 66.8 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 37 | 27m | 152 km | 96.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 36 | 28m | 275 km | 170.6 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 14 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 34 | 53m | 556 km | 325.9 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 33 | 1h 54m | 1,304 km | 742.4 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 29 | 1h 42m | 1,423 km | 711.7 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 28 | 13m | 99 km | 48.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 27 | 59m | 723 km | 336.6 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 26 | 20m | 147 km | 65.8 t |
| 27 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 24 | 16m | 183 km | 75.7 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 23 | 53m | 493 km | 195.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 23 | 1h 20m | 961 km | 381.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N145HF |  | Long Island Mac Arthur Airport (KISP) | Long Island Mac Arthur Airport (KISP) | 2026-04-04 14:53 UTC | 2026-04-04 15:05 UTC | 12m |
| N844BC |  | Laramie Regional Airport (KLAR) | Laramie Regional Airport (KLAR) | 2026-04-04 14:46 UTC | 2026-04-04 15:00 UTC | 13m |
| N65474 |  | Los Alamos Airport (KLAM) | Ohkay Owingeh Airport (KE14) | 2026-04-04 14:33 UTC | 2026-04-04 14:58 UTC | 24m |
| N308VA |  | Kent Fort Manor Airport (7MD8) | Kent Fort Manor Airport (7MD8) | 2026-04-04 14:41 UTC | 2026-04-04 14:56 UTC | 14m |
| N874BU |  | Lakeland Linder International Airport (KLAL) | Peter O Knight Airport (KTPF) | 2026-04-04 14:39 UTC | 2026-04-04 14:54 UTC | 14m |
| IE637 |  | Voghera-Rivanazzano Airport (LILH) | Voghera-Rivanazzano Airport (LILH) | 2026-04-04 14:42 UTC | 2026-04-04 14:52 UTC | 10m |
| CFHAS | CFH | Vancouver International Airport (CYVR) | Sechelt-Gibsons Airport (CAP3) | 2026-04-04 14:36 UTC | 2026-04-04 14:46 UTC | 9m |
| N912BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-04-04 13:35 UTC | 2026-04-04 14:43 UTC | 1h 7m |
| N39688 |  | Provo Municipal Airport (KPVU) | K43U (K43U) | 2026-04-04 14:14 UTC | 2026-04-04 14:39 UTC | 25m |
| N222KU |  | Chicago Midway International Airport (KMDW) | Chicago Midway International Airport (KMDW) | 2026-04-04 13:19 UTC | 2026-04-04 14:38 UTC | 1h 18m |
| DRAG381 | DRA | Grenoble Le Versoud Airport (LFLG) | L'alpe D'huez Airport (LFHU) | 2026-04-04 14:36 UTC | 2026-04-04 14:38 UTC | 1m |
| N844BC |  | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-04-04 13:50 UTC | 2026-04-04 14:35 UTC | 45m |
| N265SF |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-04-04 14:09 UTC | 2026-04-04 14:34 UTC | 24m |
| DLH35M | Lufthansa | Lisbon Portela Airport (LPPT) | Frankfurt am Main International Airport (EDDF) | 2026-04-04 12:04 UTC | 2026-04-04 14:31 UTC | 2h 27m |
| BRCAT12 | BRC | Roswell Air Center Airport (KROW) | Roswell Air Center Airport (KROW) | 2026-04-04 13:46 UTC | 2026-04-04 14:24 UTC | 37m |
| N41DZ |  | Arthur Dunn Air Park (KX21) | Arthur Dunn Air Park (KX21) | 2026-04-04 14:09 UTC | 2026-04-04 14:24 UTC | 14m |
| HB2470 |  | Barcelonnette - Saint-Pons Airport (LFMR) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-04-04 13:21 UTC | 2026-04-04 14:23 UTC | 1h 2m |
| N483P |  | Capital City Airport (KCXY) | York Airport (KTHV) | 2026-04-04 13:53 UTC | 2026-04-04 14:22 UTC | 29m |
| N65474 |  | Los Alamos Airport (KLAM) | Santa Fe Regional Airport (KSAF) | 2026-04-04 13:52 UTC | 2026-04-04 14:20 UTC | 27m |
| SWE24V | SWE | Kalixfors Airport (ESUK) | Vidsel Air Base (ESPE) | 2026-04-04 13:55 UTC | 2026-04-04 14:18 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
