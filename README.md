# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_08:37:34_UTC-green)

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

**Latest saved flight:** 2026-04-14 08:37:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 08:37:34 UTC

- **33,643** saved flights
- **14,969** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **33,643** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **414,138.1 tonnes** estimated CO2 emissions
- **24,008,005 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1429 |
| 2 | SkyWest Airlines | 1354 |
| 3 | IndiGo | 847 |
| 4 | American Airlines | 585 |
| 5 | EJA | 577 |
| 6 | Southwest Airlines | 487 |
| 7 | ENY | 449 |
| 8 | Lufthansa | 377 |
| 9 | AXM | 355 |
| 10 | Vueling | 343 |
| 11 | LATAM Airlines | 337 |
| 12 | All Nippon Airways | 307 |
| 13 | AZU | 297 |
| 14 | QLK | 289 |
| 15 | Delta Air Lines | 285 |
| 16 | LXJ | 271 |
| 17 | Swiss International | 255 |
| 18 | WIF | 233 |
| 19 | Alaska Airlines | 228 |
| 20 | easyJet | 227 |
| 21 | EJU | 224 |
| 22 | AEE | 219 |
| 23 | VIV | 218 |
| 24 | Japan Airlines | 214 |
| 25 | EDV | 195 |
| 26 | United Airlines | 193 |
| 27 | GLO | 183 |
| 28 | Avianca | 181 |
| 29 | JetBlue | 180 |
| 30 | Air France | 178 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26436 |
| 2 | 🇮🇳 IN | 2601 |
| 3 | 🇪🇸 ES | 2521 |
| 4 | 🇦🇺 AU | 2389 |
| 5 | 🇧🇷 BR | 1973 |
| 6 | 🇯🇵 JP | 1851 |
| 7 | 🇮🇹 IT | 1797 |
| 8 | 🇩🇪 DE | 1683 |
| 9 | 🇨🇴 CO | 1675 |
| 10 | 🇨🇦 CA | 1646 |
| 11 | 🇬🇧 GB | 1371 |
| 12 | 🇫🇷 FR | 1232 |
| 13 | 🇲🇽 MX | 1075 |
| 14 | 🇬🇷 GR | 978 |
| 15 | 🇨🇭 CH | 928 |
| 16 | 🇲🇾 MY | 855 |
| 17 | 🇳🇴 NO | 766 |
| 18 | 🇳🇿 NZ | 726 |
| 19 | 🇿🇦 ZA | 690 |
| 20 | 🇵🇭 PH | 644 |
| 21 | 🇹🇷 TR | 624 |
| 22 | 🇹🇭 TH | 609 |
| 23 | 🇬🇹 GT | 601 |
| 24 | 🇰🇷 KR | 577 |
| 25 | 🇵🇱 PL | 520 |
| 26 | 🇲🇦 MA | 429 |
| 27 | 🇧🇸 BS | 340 |
| 28 | 🇲🇪 ME | 336 |
| 29 | 🇳🇱 NL | 321 |
| 30 | 🇮🇩 ID | 321 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 803 |
| 2 | Tokyo International Airport |  | JP | 630 |
| 3 | El Dorado International Airport |  | CO | 599 |
| 4 | Denver International Airport |  | US | 570 |
| 5 | Indira Gandhi International Airport |  | IN | 555 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 477 |
| 7 | Harry Reid International Airport |  | US | 443 |
| 8 | La Aurora Airport |  | GT | 438 |
| 9 | Zurich Airport |  | CH | 416 |
| 10 | Guaymaral Airport |  | CO | 406 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 343 |
| 12 | Chicago O'Hare International Airport |  | US | 343 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 340 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 329 |
| 15 | Kuala Lumpur International Airport |  | MY | 328 |
| 16 | Frankfurt am Main International Airport |  | DE | 327 |
| 17 | Macau International Airport |  | MO | 319 |
| 18 | Madrid Barajas International Airport |  | ES | 307 |
| 19 | Charlotte/Douglas International Airport |  | US | 306 |
| 20 | Bengaluru International Airport |  | IN | 301 |
| 21 | Ninoy Aquino International Airport |  | PH | 297 |
| 22 | Tenerife Norte Airport |  | ES | 295 |
| 23 | Congonhas Airport |  | BR | 293 |
| 24 | Malpensa International Airport |  | IT | 277 |
| 25 | Daniel K Inouye International Airport |  | US | 259 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 258 |
| 27 | Salt Lake City International Airport |  | US | 255 |
| 28 | Capua Airport |  | IT | 244 |
| 29 | Reno/Tahoe International Airport |  | US | 243 |
| 30 | Charles de Gaulle International Airport |  | FR | 241 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 237 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 230 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 228 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 228 |
| 35 | O. R. Tambo International Airport |  | ZA | 225 |
| 36 | Vitoria/Foronda Airport |  | ES | 225 |
| 37 | Barcelona International Airport |  | ES | 218 |
| 38 | Miami International Airport |  | US | 214 |
| 39 | Seattle-Tacoma International Airport |  | US | 211 |
| 40 | Viracopos International Airport |  | BR | 206 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 158 | 1h 8m | 706 km | 1,923.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 157 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 139 | 14m | 114 km | 272.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 126 | 24m | 225 km | 488.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 111 | 28m | 304 km | 581.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 97 | 1h 27m | 910 km | 1,522.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 86 | 19m | 165 km | 244.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 82 | 31m | - | - |
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
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 58 | 20m | 250 km | 250.5 t |
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
| ICV9261 | ICV | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-04-13 21:29 UTC | 2026-04-14 08:37 UTC | 11h 7m |
|  |  | Severka Airfield (UUML) | Ramenskoye Airport (UUBW) | 2026-04-14 07:56 UTC | 2026-04-14 08:35 UTC | 39m |
| HKC393 | HKC | Budapest Ferenc Liszt International Airport (LHBP) | Macau International Airport (VMMC) | 2026-04-13 22:11 UTC | 2026-04-14 08:30 UTC | 10h 18m |
| CLX4971 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-04-13 21:29 UTC | 2026-04-14 08:25 UTC | 10h 55m |
| DKAGZ | DKA | Juist Airport (EDWJ) | Juist Airport (EDWJ) | 2026-04-14 07:24 UTC | 2026-04-14 08:23 UTC | 59m |
| DLA9800 | DLA | Linz Airport (LOWL) | Linz Airport (LOWL) | 2026-04-14 07:50 UTC | 2026-04-14 08:22 UTC | 32m |
| V632 |  | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-04-14 08:13 UTC | 2026-04-14 08:20 UTC | 7m |
| FHSMB | FHS | Lyon-Bron Airport (LFLY) | Lyon-Bron Airport (LFLY) | 2026-04-14 07:44 UTC | 2026-04-14 08:04 UTC | 19m |
| 2611 |  | Chiang Mai International Airport (VTCC) | Mae Hong Son Airport (VTCI) | 2026-04-14 07:43 UTC | 2026-04-14 07:58 UTC | 14m |
| RYR2M | Ryanair | London Luton Airport (EGGW) | Kaunas International Airport (EYKA) | 2026-04-14 05:39 UTC | 2026-04-14 07:49 UTC | 2h 9m |
| RYR93QL | Ryanair | Brussels South Charleroi Airport (EBCI) | Ampuriabrava Airport (LEAP) | 2026-04-14 06:37 UTC | 2026-04-14 07:48 UTC | 1h 11m |
| AAH11 | AAH | Daniel K Inouye International Airport (PHNL) | Haiku Airstrip (HI33) | 2026-04-14 07:32 UTC | 2026-04-14 07:48 UTC | 15m |
| AUR202 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-04-14 07:26 UTC | 2026-04-14 07:47 UTC | 21m |
| FMJAA | FMJ | Cazaux (BA 120) Air Base (LFBC) | Andernos Les Bains Airport (LFCD) | 2026-04-14 07:04 UTC | 2026-04-14 07:44 UTC | 40m |
| RYR161N | Ryanair | Barcelona International Airport (LEBL) | Malpensa International Airport (LIMC) | 2026-04-14 06:25 UTC | 2026-04-14 07:44 UTC | 1h 18m |
| AXB1498 | AXB | Bengaluru International Airport (VOBL) | Ambala Air Force Station (VIAM) | 2026-04-14 05:17 UTC | 2026-04-14 07:43 UTC | 2h 25m |
| EIN69L | Aer Lingus | Dublin Airport (EIDW) | Dusseldorf International Airport (EDDL) | 2026-04-14 06:26 UTC | 2026-04-14 07:43 UTC | 1h 17m |
| NSZ5282 | NSZ | Gothenburg-Landvetter Airport (ESGG) | Stenkovec Brazda Airport (LW75) | 2026-04-14 05:09 UTC | 2026-04-14 07:43 UTC | 2h 33m |
| RYR8571 | Ryanair | Sevilla Airport (LEZL) | Malpensa International Airport (LIMC) | 2026-04-14 05:17 UTC | 2026-04-14 07:41 UTC | 2h 23m |
| SWR5P | Swiss International | Zurich Airport (LSZH) | Manchester Airport (EGCC) | 2026-04-14 05:53 UTC | 2026-04-14 07:40 UTC | 1h 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
