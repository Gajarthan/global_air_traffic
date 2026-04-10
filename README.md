# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_07:25:15_UTC-green)

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

**Latest saved flight:** 2026-04-10 07:25:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 07:25:15 UTC

- **26,412** saved flights
- **12,562** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **26,412** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **325,125.9 tonnes** estimated CO2 emissions
- **18,847,878 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1082 |
| 2 | Ryanair | 1079 |
| 3 | IndiGo | 709 |
| 4 | EJA | 473 |
| 5 | American Airlines | 471 |
| 6 | Southwest Airlines | 380 |
| 7 | ENY | 350 |
| 8 | Lufthansa | 338 |
| 9 | AXM | 268 |
| 10 | Vueling | 267 |
| 11 | LATAM Airlines | 259 |
| 12 | QLK | 243 |
| 13 | All Nippon Airways | 234 |
| 14 | Delta Air Lines | 220 |
| 15 | LXJ | 212 |
| 16 | AZU | 211 |
| 17 | Swiss International | 181 |
| 18 | Alaska Airlines | 180 |
| 19 | VIV | 176 |
| 20 | Japan Airlines | 175 |
| 21 | easyJet | 170 |
| 22 | EJU | 169 |
| 23 | WIF | 169 |
| 24 | AEE | 167 |
| 25 | United Airlines | 159 |
| 26 | EDV | 155 |
| 27 | Avianca | 150 |
| 28 | AXB | 145 |
| 29 | JetBlue | 140 |
| 30 | ANZ | 137 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 20825 |
| 2 | 🇮🇳 IN | 2177 |
| 3 | 🇦🇺 AU | 1970 |
| 4 | 🇪🇸 ES | 1951 |
| 5 | 🇧🇷 BR | 1484 |
| 6 | 🇯🇵 JP | 1462 |
| 7 | 🇩🇪 DE | 1345 |
| 8 | 🇮🇹 IT | 1339 |
| 9 | 🇨🇴 CO | 1322 |
| 10 | 🇨🇦 CA | 1264 |
| 11 | 🇬🇧 GB | 1048 |
| 12 | 🇫🇷 FR | 968 |
| 13 | 🇲🇽 MX | 851 |
| 14 | 🇬🇷 GR | 751 |
| 15 | 🇨🇭 CH | 717 |
| 16 | 🇲🇾 MY | 646 |
| 17 | 🇳🇿 NZ | 602 |
| 18 | 🇳🇴 NO | 567 |
| 19 | 🇿🇦 ZA | 536 |
| 20 | 🇵🇭 PH | 504 |
| 21 | 🇹🇷 TR | 494 |
| 22 | 🇬🇹 GT | 490 |
| 23 | 🇰🇷 KR | 466 |
| 24 | 🇹🇭 TH | 457 |
| 25 | 🇵🇱 PL | 386 |
| 26 | 🇲🇦 MA | 323 |
| 27 | 🇧🇸 BS | 272 |
| 28 | 🇮🇩 ID | 262 |
| 29 | 🇲🇪 ME | 262 |
| 30 | 🇲🇴 MO | 259 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 623 |
| 2 | El Dorado International Airport |  | CO | 492 |
| 3 | Tokyo International Airport |  | JP | 489 |
| 4 | Denver International Airport |  | US | 448 |
| 5 | Indira Gandhi International Airport |  | IN | 447 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 366 |
| 7 | Harry Reid International Airport |  | US | 345 |
| 8 | La Aurora Airport |  | GT | 340 |
| 9 | Zurich Airport |  | CH | 306 |
| 10 | Frankfurt am Main International Airport |  | DE | 284 |
| 11 | Guaymaral Airport |  | CO | 276 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 275 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 273 |
| 14 | Chicago O'Hare International Airport |  | US | 272 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 268 |
| 16 | Macau International Airport |  | MO | 259 |
| 17 | Bengaluru International Airport |  | IN | 243 |
| 18 | Charlotte/Douglas International Airport |  | US | 242 |
| 19 | Kuala Lumpur International Airport |  | MY | 238 |
| 20 | Ninoy Aquino International Airport |  | PH | 235 |
| 21 | Tenerife Norte Airport |  | ES | 228 |
| 22 | Madrid Barajas International Airport |  | ES | 222 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 209 |
| 24 | Malpensa International Airport |  | IT | 208 |
| 25 | Salt Lake City International Airport |  | US | 206 |
| 26 | Congonhas Airport |  | BR | 205 |
| 27 | Daniel K Inouye International Airport |  | US | 201 |
| 28 | Reno/Tahoe International Airport |  | US | 194 |
| 29 | Charles de Gaulle International Airport |  | FR | 187 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 184 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 183 |
| 32 | Miami International Airport |  | US | 177 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 176 |
| 34 | O. R. Tambo International Airport |  | ZA | 170 |
| 35 | Seattle-Tacoma International Airport |  | US | 169 |
| 36 | Barcelona International Airport |  | ES | 169 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 168 |
| 38 | Vitoria/Foronda Airport |  | ES | 164 |
| 39 | Capua Airport |  | IT | 164 |
| 40 | Pune Airport |  | IN | 160 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 125 | 1h 8m | 706 km | 1,521.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 108 | 14m | 114 km | 211.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 104 | 24m | 225 km | 403.5 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 103 | 27m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 91 | 28m | 304 km | 477.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 76 | 1h 27m | 910 km | 1,192.6 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 68 | 27m | 152 km | 177.7 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 67 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 65 | 19m | 165 km | 184.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 60 | 1h 12m | 770 km | 797.1 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 55 | 55m | 546 km | 517.8 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 53 | 27m | 275 km | 251.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 52 | 31m | 369 km | 331.0 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 47 | 45m | 452 km | 366.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 22 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 45 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 43 | 13m | 99 km | 73.7 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 38 | 21m | 147 km | 96.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 36 | 1h 21m | 961 km | 596.7 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 36 | 15m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NGH28 | NGH | El Paso International Airport (KELP) | Iowa City Municipal Airport (KIOW) | 2026-04-10 05:03 UTC | 2026-04-10 07:25 UTC | 2h 22m |
| INR50310 | INR | Reus Air Base (LERS) | Castellon-Costa Azahar Airport (LEDS) | 2026-04-10 06:59 UTC | 2026-04-10 07:20 UTC | 20m |
| UWD24 | UWD | Destin Executive Airport (KDTS) | Washington Dulles International Airport (KIAD) | 2026-04-10 05:32 UTC | 2026-04-10 07:18 UTC | 1h 45m |
| 2611 |  | Chiang Mai International Airport (VTCC) | Chiang Mai International Airport (VTCC) | 2026-04-10 07:02 UTC | 2026-04-10 07:16 UTC | 13m |
| AUR202 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-04-10 06:54 UTC | 2026-04-10 07:07 UTC | 13m |
| CWA935 | CWA | Edmonton / Gartner Airport (CFQ7) | Two Hills Airport (CEL6) | 2026-04-10 06:44 UTC | 2026-04-10 06:59 UTC | 15m |
| AIB76TN | AIB | Toulouse-Blagnac Airport (LFBO) | Toulouse-Blagnac Airport (LFBO) | 2026-04-10 06:42 UTC | 2026-04-10 06:56 UTC | 14m |
| VTCNS | VTC | Safdarjung Airport (VIDD) | Kullu Manali Airport (VIBR) | 2026-04-10 06:02 UTC | 2026-04-10 06:52 UTC | 49m |
| WIF5P | WIF | Trondheim Airport Vaernes (ENVA) | Mosjøen Airport Kjaerstad (ENMS) | 2026-04-10 06:07 UTC | 2026-04-10 06:45 UTC | 37m |
| TRA275T | TRA | Eindhoven Airport (EHEH) | Vitoria/Foronda Airport (LEVT) | 2026-04-10 05:15 UTC | 2026-04-10 06:41 UTC | 1h 25m |
| EZY856 | easyJet | Aberdeen Dyce Airport (EGPD) | London Gatwick Airport (EGKK) | 2026-04-10 05:21 UTC | 2026-04-10 06:40 UTC | 1h 19m |
| VOE3544 | VOE | Asturias Airport (LEAS) | Federico Garcia Lorca Airport (LEGR) | 2026-04-10 05:29 UTC | 2026-04-10 06:40 UTC | 1h 10m |
| WIF1X | WIF | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 2026-04-10 06:36 UTC | 2026-04-10 06:39 UTC | 3m |
| BHA371 | BHA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-04-10 06:31 UTC | 2026-04-10 06:37 UTC | 6m |
| AXB2931 | AXB | Bengaluru International Airport (VOBL) | Yongphulla Airport (VQ10) | 2026-04-10 04:12 UTC | 2026-04-10 06:35 UTC | 2h 23m |
| GBA619 | GBA | Auckland International Airport (NZAA) | Whangarei Airport (NZWR) | 2026-04-10 06:10 UTC | 2026-04-10 06:33 UTC | 23m |
| KAA2481 | KAA | Gimpo International Airport (RKSS) | Daegu Airport (RKTN) | 2026-04-10 06:08 UTC | 2026-04-10 06:32 UTC | 24m |
| RYR81NH | Ryanair | Malaga Airport (LEMG) | Ifrane Airport (GMFI) | 2026-04-10 05:59 UTC | 2026-04-10 06:32 UTC | 32m |
| CJT620 | CJT | John C. Munro Hamilton International Airport (CYHM) | Chipman Airport (CCS4) | 2026-04-10 05:10 UTC | 2026-04-10 06:32 UTC | 1h 22m |
| APG223 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-04-10 06:08 UTC | 2026-04-10 06:31 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
