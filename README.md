# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_23:41:50_UTC-green)

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

**Latest saved flight:** 2026-04-06 23:41:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 23:41:50 UTC

- **21,173** saved flights
- **10,533** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **21,173** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **265,095.1 tonnes** estimated CO2 emissions
- **15,367,831 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 933 |
| 2 | Ryanair | 872 |
| 3 | IndiGo | 585 |
| 4 | American Airlines | 411 |
| 5 | EJA | 402 |
| 6 | Southwest Airlines | 307 |
| 7 | ENY | 292 |
| 8 | Lufthansa | 264 |
| 9 | Vueling | 225 |
| 10 | LATAM Airlines | 224 |
| 11 | AXM | 198 |
| 12 | Delta Air Lines | 189 |
| 13 | LXJ | 186 |
| 14 | All Nippon Airways | 176 |
| 15 | QLK | 173 |
| 16 | AZU | 168 |
| 17 | VIV | 155 |
| 18 | Swiss International | 154 |
| 19 | Alaska Airlines | 145 |
| 20 | easyJet | 143 |
| 21 | United Airlines | 143 |
| 22 | Avianca | 139 |
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
| 1 | 🇺🇸 US | 16897 |
| 2 | 🇮🇳 IN | 1782 |
| 3 | 🇪🇸 ES | 1666 |
| 4 | 🇦🇺 AU | 1463 |
| 5 | 🇧🇷 BR | 1223 |
| 6 | 🇨🇴 CO | 1171 |
| 7 | 🇯🇵 JP | 1094 |
| 8 | 🇮🇹 IT | 1035 |
| 9 | 🇩🇪 DE | 1029 |
| 10 | 🇨🇦 CA | 954 |
| 11 | 🇬🇧 GB | 826 |
| 12 | 🇫🇷 FR | 758 |
| 13 | 🇲🇽 MX | 719 |
| 14 | 🇬🇷 GR | 582 |
| 15 | 🇨🇭 CH | 566 |
| 16 | 🇬🇹 GT | 464 |
| 17 | 🇲🇾 MY | 464 |
| 18 | 🇿🇦 ZA | 461 |
| 19 | 🇳🇴 NO | 433 |
| 20 | 🇳🇿 NZ | 428 |
| 21 | 🇹🇷 TR | 411 |
| 22 | 🇵🇭 PH | 391 |
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
| 1 | Dallas-Fort Worth International Airport |  | US | 531 |
| 2 | El Dorado International Airport |  | CO | 441 |
| 3 | Denver International Airport |  | US | 393 |
| 4 | Tokyo International Airport |  | JP | 379 |
| 5 | Indira Gandhi International Airport |  | IN | 365 |
| 6 | La Aurora Airport |  | GT | 319 |
| 7 | Harry Reid International Airport |  | US | 283 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 276 |
| 9 | Zurich Airport |  | CH | 256 |
| 10 | Frankfurt am Main International Airport |  | DE | 236 |
| 11 | Chicago O'Hare International Airport |  | US | 232 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 231 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 229 |
| 14 | Guaymaral Airport |  | CO | 228 |
| 15 | Charlotte/Douglas International Airport |  | US | 208 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 208 |
| 17 | Bengaluru International Airport |  | IN | 201 |
| 18 | Macau International Airport |  | MO | 200 |
| 19 | Madrid Barajas International Airport |  | ES | 195 |
| 20 | Tenerife Norte Airport |  | ES | 191 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 187 |
| 22 | Congonhas Airport |  | BR | 181 |
| 23 | Ninoy Aquino International Airport |  | PH | 178 |
| 24 | Salt Lake City International Airport |  | US | 170 |
| 25 | Reno/Tahoe International Airport |  | US | 168 |
| 26 | Daniel K Inouye International Airport |  | US | 165 |
| 27 | Malpensa International Airport |  | IT | 162 |
| 28 | Kuala Lumpur International Airport |  | MY | 161 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 157 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 155 |
| 31 | Charles de Gaulle International Airport |  | FR | 153 |
| 32 | Miami International Airport |  | US | 152 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 147 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 146 |
| 35 | Vitoria/Foronda Airport |  | ES | 145 |
| 36 | O. R. Tambo International Airport |  | ZA | 143 |
| 37 | Pune Airport |  | IN | 142 |
| 38 | Barcelona International Airport |  | ES | 140 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 137 |
| 40 | Seattle-Tacoma International Airport |  | US | 137 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 96 | 1h 8m | 706 km | 1,168.8 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 94 | 14m | 114 km | 184.4 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 83 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 76 | 24m | 225 km | 294.8 t |
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
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 43 | 52m | 556 km | 412.2 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 42 | 55m | 546 km | 395.4 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 42 | 30m | 369 km | 267.3 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 41 | 9m | - | - |
| 21 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 39 | 4m | - | - |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 39 | 20m | 250 km | 168.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 37 | 58m | 723 km | 461.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 36 | 46m | 452 km | 280.6 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 32 | 1h 22m | 961 km | 530.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N605CA |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-04-06 23:19 UTC | 2026-04-06 23:41 UTC | 22m |
| N953PC |  | Bob Hope Airport (KBUR) | Henderson Executive Airport (KHND) | 2026-04-06 22:43 UTC | 2026-04-06 23:29 UTC | 45m |
| EJA828 | EJA | Cleveland-Hopkins International Airport (KCLE) | Rocky Mountain Metro Airport (KBJC) | 2026-04-06 20:40 UTC | 2026-04-06 23:27 UTC | 2h 47m |
| XBM | XBM | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-04-06 22:44 UTC | 2026-04-06 23:26 UTC | 41m |
| ASP864 | ASP | Calgary International Airport (CYYC) | Boeing Field/King County International Airport (KBFI) | 2026-04-06 22:09 UTC | 2026-04-06 23:23 UTC | 1h 13m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-06 23:06 UTC | 2026-04-06 23:18 UTC | 12m |
| N508ND |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-04-06 22:18 UTC | 2026-04-06 23:18 UTC | 59m |
| N213AP |  | Burnet Municipal/Kate Craddock Field (KBMQ) | Burnet Municipal/Kate Craddock Field (KBMQ) | 2026-04-06 22:25 UTC | 2026-04-06 23:15 UTC | 50m |
| FFP90 | FFP | Ted Stevens Anchorage International Airport (PANC) | Elmendorf Afb Airport (PAED) | 2026-04-06 22:34 UTC | 2026-04-06 23:12 UTC | 38m |
| N733FF |  | Casper/Natrona County International Airport (KCPR) | Chamberlain Brothers Ranch Airport (WY66) | 2026-04-06 22:49 UTC | 2026-04-06 23:12 UTC | 22m |
| N865TC |  | Friday Harbor Airport (KFHR) | Renton Municipal Airport (KRNT) | 2026-04-06 22:34 UTC | 2026-04-06 23:10 UTC | 36m |
| FWR1080 | FWR | Oxnard Airport (KOXR) | Truckee-Tahoe Airport (KTRK) | 2026-04-06 22:25 UTC | 2026-04-06 23:10 UTC | 44m |
| CRN911 | CRN | Kelowna Airport (CYLW) | Kaslo Airport (CBR2) | 2026-04-06 22:46 UTC | 2026-04-06 23:08 UTC | 22m |
| N3051W |  | Denton Enterprise Airport (KDTO) | Jim Sears Airport (3TA7) | 2026-04-06 22:48 UTC | 2026-04-06 23:07 UTC | 18m |
| AM376 |  | Melbourne Essendon Airport (YMEN) | Strathbogie Airport (YSBG) | 2026-04-06 22:43 UTC | 2026-04-06 23:04 UTC | 20m |
| N111BP |  | Lakefront Airport (KNEW) | St Paul Downtown Holman Field (KSTP) | 2026-04-06 20:23 UTC | 2026-04-06 23:03 UTC | 2h 40m |
| BRG671 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-04-06 22:31 UTC | 2026-04-06 23:02 UTC | 31m |
| N734UZ |  | San Luis Obispo County Regional Airport (KSBP) | 95CA (95CA) | 2026-04-06 22:26 UTC | 2026-04-06 22:59 UTC | 32m |
| ASA1088 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Bradshaw Army Airfield (PHSF) | 2026-04-06 22:43 UTC | 2026-04-06 22:59 UTC | 16m |
| SKW3679 | SkyWest Airlines | Salt Lake City International Airport (KSLC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-06 21:15 UTC | 2026-04-06 22:59 UTC | 1h 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
