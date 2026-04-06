# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_13:05:51_UTC-green)

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

**Latest saved flight:** 2026-04-06 13:05:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 13:05:51 UTC

- **19,855** saved flights
- **9,944** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **19,855** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **250,526.6 tonnes** estimated CO2 emissions
- **14,523,280 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 855 |
| 2 | Ryanair | 825 |
| 3 | IndiGo | 569 |
| 4 | American Airlines | 379 |
| 5 | EJA | 365 |
| 6 | Southwest Airlines | 282 |
| 7 | ENY | 267 |
| 8 | Lufthansa | 263 |
| 9 | Vueling | 215 |
| 10 | LATAM Airlines | 211 |
| 11 | AXM | 197 |
| 12 | Delta Air Lines | 177 |
| 13 | All Nippon Airways | 176 |
| 14 | LXJ | 171 |
| 15 | QLK | 164 |
| 16 | AZU | 151 |
| 17 | Swiss International | 149 |
| 18 | VIV | 149 |
| 19 | easyJet | 135 |
| 20 | Japan Airlines | 134 |
| 21 | United Airlines | 134 |
| 22 | Alaska Airlines | 132 |
| 23 | Avianca | 131 |
| 24 | EJU | 128 |
| 25 | AEE | 125 |
| 26 | WIF | 119 |
| 27 | EDV | 118 |
| 28 | AXB | 115 |
| 29 | Air France | 110 |
| 30 | Cathay Pacific | 105 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 15397 |
| 2 | 🇮🇳 IN | 1735 |
| 3 | 🇪🇸 ES | 1604 |
| 4 | 🇦🇺 AU | 1407 |
| 5 | 🇧🇷 BR | 1140 |
| 6 | 🇯🇵 JP | 1090 |
| 7 | 🇨🇴 CO | 1078 |
| 8 | 🇩🇪 DE | 1000 |
| 9 | 🇮🇹 IT | 976 |
| 10 | 🇨🇦 CA | 861 |
| 11 | 🇬🇧 GB | 782 |
| 12 | 🇫🇷 FR | 735 |
| 13 | 🇲🇽 MX | 679 |
| 14 | 🇬🇷 GR | 567 |
| 15 | 🇨🇭 CH | 537 |
| 16 | 🇲🇾 MY | 460 |
| 17 | 🇬🇹 GT | 456 |
| 18 | 🇿🇦 ZA | 451 |
| 19 | 🇳🇿 NZ | 416 |
| 20 | 🇳🇴 NO | 413 |
| 21 | 🇹🇷 TR | 390 |
| 22 | 🇵🇭 PH | 380 |
| 23 | 🇰🇷 KR | 351 |
| 24 | 🇹🇭 TH | 304 |
| 25 | 🇵🇱 PL | 288 |
| 26 | 🇲🇦 MA | 247 |
| 27 | 🇧🇸 BS | 216 |
| 28 | 🇮🇩 ID | 214 |
| 29 | 🇲🇪 ME | 210 |
| 30 | 🇲🇴 MO | 199 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 483 |
| 2 | El Dorado International Airport |  | CO | 413 |
| 3 | Tokyo International Airport |  | JP | 377 |
| 4 | Denver International Airport |  | US | 363 |
| 5 | Indira Gandhi International Airport |  | IN | 361 |
| 6 | La Aurora Airport |  | GT | 312 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 267 |
| 8 | Harry Reid International Airport |  | US | 259 |
| 9 | Zurich Airport |  | CH | 243 |
| 10 | Frankfurt am Main International Airport |  | DE | 233 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 216 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 211 |
| 13 | Chicago O'Hare International Airport |  | US | 210 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 204 |
| 15 | Guaymaral Airport |  | CO | 204 |
| 16 | Macau International Airport |  | MO | 199 |
| 17 | Bengaluru International Airport |  | IN | 193 |
| 18 | Charlotte/Douglas International Airport |  | US | 191 |
| 19 | Madrid Barajas International Airport |  | ES | 187 |
| 20 | Tenerife Norte Airport |  | ES | 180 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 179 |
| 22 | Ninoy Aquino International Airport |  | PH | 172 |
| 23 | Congonhas Airport |  | BR | 169 |
| 24 | Kuala Lumpur International Airport |  | MY | 159 |
| 25 | Salt Lake City International Airport |  | US | 157 |
| 26 | Reno/Tahoe International Airport |  | US | 156 |
| 27 | Daniel K Inouye International Airport |  | US | 154 |
| 28 | Malpensa International Airport |  | IT | 151 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 150 |
| 30 | Charles de Gaulle International Airport |  | FR | 149 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 146 |
| 32 | Vitoria/Foronda Airport |  | ES | 145 |
| 33 | Miami International Airport |  | US | 140 |
| 34 | O. R. Tambo International Airport |  | ZA | 140 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 139 |
| 36 | Pune Airport |  | IN | 135 |
| 37 | Barcelona International Airport |  | ES | 133 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 131 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 131 |
| 40 | Seattle-Tacoma International Airport |  | US | 127 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 95 | 1h 8m | 706 km | 1,156.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 89 | 14m | 114 km | 174.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 74 | 24m | 225 km | 287.1 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 74 | 27m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 69 | 28m | 304 km | 361.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 60 | 1h 27m | 910 km | 941.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 57 | 1h 43m | 1,156 km | 1,137.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 56 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 55 | 16m | 206 km | 195.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 46 | 19m | 165 km | 130.8 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 44 | 1h 12m | 770 km | 584.5 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 44 | 1h 53m | 1,304 km | 989.9 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 43 | 23m | 252 km | 186.7 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 42 | 55m | 546 km | 395.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 41 | 30m | 369 km | 261.0 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 38 | 4m | - | - |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 38 | 10m | - | - |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 37 | 13m | 99 km | 63.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 36 | 46m | 452 km | 280.6 t |
| 25 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 36 | 20m | 250 km | 155.5 t |
| 26 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 35 | 58m | 723 km | 436.3 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 31 | 12m | 15 km | 8.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N148LC |  | Concord-Padgett Regional Airport (KJQF) | Southern Wake Regional Airport (K5W5) | 2026-04-06 12:26 UTC | 2026-04-06 13:05 UTC | 39m |
| N410LK |  | Brunswick Golden Isles Airport (KBQK) | Daniel Field (KDNL) | 2026-04-06 12:21 UTC | 2026-04-06 13:00 UTC | 39m |
| TVF47TR | TVF | Vienna International Airport (LOWW) | Paris-Orly Airport (LFPO) | 2026-04-06 11:15 UTC | 2026-04-06 12:54 UTC | 1h 38m |
| HB3266 |  | Locarno Airport (LSZL) | Lodrino Air Base (LSML) | 2026-04-06 11:21 UTC | 2026-04-06 12:48 UTC | 1h 27m |
| COR1 | COR | Tambau Airport (SSET) | Adhemar Ribeiro Airport (SDRD) | 2026-04-06 12:35 UTC | 2026-04-06 12:48 UTC | 12m |
| HBKFI | HBK | Lausanne-la Blecherette Airport (LSGL) | Lausanne-la Blecherette Airport (LSGL) | 2026-04-06 11:47 UTC | 2026-04-06 12:47 UTC | 1h 0m |
| FHRNS | FHR | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-06 12:17 UTC | 2026-04-06 12:45 UTC | 27m |
| CXK407 | CXK | Clark Regional Airport (KJVY) | Clark Regional Airport (KJVY) | 2026-04-06 12:12 UTC | 2026-04-06 12:44 UTC | 31m |
| INI413H | INI | Palma De Mallorca Airport (LEPA) | E. Castellanos-Villacastin Airport (LEEV) | 2026-04-06 11:34 UTC | 2026-04-06 12:39 UTC | 1h 5m |
| GBLUZ | GBL | Old Warden Airfield (EGTH) | Old Warden Airfield (EGTH) | 2026-04-06 12:12 UTC | 2026-04-06 12:35 UTC | 22m |
| N965KW |  | Marco Island Executive Airport (KMKY) | Marco Island Executive Airport (KMKY) | 2026-04-06 12:32 UTC | 2026-04-06 12:34 UTC | 2m |
| HYD102 | HYD | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Rouyn-Noranda Airport (CYUY) | 2026-04-06 11:34 UTC | 2026-04-06 12:24 UTC | 50m |
| MFX7566 | MFX | Tallinn Airport (EETN) | Chek Lap Kok International Airport (VHHH) | 2026-04-05 19:26 UTC | 2026-04-06 12:24 UTC | 16h 57m |
| FHSMB | FHS | Lyon-Bron Airport (LFLY) | Macon-Charnay Airport (LFLM) | 2026-04-06 11:58 UTC | 2026-04-06 12:22 UTC | 24m |
| JANET77 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-04-06 12:10 UTC | 2026-04-06 12:21 UTC | 11m |
| LVCCO | LVC | Jorge Newbery Airpark (SABE) | SUGA (SUGA) | 2026-04-06 11:56 UTC | 2026-04-06 12:17 UTC | 20m |
| NSE8874 | NSE | El Dorado International Airport (SKBO) | Las Brujas Airport (SKCZ) | 2026-04-06 11:12 UTC | 2026-04-06 12:16 UTC | 1h 4m |
| WIF170 | WIF | Bergen Airport Flesland (ENBR) | Bringeland Airport (ENBL) | 2026-04-06 11:55 UTC | 2026-04-06 12:14 UTC | 19m |
| N247FS |  | Teterboro Airport (KTEB) | 32VA (32VA) | 2026-04-06 10:52 UTC | 2026-04-06 12:13 UTC | 1h 21m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-06 11:59 UTC | 2026-04-06 12:11 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
