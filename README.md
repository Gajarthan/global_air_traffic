# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_10:05:59_UTC-green)

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

**Latest saved flight:** 2026-04-14 10:05:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 10:05:59 UTC

- **33,741** saved flights
- **14,996** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **33,741** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **415,724.7 tonnes** estimated CO2 emissions
- **24,099,985 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1440 |
| 2 | SkyWest Airlines | 1354 |
| 3 | IndiGo | 851 |
| 4 | American Airlines | 585 |
| 5 | EJA | 577 |
| 6 | Southwest Airlines | 487 |
| 7 | ENY | 449 |
| 8 | Lufthansa | 378 |
| 9 | AXM | 356 |
| 10 | Vueling | 344 |
| 11 | LATAM Airlines | 337 |
| 12 | All Nippon Airways | 307 |
| 13 | AZU | 297 |
| 14 | QLK | 289 |
| 15 | Delta Air Lines | 286 |
| 16 | LXJ | 271 |
| 17 | Swiss International | 258 |
| 18 | WIF | 235 |
| 19 | Alaska Airlines | 228 |
| 20 | easyJet | 228 |
| 21 | EJU | 225 |
| 22 | AEE | 219 |
| 23 | VIV | 218 |
| 24 | Japan Airlines | 214 |
| 25 | EDV | 195 |
| 26 | United Airlines | 193 |
| 27 | GLO | 183 |
| 28 | Air France | 181 |
| 29 | Avianca | 181 |
| 30 | JetBlue | 180 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26445 |
| 2 | 🇮🇳 IN | 2613 |
| 3 | 🇪🇸 ES | 2530 |
| 4 | 🇦🇺 AU | 2411 |
| 5 | 🇧🇷 BR | 1973 |
| 6 | 🇯🇵 JP | 1852 |
| 7 | 🇮🇹 IT | 1805 |
| 8 | 🇩🇪 DE | 1701 |
| 9 | 🇨🇴 CO | 1675 |
| 10 | 🇨🇦 CA | 1646 |
| 11 | 🇬🇧 GB | 1383 |
| 12 | 🇫🇷 FR | 1246 |
| 13 | 🇲🇽 MX | 1075 |
| 14 | 🇬🇷 GR | 985 |
| 15 | 🇨🇭 CH | 933 |
| 16 | 🇲🇾 MY | 860 |
| 17 | 🇳🇴 NO | 772 |
| 18 | 🇳🇿 NZ | 726 |
| 19 | 🇿🇦 ZA | 696 |
| 20 | 🇵🇭 PH | 644 |
| 21 | 🇹🇷 TR | 627 |
| 22 | 🇹🇭 TH | 613 |
| 23 | 🇬🇹 GT | 601 |
| 24 | 🇰🇷 KR | 580 |
| 25 | 🇵🇱 PL | 526 |
| 26 | 🇲🇦 MA | 429 |
| 27 | 🇧🇸 BS | 340 |
| 28 | 🇲🇪 ME | 337 |
| 29 | 🇳🇱 NL | 324 |
| 30 | 🇮🇩 ID | 323 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 803 |
| 2 | Tokyo International Airport |  | JP | 630 |
| 3 | El Dorado International Airport |  | CO | 599 |
| 4 | Denver International Airport |  | US | 570 |
| 5 | Indira Gandhi International Airport |  | IN | 557 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 480 |
| 7 | Harry Reid International Airport |  | US | 443 |
| 8 | La Aurora Airport |  | GT | 438 |
| 9 | Zurich Airport |  | CH | 420 |
| 10 | Guaymaral Airport |  | CO | 406 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 343 |
| 12 | Chicago O'Hare International Airport |  | US | 343 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 340 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 331 |
| 15 | Kuala Lumpur International Airport |  | MY | 329 |
| 16 | Frankfurt am Main International Airport |  | DE | 328 |
| 17 | Macau International Airport |  | MO | 320 |
| 18 | Madrid Barajas International Airport |  | ES | 307 |
| 19 | Charlotte/Douglas International Airport |  | US | 306 |
| 20 | Bengaluru International Airport |  | IN | 302 |
| 21 | Ninoy Aquino International Airport |  | PH | 297 |
| 22 | Tenerife Norte Airport |  | ES | 296 |
| 23 | Congonhas Airport |  | BR | 293 |
| 24 | Malpensa International Airport |  | IT | 277 |
| 25 | Daniel K Inouye International Airport |  | US | 259 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 258 |
| 27 | Salt Lake City International Airport |  | US | 255 |
| 28 | Capua Airport |  | IT | 245 |
| 29 | Charles de Gaulle International Airport |  | FR | 244 |
| 30 | Reno/Tahoe International Airport |  | US | 243 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 237 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 234 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 232 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 228 |
| 35 | O. R. Tambo International Airport |  | ZA | 227 |
| 36 | Vitoria/Foronda Airport |  | ES | 226 |
| 37 | Barcelona International Airport |  | ES | 219 |
| 38 | Miami International Airport |  | US | 214 |
| 39 | Seattle-Tacoma International Airport |  | US | 212 |
| 40 | Viracopos International Airport |  | BR | 206 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 158 | 1h 8m | 706 km | 1,923.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 157 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 139 | 14m | 114 km | 272.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 126 | 24m | 225 km | 488.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 112 | 28m | 304 km | 587.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 97 | 1h 27m | 910 km | 1,522.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 87 | 19m | 165 km | 247.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 83 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 81 | 9m | - | - |
| 10 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 76 | 21m | 244 km | 320.0 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 74 | 27m | 275 km | 350.7 t |
| 14 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 71 | 1h 11m | 770 km | 943.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 65 | 31m | 369 km | 413.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 63 | 45m | 452 km | 491.0 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 59 | 20m | 250 km | 254.8 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 54 | 20m | 147 km | 136.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 52 | 13m | 99 km | 89.2 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 49 | 16m | 162 km | 137.4 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 48 | 23m | 252 km | 208.4 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 48 | 12m | 15 km | 12.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 47 | 14m | 154 km | 124.5 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 47 | 1h 20m | 961 km | 779.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 47 | 1h 53m | 1,304 km | 1,057.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NMU | NMU | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-04-14 09:27 UTC | 2026-04-14 10:05 UTC | 38m |
| OEFDV | OEF | Schaffen Airport (EBDT) | Schaffen Airport (EBDT) | 2026-04-14 09:20 UTC | 2026-04-14 09:50 UTC | 30m |
| DRAGO74 | DRA | Sallanches Airport (LFHZ) | Megeve Airport (LFHM) | 2026-04-14 09:21 UTC | 2026-04-14 09:46 UTC | 24m |
| URSA30 | URS | Chena Marina Airport (AK28) | Ladd Army Air Field (PAFB) | 2026-04-14 09:17 UTC | 2026-04-14 09:41 UTC | 23m |
| CPA418 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Incheon International Airport (RKSI) | 2026-04-14 06:52 UTC | 2026-04-14 09:40 UTC | 2h 47m |
| HBZVS | HBZ | Courchevel Airport (LFLJ) | Raron Airport (LSTA) | 2026-04-14 09:27 UTC | 2026-04-14 09:39 UTC | 11m |
| UAE9846 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-14 03:11 UTC | 2026-04-14 09:36 UTC | 6h 24m |
| YGI | YGI | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-04-14 08:59 UTC | 2026-04-14 09:35 UTC | 36m |
| SWR8KW | Swiss International | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Zurich Airport (LSZH) | 2026-04-14 08:37 UTC | 2026-04-14 09:35 UTC | 57m |
| PHBRI | PHB | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-04-14 09:19 UTC | 2026-04-14 09:34 UTC | 14m |
| RNA409 | RNA | Tribhuvan International Airport (VNKT) | Zhuhai Airport (ZGSD) | 2026-04-14 06:08 UTC | 2026-04-14 09:33 UTC | 3h 24m |
| FDX1777 | FDX | Indianapolis International Airport (KIND) | The Eastern Iowa Airport (KCID) | 2026-04-14 08:38 UTC | 2026-04-14 09:29 UTC | 50m |
| JUST14 | JUS | Holsworthy (Military) Airport (YSHW) | Holsworthy (Military) Airport (YSHW) | 2026-04-14 07:29 UTC | 2026-04-14 09:28 UTC | 1h 59m |
| RYR76PX | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-14 08:07 UTC | 2026-04-14 09:27 UTC | 1h 20m |
| RYR2656 | Ryanair | Memmingen Allgau Airport (EDJA) | Ampuriabrava Airport (LEAP) | 2026-04-14 08:15 UTC | 2026-04-14 09:27 UTC | 1h 12m |
| RDF26 | RDF | Ingolstadt Manching Airport (ETSI) | Ingolstadt Manching Airport (ETSI) | 2026-04-14 08:44 UTC | 2026-04-14 09:24 UTC | 39m |
| IGO2513 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Silchar Airport (VEKU) | 2026-04-14 08:45 UTC | 2026-04-14 09:24 UTC | 39m |
| RYR9GA | Ryanair | London Stansted Airport (EGSS) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-14 07:33 UTC | 2026-04-14 09:23 UTC | 1h 50m |
| NCG01 | NCG | Amsterdam Airport Schiphol (EHAM) | Borkum Airport (EDWR) | 2026-04-14 07:47 UTC | 2026-04-14 09:23 UTC | 1h 35m |
| IGO7313 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-04-14 08:02 UTC | 2026-04-14 09:22 UTC | 1h 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
