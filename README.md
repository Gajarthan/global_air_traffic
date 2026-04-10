# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_05:55:03_UTC-green)

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

**Latest saved flight:** 2026-04-10 05:55:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 05:55:03 UTC

- **26,341** saved flights
- **12,547** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **26,341** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **324,418.0 tonnes** estimated CO2 emissions
- **18,806,841 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1082 |
| 2 | Ryanair | 1077 |
| 3 | IndiGo | 706 |
| 4 | EJA | 473 |
| 5 | American Airlines | 471 |
| 6 | Southwest Airlines | 380 |
| 7 | ENY | 350 |
| 8 | Lufthansa | 338 |
| 9 | Vueling | 266 |
| 10 | AXM | 265 |
| 11 | LATAM Airlines | 259 |
| 12 | QLK | 238 |
| 13 | All Nippon Airways | 233 |
| 14 | Delta Air Lines | 220 |
| 15 | LXJ | 212 |
| 16 | AZU | 210 |
| 17 | Swiss International | 181 |
| 18 | Alaska Airlines | 180 |
| 19 | VIV | 176 |
| 20 | Japan Airlines | 175 |
| 21 | EJU | 169 |
| 22 | easyJet | 169 |
| 23 | AEE | 166 |
| 24 | WIF | 166 |
| 25 | United Airlines | 159 |
| 26 | EDV | 155 |
| 27 | Avianca | 150 |
| 28 | AXB | 144 |
| 29 | JetBlue | 140 |
| 30 | ANZ | 137 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 20813 |
| 2 | 🇮🇳 IN | 2169 |
| 3 | 🇦🇺 AU | 1949 |
| 4 | 🇪🇸 ES | 1944 |
| 5 | 🇧🇷 BR | 1482 |
| 6 | 🇯🇵 JP | 1455 |
| 7 | 🇩🇪 DE | 1344 |
| 8 | 🇮🇹 IT | 1336 |
| 9 | 🇨🇴 CO | 1322 |
| 10 | 🇨🇦 CA | 1258 |
| 11 | 🇬🇧 GB | 1046 |
| 12 | 🇫🇷 FR | 964 |
| 13 | 🇲🇽 MX | 851 |
| 14 | 🇬🇷 GR | 749 |
| 15 | 🇨🇭 CH | 716 |
| 16 | 🇲🇾 MY | 639 |
| 17 | 🇳🇿 NZ | 600 |
| 18 | 🇳🇴 NO | 561 |
| 19 | 🇿🇦 ZA | 532 |
| 20 | 🇵🇭 PH | 496 |
| 21 | 🇹🇷 TR | 494 |
| 22 | 🇬🇹 GT | 490 |
| 23 | 🇰🇷 KR | 459 |
| 24 | 🇹🇭 TH | 453 |
| 25 | 🇵🇱 PL | 386 |
| 26 | 🇲🇦 MA | 322 |
| 27 | 🇧🇸 BS | 272 |
| 28 | 🇲🇪 ME | 261 |
| 29 | 🇮🇩 ID | 260 |
| 30 | 🇲🇴 MO | 259 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 623 |
| 2 | El Dorado International Airport |  | CO | 492 |
| 3 | Tokyo International Airport |  | JP | 487 |
| 4 | Denver International Airport |  | US | 448 |
| 5 | Indira Gandhi International Airport |  | IN | 445 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 365 |
| 7 | Harry Reid International Airport |  | US | 345 |
| 8 | La Aurora Airport |  | GT | 340 |
| 9 | Zurich Airport |  | CH | 306 |
| 10 | Frankfurt am Main International Airport |  | DE | 284 |
| 11 | Guaymaral Airport |  | CO | 276 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 275 |
| 13 | Chicago O'Hare International Airport |  | US | 272 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 270 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 268 |
| 16 | Macau International Airport |  | MO | 259 |
| 17 | Charlotte/Douglas International Airport |  | US | 242 |
| 18 | Bengaluru International Airport |  | IN | 241 |
| 19 | Kuala Lumpur International Airport |  | MY | 236 |
| 20 | Ninoy Aquino International Airport |  | PH | 231 |
| 21 | Tenerife Norte Airport |  | ES | 228 |
| 22 | Madrid Barajas International Airport |  | ES | 222 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 209 |
| 24 | Malpensa International Airport |  | IT | 206 |
| 25 | Salt Lake City International Airport |  | US | 206 |
| 26 | Congonhas Airport |  | BR | 205 |
| 27 | Daniel K Inouye International Airport |  | US | 201 |
| 28 | Reno/Tahoe International Airport |  | US | 194 |
| 29 | Charles de Gaulle International Airport |  | FR | 186 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 184 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 183 |
| 32 | Miami International Airport |  | US | 177 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 176 |
| 34 | Seattle-Tacoma International Airport |  | US | 169 |
| 35 | Barcelona International Airport |  | ES | 168 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 168 |
| 37 | O. R. Tambo International Airport |  | ZA | 168 |
| 38 | Capua Airport |  | IT | 164 |
| 39 | Vitoria/Foronda Airport |  | ES | 163 |
| 40 | Pune Airport |  | IN | 160 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 125 | 1h 8m | 706 km | 1,521.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 108 | 14m | 114 km | 211.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 103 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 100 | 24m | 225 km | 388.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 89 | 28m | 304 km | 466.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 76 | 1h 27m | 910 km | 1,192.6 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 68 | 27m | 152 km | 177.7 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 66 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 65 | 19m | 165 km | 184.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 59 | 1h 12m | 770 km | 783.8 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 54 | 55m | 546 km | 508.4 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 53 | 27m | 275 km | 251.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 52 | 31m | 369 km | 331.0 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 47 | 45m | 452 km | 366.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 46 | 20m | 250 km | 198.7 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 45 | 9m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 24 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 44 | 4m | - | - |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 43 | 13m | 99 km | 73.7 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 38 | 21m | 147 km | 96.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 36 | 1h 21m | 961 km | 596.7 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 36 | 15m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 4XHZP |  | LL59 (LL59) | LL59 (LL59) | 2026-04-10 05:54 UTC | 2026-04-10 05:55 UTC | 0m |
| ZKPDZ | ZKP | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-10 05:12 UTC | 2026-04-10 05:25 UTC | 13m |
| OKC | OKC | Orange Airport (YORG) | Sydney Bankstown Airport (YSBK) | 2026-04-10 04:43 UTC | 2026-04-10 05:13 UTC | 29m |
| JMU | JMU | Melbourne Essendon Airport (YMEN) | RAAF Base East Sale (YMES) | 2026-04-10 04:48 UTC | 2026-04-10 05:12 UTC | 24m |
| KAL699T | Korean Air | Gimpo International Airport (RKSS) | Daegu Airport (RKTN) | 2026-04-10 04:45 UTC | 2026-04-10 05:09 UTC | 24m |
| BHA355 | BHA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-04-10 05:02 UTC | 2026-04-10 05:08 UTC | 5m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-04-10 04:25 UTC | 2026-04-10 05:06 UTC | 40m |
| UAL2001 | United Airlines | San Francisco International Airport (KSFO) | Gardner Municipal Airport (KGDM) | 2026-04-09 23:39 UTC | 2026-04-10 05:05 UTC | 5h 26m |
| KLW | KLW | Sunshine Coast Airport (YBMC) | Tangalooma Airport (YTGA) | 2026-04-10 04:37 UTC | 2026-04-10 05:04 UTC | 26m |
| LICHEN9 | LIC | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-10 03:38 UTC | 2026-04-10 05:03 UTC | 1h 24m |
| AIQ4501 | AIQ | Suvarnabhumi Airport (VTBS) | Nakhon Ratchasima Airport (VTUQ) | 2026-04-10 04:34 UTC | 2026-04-10 04:59 UTC | 25m |
| AEE282 | AEE | Eleftherios Venizelos International Airport (LGAV) | Aktion National Airport (LGPZ) | 2026-04-10 04:27 UTC | 2026-04-10 04:58 UTC | 31m |
| LR455 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-10 04:28 UTC | 2026-04-10 04:58 UTC | 30m |
| RXA2125 | RXA | Perth International Airport (YPPH) | Cranbrook Airport (YCRN) | 2026-04-10 04:10 UTC | 2026-04-10 04:57 UTC | 46m |
| ASL57F | ASL | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 2026-04-10 04:38 UTC | 2026-04-10 04:56 UTC | 18m |
| AE921 |  | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-04-10 04:33 UTC | 2026-04-10 04:54 UTC | 21m |
| SQV | SQV | Melbourne Essendon Airport (YMEN) | Albury Airport (YMAY) | 2026-04-10 04:06 UTC | 2026-04-10 04:53 UTC | 47m |
| N565JT |  | Miami-Opa Locka Executive Airport (KOPF) | John F Kennedy International Airport (KJFK) | 2026-04-10 02:31 UTC | 2026-04-10 04:53 UTC | 2h 21m |
| UAL124 | United Airlines | Newark Liberty International Airport (KEWR) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-09 20:24 UTC | 2026-04-10 04:51 UTC | 8h 26m |
| RYR5914 | Ryanair | Malpensa International Airport (LIMC) | Capua Airport (LIAU) | 2026-04-10 03:58 UTC | 2026-04-10 04:50 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
