# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_18:56:26_UTC-green)

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

**Latest saved flight:** 2026-04-11 18:56:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 18:56:26 UTC

- **29,360** saved flights
- **13,578** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **29,360** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **357,042.2 tonnes** estimated CO2 emissions
- **20,698,097 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1210 |
| 2 | SkyWest Airlines | 1184 |
| 3 | IndiGo | 767 |
| 4 | EJA | 508 |
| 5 | American Airlines | 504 |
| 6 | Southwest Airlines | 419 |
| 7 | ENY | 391 |
| 8 | Lufthansa | 356 |
| 9 | AXM | 314 |
| 10 | Vueling | 304 |
| 11 | LATAM Airlines | 285 |
| 12 | All Nippon Airways | 263 |
| 13 | AZU | 255 |
| 14 | QLK | 254 |
| 15 | Delta Air Lines | 243 |
| 16 | LXJ | 236 |
| 17 | Swiss International | 217 |
| 18 | Alaska Airlines | 192 |
| 19 | EJU | 191 |
| 20 | Japan Airlines | 190 |
| 21 | VIV | 190 |
| 22 | easyJet | 189 |
| 23 | WIF | 187 |
| 24 | AEE | 185 |
| 25 | United Airlines | 175 |
| 26 | EDV | 172 |
| 27 | Avianca | 164 |
| 28 | JetBlue | 155 |
| 29 | Air France | 154 |
| 30 | AXB | 153 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23142 |
| 2 | 🇮🇳 IN | 2357 |
| 3 | 🇪🇸 ES | 2176 |
| 4 | 🇦🇺 AU | 2088 |
| 5 | 🇧🇷 BR | 1686 |
| 6 | 🇯🇵 JP | 1608 |
| 7 | 🇮🇹 IT | 1512 |
| 8 | 🇩🇪 DE | 1485 |
| 9 | 🇨🇴 CO | 1475 |
| 10 | 🇨🇦 CA | 1439 |
| 11 | 🇬🇧 GB | 1184 |
| 12 | 🇫🇷 FR | 1091 |
| 13 | 🇲🇽 MX | 937 |
| 14 | 🇬🇷 GR | 842 |
| 15 | 🇨🇭 CH | 838 |
| 16 | 🇲🇾 MY | 751 |
| 17 | 🇳🇿 NZ | 636 |
| 18 | 🇳🇴 NO | 630 |
| 19 | 🇿🇦 ZA | 609 |
| 20 | 🇵🇭 PH | 547 |
| 21 | 🇬🇹 GT | 543 |
| 22 | 🇹🇭 TH | 532 |
| 23 | 🇹🇷 TR | 531 |
| 24 | 🇰🇷 KR | 497 |
| 25 | 🇵🇱 PL | 446 |
| 26 | 🇲🇦 MA | 369 |
| 27 | 🇧🇸 BS | 312 |
| 28 | 🇲🇪 ME | 295 |
| 29 | 🇳🇱 NL | 284 |
| 30 | 🇮🇩 ID | 278 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 689 |
| 2 | Tokyo International Airport |  | JP | 540 |
| 3 | El Dorado International Airport |  | CO | 525 |
| 4 | Indira Gandhi International Airport |  | IN | 491 |
| 5 | Denver International Airport |  | US | 488 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 411 |
| 7 | La Aurora Airport |  | GT | 387 |
| 8 | Harry Reid International Airport |  | US | 375 |
| 9 | Zurich Airport |  | CH | 356 |
| 10 | Guaymaral Airport |  | CO | 348 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 305 |
| 12 | Chicago O'Hare International Airport |  | US | 304 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 302 |
| 14 | Frankfurt am Main International Airport |  | DE | 299 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 289 |
| 16 | Kuala Lumpur International Airport |  | MY | 282 |
| 17 | Macau International Airport |  | MO | 269 |
| 18 | Bengaluru International Airport |  | IN | 268 |
| 19 | Charlotte/Douglas International Airport |  | US | 264 |
| 20 | Madrid Barajas International Airport |  | ES | 256 |
| 21 | Tenerife Norte Airport |  | ES | 252 |
| 22 | Ninoy Aquino International Airport |  | PH | 251 |
| 23 | Congonhas Airport |  | BR | 245 |
| 24 | Malpensa International Airport |  | IT | 231 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 228 |
| 26 | Daniel K Inouye International Airport |  | US | 224 |
| 27 | Salt Lake City International Airport |  | US | 223 |
| 28 | Reno/Tahoe International Airport |  | US | 217 |
| 29 | Charles de Gaulle International Airport |  | FR | 210 |
| 30 | Capua Airport |  | IT | 203 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 202 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 199 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 199 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 195 |
| 35 | Miami International Airport |  | US | 195 |
| 36 | O. R. Tambo International Airport |  | ZA | 194 |
| 37 | Vitoria/Foronda Airport |  | ES | 190 |
| 38 | Barcelona International Airport |  | ES | 188 |
| 39 | Seattle-Tacoma International Airport |  | US | 183 |
| 40 | Viracopos International Airport |  | BR | 179 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 139 | 1h 8m | 706 km | 1,692.3 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 135 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 122 | 14m | 114 km | 239.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 109 | 24m | 225 km | 422.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 100 | 28m | 304 km | 524.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 86 | 1h 27m | 910 km | 1,349.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 74 | 19m | 165 km | 210.5 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 65 | 55m | 546 km | 612.0 t |
| 13 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 63 | 9m | - | - |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 61 | 27m | 275 km | 289.1 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 56 | 31m | 369 km | 356.5 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 53 | 46m | 452 km | 413.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 53 | 52m | 556 km | 508.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 50 | 20m | 250 km | 216.0 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 49 | 21m | 244 km | 206.3 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 47 | 13m | 99 km | 80.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 45 | 20m | 147 km | 113.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 41 | 1h 19m | 961 km | 679.6 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 40 | 12m | 15 km | 10.6 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 39 | 26m | 215 km | 144.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KSF12 | KSF | Kent State University Airport (K1G3) | Kent State University Airport (K1G3) | 2026-04-11 17:51 UTC | 2026-04-11 18:56 UTC | 1h 5m |
| N1026V |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-04-11 18:18 UTC | 2026-04-11 18:42 UTC | 23m |
| TRP2 | TRP | Maryland Airport (K2W5) | Joint Base Andrews Airport (KADW) | 2026-04-11 18:30 UTC | 2026-04-11 18:38 UTC | 8m |
| N46709 |  | North Exuma Airport (85FA) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-04-11 18:18 UTC | 2026-04-11 18:38 UTC | 20m |
| BRG621 | BRG | Kobuk Airport (PAOB) | Ambler Airport (PAFM) | 2026-04-11 18:24 UTC | 2026-04-11 18:35 UTC | 10m |
| WMU66 | WMU | South Bend International Airport (KSBN) | Kirsch Municipal Airport (KIRS) | 2026-04-11 18:15 UTC | 2026-04-11 18:34 UTC | 18m |
| N523RH |  | Orange Poultry Farm Airport (4NY1) | Linden Airport (KLDJ) | 2026-04-11 17:41 UTC | 2026-04-11 18:34 UTC | 52m |
| BRG2621 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-04-11 17:48 UTC | 2026-04-11 18:32 UTC | 43m |
| N90JF |  | Antonio/Nery/Juarbe Pol Airport (TJAB) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-04-11 18:19 UTC | 2026-04-11 18:30 UTC | 10m |
| VLG10HP | Vueling | Barcelona International Airport (LEBL) | Tenerife Norte Airport (GCXO) | 2026-04-11 15:14 UTC | 2026-04-11 18:28 UTC | 3h 14m |
| N5253X |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-04-11 18:09 UTC | 2026-04-11 18:26 UTC | 17m |
| N65CC |  | Washington Dulles International Airport (KIAD) | Miami Executive Airport (KTMB) | 2026-04-11 16:11 UTC | 2026-04-11 18:19 UTC | 2h 7m |
| ERU392 | ERU | Daytona Beach International Airport (KDAB) | North Exuma Airport (85FA) | 2026-04-11 17:52 UTC | 2026-04-11 18:18 UTC | 26m |
| CNV4620 | CNV | Oceana Nas (Apollo Soucek Field) Airport (KNTU) | The Florida Keys Marathon International Airport (KMTH) | 2026-04-11 16:16 UTC | 2026-04-11 18:13 UTC | 1h 57m |
| N862TW |  | Martin State Airport (KMTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-11 17:16 UTC | 2026-04-11 18:11 UTC | 54m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-11 17:50 UTC | 2026-04-11 18:11 UTC | 20m |
| AEE278 | AEE | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-04-11 17:45 UTC | 2026-04-11 18:09 UTC | 24m |
| N4397Q |  | Dupage Airport (KDPA) | Schaumburg Regional Airport (K06C) | 2026-04-11 17:49 UTC | 2026-04-11 18:07 UTC | 18m |
| N2350E |  | Valkaria Airport (KX59) | Rlm Farms Airport (FD09) | 2026-04-11 17:21 UTC | 2026-04-11 18:06 UTC | 44m |
| N12NY |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-11 17:58 UTC | 2026-04-11 18:04 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
