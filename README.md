# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_15:58:49_UTC-green)

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

**Latest saved flight:** 2026-04-17 15:58:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 15:58:49 UTC

- **39,224** saved flights
- **16,820** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **39,224** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **473,742.3 tonnes** estimated CO2 emissions
- **27,463,320 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1650 |
| 2 | SkyWest Airlines | 1519 |
| 3 | IndiGo | 972 |
| 4 | EJA | 673 |
| 5 | American Airlines | 656 |
| 6 | Southwest Airlines | 542 |
| 7 | ENY | 504 |
| 8 | AXM | 413 |
| 9 | Vueling | 394 |
| 10 | LATAM Airlines | 390 |
| 11 | Lufthansa | 386 |
| 12 | All Nippon Airways | 351 |
| 13 | AZU | 348 |
| 14 | Delta Air Lines | 329 |
| 15 | QLK | 327 |
| 16 | LXJ | 310 |
| 17 | WIF | 310 |
| 18 | Swiss International | 300 |
| 19 | AEE | 262 |
| 20 | Alaska Airlines | 258 |
| 21 | easyJet | 258 |
| 22 | EJU | 256 |
| 23 | VIV | 246 |
| 24 | Japan Airlines | 238 |
| 25 | Air France | 221 |
| 26 | United Airlines | 213 |
| 27 | EDV | 212 |
| 28 | GLO | 204 |
| 29 | JetBlue | 203 |
| 30 | AIQ | 202 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 30793 |
| 2 | 🇮🇳 IN | 2965 |
| 3 | 🇪🇸 ES | 2923 |
| 4 | 🇦🇺 AU | 2785 |
| 5 | 🇧🇷 BR | 2305 |
| 6 | 🇯🇵 JP | 2129 |
| 7 | 🇮🇹 IT | 2055 |
| 8 | 🇩🇪 DE | 1994 |
| 9 | 🇨🇦 CA | 1918 |
| 10 | 🇨🇴 CO | 1903 |
| 11 | 🇬🇧 GB | 1615 |
| 12 | 🇫🇷 FR | 1495 |
| 13 | 🇲🇽 MX | 1223 |
| 14 | 🇬🇷 GR | 1188 |
| 15 | 🇨🇭 CH | 1085 |
| 16 | 🇲🇾 MY | 1003 |
| 17 | 🇳🇴 NO | 990 |
| 18 | 🇿🇦 ZA | 821 |
| 19 | 🇳🇿 NZ | 811 |
| 20 | 🇵🇭 PH | 722 |
| 21 | 🇹🇭 TH | 715 |
| 22 | 🇹🇷 TR | 696 |
| 23 | 🇬🇹 GT | 662 |
| 24 | 🇰🇷 KR | 641 |
| 25 | 🇵🇱 PL | 616 |
| 26 | 🇲🇦 MA | 487 |
| 27 | 🇳🇱 NL | 400 |
| 28 | 🇲🇪 ME | 390 |
| 29 | 🇧🇸 BS | 382 |
| 30 | 🇮🇩 ID | 365 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 907 |
| 2 | Tokyo International Airport |  | JP | 728 |
| 3 | El Dorado International Airport |  | CO | 670 |
| 4 | Denver International Airport |  | US | 651 |
| 5 | Indira Gandhi International Airport |  | IN | 638 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 589 |
| 7 | Harry Reid International Airport |  | US | 509 |
| 8 | Guaymaral Airport |  | CO | 498 |
| 9 | La Aurora Airport |  | GT | 486 |
| 10 | Zurich Airport |  | CH | 475 |
| 11 | Kuala Lumpur International Airport |  | MY | 394 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 384 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 382 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 379 |
| 15 | Chicago O'Hare International Airport |  | US | 378 |
| 16 | Macau International Airport |  | MO | 362 |
| 17 | Madrid Barajas International Airport |  | ES | 356 |
| 18 | Tenerife Norte Airport |  | ES | 354 |
| 19 | Charlotte/Douglas International Airport |  | US | 349 |
| 20 | Frankfurt am Main International Airport |  | DE | 349 |
| 21 | Bengaluru International Airport |  | IN | 344 |
| 22 | Congonhas Airport |  | BR | 339 |
| 23 | Ninoy Aquino International Airport |  | PH | 335 |
| 24 | Malpensa International Airport |  | IT | 318 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 302 |
| 26 | Salt Lake City International Airport |  | US | 296 |
| 27 | Daniel K Inouye International Airport |  | US | 290 |
| 28 | Charles de Gaulle International Airport |  | FR | 288 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 286 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 273 |
| 31 | Vitoria/Foronda Airport |  | ES | 269 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 264 |
| 33 | O. R. Tambo International Airport |  | ZA | 263 |
| 34 | Capua Airport |  | IT | 263 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 262 |
| 36 | Reno/Tahoe International Airport |  | US | 259 |
| 37 | Barcelona International Airport |  | ES | 254 |
| 38 | Viracopos International Airport |  | BR | 239 |
| 39 | Don Mueang International Airport |  | TH | 239 |
| 40 | Miami International Airport |  | US | 234 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 199 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 183 | 1h 8m | 706 km | 2,228.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 157 | 14m | 114 km | 307.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 114 | 28m | 304 km | 597.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 105 | 19m | 165 km | 298.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 101 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 99 | 21m | 244 km | 416.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 96 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 91 | 26m | 275 km | 431.2 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 82 | 21m | 99 km | 140.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 77 | 45m | 452 km | 600.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 73 | 27m | 152 km | 190.8 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 72 | 31m | 369 km | 458.3 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 62 | 52m | 556 km | 594.3 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 61 | 1h 41m | 1,423 km | 1,497.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 23 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 60 | 26m | 215 km | 222.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 59 | 13m | 99 km | 101.2 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 59 | 16m | 162 km | 165.4 t |
| 26 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 55 | 1h 53m | 1,304 km | 1,237.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 54 | 1h 21m | 961 km | 895.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SWA1062 | Southwest Airlines | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-17 14:48 UTC | 2026-04-17 15:58 UTC | 1h 10m |
| FCM1M | FCM | Tampere-Pirkkala Airport (EFTP) | Tampere-Pirkkala Airport (EFTP) | 2026-04-17 15:04 UTC | 2026-04-17 15:57 UTC | 53m |
| JBU1286 | JetBlue | Pittsburgh International Airport (KPIT) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-17 14:37 UTC | 2026-04-17 15:56 UTC | 1h 18m |
| N38809 |  | Peters Airport (4NJ8) | Sky Manor Airport (KN40) | 2026-04-17 15:29 UTC | 2026-04-17 15:52 UTC | 23m |
| N58VL |  | Republic Airport (KFRG) | Norwood Memorial Airport (KOWD) | 2026-04-17 15:14 UTC | 2026-04-17 15:51 UTC | 37m |
| N157BD |  | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-04-17 14:45 UTC | 2026-04-17 15:50 UTC | 1h 4m |
| DAL2098 | Delta Air Lines | Austin-Bergstrom International Airport (KAUS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-17 12:23 UTC | 2026-04-17 15:48 UTC | 3h 25m |
| N715LL |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-17 15:26 UTC | 2026-04-17 15:42 UTC | 16m |
| WICK1 | WIC | Randolph Afb Airport (KRND) | South Texas Regional At Hondo Airport (KHDO) | 2026-04-17 15:28 UTC | 2026-04-17 15:41 UTC | 13m |
| N409PJ |  | Funny Farm Airport (4CA2) | Funny Farm Airport (4CA2) | 2026-04-17 15:26 UTC | 2026-04-17 15:40 UTC | 14m |
| N739XU |  | Blue Mountain Academy (Pvt) Airport (PA92) | Blue Mountain Academy (Pvt) Airport (PA92) | 2026-04-17 15:15 UTC | 2026-04-17 15:40 UTC | 24m |
| N719KF |  | Half Moon Bay Airport (KHAF) | San Carlos Airport (KSQL) | 2026-04-17 15:24 UTC | 2026-04-17 15:33 UTC | 9m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-17 15:15 UTC | 2026-04-17 15:33 UTC | 17m |
| N915KF |  | Half Moon Bay Airport (KHAF) | San Carlos Airport (KSQL) | 2026-04-17 15:24 UTC | 2026-04-17 15:33 UTC | 8m |
| N425DR |  | La Aurora Airport (MGGT) | Santa Cruz del Quiche Airport (MGQC) | 2026-04-17 15:19 UTC | 2026-04-17 15:32 UTC | 13m |
| WIF514 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-17 15:02 UTC | 2026-04-17 15:29 UTC | 26m |
| PAT916 | PAT | Lincoln Airport (KLNK) | Morrilton Airport (07AR) | 2026-04-17 13:46 UTC | 2026-04-17 15:27 UTC | 1h 41m |
| N423RM |  | Clearwater Executive Airport (KCLW) | Albert Whitted Airport (KSPG) | 2026-04-17 14:26 UTC | 2026-04-17 15:26 UTC | 59m |
| IBE04GH | Iberia | Madrid Barajas International Airport (LEMD) | A Coruna Airport (LECO) | 2026-04-17 14:42 UTC | 2026-04-17 15:26 UTC | 43m |
| AFL2143 | AFL | Antalya International Airport (LTAI) | Sheremetyevo International Airport (UUEE) | 2026-04-17 11:21 UTC | 2026-04-17 15:24 UTC | 4h 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
