# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_16:33:30_UTC-green)

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

**Latest saved flight:** 2026-04-15 16:33:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-15 16:33:30 UTC

- **36,100** saved flights
- **15,779** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **36,100** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **437,833.6 tonnes** estimated CO2 emissions
- **25,381,657 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1544 |
| 2 | SkyWest Airlines | 1422 |
| 3 | IndiGo | 903 |
| 4 | EJA | 617 |
| 5 | American Airlines | 610 |
| 6 | Southwest Airlines | 509 |
| 7 | ENY | 476 |
| 8 | AXM | 386 |
| 9 | Lufthansa | 383 |
| 10 | LATAM Airlines | 368 |
| 11 | Vueling | 366 |
| 12 | AZU | 322 |
| 13 | All Nippon Airways | 321 |
| 14 | Delta Air Lines | 302 |
| 15 | QLK | 302 |
| 16 | LXJ | 285 |
| 17 | Swiss International | 275 |
| 18 | WIF | 267 |
| 19 | AEE | 245 |
| 20 | easyJet | 240 |
| 21 | Alaska Airlines | 237 |
| 22 | EJU | 235 |
| 23 | VIV | 230 |
| 24 | Japan Airlines | 222 |
| 25 | Air France | 205 |
| 26 | EDV | 203 |
| 27 | United Airlines | 199 |
| 28 | GLO | 195 |
| 29 | AIQ | 191 |
| 30 | JetBlue | 189 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 28200 |
| 2 | 🇮🇳 IN | 2763 |
| 3 | 🇪🇸 ES | 2698 |
| 4 | 🇦🇺 AU | 2549 |
| 5 | 🇧🇷 BR | 2137 |
| 6 | 🇯🇵 JP | 1968 |
| 7 | 🇮🇹 IT | 1939 |
| 8 | 🇩🇪 DE | 1862 |
| 9 | 🇨🇴 CO | 1775 |
| 10 | 🇨🇦 CA | 1755 |
| 11 | 🇬🇧 GB | 1495 |
| 12 | 🇫🇷 FR | 1363 |
| 13 | 🇲🇽 MX | 1134 |
| 14 | 🇬🇷 GR | 1099 |
| 15 | 🇨🇭 CH | 1000 |
| 16 | 🇲🇾 MY | 929 |
| 17 | 🇳🇴 NO | 871 |
| 18 | 🇳🇿 NZ | 772 |
| 19 | 🇿🇦 ZA | 768 |
| 20 | 🇵🇭 PH | 687 |
| 21 | 🇹🇭 TH | 669 |
| 22 | 🇹🇷 TR | 661 |
| 23 | 🇬🇹 GT | 619 |
| 24 | 🇰🇷 KR | 611 |
| 25 | 🇵🇱 PL | 567 |
| 26 | 🇲🇦 MA | 449 |
| 27 | 🇳🇱 NL | 360 |
| 28 | 🇲🇪 ME | 350 |
| 29 | 🇧🇸 BS | 349 |
| 30 | 🇮🇩 ID | 345 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 850 |
| 2 | Tokyo International Airport |  | JP | 667 |
| 3 | El Dorado International Airport |  | CO | 633 |
| 4 | Denver International Airport |  | US | 603 |
| 5 | Indira Gandhi International Airport |  | IN | 586 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 541 |
| 7 | Harry Reid International Airport |  | US | 475 |
| 8 | La Aurora Airport |  | GT | 454 |
| 9 | Zurich Airport |  | CH | 447 |
| 10 | Guaymaral Airport |  | CO | 443 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 363 |
| 12 | Kuala Lumpur International Airport |  | MY | 360 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 359 |
| 14 | Chicago O'Hare International Airport |  | US | 357 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 345 |
| 16 | Frankfurt am Main International Airport |  | DE | 338 |
| 17 | Madrid Barajas International Airport |  | ES | 326 |
| 18 | Macau International Airport |  | MO | 322 |
| 19 | Tenerife Norte Airport |  | ES | 322 |
| 20 | Bengaluru International Airport |  | IN | 322 |
| 21 | Charlotte/Douglas International Airport |  | US | 321 |
| 22 | Congonhas Airport |  | BR | 320 |
| 23 | Ninoy Aquino International Airport |  | PH | 318 |
| 24 | Malpensa International Airport |  | IT | 294 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 282 |
| 26 | Daniel K Inouye International Airport |  | US | 272 |
| 27 | Salt Lake City International Airport |  | US | 271 |
| 28 | Charles de Gaulle International Airport |  | FR | 269 |
| 29 | Capua Airport |  | IT | 262 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 254 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 254 |
| 32 | Reno/Tahoe International Airport |  | US | 249 |
| 33 | O. R. Tambo International Airport |  | ZA | 247 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 246 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 238 |
| 36 | Vitoria/Foronda Airport |  | ES | 237 |
| 37 | Barcelona International Airport |  | ES | 236 |
| 38 | Viracopos International Airport |  | BR | 227 |
| 39 | Don Mueang International Airport |  | TH | 226 |
| 40 | Seattle-Tacoma International Airport |  | US | 223 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 174 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 168 | 1h 8m | 706 km | 2,045.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 147 | 14m | 114 km | 288.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 134 | 24m | 225 km | 519.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 104 | 1h 27m | 910 km | 1,632.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 96 | 19m | 165 km | 273.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 91 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 87 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 86 | 21m | 244 km | 362.1 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 78 | 27m | 275 km | 369.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 78 | 21m | 99 km | 133.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 75 | 1h 11m | 770 km | 996.3 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 69 | 31m | 369 km | 439.2 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 68 | 45m | 452 km | 530.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 61 | 20m | 147 km | 154.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 60 | 52m | 556 km | 575.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 60 | 20m | 250 km | 259.2 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 55 | 13m | 99 km | 94.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 53 | 16m | 162 km | 148.6 t |
| 28 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 52 | 26m | 215 km | 192.6 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 51 | 1h 20m | 961 km | 845.4 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 50 | 12m | 15 km | 13.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ASI230 | ASI | Lakeside Airpark (AZ05) | Wickenburg Municipal Airport (KE25) | 2026-04-15 15:52 UTC | 2026-04-15 16:33 UTC | 41m |
| N564MM |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-15 15:56 UTC | 2026-04-15 16:33 UTC | 37m |
| FRA21 | FRA | RAF Northolt (EGWU) | RAF Northolt (EGWU) | 2026-04-15 15:57 UTC | 2026-04-15 16:27 UTC | 30m |
| N4612D |  | 74OR (74OR) | Mc Minnville Municipal Airport (KMMV) | 2026-04-15 16:14 UTC | 2026-04-15 16:25 UTC | 11m |
| HAF352V | HAF | Doha International Airport (OTBD) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-15 11:20 UTC | 2026-04-15 16:22 UTC | 5h 1m |
| N1019F |  | Whiteman Airport (KWHP) | Riverside Airport (KRAL) | 2026-04-15 15:36 UTC | 2026-04-15 16:19 UTC | 43m |
| CXK301 | CXK | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-04-15 15:55 UTC | 2026-04-15 16:19 UTC | 24m |
| WATTS27 | WAT | Pinal Airpark (KMZJ) | Pinal Airpark (KMZJ) | 2026-04-15 15:37 UTC | 2026-04-15 16:17 UTC | 40m |
| CXK119 | CXK | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-15 15:41 UTC | 2026-04-15 16:14 UTC | 33m |
| WLDLD27 | WLD | Centennial Airport (KAPA) | Perry Stokes Airport (KTAD) | 2026-04-15 15:36 UTC | 2026-04-15 16:13 UTC | 37m |
| CASH81 | CAS | 2TX3 (2TX3) | Flying J Ranch Airport (7TE4) | 2026-04-15 15:32 UTC | 2026-04-15 16:12 UTC | 39m |
| N2725N |  | Dane County Regional/Truax Field (KMSN) | Turner Airport (4WI4) | 2026-04-15 15:36 UTC | 2026-04-15 16:12 UTC | 35m |
| N6DM |  | Lake Havasu City Airport (KHII) | Henderson Executive Airport (KHND) | 2026-04-15 15:31 UTC | 2026-04-15 16:06 UTC | 34m |
| N834KC |  | Landing At River's Edge Airport (98TN) | Landing At River's Edge Airport (98TN) | 2026-04-15 15:56 UTC | 2026-04-15 16:03 UTC | 7m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-15 15:29 UTC | 2026-04-15 16:03 UTC | 34m |
| TG06 |  | Pueblo Memorial Airport (KPUB) | Cuchara Ranch Airport (CD48) | 2026-04-15 15:24 UTC | 2026-04-15 16:03 UTC | 39m |
| VWA102 | VWA | Falcon Field (KFFZ) | Montezuma Airport (19AZ) | 2026-04-15 14:45 UTC | 2026-04-15 16:03 UTC | 1h 17m |
| N5011K |  | Fort Worth Meacham International Airport (KFTW) | 3TX2 (3TX2) | 2026-04-15 15:49 UTC | 2026-04-15 16:02 UTC | 13m |
| N257FA |  | Lehigh Valley International Airport (KABE) | Lancaster Airport (KLNS) | 2026-04-15 15:27 UTC | 2026-04-15 16:01 UTC | 34m |
| DLH796 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-04-15 05:20 UTC | 2026-04-15 16:01 UTC | 10h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
