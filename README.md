# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_18:28:02_UTC-green)

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

**Latest saved flight:** 2026-04-19 18:28:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 18:28:02 UTC

- **43,686** saved flights
- **18,222** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **43,686** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **525,608.6 tonnes** estimated CO2 emissions
- **30,470,063 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1845 |
| 2 | SkyWest Airlines | 1686 |
| 3 | IndiGo | 1071 |
| 4 | EJA | 747 |
| 5 | American Airlines | 717 |
| 6 | Southwest Airlines | 615 |
| 7 | ENY | 566 |
| 8 | AXM | 446 |
| 9 | Lufthansa | 438 |
| 10 | Vueling | 437 |
| 11 | LATAM Airlines | 435 |
| 12 | All Nippon Airways | 397 |
| 13 | AZU | 384 |
| 14 | Delta Air Lines | 371 |
| 15 | QLK | 354 |
| 16 | LXJ | 343 |
| 17 | WIF | 340 |
| 18 | Swiss International | 337 |
| 19 | AEE | 299 |
| 20 | Alaska Airlines | 292 |
| 21 | EJU | 290 |
| 22 | easyJet | 279 |
| 23 | VIV | 276 |
| 24 | Japan Airlines | 269 |
| 25 | Air France | 250 |
| 26 | AXB | 232 |
| 27 | GLO | 230 |
| 28 | JetBlue | 230 |
| 29 | United Airlines | 230 |
| 30 | EDV | 223 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 34392 |
| 2 | 🇮🇳 IN | 3299 |
| 3 | 🇪🇸 ES | 3234 |
| 4 | 🇦🇺 AU | 3034 |
| 5 | 🇧🇷 BR | 2610 |
| 6 | 🇯🇵 JP | 2411 |
| 7 | 🇮🇹 IT | 2314 |
| 8 | 🇩🇪 DE | 2230 |
| 9 | 🇨🇦 CA | 2126 |
| 10 | 🇨🇴 CO | 2017 |
| 11 | 🇬🇧 GB | 1775 |
| 12 | 🇫🇷 FR | 1676 |
| 13 | 🇲🇽 MX | 1358 |
| 14 | 🇬🇷 GR | 1352 |
| 15 | 🇨🇭 CH | 1201 |
| 16 | 🇲🇾 MY | 1090 |
| 17 | 🇳🇴 NO | 1086 |
| 18 | 🇿🇦 ZA | 917 |
| 19 | 🇳🇿 NZ | 875 |
| 20 | 🇵🇭 PH | 792 |
| 21 | 🇹🇭 TH | 780 |
| 22 | 🇹🇷 TR | 773 |
| 23 | 🇰🇷 KR | 728 |
| 24 | 🇬🇹 GT | 716 |
| 25 | 🇵🇱 PL | 698 |
| 26 | 🇲🇦 MA | 544 |
| 27 | 🇲🇪 ME | 460 |
| 28 | 🇳🇱 NL | 449 |
| 29 | 🇧🇸 BS | 406 |
| 30 | 🇮🇩 ID | 400 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1013 |
| 2 | Tokyo International Airport |  | JP | 825 |
| 3 | Denver International Airport |  | US | 717 |
| 4 | Indira Gandhi International Airport |  | IN | 710 |
| 5 | El Dorado International Airport |  | CO | 705 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 673 |
| 7 | Harry Reid International Airport |  | US | 554 |
| 8 | Guaymaral Airport |  | CO | 549 |
| 9 | La Aurora Airport |  | GT | 529 |
| 10 | Zurich Airport |  | CH | 525 |
| 11 | Kuala Lumpur International Airport |  | MY | 432 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 428 |
| 13 | Chicago O'Hare International Airport |  | US | 428 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 423 |
| 15 | Frankfurt am Main International Airport |  | DE | 411 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 17 | Macau International Airport |  | MO | 399 |
| 18 | Bengaluru International Airport |  | IN | 392 |
| 19 | Madrid Barajas International Airport |  | ES | 390 |
| 20 | Tenerife Norte Airport |  | ES | 388 |
| 21 | Charlotte/Douglas International Airport |  | US | 377 |
| 22 | Congonhas Airport |  | BR | 375 |
| 23 | Ninoy Aquino International Airport |  | PH | 367 |
| 24 | Malpensa International Airport |  | IT | 361 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 333 |
| 26 | Salt Lake City International Airport |  | US | 331 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 328 |
| 28 | Charles de Gaulle International Airport |  | FR | 324 |
| 29 | Daniel K Inouye International Airport |  | US | 322 |
| 30 | Vitoria/Foronda Airport |  | ES | 305 |
| 31 | Reno/Tahoe International Airport |  | US | 304 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 303 |
| 33 | Capua Airport |  | IT | 300 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 296 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 296 |
| 36 | O. R. Tambo International Airport |  | ZA | 294 |
| 37 | Barcelona International Airport |  | ES | 282 |
| 38 | Viracopos International Airport |  | BR | 267 |
| 39 | Don Mueang International Airport |  | TH | 265 |
| 40 | Calgary International Airport |  | CA | 261 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 221 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 165 | 14m | 114 km | 323.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 132 | 28m | 304 km | 692.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 128 | 1h 27m | 910 km | 2,008.6 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 120 | 21m | 244 km | 505.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 118 | 19m | 165 km | 335.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 117 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 107 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 101 | 26m | 275 km | 478.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 89 | 21m | 99 km | 152.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 77 | 31m | 369 km | 490.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 72 | 20m | 147 km | 182.2 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 71 | 52m | 556 km | 680.6 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 68 | 26m | 215 km | 251.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 62 | 13m | 99 km | 106.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 61 | 57m | 493 km | 519.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 61 | 1h 52m | 1,304 km | 1,372.3 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 60 | 1h 21m | 961 km | 994.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9372H |  | North Perry Airport (KHWO) | Immokalee Regional Airport (KIMM) | 2026-04-19 17:34 UTC | 2026-04-19 18:28 UTC | 53m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-19 18:06 UTC | 2026-04-19 18:18 UTC | 12m |
| AFL1870 | AFL | Sheremetyevo International Airport (UUEE) | Bezymyanka Airfield (UWWG) | 2026-04-19 17:11 UTC | 2026-04-19 18:06 UTC | 54m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-04-19 17:44 UTC | 2026-04-19 17:59 UTC | 15m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-19 17:46 UTC | 2026-04-19 17:59 UTC | 13m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-04-19 17:42 UTC | 2026-04-19 17:59 UTC | 17m |
| EJA538 | EJA | Kansas City Downtown/Wheeler Field (KMKC) | Las Cruces International Airport (KLRU) | 2026-04-19 15:42 UTC | 2026-04-19 17:55 UTC | 2h 12m |
| N386TA |  | Birmingham-Shuttlesworth International Airport (KBHM) | WV23 (WV23) | 2026-04-19 16:51 UTC | 2026-04-19 17:52 UTC | 1h 1m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-19 17:32 UTC | 2026-04-19 17:52 UTC | 20m |
| LOST96 | LOS | Los Alamitos Army Air Field (KSLI) | Grassy Meadows/Sky Ranch Landowners Assn Airport (UT47) | 2026-04-19 16:36 UTC | 2026-04-19 17:50 UTC | 1h 14m |
| EJA945 | EJA | Sky Ranch Airport (TN98) | Kee Field (KI16) | 2026-04-19 17:14 UTC | 2026-04-19 17:49 UTC | 34m |
| N390HG |  | Orlando International Airport (KMCO) | Virgil I Grissom Municipal Airport (KBFR) | 2026-04-19 15:57 UTC | 2026-04-19 17:49 UTC | 1h 51m |
| CRN911 | CRN | Kelowna Airport (CYLW) | Castlegar Airport (CYCG) | 2026-04-19 17:31 UTC | 2026-04-19 17:48 UTC | 17m |
| N801FL |  | Baldwin Airport (WI14) | Baldwin Airport (WI14) | 2026-04-19 17:35 UTC | 2026-04-19 17:48 UTC | 13m |
| N24144 |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-04-19 17:24 UTC | 2026-04-19 17:48 UTC | 24m |
| N387A |  | KF29 (KF29) | Memorial Field (KHOT) | 2026-04-19 17:10 UTC | 2026-04-19 17:47 UTC | 36m |
| N667DB |  | 52OR (52OR) | Albany Municipal Airport (KS12) | 2026-04-19 17:17 UTC | 2026-04-19 17:46 UTC | 29m |
| N3189Z |  | Caldwell Executive Airport (KEUL) | Caldwell Executive Airport (KEUL) | 2026-04-19 17:31 UTC | 2026-04-19 17:45 UTC | 14m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-19 17:31 UTC | 2026-04-19 17:45 UTC | 13m |
| N827DP |  | Reading Regional/Carl A Spaatz Field (KRDG) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-04-19 14:41 UTC | 2026-04-19 17:38 UTC | 2h 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
