# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_23:18:09_UTC-green)

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

**Latest saved flight:** 2026-04-06 23:18:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 23:18:09 UTC

- **21,094** saved flights
- **10,512** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **21,094** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **264,210.5 tonnes** estimated CO2 emissions
- **15,316,554 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 926 |
| 2 | Ryanair | 872 |
| 3 | IndiGo | 584 |
| 4 | American Airlines | 408 |
| 5 | EJA | 400 |
| 6 | Southwest Airlines | 304 |
| 7 | ENY | 287 |
| 8 | Lufthansa | 264 |
| 9 | Vueling | 225 |
| 10 | LATAM Airlines | 220 |
| 11 | AXM | 198 |
| 12 | LXJ | 186 |
| 13 | Delta Air Lines | 185 |
| 14 | All Nippon Airways | 176 |
| 15 | QLK | 172 |
| 16 | AZU | 166 |
| 17 | Swiss International | 154 |
| 18 | VIV | 154 |
| 19 | Alaska Airlines | 144 |
| 20 | easyJet | 143 |
| 21 | United Airlines | 142 |
| 22 | Avianca | 138 |
| 23 | EJU | 135 |
| 24 | Japan Airlines | 134 |
| 25 | AEE | 128 |
| 26 | EDV | 127 |
| 27 | WIF | 126 |
| 28 | AXB | 119 |
| 29 | Air France | 111 |
| 30 | BRC | 111 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 16798 |
| 2 | 🇮🇳 IN | 1780 |
| 3 | 🇪🇸 ES | 1666 |
| 4 | 🇦🇺 AU | 1452 |
| 5 | 🇧🇷 BR | 1209 |
| 6 | 🇨🇴 CO | 1163 |
| 7 | 🇯🇵 JP | 1092 |
| 8 | 🇮🇹 IT | 1035 |
| 9 | 🇩🇪 DE | 1029 |
| 10 | 🇨🇦 CA | 948 |
| 11 | 🇬🇧 GB | 826 |
| 12 | 🇫🇷 FR | 758 |
| 13 | 🇲🇽 MX | 717 |
| 14 | 🇬🇷 GR | 582 |
| 15 | 🇨🇭 CH | 566 |
| 16 | 🇲🇾 MY | 464 |
| 17 | 🇬🇹 GT | 462 |
| 18 | 🇿🇦 ZA | 461 |
| 19 | 🇳🇴 NO | 433 |
| 20 | 🇳🇿 NZ | 428 |
| 21 | 🇹🇷 TR | 411 |
| 22 | 🇵🇭 PH | 385 |
| 23 | 🇰🇷 KR | 351 |
| 24 | 🇹🇭 TH | 307 |
| 25 | 🇵🇱 PL | 306 |
| 26 | 🇲🇦 MA | 258 |
| 27 | 🇧🇸 BS | 235 |
| 28 | 🇲🇪 ME | 219 |
| 29 | 🇮🇩 ID | 214 |
| 30 | 🇳🇱 NL | 209 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 526 |
| 2 | El Dorado International Airport |  | CO | 438 |
| 3 | Denver International Airport |  | US | 391 |
| 4 | Tokyo International Airport |  | JP | 378 |
| 5 | Indira Gandhi International Airport |  | IN | 365 |
| 6 | La Aurora Airport |  | GT | 317 |
| 7 | Harry Reid International Airport |  | US | 281 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 276 |
| 9 | Zurich Airport |  | CH | 256 |
| 10 | Frankfurt am Main International Airport |  | DE | 236 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 231 |
| 12 | Chicago O'Hare International Airport |  | US | 230 |
| 13 | Guaymaral Airport |  | CO | 228 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 227 |
| 15 | Charlotte/Douglas International Airport |  | US | 207 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 207 |
| 17 | Macau International Airport |  | MO | 200 |
| 18 | Bengaluru International Airport |  | IN | 200 |
| 19 | Madrid Barajas International Airport |  | ES | 195 |
| 20 | Tenerife Norte Airport |  | ES | 191 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 186 |
| 22 | Congonhas Airport |  | BR | 178 |
| 23 | Ninoy Aquino International Airport |  | PH | 175 |
| 24 | Salt Lake City International Airport |  | US | 166 |
| 25 | Reno/Tahoe International Airport |  | US | 165 |
| 26 | Daniel K Inouye International Airport |  | US | 164 |
| 27 | Malpensa International Airport |  | IT | 162 |
| 28 | Kuala Lumpur International Airport |  | MY | 161 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 156 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 155 |
| 31 | Charles de Gaulle International Airport |  | FR | 153 |
| 32 | Miami International Airport |  | US | 150 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 147 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 145 |
| 35 | Vitoria/Foronda Airport |  | ES | 145 |
| 36 | O. R. Tambo International Airport |  | ZA | 143 |
| 37 | Pune Airport |  | IN | 141 |
| 38 | Barcelona International Airport |  | ES | 140 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 137 |
| 40 | Seattle-Tacoma International Airport |  | US | 136 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 95 | 1h 8m | 706 km | 1,156.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 93 | 14m | 114 km | 182.4 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 83 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 75 | 24m | 225 km | 291.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 69 | 28m | 304 km | 361.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 60 | 1h 43m | 1,156 km | 1,197.0 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 60 | 1h 27m | 910 km | 941.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 58 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 46 | 19m | 165 km | 130.8 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 45 | 1h 12m | 770 km | 597.8 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 44 | 23m | 252 km | 191.0 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 42 | 55m | 546 km | 395.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 42 | 30m | 369 km | 267.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 42 | 52m | 556 km | 402.6 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 40 | 10m | - | - |
| 21 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 39 | 4m | - | - |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 39 | 20m | 250 km | 168.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 36 | 58m | 723 km | 448.8 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 36 | 46m | 452 km | 280.6 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 32 | 1h 22m | 961 km | 530.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N508ND |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-04-06 22:18 UTC | 2026-04-06 23:18 UTC | 59m |
| N213AP |  | Burnet Municipal/Kate Craddock Field (KBMQ) | Burnet Municipal/Kate Craddock Field (KBMQ) | 2026-04-06 22:25 UTC | 2026-04-06 23:15 UTC | 50m |
| N865TC |  | Friday Harbor Airport (KFHR) | Renton Municipal Airport (KRNT) | 2026-04-06 22:34 UTC | 2026-04-06 23:10 UTC | 36m |
| N3051W |  | Denton Enterprise Airport (KDTO) | Jim Sears Airport (3TA7) | 2026-04-06 22:48 UTC | 2026-04-06 23:07 UTC | 18m |
| N111BP |  | Lakefront Airport (KNEW) | St Paul Downtown Holman Field (KSTP) | 2026-04-06 20:23 UTC | 2026-04-06 23:03 UTC | 2h 40m |
| BRG671 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-04-06 22:31 UTC | 2026-04-06 23:02 UTC | 31m |
| N734UZ |  | San Luis Obispo County Regional Airport (KSBP) | 95CA (95CA) | 2026-04-06 22:26 UTC | 2026-04-06 22:59 UTC | 32m |
| GLT202 | GLT | Augusta Regional At Bush Field (KAGS) | Booneville/Baldwyn Airport (K8M1) | 2026-04-06 22:01 UTC | 2026-04-06 22:56 UTC | 55m |
| N38PA |  | Hopkinsville-Christian County Airport (KHVC) | Socks Flyers Airport (29KY) | 2026-04-06 22:24 UTC | 2026-04-06 22:54 UTC | 29m |
| N608UW |  | 9WN5 (9WN5) | Dane County Regional/Truax Field (KMSN) | 2026-04-06 22:44 UTC | 2026-04-06 22:54 UTC | 9m |
| N5158J |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Kimball Municipal/Robert E Arraj Field (KIBM) | 2026-04-06 22:16 UTC | 2026-04-06 22:47 UTC | 30m |
| N307CM |  | Dodge Center Airport (KTOB) | Northern Colorado Regional Airport (KFNL) | 2026-04-06 20:23 UTC | 2026-04-06 22:46 UTC | 2h 23m |
| N950P |  | North Texas Regional/Perrin Field (KGYI) | Cavern City Air Trml Airport (KCNM) | 2026-04-06 21:26 UTC | 2026-04-06 22:46 UTC | 1h 19m |
| PPSCF | PPS | Pinto Martins International Airport (SBFZ) | SWBE (SWBE) | 2026-04-06 22:17 UTC | 2026-04-06 22:42 UTC | 24m |
| N322EF |  | Davidson County Executive Airport (KEXX) | 67NC (67NC) | 2026-04-06 22:14 UTC | 2026-04-06 22:40 UTC | 26m |
| VOZ9429 | Virgin Australia | Perth International Airport (YPPH) | Busselton Regional Airport (YBLN) | 2026-04-06 22:10 UTC | 2026-04-06 22:37 UTC | 26m |
| N748CX |  | Iowa City Municipal Airport (KIOW) | Z M Jack Stell Field (KCRT) | 2026-04-06 21:16 UTC | 2026-04-06 22:35 UTC | 1h 18m |
| EJA816 | EJA | John Wayne/Orange County Airport (KSNA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-06 18:02 UTC | 2026-04-06 22:34 UTC | 4h 32m |
| LR453 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-06 22:05 UTC | 2026-04-06 22:34 UTC | 29m |
| QLK376D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-06 22:10 UTC | 2026-04-06 22:34 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
