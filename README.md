# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_03:50:38_UTC-green)

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

**Latest saved flight:** 2026-04-08 03:50:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 03:50:38 UTC

- **22,623** saved flights
- **11,115** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **22,623** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **279,549.9 tonnes** estimated CO2 emissions
- **16,205,790 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 970 |
| 2 | Ryanair | 929 |
| 3 | IndiGo | 629 |
| 4 | EJA | 422 |
| 5 | American Airlines | 419 |
| 6 | Southwest Airlines | 329 |
| 7 | ENY | 302 |
| 8 | Lufthansa | 281 |
| 9 | Vueling | 233 |
| 10 | LATAM Airlines | 230 |
| 11 | AXM | 225 |
| 12 | QLK | 201 |
| 13 | All Nippon Airways | 200 |
| 14 | Delta Air Lines | 197 |
| 15 | LXJ | 189 |
| 16 | AZU | 178 |
| 17 | Swiss International | 162 |
| 18 | VIV | 162 |
| 19 | Alaska Airlines | 156 |
| 20 | Japan Airlines | 155 |
| 21 | easyJet | 149 |
| 22 | United Airlines | 146 |
| 23 | EJU | 143 |
| 24 | Avianca | 139 |
| 25 | AEE | 138 |
| 26 | EDV | 135 |
| 27 | WIF | 134 |
| 28 | AXB | 127 |
| 29 | Air France | 119 |
| 30 | JetBlue | 116 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 17945 |
| 2 | 🇮🇳 IN | 1915 |
| 3 | 🇪🇸 ES | 1739 |
| 4 | 🇦🇺 AU | 1644 |
| 5 | 🇧🇷 BR | 1278 |
| 6 | 🇯🇵 JP | 1259 |
| 7 | 🇨🇴 CO | 1181 |
| 8 | 🇮🇹 IT | 1128 |
| 9 | 🇩🇪 DE | 1112 |
| 10 | 🇨🇦 CA | 1019 |
| 11 | 🇬🇧 GB | 884 |
| 12 | 🇫🇷 FR | 818 |
| 13 | 🇲🇽 MX | 745 |
| 14 | 🇬🇷 GR | 630 |
| 15 | 🇨🇭 CH | 605 |
| 16 | 🇲🇾 MY | 524 |
| 17 | 🇿🇦 ZA | 492 |
| 18 | 🇳🇿 NZ | 477 |
| 19 | 🇳🇴 NO | 467 |
| 20 | 🇬🇹 GT | 467 |
| 21 | 🇹🇷 TR | 431 |
| 22 | 🇵🇭 PH | 427 |
| 23 | 🇰🇷 KR | 402 |
| 24 | 🇹🇭 TH | 354 |
| 25 | 🇵🇱 PL | 321 |
| 26 | 🇲🇦 MA | 269 |
| 27 | 🇧🇸 BS | 243 |
| 28 | 🇮🇩 ID | 233 |
| 29 | 🇲🇪 ME | 231 |
| 30 | 🇳🇱 NL | 221 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 550 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 423 |
| 4 | Denver International Airport |  | US | 406 |
| 5 | Indira Gandhi International Airport |  | IN | 386 |
| 6 | La Aurora Airport |  | GT | 322 |
| 7 | Harry Reid International Airport |  | US | 307 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 302 |
| 9 | Zurich Airport |  | CH | 270 |
| 10 | Frankfurt am Main International Airport |  | DE | 248 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 241 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 241 |
| 13 | Chicago O'Hare International Airport |  | US | 237 |
| 14 | Guaymaral Airport |  | CO | 236 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 230 |
| 16 | Bengaluru International Airport |  | IN | 217 |
| 17 | Charlotte/Douglas International Airport |  | US | 214 |
| 18 | Macau International Airport |  | MO | 209 |
| 19 | Tenerife Norte Airport |  | ES | 202 |
| 20 | Madrid Barajas International Airport |  | ES | 200 |
| 21 | Ninoy Aquino International Airport |  | PH | 195 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 192 |
| 23 | Kuala Lumpur International Airport |  | MY | 190 |
| 24 | Congonhas Airport |  | BR | 186 |
| 25 | Salt Lake City International Airport |  | US | 182 |
| 26 | Malpensa International Airport |  | IT | 174 |
| 27 | Daniel K Inouye International Airport |  | US | 174 |
| 28 | Reno/Tahoe International Airport |  | US | 174 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 170 |
| 30 | Charles de Gaulle International Airport |  | FR | 164 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 162 |
| 32 | Miami International Airport |  | US | 155 |
| 33 | O. R. Tambo International Airport |  | ZA | 153 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 151 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 151 |
| 36 | Pune Airport |  | IN | 151 |
| 37 | Seattle-Tacoma International Airport |  | US | 148 |
| 38 | Vitoria/Foronda Airport |  | ES | 147 |
| 39 | Barcelona International Airport |  | ES | 145 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 140 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 106 | 1h 8m | 706 km | 1,290.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 87 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 84 | 24m | 225 km | 325.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 80 | 28m | 304 km | 419.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 68 | 1h 28m | 910 km | 1,067.1 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 66 | 27m | 152 km | 172.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 62 | 1h 42m | 1,156 km | 1,236.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 53 | 19m | 165 km | 150.8 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 50 | 1h 13m | 770 km | 664.2 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 49 | 55m | 546 km | 461.3 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 45 | 31m | 369 km | 286.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 45 | 52m | 556 km | 431.4 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 42 | 20m | 250 km | 181.4 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 42 | 9m | - | - |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 41 | 4m | - | - |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 40 | 46m | 452 km | 311.7 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 33 | 1h 22m | 961 km | 547.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| R03332 |  | Gray Army Air Field (Joint Base Lewis-Mcchord) Airport (KGRF) | 3WA9 (3WA9) | 2026-04-08 03:15 UTC | 2026-04-08 03:50 UTC | 35m |
| N472LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-04-08 01:18 UTC | 2026-04-08 03:48 UTC | 2h 29m |
| NIJ | NIJ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-08 03:07 UTC | 2026-04-08 03:39 UTC | 32m |
| VJT749 | VJT | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-04-07 16:39 UTC | 2026-04-08 03:36 UTC | 10h 57m |
| NKZ | NKZ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-08 03:16 UTC | 2026-04-08 03:30 UTC | 14m |
| REH71 | REH | Silver West Airport (KC08) | Usaf Academy Davis Airfield (KAFF) | 2026-04-08 02:49 UTC | 2026-04-08 03:19 UTC | 30m |
| RUCK90 | RUC | Clayton Municipal Airport (K11A) | Clayton Municipal Airport (K11A) | 2026-04-08 03:08 UTC | 2026-04-08 03:19 UTC | 10m |
| ZKIDH | ZKI | Invercargill Airport (NZNV) | Taieri Airport (NZTI) | 2026-04-08 02:28 UTC | 2026-04-08 03:17 UTC | 48m |
| N131GC |  | Harry Reid International Airport (KLAS) | Harry Reid International Airport (KLAS) | 2026-04-08 03:06 UTC | 2026-04-08 03:15 UTC | 9m |
| JHH | JHH | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-08 02:58 UTC | 2026-04-08 03:13 UTC | 15m |
| CCA101 | Air China | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-04-08 00:22 UTC | 2026-04-08 03:08 UTC | 2h 45m |
| N426RB |  | Double W Airport (3OK7) | Double W Airport (3OK7) | 2026-04-08 02:48 UTC | 2026-04-08 03:07 UTC | 18m |
| YOQ | YOQ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-08 02:48 UTC | 2026-04-08 03:06 UTC | 18m |
| AXM431 | AXM | Kuala Lumpur International Airport (WMKK) | Sultan Syarif Kasim Ii (Simpang Tiga) Airport (WIBB) | 2026-04-08 02:45 UTC | 2026-04-08 03:06 UTC | 21m |
| N643SA |  | Addison Airport (KADS) | Austin-Bergstrom International Airport (KAUS) | 2026-04-08 01:40 UTC | 2026-04-08 03:05 UTC | 1h 25m |
| VAR450 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-04-08 02:53 UTC | 2026-04-08 03:00 UTC | 7m |
| AL2 |  | Hervey Bay Airport (YHBA) | Hervey Bay Airport (YHBA) | 2026-04-08 02:35 UTC | 2026-04-08 02:58 UTC | 22m |
| UAE9780 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-04-07 20:45 UTC | 2026-04-08 02:58 UTC | 6h 12m |
| NDU841 | NDU | Mesa Gateway Airport (KIWA) | Tombstone Municipal Airport (KP29) | 2026-04-08 01:22 UTC | 2026-04-08 02:54 UTC | 1h 32m |
| ANZ774M | ANZ | Christchurch International Airport (NZCH) | Kowhai Aerodrome (NZKY) | 2026-04-08 01:40 UTC | 2026-04-08 02:50 UTC | 1h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
