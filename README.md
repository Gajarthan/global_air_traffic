# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_19:43:54_UTC-green)

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

**Latest saved flight:** 2026-04-04 19:43:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 19:43:54 UTC

- **16,654** saved flights
- **8,801** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **16,654** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **207,212.2 tonnes** estimated CO2 emissions
- **12,012,302 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 722 |
| 2 | Ryanair | 678 |
| 3 | IndiGo | 480 |
| 4 | EJA | 318 |
| 5 | American Airlines | 298 |
| 6 | Lufthansa | 238 |
| 7 | Southwest Airlines | 237 |
| 8 | ENY | 218 |
| 9 | Vueling | 186 |
| 10 | LATAM Airlines | 178 |
| 11 | AXM | 161 |
| 12 | LXJ | 144 |
| 13 | All Nippon Airways | 141 |
| 14 | Delta Air Lines | 139 |
| 15 | QLK | 137 |
| 16 | AZU | 127 |
| 17 | VIV | 124 |
| 18 | Swiss International | 123 |
| 19 | EJU | 109 |
| 20 | Alaska Airlines | 108 |
| 21 | Japan Airlines | 107 |
| 22 | Avianca | 106 |
| 23 | United Airlines | 106 |
| 24 | AEE | 105 |
| 25 | AXB | 104 |
| 26 | easyJet | 104 |
| 27 | WIF | 102 |
| 28 | EDV | 101 |
| 29 | BRC | 97 |
| 30 | GLO | 96 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13210 |
| 2 | 🇮🇳 IN | 1460 |
| 3 | 🇪🇸 ES | 1378 |
| 4 | 🇦🇺 AU | 1210 |
| 5 | 🇧🇷 BR | 972 |
| 6 | 🇩🇪 DE | 870 |
| 7 | 🇯🇵 JP | 860 |
| 8 | 🇨🇴 CO | 845 |
| 9 | 🇮🇹 IT | 776 |
| 10 | 🇨🇦 CA | 737 |
| 11 | 🇬🇧 GB | 648 |
| 12 | 🇫🇷 FR | 607 |
| 13 | 🇲🇽 MX | 570 |
| 14 | 🇬🇷 GR | 457 |
| 15 | 🇨🇭 CH | 443 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 369 |
| 18 | 🇿🇦 ZA | 350 |
| 19 | 🇳🇴 NO | 338 |
| 20 | 🇬🇹 GT | 321 |
| 21 | 🇵🇭 PH | 305 |
| 22 | 🇹🇷 TR | 303 |
| 23 | 🇰🇷 KR | 291 |
| 24 | 🇵🇱 PL | 237 |
| 25 | 🇹🇭 TH | 232 |
| 26 | 🇲🇦 MA | 204 |
| 27 | 🇧🇸 BS | 183 |
| 28 | 🇮🇩 ID | 177 |
| 29 | 🇲🇪 ME | 170 |
| 30 | 🇲🇴 MO | 166 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 394 |
| 2 | El Dorado International Airport |  | CO | 316 |
| 3 | Denver International Airport |  | US | 303 |
| 4 | Indira Gandhi International Airport |  | IN | 302 |
| 5 | Tokyo International Airport |  | JP | 299 |
| 6 | La Aurora Airport |  | GT | 225 |
| 7 | Harry Reid International Airport |  | US | 219 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 215 |
| 9 | Frankfurt am Main International Airport |  | DE | 212 |
| 10 | Zurich Airport |  | CH | 202 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 179 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 13 | Guaymaral Airport |  | CO | 175 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 169 |
| 15 | Macau International Airport |  | MO | 166 |
| 16 | Bengaluru International Airport |  | IN | 161 |
| 17 | Chicago O'Hare International Airport |  | US | 160 |
| 18 | Madrid Barajas International Airport |  | ES | 154 |
| 19 | Charlotte/Douglas International Airport |  | US | 153 |
| 20 | Congonhas Airport |  | BR | 152 |
| 21 | Tenerife Norte Airport |  | ES | 149 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 147 |
| 23 | Ninoy Aquino International Airport |  | PH | 140 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 136 |
| 25 | Salt Lake City International Airport |  | US | 133 |
| 26 | Reno/Tahoe International Airport |  | US | 131 |
| 27 | Kuala Lumpur International Airport |  | MY | 131 |
| 28 | Malpensa International Airport |  | IT | 130 |
| 29 | Daniel K Inouye International Airport |  | US | 128 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 126 |
| 31 | Vitoria/Foronda Airport |  | ES | 124 |
| 32 | Charles de Gaulle International Airport |  | FR | 123 |
| 33 | Barcelona International Airport |  | ES | 119 |
| 34 | George Bush Intcntl/Houston Airport |  | US | 115 |
| 35 | Pune Airport |  | IN | 114 |
| 36 | Miami International Airport |  | US | 111 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 110 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 109 |
| 39 | Austin-Bergstrom International Airport |  | US | 104 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 104 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 76 | 14m | 114 km | 149.1 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 67 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 50 | 1h 45m | 1,156 km | 997.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 49 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 45 | 26m | 152 km | 117.6 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 44 | 22m | 99 km | 75.4 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 42 | 16m | 206 km | 149.3 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 39 | 28m | 275 km | 184.8 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 14 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 36 | 52m | 556 km | 345.1 t |
| 16 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 35 | 1h 54m | 1,304 km | 787.4 t |
| 17 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 32 | 1h 43m | 1,423 km | 785.3 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 30 | 58m | 723 km | 374.0 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 29 | 13m | 99 km | 49.7 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 25 | 1h 24m | 961 km | 414.4 t |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 24 | 52m | 493 km | 204.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UPS22 | UPS | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-04 08:22 UTC | 2026-04-04 19:43 UTC | 11h 21m |
| CGEKA | CGE | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-04-04 19:02 UTC | 2026-04-04 19:43 UTC | 40m |
| N4841Y |  | Kelly Air Park (CO15) | Kelly Air Park (CO15) | 2026-04-04 19:29 UTC | 2026-04-04 19:41 UTC | 12m |
| AFL1843 | AFL | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-04-04 09:22 UTC | 2026-04-04 19:40 UTC | 10h 17m |
| N114RG |  | Rocky Mountain Metro Airport (KBJC) | Northern Colorado Regional Airport (KFNL) | 2026-04-04 19:20 UTC | 2026-04-04 19:38 UTC | 17m |
| N6294R |  | Sunbury Airport (K71N) | Northumberland County Airport (KN79) | 2026-04-04 19:32 UTC | 2026-04-04 19:33 UTC | 0m |
| N545GC |  | Lompoc Airport (KLPC) | Lompoc Airport (KLPC) | 2026-04-04 18:49 UTC | 2026-04-04 19:28 UTC | 39m |
| AAE127 | AAE | Henri Coanda International Airport (LROP) | Zhuhai Airport (ZGSD) | 2026-04-04 10:10 UTC | 2026-04-04 19:27 UTC | 9h 17m |
| PERRIS5 | PER | Perris Valley Airport (KL65) | Perris Valley Airport (KL65) | 2026-04-04 19:08 UTC | 2026-04-04 19:26 UTC | 17m |
| N407SL |  | Tanner Field (CO27) | Tanner Field (CO27) | 2026-04-04 19:15 UTC | 2026-04-04 19:25 UTC | 10m |
| LXJ423 | LXJ | Mc Clellan-Palomar Airport (KCRQ) | Henderson Executive Airport (KHND) | 2026-04-04 18:38 UTC | 2026-04-04 19:20 UTC | 42m |
| TGARO | TGA | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-04-04 18:38 UTC | 2026-04-04 19:16 UTC | 37m |
| N999VB |  | Iowa City Municipal Airport (KIOW) | Olney-Noble Airport (KOLY) | 2026-04-04 18:16 UTC | 2026-04-04 19:15 UTC | 58m |
| N48ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-04-04 18:09 UTC | 2026-04-04 19:12 UTC | 1h 2m |
| N204EH |  | Zephyrhills Municipal Airport (KZPH) | Zephyrhills Municipal Airport (KZPH) | 2026-04-04 17:45 UTC | 2026-04-04 19:10 UTC | 1h 25m |
| N329HP |  | Deck Airport (K9D4) | Deck Airport (K9D4) | 2026-04-04 19:05 UTC | 2026-04-04 19:09 UTC | 4m |
| CAO8420 | CAO | Los Angeles International Airport (KLAX) | Sharypovo Airport (UNKO) | 2026-04-03 21:09 UTC | 2026-04-04 19:07 UTC | 21h 57m |
| N61718 |  | La Porte Municipal Airport (KT41) | La Porte Municipal Airport (KT41) | 2026-04-04 18:54 UTC | 2026-04-04 19:05 UTC | 10m |
| SCU19 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-04-04 18:50 UTC | 2026-04-04 19:04 UTC | 13m |
| LXJ356 | LXJ | Bremerton Ntl Airport (KPWT) | Sierraville Dearwater Airport (KO79) | 2026-04-04 17:46 UTC | 2026-04-04 19:03 UTC | 1h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
