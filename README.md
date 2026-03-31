# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_11:49:14_UTC-green)

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

**Latest saved flight:** 2026-03-31 11:49:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 11:49:14 UTC

- **6,433** saved flights
- **4,211** unique routes
- **105** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **6,433** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **81,997.2 tonnes** estimated CO2 emissions
- **4,753,460 km** total distance flown
- **877 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 312 |
| 2 | Ryanair | 238 |
| 3 | IndiGo | 173 |
| 4 | EJA | 130 |
| 5 | American Airlines | 122 |
| 6 | Lufthansa | 101 |
| 7 | Southwest Airlines | 101 |
| 8 | ENY | 93 |
| 9 | AXM | 75 |
| 10 | LATAM Airlines | 68 |
| 11 | Vueling | 65 |
| 12 | All Nippon Airways | 57 |
| 13 | LXJ | 57 |
| 14 | QLK | 56 |
| 15 | Delta Air Lines | 55 |
| 16 | Swiss International | 50 |
| 17 | WIF | 49 |
| 18 | Cathay Pacific | 47 |
| 19 | Japan Airlines | 47 |
| 20 | United Airlines | 47 |
| 21 | VIV | 46 |
| 22 | AXB | 44 |
| 23 | AZU | 43 |
| 24 | Alaska Airlines | 40 |
| 25 | EDV | 39 |
| 26 | Avianca | 37 |
| 27 | EJU | 35 |
| 28 | VOE | 35 |
| 29 | easyJet | 34 |
| 30 | MXY | 33 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 5384 |
| 2 | 🇮🇳 IN | 524 |
| 3 | 🇦🇺 AU | 504 |
| 4 | 🇪🇸 ES | 491 |
| 5 | 🇯🇵 JP | 335 |
| 6 | 🇧🇷 BR | 317 |
| 7 | 🇩🇪 DE | 313 |
| 8 | 🇨🇴 CO | 293 |
| 9 | 🇮🇹 IT | 288 |
| 10 | 🇨🇦 CA | 273 |
| 11 | 🇲🇽 MX | 228 |
| 12 | 🇬🇧 GB | 216 |
| 13 | 🇫🇷 FR | 194 |
| 14 | 🇲🇾 MY | 169 |
| 15 | 🇳🇴 NO | 167 |
| 16 | 🇨🇭 CH | 152 |
| 17 | 🇬🇷 GR | 149 |
| 18 | 🇿🇦 ZA | 149 |
| 19 | 🇬🇹 GT | 132 |
| 20 | 🇵🇭 PH | 131 |
| 21 | 🇳🇿 NZ | 122 |
| 22 | 🇹🇷 TR | 103 |
| 23 | 🇹🇭 TH | 92 |
| 24 | 🇮🇩 ID | 85 |
| 25 | 🇲🇴 MO | 81 |
| 26 | 🇲🇦 MA | 78 |
| 27 | 🇰🇷 KR | 77 |
| 28 | 🇵🇱 PL | 77 |
| 29 | 🇲🇪 ME | 62 |
| 30 | 🇧🇸 BS | 60 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 163 |
| 2 | Denver International Airport |  | US | 122 |
| 3 | Tokyo International Airport |  | JP | 120 |
| 4 | Indira Gandhi International Airport |  | IN | 119 |
| 5 | El Dorado International Airport |  | CO | 109 |
| 6 | Frankfurt am Main International Airport |  | DE | 101 |
| 7 | La Aurora Airport |  | GT | 90 |
| 8 | Harry Reid International Airport |  | US | 82 |
| 9 | Macau International Airport |  | MO | 81 |
| 10 | Zurich Airport |  | CH | 80 |
| 11 | Chicago O'Hare International Airport |  | US | 76 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 75 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 75 |
| 14 | Eleftherios Venizelos International Airport |  | GR | 70 |
| 15 | Tenerife Norte Airport |  | ES | 68 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 66 |
| 17 | Guaymaral Airport |  | CO | 65 |
| 18 | Kuala Lumpur International Airport |  | MY | 61 |
| 19 | Madrid Barajas International Airport |  | ES | 60 |
| 20 | Reno/Tahoe International Airport |  | US | 59 |
| 21 | Ninoy Aquino International Airport |  | PH | 59 |
| 22 | Bengaluru International Airport |  | IN | 58 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 53 |
| 24 | Charlotte/Douglas International Airport |  | US | 50 |
| 25 | Charles de Gaulle International Airport |  | FR | 50 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 50 |
| 27 | Malpensa International Airport |  | IT | 49 |
| 28 | Salt Lake City International Airport |  | US | 49 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 48 |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 48 |
| 31 | Vitoria/Foronda Airport |  | ES | 47 |
| 32 | Miami International Airport |  | US | 46 |
| 33 | Congonhas Airport |  | BR | 45 |
| 34 | O. R. Tambo International Airport |  | ZA | 45 |
| 35 | Seattle-Tacoma International Airport |  | US | 44 |
| 36 | Daniel K Inouye International Airport |  | US | 43 |
| 37 | Amsterdam Airport Schiphol |  | NL | 43 |
| 38 | Pune Airport |  | IN | 43 |
| 39 | Centennial Airport |  | US | 43 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 42 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 28 | 1h 6m | 706 km | 340.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 28 | 14m | 114 km | 54.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 27 | 24m | 225 km | 104.7 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 25 | 27m | - | - |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 24 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 21 | 26m | 152 km | 54.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 19 | 29m | 304 km | 99.6 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 19 | 20m | 165 km | 54.0 t |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 19 | 24m | 99 km | 32.5 t |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 18 | 1h 48m | 1,156 km | 359.1 t |
| 11 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 18 | 1h 41m | 1,423 km | 441.7 t |
| 12 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 17 | 5m | - | - |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 16 | 15m | 206 km | 56.9 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 16 | 29m | 275 km | 75.8 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 16 | 1h 25m | 910 km | 251.1 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 15 | 1h 10m | 770 km | 199.3 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 15 | 30m | 369 km | 95.5 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 14 | 53m | 546 km | 131.8 t |
| 19 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 14 | 51m | 556 km | 134.2 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 13 | 11m | 127 km | 28.5 t |
| 23 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 13 | 28m | 69 km | 15.5 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 12 | 1h 46m | 1,290 km | 267.0 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 12 | 23m | - | - |
| 27 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 12 | 1h 56m | 1,304 km | 270.0 t |
| 29 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 11 | 1h 2m | 723 km | 137.1 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 11 | 12m | 99 km | 18.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PHSVD | PHS | Eelde Airport (EHGG) | Eelde Airport (EHGG) | 2026-03-31 11:00 UTC | 2026-03-31 11:49 UTC | 48m |
| SCQZ14U | SCQ | Gullknapp Flpl Airport (ENGK) | Stavanger Airport Sola (ENZV) | 2026-03-31 10:22 UTC | 2026-03-31 11:49 UTC | 1h 27m |
| N3171E |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-03-31 11:13 UTC | 2026-03-31 11:41 UTC | 27m |
| N722HG |  | Pompano Beach Airpark (KPMP) | Duda Airstrip (FA69) | 2026-03-31 10:38 UTC | 2026-03-31 11:21 UTC | 43m |
| PHZLD | PHZ | Eindhoven Airport (EHEH) | Budel Airport (EHBD) | 2026-03-31 10:39 UTC | 2026-03-31 11:17 UTC | 38m |
| INR50220 | INR | Reus Air Base (LERS) | Reus Air Base (LERS) | 2026-03-31 10:49 UTC | 2026-03-31 11:01 UTC | 11m |
| ETD914 | Etihad Airways | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-03-30 18:57 UTC | 2026-03-31 11:00 UTC | 16h 3m |
| BBC437 | BBC | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-03-31 10:27 UTC | 2026-03-31 10:57 UTC | 29m |
| VLG6XK | Vueling | Barcelona International Airport (LEBL) | Federico Garcia Lorca Airport (LEGR) | 2026-03-31 10:00 UTC | 2026-03-31 10:54 UTC | 53m |
| EDC918R | EDC | Oxford (Kidlington) Airport (EGTK) | Guernsey Airport (EGJB) | 2026-03-31 10:19 UTC | 2026-03-31 10:53 UTC | 34m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-03-31 10:40 UTC | 2026-03-31 10:52 UTC | 12m |
| WIF808 | WIF | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 2026-03-31 10:44 UTC | 2026-03-31 10:49 UTC | 5m |
| RYR6AQ | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Tortoli' / Arbatax Airport (LIET) | 2026-03-31 09:59 UTC | 2026-03-31 10:48 UTC | 49m |
| AEE6PX | AEE | Malpensa International Airport (LIMC) | Eleftherios Venizelos International Airport (LGAV) | 2026-03-31 08:31 UTC | 2026-03-31 10:44 UTC | 2h 12m |
| EVE7310 | EVE | Almeria International Airport (LEAM) | La Morgal Airport (LEMR) | 2026-03-31 09:32 UTC | 2026-03-31 10:43 UTC | 1h 11m |
| EZY94MC | easyJet | London Gatwick Airport (EGKK) | Chania International Airport (LGSA) | 2026-03-31 07:24 UTC | 2026-03-31 10:42 UTC | 3h 18m |
| SWIFT322 | SWI | Moi Air Base (HKRE) | Nairobi Wilson Airport (HKNW) | 2026-03-31 10:34 UTC | 2026-03-31 10:42 UTC | 7m |
| RYR4164 | Ryanair | Stockholm-Arlanda Airport (ESSA) | Visoko Sport Airfield (LQVI) | 2026-03-31 08:29 UTC | 2026-03-31 10:42 UTC | 2h 13m |
| ANE1121 | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-03-31 10:04 UTC | 2026-03-31 10:41 UTC | 37m |
| SFJ15 | SFJ | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-03-31 09:33 UTC | 2026-03-31 10:40 UTC | 1h 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
