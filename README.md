# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_21:10:26_UTC-green)

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

**Latest saved flight:** 2026-04-03 21:10:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 21:10:26 UTC

- **14,436** saved flights
- **7,946** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **14,436** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **178,598.4 tonnes** estimated CO2 emissions
- **10,353,528 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 631 |
| 2 | Ryanair | 554 |
| 3 | IndiGo | 403 |
| 4 | EJA | 289 |
| 5 | American Airlines | 270 |
| 6 | Lufthansa | 210 |
| 7 | Southwest Airlines | 210 |
| 8 | ENY | 189 |
| 9 | Vueling | 156 |
| 10 | LATAM Airlines | 153 |
| 11 | AXM | 142 |
| 12 | LXJ | 129 |
| 13 | All Nippon Airways | 123 |
| 14 | QLK | 123 |
| 15 | Delta Air Lines | 116 |
| 16 | AZU | 114 |
| 17 | Swiss International | 111 |
| 18 | VIV | 104 |
| 19 | WIF | 97 |
| 20 | Alaska Airlines | 94 |
| 21 | United Airlines | 93 |
| 22 | easyJet | 90 |
| 23 | AXB | 89 |
| 24 | Japan Airlines | 89 |
| 25 | AEE | 87 |
| 26 | EDV | 87 |
| 27 | EJU | 87 |
| 28 | BRC | 85 |
| 29 | Cathay Pacific | 85 |
| 30 | Avianca | 84 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 11661 |
| 2 | 🇮🇳 IN | 1228 |
| 3 | 🇪🇸 ES | 1104 |
| 4 | 🇦🇺 AU | 1084 |
| 5 | 🇧🇷 BR | 850 |
| 6 | 🇩🇪 DE | 757 |
| 7 | 🇯🇵 JP | 727 |
| 8 | 🇨🇴 CO | 717 |
| 9 | 🇨🇦 CA | 664 |
| 10 | 🇮🇹 IT | 625 |
| 11 | 🇬🇧 GB | 556 |
| 12 | 🇲🇽 MX | 502 |
| 13 | 🇫🇷 FR | 502 |
| 14 | 🇬🇷 GR | 388 |
| 15 | 🇨🇭 CH | 374 |
| 16 | 🇳🇿 NZ | 337 |
| 17 | 🇲🇾 MY | 319 |
| 18 | 🇳🇴 NO | 313 |
| 19 | 🇿🇦 ZA | 299 |
| 20 | 🇹🇷 TR | 265 |
| 21 | 🇬🇹 GT | 265 |
| 22 | 🇵🇭 PH | 265 |
| 23 | 🇰🇷 KR | 237 |
| 24 | 🇵🇱 PL | 200 |
| 25 | 🇹🇭 TH | 186 |
| 26 | 🇲🇦 MA | 174 |
| 27 | 🇮🇩 ID | 166 |
| 28 | 🇲🇴 MO | 157 |
| 29 | 🇧🇸 BS | 157 |
| 30 | 🇲🇪 ME | 149 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 357 |
| 2 | El Dorado International Airport |  | CO | 264 |
| 3 | Indira Gandhi International Airport |  | IN | 261 |
| 4 | Denver International Airport |  | US | 258 |
| 5 | Tokyo International Airport |  | JP | 253 |
| 6 | Frankfurt am Main International Airport |  | DE | 196 |
| 7 | Harry Reid International Airport |  | US | 194 |
| 8 | La Aurora Airport |  | GT | 185 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 180 |
| 10 | Zurich Airport |  | CH | 175 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 160 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 159 |
| 13 | Macau International Airport |  | MO | 157 |
| 14 | Guaymaral Airport |  | CO | 157 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 141 |
| 16 | Bengaluru International Airport |  | IN | 140 |
| 17 | Chicago O'Hare International Airport |  | US | 139 |
| 18 | Charlotte/Douglas International Airport |  | US | 133 |
| 19 | Congonhas Airport |  | BR | 132 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 128 |
| 21 | Madrid Barajas International Airport |  | ES | 125 |
| 22 | Ninoy Aquino International Airport |  | PH | 121 |
| 23 | Kuala Lumpur International Airport |  | MY | 117 |
| 24 | Tenerife Norte Airport |  | ES | 114 |
| 25 | Salt Lake City International Airport |  | US | 112 |
| 26 | Reno/Tahoe International Airport |  | US | 111 |
| 27 | Vitoria/Foronda Airport |  | ES | 111 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 110 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 109 |
| 30 | Daniel K Inouye International Airport |  | US | 105 |
| 31 | Charles de Gaulle International Airport |  | FR | 104 |
| 32 | Malpensa International Airport |  | IT | 102 |
| 33 | George Bush Intcntl/Houston Airport |  | US | 99 |
| 34 | Pune Airport |  | IN | 98 |
| 35 | Austin-Bergstrom International Airport |  | US | 97 |
| 36 | Barcelona International Airport |  | ES | 96 |
| 37 | Miami International Airport |  | US | 93 |
| 38 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 93 |
| 39 | Seattle-Tacoma International Airport |  | US | 92 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 90 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 67 | 14m | 114 km | 131.4 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 61 | 1h 7m | 706 km | 742.7 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 51 | 24m | 225 km | 197.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 43 | 1h 46m | 1,156 km | 857.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 37 | 22m | 99 km | 63.4 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 36 | 1h 26m | 910 km | 564.9 t |
| 10 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 35 | 27m | 152 km | 91.5 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 34 | 15m | 206 km | 120.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 34 | 28m | 275 km | 161.1 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 32 | 53m | 556 km | 306.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 30 | 30m | 369 km | 191.0 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 30 | 1h 55m | 1,304 km | 674.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 27 | 1h 10m | 770 km | 358.7 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 26 | 59m | 723 km | 324.1 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 24 | 23m | 252 km | 104.2 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 23 | 13m | 99 km | 39.4 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 21 | 16m | 183 km | 66.2 t |
| 29 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 20 | 1h 15m | 924 km | 319.0 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 20 | 12m | 15 km | 5.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N450CB |  | Somerset Airport (KSMQ) | Lehigh Valley International Airport (KABE) | 2026-04-03 20:46 UTC | 2026-04-03 21:10 UTC | 24m |
| SHADY05 | SHA | Porterville Municipal Airport (KPTV) | Porterville Municipal Airport (KPTV) | 2026-04-03 20:43 UTC | 2026-04-03 21:04 UTC | 20m |
| N931PA |  | Falcon Field (KFFZ) | Phoenix Deer Valley Airport (KDVT) | 2026-04-03 20:04 UTC | 2026-04-03 20:59 UTC | 54m |
| N9303N |  | Denton Enterprise Airport (KDTO) | Addington Field (4TX8) | 2026-04-03 19:59 UTC | 2026-04-03 20:56 UTC | 56m |
| N980S |  | Scottsdale Airport (KSDL) | Cascade Airport (KU70) | 2026-04-03 19:06 UTC | 2026-04-03 20:52 UTC | 1h 46m |
| CXK161 | CXK | Morristown Municipal Airport (KMMU) | Morristown Municipal Airport (KMMU) | 2026-04-03 20:33 UTC | 2026-04-03 20:50 UTC | 17m |
| N5318M |  | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-04-03 20:06 UTC | 2026-04-03 20:46 UTC | 39m |
| N63017 |  | XA90 (XA90) | Commerce Municipal Airport (K2F7) | 2026-04-03 19:50 UTC | 2026-04-03 20:44 UTC | 54m |
| N111BP |  | Schaller Airport (27OH) | Auburn University Regional Airport (KAUO) | 2026-04-03 19:17 UTC | 2026-04-03 20:44 UTC | 1h 27m |
| NGH365 | NGH | Davenport Municipal Airport (KDVN) | Spencer Municipal Airport (KSPW) | 2026-04-03 20:07 UTC | 2026-04-03 20:44 UTC | 36m |
| N724TT |  | Santa Monica Municipal Airport (KSMO) | Santa Monica Municipal Airport (KSMO) | 2026-04-03 20:13 UTC | 2026-04-03 20:43 UTC | 30m |
| N539WA |  | Dallas Love Field (KDAL) | Cisco Municipal Airport (K3F2) | 2026-04-03 20:18 UTC | 2026-04-03 20:42 UTC | 24m |
| EDL5 | EDL | Munich International Airport (EDDM) | Altenstadt Army Airfield (ETHA) | 2026-04-03 20:06 UTC | 2026-04-03 20:42 UTC | 35m |
| UAE1CL | Emirates | London Gatwick Airport (EGKK) | Buraimi Airport (OOBR) | 2026-04-03 14:04 UTC | 2026-04-03 20:41 UTC | 6h 36m |
| N952JA |  | John Wayne/Orange County Airport (KSNA) | Hesperia Airport (KL26) | 2026-04-03 19:58 UTC | 2026-04-03 20:41 UTC | 42m |
| N111WM |  | San Marcos Regional Airport (KHYI) | Mid-Way Regional Airport (KJWY) | 2026-04-03 19:28 UTC | 2026-04-03 20:40 UTC | 1h 12m |
| N98485 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-03 20:28 UTC | 2026-04-03 20:40 UTC | 11m |
| N54HA |  | University Of Oklahoma Westheimer Airport (KOUN) | Aitkin Municipal/Steve Kurtz Field (KAIT) | 2026-04-03 19:08 UTC | 2026-04-03 20:38 UTC | 1h 30m |
| N302VM |  | Montgomery County Airpark (KGAI) | Carroll County Regional/Jack B Poage Field (KDMW) | 2026-04-03 19:39 UTC | 2026-04-03 20:36 UTC | 56m |
| N810W |  | North Exuma Airport (85FA) | 46FD (46FD) | 2026-04-03 20:14 UTC | 2026-04-03 20:34 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
