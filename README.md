# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_22:04:01_UTC-green)

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

**Latest saved flight:** 2026-04-04 22:04:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 22:04:01 UTC

- **16,967** saved flights
- **8,920** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **16,967** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **212,104.7 tonnes** estimated CO2 emissions
- **12,295,924 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 750 |
| 2 | Ryanair | 686 |
| 3 | IndiGo | 481 |
| 4 | EJA | 323 |
| 5 | American Airlines | 313 |
| 6 | Southwest Airlines | 241 |
| 7 | Lufthansa | 238 |
| 8 | ENY | 228 |
| 9 | Vueling | 189 |
| 10 | LATAM Airlines | 183 |
| 11 | AXM | 161 |
| 12 | LXJ | 146 |
| 13 | Delta Air Lines | 144 |
| 14 | All Nippon Airways | 141 |
| 15 | QLK | 137 |
| 16 | AZU | 129 |
| 17 | VIV | 127 |
| 18 | Swiss International | 124 |
| 19 | United Airlines | 116 |
| 20 | Alaska Airlines | 115 |
| 21 | EJU | 109 |
| 22 | Avianca | 108 |
| 23 | easyJet | 107 |
| 24 | Japan Airlines | 107 |
| 25 | AEE | 105 |
| 26 | AXB | 105 |
| 27 | EDV | 105 |
| 28 | WIF | 102 |
| 29 | BRC | 101 |
| 30 | GLO | 97 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13587 |
| 2 | 🇮🇳 IN | 1467 |
| 3 | 🇪🇸 ES | 1398 |
| 4 | 🇦🇺 AU | 1213 |
| 5 | 🇧🇷 BR | 988 |
| 6 | 🇨🇴 CO | 873 |
| 7 | 🇩🇪 DE | 872 |
| 8 | 🇯🇵 JP | 862 |
| 9 | 🇮🇹 IT | 786 |
| 10 | 🇨🇦 CA | 761 |
| 11 | 🇬🇧 GB | 660 |
| 12 | 🇫🇷 FR | 609 |
| 13 | 🇲🇽 MX | 582 |
| 14 | 🇬🇷 GR | 459 |
| 15 | 🇨🇭 CH | 444 |
| 16 | 🇳🇿 NZ | 381 |
| 17 | 🇲🇾 MY | 369 |
| 18 | 🇿🇦 ZA | 350 |
| 19 | 🇳🇴 NO | 341 |
| 20 | 🇬🇹 GT | 329 |
| 21 | 🇹🇷 TR | 308 |
| 22 | 🇵🇭 PH | 307 |
| 23 | 🇰🇷 KR | 293 |
| 24 | 🇵🇱 PL | 239 |
| 25 | 🇹🇭 TH | 232 |
| 26 | 🇲🇦 MA | 206 |
| 27 | 🇧🇸 BS | 190 |
| 28 | 🇮🇩 ID | 178 |
| 29 | 🇲🇪 ME | 173 |
| 30 | 🇲🇴 MO | 171 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 410 |
| 2 | El Dorado International Airport |  | CO | 327 |
| 3 | Denver International Airport |  | US | 317 |
| 4 | Indira Gandhi International Airport |  | IN | 304 |
| 5 | Tokyo International Airport |  | JP | 299 |
| 6 | La Aurora Airport |  | GT | 232 |
| 7 | Harry Reid International Airport |  | US | 225 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 215 |
| 9 | Frankfurt am Main International Airport |  | DE | 212 |
| 10 | Zurich Airport |  | CH | 203 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 183 |
| 12 | Guaymaral Airport |  | CO | 180 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 178 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 15 | Macau International Airport |  | MO | 171 |
| 16 | Chicago O'Hare International Airport |  | US | 167 |
| 17 | Bengaluru International Airport |  | IN | 162 |
| 18 | Charlotte/Douglas International Airport |  | US | 158 |
| 19 | Madrid Barajas International Airport |  | ES | 156 |
| 20 | Congonhas Airport |  | BR | 154 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 150 |
| 22 | Tenerife Norte Airport |  | ES | 150 |
| 23 | Ninoy Aquino International Airport |  | PH | 141 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 136 |
| 25 | Salt Lake City International Airport |  | US | 136 |
| 26 | Daniel K Inouye International Airport |  | US | 134 |
| 27 | Malpensa International Airport |  | IT | 133 |
| 28 | Reno/Tahoe International Airport |  | US | 133 |
| 29 | Kuala Lumpur International Airport |  | MY | 131 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 128 |
| 31 | Vitoria/Foronda Airport |  | ES | 125 |
| 32 | Charles de Gaulle International Airport |  | FR | 124 |
| 33 | Miami International Airport |  | US | 121 |
| 34 | Barcelona International Airport |  | ES | 119 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 116 |
| 36 | Pune Airport |  | IN | 116 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 110 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 110 |
| 39 | Seattle-Tacoma International Airport |  | US | 108 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 107 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 77 | 14m | 114 km | 151.0 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 68 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 51 | 1h 45m | 1,156 km | 1,017.4 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 51 | 27m | 152 km | 133.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 49 | 31m | - | - |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 44 | 22m | 99 km | 75.4 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 43 | 16m | 206 km | 152.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 40 | 28m | 275 km | 189.5 t |
| 13 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 37 | 52m | 556 km | 354.7 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 15 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 35 | 30m | 369 km | 222.8 t |
| 17 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 35 | 1h 54m | 1,304 km | 787.4 t |
| 18 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 32 | 1h 43m | 1,423 km | 785.3 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 31 | 58m | 723 km | 386.5 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 30 | 13m | 99 km | 51.4 t |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 26 | 1h 23m | 961 km | 431.0 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 24 | 12m | 15 km | 6.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFDYL | CFD | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-04-04 21:42 UTC | 2026-04-04 22:04 UTC | 21m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-04 21:45 UTC | 2026-04-04 22:01 UTC | 16m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-04 19:14 UTC | 2026-04-04 22:00 UTC | 2h 46m |
| UAE9860 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-04-04 15:37 UTC | 2026-04-04 21:53 UTC | 6h 16m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-04-04 10:43 UTC | 2026-04-04 21:52 UTC | 11h 9m |
| BNO91J | BNO | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-04-04 21:11 UTC | 2026-04-04 21:52 UTC | 40m |
| FFP90 | FFP | Ted Stevens Anchorage International Airport (PANC) | Fairbanks International Airport (PAFA) | 2026-04-04 20:41 UTC | 2026-04-04 21:51 UTC | 1h 9m |
| N6605P |  | Portland-Hillsboro Airport (KHIO) | Roppair Airport (OR22) | 2026-04-04 21:02 UTC | 2026-04-04 21:50 UTC | 48m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-04 17:30 UTC | 2026-04-04 21:48 UTC | 4h 17m |
| CPA953 | Cathay Pacific | Guangzhou Baiyun International Airport (ZGGG) | Macau International Airport (VMMC) | 2026-04-04 21:32 UTC | 2026-04-04 21:46 UTC | 14m |
| TGRWC | TGR | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-04 21:21 UTC | 2026-04-04 21:45 UTC | 23m |
| N74SW |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-04-04 20:42 UTC | 2026-04-04 21:42 UTC | 1h 0m |
| EJA282 | EJA | Charleston Afb/International Airport (KCHS) | Tampa International Airport (KTPA) | 2026-04-04 20:40 UTC | 2026-04-04 21:37 UTC | 56m |
| N614MB |  | Carson City Airport (KCXP) | Desert Creek Airport (NV97) | 2026-04-04 21:18 UTC | 2026-04-04 21:36 UTC | 17m |
| N1287E |  | Santa Barbara Municipal Airport (KSBA) | Riverside Airport (KRAL) | 2026-04-04 20:08 UTC | 2026-04-04 21:36 UTC | 1h 27m |
| N734LQ |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-04-04 20:56 UTC | 2026-04-04 21:35 UTC | 38m |
| N258EA |  | Glendale Regional Airport (KGEU) | Western Sky Airpark (0AZ2) | 2026-04-04 20:22 UTC | 2026-04-04 21:32 UTC | 1h 10m |
| N884GT |  | Billings Logan International Airport (KBIL) | Billings Logan International Airport (KBIL) | 2026-04-04 21:26 UTC | 2026-04-04 21:27 UTC | 0m |
| ENY3668 | ENY | Dallas-Fort Worth International Airport (KDFW) | Shady Bend Airport (9FL5) | 2026-04-04 19:26 UTC | 2026-04-04 21:25 UTC | 1h 58m |
| N7089R |  | Pittsburgh/Butler Regional Airport (KBTP) | Pittsburgh/Butler Regional Airport (KBTP) | 2026-04-04 21:03 UTC | 2026-04-04 21:25 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
