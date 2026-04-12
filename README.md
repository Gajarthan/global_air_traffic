# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_23:44:57_UTC-green)

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

**Latest saved flight:** 2026-04-12 23:44:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 23:44:57 UTC

- **31,617** saved flights
- **14,330** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **31,617** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **388,343.9 tonnes** estimated CO2 emissions
- **22,512,688 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1315 |
| 2 | SkyWest Airlines | 1294 |
| 3 | IndiGo | 804 |
| 4 | EJA | 556 |
| 5 | American Airlines | 554 |
| 6 | Southwest Airlines | 461 |
| 7 | ENY | 429 |
| 8 | Lufthansa | 375 |
| 9 | AXM | 335 |
| 10 | LATAM Airlines | 324 |
| 11 | Vueling | 320 |
| 12 | All Nippon Airways | 287 |
| 13 | AZU | 284 |
| 14 | Delta Air Lines | 264 |
| 15 | QLK | 263 |
| 16 | LXJ | 254 |
| 17 | Swiss International | 233 |
| 18 | Alaska Airlines | 213 |
| 19 | easyJet | 211 |
| 20 | WIF | 206 |
| 21 | EJU | 205 |
| 22 | VIV | 204 |
| 23 | AEE | 197 |
| 24 | Japan Airlines | 197 |
| 25 | EDV | 189 |
| 26 | United Airlines | 184 |
| 27 | GLO | 173 |
| 28 | Avianca | 171 |
| 29 | Air France | 169 |
| 30 | JetBlue | 168 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 25012 |
| 2 | 🇮🇳 IN | 2471 |
| 3 | 🇪🇸 ES | 2339 |
| 4 | 🇦🇺 AU | 2202 |
| 5 | 🇧🇷 BR | 1890 |
| 6 | 🇯🇵 JP | 1715 |
| 7 | 🇮🇹 IT | 1650 |
| 8 | 🇨🇴 CO | 1598 |
| 9 | 🇩🇪 DE | 1593 |
| 10 | 🇨🇦 CA | 1537 |
| 11 | 🇬🇧 GB | 1275 |
| 12 | 🇫🇷 FR | 1158 |
| 13 | 🇲🇽 MX | 1015 |
| 14 | 🇬🇷 GR | 895 |
| 15 | 🇨🇭 CH | 880 |
| 16 | 🇲🇾 MY | 807 |
| 17 | 🇳🇴 NO | 695 |
| 18 | 🇳🇿 NZ | 677 |
| 19 | 🇿🇦 ZA | 646 |
| 20 | 🇬🇹 GT | 587 |
| 21 | 🇵🇭 PH | 587 |
| 22 | 🇹🇷 TR | 578 |
| 23 | 🇹🇭 TH | 569 |
| 24 | 🇰🇷 KR | 536 |
| 25 | 🇵🇱 PL | 478 |
| 26 | 🇲🇦 MA | 406 |
| 27 | 🇧🇸 BS | 331 |
| 28 | 🇲🇪 ME | 313 |
| 29 | 🇳🇱 NL | 300 |
| 30 | 🇮🇩 ID | 297 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 765 |
| 2 | Tokyo International Airport |  | JP | 577 |
| 3 | El Dorado International Airport |  | CO | 568 |
| 4 | Denver International Airport |  | US | 538 |
| 5 | Indira Gandhi International Airport |  | IN | 521 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 437 |
| 7 | La Aurora Airport |  | GT | 425 |
| 8 | Harry Reid International Airport |  | US | 412 |
| 9 | Guaymaral Airport |  | CO | 388 |
| 10 | Zurich Airport |  | CH | 387 |
| 11 | Chicago O'Hare International Airport |  | US | 330 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 329 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 327 |
| 14 | Frankfurt am Main International Airport |  | DE | 320 |
| 15 | Kuala Lumpur International Airport |  | MY | 306 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 305 |
| 17 | Macau International Airport |  | MO | 297 |
| 18 | Charlotte/Douglas International Airport |  | US | 289 |
| 19 | Tenerife Norte Airport |  | ES | 282 |
| 20 | Madrid Barajas International Airport |  | ES | 281 |
| 21 | Bengaluru International Airport |  | IN | 281 |
| 22 | Congonhas Airport |  | BR | 277 |
| 23 | Ninoy Aquino International Airport |  | PH | 270 |
| 24 | Malpensa International Airport |  | IT | 257 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 243 |
| 26 | Salt Lake City International Airport |  | US | 243 |
| 27 | Daniel K Inouye International Airport |  | US | 241 |
| 28 | Reno/Tahoe International Airport |  | US | 240 |
| 29 | Charles de Gaulle International Airport |  | FR | 230 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 229 |
| 31 | John Paul II International Airport Kraków-Balice Airport |  | PL | 217 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 216 |
| 33 | Capua Airport |  | IT | 216 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 215 |
| 35 | Miami International Airport |  | US | 210 |
| 36 | O. R. Tambo International Airport |  | ZA | 209 |
| 37 | Vitoria/Foronda Airport |  | ES | 207 |
| 38 | Seattle-Tacoma International Airport |  | US | 202 |
| 39 | Barcelona International Airport |  | ES | 197 |
| 40 | Viracopos International Airport |  | BR | 196 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 151 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 146 | 1h 8m | 706 km | 1,777.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 134 | 14m | 114 km | 262.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 114 | 24m | 225 km | 442.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 104 | 28m | 304 km | 545.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 91 | 1h 28m | 910 km | 1,428.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 81 | 19m | 165 km | 230.4 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 76 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 75 | 31m | - | - |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 70 | 55m | 546 km | 659.1 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 67 | 27m | 275 km | 317.5 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 66 | 1h 12m | 770 km | 876.8 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 63 | 21m | 244 km | 265.3 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 62 | 31m | 369 km | 394.6 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 19 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 57 | 45m | 452 km | 444.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 54 | 20m | 250 km | 233.2 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 48 | 20m | 147 km | 121.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 48 | 1h 42m | 1,423 km | 1,178.0 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 47 | 16m | 162 km | 131.7 t |
| 27 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 44 | 12m | 15 km | 11.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N91804 |  | Flandreau Municipal Airport (K4P3) | Harold Davidson Field (KVMR) | 2026-04-12 23:09 UTC | 2026-04-12 23:44 UTC | 35m |
| LXJ342 | LXJ | Napa County Airport (KAPC) | Teterboro Airport (KTEB) | 2026-04-12 18:37 UTC | 2026-04-12 23:22 UTC | 4h 44m |
| ZKIDU | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-04-12 23:07 UTC | 2026-04-12 23:21 UTC | 14m |
| N619FB |  | Bermuda Dunes Airport (KUDD) | Santa Monica Municipal Airport (KSMO) | 2026-04-12 22:37 UTC | 2026-04-12 23:17 UTC | 40m |
| N105JF |  | North Raleigh Airport (00NC) | North Raleigh Airport (00NC) | 2026-04-12 23:00 UTC | 2026-04-12 23:14 UTC | 13m |
| ANO162 | ANO | Darwin International Airport (YPDN) | Emkaytee (Unlic) Airport (YMKT) | 2026-04-12 23:01 UTC | 2026-04-12 23:05 UTC | 4m |
| LXJ449 | LXJ | Bermuda Dunes Airport (KUDD) | Van Nuys Airport (KVNY) | 2026-04-12 22:32 UTC | 2026-04-12 23:04 UTC | 32m |
| UAE9862 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-12 16:47 UTC | 2026-04-12 23:02 UTC | 6h 15m |
| CGFHA | CGF | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-04-12 22:42 UTC | 2026-04-12 22:58 UTC | 16m |
| LXJ556 | LXJ | Chicago O'Hare International Airport (KORD) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-12 22:11 UTC | 2026-04-12 22:57 UTC | 45m |
| AM318 |  | Melbourne Essendon Airport (YMEN) | RAAF Base East Sale (YMES) | 2026-04-12 22:28 UTC | 2026-04-12 22:55 UTC | 27m |
| BRG2682 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-04-12 22:20 UTC | 2026-04-12 22:54 UTC | 34m |
| RFS708 | RFS | Boeing Field/King County International Airport (KBFI) | Portland-Hillsboro Airport (KHIO) | 2026-04-12 21:34 UTC | 2026-04-12 22:54 UTC | 1h 20m |
| AUB1319 | AUB | Auburn University Regional Airport (KAUO) | Auburn University Regional Airport (KAUO) | 2026-04-12 21:49 UTC | 2026-04-12 22:52 UTC | 1h 2m |
| N953PC |  | Santa Barbara Municipal Airport (KSBA) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-12 22:05 UTC | 2026-04-12 22:51 UTC | 46m |
| AAL3207 | American Airlines | Ronald Reagan Washington Ntl Airport (KDCA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-12 21:22 UTC | 2026-04-12 22:51 UTC | 1h 29m |
| FDY158 | FDY | Pittsburgh International Airport (KPIT) | Lancaster Airport (KLNS) | 2026-04-12 21:42 UTC | 2026-04-12 22:51 UTC | 1h 9m |
| N444AM |  | Barrett Field (MS96) | Rockfish Airport (VG22) | 2026-04-12 21:25 UTC | 2026-04-12 22:51 UTC | 1h 25m |
| N884MC |  | Sugar Land Regional Airport (KSGR) | Cloud Nine Airport (ND98) | 2026-04-12 20:31 UTC | 2026-04-12 22:49 UTC | 2h 17m |
| UTY6520 | UTY | Perth International Airport (YPPH) | Orient Well Airport (YORW) | 2026-04-12 21:58 UTC | 2026-04-12 22:49 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
