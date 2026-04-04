# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_15:35:05_UTC-green)

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

**Latest saved flight:** 2026-04-04 15:35:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 15:35:05 UTC

- **15,931** saved flights
- **8,506** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **15,931** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **197,745.3 tonnes** estimated CO2 emissions
- **11,463,495 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 676 |
| 2 | Ryanair | 642 |
| 3 | IndiGo | 465 |
| 4 | EJA | 305 |
| 5 | American Airlines | 283 |
| 6 | Southwest Airlines | 227 |
| 7 | Lufthansa | 225 |
| 8 | ENY | 197 |
| 9 | Vueling | 174 |
| 10 | LATAM Airlines | 170 |
| 11 | AXM | 159 |
| 12 | All Nippon Airways | 141 |
| 13 | QLK | 137 |
| 14 | LXJ | 134 |
| 15 | Delta Air Lines | 130 |
| 16 | AZU | 122 |
| 17 | Swiss International | 122 |
| 18 | VIV | 116 |
| 19 | Japan Airlines | 107 |
| 20 | EJU | 106 |
| 21 | Alaska Airlines | 104 |
| 22 | Avianca | 104 |
| 23 | WIF | 102 |
| 24 | AEE | 101 |
| 25 | AXB | 99 |
| 26 | United Airlines | 98 |
| 27 | easyJet | 97 |
| 28 | EDV | 94 |
| 29 | BRC | 92 |
| 30 | GLO | 92 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12484 |
| 2 | 🇮🇳 IN | 1418 |
| 3 | 🇪🇸 ES | 1291 |
| 4 | 🇦🇺 AU | 1207 |
| 5 | 🇧🇷 BR | 929 |
| 6 | 🇯🇵 JP | 860 |
| 7 | 🇩🇪 DE | 836 |
| 8 | 🇨🇴 CO | 804 |
| 9 | 🇮🇹 IT | 721 |
| 10 | 🇨🇦 CA | 702 |
| 11 | 🇬🇧 GB | 623 |
| 12 | 🇫🇷 FR | 585 |
| 13 | 🇲🇽 MX | 539 |
| 14 | 🇬🇷 GR | 447 |
| 15 | 🇨🇭 CH | 429 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 367 |
| 18 | 🇿🇦 ZA | 344 |
| 19 | 🇳🇴 NO | 337 |
| 20 | 🇵🇭 PH | 305 |
| 21 | 🇹🇷 TR | 295 |
| 22 | 🇰🇷 KR | 290 |
| 23 | 🇬🇹 GT | 282 |
| 24 | 🇹🇭 TH | 230 |
| 25 | 🇵🇱 PL | 229 |
| 26 | 🇲🇦 MA | 192 |
| 27 | 🇮🇩 ID | 177 |
| 28 | 🇲🇪 ME | 166 |
| 29 | 🇲🇴 MO | 163 |
| 30 | 🇧🇸 BS | 163 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 376 |
| 2 | El Dorado International Airport |  | CO | 304 |
| 3 | Tokyo International Airport |  | JP | 299 |
| 4 | Indira Gandhi International Airport |  | IN | 292 |
| 5 | Denver International Airport |  | US | 283 |
| 6 | Harry Reid International Airport |  | US | 214 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 210 |
| 8 | Frankfurt am Main International Airport |  | DE | 207 |
| 9 | La Aurora Airport |  | GT | 197 |
| 10 | Zurich Airport |  | CH | 194 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 166 |
| 13 | Guaymaral Airport |  | CO | 165 |
| 14 | Macau International Airport |  | MO | 163 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 158 |
| 16 | Bengaluru International Airport |  | IN | 155 |
| 17 | Chicago O'Hare International Airport |  | US | 147 |
| 18 | Congonhas Airport |  | BR | 147 |
| 19 | Charlotte/Douglas International Airport |  | US | 145 |
| 20 | Madrid Barajas International Airport |  | ES | 145 |
| 21 | Ninoy Aquino International Airport |  | PH | 140 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 139 |
| 23 | Tenerife Norte Airport |  | ES | 139 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 134 |
| 25 | Kuala Lumpur International Airport |  | MY | 130 |
| 26 | Malpensa International Airport |  | IT | 123 |
| 27 | Daniel K Inouye International Airport |  | US | 123 |
| 28 | Reno/Tahoe International Airport |  | US | 123 |
| 29 | Salt Lake City International Airport |  | US | 123 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 122 |
| 31 | Charles de Gaulle International Airport |  | FR | 118 |
| 32 | Vitoria/Foronda Airport |  | ES | 116 |
| 33 | Barcelona International Airport |  | ES | 113 |
| 34 | Pune Airport |  | IN | 107 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 106 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 106 |
| 37 | Austin-Bergstrom International Airport |  | US | 103 |
| 38 | Gimpo International Airport |  | KR | 101 |
| 39 | O. R. Tambo International Airport |  | ZA | 100 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 98 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 74 | 14m | 114 km | 145.1 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 63 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 48 | 1h 45m | 1,156 km | 957.6 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 48 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 39 | 16m | 206 km | 138.7 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 39 | 22m | 99 km | 66.8 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 39 | 26m | 152 km | 101.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 37 | 28m | 275 km | 175.3 t |
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
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 23 | 53m | 493 km | 195.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 23 | 1h 20m | 961 km | 381.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6026Y |  | Burlington/Alamance Regional Airport (KBUY) | Burlington/Alamance Regional Airport (KBUY) | 2026-04-04 15:24 UTC | 2026-04-04 15:35 UTC | 10m |
| N6338F |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-04-04 14:40 UTC | 2026-04-04 15:32 UTC | 52m |
| N4841Y |  | Kelly Air Park (CO15) | Kelly Air Park (CO15) | 2026-04-04 15:05 UTC | 2026-04-04 15:30 UTC | 24m |
| SCA88 | SCA | Scottsdale Airport (KSDL) | AZ86 (AZ86) | 2026-04-04 14:43 UTC | 2026-04-04 15:30 UTC | 46m |
| N743TW |  | KU42 (KU42) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-04 14:54 UTC | 2026-04-04 15:17 UTC | 23m |
| N39476 |  | Ocean County Airport (KMJX) | Millville Municipal Airport (KMIV) | 2026-04-04 14:48 UTC | 2026-04-04 15:17 UTC | 29m |
| N38549 |  | Laconia Municipal Airport (KLCI) | Laconia Municipal Airport (KLCI) | 2026-04-04 14:03 UTC | 2026-04-04 15:17 UTC | 1h 14m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-04 14:25 UTC | 2026-04-04 15:12 UTC | 47m |
| N711LC |  | Pompano Beach Airpark (KPMP) | Okeelanta Airport (FL41) | 2026-04-04 14:34 UTC | 2026-04-04 15:11 UTC | 36m |
| N5025W |  | K55J (K55J) | Brunswick Golden Isles Airport (KBQK) | 2026-04-04 14:52 UTC | 2026-04-04 15:10 UTC | 17m |
| N48ZA |  | Essex County Airport (KCDW) | Newark Liberty International Airport (KEWR) | 2026-04-04 13:47 UTC | 2026-04-04 15:08 UTC | 1h 20m |
| N921RA |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-04 14:45 UTC | 2026-04-04 15:08 UTC | 22m |
| N738HD |  | Vance Brand Airport (KLMO) | Northern Colorado Regional Airport (KFNL) | 2026-04-04 14:51 UTC | 2026-04-04 15:07 UTC | 15m |
| HBZYJ | HBZ | Courchevel Airport (LFLJ) | Courchevel Airport (LFLJ) | 2026-04-04 15:03 UTC | 2026-04-04 15:05 UTC | 2m |
| N145HF |  | Long Island Mac Arthur Airport (KISP) | Long Island Mac Arthur Airport (KISP) | 2026-04-04 14:53 UTC | 2026-04-04 15:05 UTC | 12m |
| N431CB |  | Lehigh Valley International Airport (KABE) | Bear Pen Airport (NC43) | 2026-04-04 13:55 UTC | 2026-04-04 15:05 UTC | 1h 10m |
| N90JF |  | Antonio/Nery/Juarbe Pol Airport (TJAB) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-04-04 14:44 UTC | 2026-04-04 15:00 UTC | 15m |
| N844BC |  | Laramie Regional Airport (KLAR) | Laramie Regional Airport (KLAR) | 2026-04-04 14:46 UTC | 2026-04-04 15:00 UTC | 13m |
| N65474 |  | Los Alamos Airport (KLAM) | Ohkay Owingeh Airport (KE14) | 2026-04-04 14:33 UTC | 2026-04-04 14:58 UTC | 24m |
| N802CA |  | Olive Branch/Taylor Field (KOLV) | Johnson Memorial Airport (05XS) | 2026-04-04 14:26 UTC | 2026-04-04 14:56 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
