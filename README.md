# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_19:15:38_UTC-green)

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

**Latest saved flight:** 2026-04-05 19:15:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-05 19:15:38 UTC

- **18,741** saved flights
- **9,528** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **18,741** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **237,218.9 tonnes** estimated CO2 emissions
- **13,751,820 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 807 |
| 2 | Ryanair | 775 |
| 3 | IndiGo | 538 |
| 4 | American Airlines | 345 |
| 5 | EJA | 337 |
| 6 | Southwest Airlines | 265 |
| 7 | Lufthansa | 256 |
| 8 | ENY | 254 |
| 9 | Vueling | 206 |
| 10 | LATAM Airlines | 198 |
| 11 | AXM | 191 |
| 12 | LXJ | 162 |
| 13 | All Nippon Airways | 161 |
| 14 | Delta Air Lines | 161 |
| 15 | QLK | 154 |
| 16 | AZU | 144 |
| 17 | Swiss International | 141 |
| 18 | VIV | 141 |
| 19 | Alaska Airlines | 125 |
| 20 | Japan Airlines | 124 |
| 21 | United Airlines | 124 |
| 22 | easyJet | 123 |
| 23 | Avianca | 122 |
| 24 | AEE | 121 |
| 25 | EJU | 121 |
| 26 | EDV | 115 |
| 27 | WIF | 115 |
| 28 | AXB | 113 |
| 29 | Cathay Pacific | 105 |
| 30 | Air France | 104 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 14612 |
| 2 | 🇮🇳 IN | 1635 |
| 3 | 🇪🇸 ES | 1554 |
| 4 | 🇦🇺 AU | 1316 |
| 5 | 🇧🇷 BR | 1087 |
| 6 | 🇯🇵 JP | 994 |
| 7 | 🇨🇴 CO | 992 |
| 8 | 🇩🇪 DE | 963 |
| 9 | 🇮🇹 IT | 897 |
| 10 | 🇨🇦 CA | 823 |
| 11 | 🇬🇧 GB | 736 |
| 12 | 🇫🇷 FR | 697 |
| 13 | 🇲🇽 MX | 632 |
| 14 | 🇬🇷 GR | 536 |
| 15 | 🇨🇭 CH | 504 |
| 16 | 🇲🇾 MY | 439 |
| 17 | 🇬🇹 GT | 420 |
| 18 | 🇿🇦 ZA | 411 |
| 19 | 🇳🇿 NZ | 396 |
| 20 | 🇳🇴 NO | 383 |
| 21 | 🇹🇷 TR | 362 |
| 22 | 🇵🇭 PH | 355 |
| 23 | 🇰🇷 KR | 325 |
| 24 | 🇹🇭 TH | 273 |
| 25 | 🇵🇱 PL | 273 |
| 26 | 🇲🇦 MA | 238 |
| 27 | 🇧🇸 BS | 209 |
| 28 | 🇮🇩 ID | 205 |
| 29 | 🇲🇴 MO | 198 |
| 30 | 🇲🇪 ME | 194 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 449 |
| 2 | El Dorado International Airport |  | CO | 376 |
| 3 | Indira Gandhi International Airport |  | IN | 343 |
| 4 | Denver International Airport |  | US | 341 |
| 5 | Tokyo International Airport |  | JP | 340 |
| 6 | La Aurora Airport |  | GT | 292 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 254 |
| 8 | Harry Reid International Airport |  | US | 244 |
| 9 | Zurich Airport |  | CH | 232 |
| 10 | Frankfurt am Main International Airport |  | DE | 228 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 201 |
| 12 | Macau International Airport |  | MO | 198 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 198 |
| 14 | Guaymaral Airport |  | CO | 196 |
| 15 | Chicago O'Hare International Airport |  | US | 194 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 191 |
| 17 | Madrid Barajas International Airport |  | ES | 183 |
| 18 | Bengaluru International Airport |  | IN | 181 |
| 19 | Charlotte/Douglas International Airport |  | US | 178 |
| 20 | Tenerife Norte Airport |  | ES | 173 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 168 |
| 22 | Ninoy Aquino International Airport |  | PH | 162 |
| 23 | Congonhas Airport |  | BR | 161 |
| 24 | Kuala Lumpur International Airport |  | MY | 155 |
| 25 | Salt Lake City International Airport |  | US | 152 |
| 26 | Daniel K Inouye International Airport |  | US | 147 |
| 27 | Reno/Tahoe International Airport |  | US | 145 |
| 28 | Vitoria/Foronda Airport |  | ES | 144 |
| 29 | Malpensa International Airport |  | IT | 143 |
| 30 | Charles de Gaulle International Airport |  | FR | 142 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 140 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 139 |
| 33 | Miami International Airport |  | US | 134 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 129 |
| 35 | Barcelona International Airport |  | ES | 129 |
| 36 | Pune Airport |  | IN | 127 |
| 37 | O. R. Tambo International Airport |  | ZA | 127 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 123 |
| 39 | General Edward Lawrence Logan International Airport |  | US | 121 |
| 40 | Seattle-Tacoma International Airport |  | US | 118 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 85 | 1h 7m | 706 km | 1,034.9 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 84 | 14m | 114 km | 164.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 68 | 24m | 225 km | 263.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 63 | 27m | 152 km | 164.6 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 59 | 22m | 99 km | 101.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 55 | 1h 44m | 1,156 km | 1,097.2 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 54 | 1h 27m | 910 km | 847.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 51 | 16m | 206 km | 181.3 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 42 | 1h 53m | 1,304 km | 944.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 40 | 1h 11m | 770 km | 531.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 18 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 37 | 1h 43m | 1,423 km | 908.0 t |
| 19 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 37 | 23m | 252 km | 160.6 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 37 | 54m | 546 km | 348.4 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 37 | 4m | - | - |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 37 | 9m | - | - |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 35 | 13m | 99 km | 60.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 33 | 58m | 723 km | 411.4 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 33 | 46m | 452 km | 257.2 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 32 | 30m | 114 km | 63.0 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 29 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 30 | 20m | 250 km | 129.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 29 | 20m | 147 km | 73.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N423FP |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-04-05 18:43 UTC | 2026-04-05 19:15 UTC | 32m |
| N801GW |  | North Las Vegas Airport (KVGT) | Big Bear City Airport (KL35) | 2026-04-05 18:20 UTC | 2026-04-05 19:10 UTC | 50m |
| N177TX |  | Aero Valley Airport (K52F) | XA10 (XA10) | 2026-04-05 18:51 UTC | 2026-04-05 19:06 UTC | 15m |
| TGFYL | TGF | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-04-05 18:45 UTC | 2026-04-05 19:04 UTC | 18m |
| N386SP |  | Usaf Academy Davis Airfield (KAFF) | K00V (K00V) | 2026-04-05 18:28 UTC | 2026-04-05 18:54 UTC | 26m |
| N955SC |  | Grand Prairie Municipal Airport (KGPM) | Decatur Municipal Airport (KLUD) | 2026-04-05 18:29 UTC | 2026-04-05 18:53 UTC | 23m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-05 18:41 UTC | 2026-04-05 18:52 UTC | 11m |
| N41KS |  | Madras Municipal Airport (KS33) | Sisters Eagle Air Airport (K6K5) | 2026-04-05 18:34 UTC | 2026-04-05 18:51 UTC | 16m |
| WIF460 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-05 18:25 UTC | 2026-04-05 18:51 UTC | 25m |
| GJS4520 | GJS | Chicago O'Hare International Airport (KORD) | Chicago O'Hare International Airport (KORD) | 2026-04-05 18:47 UTC | 2026-04-05 18:48 UTC | 0m |
| N302K |  | Los Angeles International Airport (KLAX) | Bermuda Dunes Airport (KUDD) | 2026-04-05 18:27 UTC | 2026-04-05 18:47 UTC | 20m |
| N739TW |  | Palo Alto Airport (KPAO) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-05 18:33 UTC | 2026-04-05 18:47 UTC | 14m |
| VIV7345 | VIV | Francisco Sarabia International Airport (MMTC) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-05 17:41 UTC | 2026-04-05 18:43 UTC | 1h 1m |
| TGARO | TGA | Copan Ruinas Airport (MHRU) | La Aurora Airport (MGGT) | 2026-04-05 18:12 UTC | 2026-04-05 18:43 UTC | 30m |
| EAI48D | EAI | Dublin Airport (EIDW) | Letterkenny Airport (EILT) | 2026-04-05 18:10 UTC | 2026-04-05 18:40 UTC | 29m |
| N60HX |  | Indianapolis Executive Airport (KTYQ) | Scottsdale Airport (KSDL) | 2026-04-05 15:06 UTC | 2026-04-05 18:39 UTC | 3h 33m |
| KMM491 | KMM | Zurich Airport (LSZH) | Luqa Airport (LMML) | 2026-04-05 16:48 UTC | 2026-04-05 18:39 UTC | 1h 51m |
| RYR7TZ | Ryanair | Ibiza Airport (LEIB) | Ocana Airport (LEOC) | 2026-04-05 17:51 UTC | 2026-04-05 18:39 UTC | 48m |
| RYR2PW | Ryanair | Riga International Airport (EVRA) | Cologne Bonn Airport (EDDK) | 2026-04-05 16:39 UTC | 2026-04-05 18:37 UTC | 1h 58m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-05 18:16 UTC | 2026-04-05 18:36 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
