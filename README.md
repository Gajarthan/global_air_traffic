# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_22:32:13_UTC-green)

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

**Latest saved flight:** 2026-04-11 22:32:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 22:32:13 UTC

- **29,801** saved flights
- **13,731** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **29,801** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **363,728.9 tonnes** estimated CO2 emissions
- **21,085,732 km** total distance flown
- **844 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1226 |
| 2 | SkyWest Airlines | 1223 |
| 3 | IndiGo | 767 |
| 4 | EJA | 520 |
| 5 | American Airlines | 519 |
| 6 | Southwest Airlines | 432 |
| 7 | ENY | 403 |
| 8 | Lufthansa | 359 |
| 9 | AXM | 314 |
| 10 | Vueling | 306 |
| 11 | LATAM Airlines | 292 |
| 12 | All Nippon Airways | 263 |
| 13 | AZU | 262 |
| 14 | QLK | 254 |
| 15 | Delta Air Lines | 245 |
| 16 | LXJ | 238 |
| 17 | Swiss International | 217 |
| 18 | Alaska Airlines | 199 |
| 19 | EJU | 193 |
| 20 | easyJet | 193 |
| 21 | VIV | 193 |
| 22 | Japan Airlines | 190 |
| 23 | WIF | 187 |
| 24 | AEE | 186 |
| 25 | United Airlines | 179 |
| 26 | EDV | 177 |
| 27 | Avianca | 166 |
| 28 | GLO | 160 |
| 29 | JetBlue | 157 |
| 30 | Air France | 154 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23641 |
| 2 | 🇮🇳 IN | 2359 |
| 3 | 🇪🇸 ES | 2211 |
| 4 | 🇦🇺 AU | 2093 |
| 5 | 🇧🇷 BR | 1726 |
| 6 | 🇯🇵 JP | 1612 |
| 7 | 🇮🇹 IT | 1531 |
| 8 | 🇨🇴 CO | 1512 |
| 9 | 🇩🇪 DE | 1492 |
| 10 | 🇨🇦 CA | 1470 |
| 11 | 🇬🇧 GB | 1201 |
| 12 | 🇫🇷 FR | 1098 |
| 13 | 🇲🇽 MX | 960 |
| 14 | 🇬🇷 GR | 845 |
| 15 | 🇨🇭 CH | 840 |
| 16 | 🇲🇾 MY | 752 |
| 17 | 🇳🇿 NZ | 640 |
| 18 | 🇳🇴 NO | 632 |
| 19 | 🇿🇦 ZA | 609 |
| 20 | 🇬🇹 GT | 551 |
| 21 | 🇵🇭 PH | 549 |
| 22 | 🇹🇷 TR | 540 |
| 23 | 🇹🇭 TH | 532 |
| 24 | 🇰🇷 KR | 498 |
| 25 | 🇵🇱 PL | 450 |
| 26 | 🇲🇦 MA | 372 |
| 27 | 🇧🇸 BS | 318 |
| 28 | 🇲🇪 ME | 298 |
| 29 | 🇳🇱 NL | 285 |
| 30 | 🇮🇩 ID | 278 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 713 |
| 2 | Tokyo International Airport |  | JP | 540 |
| 3 | El Dorado International Airport |  | CO | 538 |
| 4 | Denver International Airport |  | US | 509 |
| 5 | Indira Gandhi International Airport |  | IN | 493 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 413 |
| 7 | La Aurora Airport |  | GT | 393 |
| 8 | Harry Reid International Airport |  | US | 384 |
| 9 | Guaymaral Airport |  | CO | 359 |
| 10 | Zurich Airport |  | CH | 358 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 311 |
| 12 | Chicago O'Hare International Airport |  | US | 311 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 310 |
| 14 | Frankfurt am Main International Airport |  | DE | 301 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 290 |
| 16 | Kuala Lumpur International Airport |  | MY | 282 |
| 17 | Macau International Airport |  | MO | 278 |
| 18 | Charlotte/Douglas International Airport |  | US | 268 |
| 19 | Bengaluru International Airport |  | IN | 268 |
| 20 | Madrid Barajas International Airport |  | ES | 263 |
| 21 | Tenerife Norte Airport |  | ES | 263 |
| 22 | Congonhas Airport |  | BR | 253 |
| 23 | Ninoy Aquino International Airport |  | PH | 252 |
| 24 | Malpensa International Airport |  | IT | 239 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 231 |
| 26 | Daniel K Inouye International Airport |  | US | 229 |
| 27 | Salt Lake City International Airport |  | US | 228 |
| 28 | Reno/Tahoe International Airport |  | US | 227 |
| 29 | Charles de Gaulle International Airport |  | FR | 211 |
| 30 | Capua Airport |  | IT | 205 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 205 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 200 |
| 33 | Miami International Airport |  | US | 200 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 199 |
| 35 | Netaji Subhash Chandra Bose International Airport |  | IN | 199 |
| 36 | O. R. Tambo International Airport |  | ZA | 194 |
| 37 | Vitoria/Foronda Airport |  | ES | 193 |
| 38 | Seattle-Tacoma International Airport |  | US | 189 |
| 39 | Barcelona International Airport |  | ES | 189 |
| 40 | Viracopos International Airport |  | BR | 183 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 139 | 1h 8m | 706 km | 1,692.3 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 139 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 125 | 14m | 114 km | 245.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 109 | 24m | 225 km | 422.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 100 | 28m | 304 km | 524.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 86 | 1h 27m | 910 km | 1,349.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 75 | 21m | 99 km | 128.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 74 | 19m | 165 km | 210.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 65 | 55m | 546 km | 612.0 t |
| 13 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 65 | 9m | - | - |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 63 | 27m | 275 km | 298.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 57 | 31m | 369 km | 362.8 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 56 | 52m | 556 km | 536.8 t |
| 19 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 53 | 21m | 244 km | 223.2 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 53 | 46m | 452 km | 413.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 50 | 20m | 250 km | 216.0 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 49 | 13m | 99 km | 84.0 t |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 46 | 20m | 147 km | 116.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 42 | 1h 19m | 961 km | 696.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 41 | 12m | 15 km | 10.8 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 39 | 26m | 215 km | 144.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GFY2112 | GFY | Scappoose Airport (KSPB) | Green Mountain Airport (WA67) | 2026-04-11 22:19 UTC | 2026-04-11 22:32 UTC | 12m |
| AFL1186 | AFL | Sheremetyevo International Airport (UUEE) | Bezymyanka Airfield (UWWG) | 2026-04-11 14:44 UTC | 2026-04-11 22:29 UTC | 7h 45m |
| KSF6 | KSF | Akron-Canton Regional Airport (KCAK) | Kent State University Airport (K1G3) | 2026-04-11 22:01 UTC | 2026-04-11 22:28 UTC | 27m |
| N1JB |  | Orlando Executive Airport (KORL) | Tampa International Airport (KTPA) | 2026-04-11 21:59 UTC | 2026-04-11 22:26 UTC | 27m |
| N8970V |  | Crystal Village Airport (2FL0) | Dawson Municipal Airport (K16J) | 2026-04-11 21:07 UTC | 2026-04-11 22:14 UTC | 1h 7m |
| CRK081 | CRK | Vancouver International Airport (CYVR) | Macau International Airport (VMMC) | 2026-04-11 08:56 UTC | 2026-04-11 22:13 UTC | 13h 17m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-04-11 11:17 UTC | 2026-04-11 22:12 UTC | 10h 54m |
| SLH386 | SLH | Punta Gorda Airport (KPGD) | Lincoln Airport (KLNK) | 2026-04-11 18:49 UTC | 2026-04-11 22:10 UTC | 3h 21m |
| CPA292 | Cathay Pacific | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Macau International Airport (VMMC) | 2026-04-11 11:38 UTC | 2026-04-11 22:09 UTC | 10h 31m |
| N9863L |  | Republic Airport (KFRG) | Francis S Gabreski Airport (KFOK) | 2026-04-11 21:39 UTC | 2026-04-11 22:09 UTC | 29m |
| TRP2 | TRP | Garner Field (02MD) | Joint Base Andrews Airport (KADW) | 2026-04-11 21:56 UTC | 2026-04-11 22:04 UTC | 7m |
| N130HB |  | Pickaway County Memorial Airport (KCYO) | Ohio State University Airport (KOSU) | 2026-04-11 21:48 UTC | 2026-04-11 22:02 UTC | 14m |
| LCY | LCY | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-04-11 21:45 UTC | 2026-04-11 22:02 UTC | 17m |
| N356CC |  | Aero Valley Airport (K52F) | Decatur Municipal Airport (KLUD) | 2026-04-11 21:53 UTC | 2026-04-11 22:00 UTC | 7m |
| N256AA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-04-11 21:27 UTC | 2026-04-11 21:58 UTC | 31m |
| N655MC |  | Baton Rouge Metro, Ryan Field (KBTR) | Austin-Bergstrom International Airport (KAUS) | 2026-04-11 20:55 UTC | 2026-04-11 21:55 UTC | 59m |
| N357BG |  | Monroe County Airport (KBMG) | Wood County Airport (K1G0) | 2026-04-11 20:08 UTC | 2026-04-11 21:51 UTC | 1h 42m |
| SCU2 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-04-11 21:48 UTC | 2026-04-11 21:48 UTC | 0m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-11 21:20 UTC | 2026-04-11 21:43 UTC | 23m |
| AAL3243 | American Airlines | Chicago O'Hare International Airport (KORD) | Harrisburg International Airport (KMDT) | 2026-04-11 20:23 UTC | 2026-04-11 21:43 UTC | 1h 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
