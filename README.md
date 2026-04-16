# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_19:45:54_UTC-green)

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

**Latest saved flight:** 2026-04-16 19:45:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-16 19:45:54 UTC

- **37,907** saved flights
- **16,385** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **37,907** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **457,356.5 tonnes** estimated CO2 emissions
- **26,513,417 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1603 |
| 2 | SkyWest Airlines | 1486 |
| 3 | IndiGo | 932 |
| 4 | EJA | 648 |
| 5 | American Airlines | 633 |
| 6 | Southwest Airlines | 524 |
| 7 | ENY | 491 |
| 8 | AXM | 401 |
| 9 | Lufthansa | 385 |
| 10 | LATAM Airlines | 381 |
| 11 | Vueling | 381 |
| 12 | AZU | 339 |
| 13 | All Nippon Airways | 337 |
| 14 | Delta Air Lines | 324 |
| 15 | QLK | 313 |
| 16 | LXJ | 303 |
| 17 | WIF | 287 |
| 18 | Swiss International | 282 |
| 19 | AEE | 253 |
| 20 | Alaska Airlines | 250 |
| 21 | EJU | 249 |
| 22 | easyJet | 249 |
| 23 | VIV | 240 |
| 24 | Japan Airlines | 227 |
| 25 | Air France | 215 |
| 26 | United Airlines | 210 |
| 27 | EDV | 208 |
| 28 | GLO | 199 |
| 29 | AIQ | 198 |
| 30 | Avianca | 195 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 29821 |
| 2 | 🇮🇳 IN | 2853 |
| 3 | 🇪🇸 ES | 2824 |
| 4 | 🇦🇺 AU | 2655 |
| 5 | 🇧🇷 BR | 2233 |
| 6 | 🇯🇵 JP | 2037 |
| 7 | 🇮🇹 IT | 2002 |
| 8 | 🇩🇪 DE | 1940 |
| 9 | 🇨🇴 CO | 1869 |
| 10 | 🇨🇦 CA | 1849 |
| 11 | 🇬🇧 GB | 1565 |
| 12 | 🇫🇷 FR | 1442 |
| 13 | 🇲🇽 MX | 1190 |
| 14 | 🇬🇷 GR | 1144 |
| 15 | 🇨🇭 CH | 1036 |
| 16 | 🇲🇾 MY | 963 |
| 17 | 🇳🇴 NO | 923 |
| 18 | 🇿🇦 ZA | 799 |
| 19 | 🇳🇿 NZ | 789 |
| 20 | 🇵🇭 PH | 704 |
| 21 | 🇹🇭 TH | 690 |
| 22 | 🇹🇷 TR | 681 |
| 23 | 🇬🇹 GT | 649 |
| 24 | 🇰🇷 KR | 627 |
| 25 | 🇵🇱 PL | 596 |
| 26 | 🇲🇦 MA | 476 |
| 27 | 🇳🇱 NL | 379 |
| 28 | 🇲🇪 ME | 373 |
| 29 | 🇧🇸 BS | 371 |
| 30 | 🇮🇩 ID | 353 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 885 |
| 2 | Tokyo International Airport |  | JP | 693 |
| 3 | El Dorado International Airport |  | CO | 660 |
| 4 | Denver International Airport |  | US | 630 |
| 5 | Indira Gandhi International Airport |  | IN | 616 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 565 |
| 7 | Harry Reid International Airport |  | US | 495 |
| 8 | Guaymaral Airport |  | CO | 484 |
| 9 | La Aurora Airport |  | GT | 477 |
| 10 | Zurich Airport |  | CH | 456 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 378 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 375 |
| 13 | Kuala Lumpur International Airport |  | MY | 375 |
| 14 | Chicago O'Hare International Airport |  | US | 368 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 361 |
| 16 | Madrid Barajas International Airport |  | ES | 346 |
| 17 | Frankfurt am Main International Airport |  | DE | 346 |
| 18 | Macau International Airport |  | MO | 342 |
| 19 | Tenerife Norte Airport |  | ES | 339 |
| 20 | Charlotte/Douglas International Airport |  | US | 338 |
| 21 | Congonhas Airport |  | BR | 330 |
| 22 | Bengaluru International Airport |  | IN | 328 |
| 23 | Ninoy Aquino International Airport |  | PH | 327 |
| 24 | Malpensa International Airport |  | IT | 312 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 292 |
| 26 | Salt Lake City International Airport |  | US | 289 |
| 27 | Daniel K Inouye International Airport |  | US | 282 |
| 28 | Charles de Gaulle International Airport |  | FR | 280 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 269 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 268 |
| 31 | Capua Airport |  | IT | 262 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 257 |
| 33 | Vitoria/Foronda Airport |  | ES | 257 |
| 34 | O. R. Tambo International Airport |  | ZA | 256 |
| 35 | Reno/Tahoe International Airport |  | US | 255 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 246 |
| 37 | Barcelona International Airport |  | ES | 243 |
| 38 | Don Mueang International Airport |  | TH | 236 |
| 39 | Viracopos International Airport |  | BR | 234 |
| 40 | Seattle-Tacoma International Airport |  | US | 230 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 192 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 174 | 1h 8m | 706 km | 2,118.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 154 | 14m | 114 km | 302.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 136 | 24m | 225 km | 527.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 109 | 1h 27m | 910 km | 1,710.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 102 | 19m | 165 km | 290.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 96 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 94 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 92 | 21m | 244 km | 387.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 86 | 26m | 275 km | 407.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 82 | 54m | 546 km | 772.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 82 | 21m | 99 km | 140.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 77 | 1h 11m | 770 km | 1,022.9 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 72 | 45m | 452 km | 561.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 71 | 31m | 369 km | 451.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 57 | 1h 41m | 1,423 km | 1,398.9 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 57 | 13m | 99 km | 97.7 t |
| 25 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 56 | 26m | 215 km | 207.4 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 56 | 16m | 162 km | 157.0 t |
| 28 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 53 | 13m | - | - |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 52 | 12m | 15 km | 13.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK1034 | CXK | Flying Cloud Airport (KFCM) | Hutchinson Municipal/Butler Field (KHCD) | 2026-04-16 19:18 UTC | 2026-04-16 19:45 UTC | 27m |
| N407DS |  | Grimes Field (KI74) | S And S Field (1OH1) | 2026-04-16 19:18 UTC | 2026-04-16 19:42 UTC | 23m |
| N768GA |  | Knoxville Downtown Island Airport (KDKX) | Knoxville Downtown Island Airport (KDKX) | 2026-04-16 19:01 UTC | 2026-04-16 19:38 UTC | 37m |
| N5444F |  | Flying J Airport (86TX) | New Braunfels Ntl Airport (KBAZ) | 2026-04-16 19:20 UTC | 2026-04-16 19:34 UTC | 14m |
| N20597 |  | Lancaster Airport (KLNS) | Deck Airport (K9D4) | 2026-04-16 18:43 UTC | 2026-04-16 19:34 UTC | 50m |
| N355G |  | Montgomery-Gibbs Executive Airport (KMYF) | San Bernardino International Airport (KSBD) | 2026-04-16 18:19 UTC | 2026-04-16 19:30 UTC | 1h 10m |
| KATT47 | KAT | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bay Minette Municipal Airport (K1R8) | 2026-04-16 19:02 UTC | 2026-04-16 19:21 UTC | 18m |
| N908FG |  | Trenton Mercer Airport (KTTN) | Northeast Philadelphia Airport (KPNE) | 2026-04-16 18:05 UTC | 2026-04-16 19:20 UTC | 1h 15m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-16 18:43 UTC | 2026-04-16 19:18 UTC | 35m |
| UAE1CR | Emirates | Dubai International Airport (OMDB) | Melbourne International Airport (YMML) | 2026-04-16 06:38 UTC | 2026-04-16 19:18 UTC | 12h 40m |
| N398AA |  | Sanctuary Ranch Airport (7TS4) | Addington Field (4TX8) | 2026-04-16 18:28 UTC | 2026-04-16 19:18 UTC | 50m |
| N310RR |  | Sutter County Airport (KO52) | Yuba County Airport (KMYV) | 2026-04-16 19:07 UTC | 2026-04-16 19:14 UTC | 7m |
| G26993 |  | Chuck's Airport (4OK6) | Mc Alester Regional Airport (KMLC) | 2026-04-16 18:34 UTC | 2026-04-16 19:12 UTC | 38m |
| N699SU |  | Aurora State Airport (KUAO) | Western Helicopter Services Airport (OR38) | 2026-04-16 19:04 UTC | 2026-04-16 19:09 UTC | 4m |
| N42SH |  | Mariposa-Yosemite Airport (KMPI) | Lake Tahoe Airport (KTVL) | 2026-04-16 18:41 UTC | 2026-04-16 19:09 UTC | 28m |
| SAMU42 | SAM | Saint-Etienne-Boutheon Airport (LFMH) | Lyon-Bron Airport (LFLY) | 2026-04-16 18:49 UTC | 2026-04-16 19:07 UTC | 17m |
| N234CR |  | Falcon Field (KFFZ) | Chapman Ranch Airstrip (58AZ) | 2026-04-16 18:47 UTC | 2026-04-16 19:07 UTC | 19m |
| RYR538B | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Son Bonet Airport (LESB) | 2026-04-16 17:40 UTC | 2026-04-16 19:06 UTC | 1h 25m |
| N68AB |  | Prescott Regional/Ernest A Love Field (KPRC) | Addington Field (4TX8) | 2026-04-16 17:27 UTC | 2026-04-16 19:06 UTC | 1h 39m |
| ERU814 | ERU | Daytona Beach International Airport (KDAB) | Arthur Dunn Air Park (KX21) | 2026-04-16 18:39 UTC | 2026-04-16 19:03 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
