# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_13:42:24_UTC-green)

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

**Latest saved flight:** 2026-04-04 13:42:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 13:42:24 UTC

- **15,650** saved flights
- **8,388** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **15,650** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **194,539.2 tonnes** estimated CO2 emissions
- **11,277,634 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 672 |
| 2 | Ryanair | 623 |
| 3 | IndiGo | 459 |
| 4 | EJA | 302 |
| 5 | American Airlines | 282 |
| 6 | Southwest Airlines | 226 |
| 7 | Lufthansa | 223 |
| 8 | ENY | 196 |
| 9 | Vueling | 169 |
| 10 | LATAM Airlines | 167 |
| 11 | AXM | 159 |
| 12 | All Nippon Airways | 141 |
| 13 | QLK | 137 |
| 14 | LXJ | 134 |
| 15 | Delta Air Lines | 125 |
| 16 | Swiss International | 121 |
| 17 | AZU | 119 |
| 18 | VIV | 111 |
| 19 | Japan Airlines | 107 |
| 20 | Alaska Airlines | 104 |
| 21 | WIF | 101 |
| 22 | EJU | 99 |
| 23 | AEE | 98 |
| 24 | AXB | 98 |
| 25 | United Airlines | 98 |
| 26 | Avianca | 97 |
| 27 | easyJet | 96 |
| 28 | EDV | 93 |
| 29 | BRC | 88 |
| 30 | Cathay Pacific | 88 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12306 |
| 2 | 🇮🇳 IN | 1399 |
| 3 | 🇪🇸 ES | 1238 |
| 4 | 🇦🇺 AU | 1205 |
| 5 | 🇧🇷 BR | 901 |
| 6 | 🇯🇵 JP | 860 |
| 7 | 🇩🇪 DE | 820 |
| 8 | 🇨🇴 CO | 774 |
| 9 | 🇮🇹 IT | 702 |
| 10 | 🇨🇦 CA | 696 |
| 11 | 🇬🇧 GB | 612 |
| 12 | 🇫🇷 FR | 560 |
| 13 | 🇲🇽 MX | 523 |
| 14 | 🇬🇷 GR | 436 |
| 15 | 🇨🇭 CH | 421 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 367 |
| 18 | 🇿🇦 ZA | 338 |
| 19 | 🇳🇴 NO | 329 |
| 20 | 🇵🇭 PH | 303 |
| 21 | 🇹🇷 TR | 292 |
| 22 | 🇰🇷 KR | 290 |
| 23 | 🇬🇹 GT | 270 |
| 24 | 🇵🇱 PL | 223 |
| 25 | 🇹🇭 TH | 222 |
| 26 | 🇲🇦 MA | 187 |
| 27 | 🇮🇩 ID | 175 |
| 28 | 🇲🇪 ME | 164 |
| 29 | 🇲🇴 MO | 163 |
| 30 | 🇧🇸 BS | 159 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 375 |
| 2 | Tokyo International Airport |  | JP | 299 |
| 3 | El Dorado International Airport |  | CO | 292 |
| 4 | Indira Gandhi International Airport |  | IN | 289 |
| 5 | Denver International Airport |  | US | 280 |
| 6 | Harry Reid International Airport |  | US | 214 |
| 7 | Frankfurt am Main International Airport |  | DE | 206 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 205 |
| 9 | Zurich Airport |  | CH | 191 |
| 10 | La Aurora Airport |  | GT | 189 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 166 |
| 13 | Macau International Airport |  | MO | 163 |
| 14 | Guaymaral Airport |  | CO | 162 |
| 15 | Bengaluru International Airport |  | IN | 154 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 153 |
| 17 | Chicago O'Hare International Airport |  | US | 147 |
| 18 | Charlotte/Douglas International Airport |  | US | 142 |
| 19 | Ninoy Aquino International Airport |  | PH | 139 |
| 20 | Congonhas Airport |  | BR | 139 |
| 21 | Madrid Barajas International Airport |  | ES | 138 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 135 |
| 23 | Netaji Subhash Chandra Bose International Airport |  | IN | 133 |
| 24 | Kuala Lumpur International Airport |  | MY | 130 |
| 25 | Tenerife Norte Airport |  | ES | 129 |
| 26 | Daniel K Inouye International Airport |  | US | 122 |
| 27 | Reno/Tahoe International Airport |  | US | 122 |
| 28 | Malpensa International Airport |  | IT | 121 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 121 |
| 30 | Salt Lake City International Airport |  | US | 121 |
| 31 | Charles de Gaulle International Airport |  | FR | 117 |
| 32 | Vitoria/Foronda Airport |  | ES | 113 |
| 33 | Barcelona International Airport |  | ES | 106 |
| 34 | Pune Airport |  | IN | 105 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 104 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 37 | Austin-Bergstrom International Airport |  | US | 103 |
| 38 | Gimpo International Airport |  | KR | 101 |
| 39 | Seattle-Tacoma International Airport |  | US | 98 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 98 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 72 | 14m | 114 km | 141.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 62 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 48 | 31m | - | - |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 46 | 1h 45m | 1,156 km | 917.7 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 39 | 16m | 206 km | 138.7 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 38 | 22m | 99 km | 65.1 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 12 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 36 | 27m | 152 km | 94.1 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 35 | 28m | 275 km | 165.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 34 | 53m | 556 km | 325.9 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 32 | 1h 54m | 1,304 km | 719.9 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 29 | 1h 42m | 1,423 km | 711.7 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 28 | 23m | 252 km | 121.6 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 27 | 59m | 723 km | 336.6 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 26 | 20m | 147 km | 65.8 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 26 | 13m | 99 km | 44.6 t |
| 27 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 23 | 16m | 183 km | 72.5 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 23 | 53m | 493 km | 195.7 t |
| 30 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 22 | 34m | 431 km | 163.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N65474 |  | Albuquerque International Sunport Airport (KABQ) | Santa Fe Regional Airport (KSAF) | 2026-04-04 10:41 UTC | 2026-04-04 13:42 UTC | 3h 0m |
| CXK141 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-04 13:20 UTC | 2026-04-04 13:40 UTC | 19m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-04 11:55 UTC | 2026-04-04 13:33 UTC | 1h 37m |
| N6986U |  | Plant City Airport (KPCM) | Plant City Airport (KPCM) | 2026-04-04 13:21 UTC | 2026-04-04 13:32 UTC | 11m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-04-04 13:10 UTC | 2026-04-04 13:29 UTC | 19m |
| BRCAT07 | BRC | Roswell Air Center Airport (KROW) | Roswell Air Center Airport (KROW) | 2026-04-04 13:00 UTC | 2026-04-04 13:26 UTC | 25m |
| NWX477 | NWX | Lebanon Municipal Airport (KM54) | Cedar Crest Field (1TN0) | 2026-04-04 13:01 UTC | 2026-04-04 13:23 UTC | 21m |
| PSFAM | PSF | Estancia Santana Airport (SWER) | Rio Arraias Airport (SIOI) | 2026-04-04 12:16 UTC | 2026-04-04 13:17 UTC | 1h 0m |
| HBZVU | HBZ | Muenster Aero Airport (LSPU) | Raron Airport (LSTA) | 2026-04-04 12:49 UTC | 2026-04-04 13:13 UTC | 24m |
| CXK141 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-04 12:51 UTC | 2026-04-04 13:08 UTC | 17m |
| N6964H |  | Montgomery County Airpark (KGAI) | Carroll County Regional/Jack B Poage Field (KDMW) | 2026-04-04 12:22 UTC | 2026-04-04 13:07 UTC | 44m |
| RYR63XE | Ryanair | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-04 11:22 UTC | 2026-04-04 13:02 UTC | 1h 40m |
| UBG157 | UBG | VGZR (VGZR) | Cox's Bazar Airport (VGCB) | 2026-04-04 12:23 UTC | 2026-04-04 13:02 UTC | 38m |
| N9569Y |  | Melbourne Orlando International Airport (KMLB) | Bartow Executive Airport (KBOW) | 2026-04-04 12:04 UTC | 2026-04-04 12:58 UTC | 53m |
| RYR75SE | Ryanair | Brussels South Charleroi Airport (EBCI) | Perugia / San Egidio Airport (LIRZ) | 2026-04-04 11:36 UTC | 2026-04-04 12:55 UTC | 1h 18m |
| PH1469 |  | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-04-04 12:10 UTC | 2026-04-04 12:51 UTC | 41m |
| SNJ37 | SNJ | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-04-04 11:24 UTC | 2026-04-04 12:51 UTC | 1h 26m |
| AZU4158 | AZU | Viracopos International Airport (SBKP) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-04-04 11:59 UTC | 2026-04-04 12:49 UTC | 49m |
| WIF170 | WIF | Bergen Airport Flesland (ENBR) | Florø Airport (ENFL) | 2026-04-04 12:20 UTC | 2026-04-04 12:49 UTC | 28m |
| IGO6437 | IndiGo | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 2026-04-04 11:09 UTC | 2026-04-04 12:48 UTC | 1h 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
